# Lot 11a — Rapport : une obligation peut tenir en une ligne

- **Révision** : `R2026-11-15r`, livrée le 21 novembre 2026.
- **Branche** : `lot-11a`.
- **Décision** : « Oui » au document de propositions du lot 11 (`Lot_11_Propositions.md`), sous-lot 11a, option A.
- **Runs** : aucun.

## 1. Ce qui change

**Aucun contenu ne bouge.** Le noyau, les routes et les troncs sont inchangés. Seule la garde des planchers (`REQ-01`, `scripts/validate_structure.py`) accepte une troisième forme.

| Forme | Ce qu'elle garantit |
|---|---|
| `("noyau", bloc)` (existante) | Le bloc entier est compilé au noyau |
| `("tronc", route, modes)` (existante) | La route est lue à chaque run de ces modes |
| **`("ligne", route)`** (nouvelle) | Une ligne du noyau porte l'étiquette `[REQUIS PAR LE MODULE — scope]` **et** nomme la route entre accents graves ; la route existe **et** garde le texte complet de l'obligation |

C'est la condition des sous-lots 11c et 11d. Une obligation pourra quitter le noyau en bloc complet sans cesser d'être lue : sa ligne reste au noyau, son texte reste dans la route.

**La procédure « Ajouter ou modifier une règle »** (`maintenance/README.md`, étape 4) et l'en-tête du validateur décrivent les trois formes.

## 2. Tests et mutations rouges

4 cas dans `test_audit_regressions.py` (classe `PlancherEnLigne`), sur une vraie obligation (`DIRECTION/DIVERGENCE`, « Diverger sur image ») :

| Cas | Mutation qui le fait échouer |
|---|---|
| Ligne valide : aucune erreur | — |
| Ligne sans route → erreur | Vérification de la ligne du noyau retirée : rouge (`test_ligne_sans_route`) |
| Route qui ne garde pas le texte → erreur | Vérification du texte de la route retirée : rouge (`test_route_sans_le_texte`) |
| Route introuvable → erreur | Erreur de route introuvable étouffée : rouge (`test_route_introuvable`) |

## 3. Préparation et livraison

À compléter.

## 4. Suite

Le sous-lot **11b** : l'index complet et compressé des 85 routes.
