import shutil
from pathlib import Path

# ========== CONFIGURATION (robuste) ==========
SCRIPT_DIR = Path(__file__).parent.resolve()          # dossier où se trouve ce script
SVG_FOLDER = SCRIPT_DIR / "../icons/svg"              # adapte si besoin
PNG_FOLDER = SCRIPT_DIR / "../icons/png"              # adapte si besoin
OUTPUT_FOLDER = SCRIPT_DIR / "../icons_triFinal"
# ============================================

def deduplicate_icons():
    svg_path = Path(SVG_FOLDER).resolve()
    png_path = Path(PNG_FOLDER).resolve()
    output_path = Path(OUTPUT_FOLDER).resolve()
    
    # Créer le dossier de sortie											
    if output_path.exists():
        shutil.rmtree(output_path)  # on repart de zéro
    output_path.mkdir(parents=True)
    
    # Dictionnaire des noms déjà traités														 
    kept_names = set()
    
    # 1. On ajoute d'abord TOUS les SVG (priorité)
    svg_count = 0
    for file in svg_path.glob("*.svg"):
        name = file.stem.lower()
        shutil.copy2(file, output_path / file.name)
        kept_names.add(name)
        svg_count += 1
    
    # 2. On ajoute les PNG uniquement s'il n'y a PAS déjà un SVG du même nom
    png_count = 0
    png_skipped = 0
    for file in png_path.glob("*.png"):
        name = file.stem.lower()
        if name in kept_names:
            png_skipped += 1
            continue
        shutil.copy2(file, output_path / file.name)
        kept_names.add(name)
        png_count += 1
    
    total = svg_count + png_count
    
    print("=" * 55)
    print("✓ Tri terminé !")
    print(f"  SVG gardés     : {svg_count}")
    print(f"  PNG gardés     : {png_count}")
    print(f"  PNG ignorés    : {png_skipped}")
    print(f"  Total unique   : {total}")
    print(f"  Dossier sortie : {output_path}")
    print("=" * 55)
    print("Tu peux maintenant utiliser ce dossier icons_triFinal comme SOURCE_FOLDER pour le script de création du pack.")																																									

if __name__ == "__main__":
    deduplicate_icons()