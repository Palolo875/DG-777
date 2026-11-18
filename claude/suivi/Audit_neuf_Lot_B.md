# Audit neuf — Lot B : le savoir de design

13 novembre 2026. Révision auditée : `R2026-11-13c`. Document hors du paquet. Rien n'est intégré.

**Lus en entier (22 fichiers, 295 k).** `design/savoir/` (13), `design/formes/` (3), `design/produit/` (6).

**Exécuté.** Résolution des 66 renvois de route du lot ; recalcul des repères de contraste en OKLCH ; taille servie de chaque route et lectures relevées dans les quatre fiches de mobilisation ; compte des gabarits de formulaire et des images ; une recherche en ligne sur un fait juridique cité.

**Statuts.** Certain : lu ou mesuré. Probable : cohérent avec plusieurs observations. Hypothèse : à éprouver. **Poids.** Important ou mineur ; aucun constat bloquant.

**Points de vue.** A agent, D designer, P personne, M mainteneur, I ingénieur, V preuve, T intégrité.

---

## 1. Verdict du lot

Le savoir est juste, souvent de niveau professionnel, et il manque sa cible deux fois : il n'est presque pas lu, et il ne se montre jamais.

1. **Le contenu tient** (certain pour ce qui a été recalculé). Les renvois se résolvent, les repères chiffrés vérifiés sont exacts, les limites sont dites.
2. **Le meilleur savoir de construction est hors du chemin** (certain). Sur 38 routes, 11 ont été lues au moins une fois dans les quatre runs : 73 k sur 262 k, soit 28 %.
3. **Tout se dit en mots** (certain). Aucune image dans les 22 fichiers. Les registres, les profils et les 41 formes du catalogue sont décrits par des phrases.
4. **Le lot porte les mêmes doublons que le lot A** (certain). Sept grilles pour juger un rendu, trois listes de rôles d'asset, quatre quotas de recherche différents dans une seule route.

---

## 2. Ce qui tient

| Vérification | Résultat |
|---|---|
| Renvois de route cités dans le lot | 66 distincts, 66 résolus |
| Repères OKLCH de `qualite-creative.md:276` | Recalculés : concordants (3:1 pour un écart de L de 0,31 à 0,33 ; 4,5:1 pour 0,40 à 0,43 ; noir pur 0,46 et 0,56) |
| Fait juridique de `images-et-sources.md:107` | Corroboré par des sources secondaires (règlement (UE) 2026/1744, échéance du 2 décembre 2026) ; source première non ouverte |
| Dimensions de registre, statuts, commandes cités | Concordants avec leurs propriétaires |

**Le savoir le plus fort, du point de vue du designer** (lu en entier, jugé à la lecture) :

| Savoir | Lieu | Lu dans les runs |
|---|---|---|
| Table des gestes de finition, 17 lignes | `design/savoir/composition.md:51-69` | 1 sur 4 |
| Douze caractères traduits en leviers chiffrés, avec leur piège | `design/formes/choisir.md:30-46` | 0 sur 4 |
| Inventaire du sujet, phrase d'idée, test du concurrent | `design/savoir/qualite-creative.md:97-101` | 2 sur 4 |
| « La valeur d'abord » : couleur par la luminosité | `design/savoir/qualite-creative.md:276-288` | 0 sur 4 |
| Écriture : argument, budget d'un titre, formes de titre | `design/savoir/qualite-creative.md:306-318` | 0 sur 4 |
| Choisir et comparer des voix typographiques | `design/savoir/typographie.md:31-42` | 4 sur 4 |
| Sourcing : lot d'assets, choix, honnêteté, droits | `design/savoir/images-et-sources.md:22`, `:59-65` | 4 sur 4 |
| Signaux de convergence structurelle | `design/formes/choisir.md:233-246` | 0 sur 4 |
| Transitions interruptibles | `design/savoir/techniques.md:56-69` | 0 sur 4 |

---

## 3. Constats importants

### B-01 — Le meilleur savoir de construction n'est pas lu
- **Lieu.** Les 38 routes du lot ; détail au tableau de la section 2.
- **Point de vue.** A, D, V.
- **Constat.** 11 routes entières lues au moins une fois, 73 k sur 262 k. Jamais lues : toute `BIBLIOTHEQUE` sauf `SEQUENCE` (59 k), `SAVOIR/CRAFT` hors `CFT-01` (couleur, écriture, composition), `SAVOIR/STYLE`, `SAVOIR/FRAME`, `SAVOIR/TECH`, `SAVOIR/CONTEXT`.
- **Statut.** Certain, dans la limite de l'instrument de lecture (lot D).
- **Poids.** Important.

### B-02 — La grille de travail de l'agent n'est pas au noyau
- **Lieu.** `design/savoir/qualite-creative.md:39` (les quatre questions) et `:53` (leur désignation).
- **Point de vue.** A.
- **Constat.** La revue sur capture en quatre questions est désignée comme grille de travail en trace légère. Ses questions n'apparaissent nulle part dans `SKILL.md`, et la route qui les porte n'a été lue par aucun run.
- **Statut.** Certain.
- **Poids.** Important.

