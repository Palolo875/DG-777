# Lot 11c — Rapport : les blocs de procédure deviennent des lignes

- **Révision** : `R2026-11-15t`, livrée le 21 novembre 2026.
- **Branche** : `lot-11c`.
- **Décision** : « À toi le choix, poursuivons » sur `Lot_11c_Lignes_a_relire.md`. J'ai retenu les options A : les lignes telles que rédigées, un budget de noyau à 31 000 octets, et un budget de tronc relevé.
- **Runs** : aucun.

## 1. La mesure, avant et après

| Mesure | Avant (`s`) | Après (`t`) |
|---|---|---|
| Noyau `SKILL.md` | 48 173 octets (46 414 caractères) | **30 502 octets (−37 %)** |
| Budget du noyau | 48 500 (provisoire) | **31 000** |
| Tronc DIRECTION | 31 398 caractères | 35 177 caractères |
| Budget du tronc | 35 000 caractères | **40 000** (voir § 3) |
| Lecture fixe d'un run DIRECTION (noyau + tronc) | ≈ 77 800 caractères | **≈ 64 600 (−17 %)** |
| Lecture fixe d'un run LITE, ITER, STANDARD ou SYSTÈME | noyau + tronc | **≈ −17 600 caractères** de noyau ; leurs troncs sont inchangés |

**Pourquoi DIRECTION gagne moins** : les routes `DIRECTION/DIVERGENCE`, `DIRECTION/CREATIVE-BOOT` et `DIRECTION/STANDARD` sont dans son tronc. Le texte complet que le noyau portait revient donc dans le tronc, lu une fois. Un run DIRECTION lit toujours la procédure entière ; les autres modes ne la lisent plus.

## 2. Ce qui change

- **13 blocs passent en « différé »**, servis en entier par leur route : `DIR-LEVIERS`, `DIR-DECLARATION`, `MOY-PLAFOND`, `ANCRE`, `BOUCLE-ATELIER`, `BOUCLE-CAPTURE`, `STRUCT-TRAME`, `COMP-SINGULARITE`, `COMP-CONVERGENCE`, `COMP-TITRE`, `VER-SCENE`, `VER-AUDIENCE`, `REGISTRES`.
- **12 lignes d'invariant les remplacent au noyau**. Chacune est un petit bloc écrit juste avant le bloc qu'elle résume, dans le même fichier source.
- **Le texte des lignes** est celui du document de relecture, avec **deux retouches** imposées par des gardes :
  - L2 (déclarer la direction) : « pris dans **au moins** deux dimensions du registre (composition, …) ». La garde REG-01 lit cette liste au noyau.
  - L6 (revue sur capture) : « où va l'œil **en premier** ». La garde CORE-01 protège cette formulation.
  - L4 (ancre et calibration) : « au niveau visé **(ligne `NIVEAU`)** ». Le test P27 de `parcours` relie la calibration à la ligne `NIVEAU`.
- **Trois obligations passent à la forme « ligne »** de 11a : diverger sur image et déclarer la direction (route `DIRECTION/DIVERGENCE`), regarder des références (route `SAVOIR/SOURCE`).
- **Trois petits blocs d'obligation restent tels quels** : `COMP-TYPO`, `COMP-CONTROLES`, `COMP-COULEUR`.

## 3. Les gardes et les tests, un par un

Sur la copie jetable, 18 tests échouaient. Avec les lignes, il n'en restait que deux.

| Garde ou test | Décision |
|---|---|
| `REQ-01`, trois planchers | **Adaptés** : forme « ligne ». Mutation rouge : sans sa route, la ligne de « Diverger sur image » est refusée (REQ-01 et `test_current_corpus_has_a_floor_for_each_obligation`). |
| `CORE-01`, revue sur capture, Gate C, esquisses en mobile | **Gardés** : les lignes portent les formulations protégées. |
| `CORE-01`, planchers couleur et typographie | **Gardés** : leurs blocs restent au noyau. |
| `REG-01`, dimensions du registre | **Gardé** : la ligne L2 porte la liste. |
| `CHG-10` et la marge de 10 % du tronc (`test_trunks_serve_gate_a_controls_only`) | **Adapté** : budget du tronc à **40 000**. J'avais proposé 36 000, mais la règle existante veut 10 % de marge (35 177 / 0,9 ≈ 39 100). Je n'ai pas assoupli la règle. |
| `test_loaded_typography_floor_folds_but_title_details_remain` | **Gardé**, et il a trouvé un vrai défaut (ci-dessous). |
| `parcours` P24 et P27 (calibration) | Trouvés par la première préparation complète, qui a échoué. **P27 gardé** : la ligne L4 porte « (ligne `NIVEAU`) ». **P24 adapté** : la ligne au noyau dit « d'une décision visuelle ouverte, regarde en image », et la phrase complète est vérifiée dans `DIRECTION/STANDARD`. |

**Le défaut trouvé.** Quand `read_route` sert une route, il remplace chaque bloc déjà au noyau par un renvoi « Déjà dans le noyau… ». Ce renvoi faisait environ 200 caractères, **plus long qu'une ligne d'invariant**. La lecture d'une route devenait plus longue qu'en `--complet`. Le renvoi est raccourci (numéro de section, 60 caractères du début, « --complet l'affiche ») ; cela allège aussi toutes les autres lectures de route.

## 4. Préparation et livraison

- **Préparation complète** : `--require-browser --empreintes`, réussie **au second passage**.
  - Le premier a échoué sur `parcours` P24 et P27 (voir § 3). Je n'avais pas relancé cette suite seule avant la préparation.
  - Tests : régressions d'audit 168, budget 19, `parcours` 176, `read_route` 106, `regard` 41, journal 19, `check_render` A, B et C.
  - Validations de structure, de carte de lecture, complète et locale : PASSED. Garde PRO-01 active.
- **Commits** : `8cf458d` sur `lot-11c`, fusionné en `3097627` sur `master` (`--no-ff`).
- **Archive GitHub** : les 151 fichiers sont identiques au commit.
- **Sortie** :
  - `Design_Governance_V1_GITHUB_R2026-11-15t.zip` (sha256 `f25d69de…8ce6`), à côté de la `k` ;
  - `claude/livraison/R2026-11-15t/` : archive Local (sha256 `3ae3c9e8…0982`) et bundle vérifié.
  - La `s` est retirée de DG-777. Elle reste dans l'historique et dans le bundle.

## 5. Ce que ce sous-lot ne prouve pas

- Qu'un agent en mode LITE, ITER ou STANDARD ouvrira la route quand une ligne l'exige : seul un run le dira (lot 13).
- Que les lignes gardent toutes les nuances : le texte complet reste servi, mais seul un rendu le montrera.
- La cible de 18 000 octets du sous-lot 11d est à revoir : il reste 30 502 octets, dont 7 383 pour l'index.
