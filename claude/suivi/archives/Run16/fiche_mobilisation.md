# Fiche de mobilisation

Présent dans le contexte à chaque run : le noyau de la skill. Les appels ci-dessous sont observés : une route « servie » a été affichée par le lecteur, ce qui ne prouve pas qu'elle a été lue. La conséquence et la preuve restent à établir sur la trace et l'artefact.

Catégories de lecture (`DIRECTION/LECTURE-INSTRUMENTEE`) : `STARTUP-NOMINAL` (recommandé avant la première décision), `CONDITIONAL-READ` (ouvert sur une condition du brief ou du risque), `AUDIT-READ` (contrôle du corpus, jamais compté pour le run), `ACTUAL-READ` (effectivement lu). Ce journal sert de base à `ACTUAL-READ`, sans le prouver.

| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |
|---|---|---|---|---|---|
| 1 | 07:14:18 | `DIRECTION/START/TREE` | sortie redirigée vers un fichier : lecture non observée | | |
| 2 | 07:14:21 | `ACTION/RUN-DIRECTION` | écrite dans un fichier (`--fichier`, 2065 car.) : lecture non observée | | |
| 2 | 07:14:21 | `DIRECTION/CREATIVE-BOOT` | écrite dans un fichier (`--fichier`, 2490 car.) : lecture non observée | | |
| 2 | 07:14:21 | `DIRECTION/VISUAL_TARGET` | écrite dans un fichier (`--fichier`, 5944 car.) : lecture non observée | | |
| 2 | 07:14:21 | `DIRECTION/FIRST-OBJECT` | écrite dans un fichier (`--fichier`, 5621 car.) : lecture non observée | | |
| 2 | 07:14:21 | `SAVOIR/TYPE` | écrite dans un fichier (`--fichier`, 4497 car.) : lecture non observée | | |
| 2 | 07:14:21 | `ACTION/FIRST-RENDER` | écrite dans un fichier (`--fichier`, 1879 car.) : lecture non observée | | |
| 2 | 07:14:21 | `ACTION/GATE-A/CONTROLES` | écrite dans un fichier (`--fichier`, 4557 car.) : lecture non observée | | |
| 2 | 07:14:21 | `BIBLIOTHEQUE/SEQUENCE` | écrite dans un fichier (`--fichier`, 4345 car.) : lecture non observée | | |
| 3 | 07:14:32 | `ACTION/UI-UX-REALITY` | sortie redirigée vers un fichier : lecture non observée | | |
| 4 | 07:14:32 | `SAVOIR/TYPE-VOIX` | sortie redirigée vers un fichier : lecture non observée | | |
| 5 | 07:14:32 | parcours tirage sur `tirage` | exécuté | | |
| 6 | 07:14:36 | `SAVOIR/TOOLS/MOYENS` | sortie redirigée vers un fichier : lecture non observée | | |
| 7 | 07:14:36 | `SAVOIR/TOOLS/CONVERGENCE` | sortie redirigée vers un fichier : lecture non observée | | |
| 8 | 07:16:11 | parcours references sur `references` | exécuté | | |
| 9 | 07:16:47 | parcours references sur `references2` | exécuté | | |
| 10 | 07:17:26 | parcours polices sur `esquisses` | exécuté | | |
| 11 | 07:19:13 | planche sur `modale.html`, `c.html`, `d.html`, `e.html` | exécuté | | |
| 12 | 07:20:59 | parcours polices sur `billet` | exécuté | | |
| 13 | 07:23:01 | parcours captures sur `billet.html` | exécuté | | |
| 14 | 07:23:40 | parcours captures sur `billet.html` | exécuté | | |
| 15 | 07:24:05 | check_render sur `billet.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT` | | |
| 16 | 07:24:12 | regard sur `billet.html` | exécuté | | |
| 17 | 07:24:28 | parcours verifier sur `billet.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni ; SIGNAL — Masse visuelle, Typographie fine, Habillage de gabarit | | |
| 18 | 07:24:43 | `SAVOIR/STATE` | sortie redirigée vers un fichier : lecture non observée | | |
| 19 | 07:25:12 | parcours typo sur `billet.src.html` | exécuté | | |
| 20 | 07:25:22 | parcours captures sur `billet.html` | exécuté | | |
| 21 | 07:25:24 | parcours captures sur `retrait.html` | exécuté | | |
| 22 | 07:26:33 | parcours captures sur `billet.html` | exécuté | | |
| 23 | 07:27:06 | parcours mouvement sur `billet.html` | exécuté | | |
| 24 | 07:27:12 | parcours mouvement sur `billet.html` | exécuté | | |
| 25 | 07:27:40 | check_render sur `billet.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT` | | |
| 26 | 07:27:44 | regard sur `billet.html` | exécuté | | |
| 27 | 07:27:59 | parcours verifier sur `billet.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni | | |
| 28 | 07:29:13 | check_render sur `billet.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT` | | |
| 29 | 07:29:18 | regard sur `billet.html` | exécuté | | |
| 30 | 07:29:30 | parcours verifier sur `billet.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni | | |
| 31 | 07:30:32 | parcours trace sur `trace.md` | exécuté | | |

## Manques

- Tronc DIRECTION servi seulement filtré, jeté ou écrit dans un fichier : `ACTION/RUN-DIRECTION`, `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/TYPE`, `ACTION/FIRST-RENDER`, `ACTION/GATE-A/CONTROLES`, `BIBLIOTHEQUE/SEQUENCE` (lecture non observée).
- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
