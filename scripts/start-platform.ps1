$ErrorActionPreference='Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
try { docker info | Out-Null } catch { throw "Docker engine is not running. Start Docker Desktop and retry." }
docker compose up -d --build
if ($LASTEXITCODE -ne 0) { throw "Docker Compose failed." }
Write-Host "Waiting for API health on host port 18080..."
$ready=$false
for($i=0;$i -lt 30;$i++){try{$h=Invoke-RestMethod http://127.0.0.1:18080/health -TimeoutSec 2;if($h.status -eq 'ok'){$ready=$true;break}}catch{};Start-Sleep 2}
if(-not $ready){docker compose ps;throw "API did not become healthy. Inspect docker compose logs api."}
Write-Host "Ready: API :18080 | Prometheus :9090 | Grafana :3000"
