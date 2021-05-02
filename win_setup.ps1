# Personal Windows setup script
# MUSE BE RUN AS ADMINISTRATOR
# CHOCOLATEY MUST BE INSTALLED

powercfg.exe /h off
choco upgrade all -y

# Essential Software
choco install 7zip googlechrome vlc jre8 vscode spotify steam reaper discord -y

# Extras
$response = Read-Host "Install extra software? [y/n]: "
if ( $response -eq "y" ) 
{
    choco install obs pia qbittorrent -y
}

echo "Done. Restart Windows."
