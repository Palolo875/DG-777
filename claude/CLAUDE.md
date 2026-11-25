# Design Governance V1 — consignes de travail

Ce fichier et le dossier `.claude/` restent hors du paquet : la validation les ignore, et le build ne copie que ce que liste `scripts/package_manifest.json`. Ne les ajoutez jamais au manifeste ni à un commit.

## Avec qui et comment

- **Personne** : Junior (Kamel), designer et développeur. Il maintient ce paquet, une skill de gouvernance de design pour agents d'IA.
- **Réponses** : en français, structurées, avec peu de remplissage. Distinguer ce qui est certain, probable ou à vérifier. Avancer étape par étape, sans changer de méthode en silence.
- **Usage** : ses limites d'usage sont serrées. Adapter l'effort à la tâche, et signaler une tâche surdimensionnée.

## Règles de travail (elles priment)

1. **Rien n'est intégré sans discussion et décision.** Ses idées sont des propositions à discuter.
2. **La version publique est V1.2.0** (V1.1 décidée en D7 le 22 novembre ; V1.1.1 correctif et V1.2.0 fin du lot 14, le 25 novembre ; garde VER-01 : manifeste, titre du README, citation, journal des changements). Les révisions internes portent des identifiants neutres : série `R2026-11-15a` à `z` close, puis **série `R2026-11-25a`, b, c…** (accord de Junior).
3. **L'historique reste hors du paquet** : récits de runs, anciens constats, anciens alias. Le suivi vit dans `.claude/suivi/`.
4. **Vérifier dans les fichiers avant de proposer.** Ne jamais se fier à la mémoire, ni à une vue dérivée.
5. **Avant toute livraison** : relire la présentation, faire la validation complète avec navigateur, régénérer les archives.
6. **Un principe s'énonce sans son auteur.** Les normes, lois et ressources à atteindre restent nommées. Une ligne `[VEILLE]` garde son type de source et sa date.
7. **Pas de juge externe à l'aveugle.** C'est Junior qui juge les rendus.
8. **En test, le mode `DIRECTION` sert en entier.**
9. **Un run = un agent neuf dans un dossier vide**, avec le paquet installé depuis l'archive livrée. Pour chaque rendu, livrer le HTML autonome et la capture de la page entière.
10. **Économiser l'usage.** Une route qu'aucun run n'a ouverte n'est pas « en trop ».

**Sécurité.** Une clé d'API, si elle est un jour fournie, reste dans l'environnement du run : jamais dans le paquet, le suivi ou la mémoire.

## Lire ses réponses courtes

- « Allons-y » ou « Poursuivons » **après un rapport** : rédiger les propositions du lot suivant.
- « D'accord », « Ça me va » ou « Allons-y » **après des propositions** : appliquer les options A partout.

## Déroulé d'un lot

1. Relire chaque constat dans les fichiers : toujours vrai, déjà corrigé, ou à écarter.
2. Écrire le document de propositions dans `.claude/suivi/` : mesure, puis proposition, avec des options et une recommandation.
3. Attendre la décision.
4. Intégrer sur une branche. Chaque garde nouvelle a un test avec une mutation rouge : on casse la propriété et le test doit échouer.
5. Pendant le travail : `python3 scripts/validate_all.py --rapide` (≈ 90 s, sans navigateur ni build). Avant toute livraison, la préparation complète, qui prend environ 8 minutes (459–469 s mesurées le 25 novembre ; **monter la révision avant**, étape 6) :
   ```bash
   python3 scripts/preparer_livraison.py --require-browser --empreintes
   ```
