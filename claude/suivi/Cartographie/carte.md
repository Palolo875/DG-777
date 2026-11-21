# Cartographie du système — R2026-11-15o

Établie le 21 novembre 2026. Schéma : `carte-systeme.svg` (et sa version `.png`).

**Méthode** : mesures tirées du paquet, avec le lecteur de routes, le registre du noyau et le manifeste. L'usage vient des journaux des runs 9 à 18 (12 runs, PILOT compris).

**Limites de la mesure** :
- la taille d'une route compte aussi ses sous-routes ;
- les citations entre routes sont relevées par motif de code ;
- « lue » veut dire servie par le lecteur, ce qui ne prouve pas que l'agent l'a lue.

## 1. Les sept couches

| Couche | Ce qu'elle contient | Chiffres |
|---|---|---|
| ① Noyau (`SKILL.md`) | Ce que l'agent lit à chaque demande | 45 810 octets sur 46 000 ; 6 962 mots ; 36 blocs ; 62 codes distincts |
| ② Modes et troncs | Lecture fixe par mode | LITE 8 k car., ITER 5,6 k, STANDARD 7 k, SYSTÈME 7,8 k, **DIRECTION 31,4 k** (budget 35 k) |
| ③ Quatre modules de routes | DIRECTION, SAVOIR, BIBLIOTHEQUE, ACTION | 85 routes, environ 500 k caractères |
| ④ Outils | `parcours`, `check_render`, `regard`, `planche`, `read_route`, journal | Environ 5 600 lignes ; 13 sous-commandes de `parcours` |
| ⑤ Contrôle de soi | Validateurs et tests | Environ 9 400 lignes ; 111 codes de garde ; environ 785 cas de test |
| ⑥ Gouvernance | Schémas, exemples, fixtures, validateurs de fiche | 45 fichiers sur 151 ; environ 30 valeurs de statut |
| ⑦ Pour les personnes | README, 3 guides, glossaire, 3 cartes, maintenance | Français seul ; pas de licence |

## 2. Ce que la carte révèle

### 2.1 Le poids est dans le savoir, l'usage est dans la procédure (certain)

| Module | Routes | Taille | Lues au moins une fois en 12 runs |
|---|---|---|---|
| SAVOIR | 17 | **180 k car.** (le plus gros) | 6 : TYPE, TYPE-VOIX, STATE, SOURCE, IDENTITY, CONTEXT. **FRAME, CRAFT et STYLE : 0** |
| ACTION | 29 | 125 k | 6, plus GATE-A/CONTROLES (sous-route, 8 fois). **GATE-B et STATUS : 0** |
| DIRECTION | 20 | 108 k | 6 : FIRST-OBJECT, VISUAL_TARGET, CREATIVE-BOOT… |
| BIBLIOTHEQUE | 19 | 86 k | 3 : SEQUENCE (8 fois), SELECT, MICRO. **READ : 0** |

Sur les 85 routes : **21 lues au moins une fois, 13 proposées mais jamais lues, 51 jamais touchées (60 %)**.

La plus grosse route du paquet, `SAVOIR/CRAFT` (44,6 k caractères, la qualité créative), n'a jamais été ni lue ni proposée par un outil.

### 2.2 Le graphe est centré sur la procédure (certain)

- **Les routes les plus citées par les autres** sont des routes de procédure ou de gouvernance :
  - `DIRECTION/START` (18 entrants) ;
  - `DIRECTION/VISUAL_TARGET` (16) ;
  - `ACTION/CLOSE-PACKAGE` (14) ;
  - `ACTION/STATUS` (13).
- **Le savoir de goût est en bout de chaîne.** FRAME est citée par 5 routes, READ par 2. Elle n'est jamais un point de passage.
- **Quatre routes ne sont citées par aucune autre** : `BIBLIOTHEQUE/SUPPORT`, `/GRID`, `/MODIFIER` et `ACTION/RUN`. Elles restent atteignables par le lecteur et par les tables.

### 2.3 Le noyau est surtout de la procédure (certain)

Répartition des 42 949 octets des 36 blocs du noyau :

| Fonction | Part | Fichiers sources |
|---|---|---|
| Procédure de direction | **49 %** | `diriger.md` (12,1 k), `standard.md` (5,2 k), `cadrer.md`, `premier-objet.md`, `boucle.md` |
| Chargement, chemins et réponse | **23 %** | `agent/chemins.md` (6,3 k), `agent/repondre.md` (3,6 k) |
| Savoir de goût | **13 %** | `qualite-creative.md`, `typographie.md`, `fondements.md`, `composition.md`, `choisir.md` |
| Atelier et finition | 9 % | `finition.md` |
| Gouvernance | 5 % | `integrite.md`, `pipeline.md`, `statuts.md` |

