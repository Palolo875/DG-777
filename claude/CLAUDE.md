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
6. Monter la révision avec `sed` dans quatre fichiers : `maintenance/versions.md`, `RELEASE_NOTES.md`, `README.md` et `design/savoir/connexions.md`.
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

## État du chantier (18 novembre 2026)

- **`master` est en `R2026-11-15k`**, au commit `c1fe44a`. Les lots S et 1 à 8b sont faits et livrés. Le plan et le registre, dans `.claude/suivi/`, les détaillent.
- **Le lot 9, le run de contrôle, a été exécuté.** Le brief portait sur la landing « Quote-part ». Les fichiers sont dans `.claude/suivi/Run9/`.
- **Il manque le verdict de Junior sur le rendu**, avant d'écrire `Lot_9_Run_rapport.md`.
- **Candidats au lot 9b**, à proposer et non à intégrer :
  1. La fiche du journal range le tronc écrit avec `--fichier` sous « Manques », alors que c'est le chemin que prescrit le noyau. C'est une fausse alerte.
  2. La trace légère du run a trois lignes de plus de 600 caractères. L'outil les signale, et l'agent ne les a pas raccourcies.
  3. La réponse visible ne nomme pas les réserves restantes (contraste du texte, nom accessible des contrôles).
- **Décision tacite** : LIS-01 mesure le texte visible, sans les cibles de liens. Junior ne l'a pas contestée.
