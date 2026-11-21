# Fiche de mobilisation

Présent dans le contexte à chaque run : le noyau de la skill. Les appels ci-dessous sont observés : une route « servie » a été affichée par le lecteur, ce qui ne prouve pas qu'elle a été lue. La conséquence et la preuve restent à établir sur la trace et l'artefact.

Catégories de lecture (`DIRECTION/LECTURE-INSTRUMENTEE`) : `STARTUP-NOMINAL` (recommandé avant la première décision), `CONDITIONAL-READ` (ouvert sur une condition du brief ou du risque), `AUDIT-READ` (contrôle du corpus, jamais compté pour le run), `ACTUAL-READ` (effectivement lu). Ce journal sert de base à `ACTUAL-READ`, sans le prouver.

| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |
|---|---|---|---|---|---|
| 1 | 16:29:36 | `DIRECTION/START/TREE` | sortie redirigée vers un fichier : lecture non observée | | |
| 2 | 16:29:41 | `ACTION/RUN-STANDARD` | écrite dans un fichier (`--fichier`, 1349 car.) : lecture non observée | | |
| 2 | 16:29:41 | `ACTION/GATE-A/CONTROLES` | écrite dans un fichier (`--fichier`, 4557 car.) : lecture non observée | | |
| 2 | 16:29:41 | `ACTION/GATE-B/B2` | écrite dans un fichier (`--fichier`, 1176 car.) : lecture non observée | | |
| 3 | 16:29:48 | `ACTION/UI-UX-REALITY` | sortie redirigée vers un fichier : lecture non observée | | |
| 4 | 16:29:48 | `BIBLIOTHEQUE/SELECT` | sortie redirigée vers un fichier : lecture non observée | | |
| 5 | 16:29:51 | `SAVOIR/CONTEXT` | sortie redirigée vers un fichier : lecture non observée | | |
| 6 | 16:29:52 | recherche « MICRO » | proposée, non servie : `BIBLIOTHEQUE/MICRO`, `BIBLIOTHEQUE/SELECT`, `BIBLIOTHEQUE/READ`, `SAVOIR/CRAFT/CFT-06`, `BIBLIOTHEQUE/COMPAT`, `DIRECTION/START/TREE` | | |
| 7 | 16:29:54 | `BIBLIOTHEQUE/MICRO` | sortie redirigée vers un fichier : lecture non observée | | |
| 8 | 16:29:54 | read_route --sommaire SAVOIR/STATE | code 0, rien servi | | |
| 9 | 16:29:59 | `SAVOIR/STATE` | sortie redirigée vers un fichier : lecture non observée | | |
| 10 | 16:29:59 | `SAVOIR/TYPE-VOIX` | sortie redirigée vers un fichier : lecture non observée | | |
| 11 | 16:30:13 | recherche « Références à observer » | proposée, non servie : `SAVOIR/TOOLS/MOYENS`, `DIRECTION/STANDARD` | | |
| 12 | 16:30:15 | `SAVOIR/TOOLS/MOYENS` | servie (7097 car.) | | |
| 13 | 16:31:27 | `SAVOIR/CRAFT/CFT-05` | servie (6672 car.) | | |
| 14 | 16:31:27 | `SAVOIR/CRAFT/CFT-06` | servie (6780 car.) | | |
| 15 | 16:31:33 | parcours polices sur `fonts-test` | exécuté | | |
| 16 | 16:34:05 | parcours polices sur `plex` | exécuté | | |
| 17 | 16:34:07 | parcours icones sur `work` | exécuté | | |
| 18 | 16:42:22 | `ACTION/RECETTE-RENDU` | servie (10808 car.) | | |
| 19 | 16:42:47 | check_render sur `planning-kine.html` | exécuté : RETURN — Chevauchement et troncature de texte, Objet de l’état clé dans son cadre (--in-frame), Objet de preuve au premier écran (#mapPanel) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; savoir proposé : `SAVOIR/TYPE`, `SAVOIR/STATE`, `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 20 | 16:42:52 | regard sur `planning-kine.html` | exécuté | | |
| 21 | 16:43:06 | parcours verifier sur `planning-kine.html` | exécuté : RETURN — Chevauchement et troncature de texte, Objet de l’état clé dans son cadre (--in-frame), Objet de preuve au premier écran (#mapPanel) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; SIGNAL — Cohérence de rayon, Surface, Masse visuelle, Accent, Typographie fine, Habillage de gabarit, Mouvement, Silhouette | | |
| 22 | 19:30:59 | check_render sur `planning-kine.html` | exécuté : RETURN — Chevauchement et troncature de texte, Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; savoir proposé : `SAVOIR/TYPE`, `SAVOIR/STATE`, `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT` | | |
| 23 | 19:31:03 | regard sur `planning-kine.html` | exécuté | | |
| 24 | 19:31:13 | parcours verifier sur `planning-kine.html` | exécuté : RETURN — Chevauchement et troncature de texte, Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Parcours clavier ; SIGNAL — Cohérence de rayon, Surface, Masse visuelle, Accent, Habillage de gabarit, Mouvement, Silhouette | | |
| 25 | 19:31:49 | check_render sur `planning-kine.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; savoir proposé : `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `SAVOIR/STATE` | | |
| 26 | 19:31:52 | regard sur `planning-kine.html` | exécuté | | |
| 27 | 19:32:02 | parcours verifier sur `planning-kine.html` | exécuté : PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; SIGNAL — Masse visuelle, Habillage de gabarit, Mouvement | | |
| 28 | 19:32:31 | parcours typo sur `planning-kine.html` | exécuté | | |
| 29 | 19:33:48 | check_render sur `planning-kine.html` | exécuté : RETURN — Chevauchement et troncature de texte, Objet de l’état clé dans son cadre (--in-frame), Objet de preuve au premier écran (#mapPanel) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; savoir proposé : `SAVOIR/TYPE`, `SAVOIR/STATE`, `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/CONTEXT`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT/CFT-04a` | | |
| 30 | 19:33:53 | regard sur `planning-kine.html` | exécuté | | |
| 31 | 19:34:06 | parcours verifier sur `planning-kine.html` | exécuté : RETURN — Chevauchement et troncature de texte, Objet de l’état clé dans son cadre (--in-frame), Objet de preuve au premier écran (#mapPanel) ; PASS-WITH-RESERVATION — Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; SIGNAL — Cohérence de rayon, Surface, Accent, Habillage de gabarit, Mouvement, Silhouette | | |
| 32 | 19:34:37 | parcours trace sur `trace.md` | exécuté | | |
| 33 | 19:34:42 | parcours trace sur `trace.md` | exécuté | | |
| 34 | 19:34:48 | parcours trace sur `trace.md` | exécuté | | |

## Manques

- Tronc STANDARD servi seulement filtré, jeté ou écrit dans un fichier : `ACTION/RUN-STANDARD`, `ACTION/GATE-A/CONTROLES`, `ACTION/GATE-B/B2` (lecture non observée).
- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
