# Requirements: chocolatey

choco upgrade all -y

choco install 7zip googlechrome vlc jre8 vscode spotify steam discord -y
choco install reaper reapack reaper-sws-extension -y

$response = Read-Host "Install extra software? [y/n]: "
if ( $response -eq "y" ) 
{
    choco install obs-studio pia qbittorrent -y
}

echo "Done. Restart Windows."