### B-03 — Le savoir ne se voit jamais
- **Lieu.** Les 22 fichiers ; `design/savoir/styles.md:39-60` ; `design/formes/catalogue.md`.
- **Point de vue.** D.
- **Constat.** Zéro image. La taxonomie en sept dimensions, les huit profils et les 41 formes du catalogue sont décrits par des phrases. Les repères chiffrés existent en cinq endroits seulement : leviers de caractère, couleur, grand texte, durées de mouvement, repères mesurés de matière.
- **Statut.** Certain.
- **Poids.** Important : un agent ne peut viser un niveau qu'il n'a jamais vu.

### B-04 — Les sections ordinaires n'ont presque pas de savoir
- **Lieu.** `design/formes/catalogue.md:243` (« Cartes »), `:439` (« Parties ordinaires »), `:153` (portée).
- **Point de vue.** D.
- **Constat.** Pour les fonctionnalités, les preuves, les tarifs, les questions et le pied de page, le savoir tient en deux paragraphes et une ligne de table. Le catalogue dit lui-même venir « surtout du produit logiciel et du B2B ».
- **Statut.** Certain.
- **Poids.** Important : ce sont les sections que les runs livrent ordinaires.

### B-05 — Sept grilles pour juger un même rendu, et la plus exigeante n'est pas lue
- **Lieu.** `qualite-creative.md:28-37`, `:39`, `:50`, `:55-62` ; `composition.md:16-33` ; `fondements.md:22-24` ; `design/direction/premier-objet.md:27-44` ; `design/produit/finition.md:8-27`.
- **Point de vue.** A, M.
- **Constat.** Qualités `CFT-00` (8), revue créative (6), revue sur capture (4), jugement visuel situé (6 dimensions, 3 niveaux), premium perçu (6), contrat positif (8), Gate C (6). La table de rattachement en réconcilie quatre. Gate C se dit « obligatoire en `DIRECTION` » et applicable en trace légère ; aucun run ne l'a lu, et ses six critères ne sont pas au noyau.
- **Statut.** Certain. Répond en partie au constat A-04 : Gate C porte un contenu que le noyau n'a pas sous cette forme.
- **Poids.** Important.

### B-06 — Quatre quotas de recherche dans la même route
- **Lieu.** `design/savoir/images-et-sources.md:59`, `:61`, `:69`, `:87`.
- **Point de vue.** A.
- **Constat.** « Deux ou trois requêtes par idée », « une fois par rôle », « deux ou trois requêtes sérieuses », « deux requêtes au plus ».
- **Statut.** Certain.
- **Poids.** Important : c'est la route que le prochain run de mesure doit éprouver.

### B-07 — Trois listes de rôles d'asset qui ne se recouvrent pas
- **Lieu.** `design/savoir/images-et-sources.md:61` (6 rôles), `:75-84` (8), `:169` (11) ; `:73`.
- **Point de vue.** A, M.
- **Constat.** La table des routes par rôle renvoie aux « Rôles d'asset » de l'atlas. Les deux listes diffèrent : « personne », « objet » et « illustration » ne sont pas dans l'atlas ; « orientation », « média temporel » et « modèle spatial » ne sont pas dans la table.
- **Statut.** Certain.
- **Poids.** Important, pour la même raison que B-06.

### B-08 — La liste des marqueurs s'allonge à chaque série de runs
- **Lieu.** `design/savoir/gout-et-tendances.md:57`.
- **Point de vue.** D, V.
- **Constat.** Un seul paragraphe de 2 158 caractères mêle la liste des marqueurs et un journal d'essais : sept dates entre le 26 septembre et le 6 novembre, chacune ajoutant une convergence observée. La dernière note que les réponses au style génératif sont « devenues à leur tour des défauts ».
- **Statut.** Certain pour le texte. Probable : nommer un marqueur le déplace sans le supprimer.
- **Poids.** Important. C'est aussi une route lue par trois runs sur quatre, où l'utile est noyé dans le daté.

### B-09 — Performance et accessibilité : presque rien à savoir, rien à mesurer
- **Lieu.** `design/savoir/contexte.md:10`, `:28-30` ; `design/produit/plancher.md:90-101`.
- **Point de vue.** D, I.
- **Constat.** L'accessibilité tient en une phrase de principes, le responsive et la performance en deux paragraphes sans repère. La liste des contrôles de la recette ne comporte ni poids de page ni temps de chargement.
- **Statut.** Certain pour les textes. À confirmer au lot C pour l'outil.
- **Poids.** Important pour un niveau professionnel ; sans effet sur une démonstration.

---

## 4. Constats mineurs

