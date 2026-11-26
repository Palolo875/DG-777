# Rétro-ingénierie 2 — Ce que font les références réelles, en décisions mesurées

Rédigé le 25 novembre 2026 (« Op 2 »). Aucun run. Rien n'est intégré.

## Méthode

- **Échantillon** : les dix sites réels que les agents ont pris comme références aux runs 22 à 24, plus nos trois rendus. Ce ne sont pas des sites choisis par Junior : c'est l'échantillon disponible sans coût, à élargir.
  - Studios d'architecture : Caruso St John, 6a, David Chipperfield, Assemble.
  - Vélo : Retrobicicletta, Vélo Bordeaux, Mission Bicycle, Brooklyn Bicycle Co.
  - Culture : Officine Saffi, e-flux.
- **Mesures** : `decompose.py` (dans ce dossier, hors paquet), à 1440 et 390 px, sur la page chargée.
  - Typographie : tailles de texte qui portent au moins 20 caractères, familles, graisses, plus grand texte rapporté au texte courant.
  - Couleur et effets : couleurs de texte, fonds, rayons, ombres.
  - Mise en page : longueur de ligne en signes, marge gauche, lignes d'alignement (bords gauches partagés par trois éléments ou plus).
  - Premier écran : mots, et part de la surface vide (proche du fond).
- **Limites** : un relevé automatique approximatif (bandeaux de cookies, polices de secours, éléments cachés). Il compte des décisions, il ne juge pas.
- **Première lecture** avec l'outil existant (`verifier --refs`) :
  - au run 23, l'écart « image ou média 0 % contre 48 % » a été signalé, puis laissé ; les banques d'images refusaient ou ne donnaient rien ;
  - au run 24, l'écart d'échelle (×3,1 contre ×1,4) n'a pas été signalé : l'outil ne relève que la part d'image.

## Résultats à 1440 px

| Page | Tailles | Familles | Graisses | Couleurs de texte | Rayons / ombres | Alignements | Plus grand / courant | Mots au 1er écran | Vide au 1er écran |
|---|---|---|---|---|---|---|---|---|---|
| Caruso St John | 3 | 2 | 2 | 1 | 0 / 0 | 2 | ×1,4 | 51 | 68 % |
| 6a | 2 | 1 | 1 | 1 | 0 / 0 | 1 | ×1,4 | 66 | 97 % |
| David Chipperfield | 2 | 2 | 2 | 3 | 1 / 0 | 4 | ×1,0 | 169 | 82 % |
| Assemble | 2 | 1 | 2 | 1 | 0 / 0 | 1 | ×1,4 | 90 | 93 % |
| Officine Saffi | 1 | 1 | 1 | 1 | 0 / 0 | 1 | ×1,0 | 7 | 50 % |
| e-flux | 4 | 1 | 2 | 4 | 1 / 0 | 36 (liste) | ×1,0 | 10 | 63 % |
| Retrobicicletta | 1 | 1 | 1 | 1 | 0 / 6 | 0 | ×1,0 | 3 | 50 % |
| Mission Bicycle | 2 | 1 | 2 | 3 | 1 / 2 | 1 | ×1,0 | 14 | 86 % |
| Vélo Bordeaux | 7 | 2 | 4 | 7 | 1 / 1 | 6 | ×2,0 | 164 | 31 % |
| Brooklyn Bicycle Co. | 12 | 6 | 4 | 12 | 14 / 57 | 39 | ×3,2 | 114 | 4 % |
| **Run 22** (invitation) | 5 | 2 | 2 | 5 | 4 / 1 | 9 | ×2,0 | 67 | 65 % |
| **Run 23** (atelier vélo) | 10 | 2 | 3 | 4 | 0 / 0 | 11 | ×7,6 | 235 | 65 % |
| **Run 24** (contact de studio) | 10 | 2 | 3 | 6 | 1 / 0 | 10 | ×3,1 | 182 | 19 % |

À 390 px, même écart : les studios ont 1 à 3 tailles ; les runs 23 et 24 en ont 10 et 11.

## Ce que ça montre

1. **Les références haut de gamme tiennent sur très peu de décisions.** Studios et culture :
   - 1 à 3 tailles de texte, souvent une seule famille, 1 ou 2 graisses, une couleur de texte ;
   - ni rayon ni ombre ; 1 à 4 lignes d'alignement ;
   - un plus grand texte à peine plus grand que le texte courant (×1 à ×1,4) ;
   - un premier écran vide aux deux tiers ou plus.

   Ce qui porte la page : le contenu, l'image, l'espace. Les sites commerciaux de masse (Brooklyn : 12 tailles, 6 familles, 57 ombres) sont à l'opposé.
2. **Nos rendus multiplient les décisions.**
   - Ce qui se multiplie : 5 à 10 tailles, 4 à 6 couleurs de texte, 9 à 11 lignes d'alignement, une échelle de ×2 à ×7,6.
   - Le premier écran du run 24 n'est vide qu'à 19 %, avec 182 mots, contre 51 à 90 mots chez les studios.
   - Le rendu que nous avons jugé le meilleur (run 24) est, en décisions, plus proche de Vélo Bordeaux que de Caruso St John.
3. **Le système dit déjà la règle, mais elle n'est pas appliquée.**
   - Le noyau dit : « Le geste qui porte l'idée se pousse jusqu'au bout ; la retenue porte sur le reste. » Les références font exactement cela : une chose forte (l'image, l'espace, une voix) et tout le reste réduit.
   - Nos agents poussent le geste, mais le reste ne se réduit pas : chaque section ajoute ses tailles, ses couleurs, ses alignements.
4. **Le relevé de références existe, mais ne compare qu'une mesure.** `verifier --refs` relève la part d'image. Il ne relève pas le nombre de tailles, de couleurs ou d'alignements, ni l'échelle, ni la densité du premier écran : précisément les écarts ci-dessus.
5. **Le signal de matière a été laissé faute d'image.** Au run 23, quand les banques d'images ont échoué, rien n'a proposé l'autre voie, une matière codée (recette `matiere`).

## Ce que ça ne montre pas

- **Que moins de décisions donne un meilleur rendu dans tous les cas.** Une page de contact de grand studio est sobre par convention. Une page de service (l'atelier vélo) peut demander plus d'information. Le bon nombre dépend du niveau d'expression déclaré.
- **Que ces références sont « excellentes ».** Elles ont été choisies par les agents, pas par toi.

## Pistes (à discuter, rien de décidé)

- **A. Étendre `verifier --refs`.** Comparer aussi tailles, familles, couleurs de texte, alignements, échelle et mots au premier écran à la médiane des références. Un écart du simple au double devient une question : « 10 tailles contre 2 : lesquelles portent l'idée ? » C'est la retenue rendue mesurable, sans fixer de style.
- **B. Une passe de réduction à l'atelier.** Après l'intensification, une variante qui réduit le reste (tailles, couleurs, alignements) sans toucher au geste porteur, comparée sur la planche. C'est la moitié manquante de « pousser le geste ».
- **C. Quand l'image manque**, le signal de matière propose la matière codée (recette `matiere`) au lieu de s'arrêter.
- **D. Un échantillon choisi par toi.** Cinq à dix sites que tu juges excellents, par type d'objet (studio, commerce de quartier, culture, produit, événement). On les mesure de la même façon : ce seront les repères de ton goût, et peut-être la base d'une liste de sources par objet (piste déjà notée).
