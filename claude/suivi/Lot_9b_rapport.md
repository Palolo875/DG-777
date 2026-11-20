# Lot 9b — Rapport

- **Révision** : `R2026-11-15l`.
- **Branche** : `lot-9b`, fusionnée dans `master` avec `--no-ff`.
- **Décision** : « Vas y » après le document de propositions (`Lot_9b_Propositions.md`). Les options A s'appliquent partout.

## 1. Ce qui est intégré

| Proposition | Ce qui change dans le paquet | Garde (test) |
|---|---|---|
| **P1** Leviers de caractère avant le build | Nouvelle sous-commande `parcours.py leviers "pôle[,pôle]"`. Elle lit à leur lieu :<br>• les leviers et le piège réflexe des pôles choisis (`BIBLIOTHEQUE/READ`) ;<br>• l'ordre de composition et « Classique et expressif » (`SAVOIR/FRAME`).<br>Elle refuse un pôle inconnu, deux pôles d'une même paire, plus de deux pôles et une demande vide (code 2). Si la source est cassée : code 3.<br>Une phrase au noyau (`DIR-DECLARATION`). Elle est documentée dans `scripts/README.md`, le glossaire (« Leviers »), `maintenance/evolution.md` et la fiche de version. | P17, P18 |
| **P2** Diagramme parmi les convergences | Une ligne dans la table des signaux de convergence de `SELECT` (`design/formes/choisir.md`), avec sa question de reprise vers `CFT-04a`. La fiche de `verifier` la sert quand un objet de preuve est nommé (`--foyer`), et seulement alors. | P19, P20 |
| **P3** Qui a choisi | La ligne « modal, trame et parti » (`DIR-LEVIERS`, au noyau) nomme qui a fait le choix : auteur du rendu, personne ou absent. `parcours.py trace` le signale s'il manque ; c'est un signal, pas un échec. Les trois exemples de `references/examples.md` et celui du guide 3 portent « choisi par ». | P68 à P71 |
| **D1** Plancher et plafond | La passe de finition (`ACTION/ATELIER-EDITION`, au noyau) dit qu'un relevé vide ne prouve pas la réussite. La fiche de `verifier` le disait déjà quand aucun signal n'est relevé. | P21 |
| **D2** Classique et expressif | Un paragraphe dans `SAVOIR/FRAME`, section SINGULARITE, servi par `leviers`. | P17 |
| **D3** et **D4** | Rien ne change, comme le prévoyait l'option A. | — |

**Noyau** : il passe de 45 250 à 45 599 octets, pour un plafond de 46 000. Il n'a pas été nécessaire de retirer une redite.

## 2. Mutations rouges

Les mutations ont été faites une à une. Chacune casse la propriété ; le test a été lancé, puis la source restaurée.

| Mutation | Résultat |
|---|---|
| Une ligne de la table de READ renommée (« Tensions ») | Rouge : P17, P18 |
| Ordre de composition de FRAME sans son gras | Rouge : P17, P18 |
| Paragraphe « Classique et expressif » renommé | Rouge : P17, P18 |
| Refus de deux pôles d'une même paire désactivé | Rouge : P18 |
| Ligne « diagramme » de SELECT modifiée | Rouge : P19, P20 |
| Service de la question dans `verifier` retiré | Rouge : P20 |
| Service sans la condition « objet de preuve nommé » | Rouge : P20 |
| Signal « choisi par » de `trace` retiré | Rouge : P71 |
| Exemple de la skill sans « choisi par » | Rouge : P68 |
| Phrase « relevé vide » retirée de la passe de finition | Rouge : P21 |

**Correction en cours de route.** Les trois premières mutations faisaient d'abord **planter** le test (code 1) au lieu de produire un échec nommé. Le test intercepte maintenant l'erreur de lecture, et l'échec est nommé.

## 3. Écarts par rapport aux propositions

- **« Statut PILOT » de P1 (ma formulation, erronée).** Les statuts du cycle de vie (`SEED`, `PILOT`…) s'appliquent aux **routes**. `leviers` n'en crée aucune : c'est une sous-commande qui sert des sections existantes. Elle entre donc au socle comme tout le paquet (`SEED`, retirable, ligne dans `maintenance/evolution.md`). La mesure prévue reste le PILOT de P6, qui est un protocole de test, pas un statut.
- **« En échange d'une redite » (P1).** Ce n'était pas nécessaire : le noyau reste sous son plafond de 46 000 octets.

## 4. Préparation et livraison

- **Première préparation : échouée.** Mon ajout à la fiche de version formait un paragraphe de 1 028 signes, au-delà de la limite de 900 (LIS-01). Je l'ai découpé en liste.
- **Seconde préparation : réussie.** `python3 scripts/preparer_livraison.py --require-browser --empreintes`.
  - Tests : `parcours` 159 cas, avec navigateur ; `check_render` A, B et C ; `regard` 39 ; `read_route` 106 ; régressions d'audit 155 ; budget du noyau 19.
  - Validations complète et locale : PASSED.
  - Le contrôle de l'export Local écarte le navigateur, comme prévu ; il garde donc ses mentions NOT-VERIFIED.
- **Commits.** `9505f4a` sur `lot-9b`, fusionné en `5d11ab9` sur `master` (`--no-ff`).
- **Archive GitHub.** Les 151 fichiers sont identiques au commit fusionné, comparés un à un. Aucun fichier n'est absent.
- **Sortie** (dépôt DG-777, branche `claude/chat-session-bfv0no`) :
  - `Design_Governance_V1_GITHUB_R2026-11-15l.zip` (sha256 `11ef26a3…275fb`), à la racine, à côté de la `k` ;
  - `claude/livraison/R2026-11-15l/Design_Governance_V1_LOCAL_R2026-11-15l.zip` (sha256 `df6afe52…8baaec`) ;
  - `claude/livraison/R2026-11-15l/design-governance_R2026-11-15l.bundle`, `--branches` : `master` et `lot-9b`, historique complet, vérifié.

## 5. Ce que ce lot ne prouve pas

- Que les rendus seront meilleurs. C'est l'objet du PILOT (P6) : trois à cinq objets, deux agents neufs par objet, Junior juge sans connaître la condition.
- Que les agents appelleront `leviers`. La phrase est au noyau, au point de déclaration ; le journal de mobilisation le dira au prochain run.
- Que la question du diagramme sera suivie. Elle est servie, mais elle se juge sur capture.
