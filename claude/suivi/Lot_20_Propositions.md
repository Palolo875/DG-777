# Lot 20 — Propositions : construire au niveau pro

Rédigé le 26 novembre 2026. Base : V1.6.1 (`R2026-11-25i`). C'est la deuxième moitié du plan d'action de l'exploration : après « brancher » (lot 18) et « le niveau pro d'abord » (lot 19, avec le correctif 19b), **écrire la couche de construction qui manque**. Le lot reprend ce qui reste du lot 17. Aucun run. Règle 1 : « D'accord » vaut pour les options A partout.

## 0. Mesure

| Constat | Source |
|---|---|
| Le système **dirige bien et construit mal**. Composition (`BIBLIOTHEQUE/GRID`, `SCENE`) : une taxonomie, sans schéma, sans proportions, sans code. Composants (`COMPONENTS`, `MICRO`) : des contrats. Techniques (`SAVOIR/TECH`) : rien pour sortir de la boîte. Mouvement : des principes, sans exécution. | `Exploration_systeme.md`, sections 2 à 9 |
| **Les recettes marchent** quand elles sont lues : procédé et code, vérifiés dans le navigateur. Onze aujourd'hui (25 789 octets). | Runs 22 à 25 ; `references/recettes.md` |
| **Les références haut de gamme tiennent sur peu de décisions** : 1 à 5 tailles de texte, une famille, une couleur de texte. Nos rendus en ont 5 à 10. Le signal des tailles ne part qu'à **10** ; aucun signal sur les couleurs de texte ; `verifier --refs` ne compare que la part d'image. | `Reverse_2/` ; `parcours.py` (`SEUILS`) |
| Les guides de praticiens donnent des **détails de composants avec des valeurs**, absents du système : ombres en couches, bords semi-transparents et teintés, états plus contrastés que le repos, contour d'image de 1 px, marge d'icône, trait d'icône accordé au texte, coins en superellipse, cibles de 24 et 44 px. | `Exploration_systeme.md`, section 3 |
| **Budgets** : noyau 32 923 sur 33 000 (marge 77) ; étape CONSTRUCTION 37 627 sur 40 000 (marge 2 373) ; étape ESQUISSES 30 467 (marge 9 533) ; tronc DIRECTION 35 177 (marge 4 823). | Mesuré le 26 novembre |
| Coût du run 25 (étapes lues) : +63 % de lecture du cache par rapport au run 23. | `Run25/protocole.md` |

**Conséquence de forme** : la construction va dans les **recettes**, servies par l'outil au moment du choix (`parcours.py recette NOM`). Les routes gardent une ligne et le nom de la recette. Ainsi rien n'entre au noyau, et les étapes grossissent à peine.

**Portée** : tous les rendus, dans leur médium (page, application, composant, affiche, identité, invitation). Les recettes sont en HTML et CSS, le médium de rendu du système. Chacune dit ce qui change en affiche ou en application quand c'est le cas.

## 1. Sous-lot 20a — Composer : grilles et techniques

