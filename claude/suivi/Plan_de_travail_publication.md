# Plan de travail — Design Governance, du `R2026-11-15o` à une version publiable

**Établi le** 21 novembre 2026, sur `R2026-11-15o` (`master` `03cdd00`).

**Il remplace**, pour la suite, la feuille de route (`Feuille_de_route_publication.md`) et le document de propositions du lot 10 (`Lot_10_Propositions.md`). Il les détaille. Il ne les contredit pas.

**Comment s'en servir.** Chaque lot a :
- un objectif ;
- un périmètre au fichier près ;
- des étapes cochables ;
- ses gardes et ses tests ;
- des critères d'acceptation mesurables ;
- ses livrables ;
- les décisions qu'il attend.

Un lot ne s'ouvre qu'après la décision de Junior sur son document de propositions (règle 1). Ce plan dit **quoi** et **dans quel ordre**. Le document de propositions de chaque lot redit la mesure du moment, avant d'intégrer (règle 4).

---

## 0. Cadre

### 0.1 Objectif

Un système **très bon à l'intérieur comme à l'extérieur**, sur cinq plans : navigation, utilisation, compréhension, présentation, qualité interne. Il doit pouvoir être publié et utilisé par le public et par des experts, au niveau de ce que publient Anthropic, Google ou Artificial Analysis. Il est **meilleur, plus rapide et moins coûteux**, sans perte de qualité des rendus.

### 0.2 Principes de travail

1. **Rien sans décision** (règle 1). Chaque lot commence par des propositions.
2. **Pas de run avant le lot 13.** Entre deux lots, la qualité est gardée par les tests, la préparation complète et des **mesures hors run**, sur les pages déjà produites au PILOT. Chaque rapport dit ce qui n'a pas été mesuré.
3. **Retirer l'obsolète, pas le non-lu** (règle 10). On retire les mesures périmées, les veilles échues, les redites, le matériau de test et les données de runs. On ne retire pas une route parce qu'aucun run ne l'a ouverte.
4. **Une seule source par savoir.** Les commandes lisent le savoir à son lieu, rien n'est recopié (principe déjà appliqué par `parcours.py`).
5. **Chaque garde a son test qui échoue quand on la casse** (mutation rouge), et ce test doit **échouer en nommant la garde, pas en plantant**. Leçon des lots 9b et 9e.
6. **Chaque constat porte la révision où il a été établi.** Leçon de l'erreur sur la comparaison du 29 octobre.
7. **Mesurer le coût d'un run comme il se paie** : nombre de tours multiplié par la taille du contexte, avec le script `Pilot_9b/cout_des_runs.py`. La taille finale du contexte n'est pas le coût.

### 0.3 Ce qui est mesuré aujourd'hui (base de comparaison)

| Grandeur | Valeur en `o` | Source |
|---|---|---|
| Noyau | 45 810 octets, 6 962 mots, 36 blocs, 62 codes, 9 obligations `[REQUIS]` au noyau | `build_core.py`, cartographie |
| Tronc DIRECTION | 31 398 caractères (8 routes, dont 1 de savoir) | `read_route.tronc_text` |
| Lecture fixe d'un run DIRECTION | environ 77 k caractères | Cartographie |
| Fichiers livrés | 151, dont 55 d'atelier (36 %) | Manifeste |
| Run DIRECTION (PILOT) | 116 à 208 tours ; 22 à 46 M jetons lus en cache ; 130 à 300 k en sortie ; 13 à 29 images ; 14 à 27 min | `cout_des_runs.py` |
| Routes | 85 ; 21 lues au moins une fois en 12 runs ; 51 jamais touchées | Journaux |
| Contrôle | 111 codes de garde ; environ 785 cas de test ; préparation d'environ 12 min | Préparation |

---

## 1. Critères de sortie du système (la définition de « fini »)

À la fin du lot 12, chaque ligne est vérifiée, et le lot 13 la confirme sur des rendus.

