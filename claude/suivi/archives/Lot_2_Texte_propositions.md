# Lot 2 — Erreurs et contradictions de texte : propositions

15 novembre 2026. Révision de départ : `R2026-11-14b`. Document hors du paquet. Rien n'est intégré.

J'ai relu les 28 constats du lot dans les fichiers actuels.

| Sort | Nombre | Constats |
|---|---|---|
| Déjà corrigés | 6 | A-19, A-21, B-17, C-12, C-13 ; A-22 en grande partie |
| À reporter au lot 6 | 2 | B-19, F-12 |
| À corriger, sans choix à faire | 16 | A-06, A-07, A-14, A-16, A-17, A-18, A-20, le reste d'A-22, A-23, B-06, B-15, B-16, E-05, E-13, F-03, F-15 |
| À corriger, avec un choix | 5 | A-05, B-14, B-18, E-08, D-09 |

**Ce que cela coûte.** Trois corrections touchent le noyau compilé (A-05, A-14, A-16) : quelques dizaines d'octets, sur une marge de près de 2 000. Une touche le tronc DIRECTION (A-23), à longueur constante ; sa marge n'est que de 480 caractères. Aucune ne touche une règle absolue. Le reste est du texte de route ou de guide.

---

## 1. Déjà corrigés

| Constat | Ce que j'ai vérifié |
|---|---|
| A-19 | Le titre vide a disparu avec `sections/` (lot S). |
| A-21 | La skill et `DIRECTION/CHARGE` nomment maintenant les mêmes lectures pour les personnes : README, niveau 3 et niveau 2 des guides (lot S). |
| A-22 | Les tables « Document : `DIRECTION.md` » ont disparu avec `sections/`. Il reste une phrase, traitée au § 3. |
| B-17, C-12 | La composition, la qualité créative et le correcteur `typo` donnent la même règle d'espaces (lot 1). |
| C-13 | Les outils renvoient à `DIRECTION/REUSE` (lot 1). |

## 2. À reporter au lot 6

| Constat | Raison |
|---|---|
| B-19 — le statut d'essai, dit dans le savoir avec deux adresses différentes | Vous avez décidé que les essais deviennent le socle de la V1. Le lot 6 réécrira ces cinq lignes ; les harmoniser maintenant serait un travail perdu. |
| F-12 — preuves attendues « jugées par plusieurs personnes », « avec et sans le tableau » | Ces lignes appartiennent à la table des sections à l'essai, que le lot 6 refait entièrement. |

---

## 3. Corrections sans choix

Chaque ligne donne le constat vérifié, puis le changement exact.

### Direction et boucle

**A-06 — la grille de travail en trace légère.** `boucle.md` exige sans condition le contrat positif du premier objet, et un « contrôle des huit dimensions ». La qualité créative dit pourtant qu'en trace légère, la grille de travail est la revue sur capture en quatre questions.
- *Changement* : « Avant de présenter, fais la revue sur capture en quatre questions (`SAVOIR/CRAFT`, « Rattachement des grilles ») ; le contrat positif de `DIRECTION/FIRST-OBJECT` sert quand une question révèle une faiblesse, et en trace complète. »
- Dans le one-shot, « contrôle des huit dimensions du premier objet » devient « revue sur capture ».
- Route seulement : ni noyau, ni tronc.

**A-07 — l'accord avant une génération, chez le propriétaire des routes de production.** `ASSET-ROUTE` définit `GÉNÉRÉ-DIRIGÉ` sans rappeler l'accord, que le noyau et la prise de brief exigent.
- *Changement* : une phrase en tête de `ASSET-ROUTE` : « Toute génération d'image, asset ou ancre `ANCHOR-GENERATED`, attend l'accord de la personne, demandé à la prise de brief, même pour une démonstration (`DIRECTION/EXTERNAL-START`). »
- La règle elle-même ne change pas ; elle est dite là où on choisit la route.

**A-14 — l'ordre de la relecture de la déclaration.** La déclaration vient « après la planche ». Le même bloc demande de la relire « avant le premier build », alors que les esquisses de la planche sont déjà construites.
- *Changement* (noyau) : « Avant le premier build, relis la déclaration » devient « Dès que la déclaration est fixée, avant de construire la suite, relis-la ».

**A-23 — le marquage d'une démonstration.** Le tronc fait porter `TRUTH/ILLUSTRATIVE` « près de l'objet ». Le noyau dit que les labels `TRUTH/*` n'apparaissent jamais dans l'interface.
- *Changement* (tronc DIRECTION, à longueur constante) : « porte dans la trace le marquage `TRUTH/ILLUSTRATIVE` […], et dans l'interface une mention en langage produit ».

### Vocabulaire et repères

