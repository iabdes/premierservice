Premier Service réunit dix étudiants et une personnalité de la vie publique autour d’une table, à huis clos, pour un dîner ou un petit-déjeuner. Après la table, les participants rejoignent le club sur Alumni Platform. L’initiative est fondée par Thawben Berka, Lara Fourneau et Louis Pemot, avec le soutien des Argonautes.

Ce système est **l’élément maître** de la marque. Toute production (site, publications, carrousels, vidéos, présentations, affiches, portraits, documents) part d’ici, et la compétence d’agent graphique et community manager s’appuie dessus. Version 2 du 13 novembre 2026 : elle réunit la charte, le site premierservice.club, les publications réseaux sociaux, les scripts vidéo et les fiches des fondateurs.

## Comment s’en servir

1. Lire ce brand book, puis la section qui correspond au support : **Le site**, **Réseaux sociaux**, **Audiovisuel**, **Les fondateurs**, **Les Argonautes**, **Saison 1**, **Produire un support**.
2. Prendre les valeurs dans `tokens.json` (couleurs, typographie, espacements, rayons, ombres, animation), jamais à l’œil.
3. Poser les fichiers des groupes d’assets tels quels : logos, sigle, portraits, cartouche. Rien ne se redessine.
4. Reproduire les composants (Logo, Badge, PortraitATable, PortraitAnime, PortraitFondateur, FormatRendezVous, CarteInvite, CarteRendezVous, Bouton, SlideCarrousel, CartoucheArgonautes) : chacun a ses règles et un aperçu.
5. Finir **chaque** support par le cartouche Les Argonautes.

Sources : dépôt GitHub `iabdes/premierservice` (fichiers sources, scripts de génération, charte en texte `charte-graphique/CHARTE.md`), présentation de la charte (35 diapositives), site premierservice.club, dossier Drive « Premier Service » (Brand Design, Rendu audiovisuel, Community Management).

## Le principe à retenir

Une table, onze places. Dix chaises bleues pour les étudiants, une chaise rouge en haut pour l’invité. Tout le système en découle : le sigle est cette table, le portrait de l’invité prend la place du plateau, le rouge ne marque que l’invité et la date du rendez-vous.

## L’esprit et le ton

- **Sobre, direct, chaleureux.** Phrases courtes, au présent, une idée par phrase, vouvoiement dans les publications. Pas de jargon administratif, pas de slogan, pas de point d’exclamation.
- **Ce qui se dit à table reste à table.** Aucune photo, vidéo ou story pendant l’échange ; aucune citation, même anonyme, sans accord écrit. Dans les vidéos, la table est montrée avant l’arrivée des participants, puis la porte se ferme.
- **Neutre, toujours.** Chaque invité est présenté de la même façon : nom complet, fonction du programme, sans qualificatif ni position. Formule pour les invités politiques : « Premier Service reçoit cette saison des personnalités d’horizons et de sensibilités différents. »
- **Une conversation, pas un débouché.** Ne jamais promettre stage, réseau, accès ou recrutement. Aucun superlatif.
- **Une seule action par support** : rejoindre le club, ou s’inscrire à un rendez-vous, sur Alumni Platform.
- **Les faits viennent du programme** (section Saison 1). Ce qui manque reste entre crochets (`[Lieu à confirmer]`) et ne part pas en publication.
- Typographie française : guillemets « », apostrophe ’, espace insécable avant : ; ? ! ; dates en toutes lettres en publication (« mercredi 2 décembre »), au format 02.12 dans les grilles. Un rendez-vous se désigne par sa date, jamais par un numéro.

### Vocabulaire de la marque

| Dire | Ne pas dire |
| --- | --- |
| une table, dix étudiants, un invité (une invitée) | un panel, une conférence, un événement networking |
| un dîner, un petit-déjeuner | un afterwork, un brunch |
| à huis clos | en off, confidentiel |
| la saison 1, la Cohorte d’automne, une session | l’édition, le programme VIP |
| 10 étudiants par session, dix places | places limitées, exclusif |
| le club, rejoindre le club | la communauté, le réseau |
| candidater, s’inscrire sur Alumni Platform | postuler, réserver |
| le chevalet Premier Service | le carton de table |

Phrases de référence : « Dix étudiants, un invité, une table. » · « Ce qui se dit à table reste à table. » · « Nous organisons les rencontres que nous aurions aimé qu’on nous propose. » · « À chaque table, une seule règle : parler vrai. » · « Le lendemain commence à table. »

## Le logo

