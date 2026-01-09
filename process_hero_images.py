#!/usr/bin/env python3
"""
Hero Image Processor for Rhythm Warriors
Automatically processes character images: removes backgrounds, resizes, and places in correct folders
"""

import os
from PIL import Image
import sys

# Define the skin mappings (which image goes to which skin)
SKIN_MAPPINGS = {
    # Format: "source_filename": ("heroId", "skinId", "description")

    # Rhythm Knight (default) - Row 1
    "neon_knight.png": ("default", "neonVanguard", "Neon/Cyan armored knight"),
    "golden_knight.png": ("default", "goldenMaestro", "Golden armored knight"),

    # Shadow Dancer (shadow) - Row 1 & 2
    "purple_shadow.png": ("shadow", "eclipsePhantom", "Purple shadowy figure"),
    "void_assassin.png": ("shadow", "voidAssassin", "Dark shadow with cloak"),

    # Iron Guardian (tank) - Row 2
    "ice_warrior.png": ("tank", "crystalSentinel", "Ice/frost warrior"),
    "runic_golem.png": ("tank", "runicFortress", "Stone golem with runes"),
    "fire_golem.png": ("tank", "moltenBulwark", "Fire/lava warrior"),

    # Berserker (berserker) - Row 3
    "cyber_warrior.png": ("berserker", "hellfireRavager", "Cyberpunk warrior"),
    "frost_warrior.png": ("berserker", "frostbiteFury", "Ice crystal warrior"),

    # Ancient Sage (ancient) - Row 3 & 4
    "astral_mage.png": ("ancient", "astralArchivist", "Cosmic/starry figure with book"),
    "time_mage.png": ("ancient", "temporalScribe", "Clockwork/steampunk mage"),
    "king_sage.png": ("ancient", "celestialOracle", "Golden king with orbs"),
    "white_sage.png": ("ancient", "default", "White-haired sage with staff"),
}

def remove_background(image_path, output_path, target_size=(256, 256)):
    """
    Remove background from image and resize it
    """
    try:
        # Try to import rembg for background removal
        try:
            from rembg import remove
            use_rembg = True
            print(f"  Using rembg for background removal...")
        except ImportError:
            use_rembg = False
            print(f"  rembg not available, will convert to RGBA...")

        # Open image
        img = Image.open(image_path)

        # Remove background if rembg is available
        if use_rembg:
            img_no_bg = remove(img)
        else:
            # Convert to RGBA
            img_no_bg = img.convert("RGBA")

            # Simple background removal: make white/near-white pixels transparent
            datas = img_no_bg.getdata()
            new_data = []
            for item in datas:
                # Change all white (or near-white) to transparent
                if item[0] > 240 and item[1] > 240 and item[2] > 240:
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)
            img_no_bg.putdata(new_data)

        # Resize to target size
        img_resized = img_no_bg.resize(target_size, Image.Resampling.LANCZOS)

        # Save as PNG
        img_resized.save(output_path, "PNG")
        print(f"  ✓ Saved: {output_path}")
        return True

    except Exception as e:
        print(f"  ✗ Error processing {image_path}: {e}")
        return False

def setup_directories():
    """Create all necessary asset directories"""
    base = "assets/heroes"
    heroes = ["default", "shadow", "tank", "berserker", "ancient"]

    for hero in heroes:
        os.makedirs(f"{base}/{hero}/default", exist_ok=True)
        os.makedirs(f"{base}/{hero}/skins", exist_ok=True)

    print("✓ Directory structure created")

