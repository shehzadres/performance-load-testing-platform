import argparse,json
from datetime import datetime,timezone
from pathlib import Path

def read(p):
    p=Path(p)
    if not p.exists():raise SystemExit(f'Summary missing: {p}')
    return json.loads(p.read_text(encoding='utf-8'))
def change(new,old):return None if old==0 else round((new-old)/old*100,2)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--baseline',required=True);ap.add_argument('--candidate',required=True);a=ap.parse_args()
    b,c=read(a.baseline),read(a.candidate)
    metrics=[('Throughput (req/s)',b['throughput_rps'],c['throughput_rps'],'higher'),('Mean response time (ms)',b['response_time_ms']['mean'],c['response_time_ms']['mean'],'lower'),('p95 response time (ms)',b['response_time_ms']['p95'],c['response_time_ms']['p95'],'lower'),('p99 response time (ms)',b['response_time_ms']['p99'],c['response_time_ms']['p99'],'lower'),('Error rate (%)',b['error_rate_pct'],c['error_rate_pct'],'lower')]
    rows=[]
    for name,old,new,prefer in metrics:
        d=change(new,old);v='N/A' if d is None else ('Within 5%' if abs(d)<5 else ('Improved' if (d>0 and prefer=='higher') or (d<0 and prefer=='lower') else 'Regressed'))
        rows.append((name,old,new,d,v))
    lines=['# Release Performance Comparison','',f"- Generated: {datetime.now(timezone.utc).isoformat()}",f"- Baseline: {b['run_id']}",f"- Candidate: {c['run_id']}","","| Metric | Baseline | Candidate | Change | Assessment |","|---|---:|---:|---:|---|"]
    lines += [f"| {n} | {o} | {v} | {'N/A' if d is None else f'{d:+.2f}%'} | {verdict} |" for n,o,v,d,verdict in rows]
    lines += ["","## Summary",f"- Regressions detected: {sum(x[4]=='Regressed' for x in rows)}","- Positive latency/error-rate change is a regression; positive throughput change is generally an improvement.","- Workload, test data, host resources and duration must be controlled for a fair comparison.",""]
    out=Path(f"reports/comparison-{b['run_id']}-vs-{c['run_id']}.md");out.parent.mkdir(exist_ok=True);out.write_text('\n'.join(lines),encoding='utf-8');print('\n'.join(lines));print(f'Saved: {out}')
if __name__=='__main__':main()
