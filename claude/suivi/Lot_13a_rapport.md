# Lot 13a — Rapport : l'atelier dans tous les modes (V1.1.1)

- **Révision** : `R2026-11-15y`, publiée comme **V1.1.1** le 25 novembre 2026.
- **Branche** : `lot-13a`.
- **Décision** : « Corrections d'abord. Pas de run direct. » après les résultats de l'étape 1 du lot 13 (`Pilot_final/protocole.md`).
- **Runs** : aucun pour cette correction. L'étape 2 attend la décision de Junior.

## 1. La cause corrigée

- **Constat** (étape 1) : le widget refait avec la V1.1.0, parti en mode STANDARD, gagne en fonction mais perd en retenue (trois colonnes denses, couleurs multipliées).
- **Cause probable, vérifiée dans les transcriptions** : l'agent n'a pas ouvert l'atelier (`ACTION/ATELIER-EDITION`). La ligne d'invariant écrite en 11c le réservait aux surfaces `DIRECTION`. En `l`, le bloc entier était au noyau et se lisait dans tous les modes : l'agent `l` du même objet parle du test de retrait 12 fois, l'agent V1.1.0 deux fois, et sa trace n'en dit rien.
- **C'est une régression que j'ai introduite en 11c** : la ligne a recopié la portée écrite du bloc (`DIRECTION`), sans voir que le bloc au noyau servait de fait tous les modes.

## 2. Ce qui change

| Où | Changement |
|---|---|
| Ligne du noyau « Atelier sur capture » | « Sur une surface `DIRECTION`, **ou dès que la décision visuelle est ouverte, quel que soit le mode**, après la première capture… » |
| Route `ACTION/ATELIER-EDITION` | Même portée pour le tour d'atelier et pour la **passe de finition**. L'exigence du scope de B1b ne change pas. |
| Garde CORE-01 | Protège la nouvelle formulation au noyau. |
| Version | **V1.1.1** (correctif) : manifeste, README (et sa version anglaise), notes et fiche de version, guide 3, citation, cartes ; `CHANGELOG.md` gagne l'entrée V1.1.1 (« Corrigé », « Mesuré »). |
| Carnet de goût (suivi) | Le jugement de l'étape 1 et la cause 3 (la serif italique jugée « modale » par l'agent), notée comme spécimen de goût, pas comme règle. |

Noyau : 31 057 → 31 127 octets (sur 31 500).

## 3. Mutation rouge

Ancienne portée remise dans la ligne du noyau : CORE-01 refuse le noyau ; rouges `test_current_core_carries_its_floor`, `test_compiled_resource_relays_cannot_disappear`, `test_core_names_the_trace_check`.

## 4. Préparation et livraison

À compléter.

## 5. Ce que cette correction ne prouve pas

- Que l'agent STANDARD fera vraiment le test de retrait : seul un run le dira. L'étape 2 (objet neuf, mode DIRECTION) ne le vérifie pas en STANDARD ; un run STANDARD dédié coûterait un run de plus.
- La cause 3 (typographie) n'est pas corrigée : c'est un goût, noté au carnet.
