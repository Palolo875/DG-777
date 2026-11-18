# Lot 4 bis, sous-lot 1 — Accessibilité et performance : rapport

15 novembre 2026. Révision livrée : `R2026-11-15f` (commit `fb3e337`, fusionné dans master en `d11b9e8`). Document hors du paquet.

Les options A ont été appliquées. La validation complète avec navigateur passe. L'archive GitHub est identique au commit, fichier par fichier.

## 1. Ce qui a changé

| Où | Changement |
|---|---|
| `SAVOIR/CONTEXT` | Deux nouvelles sous-sections, avec le texte des propositions : « Accessibilité : ce qui se décide en concevant » et « Performance : repères et leviers de conception ». Elles sont servies par la route, au signal existant du noyau. |
| `check_render.py` | Un nouveau contrôle, « Stabilité au chargement ». Le décalage cumulé de mise en page est mesuré en local, depuis le début du chargement et avant tout défilement. Au-delà de 0,1, une réserve, jamais un `RETURN`. Les images visibles sans proportions réservées sont listées pour information, sans statut. Une ancienne mesure sans ce champ ne rend pas le contrôle. |
| `parcours.py verifier` | Le poids devient un signal, avec sa question, au-delà des repères `[À ADAPTER]` : 2 Mo pour la page, 500 Ko pour une image, 300 Ko de polices intégrées. La fiche donne les repères avec le poids. |
| Mode d'emploi de la recette, README des scripts, fiche de version | Le nouveau contrôle et les signaux de poids y sont nommés. |

**Critère d'arrêt vérifié.** Sur une page piège (un bandeau inséré après le chargement), la mesure a été lancée trois fois à 1440 et à 390 px : elle donne le même résultat à chaque fois (0,0347 et 0,1429). Sur la même page sans bandeau, le décalage est nul. La mesure est donc stable : je la livre.

## 2. Écarts par rapport au texte proposé

1. **« Lignes de 45 à 80 signes » devient « une mesure de 45 à 80 signes ».** Avec le premier libellé, la recherche « le texte est trop long sur une ligne » menait d'abord à `SAVOIR/CONTEXT` au lieu de `SAVOIR/TYPE`, ce qui faisait tomber un plancher de trouvabilité. Le sens ne change pas : « mesure » est le terme typographique.
2. **Dans le mode d'emploi de la recette, « à titre d'information » est devenu « pour information »**, pour la même raison : le mot « titre » faisait remonter la recette sur la recherche « le titre écrase la photo ».
3. **Point à garder en tête.** Ces repères de lecture (16 px, interligne, mesure) vivent dans le savoir sur le contexte, parce qu'ils servent l'accessibilité. `SAVOIR/TYPE` n'en dit rien. Il n'y a donc pas de doublon, mais la typographie de lecture n'a pas encore de propriétaire. À trancher, si vous le souhaitez, au lot 8.

## 3. Vérification

| Contrôle | Résultat |
|---|---|
| Noyau | identique à `R2026-11-15e` (44 994 / 46 000 octets) |
| Troncs des cinq modes | identiques |
| Recette de rendu | A 118 cas, dont 4 nouveaux : réserve, PASS, API indisponible, mesure ancienne ; C 65 ; B 81, dont la page qui saute et la page stable |
| Parcours | 150 cas, dont 2 nouveaux sur le poids (page légère, page de 3 Mo) |
| Régressions d'audit | 135 cas ; le nouveau savoir est servi par sa route et absent du noyau |
| Lecteur | 105 cas ; planchers de trouvabilité tenus |
| Regard, journal, budget, préparation, déplacement, craft, supports, export Local, reproductibilité | passés |
| Durée de préparation | 11 min 47 s |

Empreintes :
- GitHub `dba65a60…1756d5`
- Local `6a909a83…b9ad`

## 4. Suite

Le sous-lot 2, B-04 (sections ordinaires), a besoin de votre jugement de designer. Ses propositions contiendront le texte entier des sept entrées de `BIBLIOTHEQUE/SECTIONS`.
