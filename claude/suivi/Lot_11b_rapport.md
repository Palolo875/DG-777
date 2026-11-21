# Lot 11b — Rapport : le noyau indexe toutes les routes

- **Révision** : `R2026-11-15s`, livrée le 21 novembre 2026.
- **Branche** : `lot-11b`.
- **Décision** : « Ok » au sous-lot 11b, option A, avec le plafond du noyau relevé provisoirement (option A de la contrainte signalée dans le rapport 11a).
- **Runs** : aucun.

## 1. Ce qui change

| Mesure | Avant (`r`) | Après (`s`) |
|---|---|---|
| Routes du sommaire citées dans la table des signaux du noyau | 34 sur 85 | **85 sur 85** |
| Taille de la table des signaux (bloc `CHARGE-DETAILS`) | 5 086 octets | **7 383 octets** (cible : 8 000 au plus) |
| Lignes de la table | 27 | 39 |
| Noyau `SKILL.md` | 45 876 / 46 000 octets | **48 173 / 48 500 octets** (plafond provisoire) |

**La forme reste celle d'une table** (`| Signal | Route |`), et non une liste `signal → route` comme proposé. Raison : cinq contrôles existants lisent cette table par ses lignes (LCF-06, LCF-17, SIG-01, la garde de formulation sur « Détail final susceptible », et `validate_reading_map.signal_rows`). Changer la forme les aurait tous cassés pour un gain de quelques centaines d'octets.

**En tête de la table**, la consigne : « Cette table indexe toutes les routes. Lis la route en entier au moment où elle peut changer la décision, plutôt que de t'en remettre à ta mémoire (`python3 scripts/read_route.py CODE`). »

### Les lignes ajoutées ou complétées

| Ligne | Routes ajoutées |
|---|---|
| Mode ou risque dominant à classer ou à reclasser ; delta local presque tranché (nouvelle) | `DIRECTION/START`, `DIRECTION/FAST-PATH`, `ACTION/FAST-PATH`, `SAVOIR/JUGEMENT-COURT`, `BIBLIOTHEQUE/AVANT-SELECTION` |
| Entrée, sortie et préconditions d'un mode (nouvelle) | `ACTION/RUN` et ses quatre `RUN-*`, `ACTION/PRECONDITION` |
| Question sans route évidente (nouvelle) | `ACTION/ROUTING`, `SAVOIR/ROUTING`, `SAVOIR/READ` |
| Décision visuelle ouverte : boot, cible, atelier, divergence et déclaration, cadres (nouvelle) | `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/DIRECTION-ATELIER`, `DIRECTION/DIVERGENCE`, `DIRECTION/CADRES` |
| Forme retenue à construire (nouvelle) | Dix routes `BIBLIOTHEQUE/` : support, grille, séquence, sections, objet, micro, modificateur, compatibilité, signature, dérivation |
| Formulaire ou contrôle de structure (nouvelle) | `BIBLIOTHEQUE/CONTRACTS`, `BIBLIOTHEQUE/GATE` |
| Identité de marque (nouvelle) | `SAVOIR/IDENTITY` |
| Premier rendu ; surface UI/UX nouvelle (nouvelle) | `ACTION/FIRST-RENDER`, `ACTION/UI-UX-REALITY` |
| Gate à passer ; contraste (nouvelle) | `ACTION/GATE-A`, `ACTION/GATE-B`, `ACTION/GATE-C`, `ACTION/POLICIES` |
| Statut ou verdict ; clôture du run (nouvelle) | `ACTION/STATUS`, `ACTION/CLOSE-PACKAGE`, `ACTION/CLOSE-EXIT-CHECK`, `ACTION/RUN_CARD` |
| Run instrumenté ; autonomie, reprise ou limite du service (nouvelle) | `DIRECTION/LECTURE-INSTRUMENTEE`, `ACTION/AUTHORITY`, `DIRECTION/SERVICE-BOUNDARY` |
| Changement d'une règle du système (nouvelle) | `ACTION/MAINTENANCE`, `BIBLIOTHEQUE/EVOLUTION` |
| Direction identitaire ; ancre (complétée) | `DIRECTION/ANCHOR-RESERVE` |
| Revue créative (complétée) | `ACTION/ATELIER-EDITION` |
| Réponse visible, trace complète (complétée) | `ACTION/STRUCTURED-PROOF` |
| Cadrage ambigu (complétée) | `DIRECTION/DOMAIN-FRAME` |

**À relire par Junior** : ces libellés de signal sont ce que l'agent lira pour décider d'ouvrir une route.

## 2. Garde et mutations rouges

**IDX-01** (`validate_structure.py`, garde 26) : la table des signaux, telle que compilée dans `SKILL.md`, cite chaque route du sommaire de `read_route` et tient en 8 000 octets au plus. Une route citée ailleurs dans le noyau ne compte pas.

- Sur l'ancien noyau, avant recompilation, la garde a listé les 51 routes manquantes.
- 5 cas dans `test_audit_regressions.py` (classe `IndexComplet`) :

| Mutation | Résultat |
|---|---|
| Les routes absentes ne sont plus relevées | Rouge : `test_route_absente_signalee`, `test_route_hors_table_ne_compte_pas` |
| La recherche porte sur tout le noyau, pas sur la table | Rouge : `test_route_hors_table_ne_compte_pas`, `test_noyau_reel_complet` |
| Le plafond de 8 000 octets n'est plus vérifié | Rouge : `test_index_trop_long` |

## 3. Le plafond provisoire

- `CORE_BUDGET_BYTES` passe de 46 000 à **48 500**, marqué « provisoire » dans `build_core.py`, `maintenance/README.md`, `maintenance/evolution.md` et `RELEASE_NOTES.md`.
- Les tests du budget lisent désormais la constante au lieu d'écrire 46 000 en dur. Ils gardent leur sens : limite exacte acceptée, un octet de trop refusé, octets UTF-8 comptés.
- **Il redescend en 11c**, sous 25 000 octets si la cible est tenue.

## 4. Préparation et livraison

À compléter.

## 5. Ce que ce sous-lot ne prouve pas

- Qu'un agent ouvrira plus souvent la bonne route : seul un run le dira (lot 13).
- Le noyau grossit de 2 297 octets jusqu'à 11c.
