import os
import json
import shutil
from pathlib import Path

# ========== CONFIGURATION ==========
SOURCE_FOLDER = r"C:\chemin\vers\icons_triFinal"          # ← ton dossier unique après tri
OUTPUT_FOLDER = r"C:\chemin\vers\sortie\UIP - Ultimate Icon Pack.sdIconPack"

PACK_NAME = "U.I.P. - Ultimate Icon Pack"
AUTHOR = "Spirit"
VERSION = "1.0.0"
DESCRIPTION = "Compilation ultime d'icônes (Source : SVG + PNG) - Tous les icônes de vos apps, services et jeux réunis au même endroit"
# ===================================

def clean_name(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").strip().title()

def generate_pack():
    source = Path(SOURCE_FOLDER)
    output = Path(OUTPUT_FOLDER)
    
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
            continue  # on ignore tout le reste
        
        base = file.stem
        clean = clean_name(base)
        ext = file.suffix.lower()[1:]  # svg ou png
        
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
        f.write("Usage personnel uniquement.\nPack créé par Spirit - U.I.P. Ultimate Icon Pack")
    
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