6. Monter la révision (série `R2026-11-25…`) avec `sed` dans quatre fichiers : `maintenance/versions.md`, `RELEASE_NOTES.md`, `README.md` (motif « révision interne \`R…\` ») et `design/savoir/connexions.md`. **La date affichée est la date réelle de livraison**, pas celle de la série `R2026-11-15`.
7. Commiter, puis fusionner : `git merge --no-ff` dans `master`.
8. Vérifier que l'archive GitHub est identique au commit, fichier par fichier.
9. Rassembler la sortie : les deux zips suffixés de la révision, et `git bundle create … --branches`.
10. Écrire le rapport, puis mettre à jour le plan (`Plan_corrections_Design_Governance.md`) et le registre (`Registre_couverture_audit_neuf.md`).

## Repères techniques

- **Lecture par code de route** : `python3 scripts/read_route.py CODE`. Autres formes : `--trouver TERME`, `--mode MODE`, et `--tronc MODE --fichier tronc.txt`, qui écrit la ligne du mode puis son tronc.
- **Budgets** :
  - le noyau `SKILL.md` est limité à **33 000 octets** (décision du 25 novembre ; 31 699 aujourd'hui) ; il est compilé par `scripts/build_core.py`, dont le registre s'appelle `NOYAU` ;
  - un tronc par mode est limité à 40 000 caractères (lot 11c ; DIRECTION en lit 35 177).
- **Où vivent les gardes** :
  - `scripts/validate_structure.py` : planchers `[REQUIS]`, GLO-02, LIS-01, LAN-01, VOU-01…
  - `scripts/validate_reading_map.py` : conditions de façade, en liste close ;
  - `scripts/validate_design_governance.py` : liens, ancres, manifeste.
- **Ajouter une règle** : suivre la section « Ajouter ou modifier une règle » de `maintenance/README.md`.
- **Journal de mobilisation** : `DG_JOURNAL=run.jsonl` fait noter ce que les outils ont servi, et `scripts/journal_mobilisation.py` en tire une fiche.

## État du chantier (25 novembre 2026)

- **Le suivi a un index** : `suivi/INDEX.md` (documents vivants ; le reste est dans `suivi/archives/`).

- **`master` est en `R2026-11-25d`** (version publique V1.2.0 ; V1.3.0 prévue à la fin du lot 15), au commit `7fd7b1d`. Les lots S, 1 à 9e, 10A, 10B, 11, 12, 13a, 14 (a, b, c), « outil » et 15a sont faits et livrés ; 15b (idée tirée d'un fait de deuxième rang, rareté par rang, plaidoyer pour la modale) est décidé, à faire. Dans DG-777, seules les archives `k` (référence) et `25d` (dernière) restent, plus `claude/livraison/R2026-11-25d/`. Le plan et le registre, dans `.claude/suivi/`, les détaillent.
- **Le suivi vit aussi sur GitHub** : `palolo875/DG-777`, branche `claude/chat-session-bfv0no`, dossier `claude/` (décompressé, sans zip). Il est hors du paquet.
- **Lot 9, les runs de contrôle** :
  - les runs 9 à 16 sont faits ;
  - le registre est `suivi/Registre_des_runs.md` et le rapport `suivi/archives/Lot_9_Run_rapport.md`, avec les verdicts de Junior ;
  - le run 15 a été fait à la main par Claude (avec génération dirigée).
- **En cours : la série « capacité esthétique »** :
  - un run à la fois, un agent neuf, sur un petit objet entièrement en code ;
  - Internet gratuit autorisé ; génération d'images, outils branchés et services payants interdits ;
  - le premier objet a été le billet de concert (run 16) ; **on discute avant chaque run** (« Pas de run direct »).
- **Lot 9b fait** (`archives/Lot_9b_rapport.md`) : `parcours.py leviers`, diagramme parmi les convergences, « choisi par » en trace légère, D1, D2. **PILOT fait** (`Pilot_9b/`) : `l` préféré sur 2 objets sur 2, à l'aveugle ; carnet de goût ouvert (`Carnet_de_gout.md`).
- **Lot 9c fait** (`archives/Lot_9c_rapport.md`) : modale au second degré observée (première idée), deuxième attribut, lecture hors journal (C-1, C-2). Registre des convergences hors paquet (`Convergences_observees.md`).
- **Lot 9d fait** (`archives/Lot_9d_rapport.md`) : Fontshare dans `polices`, vague typographique (vague 4) relevée par `regard`, signal « la page ne commente pas son design », calibration dès que la décision visuelle est ouverte ; B-4 clos.
- **Lot 9e fait** (`archives/Lot_9e_rapport.md`) : références sans jugement signalées par `verifier`, référence de niveau d'une source éditée ; tous les autres constats du lot 9 clos. **Pas de run tant que Junior ne le demande pas.**
- **Documents de référence (cadrage du 21 novembre)** :
  - `suivi/Plan_de_travail_publication.md` dit **quoi faire et dans quel ordre** (10A, 10B, 11, 12, 13) ;
  - `suivi/Pistes_innovantes.md` dit **comment le faire mieux** (noyau-index, contexte frais, regarder peu et bien, modale nommée, goût par l'exemple, budgets visibles ; quatre profils d'environnement E1 à E4, sous-agents en bonus seulement).
  - La feuille de route et les propositions du lot 10 sont remplacées.
- **Décision de Junior (21 novembre)** : le carnet de goût devient une fonction proposée à chaque utilisateur, personnelle et facultative (« si utile »). Le carnet de Junior reste privé.
- **Lot 10A fait** (`suivi/Lot_10A_rapport.md`) : fuites du journal retirées, mesure obsolète remplacée, garde PRO-01 (liste `suivi/noms_interdits.txt`, passée par la préparation), journal optionnel, date réelle, suivi rangé (`INDEX.md`, `archives/`). A4 et A6 reportés au lot 12.
- **Lot 10B fait** (`suivi/Lot_10B_rapport.md`) : `captures --version` en une image, `verifier` différentiel (2e appel 3 659 → 347 caractères), `chantier`, sommaire du tronc (règle de vitesse gardée), sobriété au noyau.
- **Lot 11a fait** (`suivi/Lot_11a_rapport.md`) : troisième forme de plancher (`("ligne", route)`), aucun contenu déplacé.
- **Lot 11b fait** (`suivi/Lot_11b_rapport.md`) : la table des signaux du noyau indexe les 85 routes (garde IDX-01), plafond du noyau provisoirement à 48 500.
- **Lot 11c fait** (`suivi/Lot_11c_rapport.md`) : 13 blocs de procédure en différé, 12 lignes d'invariant au noyau ; noyau 30 502 octets. Junior a laissé le choix des lignes (« À toi le choix »).
- **Lot 11d fait** (`suivi/Lot_11d_rapport.md`) : passage « Sans outils », garde SUB-01, pas de réécriture des blocs gardés (décision : D3 A). **Lot 11 clos** (bilan au rapport 11d).
- **Lot 12** : propositions dans `suivi/Lot_12_Propositions.md`, « D'accord » de Junior (options A, et mes recommandations D4 à D7 : MIT et CC BY 4.0, français avec `README.en.md`, nom gardé avec sous-titre, `V1.1` publique ; à lui rappeler avant 12d). **12a fait** (`suivi/Lot_12a_rapport.md`) : DOC-01, DOC-02 (trois clics), README « Comment l'agent lit », guide sans outils. **12b fait** (`suivi/Lot_12b_rapport.md`) : référence générée (`scripts/reference.py`, DOC-03), carte `supports/lecture.*`, garde de débordement des cartes.
- **12c abandonné** (mesure : aucun fichier d'atelier ouvert en 4 runs ; une ligne du README suffit). **12d fait** (`suivi/Lot_12d_rapport.md`) : D4 à D7 confirmées une par une ; licences, journal des changements, citation, contribution, `README.en.md`, VER-01. **Lot 12 clos.**
- **Lot 13 en cours** (décision du 25 novembre : option B, Junior juge seul, « attention à mes limites ») : **étape 1** = V1.1.0 sur les deux objets du PILOT (runs 19x, 20x), même prompt mot pour mot, mode libre, comparée à 17l et 18l en paires à l'aveugle (A/B, C/D ; correspondance tirée avant, `suivi/Pilot_final/protocole.md`). **Résultats** : coût −29 % de tours, −32 % de cache lu ; qualité 1–1 (widget : V1.1.0 ; invitation : `l`) ; jugement au carnet de goût. **13a fait** (`suivi/Lot_13a_rapport.md`, décision « Corrections d'abord. Pas de run direct. ») : V1.1.1, atelier dans tous les modes. **Étape 2** (sans système et V1.1.1 sur un objet neuf, en DIRECTION) : **pas de run sans décision de Junior**. Titulaire de la licence écrit « Palolo875 et les contributeurs » : à confirmer par Junior. D2 (visibilité de DG-777) : mise de côté par Junior. **Pas de run** avant le lot 13 (décision du 21 novembre).
- **Discussion du système du 25 novembre** (après le run 21, `suivi/Run21/`) : 18 pistes notées, **aucune intégrée**, résumées dans `suivi/Pistes_25_novembre.md` (voir, composition, hiérarchie, finition, assets, recettes, mouvement, évaluation, variété, brief vague).
- **Lot 14 « voir, et oser »** (`suivi/Lot_14_Propositions.md`, « D'accord, on lance ») : **14a fait** (`suivi/Lot_14a_rapport.md`) ; **14b fait** (`suivi/Lot_14b_rapport.md`) ; **lot outil fait** (`suivi/Lot_outil_rapport.md`, préparation 891 → 459 s) ; **14c fait** (`suivi/Lot_14c_rapport.md`, quatre signaux ; vidéo H retirée par Junior : à l'évaluation, joindre les pages HTML sous des noms neutres) ; **V1.2.0 publiée**. Ensuite : lot 15 « faire » (recettes F, matière E et D, inventaire du sujet I et M, rareté J, plaider la modale Q1-2), puis une campagne de runs sur décision de Junior.
- **Suivi sans lot** : A-2 (générique sous le premier écran) au carnet de goût ; A-4 (briefs qui vivent de l'image) dépend de la décision sur la génération d'images.
- **Pistes à proposer, à ne pas intégrer** :
  - observer la modale par une recherche d'images, et calibrer le niveau avec une liste de sources par objet ;
  - obtenir l'accord pour la génération d'images quand personne n'est là.
- **Décision tacite** : LIS-01 mesure le texte visible, sans les cibles de liens. Junior ne l'a pas contestée.
