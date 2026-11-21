# Trace — billet électronique « Gyre au Rotonde » (trace légère, design-governance-practice)

RUN: DIRECTION · décision : le premier écran du billet présenté à l’entrée, et ce qui le rend gardable · risque : billet interchangeable (carte sombre, dégradé, grille d’infos) ou code mal lu au scan · preuve : planche à quatre, atelier (sans texte, retrait, matière), `parcours.py verifier` ×3, QR décodé sur capture · arrêt : code décodé à ×1, ×2, ×3 et agrandi, place lue au premier écran, aucun signal sans correction
DIRECTION DÉCLARÉE ET THÈSE: « L’anneau du balcon » : en un regard, Camille voit sa place dans la salle ronde (rang F tracé, siège 12 allumé, porte B) et le code à présenter, et c’est ce plan qu’on garde ; registre : composition radiale de plan × deux encres sur carton teinté (anneau rouge du rang F, bandeau F/12/B entre filets) ; mouvement : l’anneau se trace puis le siège s’allume, une fois ; lignes non vues : aucune ; où je vais ? → plan calculé et bandeau de place → présenter le code (Agrandir)
MODAL, TRAME ET PARTI: modale (p 0,40) carte Wallet sombre, dégradé violet, Inter, grille à libellés mono capitales, QR en bas ; second degré : talon rétro crème (vague 2), non esquissé ; planche : salle ronde (0,07), gaufrier BD (tirage, 0,05), tableau à volets (0,10) ; gardée : la salle ronde, seule à dire « où je vais » ; elle perd la chaleur locale du gaufrier ; trame image → artiste → infos → code, rompue : le plan porte le titre, code au premier écran ; titre Unbounded contre Bricolage et Fraunces ; marqueurs relevés : aucun
PLAFOND, ESSAIS ET CONTENUS MARQUÉS: portée : connecteurs et génération exclus par la demande, web libre, pip ; typo atteinte (Unbounded, Atkinson Hyperlegible, OFL, intégrées) ; code atteint (segno, décodé par OpenCV) ; photo d’artiste exclue (artiste inventé), plan codé à la place ; références : billets Commodore et Printers’ Fair (Fonts In Use), HIG Wallet, plan de l’Odéon (Commons, CC0) ; Commons refuse 2 requêtes (429) ; artiste, porte, accès, licence et code marqués exemple ; « dimanche » imprimé : le 14/03/2027 n’est pas un samedi
DÉFAUT DOMINANT RESTANT: aucun bloquant ; ce qui retient : le plan et l’anneau du rang F ; ce qui reste générique : les listes « Votre billet » et « Conditions », ordinaires de billetterie ; geste de `SAVOIR/STATE` appliqué et recapturé : masse visuelle (scène allégée, anneau F plein, siège grossi ; la scène sort des quatre foyers, le « 12 » y entre) ; retrait : « votre place » retiré, encoches et sceau gardés ; grain contre aplat : aplat gardé
PROCHAINE PREUVE: scan réel du code par un lecteur de contrôle d’accès, sur trois téléphones, luminosité automatique, dans un hall sombre ; puis le vrai plan du Rotonde

---

## Annexe (notes de travail, hors des six lignes)

Direction déclarée, ligne par ligne, avec ce que la capture montre :
- NIVEAU — qu’on prenne la capture pour l’écran d’une billetterie de salle soignée, et le plan pour un objet imprimé qu’on garde : vu (captures à ×2).
- ASSET — plan du Rotonde calculé en SVG (anneau de balcon A–H, allées, parterre, scène, porte B), marqué « Plan indicatif » : vu.
- COMPOSANT — date en haut à droite (convention Wallet), code sur blanc avec 4 modules de zone de silence, numéro en clair sous le code, bouton « Agrandir le code » (plein écran blanc, focus sur « Fermer », Échap), ajout à l’agenda (.ics généré sur place) : vu et testé.
- FINITION — coins droits, encoches de perforation, filets de 1,5 et 3 px dans l’encre, un seul rouge pour un seul rôle (le siège), six paliers de taille, espaces insécables et apostrophes typographiques : vu.
- MOUVEMENT — l’anneau du rang F se trace (1,1 s), puis le siège s’allume avec une onde et l’étiquette F12 apparaît ; avec le mouvement réduit, l’état final s’affiche directement (vérifié) : vu sur la planche de mouvement.
- MOBILE — 390 px est la largeur native ; au bureau, le billet reste une colonne de 400 px sur la nuit de la salle : vu.

Références (consultées le 2026-11-19) :
- The Commodore tickets, fontsinuse.com/uses/8019 (consultation, tous droits réservés) : change la décision → une encre sur carton teinté, « Doors / Showtime » en couple d’heures, mentions courtes ; ne se transfère pas : corps minuscule, pastiche de caractères anciens.
- 2026 Bay Area Printers’ Fair Souvenir Ticket, fontsinuse.com/uses/75847 (consultation) : change → le billet comme objet souvenir, perforation du talon ; ne se transfère pas : mélange de caractères en bois, rétro.
- Apple Human Interface Guidelines, Wallet, developer.apple.com (consultation) : change → date en haut à droite, code sur fond clair en bas, contraste des libellés ; ne se transfère pas : la grille de champs générique et la photo floue.
- Plans de la salle de l’Odéon, Charles de Wailly, 1770–1771, Wikimedia Commons, CC0 : change → le plan de salle comme objet de beauté en traits ; ne se transfère pas : la gravure (marqueur de vague 3).

Hypothèses et contenus marqués : artiste « Gyre » (trio de musique répétitive, tournée « Révolutions »), porte B et chemin d’accès, plan de la salle, organisateur et licence PLATESV, contenu du code (« RTD-EXEMPLE|2027-0314-00412|BAL-F-12|BERNARD C »), tous indiqués à l’écran dans l’encadré « Maquette ».
Coût : 3 passes de `verifier`, 0 génération d’image, 6 références capturées (2 refusées par Commons).
