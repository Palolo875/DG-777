# Lot 8b — Les sept critères de livraison : mesures et propositions

18 novembre 2026. Révision de départ : `R2026-11-15j`. Document hors du paquet. Rien n'est intégré.

Ce lot passe le paquet au crible des sept critères du plan (§ 1 bis). Pour chaque critère, je donne ce que j'ai mesuré, puis ce que je propose. Les mesures sont faites sur les fichiers actuels, avec des scripts lancés aujourd'hui ; l'installation a été rejouée dans un projet vide.

| Critère | Mesure | Verdict | Proposition |
|---|---|---|---|
| 1. Entrée | Le README donne les trois entrées dans sa première table : guide 1 pour une personne, `SKILL.md` pour un agent, `maintenance/README.md` pour le mainteneur. | Tenu | — |
| 2. Un lieu par sujet | Le guide 3 (32 k) redit cinq procédures qui ont leur propriétaire ; 13 conditions de façade existent pour qu'il ne s'en écarte pas. | Non tenu | § 2 |
| 3. Aucun reste | 0 lien d'ancre cassé, 0 titre vide. Mais aucun contrôle ne vérifie les ancres : un lien vers une section renommée casserait sans alerte. | Tenu, sans garde | § 3 |
| 4. Lisibilité | Dans les textes pour les personnes : 14 cellules de table de plus de 500 caractères, 4 paragraphes de plus de 900. | Non tenu | § 4 |
| 5. Langue | 26 anglicismes hors code et hors glossaire (`owner`, `scope`, `polish`, `checkpoint`…), à côté de cinq termes de métier glosés (`run`, `skill`, `brief`, `build`, `craft`). | Presque tenu | § 5 |
| 6. Charge de procédure | Avant de lire son tronc, l'agent fait trois gestes ; deux suffisent. Le mainteneur n'a aucune marche à suivre pour ajouter une règle. | À réduire | § 6 |
| 7. Prêt à l'usage | Installation rejouée depuis une copie propre, pour Claude Code et Codex : les deux réussissent. Les commandes du README tournent dans la copie installée. L'exemple complet du guide 3 montre une trace complète, pas la trace légère que le système produit. | Presque tenu | § 7 |

---

## 2. Un lieu par sujet (F-06)

**Mesure.** Le guide 3 s'adresse à la personne qui pilote un travail. Ses sections 2, 3, 4, 6 et 9 redisent des règles qui ont déjà leur propriétaire. La section 1 répète le mode d'emploi du lecteur, qui est aussi dans la maintenance. Ces redites coûtent : 13 conditions de façade de la validation existent pour les garder alignées.

**Proposition.** Le guide 3 garde ce qui sert la personne, et renvoie aux règles par un lien. Les retraits, section par section :

| Section | Taille | Devient | Où vit ce qui part |
|---|---|---|---|
| Parcours commun, Où trouver la suite | 2,6 k | Gardée | — |
| 1. Lire juste ce qu'il faut | 5,0 k | Deux paragraphes : ce que fait le lecteur, et le lien vers ses commandes | `maintenance/README.md` (table des commandes), `DIRECTION/CHARGE` |
| 2. La ligne de run | 1,1 k | Une phrase et un lien | `DIRECTION/START` |
| 3. Le parcours complet | 4,5 k | La ligne « classer → diriger → construire → observer → choisir une suite → conserver », et un lien | `ACTION/RUN`, `ACTION/PIPELINE-DIRECTION` |
| 4. Choisir le mode | 2,3 k | Une phrase et un lien vers l'arbre | `DIRECTION/START/TREE` |
| 5. Charger seulement… | 0,5 k | Gardée | — |
| 6. Qualité positive dès le premier rendu | 3,1 k | Une phrase et un lien ; la table, copie du contrat du premier objet, part | `DIRECTION/FIRST-OBJECT` |
| 7. Une seule passe | 1,2 k | Gardée | — |
| 8. Confier à un agent | 2,1 k | Gardée : c'est le geste propre de ce public | — |
| 9. Exemple complet minimal | 2,8 k | Une trace légère réelle, contrôlée par `parcours.py trace`, et un lien vers les exemples | `references/examples.md` |
| 10. Observer, 11. Conserver, 12. Où sont les règles | 5,6 k | Gardées | — |

Le guide passe d'environ 32 k à environ 16 k. **Les conditions de façade qui gardaient une redite retirée sont retirées avec elle** ; je donnerai leur liste exacte dans le rapport. Les phrases propres au guide restent protégées.

Le glossaire (24 k, 89 termes) et le guide 2 restent : ce sont des tables d'orientation, gardées au lot 3.

## 3. Aucun reste : garder les ancres

**Mesure.** Aujourd'hui, aucun lien d'ancre n'est cassé et aucun titre n'est vide. Mais la validation ne contrôle que les fichiers, pas les ancres. Au lot 8a, un lien vers la section déplacée n'a été corrigé que parce que je l'avais cherché à la main.