| N° | Lieu | Vue | Constat | Statut |
|---|---|---|---|---|
| B-10 | `qualite-creative.md:141-156`, `choisir.md:56-62`, `styles.md:39-47`, `:72` | A, M | Précision de A-03 : les axes d'expression (12) et de tension (7) sont reliés par les textes ; les dimensions de registre (7) ne le sont à aucun des deux. Le noyau cite 5 axes de tension sur 7, `diriger.md:186` cite 6 axes d'expression sur 12 | Certain |
| B-11 | `cadrer.md:12-26`, `diriger.md:84`, `fondements.md:44`, `:51`, `techniques.md:22` | A, M | Cinq ordres de construction ou de jugement ; deux seulement sont réconciliés | Certain |
| B-12 | `fondements.md:37`, `qualite-creative.md:219`, `:290`, `interface.md:28`, `images-et-sources.md:107` | T | Des sources sont nommées (auteurs, entreprise, règlement). Ta règle 6 dit « sans citer leur provenance » ; le contrat de claim du système exige source et date. Les deux se contredisent | Certain ; portée de la règle à trancher |
| B-13 | `gout-et-tendances.md:57`, `images-et-sources.md:62` | M, T | Des résultats de runs datés figurent dans le savoir (« six agents neufs, trois briefs », « pages d'accueil d'agents »). Ta règle 3 vise les pages de présentation : à dire si elle vaut ici | Certain ; à trancher |
| B-14 | `plancher.md:157` contre `SKILL.md:58` | T | Une nouvelle dépendance exige une approbation ; le noyau range les paquets installables dans l'inventaire de la portée sans accord | Certain |
| B-15 | `connexions.md:76` | M | La connexion « réemploi » cite `DIRECTION/FIRST-OBJECT` ; la section est passée à `DIRECTION/REUSE` | Certain |
| B-16 | `identite.md` ; `catalogue.md:270`, `:376` | M, D | La route d'identité ne cite ni la planche de grammaire de marque ni la couche du même nom | Certain |
| B-17 | `composition.md:69` contre `qualite-creative.md:318` | A | Deux règles pour les espaces en français : fine insécable avant « ; ! ? » d'un côté, « espace insécable » pour tout de l'autre | Certain |
| B-18 | `styles.md:82-94` | M | La route des styles porte aussi le tiret cadratin et le « slop procédural », sans rapport avec son objet | Certain |
| B-19 | `qualite-creative.md:97`, `:274`, `:294` ; `images-et-sources.md:57` ; `identite.md:8` | M | Le statut d'essai se dit dans le savoir, avec deux adresses différentes (`evolution.md` ou `versions.md`) | Certain |
| B-20 | Lots A et B | M | 22 gabarits de formulaire en bloc de texte, dont 7 dans les formes | Certain |
| B-21 | Fiches de mobilisation | I, V | Deux lectures notées « partielles » étaient complètes : `CFT-01` fait 65 lignes (filtres à 80 et 120), `SAVOIR/STATE` 78 lignes (filtre à 150) | Certain ; instrument au lot D |
| B-22 | `images-et-sources.md:131` | P | La méthode demande trois ou quatre variantes par image générée : coût à connaître avant un run avec accord | Certain |

---

## 5. Propositions (non intégrées)

1. **Mettre sur le chemin ce qui sert à construire** (B-01, B-02), à budget constant : les quatre questions de la revue, les leviers chiffrés, le budget d'un titre et la valeur d'abord, contre les blocs du tronc relevés au lot A.
2. **Aligner la route de matière avant de la mesurer** (B-06, B-07) : un seul quota de recherche, une seule liste de rôles.
3. **Une grille pour l'agent** (B-05) : les quatre questions ; Gate C devient une vue de trace complète, ou ses gestes rejoignent le chemin.
4. **Séparer les marqueurs de leur journal** (B-08) : la liste utile d'un côté, les dates et sources de l'autre.
5. **Deux décisions qui te reviennent** : un savoir des sections ordinaires (B-04) ; une calibration qui se voit (B-03).
6. **Trancher la portée des règles 3 et 6** (B-12, B-13).
7. **Corrections mineures groupées** (B-14 à B-19).

---

## 6. Ce que ce lot n'a pas vérifié

- **`identite.md`** a été lu en entier plus tôt dans la session (fichier neuf dans le diff), pas relu pour ce lot. La section `GATE-A` de `plancher.md` a été lue telle que le tronc la sert.
- **Le fait juridique** n'a pas été vérifié sur sa source première.
- **Les licences et conditions de la carte des moyens** (`gout-et-tendances.md:70-86`) n'ont pas été vérifiées en ligne ; rien de contraire à ce que je sais.
- **Les faits datés** sur le socle des navigateurs, l'accord Amazon et la norme des tokens n'ont pas été vérifiés en ligne.
- **Le comportement des outils** que ce savoir cite (`typo`, la recette, `regard`) relève du lot C.
- **La justesse du savoir** est jugée à la lecture, pas sur des rendus.

Sources en ligne consultées pour le fait juridique : [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article50-watermarking-deadline/), [note sur le règlement (UE) 2026/1744](https://pasqualepillitteri.it/en/news/8951/eu-regulation-2026-1744-digital-omnibus-ai-act), [ComplianceHub](https://compliancehub.wiki/eu-ai-act-december-2-2026-legacy-systems-watermarking-grace-period-expiry/).
