import json, os, datetime
from ds_blobs import GROUPS
D = "ds/project/"
def w(p, s):
    os.makedirs(os.path.dirname(D + p), exist_ok=True); open(D + p, "w").write(s)
B = {os.path.basename(f).rsplit(".",1)[0]: "/_blob/" + b for _, _, fs in GROUPS for f, b in fs}
def b(n): return B[n]
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# ---------------- tokens ----------------
def c(name, light, dark=None, usage=""):
    return {"name": name, "value": ({"light": light, "dark": dark} if dark else light), "usage": usage}
tokens = {"name": "Premier Service", "version": 1,
 "color": {"themes": [{"id": "light", "name": "Papier"}, {"id": "dark", "name": "Bleu"}], "tokens": [
  c("bleu-marine", "#1E2F86", usage="Couleur principale. SERVICE, la table du sigle, les titres, les fonds bleus des affiches et de LinkedIn."),
  c("ciel", "#2C86D1", usage="Ciel profond. Réservé au seul mot « Premier » du logo. Jamais pour du texte courant ni pour un fond."),
  c("rouge", "#E0313B", usage="La chaise de l’invité, les numéros et dates de rendez-vous, SERVICE dans le badge. Toujours en petite surface, jamais en fond. Texte rouge : 24 px minimum (3,9:1 sur papier)."),
  c("papier", "#FAF7F0", usage="Blanc cassé : fonds de pages, de publications et de diapositives."),
  c("blanc", "#FFFFFF", usage="Fond du logo et des cartes ; texte et logo blancs sur bleu-marine."),
  c("encre", "#1A1D33", usage="Texte courant sur papier et blanc (15:1)."),
  c("gris", "#4F546E", usage="Texte secondaire, fonctions des invités, sur papier et blanc (7,6:1)."),
  c("doux", "#6B6F85", usage="Mentions et pieds de page sur papier et blanc (4,9:1)."),
  c("filet", "#E6E1D6", usage="Bordure du blanc cassé quand il est posé sur blanc."),
  c("bleu-voile", "#26389A", usage="Disque décoratif derrière les téléphones, sur bleu-marine. Jamais pour du texte."),
  c("texte-sur-bleu", "#DDE0EF", usage="Texte secondaire sur bleu-marine (10:1)."),
  c("mention-sur-bleu", "#C9CDE3", usage="Mentions et « Avec le soutien des » sur bleu-marine (8,3:1)."),
  c("surface", "#FAF7F0", "#1E2F86", "Fond de page. Papier en clair, bleu-marine en sombre (affiches, LinkedIn)."),
  c("surface-carte", "#FFFFFF", "#26389A", "Cartes et encarts posés sur surface."),
  c("titre", "#1E2F86", "#FFFFFF", "Titres et noms d’invités sur surface (10:1 en clair, 10:1 en sombre)."),
  c("texte", "#1A1D33", "#FAF7F0", "Texte courant sur surface et surface-carte."),
  c("texte-second", "#4F546E", "#DDE0EF", "Fonctions, légendes, sur surface et surface-carte."),
  c("mention", "#6B6F85", "#C9CDE3", "Pieds de page, mention du partenaire, sur surface."),
  c("accent", "#E0313B", "#FAF7F0", "Numéro et date du rendez-vous. Rouge en clair ; blanc cassé sur bleu, où le rouge ne passe pas (2,4:1)."),
  c("sigle-table", "#1E2F86", "#FFFFFF", "Disque de la table et chaises des étudiants : bleu-marine sur fond clair, blanc sur bleu."),
  c("sigle-invite", "#E0313B", "#E0313B", "Chaise de l’invité, toujours rouge, en haut."),
  c("argo-rouge", "#F10F23", usage="Les Argonautes : rouge du logo partenaire. Uniquement dans leurs fichiers, jamais dans un élément Premier Service."),
  c("argo-noir", "#010101", usage="Les Argonautes : encre du logo sur fond clair."),
  c("argo-creme", "#F5F1E8", usage="Les Argonautes : lettres du logo sur fond sombre."),
 ]},
 "type": {"fonts": [],
  "families": {"outfit": "\"Outfit\", Arial, sans-serif"},
  "groups": [
   {"name": "Charte et présentations (1920 × 1080)", "family": "outfit", "styles": [
     {"name": "titre", "fontSize": "88px", "lineHeight": 1.05, "fontWeight": 800, "letterSpacing": "-2px", "sample": "Une table", "usage": "Titre de diapositive ou de page, en titre."},
     {"name": "accroche", "fontSize": "44px", "lineHeight": 1.2, "fontWeight": 600, "sample": "Rendez-vous n°1, place Beauvau", "usage": "Accroche, intertitre."},
     {"name": "texte", "fontSize": "32px", "lineHeight": 1.4, "fontWeight": 400, "sample": "Ce qui se dit à table reste à table.", "usage": "Texte courant des présentations."},
     {"name": "mention", "fontSize": "24px", "lineHeight": 1.4, "fontWeight": 400, "sample": "Premier Service, charte graphique", "usage": "Pied de page, légende. Jamais plus petit."}]},
   {"name": "Publications (1080 × 1350, 1080 × 1920)", "family": "outfit", "styles": [
     {"name": "nom-invite", "fontSize": "78px", "lineHeight": 1.05, "fontWeight": 800, "letterSpacing": "-1px", "sample": "Marie-Pierre Vedrenne", "usage": "Nom de l’invité, en titre."},
     {"name": "numero-rdv", "fontSize": "36px", "lineHeight": 1.2, "fontWeight": 600, "sample": "Rendez-vous n°1", "usage": "Numéro du rendez-vous, en accent."},
     {"name": "fonction", "fontSize": "34px", "lineHeight": 1.3, "fontWeight": 400, "sample": "Ministre déléguée à la Citoyenneté", "usage": "Fonction de l’invité, en texte."},
     {"name": "quand-ou", "fontSize": "36px", "lineHeight": 1.3, "fontWeight": 600, "sample": "Dîner, 9 novembre, place Beauvau", "usage": "Format, date et lieu, en titre."}]},
   {"name": "Écran (site, documents)", "family": "outfit", "styles": [
     {"name": "ecran-titre", "fontSize": "40px", "lineHeight": 1.1, "fontWeight": 800, "letterSpacing": "-0.8px", "sample": "Saison 1, douze rendez-vous"},
     {"name": "ecran-intertitre", "fontSize": "22px", "lineHeight": 1.3, "fontWeight": 700, "sample": "Le dîner et le petit-déjeuner"},
     {"name": "ecran-texte", "fontSize": "17px", "lineHeight": 1.55, "fontWeight": 400, "sample": "Dix étudiants, un invité, une table."},
     {"name": "ecran-mention", "fontSize": "14px", "lineHeight": 1.45, "fontWeight": 500, "sample": "Avec le soutien des Argonautes"}]}]},
 "spacing": {"tokens": [
   {"name": "space-1", "value": "8px", "usage": "Entre une icône de format et sa date."},
   {"name": "space-2", "value": "16px", "usage": "Entre lignes d’une carte invité."},
   {"name": "space-3", "value": "24px", "usage": "Entre cartes d’une grille d’invités."},
   {"name": "space-4", "value": "32px", "usage": "Entre blocs d’une page ; gouttière des grilles 4 colonnes."},
   {"name": "space-5", "value": "48px", "usage": "Marge intérieure des cartes de présentation."},
   {"name": "space-6", "value": "56px", "usage": "Écart entre titre et contenu d’une diapositive."},
   {"name": "space-marge", "value": "128px", "usage": "Marges d’une diapositive 1920 × 1080 ; 64–72 px sur une publication 1080 px."}]},
 "radius": {"tokens": [
   {"name": "radius-carte", "value": "24px", "usage": "Cartes, encarts, photos détourées en carré."},
   {"name": "radius-encart", "value": "20px", "usage": "Petites étiquettes posées de biais (page « Ce que dit le logo »)."},
   {"name": "radius-chaise", "value": "23%", "usage": "Arrondi d’une chaise du sigle : 3,2 / 14 de sa largeur."},
   {"name": "radius-icone", "value": "22.5%", "usage": "Coins de l’icône d’application."},
   {"name": "radius-rond", "value": "50%", "usage": "La table : le portrait de l’invité est toujours découpé en disque."}]},
 "proportion": {"note": "Part de chaque couleur sur un support.", "tokens": [
   {"name": "part-fond", "value": "60%", "usage": "Papier ou blanc."},
   {"name": "part-bleu", "value": "30%", "usage": "Bleu-marine."},
   {"name": "part-accents", "value": "10%", "usage": "Ciel et rouge réunis, au plus."}]},
 "shadow": {"tokens": [{"name": "ombre-maquette", "value": "0 24px 56px rgba(26,29,51,0.22)", "usage": "Uniquement sous un téléphone ou une affiche dans une maquette de projection. Jamais sous le logo."}]}
}
w("tokens.json", json.dumps(tokens, ensure_ascii=False, indent=1))

