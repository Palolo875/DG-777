# Audit neuf — Lot C : les outils de rendu

13 novembre 2026. Révision auditée : `R2026-11-13c`. Document hors du paquet. Rien n'est intégré.

**Lus en entier (4 fichiers, 288 k).** `scripts/parcours.py`, `scripts/check_render.py`, `scripts/regard.py`, `scripts/planche.py`.

**Exécutés, lus par extraits seulement (3 fichiers, 154 k).** `scripts/test_parcours.py`, `scripts/test_check_render.py`, `scripts/test_regard.py`. Ces trois fichiers ne comptent pas comme « lus en entier » au registre.

**Exécuté.** Les trois suites de tests avec navigateur ; trois pages pièges écrites pour ce lot ; la recette et le parcours de vérification sur les pages livrées de cinq runs.

**Statuts.** Certain : lu ou mesuré. Probable : cohérent avec plusieurs observations. **Poids.** Bloquant, important ou mineur.

**Points de vue.** A agent, D designer, I ingénieur, M mainteneur, T intégrité, V preuve.

---

## 1. Verdict du lot

Les outils sont bien construits et honnêtes sur leurs limites. Trois de leurs mesures ne mesurent pas ce que le système croit.

1. **Le code tient** (certain). 425 cas de test passent : 39, 128 et 258. La recette refuse de rendre un `PASS` quand elle ne peut pas conclure.
2. **Le parcours par défaut laisse passer des défauts bloquants** (certain, reproduit). Il vérifie 1440 et 390 px. À 768 px, deux des quatre pages livrées en phase 6 débordent et ont des textes qui se chevauchent.
3. **La mesure de matière dépend de la technique, pas de ce qu'on voit** (certain, reproduit). Une atmosphère entièrement codée compte pour 0 %.
4. **L'outil de matière fournit des images trop petites pour la règle de densité du système** (certain). C'est la cause directe du signal « image sous 2× » dans les runs.

---

## 2. Ce qui tient

| Vérification | Résultat |
|---|---|
| `test_regard.py` | 39 cas, tous verts |
| `test_parcours.py` | 128 cas, tous verts |
| `test_check_render.py` | 258 cas, tous verts (114, 65 et 79 par partie) |
| Correcteur typographique sur une page piège | Juste ; entités, adresses et heures intactes |
| Règle d'accès dans `references` | Identité déclarée, une seule attente d'au plus 60 s (`parcours.py:818-839`) |

À la lecture : la recette applique correctement les seuils de contraste et l'exception d'espacement des petites cibles ; elle mesure le contraste sur le fond réellement peint ; aucun outil n'écrit dans le paquet ; les archives téléchargées ne sont jamais extraites en bloc.

---

## 3. Constat bloquant

### C-01 — Le parcours par défaut ne vérifie pas les largeurs intermédiaires
- **Lieu.** `scripts/parcours.py:2154` (largeurs par défaut « 1440,390 »), `:1485` ; `scripts/check_render.py:1308` (défaut « 390,768,1440 »).
- **Point de vue.** I, V.
- **Constat.** `verifier` passe ses deux largeurs à la recette, dont le défaut propre en compte trois. J'ai repassé la recette à 768 et 1024 px sur les pages livrées :

| Page | Défauts bloquants à 768 ou 1024 px |
|---|---|
| SOM-3 | 2 : débordement horizontal à 768 px (790 px de large), deux textes qui se chevauchent |
| FTX-1 | 2 : débordement à 768 et à 1024 px (1 185 px de large), textes qui se chevauchent |
| FIN-3 | 0 |
| IDT-1 | 0 |
| Chevet | 0 |

  La trace de SOM-3 écrit « `verifier` v9 : 0 défaut bloquant ». C'est vrai aux deux largeurs mesurées, et faux à 768 px.
- **Statut.** Certain, reproduit ici avec la recette du paquet. La cause dans chaque page n'est pas cherchée.
- **Poids.** Bloquant pour ce que le parcours affirme, pas pour le paquet : le noyau dit « recette à toutes ses largeurs ».

---

## 4. Constats importants

