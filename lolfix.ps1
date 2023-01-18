# Quick one-liner to wipe out the lag causing LoL Logs directory:
Get-ChildItem 'C:\Riot Games\League of Legends\Logs\' | Remove-Item -Recurse
