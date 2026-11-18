# Fiche de mobilisation

Présent dans le contexte à chaque run : le noyau de la skill. Les appels ci-dessous sont observés : une route « servie » a été affichée par le lecteur, ce qui ne prouve pas qu'elle a été lue. La conséquence et la preuve restent à établir sur la trace et l'artefact.

Catégories de lecture (`DIRECTION/LECTURE-INSTRUMENTEE`) : `STARTUP-NOMINAL` (recommandé avant la première décision), `CONDITIONAL-READ` (ouvert sur une condition du brief ou du risque), `AUDIT-READ` (contrôle du corpus, jamais compté pour le run), `ACTUAL-READ` (effectivement lu). Ce journal sert de base à `ACTUAL-READ`, sans le prouver.

| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |
|---|---|---|---|---|---|
| 1 | 16:26:07 | `DIRECTION/START/TREE` | servie (3522 car.) | | |
| 2 | 16:26:13 | `ACTION/RUN-STANDARD` | écrite dans un fichier (`--fichier`, 1349 car.) : lecture non observée | | |
| 2 | 16:26:13 | `ACTION/GATE-A/CONTROLES` | écrite dans un fichier (`--fichier`, 4557 car.) : lecture non observée | | |
| 2 | 16:26:13 | `ACTION/GATE-B/B2` | écrite dans un fichier (`--fichier`, 1176 car.) : lecture non observée | | |
| 3 | 16:26:21 | `ACTION/UI-UX-REALITY` | sortie redirigée vers un fichier : lecture non observée | | |
| 4 | 16:26:21 | `SAVOIR/CRAFT/CFT-05` | sortie redirigée vers un fichier : lecture non observée | | |
| 5 | 16:26:21 | `DIRECTION/FIRST-OBJECT` | sortie redirigée vers un fichier : lecture non observée | | |
| 6 | 16:26:24 | `ACTION/RECETTE-RENDU` | sortie redirigée vers un fichier : lecture non observée | | |
| 7 | 16:26:24 | `ACTION/HANDOFF` | sortie redirigée vers un fichier : lecture non observée | | |
| 8 | 16:26:26 | parcours sur `--help` | exécuté | | |
| 9 | 16:26:33 | `DIRECTION/EXTERNAL-START` | sortie redirigée vers un fichier : lecture non observée | | |
| 10 | 16:26:33 | parcours recette sur `recette` | exécuté | | |
| 11 | 16:26:34 | recherche « graphique » | proposée, non servie : `BIBLIOTHEQUE/MICRO`, `ACTION/ATELIER-EDITION`, `DIRECTION/CHARGE`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/DESIGN-ATLAS`, `SAVOIR/IDENTITY` | | |
| 12 | 16:26:37 | parcours recette sur `recette graphique` | exécuté | | |
| 13 | 16:26:37 | `BIBLIOTHEQUE/MICRO` | servie ; filtre vu dans la commande (`sed -n 1,80p`) | | |
| 14 | 16:27:57 | parcours polices sur `polices --help` | exécuté | | |
| 15 | 16:27:57 | parcours references sur `references --help` | exécuté | | |
| 16 | 16:28:01 | parcours polices sur `polices --etendu` | exécuté | | |
| 17 | 16:31:11 | parcours polices sur `page --integrer` | exécuté | | |
| 18 | 16:38:03 | parcours verifier sur `verifier --help` | exécuté, rien à traiter | | |
| 19 | 16:38:33 | check_render sur `index.html` | exécuté : PASS-WITH-RESERVATION — Défilement horizontal interne, Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; RETURN — Objet de l’état clé dans son cadre (--in-frame) ; savoir proposé : `SAVOIR/CONTEXT`, `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/STATE` | | |
| 20 | 16:38:44 | regard sur `index.html` | exécuté | | |
| 21 | 16:38:59 | parcours verifier sur `index.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Défilement horizontal interne, Contraste du texte sur fond uni, Parcours clavier ; SIGNAL — fond beige ou crème, Masse visuelle, Accent, Typographie fine, Habillage de gabarit, Gestion du vide, Alignement optique, Mouvement, Ordre de tabulation | | |
| 22 | 16:41:10 | parcours trace sur `trace.md` | exécuté | | |
| 23 | 16:41:23 | parcours trace sur `trace.md` | exécuté | | |
| 24 | 16:41:30 | parcours trace sur `trace.md` | exécuté | | |
| 25 | 16:41:48 | check_render sur `index.html` | exécuté : PASS-WITH-RESERVATION — Défilement horizontal interne, Contraste du texte sur fond uni, Nom accessible des contrôles (candidats DOM), Parcours clavier ; RETURN — Objet de l’état clé dans son cadre (--in-frame) ; savoir proposé : `SAVOIR/CONTEXT`, `ACTION/VISUAL_PROOF`, `SAVOIR/CRAFT/CFT-05`, `SAVOIR/CRAFT/CFT-03`, `SAVOIR/STATE` | | |
| 26 | 16:41:57 | regard sur `index.html` | exécuté | | |
| 27 | 16:42:12 | parcours verifier sur `index.html` | exécuté : RETURN — Objet de l’état clé dans son cadre (--in-frame) ; PASS-WITH-RESERVATION — Défilement horizontal interne, Contraste du texte sur fond uni, Parcours clavier ; SIGNAL — fond beige ou crème, Masse visuelle, Accent, Habillage de gabarit, Gestion du vide, Mouvement, Ordre de tabulation | | |

## Manques

- Tronc STANDARD servi seulement filtré, jeté ou écrit dans un fichier : `ACTION/RUN-STANDARD`, `ACTION/GATE-A/CONTROLES`, `ACTION/GATE-B/B2` (lecture non observée).
- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