**Proposition.** Une garde (ANC-01) : tout lien `fichier.md#ancre` vise un titre qui existe. Mutation rouge : une ancre inventée.

## 4. Lisibilité : seuils et découpe

**Mesure.**
- **14 cellules de plus de 500 caractères**, dont la plus longue fait 797 : README, glossaire, guide 2.
- **4 paragraphes de plus de 900 caractères** : le lancement créatif dans le guide 3 (1 572), deux capacités de la fiche de version (1 239 et 949), et le mode d'emploi des règles dans le README de la maintenance (968).

**Proposition.**
- **Seuils** `[À ADAPTER]` : 500 caractères par cellule et 900 par paragraphe, dans les textes pour les personnes (guides, README, notes de version, fiche de version, README des dossiers).
- **Découpe des 18 dépassements** : une cellule devient une phrase et un lien, ou passe sous la table ; un paragraphe devient une phrase d'ouverture et une liste. Le contenu ne change pas.
- **Garde LIS-01** sur ces seuils.

## 5. Langue

**Mesure.** Hors code et hors liens, les textes pour les personnes emploient :

| Termes | Occurrences | Proposition |
|---|---|---|
| `run`, `skill`, `brief`, `build`, `craft` | 47, 25, 15, 12, 22 | Gardés : termes du métier, tous définis au glossaire |
| `owner` 5, `scope` 4, `polish` 4, `checkpoint` 3, `gate`/`gates` 3, `token`/`tokens` 5, `rollback`, `fix`, `pattern`, `review`, `blast radius`, `workflow` (1 chacun) | 26 | Remplacés : responsable, périmètre, finition, point de contrôle, contrôle (ou « Gate A » quand c'est le nom), jeton de design, retour arrière, correctif, motif, revue, portée du changement, déroulé |

**Garde.** Deux listes closes, et le message dit « liste close » :
- les termes du métier admis, chacun présent au glossaire ;
- les anglicismes refusés dans les textes pour les personnes.

Les codes des règles ne changent pas.

## 6. Charge de procédure

**Mesure, agent.** Avant de lire son tronc, l'agent fait trois gestes :
1. ouvrir l'arbre et classer ;
2. lire la ligne de son mode (`--mode`) ;
3. écrire puis lire son tronc (`--tronc --fichier`).

Le tronc contient déjà la liste de ses routes, mais pas le reste de la ligne du mode.

**Proposition, agent.**
- `--tronc MODE --fichier` écrit aussi, en tête du fichier, la ligne du mode : ce qui se charge selon le signal.
- La « règle de vitesse » du noyau passe à deux gestes : classer, puis `--tronc`.
- Un geste de moins à chaque run. Coût au noyau : environ zéro ; la phrase change, elle ne s'allonge pas.

**Mesure, mainteneur.** Ajouter une règle demande de connaître six choses éparses :
- le titre à code ;
- le manifeste si le fichier est nouveau ;
- la balise de noyau et son registre si la règle doit arriver à chaque run ;
- le plancher si elle porte une obligation `[REQUIS]` ;
- les liens des guides ;
- la validation.

Rien ne les rassemble.

**Proposition, mainteneur.** Une section « Ajouter ou modifier une règle » dans `maintenance/README.md` : six étapes, chacune avec sa commande ou son fichier. Le retrait a déjà la sienne (lot 6).

## 7. Prêt à l'usage (F-13)

**Mesure.**
- **Installation.** `npx skills add` depuis une copie propre de l'archive GitHub, dans un projet vide, réussit pour Claude Code (`.claude/skills/`) et pour Codex (`.agents/skills/`).
- **Commandes du README.** Dans la copie installée, elles tournent : lecteur de routes, tronc, validations.
- **Une vérification impossible ici.** L'installation depuis le dépôt GitHub public dépend de ce qui y est publié.

**Proposition.**
- La phrase du README devient : « vérifiée le 18 novembre 2026 depuis une copie locale du paquet, pour Claude Code et Codex ».
- L'exemple complet du guide 3 devient une trace légère réelle (§ 2).

---

## 8. Vérification prévue

1. Branche `livraison-b`.
2. Tests :
   - les gardes ANC-01, LIS-01 et de langue, chacune avec sa mutation rouge ;
   - `--tronc --fichier` écrit la ligne du mode, et la règle de vitesse en tient compte ;
   - l'exemple du guide 3 passe `parcours.py trace`.
3. Planchers de trouvabilité tenus.
4. Taille des guides avant et après, et liste des conditions de façade retirées, dans le rapport.
5. Installation rejouée sur l'archive finale.
6. Validation complète avec navigateur, révision `R2026-11-15k`.

**Critère d'arrêt.** Si un passage du guide 3 que je retire n'a pas d'équivalent chez son propriétaire, je ne le retire pas : je vous le montre.

## 9. Ce qu'il faut me dire

« D'accord » suffit. Sinon, dites les sections du guide 3 à garder entières, et si vous voulez d'autres seuils de lisibilité.