### C-02 — La part de matière dépend de la technique employée
- **Lieu.** `scripts/parcours.py:971-1003` ; message en `:1107`.
- **Point de vue.** I, D.
- **Constat.** La mesure compte les images, vidéos, canevas, SVG d'au moins 80 px et fonds en `url()`. Elle ne compte ni dégradé, ni flou, ni matière codée. Sur mes pages pièges : une atmosphère codée de 1 400 px de haut donne 0 % ; des barres de données en `div` donnent 0 %, les mêmes en SVG 6 %.
- **Statut.** Certain, reproduit.
- **Poids.** Important. La route « Atmosphère » conseille d'abord le code natif : l'agent qui la suit garde le signal « matière manquante ». Le message du signal renvoie en outre à « Chercher par rôle », pas aux « Routes par rôle » ajoutées en 13c.

### C-03 — `references` rapporte des images plus petites que la densité exigée
- **Lieu.** `scripts/parcours.py:858` (Commons, miniature de 1 280 px), `:881` (Openverse, vignette d'abord), `:897` (843 px), `:922` (1 k), `:947`, `:966` ; seuil de densité en `:394`.
- **Point de vue.** I, D.
- **Constat.** Aucune option ne va chercher l'original. Or le système exige deux pixels réels par pixel affiché : une miniature de 1 280 px ne suffit plus au-delà de 640 px de large. Sur la page livrée de SOM-3, `verifier` relève la photo à 1,2× et 1,5× pour 744 px affichés.
- **Statut.** Certain.
- **Poids.** Important : un outil crée le défaut qu'un autre signale.

### C-04 — Une image vectorielle est signalée comme floue
- **Lieu.** `scripts/parcours.py:380-383`.
- **Point de vue.** I.
- **Constat.** La densité se calcule sur la taille naturelle de l'image, sans exclure le SVG. Un logo vectoriel de 100 px affiché à 600 px est relevé « 0,2× », alors qu'il reste net à toute taille.
- **Statut.** Certain, reproduit. Aucun test ne couvre ce cas.
- **Poids.** Important pour les runs d'identité, qui livrent des SVG.

### C-05 — Les marqueurs relevés sont ceux des vagues anciennes
- **Lieu.** `scripts/regard.py:583-595`.
- **Point de vue.** I, V.
- **Constat.** Le script ne lit que les listes écrites « Vague N : … » et sait en mesurer douze marqueurs (violet, Inter, fond crème, serif de titre…). Les convergences que le système a lui-même produites depuis octobre (donnée devenue image, grotesque condensée, didone, fiche à filets, capitales espacées) sont en prose : elles ne sont ni listées ni mesurées.
- **Statut.** Certain.
- **Poids.** Important. « Aucun marqueur relevé » devient le résultat normal d'un run qui évite déjà les vagues 1 et 2, sans rien dire de ce qu'il répète.

### C-06 — Une réserve permanente que l'outil voisin sait lever
- **Lieu.** `scripts/check_render.py:1022` ; `scripts/parcours.py:1303-1345`.
- **Point de vue.** I, A.
- **Constat.** La recette garde une réserve « nom accessible calculé non vérifié » dès qu'une page a un contrôle. `parcours.py` calcule pourtant ces noms par l'arbre d'accessibilité du navigateur. La réserve figure à chaque appel des quatre runs, et jusque dans les traces finales.
- **Statut.** Certain.
- **Poids.** Important : une réserve qui ne part jamais apprend à ne plus lire les réserves.

### C-07 — Ni poids ni temps de chargement, et des défauts d'outil qui poussent à tout intégrer
- **Lieu.** `scripts/check_render.py:771` (requêtes externes bloquées par défaut) ; `scripts/parcours.py:2141` (`--integrer`).
- **Point de vue.** D, I.
- **Constat.** Aucun contrôle ne porte sur le poids ou la vitesse d'une page. Les requêtes externes étant bloquées, l'agent intègre polices et images dans le fichier : la page de SOM-3 pèse 506 Ko en un seul fichier.
- **Statut.** Certain pour le code ; probable pour l'effet. Confirme le constat B-09.
- **Poids.** Important pour un niveau professionnel, sans effet sur une démonstration.

---

## 5. Constats mineurs

| N° | Lieu | Vue | Constat | Statut |
|---|---|---|---|---|
| C-08 | Mesuré sur la page de SOM-3 | V | Un appel de la recette prend 31 s et affiche 4 658 caractères ; un appel de `verifier` prend 39 s, affiche 2 753 caractères et écrit 13 fichiers (22 Mo). La recette répète à chaque appel un paragraphe de limites de 1 871 caractères | Certain, dans cet environnement |
| C-09 | `test_parcours.py:743` | I, V | Les tests vérifient que la mesure de matière existe, pas ce qu'elle compte ; rien sur la densité d'un SVG | Certain (recherche dans le fichier) |
| C-10 | `parcours.py:1112-1157` | I | Une référence qui répond par une page d'attente ou un bandeau de consentement serait mesurée comme la page réelle | Certain pour le code ; risque probable |
| C-11 | `regard.py:129-170` ; `check_render.py` | M | Le contraste sur capture est codé deux fois, dans deux outils | Certain |
| C-12 | `parcours.py:1700-1701` contre `composition.md:69` | A | Le correcteur met une espace fine dans les guillemets ; le savoir demande une espace insécable | Certain, reproduit |
| C-13 | `regard.py:636`, `:836` ; `parcours.py:1107` | M | Trois renvois périmés dans les outils : « Réutilisation située » dans `FIRST-OBJECT`, « Chercher par rôle » | Certain |
| C-14 | `parcours.py:160` | T | Le téléchargement des polices se présente comme « Mozilla/5.0 … Chrome/124 DesignGovernance ». À rapprocher de la règle « jamais en masquant son identité » | Certain ; à trancher |
| C-15 | `parcours.py:53` ; `check_render.py:756` ; `regard.py:708` | I | La hauteur de fenêtre change à 768 px dans un outil, à 700 px dans les deux autres | Certain |
| C-16 | `regard.py:9`, `:774` | I | La carte d'attention utilise par défaut une approximation que l'outil qualifie lui-même de « signal faible » | Certain |
| C-17 | `parcours.py:1800` | I, M | Le tirage lit ses pistes dans la prose d'une règle, par expression régulière ; un garde-fou signale l'échec | Certain |
| C-18 | `planche.py:63` | D | La planche montre chaque esquisse à moitié de sa taille. Elle sait aussi montrer le mobile : c'est le noyau qui le désactive (`--bureau-seul`), donc le constat A-10 se corrige sans code | Certain |

---

## 6. Propositions (non intégrées)

1. **Vérifier une largeur intermédiaire par défaut** (C-01) : `verifier` à 1440, 768 et 390 px. Coût : un tiers de temps en plus par appel.
2. **Dire ce que la mesure de matière compte** (C-02), ou la faire porter sur l'image rendue plutôt que sur les balises. À discuter : c'est la mesure sur laquelle repose ton prochain run.
3. **Donner à `references` une option pour l'original** (C-03), licence lue, quand l'image est destinée à être intégrée.
4. **Exclure le vectoriel du signal de densité** (C-04), avec son test.
5. **Faire entrer dans le relevé les convergences produites par le système** (C-05), ou dire dans la fiche qu'elles ne sont pas mesurées.
6. **Lever la réserve des noms quand l'arbre d'accessibilité les donne** (C-06).
7. **Corrections mineures groupées** (C-11 à C-15).

---

## 7. Ce que ce lot n'a pas vérifié

- **Les trois fichiers de tests** : exécutés en entier, lus par la liste de leurs cas et par recherche ciblée, pas ligne à ligne.
- **Quelques lignes très longues** de `check_render.py` et de `regard.py` ont été lues coupées à 900 caractères.
- **Les fonctions réseau** (`references`, `polices`, `icones`) n'ont pas été exécutées contre les sources réelles.
- **La cause des défauts à 768 px** dans SOM-3 et FTX-1 n'est pas cherchée ; les pages n'ont pas été regardées à cette largeur.
- **Les seuils** des signaux de finition, d'identité et de marqueurs n'ont pas été éprouvés au-delà de ce que les tests couvrent.
- **Le modèle d'attention appris** (option `onnx`) n'est pas dans le paquet et n'a pas été essayé.
