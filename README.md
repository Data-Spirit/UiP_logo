<!-- BANNIERE CENTRE -->
<div align="center">

![UiP Banner][github_banner]

</div>

<!-- TITRE CENTRE + Sous-Titre CENTRE -->
<h1 align="center">U.I.P. - Ultimate Icon Pack</h1>

<p align="center">
  <em><b>- Compilation ultime d'icônes pour le Stream Deck -</b></em>
</p>

<!-- BADGES CENTRES + LIENS HYPERTEXT INCLUS -->
<div align="center">

[![License: CC BY-NC-SA 4.0][badge_license]][url_license]
[![Status][badge_status]][github_repo]
[![Unofficial][badge_unofficial]][github_repo]
[![Latest Release][badge_release]][github_release]
[![Streamdeck][badge_streamdeck]][url_elgato]
[![Downloads][badge_downloads]][github_release]

</div>

> Plus de 13 000 icônes uniques regroupant les logos des applications, services et marques les plus populaires.

---

<!-- DESCRIPTION -->
## ✨ Description

> **U.I.P. (Ultimate Icon Pack)** est une compilation massive d'icônes destinée au **Stream Deck**.
>
> Avant ce projet, il n'existait aucun pack combinant à la fois une **couverture aussi large** (applications, services, jeux, marques...), une **priorité donnée aux sources SVG officielles** plutôt qu'à des recréations ou captures approximatives, et des **variantes claires/sombres** prêtes à l'emploi. Les icônes existaient déjà, mais éparpillées entre plusieurs projets, dans des formats et des qualités inégales.
>
> **U.I.P. réunit tout ça en un seul pack**, structuré et prêt à installer, en regroupant et en organisant des milliers d'icônes provenant de plusieurs sources reconnues.

---

<!-- COMMENT UTILISER + INSTALLATION -->
## 📥 Installation

> [!NOTE]
> Pour utiliser ce pack sur ton Stream Deck, il te suffit de l'installer : aucune configuration supplémentaire n'est nécessaire, les icônes sont déjà classées et taguées pour une recherche rapide dans l'éditeur. Tu peux choisir entre deux méthodes d'installation ci-dessous.

<details open>
<summary><h3>⚡ Installation automatique</h3></summary>

> - Télécharge le fichier `.streamDeckIconPack` depuis les **[Releases][github_release]**, ou ici : [![Download](./docs/assets/download-loop.svg)][download_uip]
> - Double-clique sur le fichier téléchargé.
> - Stream Deck lance automatiquement l'installation du pack.
> - Le pack apparaît ensuite dans la bibliothèque d'icônes de Stream Deck.

</details>

> [!TIP]
> Si l'installation automatique ne fonctionne pas, tu peux installer le pack manuellement.

<details>
<summary><h3>🛠️ Installation manuelle</h3></summary>

> - Télécharge le fichier `.streamDeckIconPack` depuis les **[Releases][github_release]**
> - Fais une copie du fichier si tu souhaites conserver l'archive originale.
> - Renomme l'extension du fichier **`.streamDeckIconPack`** en **`.zip`**.
>    - Exemple : `Ultimate_Icon_Pack.streamDeckIconPack` → `Ultimate_Icon_Pack.zip`
> - Ouvre l'archive `.zip` avec l'Explorateur Windows ou un logiciel d'archivage comme 7-Zip.
> - Repère le dossier du pack contenu dans l'archive et copie-le dans le répertoire suivant :
>    `%appdata%\Elgato\StreamDeck\IconPacks`
> - Relance Stream Deck si nécessaire. Le pack devrait alors apparaître dans la bibliothèque d'icônes.

<table><tr><td bgcolor="#eaf7ed">
<strong>💡 Astuce</strong><br><br>

<b>Windows peut masquer les extensions de fichiers.</b>
Dans l'Explorateur Windows, si tu ne vois pas l'extension <code>.streamDeckIconPack</code>, il faut aller dans :
<strong><code>Affichage</code> → <code>Afficher</code> → <code>Extensions de noms de fichiers</code></strong>
</td></tr></table>

</details>

---

<!-- AVANTAGES DU PACK -->
## ✨ Pourquoi ce pack se distingue

