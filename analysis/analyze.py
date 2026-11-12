import argparse
import csv
import json
import math
import statistics
from datetime import datetime, timezone
from pathlib import Path

TRANSACTION_PREFIX = "Transaction:"


def pct(values, percentile):
    ordered = sorted(values)
    if not ordered:
        return 0.0
    position = (len(ordered) - 1) * percentile
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(ordered[lower])
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def response_summary(values):
    return {
        "min": min(values),
        "mean": round(statistics.mean(values), 2),
        "median": round(pct(values, 0.5), 2),
        "p90": round(pct(values, 0.9), 2),
        "p95": round(pct(values, 0.95), 2),
        "p99": round(pct(values, 0.99), 2),
        "max": max(values),
    }


def load_samples(path):
    samples = []
    with path.open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        required = {"timeStamp", "elapsed", "success"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise SystemExit("Expected JMeter CSV JTL with timeStamp, elapsed and success columns.")
        for row in reader:
            try:
                samples.append({
                    "ts": int(row["timeStamp"]),
                    "ms": max(0, int(row["elapsed"])),
                    "ok": row["success"].lower() == "true",
                    "label": row.get("label", "unknown"),
                })
            except (ValueError, TypeError, AttributeError):
                continue
    return samples


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--environment", default="local")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        raise SystemExit(f"JTL not found: {path}")

    all_samples = load_samples(path)
    if not all_samples:
        raise SystemExit("No valid samples found.")

    transactions = [sample for sample in all_samples if sample["label"].startswith(TRANSACTION_PREFIX)]
    requests = [sample for sample in all_samples if not sample["label"].startswith(TRANSACTION_PREFIX)]
    if not requests:
        raise SystemExit("No request samples found after excluding transaction-controller rows.")

    request_times = [sample["ms"] for sample in requests]
    successful = sum(sample["ok"] for sample in requests)
    failed = len(requests) - successful
    wall = max(
        (max(sample["ts"] + sample["ms"] for sample in all_samples)
         - min(sample["ts"] for sample in all_samples)) / 1000,
        0.001,
    )

    by_sampler = {}
    for label in sorted({sample["label"] for sample in requests}):
        group = [sample for sample in requests if sample["label"] == label]
        values = [sample["ms"] for sample in group]
        by_sampler[label] = {
            "samples": len(group),
            "errors": sum(not sample["ok"] for sample in group),
            "mean_ms": round(statistics.mean(values), 2),
            "p95_ms": round(pct(values, 0.95), 2),
        }

    summary = {
        "run_id": args.run_id,
        "environment": args.environment,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_jtl_samples": len(all_samples),
        "sample_count": len(requests),
        "transaction_count": len(transactions),
        "successful_samples": successful,
        "failed_samples": failed,
        "error_rate_pct": round(failed / len(requests) * 100, 3),
        "duration_seconds": round(wall, 3),
        "throughput_rps": round(len(requests) / wall, 3),
        "response_time_ms": response_summary(request_times),
        "transaction_response_time_ms": response_summary([s["ms"] for s in transactions]) if transactions else None,
        "by_sampler": by_sampler,
    }

    Path("results").mkdir(exist_ok=True)
    Path("reports").mkdir(exist_ok=True)
    Path("results", f"{args.run_id}.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    Path("showcase/data").mkdir(parents=True, exist_ok=True)
    Path("showcase/data/latest.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [
        f"# Performance Test Report: {args.run_id}",
        "",
        f"- Environment: {args.environment}",
        f"- Generated: {summary['generated_at']}",
        f"- Request samples: {summary['sample_count']}",
        f"- Transaction samples: {summary['transaction_count']}",
        f"- Successful requests: {successful}",
        f"- Failed requests: {failed}",
        f"- Request error rate: {summary['error_rate_pct']}%",
        f"- Request throughput: {summary['throughput_rps']} req/s",
        f"- Wall time: {summary['duration_seconds']} sec",
        "",
        "## Request response time (ms)",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    lines += [f"| {key} | {value} |" for key, value in summary["response_time_ms"].items()]

    if summary["transaction_response_time_ms"] is not None:
        lines += ["", "## Transaction response time (ms)", "", "| Metric | Value |", "|---|---:|"]
        lines += [f"| {key} | {value} |" for key, value in summary["transaction_response_time_ms"].items()]

    lines += [
        "",
        "## Request sampler breakdown",
        "",
        "| Sampler | Samples | Errors | Mean ms | p95 ms |",
        "|---|---:|---:|---:|---:|",
    ]
    lines += [
        f"| {label} | {values['samples']} | {values['errors']} | {values['mean_ms']} | {values['p95_ms']} |"
        for label, values in summary["by_sampler"].items()
    ]
    lines += [
        "",
        "## Investigation notes",
        "- Transaction Controller rows are reported separately and excluded from request throughput to avoid double-counting.",
        "- Correlate slow samplers with Grafana route latency and process metrics.",
        "- Verify the JMeter generator and Docker host are not saturated.",
        "- Treat these results as valid only for the recorded workload and environment.",
        "",
    ]

    Path("reports", f"{args.run_id}.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({
        key: summary[key]
        for key in ("run_id", "sample_count", "transaction_count", "error_rate_pct", "throughput_rps", "response_time_ms")
    }, indent=2))


if __name__ == "__main__":
    main()
