# CarteRendezVous

La carte d’un rendez-vous, telle qu’elle apparaît sur premierservice.club et, agrandie, en première slide d’un post invité.

- Fournir : portrait de l’invité (`premier-service_portrait_<prénom-nom>`), format, date, nom complet, fonction du programme, statut.
- Ordre fixe : portrait carré pleine largeur ; pastille du format en haut à droite (dîner : `bleu-marine` et lune blanche ; petit-déjeuner : `blanc` et soleil bleu) ; étiquette date à cheval sur le bas du portrait (jour en `rouge-texte`, chiffre ExtraBold `bleu-marine`, mois en `gris`) ; « Prochain » en pilule `rouge` pour le rendez-vous le plus proche, qui reçoit aussi un contour rouge de 2 px ; ticket en pointillés `filet` avec deux encoches ; nom (`site-carton-nom`), fonction (`site-carton-fonction`, deux lignes au plus) ; pied : statut en `rouge-texte` et action « Candidater ».
- Passé : portrait en noir et blanc, opacité 70 %, étiquette sur `papier`, statut « Rendez-vous passé », pas d’action.
- Site : grille 2 / 3 / 4 colonnes, groupée par mois, apparition en cascade, survol (la carte monte de 4 px, l’étiquette pivote de −4°).
- Réseaux sociaux : même anatomie en 1080 × 1350 (`post-nom-carton`, statut « Dix places, à huis clos », action « S’inscrire → »), sans compte à rebours.
- Ne pas : abréger le nom, ajouter un qualificatif, changer l’ordre, mettre le portrait en rond (c’est le rôle de PortraitATable).
