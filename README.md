# Premier Service — identité et kit de marque

Premier Service réunit dix étudiants et une personnalité publique autour d’une table, à huis clos, dans un lieu de l’action publique (dîner le soir, petit-déjeuner le matin). Initiative fondée par Louis Pemot, Lara Fourneau et Thawben Berka, avec le soutien des Argonautes.

Ce dépôt rassemble tous les éléments de l’identité, version du 13 novembre 2026.

## Contenu

| Dossier | Ce qu’il contient |
| --- | --- |
| `identite/logos/` | Logo seul, horizontal (sigle à gauche), vertical (sigle au-dessus), en couleur et en blanc. SVG vectoriel + PNG transparent. |
| `identite/sigle-badge/` | Sigle (la table aux onze chaises), badge rond PREMIER / SERVICE, icône d’application. |
| `identite/construction/` | Planches de construction du logo (zone de protection x) et du sigle. |
| `identite/couleurs/` | Palette et valeurs. |
| `motion/` | Calques séparés pour l’animation : « Premier » et « SERVICE », la table et chacune des chaises, sur un canevas commun. Voir `motion/LISEZ-MOI.txt`. |
| `partenaire/les-argonautes/` | Logo du partenaire (fond clair, fond sombre, monogramme). |
| `portraits/illustres/` | Les douze portraits illustrés de la saison 1, 1254 px. |
| `portraits/a-table/` | Les mêmes, découpés au centre de la table. |
| `publications/modeles/` | Instagram 1080 × 1350, story 1080 × 1920, LinkedIn 1200 × 627, affiche A3, pour les rendez-vous n°1 et n°3. |
| `publications/projections/` | Maquettes de mise en situation. |
| `charte-graphique/` | Sources de la présentation de la charte (27 diapositives, format Slides : `deck.json`, `deck.css`, `slides/`). Les images y sont référencées par l’artefact en ligne. |
| `design-system/` | Système de marque : `README.md` (guide), `tokens.json` (couleurs, typographie, espacements), `saison-1.md`, `les-argonautes.md`, composants avec aperçus. |
| `scripts/` | Scripts Python qui génèrent logos, sigle, publications et portraits (fontTools, uharfbuzz, rsvg-convert). Chemins à adapter. |

## L’essentiel

- Logo : « Premier » au pinceau en ciel profond `#2C86D1`, « SERVICE » en Outfit ExtraBold bleu marine `#1E2F86`.
- Sigle : la table vue de dessus, dix chaises bleu marine, la chaise de l’invité en rouge `#E0313B`, toujours en haut.
- Fonds : blanc cassé `#FAF7F0` ou blanc ; bleu marine pour les affiches et LinkedIn, avec le logo blanc.
- Texte : Outfit (Google Fonts, licence libre).
- Partenaire : « Avec le soutien des » + logo des Argonautes, en bas, plus petit que le logo Premier Service.

## Saison 1 (novembre – décembre 2026)

| N° | Date | Format | Invité |
| --- | --- | --- | --- |
| 1 | 09.11 | Dîner | Marie-Pierre Vedrenne |
| 2 | 17.11 | Dîner | Olivier Faure |
| 3 | 18.11 | Petit-déjeuner | Éric Lombard |
| 4 | 19.11 | Dîner | Jérôme Guedj |
| 5 | 24.11 | Dîner | Valérie Pécresse |
| 6 | 25.11 | Petit-déjeuner | Matthieu Landon |
| 7 | 03.12 | Dîner | Karim Zéribi |
| 8 | 09.12 | Dîner | Agnès Buzyn |
| 9 | 15.12 | Dîner | Jacques Attali |
| 10 | 16.12 | Dîner | Karim Bouamrane |
| 11 | 17.12 | Petit-déjeuner | Naïma Moutchou |
| 12 | 17.12 | Dîner | Bernard Cazeneuve |

Fonctions détaillées dans `design-system/saison-1.md`, à revalider avec chaque invité avant diffusion.

## Licences et réserves

- La police du mot « Premier » (Breathing, Din Studio) est sous licence d’usage personnel : elle n’est pas incluse ici. Le mot est vectorisé dans les fichiers du logo. Acheter la licence commerciale avant toute diffusion publique.
- Le logo des Argonautes appartient aux Argonautes : à n’utiliser que pour la mention de partenariat.
- Les portraits sont des illustrations de personnalités publiques : vérifier les droits d’usage et l’accord de chaque invité avant publication.
