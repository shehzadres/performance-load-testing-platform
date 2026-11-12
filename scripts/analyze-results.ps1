param([string]$RunId='')
Set-Location (Split-Path $PSScriptRoot -Parent)
if($RunId){python .\analysis\analyze.py --input ".\results\$RunId.jtl" --run-id "$RunId"}
else{$f=Get-ChildItem .\results\*.jtl -ErrorAction SilentlyContinue|Sort-Object LastWriteTime -Descending|Select-Object -First 1;if(-not $f){throw "No JTL files found"};$id=[IO.Path]::GetFileNameWithoutExtension($f.Name);python .\analysis\analyze.py --input $f.FullName --run-id $id}
