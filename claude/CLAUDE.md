# Design Governance V1 — consignes de travail

Ce fichier et le dossier `.claude/` restent hors du paquet : la validation les ignore, et le build ne copie que ce que liste `scripts/package_manifest.json`. Ne les ajoutez jamais au manifeste ni à un commit.

## Avec qui et comment

- **Personne** : Junior (Kamel), designer et développeur. Il maintient ce paquet, une skill de gouvernance de design pour agents d'IA.
- **Réponses** : en français, structurées, avec peu de remplissage. Distinguer ce qui est certain, probable ou à vérifier. Avancer étape par étape, sans changer de méthode en silence.
- **Usage** : ses limites d'usage sont serrées. Adapter l'effort à la tâche, et signaler une tâche surdimensionnée.

## Règles de travail (elles priment)

1. **Rien n'est intégré sans discussion et décision.** Ses idées sont des propositions à discuter.
2. **Les corrections restent en V1.0.** Les révisions portent des identifiants neutres : `R2026-11-15a`, b, c…
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
5. Lancer la préparation complète, qui prend environ 12 minutes :
   ```bash
   python3 scripts/preparer_livraison.py --require-browser --empreintes
   ```
6. Monter la révision avec `sed` dans quatre fichiers : `maintenance/versions.md`, `RELEASE_NOTES.md`, `README.md` et `design/savoir/connexions.md`. **La date affichée est la date réelle de livraison**, pas celle de la série `R2026-11-15`.
7. Commiter, puis fusionner : `git merge --no-ff` dans `master`.
8. Vérifier que l'archive GitHub est identique au commit, fichier par fichier.
9. Rassembler la sortie : les deux zips suffixés de la révision, et `git bundle create … --branches`.
10. Écrire le rapport, puis mettre à jour le plan (`Plan_corrections_Design_Governance.md`) et le registre (`Registre_couverture_audit_neuf.md`).

## Repères techniques

- **Lecture par code de route** : `python3 scripts/read_route.py CODE`. Autres formes : `--trouver TERME`, `--mode MODE`, et `--tronc MODE --fichier tronc.txt`, qui écrit la ligne du mode puis son tronc.
- **Budgets** :
  - le noyau `SKILL.md` est limité à 46 000 octets ; il est compilé par `scripts/build_core.py`, dont le registre s'appelle `NOYAU` ;
  - un tronc par mode est limité à 35 000 caractères.
- **Où vivent les gardes** :
  - `scripts/validate_structure.py` : planchers `[REQUIS]`, GLO-02, LIS-01, LAN-01, VOU-01…
  - `scripts/validate_reading_map.py` : conditions de façade, en liste close ;
  - `scripts/validate_design_governance.py` : liens, ancres, manifeste.
- **Ajouter une règle** : suivre la section « Ajouter ou modifier une règle » de `maintenance/README.md`.
- **Journal de mobilisation** : `DG_JOURNAL=run.jsonl` fait noter ce que les outils ont servi, et `scripts/journal_mobilisation.py` en tire une fiche.

## État du chantier (21 novembre 2026)

- **Le suivi a un index** : `suivi/INDEX.md` (documents vivants ; le reste est dans `suivi/archives/`).

- **`master` est en `R2026-11-15p`**, au commit `b541344`. Les lots S, 1 à 9e et 10A sont faits et livrés. Dans DG-777, seules les archives `k` (référence) et `p` (dernière) restent, plus `claude/livraison/R2026-11-15p/`. Le plan et le registre, dans `.claude/suivi/`, les détaillent.
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
- **Prochaine étape** : le lot 10B (outils plus sobres), sans run, par son document de propositions. D2 (visibilité de DG-777) reste à vérifier par Junior.
- **Suivi sans lot** : A-2 (générique sous le premier écran) au carnet de goût ; A-4 (briefs qui vivent de l'image) dépend de la décision sur la génération d'images.
- **Pistes à proposer, à ne pas intégrer** :
  - observer la modale par une recherche d'images, et calibrer le niveau avec une liste de sources par objet ;
  - obtenir l'accord pour la génération d'images quand personne n'est là.
- **Décision tacite** : LIS-01 mesure le texte visible, sans les cibles de liens. Junior ne l'a pas contestée.