# ---------------- README ----------------
w("README.md", f"""Premier Service réunit dix étudiants et une personnalité publique autour d’une table, à huis clos, dans un lieu de l’action publique. L’initiative est fondée par Louis Pemot, Lara Fourneau et Thawben Berka, avec le soutien des Argonautes. Ce système sert à produire tout ce qui la montre : publications, affiches, présentations, invitations, vidéos.

## Le principe à retenir

Une table, onze places. Dix chaises bleues pour les étudiants, une chaise rouge en haut pour l’invité. Tout le système en découle : le sigle est cette table, le portrait de l’invité prend la place du plateau, le rouge ne marque que l’invité.

## Le ton

- Écrire en français, phrases courtes, au présent. Pas de majuscules de titre à l’anglaise : « Le dîner et le petit-déjeuner », pas « Le Dîner Et Le Petit-Déjeuner ».
- Nommer les choses comme elles sont : « Rendez-vous n°1 », « Dîner, 9 novembre, place Beauvau ». La formule de référence : « Dix étudiants, un invité, une table. » (« une invitée » pour une femme). La règle : « Ce qui se dit à table reste à table. »
- Typographie française : guillemets « », espace insécable avant : ; ? !, « n°1 », dates en toutes lettres dans les publications (« 9 novembre »), au format 09.11 dans les grilles.
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
""")