* 📦 **Plus de 13 000 icônes uniques** : applications, logiciels, services en ligne, streaming (Netflix, Disney+, Prime Video, etc.) — tous les logos de marques réunis au même endroit.
* 🎯 **Priorité aux fichiers `SVG`** : plus légers, plus nets, et redimensionnables sans perte — les `PNG` ne sont conservés que lorsqu'aucune version `SVG` n'existe.
* 🌗 **Variantes claires/sombres** disponibles pour une bonne partie des icônes *(pas systématiquement sur l'ensemble du pack)*, pour un rendu cohérent quel que soit le thème de ton Stream Deck.
* 🗂️ **Organisation claire** du pack (`icons/svg/` et `icons/png/`), pensée pour être facile à parcourir.
* 🔎 **Noms et tags optimisés** pour une recherche rapide et intuitive directement dans Stream Deck.
* 🧩 **3 sources reconnues consolidées** en un seul pack cohérent *(Simple Icons, DashboardIcons, selfh.st)*.
* 🆓 **Gratuit et open-source**, avec une compilation et un packaging clairement documentés.

---

<!-- STRUCTURE DU REPO -->
## 📁 Structure du repo

```
UiP_logo/
├── assets/                        → Éléments graphiques du repo (banner, logo, icône)
├── assets_.streamDeckIconPack/    → Tout le nécessaire à la génération de l'archive du pack via le script Python
├── docs/                          → Documentation additionnelle
├── icons/                         → Icônes du pack, prêtes à l'emploi (svg/ + png/)
├── icons_bank/                    → Banque brute d'icônes sources (avant dédoublonnage/tri)
├── scripts/                       → Scripts Python (déduplication, génération du pack)
├── LICENSE.md
├── TRADEMARKS.md
└── README.md                      → ce fichier
```

---

<!-- REPOS ASSOCIES -->
## 🌐 Repos associés

> U.I.P. est pensé comme une **famille de packs indépendants** plutôt qu'un pack monolithique : chaque repo est autonome (scripts et pipeline propres), et se suffit à lui-même.

<details>
<summary>📋 Légende du tableau :</summary>

- ✅ **Disponible** — Le repo existe et est utilisable.
- 🚧 **En cours** — Le repo est en cours de constitution.
- 🔜 **Prévu** — Le repo est prévu mais le travail n'a pas encore démarré.

</details>

<div align="center">

| | Pack | 🛠️ Contenu | 📦 Statut |
|:---:|---|---|:---:|
| 🖼️ | **UiP_logo** *(ce repo)* | Logos & marques *(applications, services, streaming...)* | ✅ Disponible |
| 🎮 | **UiP_games** | Icônes liées aux jeux vidéo | 🔜 Prévu |
| 🎛️ | **UiP_misc** | Icônes diverses, contrôles et streaming | 🔜 Prévu |
| 🎞️ | **UiP_animated** | Icônes animées | 🔜 Prévu |

</div>

---

<!-- ROADMAP -->
## 🗺️ Roadmap

> - ⚙️ **Automatisation GitHub Actions** : automatiser tout le pipeline de build *(déduplication → génération → `ZIP_STORED` → renommage → publication en Release)* dès que les repos seront stabilisés.
> - 🌐 **GitHub Pages** : mise en place d'une navigation croisée entre tous les repos de la famille UiP.
> - 🖼️ **Captures d'écran** : ajout d'aperçus visuels du pack une fois installé dans Stream Deck.
> - 🧩 **Nouveaux packs** : d'autres packs pourraient rejoindre la famille UiP à plus long terme, en complément de ceux déjà prévus ci-dessus.

---

## ⭐ Soutenir le projet

Si ce pack vous est utile, n'hésitez pas à mettre une étoile ⭐ sur le dépôt.
Ça fait toujours plaisir et ça aide à le faire connaître.

---

<!-- SOURCES -->
## 🙏 Sources

Ce pack est une compilation basée sur les projets suivants (merci à leurs auteurs) :

- [Site : Simple Icons][url_simpleicons] - [GitHub : simple-icons][github_simpleicons] — *icônes de marques et technologies, en SVG.*
- [Site : DashboardIcons][url_dashboardicons] - [GitHub : Dashboard Icons][github_dashboardicons] — *icônes orientées services et applications self-hosted.*
- [Site : selfh][url_selfhst] - [GitHub : selfh.st icons][github_selfhst] — *icônes complémentaires pour l'auto-hébergement.*

---

<!-- LICENCE (CREDIT + IMPORTANT + WARNING) -->
## 📜 Licence

<h3 align="center"><code> ⚠️ Crédit ⚠️ </code></h3>

> - Auteur du pack : **[Spirit][github_user]**
> - Licence du pack : **[CC BY-NC-SA 4.0][url_license]**
> - Icônes individuelles : **propriété de leurs ayants droit respectifs**

> [!IMPORTANT]
> Ce pack (la compilation, l'organisation, les noms, les tags et le packaging) est sous licence :
> **`Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)`**
>
> <strong> Vous êtes libre de : </strong>
> - Partager — copier et redistribuer le pack
> - Adapter — remixer, transformer et construire à partir du pack
>
> <strong> Aux conditions suivantes : </strong>
> - **Attribution** — Vous devez créditer l'auteur du pack
> - **NonCommercial** — Vous n'avez pas le droit d'utiliser ce pack à des fins commerciales
> - **ShareAlike** — Si vous modifiez le pack, vous devez distribuer vos contributions sous la même licence
>
> Licence complète : [CC BY-NC-SA 4.0][url_license]

<h3 align="center"><code> ⚠️ Avertissement important ⚠️ </code></h3>

> [!WARNING]
> **Toutes les icônes, logos et marques déposées individuelles restent la propriété exclusive de leurs ayants droit respectifs** (entreprises, studios de jeux, services, etc.).
>
> Spirit (l'auteur de ce pack) **ne revendique aucun droit** de propriété, de copyright ou de marque sur les icônes individuelles contenues dans cette compilation.
>
> Ce pack est uniquement une collection personnelle et non commerciale réalisée pour des raisons de confort d'utilisation, et n'est **ni affilié à, ni approuvé par Elgato** ou par les marques représentées par les icônes.
>
> L'utilisation des icônes de ce pack ne confère aucun droit sur les marques ou contenus protégés qu'elles représentent.

> 📄 Voir aussi : [LICENSE.md][github_license] · [TRADEMARKS.md][github_trademarks]

<!-- ============================== -->
<!--    Link & Badge Definitions    -->
<!-- ============================== -->

<!-- Badges (shields.io images) -->
[badge_license]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
[badge_status]: https://img.shields.io/badge/status-active-brightgreen.svg
[badge_unofficial]: https://img.shields.io/badge/Ultimate_icon_Pack_:-Logo-blue.svg
[badge_release]: https://img.shields.io/github/v/release/Data-Spirit/UiP_logo?sort=semver&display_name=tag&style=flat&logo=github&logoSize=auto&labelColor=grey&color=green
[badge_streamdeck]: https://img.shields.io/badge/Elgato-StreamDeck-blue?style=flat&logo=elgato&logoColor=white&logoSize=auto&label=Elgato&labelColor=black&color=white
[badge_downloads]: https://img.shields.io/github/downloads/Data-Spirit/UiP_logo/total?style=flat&logoSize=auto&label=Downloads&labelColor=1b6078&color=grey

<!-- External URLs (services tiers, hors GitHub) -->
[url_license]: https://creativecommons.org/licenses/by-nc-sa/4.0/
[url_elgato]: https://marketplace.elgato.com/
[url_simpleicons]: https://simpleicons.org/
[url_dashboardicons]: https://dashboardicons.com/
[url_selfhst]: https://selfh.st/icons/

<!-- GitHub links & local repo files -->
[github_repo]: https://github.com/Data-Spirit/UiP_logo
[github_release]: https://github.com/Data-Spirit/UiP_logo/releases/latest
[github_license]: ./LICENSE.md
[github_trademarks]: ./TRADEMARKS.md
[github_user]: https://github.com/Data-Spirit
[github_banner]: ./docs/img/UiP_banner_02.webp
<!-- url_lien_absolu: https://raw.githubusercontent.com/Data-Spirit/UiP_logo/main/assets/banner_01.png -->
[github_simpleicons]: https://github.com/simple-icons/simple-icons
[github_dashboardicons]: https://github.com/homarr-labs/dashboard-icons
[github_selfhst]: https://github.com/selfhst/icons

<!-- Liens de téléchargement -->
[download_uip]: https://github.com/Data-Spirit/UiP_logo/releases/download/v1.1/UIP-Ultimate_Icon_Pack_Logo.streamDeckIconPack