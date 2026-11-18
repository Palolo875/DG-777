# Fiche de mobilisation

Présent dans le contexte à chaque run : le noyau de la skill. Les appels ci-dessous sont observés : une route « servie » a été affichée par le lecteur, ce qui ne prouve pas qu'elle a été lue. La conséquence et la preuve restent à établir sur la trace et l'artefact.

Catégories de lecture (`DIRECTION/LECTURE-INSTRUMENTEE`) : `STARTUP-NOMINAL` (recommandé avant la première décision), `CONDITIONAL-READ` (ouvert sur une condition du brief ou du risque), `AUDIT-READ` (contrôle du corpus, jamais compté pour le run), `ACTUAL-READ` (effectivement lu). Ce journal sert de base à `ACTUAL-READ`, sans le prouver.

| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |
|---|---|---|---|---|---|
| 1 | 11:56:58 | `DIRECTION/START/TREE` | servie (3522 car.) | | |
| 2 | 11:57:01 | `ACTION/RUN-DIRECTION` | écrite dans un fichier (`--fichier`, 2065 car.) : lecture non observée | | |
| 2 | 11:57:01 | `DIRECTION/CREATIVE-BOOT` | écrite dans un fichier (`--fichier`, 2490 car.) : lecture non observée | | |
| 2 | 11:57:01 | `DIRECTION/VISUAL_TARGET` | écrite dans un fichier (`--fichier`, 5944 car.) : lecture non observée | | |
| 2 | 11:57:01 | `DIRECTION/FIRST-OBJECT` | écrite dans un fichier (`--fichier`, 5621 car.) : lecture non observée | | |
| 2 | 11:57:01 | `SAVOIR/TYPE` | écrite dans un fichier (`--fichier`, 4497 car.) : lecture non observée | | |
| 2 | 11:57:01 | `ACTION/FIRST-RENDER` | écrite dans un fichier (`--fichier`, 1879 car.) : lecture non observée | | |
| 2 | 11:57:01 | `ACTION/GATE-A/CONTROLES` | écrite dans un fichier (`--fichier`, 4557 car.) : lecture non observée | | |
| 2 | 11:57:01 | `BIBLIOTHEQUE/SEQUENCE` | écrite dans un fichier (`--fichier`, 4345 car.) : lecture non observée | | |
| 3 | 11:57:05 | parcours sur `--help` | exécuté | | |
| 4 | 11:57:09 | `DIRECTION/EXTERNAL-START` | servie (4013 car.) | | |
| 5 | 11:57:39 | parcours tirage sur `tirage` | exécuté | | |
| 6 | 11:57:39 | parcours polices sur `polices -h` | exécuté | | |
| 7 | 11:57:40 | parcours references sur `references -h` | exécuté | | |
| 8 | 11:57:40 | parcours verifier sur `verifier -h` | exécuté, rien à traiter | | |
| 9 | 11:57:40 | planche sur — | exécuté | | |
| 10 | 11:57:44 | `SAVOIR/TOOLS/CONVERGENCE` | servie (4154 car.) | | |
| 11 | 11:57:44 | `SAVOIR/TYPE-VOIX` | servie (2445 car.) | | |
| 12 | 11:59:02 | parcours references sur `references` | exécuté | | |
| 13 | 12:00:11 | parcours polices sur `esq` | exécuté | | |
| 14 | 12:01:39 | planche sur `modale.html`, `a-plan.html`, `b-releve.html`, `c-notes.html` | exécuté | | |
| 15 | 12:02:24 | parcours polices sur `typo` | exécuté | | |
| 16 | 12:03:38 | parcours polices sur `final` | exécuté | | |
| 17 | 12:05:12 | `SAVOIR/STATE` | servie ; filtre vu dans la commande (`grep -n -i -A3`) | | |
| 18 | 12:08:42 | parcours captures sur `captures -h` | exécuté | | |
| 19 | 12:08:44 | parcours captures sur `quote-part.html` | exécuté | | |
| 20 | 12:12:27 | check_render sur `-h` | exécuté, rien à traiter | | |
| 21 | 12:13:15 | check_render sur `quote-part.html` | exécuté : RETURN — Chevauchement et troncature de texte ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (#planfig) ; savoir proposé : `SAVOIR/TYPE`, `SAVOIR/STATE`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 22 | 12:13:20 | regard sur `quote-part.html` | exécuté | | |
| 23 | 12:13:36 | parcours verifier sur `quote-part.html` | exécuté : RETURN — Chevauchement et troncature de texte ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (#planfig) ; SIGNAL — Masse visuelle, Accent, Silhouette | | |
| 24 | 12:14:42 | planche sur `v1-anime.html`, `quote-part.html` | exécuté | | |
| 25 | 12:15:25 | check_render sur `quote-part.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (#planfig) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 26 | 12:15:30 | regard sur `quote-part.html` | exécuté | | |
| 27 | 12:15:47 | parcours verifier sur `quote-part.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (#planfig) ; SIGNAL — Masse visuelle, Accent | | |
| 28 | 12:16:08 | parcours typo sur `quote-part.html` | exécuté | | |
| 29 | 12:16:23 | check_render sur `quote-part.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT` | | |
| 30 | 12:18:09 | check_render sur `quote-part.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (#planfig) ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 31 | 12:18:14 | regard sur `quote-part.html` | exécuté | | |
| 32 | 12:18:30 | parcours verifier sur `quote-part.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (#planfig) ; SIGNAL — Masse visuelle, Accent | | |
| 33 | 12:18:49 | parcours trace sur `quote-part.trace.txt` | exécuté | | |

## Manques

- Tronc DIRECTION servi seulement filtré, jeté ou écrit dans un fichier : `ACTION/RUN-DIRECTION`, `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/TYPE`, `ACTION/FIRST-RENDER`, `ACTION/GATE-A/CONTROLES`, `BIBLIOTHEQUE/SEQUENCE` (lecture non observée).
- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