w("saison-1.md", """# Saison 1

Novembre – décembre 2026, douze rendez-vous, dans l’ordre du programme. Intitulés repris du programme ; à revalider avec chaque invité avant diffusion.

| N° | Date | Format | Invité | Fonction |
| --- | --- | --- | --- | --- |
| 1 | 09.11 | Dîner | Marie-Pierre Vedrenne | Ministre déléguée à la Citoyenneté |
| 2 | 17.11 | Dîner | Olivier Faure | Premier secrétaire du Parti socialiste |
| 3 | 18.11 | Petit-déjeuner | Éric Lombard | Ancien ministre de l’Économie |
| 4 | 19.11 | Dîner | Jérôme Guedj | Député de l’Essonne |
| 5 | 24.11 | Dîner | Valérie Pécresse | Présidente de la Région Île-de-France |
| 6 | 25.11 | Petit-déjeuner | Matthieu Landon | Secrétaire général adjoint de l’Élysée |
| 7 | 03.12 | Dîner | Karim Zéribi | Ancien député européen |
| 8 | 09.12 | Dîner | Agnès Buzyn | Ancienne ministre de la Santé |
| 9 | 15.12 | Dîner | Jacques Attali | Économiste et écrivain |
| 10 | 16.12 | Dîner | Karim Bouamrane | Maire de Saint-Ouen |
| 11 | 17.12 | Petit-déjeuner | Naïma Moutchou | Ministre des Outre-mer |
| 12 | 17.12 | Dîner | Bernard Cazeneuve | Ancien Premier ministre |

- Lieux connus : place Beauvau pour le n°1. Les autres lieux sont à compléter.
- Fichiers : `premier-service_portrait_<prénom-nom>` (illustration) et `premier-service_portrait-a-table_<prénom-nom>` (à table).
- Le numéro suit l’ordre chronologique ; le 17 décembre, le petit-déjeuner précède le dîner.
""")

