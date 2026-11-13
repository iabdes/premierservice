# Réseaux sociaux

Instagram et LinkedIn. Exemples complets dans le groupe d’assets Reseaux-sociaux (les quatre premiers posts) ; générateur `scripts/build_social.py` du dépôt.

## Le cadre d’une slide (1080 × 1350)

- Marges `space-marge-post` (88 px). Logo Premier Service en haut à gauche, 200 px de large (blanc sur bleu).
- **Barre de progression** en bas, à 64 px du bord : un segment par slide, 6 px de haut, 10 px d’écart ; segments passés et courant en `progression-active-clair` (blanc sur bleu), les autres en `progression-off-clair` (`progression-off-bleu` sur bleu).
- Première slide : « Faites glisser → » en bas à droite.
- Un champ de couleur par slide (papier ou bleu-marine), en alternance ; deux champs empilés pour une opposition. Chaque slide a un élément visuel qui la remplit : pas de moitié vide.
- Styles `post-couverture`, `post-titre`, `post-chiffre`, `post-texte`, `post-nom-carton`, `post-etiquette`.

## Les gabarits

| Gabarit | Composition |
| --- | --- |
| Couverture | Fond bleu-marine, sigle en `bleu-filigrane` coupé à droite, question ou annonce en `post-couverture` en bas à gauche, phrase d’appui en `texte-sur-bleu` |
| Opposition | Papier en haut, bleu-marine en bas, une phrase dans chaque champ |
| Dessin | Titre en haut, dessin du sigle ou des chaises en bas (la table, les chaises séparées, le cadenas) |
| Chiffres | « 10 étudiants », « 1 personnalité publique » (1 en rouge), cadenas « à huis clos », bandeau bleu « Bientôt. » |
| Deux formats | Deux cartes : dîner (bleu, lune blanche), petit-déjeuner (blanche, soleil rouge) |
| Grille de saison | Titre, période, les douze portraits en 4 × 3, ordre chronologique |
| Carte de rendez-vous | Composant CarteRendezVous en grand (première slide d’un post invité) |
| Invitation | Carte blanche sur bleu : étiquette date rouge, « Un dîner », date complète, lieu, phrase, portrait à la table |
| Étapes | « Vous avez une question à lui poser ? », trois pastilles 1-2-3, la dernière en rouge |
| Action | Fond bleu, titre, bouton blanc « Rejoindre le club » ou « S’inscrire sur Alumni Platform », URL en dessous |
| Cartouche | CartoucheArgonautes, toujours en dernier |

Structure d’un carrousel : couverture → trois à cinq slides de contenu → action → cartouche.

## Formats et publication

- Instagram : carrousel de PNG dans l’ordre ; Reel et story 1080 × 1920.
- LinkedIn : les mêmes images en un PDF, post « Document » avec un titre ; image simple 1200 × 627.
- Vidéo : native, sous-titres incrustés, couverture dédiée, carton de fin.
- Rythme : un post tous les deux à trois jours ; LinkedIn et Instagram le même jour, LinkedIn d’abord. Post d’un invité au moins cinq jours avant le rendez-vous. Pas de compte à rebours dans un visuel (il serait faux le lendemain).

## Les légendes

- Accroche en première ligne, une idée par paragraphe, une action.
- LinkedIn : liens dans le texte, identifier la page Les Argonautes et les fondateurs, 3 ou 4 hashtags, aucun émoji.
- Instagram : « lien en bio », identifier le compte des Argonautes, 5 ou 6 hashtags, deux émojis au plus.
- Hashtags de base : #PremierService #ServicePublic #IntérêtGénéral #Étudiants #Engagement #FonctionPublique.
- Dernière ligne, toujours : « Ce projet est soutenu par Les Argonautes, cabinet de conseil et d’exécution dédié au secteur public. » + lesargos.fr (LinkedIn) ou « lien en bio » (Instagram).

## Piliers éditoriaux

1. Le pourquoi (le problème, la table).
2. Le concept (format, huis clos, saison, club).
3. Les invités (un post par rendez-vous).
4. Après la table (lieu, ambiance, paroles d’étudiants validées par écrit ; jamais le contenu de l’échange).
