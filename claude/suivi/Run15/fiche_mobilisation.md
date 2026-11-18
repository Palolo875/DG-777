# Fiche de mobilisation

Présent dans le contexte à chaque run : le noyau de la skill. Les appels ci-dessous sont observés : une route « servie » a été affichée par le lecteur, ce qui ne prouve pas qu'elle a été lue. La conséquence et la preuve restent à établir sur la trace et l'artefact.

Catégories de lecture (`DIRECTION/LECTURE-INSTRUMENTEE`) : `STARTUP-NOMINAL` (recommandé avant la première décision), `CONDITIONAL-READ` (ouvert sur une condition du brief ou du risque), `AUDIT-READ` (contrôle du corpus, jamais compté pour le run), `ACTUAL-READ` (effectivement lu). Ce journal sert de base à `ACTUAL-READ`, sans le prouver.

| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |
|---|---|---|---|---|---|
| 1 | 19:44:40 | `DIRECTION/START/TREE` | servie ; filtre vu dans la commande (`sed -n`) | | |
| 2 | 19:44:44 | `ACTION/RUN-DIRECTION` | écrite dans un fichier (`--fichier`, 2065 car.) : lecture non observée | | |
| 2 | 19:44:44 | `DIRECTION/CREATIVE-BOOT` | écrite dans un fichier (`--fichier`, 2490 car.) : lecture non observée | | |
| 2 | 19:44:44 | `DIRECTION/VISUAL_TARGET` | écrite dans un fichier (`--fichier`, 5944 car.) : lecture non observée | | |
| 2 | 19:44:44 | `DIRECTION/FIRST-OBJECT` | écrite dans un fichier (`--fichier`, 5621 car.) : lecture non observée | | |
| 2 | 19:44:44 | `SAVOIR/TYPE` | écrite dans un fichier (`--fichier`, 4497 car.) : lecture non observée | | |
| 2 | 19:44:44 | `ACTION/FIRST-RENDER` | écrite dans un fichier (`--fichier`, 1879 car.) : lecture non observée | | |
| 2 | 19:44:44 | `ACTION/GATE-A/CONTROLES` | écrite dans un fichier (`--fichier`, 4557 car.) : lecture non observée | | |
| 2 | 19:44:44 | `BIBLIOTHEQUE/SEQUENCE` | écrite dans un fichier (`--fichier`, 4345 car.) : lecture non observée | | |
| 3 | 19:44:52 | `SAVOIR/SOURCE` | sortie redirigée vers un fichier : lecture non observée | | |
| 4 | 19:45:16 | parcours tirage sur `tirage` | exécuté | | |
| 5 | 19:46:07 | parcours references sur `refs` | exécuté | | |
| 6 | 19:48:11 | parcours polices sur `polices --help` | exécuté | | |
| 7 | 19:48:12 | parcours polices sur `fonts` | exécuté | | |
| 8 | 19:48:55 | planche sur `modale.html`, `a-ecran.html`, `b-generique.html`, `c-feuille.html` | exécuté | | |
| 9 | 19:51:23 | parcours captures sur `page.html` | exécuté | | |
| 10 | 19:52:37 | check_render sur `page.html` | exécuté : RETURN — Débordement horizontal, Chevauchement et troncature de texte, Contraste du texte sur fond uni ; PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM), Contraste de l’indicateur de focus, Objet de preuve au premier écran (.ecran) ; savoir proposé : `SAVOIR/CONTEXT`, `BIBLIOTHEQUE/SEQUENCE`, `SAVOIR/TYPE`, `SAVOIR/STATE`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 11 | 19:52:44 | regard sur `page.html` | exécuté | | |
| 12 | 19:53:03 | parcours verifier sur `page.html` | exécuté : RETURN — Débordement horizontal, Chevauchement et troncature de texte, Contraste du texte sur fond uni ; PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM), Contraste de l’indicateur de focus, Objet de preuve au premier écran (.ecran) ; SIGNAL — serif de caractère ou serif italique, Masse visuelle, Alignement optique, Typographie fine, Habillage de gabarit, Image intégrée | | |
| 13 | 19:54:26 | check_render sur `page.html` | exécuté : PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (.ecran) ; savoir proposé : `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 14 | 19:54:33 | regard sur `page.html` | exécuté | | |
| 15 | 19:54:52 | parcours verifier sur `page.html` | exécuté : PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (.ecran) ; SIGNAL — serif de caractère ou serif italique, Masse visuelle, Alignement optique, Habillage de gabarit, Image intégrée | | |
| 16 | 19:55:05 | planche sur `page.html`, `variante-anybody.html` | exécuté | | |
| 17 | 19:55:14 | parcours polices sur `fonts-int` | exécuté | | |
| 18 | 19:55:51 | check_render sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (.ecran) ; savoir proposé : `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 19 | 19:55:58 | regard sur `les-lueurs.html` | exécuté | | |
| 20 | 19:56:18 | parcours verifier sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM), Objet de preuve au premier écran (.ecran) ; SIGNAL — serif de caractère ou serif italique, Masse visuelle, Alignement optique, Habillage de gabarit, Image intégrée | | |
| 21 | 19:57:14 | check_render sur `les-lueurs.html` | exécuté : PASS-WITH-RESERVATION — Nom accessible des contrôles (candidats DOM) ; savoir proposé : `SAVOIR/CONTEXT` | | |
| 22 | 19:57:30 | parcours trace sur `trace.txt` | exécuté | | |
| 23 | 19:57:37 | parcours trace sur `trace.txt` | exécuté | | |

## Manques

- Tronc DIRECTION servi seulement filtré, jeté ou écrit dans un fichier : `ACTION/RUN-DIRECTION`, `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/TYPE`, `ACTION/FIRST-RENDER`, `ACTION/GATE-A/CONTROLES`, `BIBLIOTHEQUE/SEQUENCE` (lecture non observée).
- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
