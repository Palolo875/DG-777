# Lot 17 — Propositions : le fini

Rédigé le 25 novembre 2026. C'est la synthèse de la rétro-ingénierie (runs 22 à 24, références des agents, 16 références de Junior). Base : V1.4.0 (`R2026-11-25f`). Aucun run. Règle 1 : rien n'est intégré sans décision ; « D'accord » vaut pour les options A partout.

**Le critère de Junior** : « le côté soigné, fini, abouti, le visuel global ».

## 0. Mesure

| Constat | Source |
|---|---|
| Les références tiennent sur **peu de décisions**. Studios : 2 à 3 tailles de texte, 1 couleur de texte, ni rayon ni ombre. Références de Junior : une famille, 3 à 5 tailles, un accent. | `Reverse_2/` |
| Nos rendus en ont **5 à 10 tailles**, 4 à 6 couleurs de texte, 9 à 11 lignes d'alignement. | `Reverse_2/decompose.json` |
| **Le signal de tailles existe, mais à 10** (`SEUILS["tailles"]` dans `parcours.py`). Le run 24 est passé de 12 à 9 tailles et s'est arrêté là, sous le seuil. Aucun signal sur le nombre de couleurs de texte (seules les teintes vives sont comptées). | `scripts/parcours.py`, trace du run 24 |
| `verifier --refs` ne compare aux références que la part d'image. | `Reverse_2` |
| Les gestes de finition existent déjà : rayons emboîtés, masse, vide, surface, chiffres, accent, détail révélateur, partie ordinaire, habillage de gabarit… Les références de Junior en sont l'application soignée. **Absents** : la profondeur par la luminance, la retenue du système (le nombre de décisions). | `SAVOIR/STATE` (`design/savoir/composition.md`) |
| Ses références reposent souvent sur un **objet géométrique dessiné** (carte pliée, téléviseur en isométrie, billets de verre). La règle « Pas de figuratif de mémoire » demande de déclarer un registre dessiné, et préfère l'atmosphère au dessin. **Aucun de nos rendus n'a d'objet dessiné.** | `design/direction/diriger.md`, lots 2 et 3 |
| Procédés vus dans les références et absents du système : matière en plans (formes, flou, texture, fondu vers le texte), lumière et verre concentrés sur une zone, détail de données (hachures, barres segmentées, courbes miniatures, annotation qui raconte), couche d'annotation, touche de main, palette prélevée sur l'image. | Lots 1 à 3 |
| Le système n'a presque jamais été éprouvé sur une **interface de produit**, le terrain de toutes les références de Junior. | Registre des runs |

Noyau : 32 004 octets sur 33 000.

## 1. Sous-lot 17a — La retenue mesurable

- **A (recommandée).**
  - **Seuil des tailles abaissé** de 10 à **6** (`[À ADAPTER]`). Base : références 1 à 5 tailles, nos rendus 5 à 10.
  - **Nouveau signal : couleurs de texte**, dès 5. Question posée : « Une couleur de texte et un gris par rôle, ou des couleurs qui s'additionnent ? »
  - **`verifier --refs` compare aussi** le nombre de tailles, les couleurs de texte, l'échelle (plus grand texte rapporté au courant) et les mots au premier écran, chacun à la médiane des références. Un écart du simple au double devient une question.
  - **Une ligne nouvelle dans `SAVOIR/STATE` : « Retenue du système ».**
    - *Signal* : beaucoup de tailles, de couleurs ou de bords d'alignement.
    - *Geste* : fusionner les tailles proches, garder une couleur de texte et un gris, aligner sur moins de bords.
    - *Réinspection* : la hiérarchie tient-elle encore ?
  - C'est la moitié manquante de « pousser le geste » : le geste porteur reste, le reste se réduit.
- **B.** Une quatrième variante d'atelier (« réduction »). Je ne la recommande pas : elle ajoute une planche à chaque run, alors que la passe de finition peut porter ce geste.

## 2. Sous-lot 17b — Les procédés du fini

Rien au noyau ; recettes et lignes de `SAVOIR/STATE`, vérifiées dans le navigateur comme les dix recettes actuelles.

