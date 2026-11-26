# Lot 14 — Propositions : voir, et oser

Rédigé le 25 novembre 2026. Base : V1.1.1 (`R2026-11-15y`, `master` `8f32436`). Aucun run dans ce lot. Règle 1 : rien n'est intégré sans décision ; « D'accord » vaut pour les options A partout.

## 0. Pourquoi ce lot

La discussion du 25 novembre (`Pistes_25_novembre.md`, `Run21/protocole.md`) conclut, avec l'accord de Junior : **le système est optimisé contre l'échec, pas pour la grandeur.** Il tient le plancher (vérité, fonction, finition, coût). Il aide peu l'agent à **voir** (l'agent juge son propre travail), et tout ce qui pousse vers l'audace y est conditionnel, alors que tout ce qui freine est systématique.

**Constats (runs 19x, 20x, 21y)** :
- deux pertes d'expression relevées par Junior sont des éléments **retirés à l'atelier** : le tampon de l'invitation, le cadre sombre du livre de la fonderie ;
- le premier écran mobile de la fonderie a perdu l'idée, sans qu'aucun contrôle le voie ;
- l'atelier fait un test de retrait à chaque fois ; la variante qui **intensifie** ne se construit « que si la capture la montre timide », et l'agent ne juge presque jamais son rendu timide.

**Ce qui existe déjà** : la règle « Classique et expressif » (`SAVOIR/FRAME`) ; la lecture sans le texte (`regard.py`, au bureau) ; l'atelier avec test de retrait (`ACTION/ATELIER-EDITION`) ; les captures par version (`captures --version`).

Le lot ne touche que des outils et quelques lignes. **Son effet sur les rendus ne se mesurera qu'en run** (campagne groupée, plus tard, sur décision de Junior).

## 1. Sous-lot 14a — Voir

### V1 — Comparer chaque version à l'esquisse retenue
- **A (recommandée).** `parcours.py captures --version vN --contre ESQUISSE.html` ajoute, sur la même planche, l'esquisse gagnante de la planche de divergence, au même cadrage, au bureau et sur téléphone. La ligne d'atelier gagne une question : « l'idée se lit-elle aussi vite qu'à l'esquisse ? Sinon, ce qui la portait revient. »
- **B.** Seulement la question, sans outil.

### V2 — La lecture sans le texte, aussi sur téléphone
- **A (recommandée).** La lecture sans le texte de `regard.py` est produite aussi au premier écran à 390 px, et l'atelier la fait aux deux largeurs : « l'idée survit-elle à la recomposition ? ».
- **B.** Rien ; la règle « en mobile, l'idée survit » reste une phrase.

### V3 — Le retrait protège ce qui porte l'idée
- **A (recommandée).** Le test de retrait garde sa règle (« ce qui ne manque pas part »), avec une exception écrite : **l'élément qui porte l'idée ne part pas** ; s'il manque à la lecture sans le texte, il revient. L'agent nomme cet élément dans la déclaration (ligne `REGISTRE` ou `ASSET`).
- **B.** Rien.

## 2. Sous-lot 14b — Oser

### N — Un atelier symétrique
- **A (recommandée).** Après la première capture, deux variantes au même niveau de finition, toujours : le **retrait** (comme aujourd'hui) et l'**intensification** de l'élément qui porte l'idée (échelle, contraste, fond perdu, matière, cadrage). Les trois versions se comparent sur une planche ; on garde la plus forte, et « garder l'actuelle » reste un résultat valide.
  - Coût : une variante de plus par run, environ 2 à 4 tours.
- **B.** L'intensification reste conditionnelle, mais l'agent doit écrire pourquoi il ne la juge pas nécessaire.

### O — Le niveau d'expression déclaré
- **A (recommandée).** La ligne `NIVEAU` de la déclaration dit aussi l'**expression attendue** : *sobre*, *affirmée* ou *expressive*, déduite du sujet, du public et de la destination (une invitation de galerie n'appelle pas la même chose qu'un widget de marées). L'atelier juge l'intensification contre ce niveau. Elle s'appuie sur la règle « Classique et expressif », sans la changer.
- **B.** Rien.

### Q — Une ambition au-delà du plancher
- **A (recommandée).** Une phrase au noyau, dans le rôle ou la boucle : « Le plancher protège ; le geste qui porte l'idée se pousse jusqu'au bout. La retenue porte sur le reste, pas sur lui. »
- **B.** Rien au noyau ; la phrase va dans `DIRECTION/STANDARD`.

## 3. Sous-lot 14c — Mesurer et juger (sans run)

### C — Quatre signaux de finition dans `verifier`
- **A (recommandée).** Texte trop près du bord de la fenêtre ; contraste des éléments graphiques porteurs d'information (WCAG 1.4.11) ; contraste sur chaque image du mouvement ; commandes personnalisées manipulées au clavier. Mesurer la longueur de la fiche avant et après.
- **B.** Reporter.

### H — Le mouvement jugé
- **A (recommandée).** Pour un rendu animé, `parcours.py mouvement --video` enregistre une courte vidéo du moment orchestré ; le protocole d'évaluation la joint aux planches de jugement.
- **B.** Reporter à la campagne de runs.

**Reportées** : B (signaux de hiérarchie), A (gestes de composition écrits), G (signaux de mouvement), K (mesure de variété), Q1-3 (goût par l'exemple), et tout le bloc « Faire » (recettes F, matière E et D, inventaire du sujet I et M, rareté J), prévu pour un lot 15.

## 4. Gardes et tests (mutation rouge, échec nommé)

- V1 : la planche `--contre` contient l'esquisse et la version, aux deux largeurs.
- V2 : `regard.py` produit la lecture sans le texte à 390 px.
- V3, N, O, Q : formulations protégées au noyau (CORE-01) ; la ligne de déclaration `NIVEAU` demande l'expression (test de forme de la trace).
- C : chaque signal a son cas positif et son cas négatif.
- H : la vidéo est produite, et rien ne bouge en mouvement réduit.

## 5. Coût et budget

- Le noyau est à 31 127 octets sur 31 500 : les lignes de V1, V3, N, O et Q demanderont environ 600 octets. **Budget à relever vers 32 000**, ou à financer en raccourcissant une ligne existante (je montrerai laquelle).
- Le tronc DIRECTION ne bouge pas.
- Chaque run fera environ une variante de plus (N) : quelques tours de plus, contre un rendu plus affirmé, à vérifier en run.

## 6. Ce que le lot ne prouvera pas

- Que les rendus deviennent plus audacieux, ni qu'ils restent justes : seuls des runs jugés par Junior le diront.
- Le risque inverse existe : un atelier qui intensifie toujours peut pousser vers l'excès. La parade est la comparaison des trois versions, et « garder l'actuelle » reste valide.

## 7. Ordre proposé

1. **14a** (voir) : révision `z`.
2. **14b** (oser).
3. **14c** (mesurer et juger).

Puis le lot 15 (faire), puis une seule campagne de runs, sur décision de Junior.
