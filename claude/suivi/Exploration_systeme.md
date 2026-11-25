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

## 2. Double recherche (25 novembre, « À toi le choix »)

### 2.1 Interne : le contenu des routes de composition est-il assez concret ?

**Lu** : `design/formes/catalogue.md`, sections `BIBLIOTHEQUE/GRID` et `BIBLIOTHEQUE/SCENE`.

- **Forme des fiches** : une définition (« Unités répétables : cellules, blocs… »), « Choisir lorsque », « Éviter lorsque », une « Preuve » abstraite (« les cellules créent rythme et priorité »).
- **Ce qui manque** : aucun schéma, aucune proportion, aucun squelette de code, aucun exemple, aucun piège d'exécution. Comment se construit une grille radiale ou axiale en page web ? La fiche ne le dit pas.
- **Portée** : le catalogue le reconnaît lui-même : « Les scènes, objets et micro-unités de ce catalogue viennent surtout du produit logiciel et du B2B. »

**Conclusion (probable)** : ces fiches sont une **taxonomie de jugement**, pas un **savoir de construction**. Même lues, elles aideraient à nommer un choix, peu à l'exécuter. À l'inverse, les recettes (procédé et code) sont utilisées et tiennent quand l'agent les lit.

### 2.2 Externe : ce que disent les pratiques et la recherche

Lu dans les résumés des résultats de recherche ; **non vérifié en détail**.

- **Mobilisation**
  - Les guides de compétences d'agents recommandent de **dire quand lire** chaque fichier de référence, plutôt que de laisser l'agent le déduire. Un catalogue de techniques traite précisément de la « paresse » des agents, qui sautent les références et improvisent.
  - Autre conseil : **faire exécuter un script** plutôt que lire un fichier.
  - C'est ce que montrent nos journaux : ce qu'un outil sert est utilisé ; ce qui dépend du jugement de l'agent ne l'est pas.
- **Diversité**
  - Un article (« Mine, Sample, Render », arXiv) constate que les pages web générées par les modèles **convergent vers un même aspect et une même structure**.
  - Le même article montre qu'un **schéma de structure imposé à la génération** augmente la diversité visuelle et structurelle, par rapport à une consigne seule. C'est l'équivalent de notre tirage, étendu à la structure.
- **Qualité de mise en page** : plusieurs travaux améliorent la mise en page en **récupérant des exemples pertinents**, au lieu de définitions :
  - APD-agents (récupération d'exemples pour des écrans d'application) ;
  - LayoutCoT (génération augmentée par récupération, attentive à la mise en page) ;
  - MM-WebAgent (révision sur capture, ce que fait déjà notre atelier).
- **Empreintes de génération** : police Inter, dégradés violet-bleu, cartes très arrondies à ombre douce, héro centré. Le système les traite déjà, par la convergence et l'habillage de gabarit.

### 2.3 Ce qui en sort (pistes, rien de décidé)

1. **Changer la forme du savoir de composition.** Chaque scène et chaque grille devient une **fiche de construction**, sur le modèle des recettes :
   - un schéma (une petite image ou un squelette rendu) ;
   - des proportions ;
   - un squelette de code ;
   - un exemple d'usage ;
   - ses pièges ;
   - « choisir lorsque », gardé.

   Les recherches sur la récupération d'exemples vont dans ce sens.
2. **Servir par l'outil, à une étape obligatoire.**
   - `tirage` tire aussi une structure (scène, grille) pour l'une des esquisses, comme le schéma imposé de l'article sur la diversité. C'est notre levier le plus fort.
   - `chantier` sert les fiches tirées.
3. **Dire quand lire, dans le noyau.** Remplacer « lis X si le signal apparaît » par une étape : « avant les esquisses, lis les fiches de structure servies par `chantier` ».
4. **Faire choisir par code et le tracer** : scène, grille et objet dans la ligne « modal, trame et parti », relevés par `trace`.
5. **Vérifier la mobilisation** : un signal si un run DIRECTION n'a lu aucune fiche de structure.