w("les-argonautes.md", """# Les Argonautes, partenaire

Les Argonautes, cabinet de conseil et d’exécution pour le secteur public, soutiennent Premier Service, notamment sur la communication. Leur présence est une signature de partenaire, jamais une co-marque.

- Écrire « Avec le soutien des » en Outfit, couleur `mention` (ou `mention-sur-bleu`), puis le logo des Argonautes. Ne jamais recomposer « Les Argonautes » dans une police : toujours les fichiers du groupe Les-Argonautes.
- Sur fond clair : `les-argonautes_logo_fond-clair` (encre `argo-noir`, accent `argo-rouge`). Sur bleu ou sombre : `les-argonautes_logo_fond-sombre` (lettres `argo-creme`). Sous 80 px de large : le monogramme.
- Place : en bas du support, centré ou à droite, séparé du logo Premier Service par au moins deux fois sa propre hauteur. Largeur : 140 à 190 px sur une publication de 1080 px, soit environ la moitié de la largeur du logo Premier Service ou moins.
- Couleurs : `argo-rouge`, `argo-noir`, `argo-creme` ne vivent que dans les fichiers des Argonautes. Le rouge Premier Service reste `rouge`.
- Dans une vidéo : mention en fin de signature, après le logo Premier Service, une seconde au moins.
- Ne pas présenter le soutien des Argonautes comme un accès privilégié aux invités ou aux institutions.
""")

# ---------------- bundle.css ----------------
w("components/bundle.css", """.ps { font-family: var(--font-outfit); color: var(--texte); }
.ps-format { display: inline-flex; align-items: center; gap: var(--space-1); font-weight: 600; color: var(--accent); }
.ps-format svg { width: 1.1em; height: 1.1em; flex: none; }
.ps-format .lune { fill: var(--titre); }
.ps-format .soleil { fill: var(--accent); stroke: var(--accent); }
.ps-carte { display: flex; align-items: center; gap: var(--space-3); }
.ps-carte img { width: 120px; height: 120px; object-fit: contain; flex: none; }
.ps-carte .nom { font-weight: 800; color: var(--titre); line-height: 1.1; letter-spacing: -0.3px; }
.ps-carte .fonction { color: var(--texte-second); line-height: 1.3; }
.ps-partenaire { display: inline-flex; align-items: center; gap: 10px; color: var(--mention); }
.ps-partenaire img { height: 26px; width: auto; }
""")

def card(name, group, height, subtitle, body, readme):
    w(f"components/{name}/preview.html", f'<!-- @dsCard group="{group}" height={height} subtitle="{subtitle}" -->\n{body}\n')
    w(f"components/{name}/README.md", readme)

