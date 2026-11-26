# Audit — Design Governance V1, révision R2026-11-13c

13 novembre 2026. Document hors du paquet, à rattacher au suivi. Rien n'est intégré : tout ce qui suit est constat ou proposition à discuter.

**Question directrice.** Après les huit phases, qu'est-ce qui sépare encore les rendus du niveau professionnel, et la cause est-elle dans le système ou hors de lui ?

**Périmètre.** Tout le paquet, en s'appuyant sur l'audit du 11 novembre : lecture à neuf de ce qui a changé depuis, revérification de ses constats dans les fichiers pour le reste.

**Statuts.** **Certain** : lu dans les fichiers ou mesuré. **Probable** : cohérent avec plusieurs observations, non prouvé. **Hypothèse** : à éprouver. La section 6 dit ce qui n'a pas été vérifié.

---

## 1. Verdict

1. **Le programme du 11 novembre est exécuté et sa priorité a tenu** (certain). La suite de la page tient le fil du premier écran sur quatre runs sur quatre. L'atteinte du savoir n'est plus le premier frein.
2. **Ce qui sépare encore du niveau pro est surtout hors des règles** (probable). La matière et la convergence entre runs dépendent de ce qui entre dans le run, pas d'une règle de plus. Deux écarts restent dans le système : les sections ordinaires et l'absence de calibration visuelle.
3. **Le système grossit plus vite qu'il n'est jugé** (certain). En trois jours : 22 puis 25 essais `PILOT`, aucun adopté ni retiré ; deux révisions livrées sans run ; un coût par run en hausse d'environ 40 %.
4. **La question de fond n'a qu'un point de mesure, et il est défavorable** (certain). La seule comparaison avec et sans le système date du 29 octobre : sur les quatre briefs que tu as notés, tu as préféré trois fois le rendu fait sans lui. Rien ne l'a remesuré depuis.

---

## 2. État des constats du 11 novembre

| Constat | Ce qui a été fait | État, vérifié dans R2026-11-13c |
|---|---|---|
| 2.1 L'effort porte sur le premier écran | Étape de séquence au noyau, `SEQUENCE` au tronc, références en page entière | **Résolu sur les traces** : 4 runs sur 4. La divergence, la planche et l'atelier restent au premier écran, par construction |
| 2.2 La matière manque | Mesure contre les références, densité 2×, repères mesurés | **Mesuré, non résolu** : SOM-3 17 % contre 53 %, FTX-1 13 % contre 45 %, FIN-3 5 % contre 57 %. L'agent voit l'écart et le garde |
| 2.3 Du cadre plus que de la construction | `SEQUENCE` au tronc | **Peu changé** : la part de construction lue d'office passe d'environ 15 % à 21 % (15 516 caractères sur 74 298) |
| 2.4 La convergence se déplace quand on la nomme | Palette prélevée sur le sujet | **Résolu pour la palette** (SOM-3). **Ouvert pour l'idée et l'image** : même photo, même nom d'un run à l'autre |
| 2.5 La recherche par rôle n'atteint pas l'agent | Phrase au noyau, puis routes par rôle (13c) | **Atteinte** (recherche faite et tracée). Les routes par rôle n'ont aucun run |
| 2.6 Le juge reste l'agent | Aucun, par décision : le juge est Junior | **Inchangé** |
| L1-2 Leviers chiffrés hors du noyau | Non repris au plan | **Ouvert** : la ligne `REGISTRE` ne renvoie pas à `STRUCT-LEVIERS` |
| L1-3 Sections ordinaires peu couvertes | Reporté « après la phase 6 » | **Ouvert, et dû** : FTX-1 « moitié basse ordinaire », SOM-3 « section la plus pauvre » |
| L1-5 Aucune calibration visuelle | Mesures seulement (D4) | **Ouvert**. La condition posée pour calibrer sur tes rendus (trois rendus avec ton accord) paraît atteinte : Soleil noir, Cédille, sélecteur v3, SOM-3. À toi de le dire |
| L2-4 Les essais ne sortent pas de l'essai | Preuve réécrite (D5), tri proposé | **Mécanisme en place, bloqué** par les verdicts sur quatre paires |
| L3-3 Tronc saturé | Échange cadres et réutilisation contre `SEQUENCE` | **Fait**, mais le tronc reste à 98,6 % |
| L3-4, L4-3, L4-5, L5-1, L6-5, L6-6 | Phases 3 et 4 | **Résolus** (ligne « Outils », `typo`, glossaire, périmètre, sens de `CHANGELOG`, en-tête du test) |
| L6-4 Un cinquième de l'outillage sert la trace complète | Aucun, par principe | **Inchangé** : aucun run en trace complète |

