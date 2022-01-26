# Requirements: chocolatey

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