- « Premier » au pinceau en `ciel`, « SERVICE » en capitales Outfit ExtraBold en `bleu-marine`. SERVICE se loge sous « Premier » ; le P descend le long du S.
- Toujours depuis les fichiers du groupe Logos (seul, horizontal, vertical ; couleur ou blanc). Le texte est vectorisé : rien à recomposer.
- Sur `papier` ou `blanc` : version couleur. Sur `bleu-marine`, une photo ou un fond sombre : version blanche.
- Zone de protection : la hauteur des capitales de SERVICE, sur les quatre côtés. Taille minimale : 30 mm imprimé, 160 px à l’écran ; en dessous, le badge. Dans un carrousel : 200 px de large, à 72 px du bord gauche et 60 px du haut.
- Interdits : déformer, pivoter, recolorer, ajouter ombre, contour ou dégradé, recomposer « Premier » dans une autre police, poser la version couleur sur un fond rouge ou bleu.

## Le sigle, le badge, l’icône

- Le sigle est la table vue de dessus : disque `sigle-table`, onze chaises à intervalles égaux, la chaise `sigle-invite` toujours en haut. Ne jamais changer le nombre de chaises ni la place de la rouge.
- En filigrane : sur les couvertures bleu-marine, le sigle en `bleu-filigrane`, coupé par le bord droit, chaise rouge conservée.
- Le badge (PREMIER en haut, SERVICE en bas en rouge) sert aux formats ronds : avatar, tampon, chevalet. Jamais le logo et le badge sur le même support.
- L’icône (table blanche sur carré bleu-marine, `radius-icone`) : application, favicon (fond blanc pour le favicon du site).

## Les couleurs

`bleu-marine` porte la marque, `ciel` ne sert qu’au mot « Premier », `rouge` ne marque que l’invité (chaise, date, « Prochain », un chiffre), `papier` fait les fonds, `blanc` les cartes, `encre` le texte, `gris` le texte secondaire. En petit texte rouge, `rouge-texte`. Parts : `part-fond` 60 %, `part-bleu` 30 %, `part-accents` 10 % au plus. Thèmes Papier et Bleu : utiliser `surface`, `surface-carte`, `titre`, `texte`, `texte-second`, `mention`, `accent`, qui changent avec eux.

Les couleurs des Argonautes (`argo-creme`, `argo-noir`, `argo-rouge`, `argo-galet`) ne vivent que dans leur cartouche et leurs fichiers.

## La typographie

- Outfit (Google Fonts, libre) pour tout le texte. Titres ExtraBold 800, interlettrage −0,02 em ; texte Regular ; étiquettes SemiBold. Pas d’italique, pas de capitales espacées, pas de mot coloré dans un titre.
- Groupes de styles : présentations, publications, carrousels (`post-*`), site (`site-*`), écran. Jamais sous 32 px sur un visuel de 1080 px, 24 px en présentation, 14 px à l’écran.
- Breathing ne sert qu’au mot « Premier » du logo, déjà vectorisé. Licence personnelle seulement : licence commerciale à acheter avant diffusion publique.

## Les portraits

- **Invités** : illustration peinte, fond crème, buste de face, jamais une photo brute. À table : portrait en disque à la place du plateau, onze chaises autour, la rouge au-dessus (PortraitATable). Animé : boucle de 3 s, muette, au ralenti (`vitesse-portrait-anime`), deux au plus en même temps (PortraitAnime). Rendez-vous passé : noir et blanc.
- **Fondateurs** : dessin au crayon et à la gouache dans un médaillon bleu-marine au filet ivoire (PortraitFondateur). Voir la section Les fondateurs.
- Chaque portrait porte le nom complet et la fonction du programme, dans cet ordre. Accord de chaque invité sur son portrait avant diffusion.

## Les formats de rendez-vous

Le dîner (le soir, lune) et le petit-déjeuner (le matin, soleil). Toujours format, date, lieu, dans cet ordre : « Dîner, mercredi 2 décembre, [lieu] ». Composant FormatRendezVous ; pastille de format dans CarteRendezVous.

## Les supports

| Support | Format | Section |
| --- | --- | --- |
| Site | premierservice.club | Le site |
| Carrousel Instagram, PDF LinkedIn | 1080 × 1350 | Réseaux sociaux |
| Story, Reel, film | 1080 × 1920 | Réseaux sociaux, Audiovisuel |
| Image LinkedIn | 1200 × 627 | groupe Publications |
| Affiche | A3 | groupe Publications |
| Présentation | 1920 × 1080, marges `space-marge` | Produire un support |
| Fiche de script, storyboard, document de production | A4, charte des Argonautes | Audiovisuel |

## Le cartouche Les Argonautes (obligatoire)

Chaque support se termine par le soutien des Argonautes : dernière slide d’un carrousel, carton de fin d’une vidéo, dernière diapositive d’une présentation publique, dernière ligne d’une légende. Fond `argo-creme`, tout centré : « Ce projet est soutenu par », le logo des Argonautes, « Cabinet de conseil et d’exécution dédié au secteur public. », l’étiquette lesargos.fr. Composant CartoucheArgonautes, section Les Argonautes.

## Iconographie

Pas de jeu d’icônes. Les seuls signes sont le sigle, le badge, l’icône, la lune et le soleil des formats, le cadenas du huis clos et la flèche des actions (« Faites glisser → », « S’inscrire → »), dessinés au trait rond.