| Plan | Critère | Comment on le vérifie |
|---|---|---|
| **Navigation** | Une page d'entrée lisible en 2 minutes. Une documentation en quatre types (tutoriel, guides pratiques, référence, explication). Toute page à deux clics au plus de l'entrée. | Un validateur de profondeur de liens ; la lecture de Junior |
| **Utilisation** | Installation en une commande, dépendances comprises. Une archive « skill » sans atelier. Un mode de secours sans navigateur. Des erreurs qui disent quoi faire. | Une installation propre dans un dossier vide ; des tests des messages d'erreur |
| **Compréhension** | Pas de code (`CFT-04a`, `B1b`…) dans les pages pour les personnes, hors référence. Un schéma public. Un glossaire généré depuis les sources. | Un validateur ; le glossaire comparé aux sources |
| **Présentation** | Licence, journal des changements, versions datées juste, page de méthode, page « Fondements et sources », positionnement en une phrase, langue décidée. | Une liste de contrôle à la livraison |
| **Propreté** | Aucun matériau de test, nom de brief ou mesure périmée dans la skill. Aucune veille échue livrée. | Une garde des noms (lot 10A) ; la garde des échéances existante |
| **Qualité interne** | Noyau de 18 000 octets au plus (environ 5 000 tokens). Une commande par étape de la boucle. Toute obligation `[REQUIS]` servie, au noyau ou par une commande testée. | Garde de budget ; garde des planchers étendue |
| **Sobriété** | Lecture fixe d'un run DIRECTION de 30 k caractères au plus, contre 77 k. Sorties d'outils plus courtes (seuils au lot 10B). | Mesures hors run |
| **Preuve** | Coût et qualité mesurés au lot 13 : sans système, `o` et version finale, jugés à l'aveugle. Résultats publiés avec leurs limites. | Protocole du lot 13 |

---

## 2. Décisions à prendre (et le lot qu'elles bloquent)

| # | Décision | Options | Ma recommandation | Bloque |
|---|---|---|---|---|
| D1 | Ligne de veille « Convergences relevées avec le système » (tirée des essais de Junior) | Garder en disant son origine (« essais sur peu de briefs, 09 à 11-2026 ») / la sortir vers le suivi | Garder, origine dite | 10A |
| D2 | Visibilité de DG-777 (le journal de Junior y est) | Privé / public / déplacer le suivi ailleurs | Vérifier ; privé si possible | 10A |
| D3 | Archives intermédiaires dans DG-777 (`l`, `m`, `n`) | Garder / ne garder que la dernière livrée et la `k` de référence | Ne garder que `k` et la dernière | 10A |
| D4 | Licence | MIT et CC BY 4.0 / Apache 2.0 et CC BY 4.0 / autre | MIT pour le code, CC BY 4.0 pour les textes | 12 |
| D5 | Langue | Français seul / français et anglais / anglais avec français tenu | Français et anglais pour l'entrée, le tutoriel et la référence ; savoir en français d'abord | 12 |
| D6 | Nom | Garder « Design Governance » / un nom qui dit la direction artistique | Garder, avec un sous-titre explicite | 12 |
| D7 | Numérotation publique | `R…` seul / `V1.1` publique avec `R…` en interne | `V1.1` publique datée, `R…` en interne | 12 |
| D8 | Juges du lot 13 | Junior seul (règle 7) / Junior et 2 ou 3 designers à l'aveugle | Junior seul, plus des designers en option si le budget le permet | 13 |
| D9 | Conditions du lot 13 | 3 conditions (sans, `o`, final) / 2 (sans, final) | Voir le lot 13 : 2 conditions sur 3 objets, plus `o` sur 1 objet | 13 |

---

## 3. Les lots

### Lot 10A — Propreté (aucun run, 1 session)

**Objectif.** Une skill sans matériau d'essai ni donnée obsolète, et un atelier séparé de la skill.

**Périmètre et étapes.**
- [ ] **A1 Fuites du journal** :
  - `design/savoir/qualite-creative.md` l. 321 : exemples neutres à la place des citations de runs ;
  - `scripts/test_regard.py` l. 167 : donnée neutre à la place de « Terres lentes » ;
  - `design/savoir/gout-et-tendances.md` l. 56 : selon D1.
