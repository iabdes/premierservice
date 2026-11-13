# Site Premier Service — brief de réalisation

Site vitrine d’une page (plus pages légales) pour Premier Service : dix étudiants et une personnalité de la vie publique, à huis clos, autour d’un dîner ou d’un petit-déjeuner. Initiative fondée par Louis Pemot, Lara Fourneau et Thawben Berka, soutenue par Les Argonautes.

Maquette de référence (source exacte des textes, couleurs et comportements) : `site/maquette/Main.dc.html`.

## Règles

- Français, typographie française (’ ; espaces insécables avant : ; ? ! ; guillemets « »).
- Utiliser exactement les textes de la maquette. N’inventer aucun chiffre, citation, témoignage ou logo.
- Pas de base de données, pas de compte : la candidature se fait sur Alumni Platform (lien externe).
- Accessibilité : contrastes AA, navigation clavier, focus visible (anneau #2C86D1), textes alternatifs, `prefers-reduced-motion` respecté (toutes les animations à l’arrêt, bulles immobiles sans chevauchement).
- Aucun cookie ni traceur tiers.

## Identité

| Jeton | Valeur | Usage |
| --- | --- | --- |
| bleu-marine | #1E2F86 | Titres, boutons, SERVICE |
| ciel | #2C86D1 | Uniquement le mot « Premier » du logo et l’anneau de focus |
| rouge | #E0313B | Chaise de l’invité, dates, numéros, compte à rebours |
| papier | #FAF7F0 | Fond général |
| blanc | #FFFFFF | Sections alternées, cartes |
| encre | #1A1D33 | Texte, pied de page |
| gris | #4F546E | Texte secondaire |
| doux | #6B6F85 | Mentions |
| argo-creme | #F5F1E8 | Carte partenaire |
| argo-rouge | #F10F23 | Survol du bouton lesargos.fr uniquement |

Police : Outfit (Google Fonts) 400 à 800. Titres 800, interlettrage −0,02 em. Rayons : cartes 24 px, boutons en pilule.

## Fichiers (dans ce dépôt, à copier dans `public/`)

- Logo horizontal couleur : `identite/logos/premier-service_logo-horizontal_couleur.svg`
- Logo blanc : `identite/logos/premier-service_logo_blanc.svg`
- Les Argonautes : `partenaire/les-argonautes/les-argonautes_logo_fond-clair.svg`
- Portraits (900 px) : `portraits/web/premier-service_portrait_<prénom-nom>.jpg`

## Sections, dans l’ordre

1. **En-tête** blanc : logo horizontal ; liens Le principe, La saison, Le club ; bouton « Candidater ». Menu repliable sur mobile.
2. **Accueil** : H1 « Entre ceux qui ont servi l’État et ceux qui le serviront, il manquait une table. », paragraphe, deux boutons. Dessous, une **scène** (hauteur clamp(360px, 42vw, 580px)) :
   - au centre, un **grand rond bleu marine** (210 à 380 px) avec le logo blanc, un bouton lecture blanc entouré d’une onde qui pulse et « Le film · 1 min 30 » ;
   - autour, **les douze portraits en bulles rondes** (bord blanc 5 px, ombre), de 67 à 140 px ;
   - **moteur physique** simple : chaque bulle avance en ligne droite (22 à 38 px/s, le grand rond 9 px/s), rebondit sur les bords, et les bulles **se cognent sans jamais se superposer** (collisions élastiques, masse proportionnelle à la surface, écart minimal 6 px) ;
   - **survol ou focus** d’une bulle : elle s’arrête, grossit de 25 % (et repousse ses voisines), son nom apparaît dans une pastille ; **clic** : contour rouge et fiche en bas de la scène (numéro, format, date, nom, fonction, bouton fermer) ;
   - **clic sur le grand rond** : fenêtre modale avec lecteur vertical 9:16 (86 vh, coins 28 px) qui apparaît en « pop-in » ; plein écran sous 600 px ; fermeture par × , clic sur le fond et touche Échap. Vidéo : emplacement réservé `[URL_VIDEO]`, avec image d’aperçu et sous-titres à brancher.
3. **Le principe** : trois cartes animées (au chargement puis au survol) : « Une table » (la table apparaît, les dix chaises bleues une à une, la rouge en dernier), « À huis clos » (le cadenas se ferme, une bulle « Ce qui se dit à table reste à table. » apparaît), « Deux formats » (fenêtre de ciel : la lune descend, le soleil se lève).
4. **Le prochain invité** : calculé à la date du jour ; grand portrait flottant, pastille rouge « Aujourd’hui / Demain / Dans N jours », « Le prochain invité · rendez-vous n°N », nom en très grand, fonction, format avec lune ou soleil et date complète (« Dîner, mardi 17 novembre »), boutons « Candidater pour ce rendez-vous » et « Toute la saison ».
5. **Saison 1, douze rendez-vous** : filtre Tous / Dîners / Petits-déjeuners ; cartes verticales (portrait carré, pastille date · format, « Rendez-vous n°N », nom, fonction) ; rendez-vous passés en noir et blanc avec la pastille « Passé ».
6. **Prendre place à la table** (candidater) : texte, critères `[À PRÉCISER]`, bouton « Candidater sur Alumni Platform » (https://alumniplatform.net/join/premierservice), trois étapes reliées par un trait.
7. **Après la table, le club** : annuaire, événements, lettre, groupe WhatsApp.
8. **Le mot des fondateurs** : trois bulles flottantes (initiales en attendant les photos) avec nom en pastille ; texte de la maquette (à faire valider par les fondateurs).
9. **Pied de page** sombre, avec la **carte partenaire** crème à cheval sur la section précédente : logo Les Argonautes, filet, « Ce projet est soutenu par Les Argonautes, cabinet de conseil et d’exécution dédié au secteur public. », bouton « lesargos.fr » (https://lesargos.fr, nouvel onglet). Puis logo blanc, navigation, contact `[ADRESSE E-MAIL]`, liens Mentions légales, Confidentialité, Accessibilité (pages à créer avec des emplacements `[À REMPLIR]`).

## Programme (source unique, un fichier de données)

| N° | Date | Format | Invité | Fonction | Portrait |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-11-09 | Dîner | Marie-Pierre Vedrenne | Ministre déléguée à la Citoyenneté | marie-pierre-vedrenne |
| 2 | 2026-11-17 | Dîner | Olivier Faure | Premier secrétaire du Parti socialiste | olivier-faure |
| 3 | 2026-11-18 | Petit-déjeuner | Éric Lombard | Ancien ministre de l’Économie | eric-lombard |
| 4 | 2026-11-24 | Dîner | Valérie Pécresse | Présidente de la Région Île-de-France | valerie-pecresse |
| 5 | 2026-11-25 | Petit-déjeuner | Matthieu Landon | Secrétaire général adjoint de l’Élysée | matthieu-landon |
| 6 | 2026-12-02 | Dîner | Jérôme Guedj | Député de l’Essonne | jerome-guedj |
| 7 | 2026-12-03 | Dîner | Karim Zéribi | Ancien député européen | karim-zeribi |
| 8 | 2026-12-09 | Dîner | Agnès Buzyn | Ancienne ministre de la Santé | agnes-buzyn |
| 9 | 2026-12-15 | Dîner | Jacques Attali | Économiste et écrivain | jacques-attali |
| 10 | 2026-12-16 | Dîner | Karim Bouamrane | Maire de Saint-Ouen | karim-bouamrane |
| 11 | 2026-12-17 | Petit-déjeuner | Naïma Moutchou | Ministre des Outre-mer | naima-moutchou |
| 12 | 2026-12-17 | Dîner | Bernard Cazeneuve | Ancien Premier ministre | bernard-cazeneuve |

## Emplacements à remplir

`[URL_VIDEO]`, https://alumniplatform.net/join/premierservice, lien WhatsApp, critères d’éligibilité, photos des fondateurs, adresse de contact, mentions légales (éditeur, hébergeur), politique de confidentialité, déclaration d’accessibilité.