**A-16 — une case, trois noms.** La case de la ligne `RUN` s'appelle « preuve minimale », « preuve suivante » ou « prochaine preuve ». Le paquet emploie 41 fois « prochaine preuve ».
- *Changement* :
  - « preuve minimale » devient « prochaine preuve » dans l'absolu 4 (noyau) ;
  - « [preuve suivante] » devient « [prochaine preuve] » dans le gabarit de `DIRECTION/START` ;
  - même changement pour « preuve suivante attendue », dans `ACTION/GATE-A`.
- « Preuve minimale sans rituel », le titre de `ACTION/FAST-PATH`, désigne autre chose et reste.

**A-17 — des étiquettes définies et jamais employées.** `[FORCÉ]`, `[RECOMMANDÉ]` et `[DÉPRÉCIÉ]` ne servent nulle part.
- *Changement* : retirer leurs trois lignes de légende, et la mention « `[RECOMMANDÉ]` n'y est pas employé ».

**A-18 — « P1 » et « P0–P3 » sans renvoi.**
- *Changement* : à leur première mention dans `DIRECTION/STANDARD`, ajouter « (`SAVOIR/TECH`, « Hiérarchie de jugement pour les interfaces ») ».

**A-22, la phrase restante.** `ACTION/ROUTING` rappelle que « les anciennes références de section ne sont pas des routes quotidiennes ». Cela concerne les alias `REFERENCES/*`, déjà traités dans « Migration des anciens aliases ».
- *Changement* : retirer la phrase de la route de run. La migration reste documentée en maintenance, et `BIBLIOTHEQUE` y renvoie déjà.

**F-15 — « package » et « paquet ».** Le paquet emploie l'un ou l'autre selon le fichier.
- *Changement* : « paquet » partout où le mot désigne Design Governance (guides, README de maintenance, fichiers de règles).
- « package » reste quand il désigne un paquet logiciel (« une commande, un package ou une intégration »).
- Les deux gardes qui citent « README du package » et « localise le package réellement fourni » suivent.

### Savoir

**B-06 — quatre quotas de recherche dans une route.** « Deux ou trois requêtes par idée », « une fois par rôle », « deux ou trois requêtes sérieuses », « deux requêtes au plus ».
- *Changement* : un seul quota, écrit une fois, à la recherche par rôle : « deux ou trois requêtes tirées de l'inventaire du sujet, par rôle qui change la décision ». Les trois autres passages y renvoient (« ces requêtes »).
- Les trois listes de rôles (B-07) restent au lot 3.

**B-15 — la connexion « réemploi » cite la mauvaise section.**
- *Changement* : dans C05, `DIRECTION/FIRST-OBJECT` devient `DIRECTION/REUSE`.

**B-16 — l'identité ne cite pas ses outils de structure.**
- *Changement* : une phrase dans `SAVOIR/IDENTITY` : « Quand l'identité doit devenir une décision répétable dans une interface, la planche de grammaire de marque (`OBJECT/BRAND_GRAMMAR_PLATE`) et la couche `LAYER/BRAND_GRAMMAR` en portent la traduction (`BIBLIOTHEQUE/COMPONENTS`). »

### Gouvernance et entrées

**E-05 — la table des conditions de départ ignore le niveau de trace.** La ligne DIRECTION exige gates A/B/C, statut de direction et V/U/A/T sans réserve. Trois autres passages réservent Gate B, B1b et le verdict à la trace complète.
- *Changement* : une phrase sous la table : « Cette table décrit la trace complète. En trace légère, le run charge ce que la ligne du mode de `DIRECTION/CHARGE` charge d'abord ; Gate B hors du risque déclaré, B1b, statut de direction et V/U/A/T n'y sont pas dus. »
- Le fait que ce soit une troisième table « par mode » relève du lot 3, avec A-12.

**E-13 — un message en anglais dans un outil en français.**
- *Changement* : « valid » devient « valide ».
- Le message final devient « CONTRACT VALIDATION PASSED — contrats de domaine, de recherche, de direction créative, de réalité UI/UX et d'évaluation ».

**F-03 — une phrase fausse sur l'identité de marque.** Le README et l'en-tête de la fiche disent « aucun run ne l'a encore éprouvée ». La même fiche décrit le run d'identité observé.
- *Changement* (README et fiche) : « sa méthode et sa planche d'épreuve existent ; un run d'agent neuf l'a parcourue de bout en bout, et elle reste à l'essai ».
- Cette formulation reste vraie, que vous ayez jugé ce run ou non.

**A-20 — la liste du savoir omet `identite.md`.**
- *Changement* : ajouter « [identité de marque](savoir/identite.md) » à la liste du README de `design/`.

---

## 4. Corrections avec un choix

### A-05 — `SAVOIR/STYLE` est exigée, recommandée et déconseillée à la fois

**Constat vérifié.** Trois passages se contredisent :
- La ligne `REGISTRE` du noyau compose le registre « dans deux dimensions de `SAVOIR/STYLE` ».
- La table des signaux envoie à `SAVOIR/STYLE` dès qu'« un registre est à nommer », donc à chaque run DIRECTION.
- La ligne DIRECTION de la table de chargement dit de ne la lire « que si le choix de style peut modifier une décision ; jamais comme catalogue automatique ».

