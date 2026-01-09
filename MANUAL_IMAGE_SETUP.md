# Manual Image Setup Guide

Since I cannot directly manipulate images, here's how to add your character artwork yourself:

## Option 1: Automated Python Script (Recommended)

### Step 1: Install Requirements

**Windows PowerShell:**
```powershell
# Install Python PIL/Pillow
pip install Pillow

# Optional: Install rembg for better background removal
pip install rembg
```

**Mac/Linux:**
```bash
pip install Pillow
pip install rembg
```

### Step 2: Prepare Your Images
1. Save the character image grid you shared
2. Split it into individual character images (use any image editor)
3. Create a folder called `hero_images` in the Rhythm-Warriors directory
4. Place all individual character images there

### Step 3: Run the Script

**Windows PowerShell:**
```powershell
cd Rhythm-Warriors
python process_hero_images.py
```

**Mac/Linux:**
```bash
cd Rhythm-Warriors
python3 process_hero_images.py
```

The script will:
- Remove backgrounds automatically
- Resize to 256x256
- Place in correct folders
- Name correctly

### Interactive Mode

**Windows PowerShell:**
```powershell
python process_hero_images.py --interactive
```

**Mac/Linux:**
```bash
python3 process_hero_images.py --interactive
```

---

## Option 2: Manual Process

### Tools You'll Need:
- Image editor (Photoshop, GIMP, Photopea, remove.bg)
- File manager

### Step-by-Step Instructions:

#### 1. Extract Individual Characters
From your image grid, save each character as a separate file:
- Top-left (neon/cyan knight) → `neon_knight.png`
- Top-middle (golden knight) → `golden_knight.png`
- Top-right (purple shadow) → `purple_shadow.png`
- etc.

#### 2. Remove Backgrounds
For each image:

**Using remove.bg (easiest):**
1. Go to https://www.remove.bg
2. Upload image
3. Download the transparent PNG

**Using GIMP (free):**
1. Open image
2. Layer → Transparency → Add Alpha Channel
3. Select → By Color
4. Click background
5. Press Delete
6. Export as PNG

**Using Photopea (online, free):**
1. Go to https://www.photopea.com
2. Open image
3. Magic Wand tool → Click background
4. Press Delete
5. File → Export As → PNG

#### 3. Resize Images
Resize each to **256x256 pixels** (or 128x128, 512x512)
- Maintain aspect ratio
- Use high-quality resampling

#### 4. Name and Place Files

**Folder Structure:**
```
Rhythm-Warriors/
└── assets/
    └── heroes/
        ├── default/
        │   ├── default/
        │   │   └── default_default.png
        │   └── skins/
        │       ├── default_neonVanguard.png
        │       ├── default_goldenMaestro.png
        │       └── default_festivalChampion.png
        ├── shadow/
        │   ├── default/
        │   │   └── shadow_default.png
        │   └── skins/
        │       ├── shadow_voidAssassin.png
        │       ├── shadow_cyberNinja.png
        │       └── shadow_eclipsePhantom.png
        ├── tank/
        │   ├── default/
        │   │   └── tank_default.png
        │   └── skins/
        │       ├── tank_runicFortress.png
        │       ├── tank_moltenBulwark.png
        │       └── tank_crystalSentinel.png
        ├── berserker/
        │   ├── default/
        │   │   └── berserker_default.png
        │   └── skins/
        │       ├── berserker_bloodDrummer.png
        │       ├── berserker_hellfireRavager.png
        │       └── berserker_frostbiteFury.png
        └── ancient/
            ├── default/
            │   └── ancient_default.png
            └── skins/
                ├── ancient_astralArchivist.png
                ├── ancient_celestialOracle.png
                └── ancient_temporalScribe.png
```

#### 5. Image-to-Skin Mapping

Based on your image grid, here's what I recommend:

**Row 1 (Top):**
- Left (Neon/Cyan knight) → `default_neonVanguard.png`
- Middle (Golden knight) → `default_goldenMaestro.png`
- Right (Purple shadow) → `shadow_eclipsePhantom.png`

**Row 2:**
- Left (Ice/frost warrior) → `berserker_frostbiteFury.png` or `tank_crystalSentinel.png`
- Middle (Runic golem) → `tank_runicFortress.png`
- Right (Fire golem) → `tank_moltenBulwark.png`

**Row 3:**
- Left (Cosmic/stars figure) → `ancient_astralArchivist.png`
- Middle (Cyberpunk warrior) → `shadow_cyberNinja.png` or `berserker_hellfireRavager.png`
- Right (Ice crystal warrior) → `berserker_frostbiteFury.png`

**Row 4:**
- Left (Steampunk/clockwork) → `ancient_temporalScribe.png`
- Middle (Golden king) → `ancient_celestialOracle.png`
- Right (White sage) → `ancient_default.png`

#### 6. Test in Game
1. Open `rhythm-warriors-combined.html` in a browser
2. Press F12 to open Console
3. Look for image loading messages
4. Check for any errors
5. Go to Skins menu to verify

---

## Option 3: Quick Test (No Background Removal)

To quickly test if the system works:

1. Save just ONE character image
2. Rename it to `default_neonVanguard.png`
3. Place in folder:
   - **Windows:** `assets\heroes\default\skins\`
   - **Mac/Linux:** `assets/heroes/default/skins/`
4. Refresh game in browser
5. Go to Skins menu → Equip Neon Vanguard skin
6. Start a game

You should see your image (even with background)!

---

## Troubleshooting

### Images Not Showing
**Check:**
- File path is correct
- File name matches exactly (case-sensitive!)
- PNG format
- Open browser console (F12) for errors

### Background Not Transparent
**Fix:**
- Use image editor to manually remove background
- Or leave background (will work, just less polished)

### Wrong Size
**Fix:**
- Resize to 256x256 pixels
- Game will still load, but may look stretched

---

## Quick Commands

**Windows PowerShell:**
```powershell
# Check if files are in right place
cd Rhythm-Warriors
Get-ChildItem -Recurse assets\heroes

# Make all directories at once (run the setup script)
.\setup_asset_folders.ps1

# Or create folders manually
New-Item -ItemType Directory -Force assets\heroes\default\default
New-Item -ItemType Directory -Force assets\heroes\default\skins
# ... repeat for other heroes

# Run Python script
python process_hero_images.py
```

**Mac/Linux:**
```bash
# Check if files are in right place
cd Rhythm-Warriors
ls -R assets/heroes/

# Make all directories at once (run the setup script)
./setup_asset_folders.sh

# Or create folders manually
mkdir -p assets/heroes/{default,shadow,tank,berserker,ancient}/{default,skins}

# Run Python script
python3 process_hero_images.py
```

---

## What I Can Do to Help

While I can't manipulate images, I can:

1. ✅ Create scripts to automate the process
2. ✅ Provide detailed instructions
3. ✅ Help debug any errors
4. ✅ Modify the game code if needed
5. ✅ Create additional tools

**I cannot:**
- ❌ View, download, or edit your images directly
- ❌ Remove backgrounds from images
- ❌ Split your image grid automatically

---

## Next Steps

1. **Choose your method** (Auto script or Manual)
2. **Process your images** (remove backgrounds, resize)
3. **Place files** in correct folders with correct names
4. **Test in game** - Open browser, check console, play!
5. **Ask me** if you encounter any errors or need help!

I'm here to help with any technical issues, code modifications, or troubleshooting! 🚀
