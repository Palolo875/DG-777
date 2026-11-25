# Rétro-ingénierie 1 — Des rendus aux causes (runs 22, 23, 24)

Rédigé le 25 novembre 2026, sur la demande de Junior (« On va faire du reverse engineering », puis « Allons-y » : option 1 d'abord, puis 2). Sources : journaux (`journal.jsonl`), traces, fichiers de chantier et planches des runs. Aucun run. Rien n'est intégré.

**Méthode** : pour chaque qualité observée, chercher dans le journal et la trace l'étape qui l'a produite. Le contrefactuel manque (aucun run sans système sur ces briefs) : une cause relevée est **probable**, pas prouvée. Une part revient au modèle lui-même (par exemple, calculer un trajet piéton sur OpenStreetMap).

## 1. Ce qui a produit les qualités

| Qualité | Run | Cause relevée | Force |
|---|---|---|---|
| **Idée propre au sujet** | 23, 24 | **Le tirage** (`parcours.py tirage`, servi par `chantier`). 23 : pistes tirées « son rituel ; une donnée qui lui est propre », dimension « époque et culture » → « Départs » (le rituel du dépôt et du départ, l'affiche jaune des gares françaises). 24 : « son opposé ; une donnée qui lui est propre », même dimension → plan réel et trajet calculé (la donnée propre), cadran des heures (donnée). Les trois esquisses du run 24 et l'esquisse gardée du run 23 viennent du tirage. | Forte : l'idée gardée reprend mot pour mot la piste et la dimension tirées. |
| **…mais le tirage peut être absorbé par la modale** | 22 | Pistes tirées : « son nom » ; « sa forme ou son deuxième attribut ». L'agent a rattaché la modale de la céramique (l'émail qui coule) à la seconde, et l'a déclarée « tirage, rang 3 ». | Forte : c'est le mécanisme de la convergence observée. |
| **Voix typographique juste** | 23, 24 | `SAVOIR/TYPE-VOIX` lu dans les deux runs ; voix comparées sur le vrai titre (23 : Archivo Narrow contre Archivo 800 et Familjen ; 24 : Newsreader contre Literata, Inter et Archivo). | Forte : la trace le dit, et le choix final est celui de la comparaison. |
| **Retenue, une couleur d'accent** | 23, 24 | `parcours.py leviers` (23 : précision, chaleur, instrument ; 24 : précision, calme) ; palette par rôles au noyau. | Probable. |
| **Défauts corrigés avant de montrer** | 23, 24 | Signaux de `verifier` et atelier : 23, « Retards » recomposé contre une **silhouette jumelle**, pictos retirés, heures intensifiées ; 24, **sur-titres de gabarit retirés** (marqueurs de vague), échelle de 12 à 9 tailles, étiquettes sorties du trajet, **bords de champs à 3,8:1** (signal du lot 14c). | Forte : chaque correction nomme le signal qui l'a appelée. |
| **Esquisses à armes égales** | 23, 24 | Lot 16b (règle lue dans `DIRECTION/DIVERGENCE`) ; esquisses de 3,1 à 4,0 ko au run 23 contre 1,6 à 2,6 au run 22. | Probable : deux runs, et des sujets différents du run 22. |
| **Contenus d'exemple honnêtes** | 22, 23, 24 | Règles de vérité (`CNT-01`, `TRUTH`) : contenus marqués « exemple », aucune fausse photo, domaines `.example`, plage de téléphone fictive. | Forte et constante. |
| **Action et idée au premier écran mobile** | 24 | Lecture mobile à l'atelier (lot 14a) : la trace déclare « mobile : titre et action, puis le plan recadré dès le premier écran ». | Probable ; au run 23, le tableau n'y est pas. |
| **Une fin qui reprend le titre** | 23, 24 | Probablement la séquence (`BIBLIOTHEQUE/SEQUENCE`, présente dans le tronc DIRECTION) ; aucune route lue à part. | À vérifier. |

## 2. Ce qui n'a pas produit d'effet visible

| Élément | Constat |
|---|---|
| **Probabilités et rangs** | Remplis dans les trois traces, faux au run 22, sans effet visible sur le choix dans les runs 23 et 24 : l'idée vient du tirage. |
| **Défense de la modale** | Écrite dans les trois runs ; la modale n'a jamais gagné. Effet sur le jugement : invisible ici. |
| **Une source par piste (16a)** | Suivie au run 23 (pierre, étiquette, craie), pas au run 24 (calibration seule). |
| **Recettes** | Une seule lue en trois runs (`matiere`, au run 22). Les autres besoins ont été codés de mémoire, correctement. |
| **Inventaire du sujet (CFT-01)** | Lu aux runs 22 et 23, pas au run 24 ; les idées gardées viennent du tirage, pas d'un rang de l'inventaire. |

## 3. Ce qui manque encore, et pourquoi

| Manque | Cause probable |
|---|---|
| **La chaleur et la matière (23)** | Aucune matière déclarée par la direction, donc ni la recette `matiere` ni `SAVOIR/SOURCE` n'ont été ouvertes. En fondant l'esquisse C (étiquette kraft) dans A, l'agent a repris le geste et laissé la matière : aucune règle ne dit ce qu'une fusion garde. |
| **L'accord entre titre et action (24)** | Le titre porte l'idée (venir), l'action principale est d'écrire. Rien ne vérifie que le titre mène à l'action principale. |
| **La moitié basse s'aplatit (24)** | Deux sections de même silhouette ; le signal de silhouette jumelle a corrigé le run 23, pas celui-ci (non déclenché ou gardé : à vérifier dans la fiche de `verifier`). |

## 4. Ce qu'on en tire (pistes à discuter, rien de décidé)

1. **Le tirage est le levier le plus fort de l'idée.** Le protéger de la modale : l'esquisse issue du tirage ne doit pas reprendre le fait principal de la modale. La piste « sa forme ou son deuxième attribut » est celle qui a ramené l'émail au run 22.
2. **Garder sans retoucher** : comparaison des voix sur le vrai titre, signaux de `verifier`, règles de vérité. Ce sont des causes nettes.
3. **Probabilités, rangs et défense de la modale** n'ont pas d'effet visible. Je ne propose pas de les retirer (ta règle : ne pas alléger ce qui peut servir), mais de ne plus rien leur ajouter.
4. **La fusion d'esquisses** : quand on reprend un geste d'une esquisse écartée, on reprend aussi sa matière, ou on dit pourquoi pas.
5. **Le titre et l'action** : une question à l'atelier : le titre mène-t-il à l'action principale ?

## 5. Limites

- Trois runs, trois sujets : des tendances.
- Les causes sont lues dans les journaux et les traces. L'agent peut écrire après coup une raison qui n'a pas guidé son choix.
- La part du modèle est grande et non séparable ici.
