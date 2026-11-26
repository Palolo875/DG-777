# Lot 20 (a, b, c) — Rapport : construire au niveau pro ; publication V1.7.0

- **Révision** : `R2026-11-25j`, 26 novembre 2026. Publication **V1.7.0**.
- **Branche** : `lot-20`.
- **Décision** : « Oui » (options A du lot 20). Ordre : 20a, 20b, 20c d'abord ; 20d et 20e ensuite.
- **Runs** : aucun.

## 1. Ce qui change

| Sous-lot | Où | Changement |
|---|---|---|
| **20a Composer** | `references/recettes.md` ; `BIBLIOTHEQUE/GRID` ; `SAVOIR/TECH` ; `parcours.py tirage` et `chantier` | **Six recettes de grille** (modulaire, colonnes, radiale, hiérarchique, ligne de base, axiale) et **quatre techniques** (superposition, découpe et masque, fond perdu, grille rompue). Chaque recette donne un squelette de code, des proportions, une adaptation mobile, son usage en application et en affiche, et ce qui se vérifie. Chaque fiche de grille nomme sa recette (« **Construire :** `parcours.py recette …` »). Le tirage et `chantier` annoncent la recette de la grille tirée (`recette_de_grille`). `SAVOIR/TECH` renvoie aux quatre techniques (« Sortir de la boîte »). |
| **20b Détails des composants** | Recette `details-composants` ; `SAVOIR/STATE` « Partie ordinaire » | Ombres en deux couches, bord semi-transparent, teinte des bords et des ombres, états plus contrastés que le repos sans déplacer la cible, contour d'image de 1 px, marge réduite du côté de l'icône, cible de 44 px, superellipse en amélioration progressive. La ligne « Partie ordinaire » y renvoie. |
| **20c Retenue mesurable** | `parcours.py` (finition et `verifier --refs`) ; `SAVOIR/STATE` ; `SAVOIR/TYPE` | Seuil des tailles de texte de 10 à **6**. Signal **couleurs de texte** dès 5 (ligne « Retenue du système », nouvelle dans `SAVOIR/STATE`). Mesures de niveau étendues : couleurs de texte, mots au premier écran. `verifier --refs` affiche tailles, couleurs, échelle et mots, et nomme l'écart « du simple au double ». Les références anciennes, sans ces mesures, affichent « — ». Paragraphe « Échelle restreinte » dans `SAVOIR/TYPE`, dans le tronc. |

- **Écart à la proposition** : les « schémas rendus en image » des grilles ne sont pas générés. Le squelette de code de chaque recette rend le schéma ; l'agent le capture s'il veut le voir. Je l'aurais proposé à part si une image avait été nécessaire.
- **Règle d'entrée des recettes** (« plusieurs rendus ont achoppé ») : la composition basique est relevée dans tous les runs 21 à 25 ; les détails de composants, dans les mêmes rendus et dans la comparaison aux références (`Reverse_2/`).
- **Noyau inchangé** : 32 923 octets.
- **Tronc DIRECTION** : 35 438 caractères (+261, marge 4 562).
- **Étape CONSTRUCTION** : 38 157 caractères (marge 1 843).
- **Étape ESQUISSES** : environ +500 caractères.
- **Recettes** : vingt-deux en tout.

## 2. Tests et mutations rouges

- `parcours` : 214 cas.
  - Chaque recette de construction est vérifiée dans le navigateur à 1440 et 390 px, sur sa promesse et sans débordement.
  - Chaque fiche de grille nomme une recette qui existe.
  - Signaux de retenue sur une page à sept tailles et cinq couleurs ; rien sur une page sobre.
  - Écart du double contre des références mesurées.
- **Mutations** :
  - copie 1 (signaux) : signal des couleurs retiré, écart du double retiré, recette retirée d'une fiche de grille ;
  - copie 2 : les onze recettes, chacune cassée sur sa propre promesse ;
  - copie 3 : seuil remis à 10.
- **Deux tests trop permissifs, corrigés** : la grille hiérarchique (seuil relevé à quatre fois la surface au bureau) et la superposition (deux blocs qui se touchent par un coin comptaient comme un recouvrement ; il faut maintenant 10 % de surface commune).

| Mutation | Résultat |
|---|---|
| Signal des couleurs de texte retiré ; écart du double retiré | Rouge : P200 |
| Recette retirée de la fiche `GRID/AXIAL` | Rouge : P17 |
| Seuil des tailles remis à 10 | Rouge : P200 |
| Chacune des onze recettes cassée sur sa promesse | Rouge : P149 à P159, chacune par son nom (après correction des tests de P152 et P155) |

## 3. Préparation et livraison

- **Police des cartes** : « V1.7.0 » demandait un chiffre absent du sous-ensemble de la police des cartes (garde de fraîcheur des supports). Police régénérée avec les versions figées de `supports/fonts/requirements.txt`, installées dans un environnement à part, puis cartes régénérées.
- **Préparation complète** : réussie en **553 s**, plus longue que d'habitude (onze recettes de plus vérifiées dans le navigateur). Tests : `parcours` 214, `read_route` 107, `regard` 42, `check_render` 265… ; reproductibilité vérifiée.
- **Commits** : `e8b2a65` sur `lot-20`, fusionné en `a0be5b3` sur `master` (`--no-ff`).
- **Archive GitHub** : les 164 fichiers sont identiques au commit.
- **Sortie** : `Design_Governance_V1_GITHUB_R2026-11-25j.zip` (sha256 `65ab182f…1359`) ; dans `claude/livraison/R2026-11-25j/` : archive Local (sha256 `d86da9a5…8127`) et bundle vérifié. La `25i` est retirée de DG-777.

## 4. Ce que le lot ne prouve pas

- **Que les rendus deviennent professionnels** : seul le regard de Junior sur un run le dira.
- **Que l'agent appelle les recettes** : il appelle celle de la grille tirée, nommée par le tirage. Les autres dépendent des renvois dans les routes servies par les étapes.
- **Le seuil de 6 tailles** peut relever des pages riches et justes : c'est une question, pas un verdict.
