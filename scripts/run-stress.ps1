param([ValidateRange(1,500)][int]$Users=50,[ValidateRange(10,1800)][int]$Duration=90)
& "$PSScriptRoot\run-test.ps1" -Users $Users -RampUp 20 -Duration $Duration -Label stress
