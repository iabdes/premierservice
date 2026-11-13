# SlideCarrousel

Le cadre commun des slides d’un carrousel Instagram ou d’un document LinkedIn, 1080 × 1350 px.

- Marges `space-marge-post`. Logo en haut à gauche, 200 px de large, blanc sur bleu, couleur sur papier.
- Barre de progression à 64 px du bas : un segment par slide, 6 px de haut ; actifs en `progression-active-clair` (blanc sur bleu), inactifs en `progression-off-clair` ou `progression-off-bleu`.
- Un champ par slide : `bleu-marine` ou `papier`, en alternance ; deux champs empilés pour une opposition.
- Couverture : sigle en `bleu-filigrane` coupé à droite, titre `post-couverture` en bas à gauche, phrase d’appui en `texte-sur-bleu`, « Faites glisser → ».
- Contenu : titre `post-titre` en haut, un élément visuel en bas (sigle, chaises, cadenas, cartes, portraits) : jamais une moitié vide. Texte `post-texte`, jamais sous 32 px.
- Ordre : couverture, trois à cinq slides de contenu, action, CartoucheArgonautes.
- Générateur : `scripts/build_social.py` du dépôt (`frame`, `progress`, `cover`, `carton`, `argo_card`). Exemples complets : groupe Reseaux-sociaux.
