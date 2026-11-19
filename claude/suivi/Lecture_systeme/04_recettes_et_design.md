# Lecture du système, étape 4 : references/recettes.md et design/README.md (19 novembre 2026)

Les deux fichiers sont lus en entier (175 et 41 lignes).

## references/recettes.md
- **Le format :** problème, quand l'utiliser et quand ne pas l'utiliser, procédé, code court, ce que la direction décide, ce qu'on vérifie sur capture. C'est clair et court, sans doute le format le plus efficace du paquet.
- **Le contenu :** cinq recettes (graphique lisible en mobile, grand chiffre qui change, moment orchestré, focus sur tout fond, contrôles natifs). **Toutes règlent la robustesse** : débordement, accessibilité, mouvement réduit, clavier. **Aucune ne règle la qualité visuelle**, et c'est voulu : « jamais une apparence ».
- **Une exception :** la recette « moment orchestré » fixe une apparence précise (une entrée avec une rotation de −1,5°). Si elle est reprise telle quelle, toutes les entrées se ressembleront. Point mineur, à vérifier sur les runs qui l'ont utilisée.
- **Une règle d'entrée saine :** « une recette n'entre ici que si plusieurs rendus ont achoppé sur la même difficulté ». Les runs 9 à 16 donnent de telles difficultés répétées : le bas de page générique, la grille d'informations d'un billet ou d'une fiche, la hiérarchie d'échelle. Mais ces difficultés touchent l'apparence, que les recettes refusent par principe.

## design/README.md
- **Le cœur du système :** quatre dossiers (direction, savoir, formes, produit), soit **56 805 mots** de savoir mesurés (direction 12 132, savoir 27 597, formes 10 299, produit 6 264). L'agent n'en lit qu'une partie, par routes.
- **Un choix explicite :** « Ce n'est ni un catalogue de styles, ni une bibliothèque de composants prêts à l'emploi. » C'est cohérent avec les recettes.
- **Une phrase juste :** « Une preuve technique ne vaut pas jugement esthétique ». Or la finition s'arrête quand `verifier` se tait, c'est-à-dire sur une preuve technique. Le texte dit une chose, la procédure en fait une autre.
- **La table « Créer / Observer et corriger » :** la colonne de droite contient surtout de la gouvernance (mesurer l'enjeu, dire ce qui est concerné, protéger les contraintes). Seules deux lignes sur cinq parlent vraiment de regarder et corriger.

## Recherche faite à côté : un modèle peut-il juger la qualité visuelle ?
- *MLLM as a UI Judge* (https://arxiv.org/abs/2510.08783, 2025) :
  - Claude et GPT-4o choisissent la même interface que les humains dans **environ 59 %** des paires ;
  - c'est **proche du hasard quand les deux interfaces sont proches**, et cela monte jusqu'à environ 90 % quand l'écart est grand ;
  - les modèles réussissent mieux sur la hiérarchie et la confiance que sur l'émotion et la facilité d'usage.
- *UICrit* (https://arxiv.org/html/2407.08850v3, 2024) : 3 059 critiques écrites par 7 designers. Donner des exemples de critiques au modèle améliore ses retours de 55 %, mais ils restent sous le niveau humain (score 0,48 contre 0,75).
- *DesignPref* (https://arxiv.org/pdf/2511.20513v1) : 12 000 comparaisons faites par 20 designers professionnels ; même eux sont souvent en désaccord, ce qui fixe un plafond à tout juge.
- *Rate My Web Design?* (ICSE 2026, https://doi.org/10.1145/3774748.3795676) : sur des maquettes générées, la note de GPT-4o s'accorde mal avec celle de 39 experts.
- Signalé par la recherche mais non vérifié : AUV-Bench (https://arxiv.org/pdf/2609.34854).

## Ce que ça change à mes pistes
1. **Correction :** le « regard séparé qui compare deux images », que je présentais comme un levier fort, ne vaut que pour **écarter une option nettement moins bonne**. Entre deux bonnes versions, un modèle juge presque au hasard. **Ton jugement reste irremplaçable, ce qui donne raison à ta règle 7.** Le levier réaliste : laisser le modèle trier grossièrement beaucoup de variantes, et te garder les dernières comparaisons.
2. **Ton carnet de goût a plus de valeur que je ne pensais.** UICrit montre que des critiques d'experts données en exemples améliorent nettement le jugement d'un modèle. Tes verdicts, avec leurs raisons, sont exactement ce type de matériau.
3. **Les recettes montrent le bon format** (court, un problème, du code, quoi vérifier), mais elles l'appliquent volontairement à la robustesse, pas à la qualité. Si l'on ajoute des exemples d'exécution, ce serait la piste des triptyques, dans ce même format.

## Suite proposée
Lire `design/direction/README.md`, puis `design/produit/finition.md`, où vivent l'atelier et la passe de finition.