Sources (lues dans les résumés de recherche) : [skill-reach, progressive disclosure](https://google.github.io/skill-reach/concepts/progressive-disclosure/) ; [Preventing Agent Laziness in Skill References](https://wenbo97.github.io/prompt-context-patterns/catalog/techniques/anti-laziness) ; [Agent Skill best practices](https://geminicli.com/docs/cli/skills-best-practices/) ; [Mine, Sample, Render](https://arxiv.org/pdf/2610.21185) ; [WebGen-V Bench](https://arxiv.org/html/2510.15306v1) ; [MM-WebAgent](https://arxiv.org/pdf/2604.15309) ; [LLMs as Layout Designers](https://arxiv.org/pdf/2509.16891) ; [UI-Bench](https://arxiv.org/pdf/2508.20410) ; [How to fix the AI-generated look](https://dev.to/alanwest/how-to-fix-the-ai-generated-look-in-your-frontend-1ahh).

## 3. Partie 2 — Composants et micro-interfaces

**Interne (lu)**
- **`BIBLIOTHEQUE/COMPONENTS`** décrit des **couches et un contrat de composant partagé** : jetons, grammaire de marque, primitives, objets, scènes, gabarits ; intention, slots, jetons consommés, variantes, états, responsive, frontières de composition. C'est de la **gouvernance**, utile à un système de design partagé, muette sur l'aspect d'un bon bouton, d'une bonne carte ou d'un bon champ.
- **`BIBLIOTHEQUE/MICRO`** décrit sept micro-interfaces (réglages, profil, santé d'une requête, rail d'état, itinéraire, registre d'usage…) par leur **responsabilité et leur vérification** : bonne sur le fond (« un graphique écrit sa conclusion », « la couleur suit le sens de la mesure »), sans procédé visuel.
- **Le savoir visuel des composants** vit ailleurs : la table des gestes de `SAVOIR/STATE` (rayons, surface, alignement optique, partie ordinaire…) et la recette `controles`. Cette table est **concrète** (formule du rayon intérieur, liseré de 1 px, figures tabulaires), mais elle n'est servie **qu'en réaction**, par fragments, quand `verifier` émet un signal. Jamais comme guide de construction avant le premier build.

**Externe** : les guides de praticiens sont des **listes de détails concrets, avec des valeurs**. Sources : Web Interface Guidelines de Vercel et de Rauno Freiberg, aide-mémoire interfaces.dev et BoringUI. Présents chez eux, absents du système :
- **ombres en couches** (lumière ambiante et directe, au moins deux couches) ;
- **bords nets semi-transparents** combinés à l'ombre ;
- **bords et ombres teintés** vers la teinte d'un fond non neutre ;
- **états qui augmentent le contraste** (survol, appui, focus plus contrastés que le repos ; chaque combinaison distincte) ;
- **contour intérieur de 1 px** sur les images (8 % de noir en clair, 8 % de blanc en sombre) ;
- **marge réduite du côté de l'icône** dans un bouton ;
- **trait d'icône accordé à la graisse du texte voisin** ;
- **coins en superellipse** en amélioration progressive ;
- **cibles d'au moins 24 px**, 44 px au toucher.

Déjà dans le système : rayons emboîtés, alignement optique, focus visible, libellés, erreurs près du champ.

**Conclusion (probable)** : les composants sont basiques parce que le système les traite en **contrat** (ce qu'ils doivent garantir) et en **correction** (ce que `verifier` relève après coup), pas en **construction** (comment les dessiner bien du premier coup).

## 4. Partie 3 — Finition

- **`SAVOIR/STATE`** est la partie la plus proche des guides de praticiens : symptôme, geste concret, condition, réinspection. Sa qualité est bonne.
- **Ses deux faiblesses**
  - **Elle arrive tard** : la passe de finition et les signaux de `verifier`, après le premier build.
  - **Il lui manque les détails de la liste ci-dessus** : ombres en couches, teinte des bords, états, contour d'image, icônes.
- **Six planches de principes** existent (`design/principes/*.png` : accent de foyer, chiffres, fonds voisins, grand titre, masse visuelle, rayons). Ce sont les seuls exemples visuels du système. Aucun run ne les a ouvertes.

## 5. Partie 5 (avancée) — Techniques de composition

- **Interne** : `SAVOIR/TECH` (13 ko) traite de la hiérarchie de jugement, de l'amélioration progressive, des médiums, de la recherche de méthode, des transitions et du mobile. **Aucune technique pour sortir du rectangle.**
- **Externe** : les techniques sont documentées et simples :
  - superposer des éléments sur une même grille (CSS Grid avec chevauchement et `z-index`) ;
  - découper par `clip-path` et `mask-image` ;
  - faire épouser une forme au texte (CSS Shapes) ;
  - rompre la grille par contenants, couches, vide ou gouttières (maçonnerie) ;
  - révéler partiellement par une fenêtre découpée.

  Un article (« Breaking the Layout Monoculture ») traite précisément de la monoculture des mises en page.
- **Conclusion** : la composition basique a deux causes. Le savoir de composition est une taxonomie (partie 1), et **le savoir-faire technique pour construire autre chose qu'une boîte manque** (partie 5).

Sources (lues dans les extraits) : [Vercel, Web Interface Guidelines](https://vercel.com/design/guidelines) ; [interfaces.dev, cheat sheet](https://interfaces.dev/cheat-sheet) ; [BoringUI, Interface Cheat Sheet](https://boringui.dev/docs/interface-cheat-sheet/) ; [Rauno Freiberg, Web Interface Guidelines](https://interfaces.rauno.me/) ; [Chrome, natural interactions](https://developer.chrome.com/docs/modern-web-guidance/guides/user-experience/natural-interactions) ; [Codrops, cutout collage with CSS Grid and clip-path](https://tympanus.net/codrops/2020/02/05/crafting-a-cutout-collage-layout-with-css-grid-and-clip-path/) ; [Mandy Michael, 3D layout with CSS Grid](https://javascript.plainenglish.io/creating-3d-layout-with-css-using-grid-perspective-65cd03dfc56c) ; [Breaking the Layout Monoculture](https://design.cnbb.pub/research/breaking-the-layout-monoculture/) ; [Escaping Gridlock](https://usabilitygeek.com/when-how-break-grid-layout/) ; [web.dev, CSS Shapes](https://web.dev/articles/shapes-getting-started).

## 6. Partie 4 — Couleur et image

**Couleur (`SAVOIR/CRAFT/CFT-05`)** : **la partie la plus solide lue jusqu'ici.** Elle est concrète et chiffrée :
- la valeur avant la teinte (en OKLCH, des écarts de L donnés pour 3:1 et 4,5:1) ;
- des neutres teintés d'une chroma de 0,005 à 0,02 ;
- des fonds voisins distingués par la luminosité, avec une planche ;
- l'accent de marque distinct de l'accent de foyer, avec une planche ;
- en sombre, « l'élévation par pas de luminosité des surfaces plutôt que par des lueurs » : **la profondeur par la luminance des références de Junior y est déjà**, contrairement à ce qu'écrit le lot 17 ;
- la variable visuelle accordée à la donnée (polarité, grandeur, ordre).

**Mais le détail n'est jamais lu** : seule la ligne du noyau (palette par rôles) arrive au run. Correction à porter au lot 17 : la « profondeur par la luminance » n'est pas à créer ; il faut la faire servir.

**Image (`SAVOIR/SOURCE`)** :
- **Contenu riche** : test d'utilité de l'ancre, recherche orientée décision, collections ouvertes, routes par rôle, curer et intégrer, diriger une génération, construire une atmosphère.
- **Les runs ont un frein qui ne vient pas du système, mais de nos conditions de test** : génération d'images interdite, banques ouvertes qui refusent ou ne donnent rien (Commons en 429 au run 23), interdiction justifiée de présenter une fausse photo. **Les références de Junior vivent d'images** : illustrations, 3D, photos, logos réels. Nos runs plafonnent donc en partie à cause du protocole.

**À décider** : ouvrir, dans un prochain run, la génération dirigée et marquée (le système la prévoit : « Diriger une génération »), pour mesurer ce plafond ? C'est une piste déjà notée : « obtenir l'accord pour la génération d'images quand personne n'est là ».

## 7. Partie 5 — Style

**`SAVOIR/STYLE`** propose huit profils, avec intention et marqueurs :
- `RAW_BRUTALISM` ;
- `EDITORIAL_PRECISION` ;
- `PICTORIAL_UTILITY` (l'image ou l'illustration qui explique) ;
- `QUIET_SYSTEM` ;
- `MAXIMAL_EXPRESSION` ;
- `DIGITAL_MEMORY` ;
- `TACTILE_VOLUME` (volume doux, ombres calibrées) ;
- `COLLAGE_ASSEMBLY` (fragments, découpes).

S'y ajoutent des réglages (« dials ») et une taxonomie de registre.

- **Les runs restent dans `EDITORIAL_PRECISION` ou `QUIET_SYSTEM`** (le profil « éditorial imprimé » observé), sans jamais lire la route.
- **Plusieurs références de Junior relèvent de profils jamais pris** : `TACTILE_VOLUME` (applications aux volumes doux), `PICTORIAL_UTILITY` (carte pliée, téléviseur), `COLLAGE_ASSEMBLY` (collage de tableaux).
- **La règle tient le profil à distance** : « Aucun profil n'est choisi par défaut », « retenu seulement s'il modifie une décision ». L'agent n'en retient jamais. Son défaut, c'est l'éditorial.
- **Forme** : une ligne de tableau par profil. Plus concret que les scènes (des marqueurs sont donnés), mais sans exemple ni procédé.

## 8. Bilan provisoire (parties 1 à 5)

| Partie | Qualité du contenu | Mobilisation |
|---|---|---|
| Composition | Taxonomie abstraite | Jamais lue |
| Composants | Contrats et gouvernance, pas de construction | Jamais lue |
| Finition | Bonne, concrète ; il manque des détails | Servie après coup, par fragments |
| Techniques | Rien pour construire autre chose qu'une boîte | Jamais lue |
| Couleur | **Très bonne**, chiffrée, avec planches | Seule la ligne du noyau arrive |
| Image | Riche | Bloquée par le protocole (pas de génération, banques en échec) |
| Style | Huit profils, réglages ; peu d'exemples | Jamais lue ; défaut éditorial |

**Deux problèmes distincts** :
1. **La mobilisation, partout.** Même le meilleur savoir (couleur) n'arrive pas.
2. **La forme du savoir, par endroits.** Composition, composants et techniques sont abstraits ou orientés gouvernance là où il faudrait de la construction.
