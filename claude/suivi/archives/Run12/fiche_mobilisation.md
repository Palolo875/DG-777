# Fiche de mobilisation

Présent dans le contexte à chaque run : le noyau de la skill. Les appels ci-dessous sont observés : une route « servie » a été affichée par le lecteur, ce qui ne prouve pas qu'elle a été lue. La conséquence et la preuve restent à établir sur la trace et l'artefact.

Catégories de lecture (`DIRECTION/LECTURE-INSTRUMENTEE`) : `STARTUP-NOMINAL` (recommandé avant la première décision), `CONDITIONAL-READ` (ouvert sur une condition du brief ou du risque), `AUDIT-READ` (contrôle du corpus, jamais compté pour le run), `ACTUAL-READ` (effectivement lu). Ce journal sert de base à `ACTUAL-READ`, sans le prouver.

| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |
|---|---|---|---|---|---|
| 1 | 16:29:36 | `DIRECTION/START/TREE` | sortie redirigée vers un fichier : lecture non observée | | |
| 2 | 16:29:38 | `ACTION/RUN-DIRECTION` | écrite dans un fichier (`--fichier`, 2065 car.) : lecture non observée | | |
| 2 | 16:29:38 | `DIRECTION/CREATIVE-BOOT` | écrite dans un fichier (`--fichier`, 2490 car.) : lecture non observée | | |
| 2 | 16:29:38 | `DIRECTION/VISUAL_TARGET` | écrite dans un fichier (`--fichier`, 5944 car.) : lecture non observée | | |
| 2 | 16:29:38 | `DIRECTION/FIRST-OBJECT` | écrite dans un fichier (`--fichier`, 5621 car.) : lecture non observée | | |
| 2 | 16:29:38 | `SAVOIR/TYPE` | écrite dans un fichier (`--fichier`, 4497 car.) : lecture non observée | | |
| 2 | 16:29:38 | `ACTION/FIRST-RENDER` | écrite dans un fichier (`--fichier`, 1879 car.) : lecture non observée | | |
| 2 | 16:29:38 | `ACTION/GATE-A/CONTROLES` | écrite dans un fichier (`--fichier`, 4557 car.) : lecture non observée | | |
| 2 | 16:29:38 | `BIBLIOTHEQUE/SEQUENCE` | écrite dans un fichier (`--fichier`, 4345 car.) : lecture non observée | | |
| 3 | 16:29:44 | `SAVOIR/IDENTITY` | sortie redirigée vers un fichier : lecture non observée | | |
| 4 | 16:29:53 | `SAVOIR/TOOLS/MOYENS` | sortie redirigée vers un fichier : lecture non observée | | |
| 5 | 16:29:53 | `SAVOIR/TYPE-VOIX` | sortie redirigée vers un fichier : lecture non observée | | |
| 6 | 16:30:08 | `SAVOIR/CRAFT/CFT-01` | sortie redirigée vers un fichier : lecture non observée | | |
| 7 | 16:30:08 | parcours tirage sur `tirage` | exécuté | | |
| 8 | 16:30:08 | parcours references sur `references --help` | exécuté | | |
| 9 | 16:31:01 | parcours references sur `references` | exécuté | | |
| 10 | 16:31:42 | parcours references sur `references2` | exécuté | | |
| 11 | 16:32:41 | recherche « Calibration culturelle » | proposée, non servie : `SAVOIR/SOURCE`, `DIRECTION/DIVERGENCE` | | |
| 12 | 16:32:42 | recherche « Construire une atmosphère » | proposée, non servie : `SAVOIR/SOURCE`, `DIRECTION/CREATIVE-BOOT` | | |
| 13 | 16:32:42 | parcours polices sur `polices --help` | exécuté | | |
| 14 | 16:32:59 | parcours polices sur `esquisses` | exécuté | | |
| 15 | 16:34:27 | planche sur `modale.html`, `a-travees.html`, `b-mercuriale.html`, `c-on-rouvre.html` | exécuté | | |
| 16 | 16:34:38 | planche sur `modale.html`, `a-travees.html`, `b-mercuriale.html`, `c-on-rouvre.html` | exécuté | | |
| 17 | 16:35:36 | parcours polices sur `voix` | exécuté | | |
| 18 | 16:36:30 | parcours captures sur `captures --help` | exécuté | | |
| 19 | 16:36:34 | parcours captures sur `voix.html` | exécuté | | |
| 20 | 16:36:39 | parcours captures sur `voix.html` | exécuté | | |
| 21 | 16:37:42 | parcours identite sur `identite --help` | exécuté | | |
| 22 | 16:37:48 | parcours identite sur `epreuve` | exécuté | | |
| 23 | 16:38:36 | parcours polices sur `build` | exécuté | | |
| 24 | 16:42:47 | parcours captures sur `index.html` | exécuté | | |
| 25 | 16:43:22 | parcours captures sur `index.html` | exécuté | | |
| 26 | 16:43:38 | regard sur `affiche.html` | exécuté | | |
| 27 | 16:44:39 | check_render sur `index.html` | exécuté : PASS-WITH-RESERVATION — Chevauchement et troncature de texte, Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (#affiche .poster) ; RETURN — Objet de l’état clé dans son cadre (--in-frame) ; savoir proposé : `SAVOIR/TYPE`, `SAVOIR/STATE`, `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 28 | 16:44:47 | regard sur `index.html` | exécuté | | |
| 29 | 16:45:01 | parcours verifier sur `index.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Chevauchement et troncature de texte, Contraste du texte sur fond uni, Objet de preuve au premier écran (#affiche .poster) ; SIGNAL — fond beige ou crème, orange rouille, libellés mono en capitales, Cumul : 3 marqueurs sur le premier écran., Texte secondaire, Masse visuelle, Alignement optique, Typographie fine, Habillage de gabarit, Mouvement, Silhouette | | |
| 30 | 16:45:25 | planche sur `avec.html`, `sans-marqueurs.html` | exécuté | | |
| 31 | 19:29:17 | parcours typo sur `index.html` | exécuté | | |
| 32 | 19:30:00 | check_render sur `index.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (#affiche .poster) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 33 | 19:30:10 | regard sur `index.html` | exécuté | | |
| 34 | 19:30:24 | parcours verifier sur `index.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Objet de preuve au premier écran (#affiche .poster) ; SIGNAL — fond beige ou crème, orange rouille, libellés mono en capitales, Cumul : 3 marqueurs sur le premier écran., Masse visuelle, Texte secondaire, Habillage de gabarit, Gestion du vide, Mouvement, Silhouette | | |
| 35 | 19:30:48 | parcours captures sur `index.html` | exécuté | | |
| 36 | 19:31:25 | parcours trace sur `trace.txt` | exécuté | | |

## Manques

- Tronc DIRECTION servi seulement filtré, jeté ou écrit dans un fichier : `ACTION/RUN-DIRECTION`, `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/TYPE`, `ACTION/FIRST-RENDER`, `ACTION/GATE-A/CONTROLES`, `BIBLIOTHEQUE/SEQUENCE` (lecture non observée).
- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