Plus gros blocs : `CHARGE-DETAILS` (5,1 k), `DIR-LEVIERS` (5,0 k), `BOUCLE-ATELIER` (3,9 k), `MOY-PLAFOND` (3,4 k), `DIR-DECLARATION` (2,9 k).

### 2.4 Le tronc DIRECTION est presque entièrement de la procédure (certain)

- Ses 8 routes : RUN-DIRECTION, CREATIVE-BOOT, VISUAL_TARGET, FIRST-OBJECT, TYPE, FIRST-RENDER, GATE-A/CONTROLES, SEQUENCE.
- **Une seule est du savoir : TYPE.**
- **Lecture fixe d'un run DIRECTION** : noyau plus tronc, environ 77 k caractères, soit environ 20 à 25 k tokens, avant tout travail. Un run complet en a consommé 250 à 330 k.

### 2.5 Le canal qui marche, ce sont les outils (certain pour l'usage, probable pour l'effet)

- `verifier` a tourné dans 8 runs sur 8, et `tirage` aussi.
- `leviers` a été appelé dès qu'il a existé (2 runs sur 2).
- Ces outils **lisent le savoir à son lieu et servent la bonne ligne au bon moment** : les gestes de STATE, les leviers de READ, les pistes, les marqueurs de vague.
- Les routes, elles, attendent qu'on les lise, et on ne les lit pas.
- C'est le constat transversal de la lecture du système (notes 12 à 16) et des lots 9b à 9e. **La vraie interface du système est `parcours.py`, pas la bibliothèque de routes.**

### 2.6 Le système se contrôle plus qu'il ne produit (certain pour les chiffres)

- **Lignes de code** : environ 9 400 lignes de contrôle (validateurs et tests), contre environ 5 600 lignes d'outils de production.
- **Ce que vérifient les 111 gardes** : la forme du texte (longueur des cellules, vocabulaire, vouvoiement, liens, planchers) et le comportement des outils. **Aucune ne porte sur la qualité d'un rendu**, et c'est voulu : la qualité se juge à la vue.
- **Le coût** : chaque changement passe par environ 12 minutes de préparation, et une petite modification de texte peut échouer sur une garde de forme. Cela s'est produit 3 fois sur les lots 9b à 9e (LIS-01 deux fois, et une référence de fichier).

### 2.7 La gouvernance est lourde pour un usage qui ne s'en sert pas (certain)

- 45 fichiers sur 151 (schémas JSON, fixtures, exemples, validateurs de fiche).
- Environ 30 valeurs de statut :
  - 7 états ;
  - 6 issues ;
  - 6 verdicts globaux ;
  - 4 axes avec 5 statuts chacun ;
  - 4 statuts de direction ;
  - 5 conséquences décisionnelles.
- Aucun des 12 runs n'en a eu besoin : tous étaient en trace légère.

### 2.8 Plusieurs « ordres » se superposent (certain)

FRAME distingue lui-même **quatre ordres** :
- ce qui prime en cas de conflit ;
- l'ordre de construction ;
- l'ordre d'examen (P0 à P3) ;
- l'ordre de correction sur un brief vague.

S'y ajoutent la chaîne promesse → objet de preuve → geste, la boucle d'édition en 8 temps et la chaîne support → grille → scène → objet → primitive. Chacun est juste dans son cadre, mais l'ensemble est difficile à tenir en tête, pour un agent comme pour une personne.

## 3. Ce que cela veut dire pour une présentation

| Couche | Maturité | Ce qu'un expert verra |
|---|---|---|
| Outils (④) | **Bonne** : utilisés, testés, efficaces au PILOT | L'atout le plus convaincant, à montrer en premier |
| Contrôle (⑤) | **Très bonne**, peut-être excessive | Une rigueur rare ; le coût de modification peut inquiéter |
| Noyau et troncs (①, ②) | **Moyenne** : lourds, centrés sur la procédure | Trop long pour une skill, et le goût y tient peu de place |
| Bibliothèque de routes (③) | **Faible en usage** : 60 % jamais touchée | Un corpus riche mais dormant |
| Gouvernance (⑥) | Complète mais inutilisée en pratique | À présenter comme un module optionnel |
| Pour les personnes (⑦) | Correcte | Manquent une licence, une vitrine et une phrase de positionnement |

**Lecture d'ensemble (probable).** Le système a grandi comme une **bibliothèque de règles avec un appareil de contrôle**. Ce qui produit l'effet observé est **une couche d'outils qui sert le savoir au bon moment**. Une version présentable mettrait cette couche au centre :

**un noyau court, des outils comme interface principale, et une bibliothèque consultée par les outils plutôt que par l'agent.**

C'est une hypothèse d'architecture, pas une décision. Elle demanderait un lot à part, mesuré contre l'actuel, ce qui veut dire des runs.
