# Le site

premierservice.club : une page, puis trois pages légales. Fond `papier`, sections alternées `blanc`, largeur utile 1240 px, marge verticale `space-section-site`. Aucun cookie ni traceur tiers. Toutes les animations s’arrêtent si le visiteur réduit les animations.

## Les sections, dans l’ordre

| Section | Contenu | Composants |
| --- | --- | --- |
| En-tête | Logo horizontal, liens Le principe, La saison, Le club, bouton « Rejoindre le club » | Logo, Bouton |
| Accueil | Titre `site-h1` « Entre ceux qui ont servi l’État et ceux qui le serviront, il manquait une table. », deux boutons, puis la scène : douze bulles de portraits qui se cognent sans se superposer autour d’un grand rond bleu-marine qui lance le film | BulleInvite, Bouton |
| Film | Au clic sur le grand rond : lecteur vertical 9:16 en fenêtre modale, `radius-modale`, ouverture en pop-in (`ease-rebond`), plein écran sous 600 px, fermeture par ×, fond ou Échap | |
| Le principe | Trois cartes animées : « Une table » (la table, puis les chaises une à une, la rouge en dernier), « À huis clos » (le cadenas se ferme, la bulle « Ce qui se dit à table reste à table. »), « Deux formats » (la lune descend, le soleil se lève) | FormatRendezVous |
| Le prochain invité | Calculé à la date du jour : portrait animé en grand, compte à rebours rouge, nom très grand, fonction, format et date complète, boutons | PortraitAnime, Bouton |
| La saison | « Saison 1, douze rendez-vous », filtres Tous / Dîners / Petits-déjeuners avec leur nombre, cartes groupées par mois | CarteRendezVous |
| Prendre place à la table | Candidature en trois étapes sur Alumni Platform : créer son profil, choisir un rendez-vous, recevoir l’invitation | Bouton |
| Le mot des fondateurs | Le visuel principal des trois fondateurs (médaillon bleu), légende « De gauche à droite : Thawben Berka, Lara Fourneau, Louis Pemot », texte signé | PortraitFondateur |
| Après la table, le club | Annuaire, événements, lettre, groupe WhatsApp, bouton « Rejoindre le club » | Bouton |
| Pied de page | Carte partenaire écume à cheval sur la section précédente (logo des Argonautes, phrase, bouton lesargos.fr qui passe au rouge `argo-rouge` au survol), logo blanc, navigation, contact, mentions | CartoucheArgonautes, Bouton |

## Comportements

- **Bulles** : vitesse `vitesse-bulles`, rebond sur les bords, collisions élastiques, écart minimal 6 px. Survol ou focus : la bulle s’arrête, grossit de 25 %, son nom apparaît en pastille bleu-marine ; clic : contour rouge et fiche du rendez-vous. Pas d’animation de portrait dans l’en-tête (trop petit).
- **Portraits animés** : un à la fois par carte, à tour de rôle, au ralenti ; image fixe en attente.
- **Cartes de la saison** : apparition en cascade (`duree-cascade`), survol : la carte monte de 4 px, l’image zoome de 5 %, l’étiquette date pivote de −4°. Rendez-vous passé : noir et blanc, opacité 70 %, « Rendez-vous passé ».
- **Focus** : anneau `ciel` de 3 px, décalé de 3 px. Cibles de 48 px au moins.

## Liens

- Club et candidature : https://alumniplatform.net/join/premierservice (« Rejoindre le club »).
- Partenaire : https://lesargos.fr, nouvel onglet.
- Encore à fournir : URL de la vidéo et sous-titres, lien WhatsApp, adresse de contact, pages légales.
