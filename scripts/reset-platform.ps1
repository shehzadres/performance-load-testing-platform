param([switch]$ConfirmDataLoss)
if(-not $ConfirmDataLoss){throw "This deletes Prometheus and Grafana volumes. Pass -ConfirmDataLoss to confirm."}
Set-Location (Split-Path $PSScriptRoot -Parent)
docker compose down -v
