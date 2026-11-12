param([ValidateRange(1,500)][int]$Users=10,[ValidateRange(1,300)][int]$RampUp=10,[ValidateRange(10,1800)][int]$Duration=60,[ValidatePattern('^[a-zA-Z0-9._-]+$')][string]$Label='manual')
$ErrorActionPreference='Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
try{docker info|Out-Null}catch{throw "Docker engine is not running."}
$runId="$(Get-Date -Format 'yyyyMMdd-HHmmss')-$Label"
New-Item -ItemType Directory -Force results,reports|Out-Null
Write-Host "Run $runId | users=$Users | ramp=$RampUp sec | duration=$Duration sec"
docker compose --profile load run --rm -T jmeter -n -t /work/jmeter/performance-test.jmx "-Jusers=$Users" "-Jramp=$RampUp" "-Jduration=$Duration" -Jjmeter.save.saveservice.output_format=csv -Jjmeter.save.saveservice.print_field_names=true -l "/work/results/$runId.jtl"
if($LASTEXITCODE -ne 0){throw "JMeter failed with exit code $LASTEXITCODE"}
python .\analysis\analyze.py --input ".\results\$runId.jtl" --run-id "$runId"
if($LASTEXITCODE -ne 0){throw "Analysis failed"}
Write-Host "Saved results/$runId.jtl and reports/$runId.md"
