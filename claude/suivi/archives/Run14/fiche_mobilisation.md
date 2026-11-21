# Fiche de mobilisation

Présent dans le contexte à chaque run : le noyau de la skill. Les appels ci-dessous sont observés : une route « servie » a été affichée par le lecteur, ce qui ne prouve pas qu'elle a été lue. La conséquence et la preuve restent à établir sur la trace et l'artefact.

Catégories de lecture (`DIRECTION/LECTURE-INSTRUMENTEE`) : `STARTUP-NOMINAL` (recommandé avant la première décision), `CONDITIONAL-READ` (ouvert sur une condition du brief ou du risque), `AUDIT-READ` (contrôle du corpus, jamais compté pour le run), `ACTUAL-READ` (effectivement lu). Ce journal sert de base à `ACTUAL-READ`, sans le prouver.

| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |
|---|---|---|---|---|---|
| 1 | 16:29:36 | `DIRECTION/START/TREE` | servie (3522 car.) | | |
| 2 | 16:29:39 | `ACTION/RUN-DIRECTION` | écrite dans un fichier (`--fichier`, 2065 car.) : lecture non observée | | |
| 2 | 16:29:39 | `DIRECTION/CREATIVE-BOOT` | écrite dans un fichier (`--fichier`, 2490 car.) : lecture non observée | | |
| 2 | 16:29:39 | `DIRECTION/VISUAL_TARGET` | écrite dans un fichier (`--fichier`, 5944 car.) : lecture non observée | | |
| 2 | 16:29:39 | `DIRECTION/FIRST-OBJECT` | écrite dans un fichier (`--fichier`, 5621 car.) : lecture non observée | | |
| 2 | 16:29:39 | `SAVOIR/TYPE` | écrite dans un fichier (`--fichier`, 4497 car.) : lecture non observée | | |
| 2 | 16:29:39 | `ACTION/FIRST-RENDER` | écrite dans un fichier (`--fichier`, 1879 car.) : lecture non observée | | |
| 2 | 16:29:39 | `ACTION/GATE-A/CONTROLES` | écrite dans un fichier (`--fichier`, 4557 car.) : lecture non observée | | |
| 2 | 16:29:39 | `BIBLIOTHEQUE/SEQUENCE` | écrite dans un fichier (`--fichier`, 4345 car.) : lecture non observée | | |
| 3 | 16:29:50 | `DIRECTION/EXTERNAL-START` | sortie redirigée vers un fichier : lecture non observée | | |
| 4 | 16:29:50 | `DIRECTION/ASSET-ROUTE` | sortie redirigée vers un fichier : lecture non observée | | |
| 5 | 16:29:52 | `SAVOIR/SOURCE` | servie (22631 car.) | | |
| 6 | 16:30:00 | `SAVOIR/TOOLS/MOYENS` | servie (7097 car.) | | |
| 7 | 16:30:00 | `SAVOIR/TYPE-VOIX` | sortie redirigée vers un fichier : lecture non observée | | |
| 8 | 16:30:06 | parcours sur `--help` | exécuté | | |
| 9 | 16:30:06 | parcours tirage sur `tirage` | exécuté | | |
| 10 | 16:30:11 | parcours recette sur `recette` | exécuté | | |
| 11 | 16:30:11 | parcours references sur `references --help` | exécuté | | |
| 12 | 16:31:02 | parcours references sur `references` | exécuté | | |
| 13 | 16:31:52 | parcours references sur `references2` | exécuté | | |
| 14 | 16:32:06 | parcours references sur `references2` | exécuté | | |
| 15 | 16:32:21 | parcours references sur `references3` | exécuté | | |
| 16 | 16:32:54 | `SAVOIR/TOOLS/CONVERGENCE` | servie (4154 car.) | | |
| 17 | 16:33:42 | parcours polices sur `polices --help` | exécuté | | |
| 18 | 16:33:43 | parcours polices sur `polices Cormorant Garamond:500,500i Young Serif:400 Tenor Sans:400 Hanken Grotesk:400,500,600 Gloock:400` | exécuté | | |
| 19 | 16:35:33 | planche sur — | exécuté | | |
| 20 | 16:35:37 | planche sur `modale.html`, `coupe.html`, `emaux.html`, `semaines.html` | en échec (code 2) | | |
| 21 | 16:35:42 | planche sur `modale.html`, `coupe.html`, `emaux.html`, `semaines.html` | exécuté | | |
| 22 | 16:36:02 | planche sur `modale.html`, `coupe.html`, `emaux.html`, `semaines.html` | exécuté | | |
| 23 | 16:37:00 | parcours polices sur `polices Young Serif:400 Hanken Grotesk:400,500,600 --integrer` | exécuté | | |
| 24 | 16:39:57 | parcours captures sur `captures --help` | exécuté | | |
| 25 | 16:40:01 | parcours captures sur `page.html` | exécuté | | |
| 26 | 16:41:22 | parcours captures sur `page.html` | exécuté | | |
| 27 | 16:42:01 | parcours verifier sur `verifier --help` | exécuté, rien à traiter | | |
| 28 | 16:42:27 | check_render sur `page.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame), Contraste du texte sur fond uni ; PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM), Parcours clavier, Contraste de l’indicateur de focus ; savoir proposé : `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE` | | |
| 29 | 16:42:31 | regard sur `page.html` | exécuté | | |
| 30 | 16:42:44 | parcours verifier sur `page.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame), Contraste du texte sur fond uni ; PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM), Parcours clavier, Contraste de l’indicateur de focus ; SIGNAL — serif de caractère ou serif italique, Masse visuelle, Alignement optique, Typographie fine, Habillage de gabarit, Mouvement | | |
| 31 | 16:43:16 | parcours typo sur `typo --help` | exécuté | | |
| 32 | 16:43:20 | parcours typo sur `gabarit.html` | exécuté | | |
| 33 | 16:43:39 | planche sur `page.html`, `retrait.html` | exécuté | | |
| 34 | 16:44:12 | parcours mouvement sur `page.html` | exécuté | | |
| 35 | 16:44:32 | check_render sur `page.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; savoir proposé : `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE` | | |
| 36 | 16:44:36 | regard sur `page.html` | exécuté | | |
| 37 | 16:44:50 | parcours verifier sur `page.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; SIGNAL — serif de caractère ou serif italique, Habillage de gabarit | | |
| 38 | 16:45:02 | planche sur `page.html`, `voix-tenor.html` | exécuté | | |
| 39 | 16:45:18 | check_render sur `page.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE` | | |
| 40 | 16:45:21 | regard sur `page.html` | exécuté | | |
| 41 | 16:45:31 | parcours verifier sur `page.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; SIGNAL — serif de caractère ou serif italique, Masse visuelle, Habillage de gabarit | | |
| 42 | 19:29:20 | parcours captures sur `page.html` | exécuté | | |
| 43 | 19:30:21 | check_render sur `page.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; savoir proposé : `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE` | | |
| 44 | 19:30:25 | regard sur `page.html` | exécuté | | |
| 45 | 19:30:38 | parcours verifier sur `page.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; SIGNAL — serif de caractère ou serif italique, Habillage de gabarit | | |
| 46 | 19:30:47 | check_render sur `page.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE` | | |
| 47 | 19:30:50 | regard sur `page.html` | exécuté | | |
| 48 | 19:31:00 | parcours verifier sur `page.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; SIGNAL — serif de caractère ou serif italique, Masse visuelle, Habillage de gabarit | | |
| 49 | 19:32:53 | parcours trace sur `trace.txt` | exécuté | | |
| 50 | 19:33:06 | parcours trace sur `trace.txt` | exécuté | | |
| 51 | 19:33:14 | parcours trace sur `trace.txt` | exécuté | | |
| 52 | 19:33:19 | parcours trace sur `trace.txt` | exécuté | | |

## Manques

- Tronc DIRECTION servi seulement filtré, jeté ou écrit dans un fichier : `ACTION/RUN-DIRECTION`, `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/TYPE`, `ACTION/FIRST-RENDER`, `ACTION/GATE-A/CONTROLES`, `BIBLIOTHEQUE/SEQUENCE` (lecture non observée).
- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