---

## 3. Constats nouveaux

### N1 — Les agents lisent tout au départ, presque rien ensuite — **certain** (fiches), lecture prudente

Sur les quatre runs de la phase 6, les fiches de mobilisation relèvent 67 lectures de routes. 64 ont lieu dans les deux premières minutes ; 3 seulement après (`SAVOIR/STATE` et `ACTION/ATELIER-EDITION` à 12 minutes, `SAVOIR/TYPE-VOIX` à 2 minutes). Les runs durent 19 à 28 minutes.

Le noyau demande l'inverse : « lis la route en entier au moment où elle peut changer la décision ». En pratique, la table des signaux (27 lignes, 13 % du noyau) sert de menu de départ. Ce qui n'est pas lu avant la première esquisse n'est presque jamais lu.

Limite : le journal ne voit que les appels du lecteur de routes. Un fichier relu avec un autre outil lui échappe.

### N2 — Quatorze routes hors tronc sur quatre runs — **certain**

Le sommaire compte 84 routes. Hors tronc, les quatre runs en ont lu 14, dont 5 à chaque fois (`START/TREE`, `EXTERNAL-START`, `MOYENS`, `SOURCE`, `TYPE-VOIX`).

Jamais lues, alors que le noyau ou le tronc y renvoient : `SAVOIR/STYLE` (la ligne `REGISTRE` demande deux de ses dimensions), `BIBLIOTHEQUE/READ`, `SELECT` et `TENSION`, `SAVOIR/CRAFT/CFT-03`, `CFT-05` et `CFT-06`, `SAVOIR/FRAME`. `SAVOIR/STATE`, qui porte les gestes de la passe de finition, a été lue une fois sur quatre.

Conséquence, avec N1 : le système effectif d'un run est le noyau et le tronc (environ 74 000 caractères lus d'office), plus sept à treize routes ouvertes au départ. Le reste du savoir existe et ne sert pas.

### N3 — Un quart du tronc sert un chemin que les runs ne prennent pas — **certain** (tailles), **probable** (inutilité)

Sept blocs du tronc `DIRECTION` concernent la trace complète, la conformité déclarée ou l'acceptation. Ils pèsent 8 539 caractères sur 34 520, soit 25 %.

| Bloc | Taille |
|---|---|
| `FIRST-OBJECT`, « Contrat positif » en huit dimensions | 2 717 |
| `GATE-A`, « Familles de méthodes » et provenance de `RUN_CARD` | 1 489 |
| `GATE-A`, « Contrat de portée » | 1 439 |
| `SAVOIR/TYPE`, « Preuve typographique » | 1 070 |
| `GATE-A`, « Adéquation des preuves » | 736 |
| `VISUAL_TARGET`, « Prête à construire » | 596 |
| `RUN-DIRECTION`, « Clôture » | 492 |

Les runs de la campagne sont en trace légère. La table qui réconciliait les vues du cadre est sortie du tronc, mais l'agent lit toujours d'office les vues elles-mêmes : douze champs du Creative Boot, onze de la cible et huit dimensions du contrat dans le tronc ; neuf lignes de déclaration et six lignes de trace dans le noyau.

### N4 — L'instrument de preuve se trompe sur le tronc — **certain** (reproduit)

Les fiches de SOM-3 et d'IDT-1 écrivent « Tronc `DIRECTION` non consulté ». Le suivi (14.33) écrit pour SOM-3 : « le tronc a été lu en entier ». Les deux ne peuvent pas être vrais.

Cause : le journal déclare une lecture partielle dès que la commande contient un filtre. Il ne tient pas compte de `--fichier`. J'ai reproduit le cas : `--tronc DIRECTION --fichier … | head -80` écrit le tronc entier dans le fichier, et la fiche le déclare non consulté. Aucun test ne couvre ce cas.

