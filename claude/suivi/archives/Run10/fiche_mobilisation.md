# Fiche de mobilisation

Présent dans le contexte à chaque run : le noyau de la skill. Les appels ci-dessous sont observés : une route « servie » a été affichée par le lecteur, ce qui ne prouve pas qu'elle a été lue. La conséquence et la preuve restent à établir sur la trace et l'artefact.

Catégories de lecture (`DIRECTION/LECTURE-INSTRUMENTEE`) : `STARTUP-NOMINAL` (recommandé avant la première décision), `CONDITIONAL-READ` (ouvert sur une condition du brief ou du risque), `AUDIT-READ` (contrôle du corpus, jamais compté pour le run), `ACTUAL-READ` (effectivement lu). Ce journal sert de base à `ACTUAL-READ`, sans le prouver.

| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |
|---|---|---|---|---|---|
| 1 | 14:37:04 | `DIRECTION/START/TREE` | sortie redirigée vers un fichier : lecture non observée | | |
| 2 | 14:37:07 | `ACTION/RUN-DIRECTION` | écrite dans un fichier (`--fichier`, 2065 car.) : lecture non observée | | |
| 2 | 14:37:07 | `DIRECTION/CREATIVE-BOOT` | écrite dans un fichier (`--fichier`, 2490 car.) : lecture non observée | | |
| 2 | 14:37:07 | `DIRECTION/VISUAL_TARGET` | écrite dans un fichier (`--fichier`, 5944 car.) : lecture non observée | | |
| 2 | 14:37:07 | `DIRECTION/FIRST-OBJECT` | écrite dans un fichier (`--fichier`, 5621 car.) : lecture non observée | | |
| 2 | 14:37:07 | `SAVOIR/TYPE` | écrite dans un fichier (`--fichier`, 4497 car.) : lecture non observée | | |
| 2 | 14:37:07 | `ACTION/FIRST-RENDER` | écrite dans un fichier (`--fichier`, 1879 car.) : lecture non observée | | |
| 2 | 14:37:07 | `ACTION/GATE-A/CONTROLES` | écrite dans un fichier (`--fichier`, 4557 car.) : lecture non observée | | |
| 2 | 14:37:07 | `BIBLIOTHEQUE/SEQUENCE` | écrite dans un fichier (`--fichier`, 4345 car.) : lecture non observée | | |
| 3 | 14:37:12 | `DIRECTION/EXTERNAL-START` | sortie redirigée vers un fichier : lecture non observée | | |
| 4 | 14:37:16 | parcours sur `--help` | exécuté | | |
| 5 | 14:37:16 | `SAVOIR/TOOLS/MOYENS` | sortie redirigée vers un fichier : lecture non observée | | |
| 6 | 14:37:23 | `SAVOIR/SOURCE` | sortie redirigée vers un fichier : lecture non observée | | |
| 7 | 14:37:31 | `SAVOIR/TYPE-VOIX` | sortie redirigée vers un fichier : lecture non observée | | |
| 8 | 14:37:31 | `SAVOIR/TOOLS/CONVERGENCE` | sortie redirigée vers un fichier : lecture non observée | | |
| 9 | 14:37:35 | `SAVOIR/CRAFT/CFT-01` | servie (6738 car.) | | |
| 10 | 14:38:05 | parcours references sur `references --help` | exécuté | | |
| 11 | 14:38:05 | parcours tirage sur `tirage --help` | exécuté | | |
| 12 | 14:38:05 | parcours verifier sur `verifier --help` | exécuté, rien à traiter | | |
| 13 | 14:38:08 | parcours tirage sur `tirage` | exécuté | | |
| 14 | 14:40:46 | parcours references sur `references` | exécuté | | |
| 15 | 14:41:23 | parcours polices sur `polices --help` | exécuté | | |
| 16 | 14:41:27 | parcours polices sur `fonts` | exécuté | | |
| 17 | 14:43:03 | planche sur — | exécuté | | |
| 18 | 14:43:11 | planche sur `modale.html`, `a-plan.html`, `b-affiche.html`, `c-ziem.html` | exécuté | | |
| 19 | 14:44:35 | check_render sur `--help` | exécuté, rien à traiter | | |
| 20 | 14:44:35 | parcours polices sur `fonts-final` | exécuté | | |
| 21 | 14:48:51 | check_render sur `les-lueurs.html` | exécuté : RETURN — Chevauchement et troncature de texte ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; savoir proposé : `SAVOIR/TYPE`, `SAVOIR/STATE`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 22 | 14:48:58 | regard sur `les-lueurs.html` | exécuté | | |
| 23 | 14:49:21 | parcours verifier sur `les-lueurs.html` | exécuté : RETURN — Chevauchement et troncature de texte ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; SIGNAL — Masse visuelle, Typographie fine, Habillage de gabarit, Alignement optique, Mouvement, Silhouette | | |
| 24 | 14:49:40 | planche sur `les-lueurs.html`, `retiree.html` | en échec (code 2) | | |
| 25 | 14:49:45 | planche sur `les-lueurs.html`, `retiree.html` | exécuté | | |
| 26 | 14:50:32 | parcours typo sur `typo --help` | exécuté | | |
| 27 | 14:50:32 | parcours typo sur `les-lueurs.html` | exécuté | | |
| 28 | 14:50:37 | parcours captures sur `les-lueurs.html` | exécuté | | |
| 29 | 14:50:50 | parcours typo sur `les-lueurs.html` | exécuté | | |
| 30 | 14:51:28 | check_render sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 31 | 14:51:34 | regard sur `les-lueurs.html` | exécuté | | |
| 32 | 14:51:53 | parcours verifier sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; SIGNAL — Masse visuelle, Habillage de gabarit, Alignement optique, Mouvement | | |
| 33 | 14:52:06 | parcours typo sur `les-lueurs.html` | exécuté | | |
| 34 | 14:52:20 | parcours typo sur `les-lueurs.html` | exécuté | | |
| 35 | 14:52:43 | parcours typo sur `les-lueurs.html` | exécuté | | |
| 36 | 14:52:56 | parcours typo sur `les-lueurs.html` | exécuté | | |
| 37 | 14:53:38 | check_render sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 38 | 14:53:44 | regard sur `les-lueurs.html` | exécuté | | |
| 39 | 14:54:03 | parcours verifier sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; SIGNAL — Masse visuelle, Habillage de gabarit, Mouvement | | |
| 40 | 14:54:55 | parcours typo sur `les-lueurs.html` | exécuté | | |
| 41 | 14:55:29 | check_render sur `les-lueurs.html` | exécuté : RETURN — Chevauchement et troncature de texte ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; savoir proposé : `SAVOIR/TYPE`, `SAVOIR/STATE`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 42 | 14:55:35 | regard sur `les-lueurs.html` | exécuté | | |
| 43 | 14:55:54 | parcours verifier sur `les-lueurs.html` | exécuté : RETURN — Chevauchement et troncature de texte ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; SIGNAL — Masse visuelle, Habillage de gabarit, Mouvement | | |
| 44 | 14:56:02 | parcours typo sur `les-lueurs.html` | exécuté | | |
| 45 | 14:56:35 | check_render sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 46 | 14:56:41 | regard sur `les-lueurs.html` | exécuté | | |
| 47 | 14:57:01 | parcours verifier sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier, Objet de preuve au premier écran (#plan) ; SIGNAL — Masse visuelle, Habillage de gabarit, Mouvement | | |
| 48 | 14:57:30 | parcours trace sur `trace.txt` | exécuté | | |
| 49 | 14:57:43 | parcours trace sur `trace.txt` | exécuté | | |

## Manques

- Tronc DIRECTION servi seulement filtré, jeté ou écrit dans un fichier : `ACTION/RUN-DIRECTION`, `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/TYPE`, `ACTION/FIRST-RENDER`, `ACTION/GATE-A/CONTROLES`, `BIBLIOTHEQUE/SEQUENCE` (lecture non observée).
- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
