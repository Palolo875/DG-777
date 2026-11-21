# Audit neuf — Lot A : le chemin de l'agent

13 novembre 2026. Révision auditée : `R2026-11-13c`. Document hors du paquet. Rien n'est intégré.

**Lus en entier (17 fichiers, 209 k).** `SKILL.md`, `agent/` (3), `sections/` (6), `design/README.md`, `design/direction/` (6).

**Exécuté.** Résolution des 100 renvois de route du lot ; comparaison des blocs marqués « noyau » au noyau compilé ; `build_core.py --check` ; aide de chaque commande citée ; troncs des cinq modes ; gabarit de domaine contre son schéma ; recherche de notions dans les quatre traces de la phase 6.

**Statuts.** Certain : lu ou mesuré. Probable : cohérent avec plusieurs observations. Hypothèse : à éprouver. **Poids.** Important ou mineur ; aucun constat bloquant dans ce lot.

**Points de vue.** A agent, D designer, P personne, M mainteneur, I ingénieur, V preuve, T intégrité.

---

## 1. Verdict du lot

Le chemin de l'agent est juste dans sa forme et trop large dans son contenu.

1. **La forme tient** (certain). Tous les renvois se résolvent, le noyau est conforme à sa compilation, les commandes citées existent.
2. **L'agent n'utilise qu'une partie de ce chemin** (certain sur les traces). Il écrit avec la déclaration du noyau ; les cadres du tronc ne laissent presque aucune trace.
3. **Le chemin dit plusieurs fois la même chose sous des noms différents** (certain). Sept cadres pour une direction, trois systèmes d'axes, six endroits qui disent quoi charger.
4. **Deux règles récentes ne sont pas arrivées chez leur propriétaire** (certain). L'accord avant génération et la grille de travail de l'agent.

---

## 2. Ce qui tient

| Vérification | Résultat |
|---|---|
| Renvois de route cités dans le lot | 100 distincts, 100 résolus |
| Noyau compilé | Conforme à ses sources, 43 984 octets sur 46 000 |
| Commandes et options citées | Toutes présentes dans l'aide des outils |
| Gabarit `DOMAIN-FRAME` contre son schéma | 16 clés sur 16, identiques |
| Statuts cités (`BLOCKED`, `HELD`) | Définis dans `gouvernance/statuts.md` |
| Dimensions de registre du noyau contre `SAVOIR/STYLE` | Les sept concordent |

S'y ajoutent, à la lecture : un arbre de classification net (`agent/chemins.md:16-23`), une protection de niveau explicite (`:29`), une réponse en quatre rubriques sans jargon (`agent/repondre.md:22-31`), et des absolus qui refusent de compenser une preuve absente (`design/direction/standard.md:9-15`).

---

## 3. Constats importants

### A-01 — Les cadres du tronc ne laissent aucune trace dans les runs
- **Lieu.** `design/direction/diriger.md:12-25` (Creative Boot, 12 champs) et `:45-57` (cible visuelle, 11 champs).
- **Point de vue.** A, V.
- **Constat.** Dans les quatre traces de la phase 6, les notions propres à ces deux cadres (tension, signature, silhouette, opération dominante, relations de plans, qualités `CFT`, moment humain, contre-choix) apparaissent 2 fois en tout. Les notions de la déclaration du noyau (`REGISTRE`, `NIVEAU`, `MOBILE`, `FINITION`, promesse, objet de preuve) sont dans les quatre.
- **Statut.** Certain pour le comptage. Probable pour le non-usage : la trace légère n'oblige pas à écrire ces champs.
- **Poids.** Important. Ces deux cadres pèsent 8 434 caractères, soit 24 % du tronc.