Le noyau liste pourtant déjà les sept dimensions, au levier « Échantillonner ».

| Option | Changement | Effet |
|---|---|---|
| **A (recommandée)** | La ligne `REGISTRE` dit « deux dimensions du registre (listées au levier « Échantillonner ») ». La ligne de la table des signaux ne se déclenche plus sur le registre, mais sur « un profil de style à retenir, une famille de design, une technique ou un médium ». | Le registre se compose avec le noyau. `SAVOIR/STYLE` se lit quand un profil peut changer une décision, comme le dit déjà la table de chargement. Noyau : une dizaine d'octets de plus. |
| B | `SAVOIR/STYLE` entre au tronc DIRECTION. | Impossible sans dépasser le budget : la route fait 14 400 caractères, la marge 480. |

### B-14 — l'approbation d'une nouvelle dépendance

**Constat vérifié.** `ACTION/GATE-A` (inspection) exige une approbation pour toute « nouvelle dépendance ». Le noyau, lui, range « paquets et bibliothèques installables » dans l'inventaire de la portée, sans accord.

| Option | Changement |
|---|---|
| **A (recommandée)** | Préciser la portée dans `ACTION/GATE-A` : « nouvelle dépendance ajoutée au projet livré : approbation requise ». Un paquet installé dans l'environnement de travail de l'agent, sans entrer dans le livrable, suit la ligne « script local ». Le noyau ne change pas. |
| B | Exiger l'accord pour toute installation, y compris dans l'environnement de travail. Le noyau change, et les runs demandent une permission de plus. |

### B-18 — deux sujets hors de leur route dans `SAVOIR/STYLE`

**Constat vérifié.** La route des styles porte aussi « Ponctuation située : le tiret cadratin » et « Test anti-slop procédural ».

| Option | Changement |
|---|---|
| **A (recommandée)** | Déplacer la ponctuation dans `SAVOIR/CRAFT/CFT-06` (écriture et contenu), à côté de la micro-typographie française. Déplacer le test anti-slop procédural dans `SAVOIR/INTEGRITY`, qui traite déjà de la critique et des limites. Le texte ne change pas, seulement sa place. |
| B | Les laisser au lot 3, avec les autres doublons. |

### E-08 — un « principe positif de qualité » rangé dans les statuts

**Constat vérifié.** Le paragraphe redit deux choses dites ailleurs. La clôture d'un one-shot après la première observation est déjà dans `DIRECTION/DOUBLE-LOOP`. La déclaration avant le build est au noyau. Une garde de fidélité le protège : « rendu one-shot » avec B1b.

| Option | Changement |
|---|---|
| **A (recommandée)** | Le retirer de `ACTION/STATUS`. Ce qu'il dit vit déjà dans `DIRECTION/DOUBLE-LOOP` et au noyau. La garde de fidélité continue de protéger la phrase de la boucle. |
| B | Le déplacer dans `ACTION/FIRST-RENDER`. |

### D-09 — la ligne de `parcours.py` dans le README des outils

**Constat vérifié.** Une cellule de 4 060 caractères. `preparer_livraison.py`, `build_distributions.sh` et `test_preparer_livraison.py` n'y figurent pas.

| Option | Changement |
|---|---|
| **A (recommandée)** | Une ligne courte pour `parcours.py`, puis une petite table de ses douze sous-commandes, une phrase chacune, reprise de son aide. Ajout des trois fichiers manquants. Le détail reste dans `python3 scripts/parcours.py SOUS-COMMANDE --help`. |
| B | Ajouter seulement les trois fichiers manquants, et laisser la cellule. |

---

## 5. Vérification prévue

1. Branche `texte`.
2. Les tests existants, plus une garde par correction qui peut revenir, avec sa mutation rouge :
   - A-06 : « huit dimensions » sans condition ;
   - A-16 : « preuve suivante » ou « preuve minimale » dans la ligne `RUN` ;
   - A-23 : `TRUTH/*` « près de l'objet » ;
   - B-15 : connexion C05 vers `DIRECTION/FIRST-OBJECT` ;
   - E-13 : sortie anglaise d'un validateur ;
   - F-15 : « package » pour le paquet.
3. Le noyau comparé avant et après : seules les trois phrases annoncées changent. Tronc DIRECTION sous 35 000.
4. Validation complète avec navigateur, archives régénérées, révision `R2026-11-15a`.
5. Registre : chaque constat passe à « corrigé », « déjà corrigé » ou « reporté au lot 6 ».

**Critère d'arrêt.** Si une phrase corrigée fait dépasser le budget du tronc DIRECTION, je m'arrête et vous la montre.

## 6. Ce qu'il faut me dire

« D'accord, options A partout » suffit. Sinon : les constats du § 3 à écarter, et l'option choisie pour A-05, B-14, B-18, E-08 et D-09.
