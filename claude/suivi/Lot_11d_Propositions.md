# Lot 11d — Propositions : sans outils, sans sous-agent, et ce qui reste à réduire

Rédigé le 21 novembre 2026. Base : `R2026-11-15t` (`master` `3097627`). **Rien n'est intégré** : ce document est à relire. Aucun run.

## 0. Mesure (révision `t`)

| Part du noyau | Octets |
|---|---|
| Index (table des signaux) | 7 383 |
| 12 lignes d'invariant (11c) | ≈ 4 450 |
| 23 blocs gardés tels quels | ≈ 15 900 |
| En-têtes, métadonnées, titres de section | ≈ 2 750 |
| **Total** | **30 502** sur 31 000 |

**Les cinq plus gros blocs gardés** : `TRACE` (2 248), `BRIEF` (1 339), `SORTIE` (1 309), `ABSOLUS` (1 238), `ROLE` (1 195).

**Ce que j'ai relu dans ces blocs.** Ils sont déjà denses. Presque chaque phrase y est une règle, et 14 formulations sont protégées par la garde CORE-01 ou par un test (par exemple « Coût : en une ligne, ce que le run a coûté », « `python3 scripts/parcours.py trace FICHIER` », « fonctions, intégrations et conformités affirmées »).

**Mention d'un sous-agent au noyau** : aucune aujourd'hui. Le « regard séparé » par un second agent est parti avec `BOUCLE-ATELIER` en 11c ; il reste dans sa route, marqué « facultatif ».

## 1. Mon avis sur la réécriture courte

**La cible de 18 000 octets ne vaut pas son prix.**
- Réécrire un bloc gardé change son **texte canonique** : contrairement à 11c, il n'en reste pas de version complète ailleurs.
- La parade serait celle de 11c : une version courte au noyau et le bloc entier dans sa route. Mais ces blocs (trace, sortie, brief) servent à **chaque** run, et leur route (`ACTION/HANDOFF`) n'est pas dans le tronc DIRECTION. La version courte serait alors la seule lue, et elle doit tout garder.
- Gain estimé avec cette parade, sur les quatre plus gros blocs : environ −1 900 octets, soit **−6 %**, au risque de perdre une nuance de la trace ou de la sortie, que seul un run révélerait.

Le noyau est déjà passé de 48 173 à 30 502 octets. Le reste du coût d'un run tient au nombre de tours et aux images (lot 10), pas à ces derniers octets.

## 2. Propositions

### D1 — Le passage « Sans outils » (profil E2 : agent sans exécution de code)

- **A (recommandée).** Un court bloc au noyau, dans la section « Classer, puis charger » (≈ 560 octets) :

> **Sans outils.** Si l'environnement n'exécute pas de code, lis une route en ouvrant le fichier dont un titre porte son code (cherche « `CODE —` » dans les fichiers `.md` du paquet) ; les obligations restent dues. Ce qui demande un script ou une capture (recette de rendu, `verifier`, planche, contraste mesuré) devient `NOT-VERIFIED`, jamais `PASS` : dis-le dans la réponse et nomme le contrôle qui manque. La boucle se fait alors sur le code relu : défaut dominant, modification, relecture. Ne décris jamais un rendu que tu n'as pas vu.

- **B.** Le même texte dans `guides/1-utiliser.md` seulement, hors du noyau. Un agent sans outils ne le lirait pas forcément.

### D2 — Garde « aucune consigne du noyau ne suppose un sous-agent » (SUB-01)

- **A (recommandée).** `validate_structure.py` refuse, dans le noyau compilé, une phrase qui parle d'un sous-agent, d'un second ou autre agent, d'agents séparés ou d'un travail en parallèle, **sauf** si la même phrase la dit facultative ou soumise à l'environnement (« si l'environnement… », « facultatif »).
  - Mutation rouge : une phrase « fais critiquer la page par un second agent » ajoutée au noyau doit être refusée ; la même avec « si l'environnement le permet » doit passer.
- **B.** Une simple relecture, sans garde.

### D3 — La réécriture courte des blocs gardés

- **A (recommandée).** **Ne pas réécrire.** Le budget du noyau **monte légèrement, à 31 500 octets**, pour accueillir D1 (30 502 + ≈ 560 dépasse 31 000), et la mesure se fera en run (lot 13). Si un run montre qu'un bloc n'est pas lu ou qu'il gêne, on le réduira avec la preuve.
- **B.** Version courte au noyau et bloc entier en route (méthode de 11c) pour `TRACE`, `BRIEF`, `SORTIE` et `ROLE` : environ −1 900 octets. Je rédigerais alors les quatre versions courtes pour ta relecture avant toute intégration.

## 3. Ce que ce lot ne prouvera pas

- Qu'un agent sans outils suit le passage : il faudrait un run dans un environnement sans exécution (profil E2).
- Que la garde SUB-01 attrape toutes les formulations : c'est une liste close, comme les autres gardes de formulation.

## 4. Révision prévue

`R2026-11-15u`, avec D1 et D2 (et D3 B si tu la choisis).
