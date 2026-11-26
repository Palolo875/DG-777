# Lot 12d — Rapport : les fichiers du projet, et la V1.1.0

- **Révision** : `R2026-11-15x`, publiée comme **V1.1.0** le 22 novembre 2026.
- **Branche** : `lot-12d`.
- **Décisions** :
  - 12c : « Poursuivons » après mon avis. **12c abandonné** (option A) : l'archive « skill » sans l'atelier n'apportait rien à ce que lit l'agent ; à la place, une ligne du README dit quels dossiers ignorer.
  - D4 à D7, confirmées une par une : **MIT + CC BY 4.0**, **français + `README.en.md`**, **nom gardé avec sous-titre**, **V1.1 datée**.
- **Runs** : aucun.

## 1. Pourquoi 12c a été abandonné (mesure)

- L'atelier pèse 686 Ko sur 2,9 Mo (−24 %), un poids qui ne joue que sur le téléchargement.
- Dans les 4 runs du PILOT, les agents n'ont ouvert **aucun** test, validateur ni fichier de maintenance (seul `journal_mobilisation.py`, appelé par le protocole du run).
- Coût évité : une troisième archive à construire et valider à chaque révision, 35 renvois réécrits pour elle seule.
- Ce qui en reste : la clarté pour un utilisateur public, obtenue par une phrase du README (« Pour utiliser la skill, vous pouvez ignorer l'atelier… »).

## 2. Ce qui change

| Fichier | Contenu |
|---|---|
| `LICENSE` | Deux licences selon la nature du fichier : MIT pour le code (`.py`, `.sh`, `.yml`, `.json`, gabarit HTML), CC BY 4.0 pour le reste ; la police Manrope garde l'OFL. Titulaire : « Palolo875 et les contributeurs de Design Governance » (le nom public du dépôt) — **à changer si tu veux un autre nom**. |
| `LICENSE-CC-BY-4.0.txt` | Texte officiel, téléchargé depuis creativecommons.org (18 657 octets). |
| `CITATION.cff` | Titre avec sous-titre, version 1.1.0, date, dépôt, licences, résumé. |
| `CHANGELOG.md` | S'ouvre à V1.1.0 : ajouté, changé, contrôles ajoutés ; renvoie à la fiche de version. Les notes de version (`RELEASE_NOTES.md`) restent : elles décrivent la révision livrée. |
| `CONTRIBUTING.md` | Proposer, écrire une règle (renvoi à la procédure), trois principes du projet, vérifier, licence des contributions. |
| `README.en.md` | Présentation courte en anglais : ce que c'est, pour qui, installation, comment l'agent lit, limites, licences. |
| Version | `V1.0.0` → **`V1.1.0`** : manifeste, titre du README (avec le sous-titre « direction artistique et preuve pour agents de design »), fiche de version, notes de version, guide 3, cartes régénérées. Le README dit « révision interne `R…` ». |
| README | Ligne « Projet » du tableau du dépôt (en mots : la garde du glossaire refuse « `LICENSE` » en capitales), phrase sur l'atelier à ignorer. |

## 3. Garde nouvelle et mutations rouges

**VER-01** (garde 31) : la version du manifeste est la même dans le titre du README, le champ `version` de la citation et la **première** entrée du journal des changements. 5 cas (`VersionPublique`).

| Mutation | Résultat |
|---|---|
| L'écart n'est plus relevé | Rouge : `test_readme_en_retard`, `test_citation_en_retard`, `test_journal_sans_entree_en_tete` |
| Le champ de la citation n'est plus comparé | Rouge : `test_citation_en_retard` |
| La version peut être n'importe quelle entrée du journal | Rouge : `test_journal_sans_entree_en_tete` |

## 4. Préparation et livraison

- **Préparation complète** : `--require-browser --empreintes`, réussie du premier coup.
  - Tests : régressions d'audit 193 (188 + 5), budget 19, `parcours` 176, `read_route` 106, `regard` 41, journal 19, préparation 10, `check_render` A, B et C ; quatre cartes sans défaut bloquant ; contrôle de déplacement PASSED.
  - Validations de structure, de carte de lecture, des supports, complète et locale : PASSED. Garde PRO-01 active.
- **Commits** : `bad0d58` sur `lot-12d`, fusionné en `04688c2` sur `master` (`--no-ff`).
- **Archive GitHub** : les **164** fichiers sont identiques au commit (158 + les six fichiers du projet).
- **Sortie** :
  - `Design_Governance_V1_GITHUB_R2026-11-15x.zip` (sha256 `b48305d0…42d8`), à côté de la `k` ;
  - `claude/livraison/R2026-11-15x/` : archive Local (sha256 `ded1b639…e87a`) et bundle vérifié.
  - La `w` est retirée de DG-777. Elle reste dans l'historique et dans le bundle.

## 5. À noter pour la suite

- **La règle 2 de `CLAUDE.md`** (« les corrections restent en V1.0 ») est dépassée par D7 : la version publique est V1.1.0 ; les révisions `R…` continuent en interne.
- **La commande de montée de révision** pour le README devient : `sed -i 's/révision interne \`R…\`/…/' README.md`.
- **Le lot 12 est clos** : 12a, 12b, 12d livrés ; 12c abandonné sur mesure.