Second faux positif : `SAVOIR/SOURCE` est notée « lecture partielle » dans les quatre fiches, avec des filtres de 200 à 400 lignes, alors que la route en fait 130 aujourd'hui et environ 110 au moment des runs.

La colonne « routes lues » du tableau de preuve, dont dépend l'adoption (D5), repose sur cet instrument. Pour IDT-1, on ne sait donc pas si le tronc a été lu.

### N5 — Deux révisions livrées sans run — **certain**

Les quatre runs de la phase 6 portent sur le commit `89213ed`. L'inventaire de la portée et la règle d'accord (13b), puis les routes par rôle (13c), sont venus après. Aucun run ne les a éprouvés.

La règle d'accord a un effet direct sur la matière : sans accord écrit dans le texte de lancement, la route de génération n'est jamais prise. Dans un run sans personne pour répondre, la matière ne peut donc monter que par les sources ouvertes, dont les quatre runs ont montré la limite.

### N6 — Le chemin réel d'un run est entièrement à l'essai — **certain**

La table compte 25 lignes `PILOT` (22 le 11 novembre, 24 sur `suite`), aucune adoptée ni retirée. Ces lignes ne sont pas des marges : divergence sur image, déclaration, tronc par mode, atelier, séquence, `parcours.py`, `regard.py`. Ce que chaque agent exécute est à l'essai d'un bout à l'autre.

Une ligne a une preuve attendue que les runs contredisent : celle de la modale au second degré et du tirage demande « plusieurs runs sur un même brief : idées différentes ». La fiche de version note elle-même le contraire (même hypothèse de produit, mêmes esquisses, même photo). Elle peut se décider sur les traces, sans attendre un verdict sur image.

Le noyau a gagné 1 692 octets en trois jours (42 292, puis 43 050, puis 43 984 sur 46 000). Il reste 2 016 octets.

### N7 — Pourquoi les runs convergent — **hypothèse**, appuyée sur le code et les traces

`tirage` tire au sort deux pistes sur huit et une dimension de registre (certain, code lu). Le hasard porte sur la catégorie d'angle. Trois étapes restent sans hasard :

1. **Le remplissage.** Le même modèle remplit la piste : pour le sommeil, « ce qu'il produit » donne le drap à chaque fois.
2. **La recherche.** Les mêmes requêtes dans les mêmes collections rendent la même photo (certain : « Crumpled Sleep » deux fois, par les mêmes requêtes).
3. **Le choix.** La planche est jugée par le même modèle, qui retient la même esquisse.

Si l'hypothèse tient, ajouter des pistes ou des marqueurs ne changera rien : il faut du hasard ou un autre juge à l'une de ces trois étapes.

### N8 — Le coût monte — **certain** (tableau), cause **probable**

| Runs | Appels d'outils | Durée |
|---|---|---|
| Chevet et Somme (avant les phases) | 65 et 68 | 12 min 45 et 13 min 54 |
| SOM-3, FIN-3, FTX-1 (pages) | 102, 88, 90 | 22 min 57, 20 min 31, 18 min 57 |
| IDT-1 (identité, livrable plus large) | 110 | 27 min 36 |

Sur les trois pages, la moyenne passe de 66,5 à 93 appels (+40 %) et de 13 min 20 à 20 min 48 (+56 %). Le critère de réussite du 11 novembre disait « sans hausse de coût marquée » : il n'est pas tenu. Le gain en face est réel (la séquence, les données recoupées).

### N9 — La forme tient — **certain**

Les quatre contrôles rapides passent (structure, carte de lecture, paquet à 149 fichiers, 103 cas du lecteur). L'identifiant de révision est cohérent partout. Le `README` dit le périmètre réel et garde l'efficacité `NOT-VERIFIED`.

Trois écarts mineurs :

- `SAVOIR/SOURCE` dit « deux ou trois requêtes sérieuses », puis, dans les signes d'arrêt, « deux requêtes au plus ».
- Le noyau garde « un essai par couche » à côté de routes à essayer dans l'ordre : l'exception pour l'asset et la matière n'est pas dite.
- Le suivi (§ 15) écrit « sur 32 runs, 8 verdicts » ; le tableau compte 36 lignes et 10 verdicts.

