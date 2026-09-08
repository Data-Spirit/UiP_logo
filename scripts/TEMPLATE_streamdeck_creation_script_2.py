import json
import shutil
from pathlib import Path

# ========== CONFIGURATION (robuste) ==========
SCRIPT_DIR = Path(__file__).parent.resolve()

SOURCE_FOLDER = SCRIPT_DIR / "../icons_triFinal"                    # dossier après tri
OUTPUT_FOLDER = SCRIPT_DIR / "../UIP - Ultimate Icon Pack.sdIconPack"

PACK_NAME = "U.I.P. - Ultimate Icon Pack"
AUTHOR = "Spirit"
VERSION = "1.0.0"
DESCRIPTION = "Compilation ultime d'icônes (Source : SVG + PNG) - Tous les icônes de vos apps, services et jeux réunis au même endroit"
# ============================================

def clean_name(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").strip().title()

def generate_pack():
    source = Path(SOURCE_FOLDER).resolve()
    output = Path(OUTPUT_FOLDER).resolve()
    
    # Dossiers de destination dans le pack                                          
    icons_dir = output / "icons"
    svg_dir = icons_dir / "svg"
    png_dir = icons_dir / "png"
    
    svg_dir.mkdir(parents=True, exist_ok=True)
    png_dir.mkdir(parents=True, exist_ok=True)
    
    icons_list = []
    
    # On parcourt TOUS les fichiers du dossier unique                                                     
    for file in sorted(source.glob("*")):
        if file.suffix.lower() not in [".svg", ".png"]:
            continue
        
        base = file.stem
        clean = clean_name(base)
        ext = file.suffix.lower()[1:]
        
        display_name = f"{clean} ({ext.upper()})"
        
        if ext == "svg":
            relative_path = f"svg/{file.name}"
            dest = svg_dir / file.name
            tags = [base.lower(), clean.lower(), "svg", "vector"]
        else:
            relative_path = f"png/{file.name}"
            dest = png_dir / file.name
            tags = [base.lower(), clean.lower(), "png", "raster"]
        
        shutil.copy2(file, dest)
        
        icons_list.append({
            "path": relative_path,
            "name": display_name,
            "tags": tags
        })
    
    # icons.json
    with open(output / "icons.json", "w", encoding="utf-8") as f:
        json.dump(icons_list, f, indent=2, ensure_ascii=False)
    
    # manifest.json
    manifest = {
        "Name": PACK_NAME,
        "Version": VERSION,
        "Description": DESCRIPTION,
        "Author": AUTHOR,
        "URL": "",
        "Icon": "icon.png",
        "License": "license.txt"
    }
    
    with open(output / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    # license.txt
    with open(output / "license.txt", "w", encoding="utf-8") as f:
        f.write("""
U.I.P. - Ultimate Icon Pack
Copyright (c) 2026 Spirit

================================================================================
1. LICENSE OF THE PACK (COMPILATION)
================================================================================

This icon pack, including but not limited to:
- The compilation and selection of icons
- The organization and folder structure
- The naming conventions and tags
- The packaging, manifest, and any accompanying files
- Any scripts or tools created for this pack

is the intellectual property of Spirit and is licensed under the 
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following strict terms:
- Attribution — You must give appropriate credit to "Spirit" as the author of the pack
- NonCommercial — You may not use the material for commercial purposes
- ShareAlike — If you remix, transform, or build upon the material, 
  you must distribute your contributions under the same license as the original.

Full legal code: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

================================================================================
2. OWNERSHIP OF THE ICONS AND TRADEMARKS
================================================================================

All individual icons, logos, symbols, and trademarks contained in this pack 
remain the exclusive intellectual property of their respective owners.

Spirit does NOT claim any ownership over any individual icon or logo.

================================================================================
3. DISCLAIMER
================================================================================

This pack is provided "as is", without warranty of any kind.
""")
    
    svg_count = len(list(svg_dir.glob("*.svg")))
    png_count = len(list(png_dir.glob("*.png")))
    
    print("=" * 60)
    print("✓ Pack U.I.P. généré avec succès !")
    print(f"  Nom            : {PACK_NAME}")
    print(f"  Auteur         : {AUTHOR}")
    print(f"  Total icônes   : {len(icons_list)}")
    print(f"  → SVG          : {svg_count}")
    print(f"  → PNG          : {png_count}")
    print(f"  Dossier sortie : {output}")
    print("=" * 60)
    print("N'oublie pas d'ajouter un petit icon.png (128×128 recommandé) dans le dossier racine du pack.")

if __name__ == "__main__":
    generate_pack()