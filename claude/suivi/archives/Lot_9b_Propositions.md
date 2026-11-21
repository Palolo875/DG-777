# Lot 9b — Propositions

Rédigé le 19 novembre 2026. Base : `R2026-11-15k` (`master` `c1fe44a`).

Sources :
- le rapport du lot 9 (constats A à E, runs 9 à 16, verdicts de Junior) ;
- la lecture du système (notes `Lecture_systeme/01` à `17`).

Règle 1 : rien n'est intégré sans décision. « D'accord » vaut pour les options A partout.

## 0. Correction préalable (vérifiée dans le code)

`parcours.py verifier` **sert déjà le texte des gestes de `SAVOIR/STATE`**. Chaque signal relevé porte un `geste_texte` lu à son lieu (`ROUTE_GESTES`, l. 55 ; `ajouter`, l. 452). `verifier` a tourné dans les huit runs, de 2 à 6 fois chacun (journaux). Les gestes de finition ont donc bien été servis au bon moment, même sans lecture de la route.

Ce que ça change :
- La piste 1 de la note 14 est déjà faite.
- La part « STATE » de la piste A1 de la synthèse aussi.
- Le constat P3 (la finition relève le plancher, pas le plafond) en sort **renforcé**. Les gestes ont été servis à chaque run, et les rendus sont restés « génériques, cheap » selon Junior.
- **Il manque des lignes de direction servies avant le build, pas des lignes de finition servies après.**

## 1. Mesures

| Mesure | Valeur | Source |
|---|---|---|
| Routes lues sur 8 runs | 20 sur 85 | Note 09 |
| Routes de goût jamais lues | FRAME, READ, CFT-03, CFT-05, CFT-04a, GATE-B (B1b, B3), PIPELINE-DIRECTION | Notes 12 à 15 |
| `tirage`, lancé avant le build | 8 runs sur 8 (1 à 2 fois) | Journaux |
| `verifier`, lancé après le build | 8 runs sur 8 (2 à 6 fois) | Journaux |
| Diagramme comme objet principal | Runs 9, 10, 14, 16 | Rapport du lot 9, A-3 |
| Noyau | 45 250 octets pour un plafond de 46 000 | Note 16 |

## 2. Propositions

### P1 — Servir les leviers de caractère avant le build

**Constats** : A-2, E-3, E-4, B-2. Synthèse : C1, P1 et P2.

**Mesure.**
- La table « Traduire un caractère en leviers » de `BIBLIOTHEQUE/READ` donne, pour 12 caractères, des leviers concrets et un piège réflexe. Elle n'a jamais été lue.
- `tirage` est le seul outil lancé avant le build dans tous les runs. Il lit déjà `SAVOIR/STYLE` à son lieu.

**Options.**
- **A (recommandée).** Une sous-commande `parcours.py leviers "pôle[,pôle]"`.
  - Elle lit à son lieu les lignes des pôles choisis (deux au plus, un par paire) : leviers et piège, rien n'est recopié.
  - Elle y ajoute l'ordre de composition de `SAVOIR/FRAME` : intention → tension → foyer → masse → rythme → matière et type.
  - Une demi-ligne dans le noyau, au point de déclaration du registre, appelle la commande. Elle remplace une redite, à trouver au moment de l'intégration, pour tenir dans les 750 octets restants.
  - La garde est un test qui casse la table de READ et vérifie que la commande échoue (mutation rouge).
  - Statut `PILOT`.
- **B.** Ajouter ces lignes à la sortie de `tirage`. Plus simple, mais `tirage` tire au hasard. Les leviers doivent suivre le pôle **choisi**, pas un pôle tiré.
- **C.** Ne rien outiller : une phrase du noyau renvoie à `BIBLIOTHEQUE/READ`. C'est peu coûteux, mais la proposition d'une route ne vaut pas sa lecture (STATE : 19 propositions, 3 lectures).

### P2 — Nommer le diagramme parmi les convergences, avec son contrepoids

**Constats** : A-1, A-3. Synthèse : C3.

