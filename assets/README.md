# Hero Assets Directory

This directory contains character sprites and images for the Rhythm Warriors game.

## Directory Structure

```
assets/
└── heroes/
    ├── default/          # Rhythm Knight
    │   ├── default/      # Default Rhythm Knight skin
    │   └── skins/        # Variant skins (Neon Vanguard, Golden Maestro, etc.)
    ├── shadow/           # Shadow Dancer
    │   ├── default/
    │   └── skins/
    ├── tank/             # Iron Guardian
    │   ├── default/
    │   └── skins/
    ├── berserker/        # Berserker
    │   ├── default/
    │   └── skins/
    └── ancient/          # Ancient Sage
        ├── default/
        └── skins/
```

## Adding Character Images

### File Naming Convention

For each hero skin, add an image file with this naming pattern:
- `{heroId}_{skinId}.png`

Examples:
- `default_default.png` - Default Rhythm Knight
- `default_neonVanguard.png` - Neon Vanguard skin
- `shadow_voidAssassin.png` - Shadow Dancer's Void Assassin skin

### Supported Formats

- PNG (recommended for transparency)
- JPG/JPEG
- WebP
- GIF

### Image Specifications

- **Recommended size**: 128x128 to 256x256 pixels
- **Transparent background**: Recommended for best visual effect
- **Facing**: Character should face right (→)
- **Pose**: Idle/standing pose works best

### Placement

1. Navigate to the appropriate hero folder (e.g., `assets/heroes/default/`)
2. Place default skin in `default/` subfolder
3. Place variant skins in `skins/` subfolder
4. Use the naming convention above

### Example Setup

```
assets/heroes/default/
├── default/
│   └── default_default.png        # Default Rhythm Knight
└── skins/
    ├── default_neonVanguard.png   # Neon Vanguard skin
    ├── default_goldenMaestro.png  # Golden Maestro skin
    └── default_festivalChampion.png # Festival Champion skin
```

## Image Loading System

The game includes an automatic image loading system:
- Images are loaded asynchronously when the game starts
- If an image fails to load, the game falls back to geometric shapes
- Images are cached for performance
- All images are preloaded during the loading screen

## Fallback Behavior

If no images are provided, the game will automatically display:
- Colored geometric shapes (current system)
- Triangle bodies with circular heads
- Color-coded based on skin data

This means the game works perfectly even without images!

## Tips for Best Results

1. **Keep file sizes small** (< 100KB per image) for fast loading
2. **Use consistent dimensions** across all character images
3. **Test your images** by opening the game in a browser
4. **Check console** for any image loading errors (F12 → Console)

## Future Enhancements

Planned features for the image system:
- Animated sprite sheets
- Attack animations
- Idle animations
- Special effect overlays