---

## 4. Ce qui sépare encore du niveau professionnel

| Écart | Preuve | Où est la cause |
|---|---|---|
| **Matière** | 5 à 17 % contre 45 à 57 % pour les références que chaque agent a choisies ; Chevet, avec six photos fournies, est à 26 % | **Hors du système** : intrants et accords (probable) |
| **Convergence entre runs** | Même idée, même photo, même nom | **À la frontière** : remplissage, recherche et choix sans hasard (hypothèse N7) |
| **Sections ordinaires** | « Moitié basse ordinaire », « section la plus pauvre » | **Dans le système** : savoir mince, et `SAVOIR/STATE` lue une fois sur quatre |
| **Premier écran attendu** | Sur la planche, SOM-3, FIN-3 et Chevet partagent la même coupe : texte à gauche, objet à droite. Ton verdict sur SOM-3 le dit aussi | **Dans le système** : le choix sur planche revient à l'agent (hypothèse) |
| **Niveau non montré** | Aucune image de niveau dans le paquet | **Dans le système**, sur décision (D4) |

La dernière ligne de la planche est mon avis, pas un verdict.

---

## 5. Propositions, par ordre

Une priorité : **juger avant d'ajouter.**

1. **Verdicts** (aucun run). IDT-1, FIN-3 contre Parité, les quatre paires de la note de tri. Et décider sur traces la ligne du tirage (N6).
2. **Corriger le journal** (N4) avant tout nouveau run : tenir compte de `--fichier` et d'un filtre plus long que la sortie, avec un test. Coût faible. Sans cela, la colonne « routes lues » reste fausse.
3. **Un run sommeil avec accord de génération**, contre SOM-3. Il éprouve d'un coup 13b, 13c et la thèse des intrants.
   - Réussite : tu juges la matière au-dessus de SOM-3, la part d'image se rapproche de 53 %, une autre photo que « Crumpled Sleep », un coût au plus égal à SOM-3 (102 appels, 23 minutes).
   - Arrêt : si la matière ne monte pas avec l'accord, la cause n'est pas l'accès. Revenir alors à la calibration sur tes rendus avant d'ajouter quoi que ce soit.
4. **Rendre au tronc ce qui sert à construire** (N1 à N3), à budget constant : sortir les blocs de trace complète, servis à la demande, et y faire entrer ce que les runs ne lisent pas (gestes de finition, principes des sections ordinaires).
5. **Convergence** : mettre du hasard ou un autre juge dans l'une des trois étapes de N7. Deux pistes à discuter : tu choisis sur la planche quand tu suis le run ; ou le tirage porte sur l'inventaire du sujet écrit par l'agent, pas seulement sur la catégorie.
6. **Question de fond, si tu veux la rouvrir** : une paire avec et sans le système sur un brief, jugée par toi. Elle touche D5 (« une comparaison avec et sans n'est pas exigée ») sans la contredire. Raison de la poser : le coût a encore monté et le seul point de mesure date du 29 octobre.
7. **Corrections mineures** de N9.

---

## 6. Ce que cet audit n'a pas vérifié

- **Lecture.** Lus en entier : le noyau, le tronc `DIRECTION`, l'audit du 11 novembre, le plan, le diff des documents depuis l'audit, la fiche des essais, la trace et les fiches de SOM-3. Les traces de FIN-3, FTX-1 et IDT-1 ont été lues par extraits. Les 114 fichiers inchangés n'ont pas été relus : seuls les constats du 11 novembre y ont été revérifiés.
- **Code.** Les 590 lignes ajoutées à `parcours.py` n'ont pas été relues ligne par ligne ; seules `tirage` et la détection de filtre du journal l'ont été.
- **Validation.** Quatre contrôles rapides lancés ; ni la validation complète avec navigateur, ni `pytest`.
- **Rendus.** Vus sur la planche seulement, pas ouverts dans un navigateur.
- **Journaux bruts.** Les `journal.jsonl` ne sont pas dans l'archive : la commande exacte tapée par les agents de SOM-3 et d'IDT-1 n'est pas connue.
- **Hypothèses.** N7 et la cause du premier écran attendu ne sont pas éprouvées.