### A-02 — Sept cadres décrivent la même direction, et leur table de correspondance ignore le plus utilisé
- **Lieu.** `design/direction/diriger.md:61-80` (`DIRECTION/CADRES`), `:207-219` (déclaration), `design/direction/cadrer.md:12-26` (`RUN-PRIORITY`).
- **Point de vue.** A, M.
- **Constat.** L'agent rencontre sept cadres : ligne `RUN` (5 éléments), `RUN-PRIORITY` (4 et un interdit), Creative Boot (12), cible (11), déclaration (9), contrat positif (8), trace légère (6). La table `CADRES` en réconcilie six vues. La déclaration en neuf lignes, la seule que les quatre runs ont écrite, n'y figure pas ; `RUN-PRIORITY` non plus.
- **Statut.** Certain.
- **Poids.** Important.

### A-03 — Trois systèmes d'axes pour situer une direction
- **Lieu.** `design/direction/diriger.md:186` (six axes de `CFT-02`), `:194` (sept dimensions de registre), `SKILL.md:181` (cinq axes de tension).
- **Point de vue.** A, D.
- **Constat.** Les trois se recouvrent (matière et densité sont dans les trois, voix dans deux). Le noyau fait diverger par le registre ; la route `DIVERGENCE` demande d'abord de situer l'idée sur `CFT-02` ; le Creative Boot demande une tension. Rien ne dit lequel prime.
- **Statut.** Certain.
- **Poids.** Important.

