# Exploration du système — partie par partie

Ouverte le 25 novembre 2026 sur la demande de Junior : « Les runs ont des composants très basiques, une composition basique, des lignes droites, des rectangles. Je pense que le système a ce qu'il faut. […] Là, c'est quasiment du slop. On va explorer différentes parties du système en général. »

## 0. Premier constat : la mobilisation

**Mesure** (journaux des runs 21 à 24) :
- `agent/chemins.md` cite 96 routes. Les runs ont lu le noyau, le tronc DIRECTION (8 routes) et **11 routes** en plus.
- Routes lues en plus du tronc :
  - DIRECTION/START, EXTERNAL-START et DIVERGENCE ;
  - ACTION/UI-UX-REALITY, ATELIER-EDITION et RECETTE-RENDU ;
  - SAVOIR/TYPE-VOIX et CRAFT/CFT-01 ;
  - TOOLS/CONVERGENCE et MOYENS ;
  - BIBLIOTHEQUE/READ (une fois).
- Tronc DIRECTION : RUN-DIRECTION, CREATIVE-BOOT, VISUAL_TARGET, FIRST-OBJECT, SAVOIR/TYPE, FIRST-RENDER, GATE-A/CONTROLES, BIBLIOTHEQUE/SEQUENCE.

**Jamais lues en quatre runs**, alors que leur signal au noyau est vrai à chaque run DIRECTION (« Structure ouverte », « Forme retenue à construire ») :
- **Composition**, dans `design/formes/catalogue.md` (40 ko) et `choisir.md` (33 ko) :
  - `BIBLIOTHEQUE/SELECT`, `TENSION` ;
  - `SUPPORT` (4 supports), `GRID` (6 grilles : modulaire, colonnes, **radiale**, hiérarchique, ligne de base, **axiale**) ;
  - `SCENE` (6 scènes), `SECTIONS`, `OBJECT`, `MICRO`, `MODIFIER`, `SIGNATURE`.
- **Finition** : `SAVOIR/STATE` (la table des gestes : rayons, masse, vide, surface, détail révélateur, partie ordinaire…). Elle n'est servie qu'en extraits, par les signaux de `verifier`.
- **Créativité et couleur** : `SAVOIR/CRAFT/CFT-02` (axes), `CFT-03`, `CFT-05` (couleur), `CFT-06`.
- **Style, technique, sources** : `SAVOIR/STYLE`, `SAVOIR/TECH`, `SAVOIR/SOURCE`, `SAVOIR/DESIGN-ATLAS`.

**Lecture (probable)** :
- Le système a ce qu'il faut, comme le pense Junior, mais **ce savoir ne sert pas**.
- Le noyau dit de lire une route « quand son signal apparaît ». L'agent juge qu'il n'en a pas besoin et compose de mémoire : deux colonnes, rectangles, filets.
- Les lots d'allègement ont pu y contribuer : 10B (sobriété), 11c (procédures en différé).

## 1. Plan d'exploration

Pour chaque partie :
1. ce qu'elle contient, lu dans les fichiers ;
2. sa qualité propre : concrète et actionnable, ou abstraite ;
3. si les runs l'ont mobilisée, et ce qu'elle aurait changé aux rendus 22 à 24 ;
4. comment la faire servir.

Ordre proposé, du plus lié à la plainte au moins lié :

| # | Partie | Routes | Lien avec « basique » |
|---|---|---|---|
| 1 | Composition et mise en page | `BIBLIOTHEQUE/SELECT`, `TENSION`, `SUPPORT`, `GRID`, `SCENE`, `SECTIONS`, `OBJECT`, `SIGNATURE` | Rectangles, deux colonnes, lignes droites |
| 2 | Composants et micro-interfaces | `BIBLIOTHEQUE/COMPONENTS`, `MICRO`, `MODIFIER`, `SAVOIR/STATE` « Partie ordinaire » | Composants très basiques |
| 3 | Finition | `SAVOIR/STATE`, `CFT-00`, `CFT-02` | Le fini |
| 4 | Couleur et image | `CFT-05`, `CFT-03`, `SAVOIR/SOURCE` | Plat, sans matière |
| 5 | Style et technique | `SAVOIR/STYLE`, `SAVOIR/TECH`, `DESIGN-ATLAS` | Le même profil à chaque run |
| 6 | Typographie | `SAVOIR/TYPE`, `TYPE-VOIX` | Déjà servie : à juger sur sa qualité |
| 7 | Mouvement | `SAVOIR/STATE` « Mouvement », `parcours.py mouvement` | |
| 8 | Direction et idée | `DIRECTION/*`, `CFT-01` | Déjà servie : idée correcte, rendu basique |

Après l'exploration : une décision d'ensemble sur la mobilisation. Plusieurs voies possibles : lecture obligatoire de certaines routes en DIRECTION, tronc élargi, outil qui sert le savoir au bon moment. Rien n'est intégré sans décision.