- **A (recommandée).**
  1. **Recette `objet-geometrique`.**
     - *Contenu* : un objet en SVG, de face ou en isométrie, au trait et en aplats ; trois tons par face selon une lumière constante ; ombre portée simple.
     - *Quand* : la métaphore du produit est un objet (carte, appareil, document, billet).
     - *Pas quand* : le sujet est organique (personne, animal, plante, paysage).
  2. **Recette `donnees-detail`.**
     - *Procédés* : une valeur distinguée avec sa bulle et une annotation qui raconte (« semaine du Black Friday ») ; hachures pour l'emphase ou le reste ; barres segmentées en traits ; courbe miniature ; puce d'écart.
     - *Ce que la recette garantit* : les totaux se recoupent, et les hachures et couleurs restent lisibles en contraste non textuel.
  3. **Recette `lumiere-verre`.** Un halo dégradé derrière une action, du verre dépoli (flou d'arrière-plan, bord clair de 1 px, repli opaque si le flou n'est pas pris en charge), et le fondu d'une image vers la zone de texte (masque). **Règle de concentration** : une seule zone.
  4. **Recette `matiere` précisée** : l'ordre formes, flou, texture, puis fondu vers la zone de lecture. Et quand les banques d'images échouent, le signal de `verifier --refs` (image manquante) renvoie vers cette recette, au lieu de s'arrêter (constat du run 23).
  5. **`SAVOIR/STATE`** :
     - une ligne « **Profondeur** » : plans distingués par un cran de luminance (fond, carte, élément), sans ombre dure, en sombre comme en clair ;
     - à la ligne « Élément de caractère », deux touches possibles, la **touche de main** (trait, écriture) et l'**annotation** qui désigne l'objet héros, avec leur limite : une police manuscrite de gabarit sonne faux.
  6. **Palette** : quand une image ou une œuvre porte la page, la palette se prélève sur elle (`SAVOIR/CRAFT/CFT-05`).
- **B.** Seulement 1 et 2 : l'objet et la donnée, les deux écarts les plus visibles avec les références de Junior.

## 3. Sous-lot 17c — L'objet géométrique dessiné

- **A (recommandée).** Préciser « Pas de figuratif de mémoire » : un objet **géométrique** se code comme une géométrie (recette `objet-geometrique`), sans déclarer un registre dessiné. Par objet géométrique, on entend un appareil, une feuille pliée, un billet ou un bâtiment simplifié, en isométrie ou de face, au trait et en aplats. Le reste ne change pas : personne, animal, plante et paysage viennent d'un asset ou d'un emplacement marqué. Texte différé, 0 octet au noyau.
- **B.** Ne rien changer : l'agent peut déjà déclarer un registre dessiné.

## 4. Coût et budget

- **Noyau** : 0 octet, sauf si une phrase protégée s'avère utile, auquel cas 100 au plus.
- **Recettes** : environ 12 ko de plus dans `references/recettes.md`.
- **Par run** : plus de signaux de finition, donc probablement quelques corrections de plus, et quelques tours. Non mesuré.

## 5. Gardes et tests (mutation rouge, échec nommé)

- **Signaux** : une page à 7 tailles et une page à 5 couleurs de texte sont signalées ; une page sobre ne l'est pas. Mutation : le signal retiré, et le test doit échouer.
- **`verifier --refs`** : les nouvelles colonnes, et l'écart du double signalé.
- **Recettes** : chacune vérifiée dans le navigateur.
  - `objet-geometrique` : trois tons par face, mêmes proportions à 390 et 1440 px.
  - `donnees-detail` : les totaux se recoupent, et la valeur distinguée a sa bulle.
  - `lumiere-verre` : repli opaque si le flou n'est pas pris en charge, texte lisible sur le verre.
- **Mutation par recette.**
- **Les tests existants dont les pages d'essai franchiront le nouveau seuil** de tailles seront adaptés, et dits dans le rapport.

## 6. Ce que le lot ne prouvera pas

- **Que les rendus deviennent « finis » à ton sens.** Les signaux comptent des décisions, pas la qualité ; une page riche peut être juste.
- **Que les références de présentation transfèrent telles quelles.** Ce sont des images soignées pour être montrées ; certains gris y manquent de contraste.
- **Que l'objet géométrique sera beau.** Un objet SVG mal dessiné est pire qu'une atmosphère ; seule ta lecture le dira.

## 7. Ordre et vérification

1. **17a, 17b et 17c ensemble** : révision `R2026-11-25g`, publication V1.5.0.
2. **Puis un run sur une interface de produit**, ton terrain. Je propose un brief d'une ligne au choix :
   - « l'écran d'accueil d'une application de suivi de dépenses » ;
   - « le tableau de bord d'un petit service d'abonnements ».

   Ou ton brief. Jugement sur ton critère : soigné, fini, abouti, le visuel global.