STY = '<style>body{margin:0;background:var(--surface);font-family:var(--font-outfit)} .row{display:flex;gap:24px;padding:20px;flex-wrap:wrap;align-items:center} .tile{border-radius:16px;padding:20px;display:flex;align-items:center;justify-content:center} .lbl{font:500 13px var(--font-outfit);color:var(--mention);margin-top:8px;text-align:center}</style>'
card("Logo", "Identité", 260, "Couleur sur clair, blanc sur bleu",
 STY + f'<div class="row"><div><div class="tile" style="background:#FFFFFF;width:300px;height:150px"><img src="{b("premier-service_logo-horizontal_couleur")}" alt="Logo Premier Service horizontal, couleur" style="width:270px"></div><div class="lbl">Horizontal, couleur</div></div>'
 f'<div><div class="tile" style="background:#1E2F86;width:300px;height:150px"><img src="{b("premier-service_logo-horizontal_blanc")}" alt="Logo Premier Service horizontal, blanc" style="width:270px"></div><div class="lbl">Horizontal, blanc</div></div>'
 f'<div><div class="tile" style="background:#FAF7F0;width:150px;height:150px"><img src="{b("premier-service_logo_couleur")}" alt="Logo Premier Service" style="width:130px"></div><div class="lbl">Seul</div></div></div>',
 """# Logo

La signature Premier Service : « Premier » au pinceau en `ciel`, « SERVICE » en `bleu-marine`, avec ou sans le sigle.

- Fournir : le fichier SVG ou PNG du groupe Logos, jamais une recomposition. Trois formes : seul, horizontal (sigle à gauche), vertical (sigle au-dessus).
- Fond clair (`papier`, `blanc`) : couleur. Fond `bleu-marine`, photo ou sombre : blanc.
- Zone de protection x (hauteur des capitales de SERVICE) ; minimum 160 px à l’écran, 30 mm imprimé.
- Ne pas : déformer, pivoter, recolorer, ombrer, poser la version couleur sur bleu ou rouge, le mettre avec le badge sur le même support.
""")
card("Badge", "Identité", 220, "Formats ronds et carrés",
 STY + f'<div class="row"><div><div class="tile" style="background:#FFFFFF;width:170px;height:170px"><img src="{b("premier-service_badge_couleur")}" alt="Badge Premier Service, couleur" style="width:150px"></div><div class="lbl">Badge</div></div>'
 f'<div><div class="tile" style="background:#1E2F86;width:170px;height:170px"><img src="{b("premier-service_badge_blanc")}" alt="Badge Premier Service, blanc" style="width:150px"></div><div class="lbl">Badge blanc</div></div>'
 f'<div><div class="tile" style="background:#FFFFFF;width:170px;height:170px"><img src="{b("premier-service_sigle_couleur")}" alt="Sigle : la table aux onze chaises" style="width:140px"></div><div class="lbl">Sigle</div></div>'
 f'<div><div class="tile" style="background:#FAF7F0;width:170px;height:170px"><img src="{b("premier-service_icone")}" alt="Icône d’application" style="width:120px"></div><div class="lbl">Icône</div></div></div>',
 """# Badge

Le sigle seul, le badge rond et l’icône, pour les formats où le logo serait trop petit.

- Badge : avatar de réseau social, tampon, chevalet, autocollant ; minimum 48 px, 12 mm. PREMIER en `bleu-marine` en haut, SERVICE en `rouge` en bas.
- Sigle : ouverture et fin de vidéo, motif, filigrane. Onze chaises, la `sigle-invite` en haut.
- Icône : application et favicon uniquement.
- Ne pas : faire tourner la table, changer le nombre de chaises, mettre la chaise rouge ailleurs qu’en haut, poser badge et logo ensemble.
""")
pa = [("premier-service_portrait-a-table_marie-pierre-vedrenne","Marie-Pierre Vedrenne"),("premier-service_portrait-a-table_eric-lombard","Éric Lombard"),("premier-service_portrait-a-table_valerie-pecresse","Valérie Pécresse"),("premier-service_portrait-a-table_karim-bouamrane","Karim Bouamrane")]
card("PortraitATable", "Invités", 240, "L’invité à la place de la table",
 STY + '<div class="row">' + "".join(f'<div><img src="{b(k)}" alt="Portrait de {n} à la table Premier Service" style="width:170px;height:170px"><div class="lbl">{n}</div></div>' for k, n in pa) + '</div>',
 """# PortraitATable

Le portrait illustré de l’invité, découpé en disque à la place du plateau, entouré des onze chaises, la rouge au-dessus.

- Fournir : le fichier `premier-service_portrait-a-table_<prénom-nom>` (groupe Portraits-a-table). Pour un nouvel invité : portrait carré 1254 px, visage centré à 48 % de la hauteur, fond crème, puis découpe en disque de 94 % de la largeur.
- Toujours avec le nom complet et la fonction du programme à proximité.
- Sur `bleu-marine`, chaises en blanc cassé, chaise de l’invité rouge.
- Ne pas : utiliser une photo brute, recadrer en carré, ajouter un cadre.
""")
MOON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path class="lune" d="M15.5 3.2A9 9 0 1 0 20.8 15 7.2 7.2 0 0 1 15.5 3.2Z"/></svg>'
SUN = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle class="soleil" cx="12" cy="12" r="4.6"/><path class="soleil" d="M12 1.8v3M12 19.2v3M1.8 12h3M19.2 12h3M4.8 4.8l2.1 2.1M17.1 17.1l2.1 2.1M4.8 19.2l2.1-2.1M17.1 6.9l2.1-2.1" stroke-width="2" stroke-linecap="round" fill="none"/></svg>'
card("FormatRendezVous", "Invités", 120, "Dîner le soir, petit-déjeuner le matin",
 STY + f'<div class="row ps" style="font-size:24px;gap:40px"><span class="ps-format">{MOON}09.11 · Dîner</span><span class="ps-format">{SUN}18.11 · Petit-déjeuner</span></div>',
 """# FormatRendezVous

L’étiquette qui dit quand a lieu le rendez-vous : pictogramme, date, format.

- Fournir : la date (09.11 dans une grille, « 9 novembre » dans une publication) et le format, « Dîner » ou « Petit-déjeuner ».
- Lune en `titre` pour le dîner, soleil en `accent` pour le petit-déjeuner ; texte en `accent`, Outfit 600, 24 px minimum.
- Le format s’écrit toujours avant la date et le lieu dans une phrase : « Dîner, 9 novembre, place Beauvau ».
- Le pictogramme accompagne toujours le mot : il ne le remplace jamais.
""")
G2 = [("premier-service_portrait-a-table_marie-pierre-vedrenne","Marie-Pierre Vedrenne","Ministre déléguée à la Citoyenneté","09.11","Dîner"),("premier-service_portrait-a-table_eric-lombard","Éric Lombard","Ancien ministre de l’Économie","18.11","Petit-déjeuner")]
card("CarteInvite", "Invités", 200, "Une case de la grille de la saison",
 STY + '<div class="row ps" style="gap:48px">' + "".join(f'<div class="ps-carte"><img src="{b(k)}" alt="Portrait de {n} à la table Premier Service"><div style="display:flex;flex-direction:column;gap:6px"><span class="ps-format" style="font-size:16px">{MOON if f=="Dîner" else SUN}{d} · {f}</span><span class="nom" style="font-size:22px">{n}</span><span class="fonction" style="font-size:15px">{t}</span></div></div>' for k,n,t,d,f in G2) + '</div>',
 """# CarteInvite

Une case de la grille des invités : portrait à table, format et date, nom, fonction.

- Fournir : le portrait à table, la date, le format, le nom complet, la fonction exacte du programme.
- Ordre de lecture fixe : format et date (`accent`), nom (`titre`, ExtraBold), fonction (`texte-second`).
- Grilles de 4 × 3 en présentation, de 3 × 4 en document portrait ; ordre chronologique.
- Ne pas : abréger le nom, ajouter un qualificatif, changer l’ordre des lignes.
""")
card("MentionPartenaire", "Partenaire", 140, "Avec le soutien des Argonautes",
 STY + f'<div class="row" style="padding:0"><div class="tile ps" style="background:#FAF7F0;width:340px;height:80px;border-radius:0"><span class="ps-partenaire" style="color:#6B6F85;font-size:15px">Avec le soutien des <img src="{b("les-argonautes_logo_fond-clair")}" alt="Les Argonautes"></span></div>'
 f'<div class="tile ps" style="background:#1E2F86;width:340px;height:80px;border-radius:0"><span class="ps-partenaire" style="color:#C9CDE3;font-size:15px">Avec le soutien des <img src="{b("les-argonautes_logo_fond-sombre")}" alt="Les Argonautes"></span></div></div>',
 """# MentionPartenaire

La signature du partenaire : « Avec le soutien des » suivi du logo des Argonautes.

- Fournir : le fichier `les-argonautes_logo_fond-clair` sur fond clair, `_fond-sombre` sur bleu ; le monogramme sous 80 px.
- Texte en `mention` (clair) ou `mention-sur-bleu` (bleu), Outfit, même hauteur optique que le logo.
- En bas du support, plus petit que le logo Premier Service, jamais dans le même bloc que lui.
- Ne pas : recomposer « Les Argonautes » en texte, recolorer leur logo, utiliser `argo-rouge` ailleurs.
""")

