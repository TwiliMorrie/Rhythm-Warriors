# Windows Quick Start Guide 🪟

This guide is specifically for **Windows PowerShell** users!

## 🚀 Quick Setup (3 Steps)

### Step 1: Create Asset Folders
```powershell
# Navigate to game folder
cd Rhythm-Warriors

# Run the setup script
.\setup_asset_folders.ps1
```

This creates all necessary folders automatically!

### Step 2: Add Your Character Images

**Option A: Quick Test (One Image)**
1. Save ONE character from your grid as a PNG
2. Remove background using https://remove.bg
3. Rename to: `default_neonVanguard.png`
4. Place in: `assets\heroes\default\skins\`
5. Open `rhythm-warriors-combined.html` in browser
6. Done! Test it out!

**Option B: Process All Images (Automated)**
1. Install Python requirements:
   ```powershell
   pip install Pillow
   pip install rembg
   ```

2. Split your image grid into 12 separate images
3. Create folder and add images:
   ```powershell
   mkdir hero_images
   # Save individual character images in hero_images folder
   ```

4. Run the processing script:
   ```powershell
   python process_hero_images.py
   ```

The script will automatically:
- Remove backgrounds
- Resize to 256x256
- Place in correct folders
- Name files correctly

### Step 3: Test in Game
1. Open `rhythm-warriors-combined.html` in any browser
2. Press `F12` to open Console (to see image loading status)
3. Go to **Skins** menu
4. Equip a skin
5. Start playing!

---

## 📁 Folder Structure

After running setup, you'll have:
```
Rhythm-Warriors\
└── assets\
    └── heroes\
        ├── default\         (Rhythm Knight)
        │   ├── default\
        │   └── skins\
        ├── shadow\          (Shadow Dancer)
        │   ├── default\
        │   └── skins\
        ├── tank\            (Iron Guardian)
        │   ├── default\
        │   └── skins\
        ├── berserker\       (Berserker)
        │   ├── default\
        │   └── skins\
        └── ancient\         (Ancient Sage)
            ├── default\
            └── skins\
```

---

## 🎨 Image File Naming

Place images in the appropriate folder with this naming:
- `{heroId}_{skinId}.png`

**Examples:**
- `default_neonVanguard.png` → Neon Vanguard skin for Rhythm Knight
- `shadow_voidAssassin.png` → Void Assassin skin for Shadow Dancer
- `tank_runicFortress.png` → Runic Fortress skin for Iron Guardian

**Full List:**

### Rhythm Knight (default)
- `default\skins\default_neonVanguard.png`
- `default\skins\default_goldenMaestro.png`
- `default\skins\default_festivalChampion.png`

### Shadow Dancer (shadow)
- `shadow\skins\shadow_voidAssassin.png`
- `shadow\skins\shadow_cyberNinja.png`
- `shadow\skins\shadow_eclipsePhantom.png`

### Iron Guardian (tank)
- `tank\skins\tank_runicFortress.png`
- `tank\skins\tank_moltenBulwark.png`
- `tank\skins\tank_crystalSentinel.png`

### Berserker (berserker)
- `berserker\skins\berserker_bloodDrummer.png`
- `berserker\skins\berserker_hellfireRavager.png`
- `berserker\skins\berserker_frostbiteFury.png`

### Ancient Sage (ancient)
- `ancient\skins\ancient_astralArchivist.png`
- `ancient\skins\ancient_celestialOracle.png`
- `ancient\skins\ancient_temporalScribe.png`

---

## 🔧 Common PowerShell Commands

### Check If Images Are In Right Place
```powershell
Get-ChildItem -Recurse assets\heroes
```

### Create A Single Folder
```powershell
New-Item -ItemType Directory -Force assets\heroes\default\skins
```

### Run Image Processing (Interactive Mode)
```powershell
python process_hero_images.py --interactive
```
This lets you manually choose which image goes to which hero/skin.

### Open Assets Folder
```powershell
explorer assets\heroes
```

---

## ⚠️ Troubleshooting

### "Cannot run script" Error
If PowerShell won't run `.ps1` files, you need to enable scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Python Not Found
Install Python from https://python.org (check "Add to PATH" during install)

### Images Not Showing in Game
1. Open browser console (F12)
2. Look for error messages
3. Check file path and name exactly match
4. Verify PNG format
5. Try refreshing browser (Ctrl+F5)

### Need to Remove Background
Use one of these tools:
- **Easy:** https://remove.bg (upload, download)
- **Free:** https://photopea.com (online Photoshop)
- **Software:** GIMP (free download)

---

## 💡 Pro Tips

1. **Test with one image first** before processing all
2. **Keep backups** of your original images
3. **Use descriptive filenames** when saving from grid
4. **Check console** (F12 in browser) for loading errors
5. **Image size:** 128-512 pixels works great (256 is perfect)

---

## 📋 Workflow Example

Here's a complete workflow:

```powershell
# 1. Setup folders
cd Rhythm-Warriors
.\setup_asset_folders.ps1

# 2. Create hero_images folder
mkdir hero_images

# 3. Split your grid into individual images
#    Save each character as: neon_knight.png, golden_knight.png, etc.

# 4. Process all images
pip install Pillow rembg
python process_hero_images.py

# 5. Open game
start rhythm-warriors-combined.html

# Done! Your character images are now in the game!
```

---

## 🎮 What Works Without Images

The game **works perfectly** without images! It uses geometric shapes:
- Colored triangles for bodies
- Circles for heads
- Your skin colors still apply

So you can play right now even without adding images!

---

## 📞 Need Help?

- Check `MANUAL_IMAGE_SETUP.md` for detailed instructions
- Check `SKIN_SYSTEM_COMPLETE.md` for full documentation
- Open an issue if you encounter problems

**The game is ready to play right now with or without custom images!** 🚀
