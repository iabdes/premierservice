Premier Service réunit dix étudiants et une personnalité publique autour d’une table, à huis clos, dans un lieu de l’action publique. L’initiative est fondée par Louis Pemot, Lara Fourneau et Thawben Berka, avec le soutien des Argonautes. Ce système sert à produire tout ce qui la montre : publications, affiches, présentations, invitations, vidéos.

## Le principe à retenir

Une table, onze places. Dix chaises bleues pour les étudiants, une chaise rouge en haut pour l’invité. Tout le système en découle : le sigle est cette table, le portrait de l’invité prend la place du plateau, le rouge ne marque que l’invité.

## Le ton

- Écrire en français, phrases courtes, au présent. Pas de majuscules de titre à l’anglaise : « Le dîner et le petit-déjeuner », pas « Le Dîner Et Le Petit-Déjeuner ».
- Nommer les choses comme elles sont : « Dîner, lundi 9 novembre, place Beauvau ». Un rendez-vous se désigne par sa date, jamais par un numéro. La formule de référence : « Dix étudiants, un invité, une table. » (« une invitée » pour une femme). La règle : « Ce qui se dit à table reste à table. »
- Typographie française : guillemets « », espace insécable avant : ; ? !, dates en toutes lettres dans les publications (« 9 novembre »), au format 09.11 dans les grilles.
- Pas d’emoji, pas de point d’exclamation, pas de slogan. Les fonctions des invités sont celles du programme officiel, vérifiées avant diffusion.
- Neutralité : chaque invité est présenté de la même façon, sans qualificatif.

## Le logo

- « Premier » au pinceau en `ciel`, « SERVICE » en capitales Outfit ExtraBold en `bleu-marine`. SERVICE se loge sous « Premier » ; le P descend le long du S.
- Toujours depuis les fichiers du groupe Logos (`premier-service_logo_couleur`, `_horizontal_`, `_vertical_`). Le texte est vectorisé : rien à recomposer.
- Sur `papier` ou `blanc` : version couleur. Sur `bleu-marine`, une photo ou un fond sombre : version blanche (le ciel n’y est pas lisible).
- Zone de protection : la hauteur des capitales de SERVICE (x), sur les quatre côtés. Taille minimale : 30 mm imprimé, 160 px à l’écran ; en dessous, le badge.
- Interdits : déformer, pivoter, recolorer, ajouter ombre, contour ou dégradé, recomposer « Premier » dans une autre police, poser la version couleur sur un fond rouge ou bleu.

## Le sigle, le badge, l’icône

- Le sigle est la table vue de dessus : disque `sigle-table`, onze chaises à intervalles égaux, la chaise `sigle-invite` toujours en haut. Ne jamais changer le nombre de chaises ni la place de la rouge.
- Le badge (PREMIER en haut en bleu-marine, SERVICE en bas en rouge) sert aux formats ronds et carrés : avatar, tampon, chevalet. Jamais le logo et le badge sur le même support.
- L’icône (table blanche sur carré bleu-marine, `radius-icone`) sert uniquement à l’application et à l’icône du site.

## Les couleurs

Quatre couleurs de marque, chacune avec un rôle : `bleu-marine` porte la marque, `ciel` ne sert qu’au mot « Premier », `rouge` ne marque que l’invité (chaise, numéro, date), `papier` fait les fonds. Respecter les parts : `part-fond`, `part-bleu`, `part-accents`. Les thèmes Papier et Bleu correspondent aux deux fonds des supports ; utiliser `surface`, `titre`, `texte`, `texte-second`, `mention`, `accent`, qui changent avec eux. Sur bleu, l’accent passe en `papier`.

## La typographie

- Outfit (Google Fonts, libre) pour tout le texte : `titre`, `accroche`, `texte`, `mention` en présentation ; `nom-invite`, `numero-rdv`, `fonction`, `quand-ou` en publication ; les styles `ecran-*` sur le web.
- Breathing ne sert qu’au mot « Premier » du logo, déjà vectorisé. Licence personnelle seulement : acheter la licence commerciale auprès de Din Studio avant toute diffusion publique.
- Mettre en valeur par la graisse ou la couleur, jamais par une taille de plus.

## Les portraits

- Une illustration (portrait peint, fond crème, buste de face), jamais une photo brute. Fichiers du groupe Portraits.
- À table : le portrait est découpé en disque (`radius-rond`) à la place du plateau, entouré des onze chaises, la rouge au-dessus. Fichiers du groupe Portraits-a-table ; composant PortraitATable.
- Animé : chaque invité a un portrait animé de 3 secondes (même cadrage, léger mouvement du visage), en boucle. Fichiers du groupe Portraits-animes (480 px, MP4 sans son) ; originaux 960 px dans le dépôt GitHub. Composant PortraitAnime.
- Le portrait animé se lit toujours muet, en boucle, sans commandes, avec le portrait fixe correspondant en image d’attente. Si le visiteur a demandé de réduire les animations, afficher le portrait fixe seul. Jamais plus de six portraits animés visibles en même temps.
- Chaque portrait porte le nom complet et la fonction du programme, dans cet ordre. Voir la section Saison 1.

## Les formats de rendez-vous

- Deux formats : le dîner (le soir, pictogramme lune) et le petit-déjeuner (le matin, pictogramme soleil). Composant FormatRendezVous.
- Toujours écrire format, date, lieu dans cet ordre : « Petit-déjeuner, 18 novembre, [lieu] ».

## Les supports

- Publication Instagram 1080 × 1350 sur `papier` ; story 1080 × 1920 sur `papier` ; LinkedIn 1200 × 627 et affiche A3 sur `bleu-marine`. Modèles dans le groupe Publications, projections dans Projections.
- Présentations 1920 × 1080 : marges `space-marge`, titre en haut à gauche, pied de page en `mention` à 64 px du bas.
- Partenaire : la mention « Avec le soutien des » suivie du logo des Argonautes, en bas, plus petit que le logo Premier Service. Voir la section Les Argonautes et le composant MentionPartenaire.

## Iconographie

Pas de jeu d’icônes. Les seuls signes sont le sigle, le badge, l’icône et les deux pictogrammes de format (lune, soleil), dessinés dans le composant FormatRendezVous en `bleu-marine` et `rouge`.
