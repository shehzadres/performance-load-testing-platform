param([Parameter(Mandatory=$true)][string]$Baseline,[Parameter(Mandatory=$true)][string]$Candidate)
Set-Location (Split-Path $PSScriptRoot -Parent)
python .\analysis\compare.py --baseline ".\results\$Baseline.json" --candidate ".\results\$Candidate.json"
if($LASTEXITCODE -ne 0){throw "Comparison failed. Check run summary files."}