**Mesure.**
- `SELECT` liste sept signaux de convergence, dont « grain repris d'un brief à l'autre », mais pas le diagramme comme objet principal.
- Le contrepoids, `CFT-04a` (« l'objet ou le geste peut ouvrir »), est dans un bloc différé et n'a jamais été lu.
- `parcours.py` lit déjà le signal « Objet de preuve au premier écran » de `check_render` (l. 1672).

**Options.**
- **A (recommandée).**
  - Ajouter une ligne à la table de convergence de `SELECT` : « Plan, schéma ou diagramme comme objet principal d'un brief qui vit de l'atmosphère ou de l'envie ». Question de reprise : « l'idée se lit-elle sans légende ? Quel objet ou geste du sujet ouvrirait à sa place (`CFT-04a`) ? »
  - Quand `verifier` voit le signal d'objet de preuve, il sert cette question (lue à son lieu).
  - Les tests vérifient la ligne et son service (mutation rouge).
- **B.** La ligne dans SELECT seulement.
- **C.** Un marqueur dans `regard.py`. Je ne le recommande pas : un diagramme ne se détecte pas de façon fiable sur capture.

### P3 — Dire qui a choisi, en trace légère

**Constats** : synthèse C4 et P4 ; GATE-B, B3.

**Mesure.**
- En trace légère, la ligne « modal, trame et parti » nomme déjà « le choix et sa raison » (`agent/repondre.md` l. 44 ; noyau l. 95). Elle ne dit pas **qui** a choisi.
- La réserve de B3 (auto-comparaison) ne vit qu'en trace complète.

**Options.**
- **A (recommandée).** Ajouter à la ligne existante : « choisi par : auteur du rendu / personne / absent ». Pas de ligne nouvelle : la trace reste à six lignes. `parcours.py trace` le relève s'il manque.
- **B.** Une septième ligne. Je ne la recommande pas : elle casse le plafond des six lignes.
- **C.** Rien.

### P4 — Méthode de la série esthétique : jugement par paires et carnet de goût (hors paquet)

**Constats** : synthèse P4 et P5 ; règle 7.

**Options.**
- **A (recommandée).**
  - Chaque run de la série livre deux candidats finis : la direction gardée et la meilleure alternative, au même niveau de finition.
  - Je les présente à Junior dans un ordre masqué. Il choisit, avec une phrase de raison, puis je révèle.
  - Le choix va dans `suivi/Carnet_de_gout.md` : objet, deux captures, choix, raison.
  - Coût : environ un rendu de plus par run.
  - **Rien ne change dans le paquet.** C'est le protocole de test, dans `.claude/suivi`.
- **B.** Un seul candidat, comme aujourd'hui.

### P5 — Doctrine (décisions de Junior)

| Question | Option A (recommandée) | Option B |
|---|---|---|
| **D1. Plancher / plafond** | Une phrase dans la passe de finition (`ATELIER-EDITION`), et en pied de sortie de `verifier` : « Un relevé vide prouve l'absence des signaux mesurés, pas la réussite : présence, caractère et choix se jugent sur capture. » | Rien. |
| **D2. Classique / expressif** | Une phrase dans `SINGULARITE` (FRAME), servie aussi par `leviers` (P1) : « Garder une structure lisible et attendue du genre ; porter l'écart sur une ou deux dimensions (matière, type, couleur, échelle). » Appui : Tuch 2012 ; Lavie & Tractinsky 2004. | Rien. |
| **D3. Portée de FND-01 sur un objet d'identité** | Ne rien changer : la route n'a jamais été lue, donc elle n'a pas pu nuire. D2 suffit. | Une phrase de portée : « sur une surface d'identité, la présence se décide avant la retenue ». |
| **D4. Relecteur séparé dans un run** | Laisser ce que le système permet déjà (« Regard séparé », facultatif). Il est nommé « même modèle, non indépendant » et ne remplace jamais le jugement de Junior. La règle 7 reste inchangée. | L'interdire dans les runs de la série. |

### P6 — Mesurer avant d'étendre (PILOT)

- **Protocole.**
  - Trois à cinq petits objets en code, comme dans la série.
  - Pour chacun, deux agents neufs. Le premier reçoit le paquet `R2026-11-15k` ; le second, le paquet avec P1 et P2.
  - Junior compare les deux rendus **sans savoir lequel vient de quelle condition**. C'est son jugement : la règle 7 tient.
  - Le résultat va dans le carnet (P4).
- **Décision.** On garde P1 et P2 si Junior préfère la condition avec P1 et P2 sur la majorité des objets. Sinon, on les retire ou on les reprend.
  - La limite est déclarée : c'est un petit échantillon, qui sert à orienter une décision, pas à la prouver.
  - Le contrat `EVALUATION_CASE` sert de format.
- **Coût.** Deux runs par objet, soit six à dix runs. Ce peut être la suite naturelle de la série esthétique.

## 3. Hors de ce lot (à relire avant de les proposer, règle 4)

- **C-1 et C-2** : fausses alertes de la fiche de mobilisation sur `--fichier` et sur les routes redirigées. C'est un défaut d'outil, à reproduire puis à traiter dans un petit lot séparé.
- **B-4** (sources d'images pauvres) et **B-5** (pas de référence en `STANDARD`) : à rouvrir après le PILOT, parce que P1 change ce qu'on demande aux références.
- **E-1** (la voix du designer passe dans la page) et **E-2** (polices à la mode) : à mesurer dans le carnet de goût avant d'écrire une règle.

## 4. Ordre proposé

1. Décision de Junior sur P1 à P5.
2. Intégration sur une branche de P1, P2, P3, D1 et D2, avec les tests en mutation rouge, puis la préparation complète (environ 12 min) et la révision `R2026-11-15l`.
3. PILOT (P6), avec P4 comme protocole de jugement.