- [ ] **A2 Mesure obsolète** : `maintenance/versions.md` l. 85, la phrase de coût tirée du 29 octobre, remplacée par la mesure actuelle datée (tours, lecture de cache, durée ; sans comparaison).
- [ ] **A3 Garde des noms de runs** (nouveau code `PRO-01`) :
  - `validate_structure.py` accepte `--interdits FICHIER` ;
  - `preparer_livraison.py` passe `.claude/suivi/noms_interdits.txt` s'il existe (noms de briefs, lieux, titres, artistes inventés des runs) ;
  - le paquet ne contient jamais la liste.
- [ ] **A4 Distribution « skill »** :
  - une liste `skill` dans `scripts/package_manifest.json` : la liste `github` moins l'atelier, soit 55 fichiers (tests, validateurs, fixtures, compilation, préparation, CI, maintenance, génération des supports, `journal_mobilisation.py`) ;
  - `build_distributions.sh` produit `Design_Governance_V1_SKILL.zip`.
- [ ] **A5 Journal optionnel** : les 6 outils de production importent `journal_mobilisation` **seulement s'il est présent**, et s'exécutent normalement sinon.
- [ ] **A6 Route d'instrumentation** : `DIRECTION/LECTURE-INSTRUMENTEE` sort de la skill vers l'atelier (`maintenance/`), avec ses renvois.
- [ ] **A7 Date de révision juste** : la ligne de révision porte la date réelle de livraison. L'étape 6 du déroulé d'un lot (`CLAUDE.md`) le dit.
- [ ] **A8 Suivi** :
  - `suivi/INDEX.md` liste les documents vivants ;
  - les documents dépassés (anciens plans d'audit, lots clos) vont dans `suivi/archives/`, sans être supprimés ;
  - archives de DG-777 selon D3.

**Gardes et tests (mutation rouge, échec nommé).**
- `PRO-01` : un nom interdit remis dans un fichier fait échouer la validation.
- L'archive « skill » ne contient aucun fichier d'atelier, et contient tout fichier cité par le noyau ou par un outil de production.
- Les outils de production se lancent (`--help`, et `parcours.py trace` sur l'exemple) dans une copie **sans** `journal_mobilisation.py`.

**Critères d'acceptation.**
- Zéro occurrence des noms interdits dans les trois archives.
- L'archive « skill » s'installe dans un dossier vide, et `parcours.py verifier` tourne sur une page d'exemple.
- La préparation complète réussit.

**Livrables.** Révision `R…p` (trois archives et bundle), `Lot_10A_rapport.md`, `suivi/INDEX.md`.

---

### Lot 10B — Outils plus sobres (aucun run, 1 à 2 sessions)

**Objectif.** Moins de tours et un contexte plus léger, avec **les mêmes contrôles**. C'est le premier pas de l'architecture « outils d'abord ».

**Étapes.**
- [ ] **B1 Planche de boucle** : `parcours.py captures --version vN` produit **une** image qui met côte à côte le premier écran au bureau et en mobile, en 1×. Le ×2 reste au zoom (`--foyer`) et aux captures de livraison (`--pleine`).
- [ ] **B2 `verifier` en différé** : dès le 2e appel sur une même page, la sortie écran ne montre que les défauts et signaux **apparus ou disparus**, plus le chemin de la fiche complète. `parcours.md` reste complet.
- [ ] **B3 `parcours.py chantier`** : en un appel, il crée les dossiers, lance `tirage`, lance `leviers` si des pôles sont donnés, écrit le gabarit de trace légère et la commande `references` à compléter. Sortie de 1 500 caractères au plus. Il n'écrit aucune décision.
- [ ] **B4 Sommaire du tronc** : `read_route --tronc MODE --fichier` écrit en tête un sommaire, avec une ligne par route (quand la lire, sa ligne-clé). Le corps suit. Le noyau dit de lire le sommaire, puis la route au moment où elle sert.
- [ ] **B5 Trois consignes au noyau** : grouper les commandes ; écrire le HTML une fois puis le retoucher ; ne relancer `verifier` qu'après un changement qui peut modifier un défaut. Environ 200 octets, financés par une redite retirée, à identifier en ouvrant le lot.

**Mesures hors run** (sur les pages du PILOT, `Pilot_9b/objet*/`, sans agent) :

| Mesure | En `o` | Cible |
|---|---|---|
| Caractères affichés par le 2e appel de `verifier` | Environ 1 300 à 4 500 | ÷ 3 au moins |
| Images produites par `captures --version` | 2 (une par largeur) | 1 |
| Appels pour démarrer un chantier | 5 à 15 (journaux) | 1 |
| Tête du tronc DIRECTION à lire d'abord | 31 k caractères | 4 k au plus (sommaire) |

**Gardes et tests.**
- Sortie en différé : un défaut corrigé disparaît, un nouveau apparaît.
- `chantier` ne décide rien (pas de direction écrite) et respecte son plafond de sortie.
- Le sommaire du tronc cite chaque route du tronc.
- Chaque garde a sa mutation rouge.

**Critères d'acceptation.** Les cibles du tableau sont atteintes et la préparation complète réussit.

**Livrables.** Révision `R…q`, `Lot_10B_rapport.md` avec les mesures avant et après.

---

### Lot 11 — Outils d'abord (aucun run, 3 à 4 sessions, en quatre sous-lots)

**Objectif.**
- Un noyau court, environ 5 000 tokens.
- Une commande par étape de la boucle.
- La bibliothèque lue par les commandes.
- La gouvernance en module optionnel.
- Un mode de secours sans outils.

**Destination proposée des 36 blocs du noyau** (à revérifier à l'ouverture de chaque sous-lot) :

| Destination | Blocs (octets) | Total |
|---|---|---|
| **Reste au noyau**, réécrit court | ROLE (1 220), POSTURE (614), ABSOLUS (1 239), BRIEF (1 340), CONTENU (708), DONNEES-EXEMPLE (701), SORTIE (1 334), TRACE (2 273), CHECKPOINT (713), INTEG-RECITATION (316, REQ), INTEG-LIMITES (316, REQ), VER-FAUX-ASSET (456), CHARGE-REGLE (435), CHARGE-FIN (358, REQ), plus un nouveau bloc « La boucle en six commandes » (environ 1 500) | Environ 13 700, réécrit vers 12 000 |
| → `chantier` (cadrer) | CHARGE-DETAILS (5 076, en partie), CHARGE-TROUVER (403), MOY-PLAFOND (3 444, partie moyens), FND-CADRAGE (345, REQ) | |
| → `diverger` | DIR-LEVIERS (4 973, REQ), PREMIER-OBJET (549), STRUCT-TRAME (703), ANCRE (2 078), COMP-CONVERGENCE (846), COMP-SINGULARITE (633) | |
| → `declarer` | DIR-DECLARATION (2 897, REQ), COMP-TYPO (213, REQ), COMP-COULEUR (532, REQ), COMP-TITRE (957) | |
| → `verifier` et `atelier` | BOUCLE (766), BOUCLE-CAPTURE (569), BOUCLE-ATELIER (3 904), STATE-PLANCHER (304, REQ), COMP-CONTROLES (476), VER-SCENE (431), VER-AUDIENCE (371) | |
| → `livrer` | MOY-PLAFOND (partie plafond) | |
| → module de gouvernance | REGISTRES (456) | |

**Sous-lots.**
- [ ] **11a Nouvelle garde des planchers.** Une obligation `[REQUIS]` est tenue soit au noyau, soit par une commande dont un test prouve qu'elle sert le texte de l'obligation, lu à son lieu. Extension de `validate_structure.py` (`PLANCHERS`), avec mutation rouge. **Rien ne sort du noyau avant que cette garde existe.**
- [ ] **11b `diverger` et `declarer`.** Les blocs correspondants sortent du noyau ; le tronc DIRECTION est réduit d'autant.
- [ ] **11c `atelier` et `livrer`**, plus le mode de secours (une page de texte qui dit la boucle sans outils, lue seulement si Python ou le navigateur manquent).
- [ ] **11d Gouvernance optionnelle.** `REGISTRES` et les renvois à la trace complète sont chargés seulement si le travail est repris, audité ou accepté. Le module est documenté comme tel.

**Gardes et tests.**
- Garde de budget du noyau ramenée à 18 000 octets à la fin de 11d (aujourd'hui 46 000).
- Chaque commande a des tests hors réseau, dont un qui vérifie le texte servi (comme P17 pour `leviers`).
- Le tronc DIRECTION fait 12 000 caractères au plus.

**Critères d'acceptation.**
- Noyau de 18 000 octets au plus.
- Lecture fixe d'un run DIRECTION de 30 k caractères au plus.
- Toutes les obligations sont servies et testées.
- Préparation complète réussie.
- Les guides existants ne contredisent pas la nouvelle boucle (relecture).

**Risques et parades.**
- **Homogénéisation** : les commandes servent des questions et des leviers, jamais des réponses. Le hasard (`tirage`) et la « première idée observée » restent.
- **Perte d'une obligation** : la garde 11a passe en premier.
- **Médiums hors Web** : l'identité garde sa planche ; l'imprimé et le reste sont signalés « moins outillés ».

**Livrables.** Une révision par sous-lot et un rapport par sous-lot.

---

### Lot 12 — Documentation de publication (aucun run, 2 à 3 sessions)

**Objectif.** La présentation et la documentation au niveau des publications de référence, décrivant l'architecture finale.

**Documents** (le public visé, l'usage et la longueur sont dits en tête de chacun) :

| Type | Document | Contenu | Cible |
|---|---|---|---|
| Entrée | `README.md` | Ce que c'est, pour qui, en une phrase ; démonstration (un brief, un rendu, la trace) ; installation ; coût mesuré ; limites ; liens vers les 4 types | 1 page, 2 minutes |
| Tutoriel | `docs/tutoriel.md` | « Premier rendu en 10 minutes », pas à pas, avec la boucle en six commandes | Une session |
| Guides pratiques | `docs/guides/` | Une tâche par page : diriger un premier écran, une identité, reprendre un existant, travailler sans navigateur, passer en trace complète | 1 à 2 pages chacun |
| Référence | `docs/reference/` | **Générée** depuis les sources : commandes et options (`--help`), routes (`read_route --sommaire`), codes, statuts, glossaire | Sans rédaction à la main |
| Explication | `docs/fondements.md`, `docs/methode.md` | Pourquoi l'architecture ; les sources de recherche (bibliographie séparée des règles, compatible avec la règle 6) ; la méthode d'évaluation et ses limites | Lecture d'expert |
| Projet | `LICENSE`, `CHANGELOG.md`, `CITATION.cff`, `CONTRIBUTING.md` | Selon D4 et D7 ; le CHANGELOG commence à la version publique | |
| Visuel | Schéma public | Tiré de la cartographie, mis à jour sur l'architecture finale, en clair et en sombre (comme `supports/`) | |

**Étapes.**
- [ ] Réorganiser `guides/` vers les quatre types, sans perte de contenu utile (les doublons partent, avec un tableau de correspondance dans le rapport).
- [ ] Écrire le générateur de référence (`scripts/` côté atelier) et sa garde : référence identique aux sources.
- [ ] Les codes hors de la référence deviennent des mots (garde `DOC-01`).
- [ ] Langue selon D5 ; nom et sous-titre selon D6.
- [ ] Relecture complète de la présentation (règle 5).

**Gardes et tests.**
- Profondeur de liens de 2 au plus depuis le README (`DOC-02`).
- Référence générée identique aux sources (`DOC-03`).
- Aucun code dans les pages pour les personnes (`DOC-01`).
- Les gardes existantes : liens, LIS-01, LAN-01, glossaire.

**Critères d'acceptation.** La section 1 est cochée entièrement, sauf « Preuve ». Relecture et décision de Junior.

**Livrables.** Révision publiable candidate (`V1.1` selon D7), `Lot_12_rapport.md`.

---

### Lot 13 — Évaluation finale (les seuls runs)

**Objectif.** Mesurer, en une seule campagne, la qualité et le coût de la version candidate, et publier les résultats avec leurs limites.

**Protocole.**
- **Objets** : 3 petits objets en code, sur des genres différents (atmosphère, outil ou données, identité), aucun déjà vu au PILOT.
- **Conditions** (D9) :
  - **sans système** et **version finale** sur les 3 objets ;
  - **`o`** sur 1 objet, pour situer le gain des lots 10 à 12.
  - Soit 7 runs.
  - Variante : 3 conditions sur 3 objets, soit 9 runs, si les limites le permettent.
- **Agents** : neufs, même modèle, même effort, dossier vide, même prompt au brief près (règle 9). Le mode est imposé `DIRECTION` (règle 8).
- **Aveugle** :
  - correspondance tirée au sort avant les runs, empreinte publiée ;
  - captures refaites aux mêmes réglages ;
  - traces masquées jusqu'au jugement.
- **Jugement** : Junior, par paires, avec une phrase de raison (D8 pour d'autres juges). Les résultats vont au carnet de goût.
- **Coût** : `cout_des_runs.py` sur chaque transcription (tours, contexte maximal, lecture de cache, sortie, images, durée).
- **Règle de décision** : la version finale est retenue si elle n'est pas moins bien jugée que « sans système » sur la majorité des objets **et** si son coût est inférieur d'au moins 30 % à celui de `o`. Sinon, on identifie la cause avant de publier.
- **Publication** : `docs/methode.md` et une page de résultats donnent les chiffres, les limites (un seul juge, petit échantillon, un seul modèle) et les captures.

**Livrables.** `Pilot_final/` dans le suivi, page de résultats dans le paquet, `Lot_13_rapport.md`, décision de publication.

---

## 4. Ordre, points d'arrêt et charge

| Étape | Point d'arrêt (décision de Junior) | Charge estimée | Runs |
|---|---|---|---|
| Décisions D1 à D3 | Avant 10A | Une réponse | 0 |
| 10A Propreté | Propositions, puis rapport | 1 session | 0 |
| 10B Outils sobres | Propositions, puis rapport | 1 à 2 sessions | 0 |
| 11a à 11d Outils d'abord | Propositions et rapport à chaque sous-lot | 3 à 4 sessions | 0 |
| Décisions D4 à D7 | Avant 12 | Une réponse | 0 |
| 12 Documentation | Propositions, relecture, rapport | 2 à 3 sessions | 0 |
| Décisions D8 et D9 | Avant 13 | Une réponse | 0 |
| 13 Évaluation finale | Protocole, jugement, décision de publication | 1 à 2 sessions | 7 à 9 |

Une session prépare au plus un lot ou un sous-lot, pour tenir dans les limites d'usage. Le suivi (`CLAUDE.md`, `suivi/INDEX.md`) est mis à jour à la fin de chacune, pour reprendre sans perte.

## 5. Risques globaux et parades

| Risque | Parade |
|---|---|
| Une régression de qualité invisible sans run | Contrôles inchangés, gardes de service du savoir, mesures hors run ; le lot 13 tranche |
| Un chantier trop gros (lot 11) | Quatre sous-lots, chacun livrable et réversible ; la garde des planchers d'abord |
| Une documentation qui vieillit vite | La référence est générée et gardée ; la veille reste datée |
| Une erreur de mesure ou de constat | Chaque constat porte sa révision ; le coût se mesure avec le script ; chaque rapport a une section « ce qui n'est pas mesuré » |
| Les limites d'usage | Une session par lot ; les runs groupés au lot 13 ; une variante à 7 runs |

## 6. Hors de ce plan

- La génération d'images (piste en attente de décision) et l'observation de la modale par recherche d'images.
- La série « capacité esthétique » : elle pourra reprendre après le lot 13, sur la version publiée.