# ---------------- cover ----------------
chairs = []
import math
cx, cy, R = 700, 150, 168
for i in range(11):
    a = i * 360 / 11
    cls = "inv" if i == 0 else "ch"
    chairs.append(f'<rect class="{cls}" x="{cx-21}" y="{cy-R-13}" width="42" height="26" rx="8" transform="rotate({a:.2f} {cx} {cy})"/>')
w("components/Cover/preview.html", f"""<!-- @dsCard height=300 -->
<style>
html,body{{margin:0;height:100%;background:var(--surface)}}
.cv{{position:relative;width:960px;height:300px;overflow:hidden;background:var(--surface);font-family:var(--font-outfit)}}
.cv svg{{position:absolute;left:0;top:0}}
.tab{{fill:var(--sigle-table)}} .ch{{fill:var(--sigle-table)}} .inv{{fill:var(--sigle-invite)}} .sky{{fill:var(--ciel)}} .voile{{fill:var(--surface-carte)}}
.nm{{position:absolute;left:48px;bottom:64px;width:420px;font-weight:800;font-size:96px;line-height:.95;letter-spacing:-2px;color:var(--titre);margin:0}}
.tg{{position:absolute;left:48px;bottom:32px;width:420px;font-size:14px;color:var(--texte-second);margin:0}}
</style>
<div class="cv">
<svg width="960" height="300" viewBox="0 0 960 300" aria-hidden="true">
<!-- blocks: sigle-table disc r=120 (the table) + surface-carte slab 400x300 + ciel band 160x56 rx 24 (radius-carte) + sigle-invite chair
     arrangement: one slab bleeding off the right edge, the table centred on it, ciel band low left of the slab
     pattern: literal motif, the table's eleven chairs on one ring (radius-chaise ≈ 8/42); the brand IS a table seen from above
     scales: ring 168 = table r 120 x 1.4 (R_RING/R_TABLE), chair 42x26, gap space-4 32, radius-carte 24 -->
<rect class="voile" x="560" y="0" width="400" height="300"/>
<rect class="sky" x="496" y="212" width="160" height="56" rx="24"/>
<circle class="tab" cx="{cx}" cy="{cy}" r="120"/>
{''.join(chairs)}
</svg>
<p class="nm">Premier<br>Service</p>
<p class="tg">Dix étudiants, un invité, une table.</p>
</div>
""")

