# Lot « outil » — Rapport : une préparation deux fois plus rapide

- **Révision** : `R2026-11-25b`, livrée le 25 novembre 2026 (version publique V1.1.1).
- **Branche** : `lot-outil`.
- **Décision** : « D'accord, P1 P2 P3 d'abord, puis 14c ». P4 (accélérer les suites lentes) n'est pas fait.
- **Runs** : aucun.

## 1. La mesure (avant)

Préparation complète du 25 novembre (`R2026-11-25a`) : **891 s**. Étape par étape : tests avec navigateur 414 s (`parcours` 197, `check_render` 184, `regard` 33) ; build des archives 206 s, dont la suite de tests relancée sur l'export Local ; tests sans navigateur ~100 s ; contrôle de déplacement 44 s ; second build de reproductibilité ; validations ~12 s. Tout s'exécutait l'un après l'autre, sur une machine à 4 cœurs.

## 2. Ce qui change

| Piste | Changement |
|---|---|
| **P1** Parallèle | `validate_all.py` lance les 8 suites de tests (5 sans navigateur, 3 avec) en même temps, au plus une par cœur (`run_parallele`). Les sorties s'affichent dans l'ordre ; la première suite en échec est nommée et fait échouer la validation, comme avant. |
| **P2** Export Local | Le build ne relance plus toute la suite sur l'export Local. Il vérifie que ses fichiers sont **identiques octet pour octet** à la source (README à part, qui reçoit ses variantes locales : `validate_all.py --identite-locale`), puis lance `validate_all.py --essentiel` (validations, RUN_CARD, lignes de commande). |
| **P3** Mode rapide | `python3 scripts/validate_all.py --rapide` : validations et tests sans navigateur, en parallèle, sans contrôle de déplacement ni build, en **91 s**. Documenté dans `maintenance/README.md` : il ne remplace jamais la préparation complète avant une livraison. |

**Ce qui ne change pas** : la préparation complète garde le navigateur, le contrôle de déplacement, les deux builds et la comparaison de reproductibilité ; l'archive GitHub reste comparée au commit fichier par fichier.

## 3. Le résultat

| Mesure | Avant | Après |
|---|---|---|
| Préparation complète | 891 s | **459 s et 469 s (−48 %)**, deux mesures |
| Vérification pendant le travail | 891 s (seul mode) | **91 s** (`--rapide`) |

## 4. Tests et mutations rouges

3 cas (`PreparationPlusRapide`, 196 cas d'audit en tout) : une suite en échec est nommée et les sorties restent dans l'ordre ; toutes vertes, aucune erreur ; export Local identique, puis fichier changé et fichier manquant relevés.

| Mutation | Résultat |
|---|---|
| Les échecs des suites parallèles sont ignorés | Rouge : `test_parallele_nomme_l_echec` |
| L'identité de l'export Local n'est plus vérifiée | Rouge : `test_identite_locale` |

## 5. Préparation et livraison

- **Préparation complète** : réussie deux fois (459 s, puis 469 s après la montée de révision oubliée au premier passage). Tous les tests passent ; « LOCAL IDENTITY PASSED — 157 fichiers identiques à la source, README à part ».
- **Commits** : `2407a12` sur `lot-outil`, fusionné en `a0a03d9` sur `master` (`--no-ff`).
- **Archive GitHub** : les 164 fichiers sont identiques au commit.
- **Sortie** : `Design_Governance_V1_GITHUB_R2026-11-25b.zip` (sha256 `051e96e2…74af3`) ; `claude/livraison/R2026-11-25b/` : archive Local (sha256 `67560bd7…bf94`) et bundle vérifié. La `25a` est retirée de DG-777.

## 6. Ce qui reste possible (P4, non fait)

Accélérer `test_check_render` (184 s) et `test_parcours` (197 s), qui bornent maintenant la durée : un navigateur partagé entre les cas, moins de sous-processus. Gain estimé : encore 1 à 2 minutes.
