import os
import shutil
from pathlib import Path

# ========== CONFIGURATION ==========
SVG_FOLDER = r"C:\chemin\vers\icons\svg"          # ← dossier des SVG
PNG_FOLDER = r"C:\chemin\vers\icons\png"          # ← dossier des PNG
OUTPUT_FOLDER = r"C:\chemin\vers\icons_triFinal"  # ← dossier de sortie (unique)
# ===================================

def deduplicate_icons():
    svg_path = Path(SVG_FOLDER)
    png_path = Path(PNG_FOLDER)
    output_path = Path(OUTPUT_FOLDER)
    
    # Créer le dossier de sortie
    if output_path.exists():
        shutil.rmtree(output_path)  # on repart de zéro
    output_path.mkdir(parents=True)
    
    # Dictionnaire des noms déjà traités
    kept_names = set()
    
    # 1. On ajoute d'abord TOUS les SVG (priorité)
    svg_count = 0
    for file in svg_path.glob("*.svg"):
        name = file.stem.lower()  # on ignore la casse
        dest = output_path / file.name
        shutil.copy2(file, dest)
        kept_names.add(name)
        svg_count += 1
    
    # 2. On ajoute les PNG uniquement s'il n'y a PAS déjà un SVG du même nom
    png_count = 0
    png_skipped = 0
    for file in png_path.glob("*.png"):
        name = file.stem.lower()
        
        if name in kept_names:
            png_skipped += 1
            continue  # on ignore ce PNG car SVG existe déjà
        
        # Pas de version SVG → on garde le PNG
        dest = output_path / file.name
        shutil.copy2(file, dest)
        kept_names.add(name)
        png_count += 1
    
    total = svg_count + png_count
    
    print("=" * 55)
    print("✓ Tri terminé !")
    print(f"  SVG gardés          : {svg_count}")
    print(f"  PNG gardés          : {png_count}  (ceux qui n'avaient pas de SVG)")
    print(f"  PNG ignorés         : {png_skipped}  (doublons SVG existants)")
    print(f"  Total unique final  : {total}")
    print(f"  Dossier de sortie   : {output_path}")
    print("=" * 55)
    print("Tu peux maintenant utiliser ce dossier icons_triFinal comme SOURCE_FOLDER pour le script de création du pack.")

if __name__ == "__main__":
    deduplicate_icons()