### A-04 — Trois routes prescrites pendant la fabrication ne sont jamais lues
- **Lieu.** `agent/chemins.md:106` (« Pendant la fabrication et l'observation ») et `:205` (« Exécuter le pipeline `ACTION/PIPELINE-DIRECTION` »).
- **Point de vue.** A, V.
- **Constat.** La ligne du mode prescrit `ACTION/PIPELINE-DIRECTION`, `ACTION/VISUAL_PROOF` et `ACTION/GATE-C`, sans condition. Aucun des quatre runs ne les a lues. Les agents suivent les étapes du noyau à la place.
- **Statut.** Certain (fiches de mobilisation). Reste à vérifier au lot E si ces routes disent autre chose que le noyau.
- **Poids.** Important : soit la ligne du mode prescrit trop, soit les agents manquent quelque chose.

### A-05 — `SAVOIR/STYLE` est exigée, recommandée et déconseillée à la fois
- **Lieu.** `design/direction/diriger.md:212`, `agent/chemins.md:133` et `:106`.
- **Point de vue.** A.
- **Constat.** La ligne `REGISTRE` exige « deux dimensions de `SAVOIR/STYLE` » à chaque run `DIRECTION`. La table des signaux y renvoie dès qu'un registre est à nommer. La ligne du mode dit de ne la charger que si le style peut changer une décision, « jamais comme catalogue automatique ». Aucun des quatre runs ne l'a lue ; tous ont nommé un registre.
- **Statut.** Certain.
- **Poids.** Important. Le noyau liste déjà les sept dimensions (`SKILL.md:68`) : le renvoi est peut-être superflu.

### A-06 — Le contrôle en huit dimensions reste exigé là où la grille en quatre questions devait le remplacer
- **Lieu.** `design/direction/boucle.md:14` et `:20`, contre `design/savoir/qualite-creative.md:53`.
- **Point de vue.** A, M.
- **Constat.** `qualite-creative.md` fait de la revue en quatre questions la grille de travail de l'agent en trace légère. `boucle.md` dit toujours, sans condition : « Avant de présenter, applique le contrat positif », puis « contrôle des huit dimensions du premier objet ».
- **Statut.** Certain (contradiction de texte).
- **Poids.** Important pour la cohérence ; effet faible aujourd'hui, la route n'étant pas lue.

### A-07 — La règle d'accord n'est pas écrite chez le propriétaire des routes de production
- **Lieu.** `design/direction/diriger.md:104-121` (`ASSET-ROUTE`), `:22`, `:33` ; `design/direction/standard.md:44` et `:53`.
- **Point de vue.** T, M.
- **Constat.** L'accord avant toute génération est écrit au noyau et à la prise de brief. Il manque dans `ASSET-ROUTE`, qui définit la route `GÉNÉRÉ-DIRIGÉ` sans le citer. Le champ `FABRICATION` liste « génération » parmi les moyens. Le paragraphe du noyau garde « génération dirigée si la destination la permet » à côté de « attend son accord, même pour une démonstration ». La voie d'ancrage `ANCHOR-GENERATED` ne dit pas si elle relève de cet accord.
- **Statut.** Certain.
- **Poids.** Important : c'est une règle de consentement.

### A-08 — Le garde-fou contre la répétition suppose un antécédent que le protocole de test supprime
- **Lieu.** `design/direction/premier-objet.md:61-76` (`DIRECTION/REUSE`).
- **Point de vue.** V, A.
- **Constat.** `REUSE-CHALLENGE` compare le run à ce que les runs précédents ont laissé (traces, fichiers livrés). Les runs de mesure se font dans un dossier vide, avec un agent neuf : il n'y a rien à comparer.
- **Statut.** Certain pour les textes. Hypothèse pour la conséquence : la convergence mesurée entre runs serait en partie celle d'agents privés du seul garde-fou prévu.
- **Poids.** Important pour lire les résultats de la phase 6.

### A-09 — Aucune borne de coût
- **Lieu.** `design/direction/standard.md:75-88` (absolu 4, « mode, preuve et budget ») ; `design/direction/diriger.md:195`.
- **Point de vue.** M, V.
- **Constat.** L'absolu 4 définit le budget comme « une suite de jalons, pas un nombre d'appels d'outil ». Aucune limite de durée, d'appels ou d'esquisses n'existe. La divergence impose quatre premiers écrans (la modale et trois esquisses) avant la page.
- **Statut.** Certain.
- **Poids.** Important.

### A-10 — La direction se choisit au bureau, même pour un produit mobile
- **Lieu.** `design/direction/diriger.md:195` (« à 1440 px », `--bureau-seul`).
- **Point de vue.** D.
- **Constat.** Les trois esquisses et la modale se comparent en 1440 px. Le mobile se construit ensuite, sur la seule direction gardée. Trois des quatre briefs de la phase 6 portent sur une application.
- **Statut.** Certain pour le texte. Probable pour l'effet : une idée forte en mobile peut perdre sur la planche.
- **Poids.** Important.

### A-11 — Le choix de la direction n'a qu'un juge
- **Lieu.** `design/direction/diriger.md:195` (« ce choix est celui de l'agent ») et `:158` (« la personne reçoit une proposition principale »).
- **Point de vue.** D, P.
- **Constat.** L'agent esquisse, juge et retient. La personne ne voit la planche que si elle le demande ; elle reçoit une proposition et l'alternative écartée en une phrase.
- **Statut.** Certain pour le texte. Hypothèse : c'est l'une des étapes où deux runs retombent sur le même choix.
- **Poids.** Important.

### A-12 — Six endroits disent quoi charger, et les agents font autrement
- **Lieu.** `agent/chemins.md:98` (« seule liste de chargement »), `SKILL.md:170-204`, `agent/chemins.md:250`, `sections/SAVOIR.md:30`, `sections/BIBLIOTHEQUE.md:32`, `sections/READING_MAP.md:26`.
- **Point de vue.** A, M.
- **Constat.** `SAVOIR/READ` dit « zéro à deux routes » par run. Les quatre runs en ont ouvert sept à treize, presque toutes au départ.
- **Statut.** Certain.
- **Poids.** Important.

---

## 4. Constats mineurs

| N° | Lieu | Vue | Constat | Statut |
|---|---|---|---|---|
| A-13 | `SKILL.md:48`, `:58`, `:68`, `:162` | A | Quatre paragraphes de 1 273 à 2 015 caractères, soit 17 % du noyau, comptent chacun 17 à 26 segments de phrase enchaînés | Certain |
| A-14 | `design/direction/diriger.md:207` et `:225` | A | La déclaration vient « après la planche », puis se relit « avant le premier build ». La trace de SOM-3 note l'avoir relue après | Certain |
| A-15 | 31 blocs, 14 fichiers | M | 66 blocs portent le marqueur « noyau » ; 35 sont au noyau, 31 (36 376 caractères) n'y sont pas | Certain |
| A-16 | `SKILL.md:33`, `agent/chemins.md:54`, `SKILL.md:162` | A | Une même case s'appelle « preuve minimale », « preuve suivante » et « prochaine preuve ». Les traces emploient l'une ou l'autre | Certain |
| A-17 | `design/direction/standard.md:111`, `:113` ; `agent/chemins.md:278` | M | Les tags `[FORCÉ]`, `[RECOMMANDÉ]` et `[DÉPRÉCIÉ]` sont définis et jamais employés | Certain |
| A-18 | `design/direction/standard.md:38`, `:127` | A | « P1 » et « P0–P3 » sont cités sans définition ni renvoi ; la définition est dans `design/savoir/techniques.md:22` | Certain |
| A-19 | `sections/DIRECTION.md:42` | M | Titre « Réconciliation des vues de direction » sans contenu | Certain |
| A-20 | `design/README.md:8` | P, M | La liste du savoir omet `identite.md` | Certain |
| A-21 | `SKILL.md:213`, `agent/chemins.md:115` | M | Les lectures « pour les personnes » ne sont pas les mêmes aux deux endroits | Certain |
| A-22 | `sections/BIBLIOTHEQUE.md:27`, `sections/SAVOIR.md:36`, `agent/chemins.md:241`, `:282` | M | Restes de l'ancien rangement : tables « Document : `DIRECTION.md` », rappels des « anciennes références de section » | Certain |
| A-23 | `design/direction/premier-objet.md:15` | A, T | Le tronc dit de porter le marquage `TRUTH/ILLUSTRATIVE` « près de l'objet » ; le noyau dit que ces labels n'apparaissent jamais dans l'interface | Certain |
| A-24 | `SKILL.md:99-101` | M | La section 5 du noyau, « situer l'interface et son caractère », ne contient que le test de trame | Certain |
| A-25 | Troncs des modes | M | Le tronc `DIRECTION` fait 34 520 caractères ; ceux des quatre autres modes, 9 109 à 11 529 | Certain |

---

## 5. Propositions (non intégrées)

1. **Un seul cadre de travail en trace légère** (A-01, A-02) : la déclaration et la chaîne promesse, objet de preuve, geste. Le Creative Boot et la cible deviendraient des vues de trace complète, servies à la demande. Cela libérerait jusqu'à 8 400 caractères de tronc. À confirmer après les lots B et E.
2. **Porter deux règles chez leur propriétaire** (A-06, A-07) : l'accord dans `ASSET-ROUTE`, la grille en quatre questions dans `DOUBLE-LOOP`.
3. **Trancher `SAVOIR/STYLE`** (A-05) : soit le noyau suffit et les renvois partent, soit la route entre au tronc.
4. **Un seul système d'axes nommé comme premier** (A-03).
5. **Décider d'une borne de coût** (A-09) : une durée, ou un nombre d'esquisses selon la demande.
6. **Corrections mineures groupées** (A-14 à A-24).

Les constats A-04, A-08, A-10 et A-11 ne reçoivent pas de proposition ici : ils demandent d'abord une discussion.

---

## 6. Ce que ce lot n'a pas vérifié

- **`SKILL.md`** a été lu en entier plus tôt dans la session, pas relu pour ce lot.
- **Le regard d'un agent neuf** est affaibli : j'avais lu le suivi et les audits précédents avant ce lot.
- **Les lectures de routes** viennent des fiches de mobilisation, dont l'instrument reste à auditer au lot D.
- **Le contenu des routes citées mais rangées ailleurs** (`PIPELINE-DIRECTION`, `GATE-C`, `SAVOIR/STYLE`, `CFT-02`) relève des lots B et E.
- **L'effet réel des cadres du tronc sur le raisonnement de l'agent** : les traces ne le montrent pas, elles ne le réfutent pas non plus.
- **Les hypothèses** de A-08 et A-11.
