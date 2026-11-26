# Lot 8b — Les sept critères de livraison : rapport

18 novembre 2026. Révision livrée : `R2026-11-15k` (commit `a8a8c36`, fusion `c1fe44a` sur master). Document hors du paquet.

Les propositions ont été appliquées telles qu'approuvées, avec les options A partout. Trois points s'en écartent ; ils sont signalés en tête.

## À savoir d'abord

1. **ANC-01 existait déjà.** Ma mesure était fausse. `check_links` refuse déjà toute ancre introuvable (« fragment Markdown introuvable ») et des tests le couvrent. Je n'ai ajouté qu'un test : une ancre inventée vers un autre fichier est refusée, la vraie est admise.
2. **LIS-01 mesure le texte visible.** Le seuil s'applique à ce que la personne lit, cibles de liens et commentaires HTML exclus. Avec cette mesure, il y avait 10 dépassements au lieu de 17. **À confirmer** si vous préférez compter les caractères bruts.
3. **Guide 3 : 19 604 caractères au lieu des 16 000 prévus.** Les sections 8, 10, 11 et 12 sont gardées entières, comme prévu. L'écart vient de ces sections, plus longues que je ne l'avais estimé.

## Ce qui a été fait

| Critère | Fait | Contrôle |
|---|---|---|
| 2. Un lieu par sujet | Guide 3 : de 32 980 à 19 604 caractères (−41 %). Les sections 1, 2, 3, 4, 6 et 9 renvoient à leurs propriétaires. Les commandes périmées de la section 3 sont corrigées. | Conditions de façade retirées (liste ci-dessous) |
| 3. Aucun reste | La garde d'ancres existait déjà (voir plus haut) ; un test croisé est ajouté. | `test_invented_anchor_in_other_file_refused` |
| 4. Lisibilité | **LIS-01** : au plus 500 signes visibles par cellule et 900 par paragraphe, seuils `[À ADAPTER]`. Dix découpes : glossaire (2), `versions.md` (2 capacités mises en liste), README de maintenance (1 paragraphe, 2 lignes de table), README des scripts (3). | Mutation rouge : cellule de 501, paragraphe de 901 ; un long lien ne compte pas |
| 5. Langue | **LAN-01**, avec deux listes closes. Les mots gardés (run, skill, brief, build, craft) ont chacun leur ligne au glossaire, et Skill, Brief et Build y sont ajoutés. Les mots remplacés sont owner, scope, polish, checkpoint, gate, token, rollback, fix, pattern, review, blast radius et workflow. | Mutations rouges : trois mots injectés, et la ligne « Skill » retirée |
| 6. Charge de procédure | La « règle de vitesse » du noyau passe à deux gestes : classer, puis `--tronc MODE --fichier tronc.txt`. Le fichier commence par la ligne du mode (de 0,4 k à 2,6 k selon le mode). La maintenance gagne une section « Ajouter ou modifier une règle » en six étapes. | Mutation rouge : sans la ligne du mode, le test échoue |
| 7. Prêt à l'usage | L'exemple du guide 3 est une trace légère, contrôlée par `parcours.py trace`. Le README date l'installation au 18 novembre 2026. | Test P65 du parcours |

Pour LAN-01, trois cas restent hors garde :

- les en-têtes du glossaire, qui donnent le terme anglais entre parenthèses, comme « Responsable (owner) » ;
- les noms Gate A, B et C ;
- les noms de fichiers, comme `owner.txt`.

Le glossaire renomme deux entrées : « Polish » devient « Finition (polish) » et « Gate » devient « Contrôle (Gate A, B, C) ».

## Conditions de façade retirées ou ajustées

**Retirées avec les redites du guide 3 :**

- LCF-04, LCF-05 et LCF-10 sont fusionnées en une seule LCF-04 : le README n'a pas de table de mode, et le guide renvoie à l'arbre `DIRECTION/START/TREE` ;
- LCF-15, LCF-30 et LCF-42 sont retirées ;
- LCF-43, 44, 45 et 55 perdent leur exigence sur le guide 3, mais gardent leurs autres sources.

**Traduites en même temps que les textes, sans relâcher la garde :**

- LCF-03 : « contrôle » au lieu de « gate », « retour arrière » au lieu de « rollback » ;
- LCF-12 : « responsable » au lieu de « owner » ;
- FAC-01 : « point de contrôle » au lieu de « checkpoint ».

## Validation

La préparation complète avec navigateur a réussi :

| Suite | Résultat |
|---|---|
| Recette | A 119, C 65, B 81 |
| Regard | 39 |
| Parcours | 153 |
| Audit | 155 |
| read_route | 106 |
| Journal | 18 |
| Budget | 19 |
| Préparation | 10 |
| Supports, export Local, reproductibilité | réussis |

Autres contrôles :

- **Noyau :** 45 250 octets sur 46 000.
- **Archive GitHub :** identique au commit, 151 fichiers et aucun écart.
- **Installation rejouée sur l'archive finale :** pour Claude Code et pour Codex, l'installation réussit, et `--tronc --fichier`, `--mode`, la lecture d'une route et la validation tournent dans la copie installée.

**Empreintes SHA256 :**

- GITHUB : `5d670f95…7188b06be92a`
- LOCAL : `c5f57e0b…ba7a6bef23e`

## Suite

Le lot 9, le run de contrôle, est prêt à ouvrir. Le plan et le registre sont à jour.
