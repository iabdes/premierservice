# BulleInvite

La scène d’accueil du site : douze bulles de portraits (67 à 140 px, bord blanc de 5 px, `ombre-bulle`) qui dérivent et se cognent autour d’un grand rond `bleu-marine` (210 à 380 px) qui lance le film.

- Mouvement : ligne droite à `vitesse-bulles`, rebond sur les bords, collisions élastiques (masse proportionnelle à la surface), jamais de superposition, écart minimal 6 px. Le grand rond avance à 9 px/s.
- Survol ou focus : la bulle s’arrête, grossit de 25 % (`ease-rebond`), son nom apparaît en pilule `bleu-marine`. Clic : contour `rouge` et fiche du rendez-vous (format, date, nom, fonction).
- Grand rond : bouton lecture blanc avec une onde qui pulse, « Le film · 1 min 30 » ; au clic, lecteur vertical 9:16 en modale (`radius-modale`, pop-in).
- Animations réduites : bulles immobiles, réparties sans chevauchement. Pas de portrait animé dans les bulles.
