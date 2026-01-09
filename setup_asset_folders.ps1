# Rhythm Warriors - Asset Folder Setup Script for Windows PowerShell
# Run this script to create all necessary asset directories

Write-Host "🎮 Setting up Rhythm Warriors asset folders..." -ForegroundColor Cyan

# Create all necessary directories
$folders = @(
    "assets\heroes\default\default",
    "assets\heroes\default\skins",
    "assets\heroes\shadow\default",
    "assets\heroes\shadow\skins",
    "assets\heroes\tank\default",
    "assets\heroes\tank\skins",
    "assets\heroes\berserker\default",
    "assets\heroes\berserker\skins",
    "assets\heroes\ancient\default",
    "assets\heroes\ancient\skins"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

Write-Host "✅ Asset folders created!" -ForegroundColor Green
Write-Host ""
Write-Host "📁 Folder structure:" -ForegroundColor Yellow

# Display folder structure
Get-ChildItem -Path "assets" -Recurse -Directory | ForEach-Object {
    $depth = ($_.FullName.Substring($PWD.Path.Length) -split '\\').Count - 1
    $indent = "  " * $depth
    Write-Host "$indent📂 $($_.Name)"
}

Write-Host ""
Write-Host "📝 Next steps:" -ForegroundColor Yellow
Write-Host "  1. Place your character images in assets\heroes\{heroId}\skins\"
Write-Host "  2. Name them as {heroId}_{skinId}.png"
Write-Host "  3. Example: assets\heroes\default\skins\default_neonVanguard.png"
Write-Host ""
Write-Host "Need help? Read MANUAL_IMAGE_SETUP.md or run:" -ForegroundColor Cyan
Write-Host "  python process_hero_images.py" -ForegroundColor White
Write-Host ""

# Optional: Open the assets folder in File Explorer
$openExplorer = Read-Host "Open assets folder in File Explorer? (y/n)"
if ($openExplorer -eq 'y') {
    Start-Process explorer.exe -ArgumentList (Join-Path $PWD "assets\heroes")
}
