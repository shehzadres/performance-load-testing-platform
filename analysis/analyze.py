import argparse,csv,json,math,statistics
from datetime import datetime,timezone
from pathlib import Path

def pct(a,p):
    a=sorted(a)
    if not a:return 0.0
    x=(len(a)-1)*p;lo=math.floor(x);hi=math.ceil(x)
    return float(a[lo]) if lo==hi else a[lo]+(a[hi]-a[lo])*(x-lo)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--run-id',required=True);ap.add_argument('--environment',default='local');args=ap.parse_args()
    path=Path(args.input)
    if not path.exists():raise SystemExit(f'JTL not found: {path}')
    samples=[]
    with path.open(newline='',encoding='utf-8-sig') as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames or not {'timeStamp','elapsed','success'}.issubset(reader.fieldnames):raise SystemExit('Expected JMeter CSV JTL with timeStamp, elapsed, success columns.')
        for row in reader:
            try:samples.append({'ts':int(row['timeStamp']),'ms':max(0,int(row['elapsed'])),'ok':row['success'].lower()=='true','label':row.get('label','unknown')})
            except (ValueError,TypeError,AttributeError):pass
    if not samples:raise SystemExit('No valid samples found.')
    times=[s['ms'] for s in samples];ok=sum(s['ok'] for s in samples);wall=max((max(s['ts']+s['ms'] for s in samples)-min(s['ts'] for s in samples))/1000,.001)
    summary={'run_id':args.run_id,'environment':args.environment,'generated_at':datetime.now(timezone.utc).isoformat(),'sample_count':len(samples),'successful_samples':ok,'failed_samples':len(samples)-ok,'error_rate_pct':round((len(samples)-ok)/len(samples)*100,3),'duration_seconds':round(wall,3),'throughput_rps':round(len(samples)/wall,3),'response_time_ms':{'min':min(times),'mean':round(statistics.mean(times),2),'median':round(pct(times,.5),2),'p90':round(pct(times,.9),2),'p95':round(pct(times,.95),2),'p99':round(pct(times,.99),2),'max':max(times)},'by_sampler':{}}
    for label in sorted({s['label'] for s in samples}):
        group=[s for s in samples if s['label']==label];v=[s['ms'] for s in group]
        summary['by_sampler'][label]={'samples':len(group),'errors':sum(not s['ok'] for s in group),'mean_ms':round(statistics.mean(v),2),'p95_ms':round(pct(v,.95),2)}
    Path('results').mkdir(exist_ok=True);Path('reports').mkdir(exist_ok=True)
    Path(f'results/{args.run_id}.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    Path('showcase/data').mkdir(parents=True,exist_ok=True)
    Path('showcase/data/latest.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    lines=[f"# Performance Test Report: {args.run_id}","",f"- Generated: {summary['generated_at']}",f"- Samples: {len(samples)}",f"- Successful: {ok}",f"- Failed: {len(samples)-ok}",f"- Error rate: {summary['error_rate_pct']}%",f"- Throughput: {summary['throughput_rps']} req/s",f"- Wall time: {summary['duration_seconds']} sec","","## Response time (ms)","","| Metric | Value |","|---|---:|"]
    lines += [f"| {k} | {v} |" for k,v in summary['response_time_ms'].items()]
    lines += ["","## Sampler breakdown","","| Sampler | Samples | Errors | Mean ms | p95 ms |","|---|---:|---:|---:|---:|"]
    lines += [f"| {k} | {v['samples']} | {v['errors']} | {v['mean_ms']} | {v['p95_ms']} |" for k,v in summary['by_sampler'].items()]
    lines += ["","## Investigation notes","- Correlate slow samplers with Grafana route latency and process metrics.","- Verify JMeter generator and Docker host are not saturated.","- Treat these results as valid only for the recorded workload and environment.",""]
    Path(f'reports/{args.run_id}.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({k:summary[k] for k in ('run_id','sample_count','error_rate_pct','throughput_rps','response_time_ms')},indent=2))
if __name__=='__main__':main()
