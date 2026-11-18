# Cadrage de travail (notes internes, run STANDARD)

RUN: STANDARD · décision : l'écran principal du planning d'accueil (semaine de 6 praticiens, placer/déplacer, annulations, liste d'attente) · risque : erreur de placement ou de déplacement (mauvais praticien, mauvais jour, double réservation) et fatigue sur 8 h · preuve : comparaison de voix typographiques, recette `parcours.py verifier` (1440/768/390), parcours des états critiques au navigateur (création, déplacement, annulation → liste d'attente, annuler l'action) · arrêt : aucun défaut bloquant, états critiques parcourus, captures 1440 et 390 livrées

Classement : TREE q2 non (écran produit, pas de marque ni premier contact demandé) ; q5 oui → STANDARD. Décision visuelle ouverte (aucune charte) → déclaration de direction requise, question de convergence et comparaison de voix. Protection de niveau : contexte santé + prévention d'erreur → pas de LITE/ITER, états et récupération obligatoires.

## Cadrage
- Public : (1) secrétaire d'accueil, grand écran, toute la journée, souvent au téléphone (une main sur le combiné, attention partagée) ; (2) six praticiens, téléphone, entre deux patients (coup d'œil de 10 s).
- JTBD secrétaire : « Pendant que le patient est au téléphone, je trouve un créneau qui lui va, je le pose chez le bon praticien sans me tromper, et quand quelqu'un annule, je comble le trou avec un patient de la liste d'attente. »
- JTBD praticien : « Entre deux patients, je vois qui est le prochain et ce qui a changé dans ma journée. »
- Décision dominante : rendre visibles les trous de la semaine (6 × 6 jours) et faire du comblement d'un créneau libéré un geste court et sûr.
- Preuves : états parcourus (création, conflit, déplacement par glisser ET par clic/clavier, annulation dernière minute, attribution à la liste d'attente, annuler l'action), recette de rendu, contraste calculé.
- Contraintes : pas de charte, pas d'existant ; aucune donnée réelle → tout est exemple marqué ; heure de démonstration fixe (mer. 18 nov. 2026, 10:42) pour des captures stables.
- Hypothèses nommées : séances de 30 min sur une grille de 30 min, bilans de 60 min ; cabinet ouvert 8 h–20 h en semaine, samedi matin pour 2 praticiens ; prévenir le patient se fait par appel/SMS hors de l'écran (case « patient prévenu »).

## Inventaire de portée (une ligne)
Réseau ouvert (Fontsource atteint) ; paquets Python (Playwright/Chromium, Pillow, NumPy, SciPy, fontTools installé) ; icônes Lucide via `parcours.py icones` ; connecteurs du compte (Adobe, Figma, Canva…) non utilisés : demandent l'accord de la personne, absente ; aucune génération d'image (inutile : rien de figuratif, et accord absent) ; aucun fichier fourni.

## Modal, trame
- MODAL (≈ 60 %) : clone de Google Agenda — barre latérale gauche avec mini-calendrier et cases à cocher praticiens, grille semaine horaire avec blocs pastel colorés par praticien, modale « Nouveau RDV », liste d'attente sur une autre page ; blanc + un accent sarcelle « santé », Inter.
- Modale au second degré : tableau de bord « KPI » (taux de remplissage en cartes) au-dessus de l'agenda.
- Trame modale : barre latérale (mini-calendrier + filtres) → grille semaine → modale. Rompue : l'objet qui organise l'écran est le trou, pas le rendez-vous. Ordre : carte de la semaine (6 praticiens × 6 jours, trous et créneaux libérés visibles d'un coup) → agenda du jour en colonnes praticiens (où l'on place et déplace) → rail « À combler » (créneaux libérés + candidats de la liste d'attente) puis la liste d'attente. Gardé : grille horaire verticale par praticien, tiroir latéral, toast d'annulation — conventions que l'œil attend.

## Déclaration de direction
DIRECTION — « Créneaux surlignés »
VISION — La secrétaire voit d'un regard où sont les trous de la semaine des six praticiens ; un créneau libéré par une annulation est surligné comme sur l'agenda papier de l'accueil, avec à côté les patients de la liste d'attente qui peuvent le prendre ; chaque placement ou déplacement se relit en une phrase avant validation et s'annule en un clic.
REGISTRE — base : composition de registre d'accueil (lignes réglées, une colonne par praticien, filets fins, densité tenue) ; modificateur : matière des fournitures de bureau (encre bleue = confirmé, crayon gris pointillé = à confirmer, surligneur jaune = libéré, stylo rouge = conflit). Marqueurs visibles : (1) bande de surligneur jaune sur les créneaux libérés, dans la carte et dans l'agenda ; (2) séance « à confirmer » en contour pointillé gris crayon contre filet d'encre bleue pour la séance confirmée.
NIVEAU — qu'on prenne la capture 1440 pour celle d'un logiciel métier en production : ~150 séances/semaine à leur vraie densité, heures alignées, aucun contrôle au style par défaut du navigateur.
ASSET — aucun asset figuratif ; l'objet principal est codé : carte de la semaine (occupation par demi-heure) et agenda du jour, données d'exemple marquées.
COMPOSANT — grille horaire 8 h–20 h par praticien ; bouton primaire « Nouveau rendez-vous » ; recherche patient (touche /) ; tiroir latéral droit pour créer, consulter, annuler ; bandeau de déplacement + confirmation ; toast « Annuler l'action » en bas à gauche ; navigation semaine ‹ › Aujourd'hui.
FINITION — rayons 6 px (séances) dans panneaux 10 px ; filets 1 px ; trois gris teintés chauds (texte, secondaire, filet) ; heures en chiffres tabulaires alignées ; icônes Lucide seule famille 16 px ; focus anneau encre bleue 2 px décalé.
MOUVEMENT — un seul moment : à l'annulation, le surlignage s'étend sur le créneau (≈ 300 ms) et la carte « À combler » entre dans le rail ; retours de geste ≤ 150 ms ; aucun fondu de section ; sous mouvement réduit, surlignage immédiat.
MOBILE — à 390 px, l'écran devient « Ma journée » d'un praticien : la prochaine séance en tête (heure en grand), la liste du jour, les changements depuis le matin écrits en clair (annulé, ajouté, déplacé) ; la semaine devient une rangée de jours avec le nombre de séances ; créneaux libérés et liste d'attente en dessous.

Relecture contre n'importe quel brief semblable : « grille horaire + tiroir + toast » se retrouverait partout → gardé volontairement (convention), mais la couleur par praticien (réflexe du modal) est retirée : la couleur ne code que l'état (encre/crayon/surligneur/rouge), le praticien est porté par la colonne et le nom. Changé : la vision citait d'abord « un planning clair » → remplacé par le trou et le surligneur, propres au métier d'accueil.

Thèse : ce que la secrétaire veut savoir (« où y a-t-il de la place, et qui peut prendre ce trou ? ») → objet : carte de la semaine + créneau surligné avec ses candidats → geste : « Placer ici » puis confirmer la phrase de récapitulation.