- **A (recommandée).**
  - **Six fiches de grille en recettes** : modulaire, colonnes, radiale, hiérarchique, ligne de base, axiale. Chaque fiche donne :
    - un schéma rendu, petite image générée par le script, comme les planches de principes ;
    - les proportions de départ et un squelette CSS Grid ;
    - l'adaptation mobile ;
    - l'usage en page, en application et en affiche ;
    - les pièges.
    
    La route `BIBLIOTHEQUE/GRID` garde ses définitions et ajoute, pour chaque grille, « squelette : `parcours.py recette grille-radiale` ». Environ 400 caractères de plus dans l'étape ESQUISSES.
  - **Le tirage annonce la recette de la grille tirée** (« Grille tirée : `GRID/RADIAL` ; squelette : `parcours.py recette grille-radiale` »).
  - **Quatre techniques pour sortir de la boîte, en recettes** :
    - superposition sur une même grille (chevauchement réglé, profondeur par couches) ;
    - découpe et masque (`clip-path`, `mask-image`, avec repli) ;
    - fond perdu et recadrage (image ou forme qui sort du cadre, tenue à 390 px) ;
    - grille rompue (un élément qui casse la grille pour désigner l'idée, le reste aligné).
    
    `SAVOIR/TECH` y renvoie en une ligne.
- **B.** Les six grilles seules, sans les techniques.
- Les scènes (`SCENE/*`, très « produit logiciel ») sont **laissées pour un lot suivant**, sur mesure.

## 2. Sous-lot 20b — Les détails des composants

- **A (recommandée).** Une recette `details-composants` avec code vérifié :
  - ombres en deux couches (ambiante et directe), bord semi-transparent combiné ;
  - bords et ombres teintés vers la couleur d'un fond non neutre ;
  - états survol, appui et focus plus contrastés que le repos, chaque combinaison distincte ;
  - contour intérieur de 1 px sur les images ;
  - marge réduite du côté de l'icône, trait d'icône accordé à la graisse du texte ;
  - coins en superellipse (`corner-shape`) en amélioration progressive, repli rond ;
  - cibles d'au moins 24 px, 44 px au toucher, sans déplacer la mise en page.
  
  La ligne « Partie ordinaire » de `SAVOIR/STATE` y renvoie en une phrase. Environ 150 caractères dans l'étape CONSTRUCTION.
- **B.** Une liste écrite dans `SAVOIR/STATE`, sans code. Je ne la recommande pas : elle grossirait l'étape CONSTRUCTION, déjà à 94 % de son budget.

## 3. Sous-lot 20c — La retenue mesurable (repris du lot 17a)

- **A (recommandée).**
  - Seuil des tailles de texte abaissé de **10 à 6** (`[À ADAPTER]`).
  - Nouveau signal **couleurs de texte**, dès 5.
  - `verifier --refs` compare aussi les tailles, les couleurs de texte, l'échelle (plus grand texte rapporté au texte courant) et les mots au premier écran, chacun à la médiane des références : un écart du simple au double devient une question.
  - Une phrase d'**échelle restreinte** dans `SAVOIR/TYPE` (dans le tronc, marge de 4 823) : « Une échelle se décide en peu de paliers nets, souvent trois à cinq ; deux tailles proches se concurrencent. »
  - Une ligne « **Retenue du système** » dans `SAVOIR/STATE` : fusionner les tailles proches, une couleur de texte et un gris, moins de bords d'alignement.
- **B.** Les seuils seuls.

## 4. Sous-lot 20d — Le mouvement d'interface

- **A (recommandée).** Une recette `mouvement-interface` :
  - durées et courbes par rôle (retour d'appui, apparition, déplacement, sortie) ;
  - retours de survol et d'appui sans déplacer la cible ;
  - échelonnement d'une liste, borné ;
  - transition de vue avec repli ;
  - mouvement réduit respecté.
  
  La ligne « Mouvement » de `SAVOIR/STATE` y renvoie.
- **B.** Rien sur le mouvement dans ce lot.

## 5. Sous-lot 20e — Repris du lot 17b

- **A (recommandée).** Deux recettes :
  - `donnees-detail` : une valeur distinguée avec sa bulle et une annotation qui raconte ; hachures pour l'emphase ou le reste ; barres segmentées ; courbe miniature ; puce d'écart ; totaux qui se recoupent ;
  - `lumiere-verre` : halo derrière une action, verre dépoli avec repli opaque, fondu d'une image vers la zone de texte, concentrés sur une seule zone.
- **B.** Ajouter aussi `objet-geometrique` (objet en SVG, de face ou en isométrie). Je ne le recommande pas maintenant : après le verdict « gadget », un objet dessiné doit d'abord passer le test du produit fini ; on le reprendra s'il manque.
- **Repris aussi** : l'ordre de la recette `matiere` (formes, flou, texture, fondu vers la lecture).

## 6. Coût et budget

- **Noyau : 0 octet.**
- **Étapes** : ESQUISSES environ +400 caractères (marge 9 533) ; CONSTRUCTION environ +300 (marge 2 373). La garde CHG-11 le vérifie.
- **Recettes** : environ 40 à 50 ko de plus (14 recettes), servies une à une, seulement quand l'agent les appelle. Le coût par run ne grandit que de ce qui est lu.
- **Le surcoût des étapes (lot 18) n'est pas traité ici.** Il pourra l'être ensuite en servant des extraits plus courts, sans retirer de contenu utile.

## 7. Gardes et tests (mutation rouge, échec nommé)

- **Chaque recette est vérifiée dans le navigateur** sur sa promesse. Exemples :
  - une grille tient ses colonnes à 1440 et se recompose à 390 ;
  - un masque garde son repli ;
  - un état d'appui ne déplace pas la cible ;
  - les totaux d'un graphique se recoupent.
  
  Une mutation par recette.
- **Les schémas de grille** sont régénérés par leur script et vérifiés comme les planches de principes.
- **Signaux** : une page à 7 tailles et une page à 5 couleurs de texte sont signalées ; une page sobre ne l'est pas.
- **`verifier --refs`** : les nouvelles colonnes, et l'écart du double signalé.
- **Les tests existants dont les pages d'essai franchiront le nouveau seuil** de tailles seront adaptés, et dits dans le rapport.

## 8. Ce que le lot ne prouvera pas

- **Que les rendus deviendront professionnels.** Le savoir sera là et servi au bon moment ; seul ton regard sur un run le dira.
- **Que l'agent appellera les recettes.** Il appelle celles que le tirage, `chantier` ou un signal lui nomment ; les autres dépendent de son jugement. Les renvois depuis les routes servies par les étapes réduisent ce risque.

## 9. Ordre proposé

1. **20a, 20b et 20c**, les plus liés au « basique » : révision `R2026-11-25j`, V1.7.0.
2. **20d et 20e** : révision suivante, V1.7.1 ou V1.8.0.
3. **Puis un run**, sur ta décision, sur un objet qui n'est pas un site, pour éprouver la portée générale.
