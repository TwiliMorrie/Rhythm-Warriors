#!/bin/bash
# Quick setup script for asset folders

echo "🎮 Setting up Rhythm Warriors asset folders..."

# Create all necessary directories
mkdir -p assets/heroes/default/default
mkdir -p assets/heroes/default/skins
mkdir -p assets/heroes/shadow/default
mkdir -p assets/heroes/shadow/skins
mkdir -p assets/heroes/tank/default
mkdir -p assets/heroes/tank/skins
mkdir -p assets/heroes/berserker/default
mkdir -p assets/heroes/berserker/skins
mkdir -p assets/heroes/ancient/default
mkdir -p assets/heroes/ancient/skins

echo "✅ Asset folders created!"
echo ""
echo "📁 Folder structure:"
tree assets/ 2>/dev/null || ls -R assets/

echo ""
echo "📝 Next steps:"
echo "  1. Place your character images in assets/heroes/{heroId}/skins/"
echo "  2. Name them as {heroId}_{skinId}.png"
echo "  3. Example: assets/heroes/default/skins/default_neonVanguard.png"
echo ""
echo "Need help? Read MANUAL_IMAGE_SETUP.md or run process_hero_images.py"