def process_images(source_dir="hero_images"):
    """
    Process all images in source directory
    """
    if not os.path.exists(source_dir):
        print(f"Creating {source_dir}/ directory...")
        os.makedirs(source_dir)
        print(f"\n⚠️  Please place your character images in the '{source_dir}/' folder")
        print("   You can name them descriptively (e.g., neon_knight.png, golden_knight.png)")
        print("   Then run this script again.")
        return

    # Get all image files
    image_files = [f for f in os.listdir(source_dir)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    if not image_files:
        print(f"⚠️  No images found in {source_dir}/")
        print("   Please add your character images and run again.")
        return

    print(f"\n📦 Found {len(image_files)} images to process\n")

    setup_directories()

    processed = 0
    for img_file in image_files:
        source_path = os.path.join(source_dir, img_file)

        # Check if we have a mapping for this file
        if img_file in SKIN_MAPPINGS:
            hero_id, skin_id, description = SKIN_MAPPINGS[img_file]

            # Determine output folder
            folder = "default" if skin_id == "default" else "skins"
            output_filename = f"{hero_id}_{skin_id}.png"
            output_path = f"assets/heroes/{hero_id}/{folder}/{output_filename}"

            print(f"Processing: {img_file}")
            print(f"  → {description}")
            print(f"  → {output_path}")

            if remove_background(source_path, output_path):
                processed += 1
        else:
            print(f"⚠️  Skipping {img_file} (no mapping defined)")
            print(f"   Add to SKIN_MAPPINGS in the script to process this image")

    print(f"\n✅ Processed {processed} images successfully!")
    print(f"\nImages are ready in assets/heroes/ folders")
    print(f"Refresh your game to see them!")

def interactive_mode():
    """
    Interactive mode to manually map images to skins
    """
    print("\n🎮 Interactive Hero Image Mapper")
    print("=" * 50)

    source_dir = "hero_images"
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
        print(f"\nPlease place your character images in '{source_dir}/'")
        return

    image_files = [f for f in os.listdir(source_dir)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    if not image_files:
        print(f"\nNo images found in {source_dir}/")
        return

    setup_directories()

    heroes = {
        "1": ("default", "Rhythm Knight"),
        "2": ("shadow", "Shadow Dancer"),
        "3": ("tank", "Iron Guardian"),
        "4": ("berserker", "Berserker"),
        "5": ("ancient", "Ancient Sage")
    }

    skins_by_hero = {
        "default": ["default", "neonVanguard", "goldenMaestro", "festivalChampion"],
        "shadow": ["default", "voidAssassin", "cyberNinja", "eclipsePhantom"],
        "tank": ["default", "runicFortress", "moltenBulwark", "crystalSentinel"],
        "berserker": ["default", "bloodDrummer", "hellfireRavager", "frostbiteFury"],
        "ancient": ["default", "astralArchivist", "celestialOracle", "temporalScribe"]
    }

    print(f"\nFound {len(image_files)} images")

    for img_file in image_files:
        print(f"\n📸 Image: {img_file}")
        print("\nSelect hero:")
        for key, (hero_id, hero_name) in heroes.items():
            print(f"  {key}. {hero_name}")

        hero_choice = input("Hero number (or 's' to skip): ").strip()
        if hero_choice.lower() == 's':
            continue

        if hero_choice not in heroes:
            print("Invalid choice, skipping...")
            continue

        hero_id, hero_name = heroes[hero_choice]

        print(f"\nSelect skin for {hero_name}:")
        for i, skin_id in enumerate(skins_by_hero[hero_id], 1):
            print(f"  {i}. {skin_id}")

        skin_choice = input("Skin number: ").strip()
        try:
            skin_idx = int(skin_choice) - 1
            skin_id = skins_by_hero[hero_id][skin_idx]
        except:
            print("Invalid choice, skipping...")
            continue

        # Process the image
        source_path = os.path.join(source_dir, img_file)
        folder = "default" if skin_id == "default" else "skins"
        output_filename = f"{hero_id}_{skin_id}.png"
        output_path = f"assets/heroes/{hero_id}/{folder}/{output_filename}"

        print(f"\nProcessing: {img_file} → {output_path}")
        remove_background(source_path, output_path)

    print("\n✅ Done! Refresh your game to see the images.")

def main():
    print("🎨 Rhythm Warriors - Hero Image Processor")
    print("=" * 50)

    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        print("\nThis script will:")
        print("  1. Remove backgrounds from your character images")
        print("  2. Resize them to 256x256 pixels")
        print("  3. Place them in the correct asset folders")
        print("  4. Name them correctly for the game")
        print("\nModes:")
        print("  • Auto mode: python3 process_hero_images.py")
        print("  • Interactive mode: python3 process_hero_images.py --interactive")
        print("\nStarting auto mode...\n")
        process_images()

if __name__ == "__main__":
    main()