# ---------------- index ----------------
ag, groups = {}, []
readmes = {
 "Logos": "Le logo Premier Service en SVG : seul, horizontal (sigle à gauche), vertical (sigle au-dessus), en couleur (fond clair) et en blanc (fond bleu ou photo). Couleur : « Premier » `ciel`, SERVICE `bleu-marine`, chaise de l’invité `rouge`. Blanc : tout en blanc sauf la chaise de l’invité, rouge.",
 "Sigle": "Sigle (la table et ses onze chaises), badge rond PREMIER / SERVICE, icône d’application. Couleur : table `bleu-marine`, chaise de l’invité `rouge`. Blanc : table blanche, chaise rouge, pour les fonds bleus.",
 "Construction": "Planches de construction : le logo avec sa zone de protection x et le sigle avec ses cercles et ses onze axes.",
 "Portraits-a-table": "Les douze invités de la saison 1, portrait découpé en disque au centre de la table. Nommés premier-service_portrait-a-table_<prénom-nom>.",
 "Portraits": "Les douze portraits illustrés, carrés, fond crème, 900 px (originaux 1254 px dans le dossier Drive du projet). Nommés premier-service_portrait_<prénom-nom>.",
 "Publications": "Modèles des rendez-vous n°1 (dîner, Marie-Pierre Vedrenne) et n°3 (petit-déjeuner, Éric Lombard) : Instagram 1080 × 1350, story 1080 × 1920, LinkedIn 1200 × 627, affiche A3 1190 × 1684.",
 "Projections": "Maquettes de mise en situation : téléphones Instagram et stories, publication LinkedIn, affiches au mur.",
 "Les-Argonautes": "Logo du partenaire Les Argonautes. fond-clair : encre `argo-noir`, accent `argo-rouge`. fond-sombre : lettres `argo-creme`. Monogramme pour les petits formats. Ne jamais recomposer ni recolorer.",
}
mime = {"svg": "image/svg+xml", "png": "image/png", "jpg": "image/jpeg"}
for g, tile, fs in GROUPS:
    files, order = {}, []
    for f, bid in fs:
        n = os.path.basename(f); order.append(n)
        files[n] = {"name": n, "blob": bid, "size": os.path.getsize(f), "type": mime[n.rsplit(".",1)[1]]}
    ag[g] = {"name": g, "tile": tile, "order": order, "files": files}
    groups.append(g)
    w(f"assets/{g}/README.md", readmes[g] + "\n")
index = {"v": 3, "layout": "files", "createdOnFiles": {"v": 1, "at": NOW}, "title": "Premier Service", "namespace": "PremierService",
 "libraries": [], "sections": {}, "groups": groups, "assetGroups": ag, "blobs": {}, "docs": {"readme": "project/README.md", "sections": []},
 "lastChange": {"by": "Abdes", "at": NOW, "via": "Claude", "note": "Système de marque Premier Service, saison 1, avec le partenaire Les Argonautes."}}
w("design-system.json", json.dumps(index, ensure_ascii=False, indent=1))
print("ok")
