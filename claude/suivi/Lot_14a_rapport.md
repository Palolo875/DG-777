# Lot 14a — Rapport : voir

- **Révision** : `R2026-11-15z`, livrée le 25 novembre 2026. La version publique reste **V1.1.1** pendant 14a à 14c ; la **V1.2.0** sera publiée à la fin du lot 14, avec un seul journal des changements.
- **Branche** : `lot-14a`.
- **Décision** : « D'accord, on lance. » sur `Lot_14_Propositions.md` : options A partout ; 14a d'abord.
- **Runs** : aucun.

## 1. Ce qui change

| Proposition | Changement |
|---|---|
| **V1** Comparer à l'esquisse retenue | `parcours.py captures PAGE --version vN --contre ESQUISSE.html` : l'esquisse retenue en première rangée, la version dessous, au même cadrage, aux mêmes largeurs, en une seule image. Refusé sans `--version`, avec `--pleine` ou `--separees`, ou si l'esquisse manque. La fiche de `verifier` le rappelle. |
| **V2** Lecture sans le texte sur mobile | `regard.py` la produisait déjà à chaque largeur ; la fiche de `verifier` ne faisait regarder d'abord que le bureau. Elle fait maintenant lire **aussi le haut de l'image sans texte à 390 px** : « l'idée survit-elle à la recomposition ? Sinon, c'est la version mobile qui se reprend, pas l'idée. » |
| **V3** Le retrait protège l'idée | Test de retrait : « ce qui ne manque pas part, **sauf l'élément qui porte l'idée** (le « grâce à quoi » de la ligne `VISION`) : il ne se retire pas, et s'il manque à la lecture sans le texte, il revient. » |
| Ligne d'atelier au noyau | Lecture sans le texte au bureau et au premier écran mobile ; test de retrait qui protège l'élément porteur ; chaque version jugée contre l'esquisse retenue. Trois formulations protégées par CORE-01. |
| Route `ACTION/ATELIER-EDITION` | Les trois règles, en entier. |
| Référence générée | Régénérée (l'aide de `captures` gagne `--contre`), garde DOC-03. |

Noyau : 31 127 → 31 358 octets (sur 31 500).

**Choix fait en route** : l'élément porteur n'a pas de ligne nouvelle dans la déclaration ; c'est le « grâce à quoi » que la ligne `VISION` demande déjà. Rien n'est ajouté à la forme de la trace.

## 2. Tests et mutations rouges

4 cas dans `test_parcours.py` (180 cas en tout, navigateur compris) :
- planche contre l'esquisse, sans navigateur : esquisse en première rangée, hauteur doublée ;
- fiche de `verifier` : la lecture sans texte à 390 px est dans la consigne « D'abord » quand une largeur mobile est demandée, et absente sinon ;
- avec navigateur : `captures --version v2 --contre` produit une seule image, deux rangées ;
- options refusées : `--contre` sans `--version`, esquisse introuvable.

| Mutation | Résultat |
|---|---|
| La planche ignore l'esquisse | Rouge : P19 (sans navigateur) et P138 (navigateur) |
| `captures` ne transmet pas l'esquisse | Rouge : P138 |
| La consigne mobile disparaît de la fiche | Rouge : P20 |
| Phrases du noyau retirées | CORE-01 (même mécanisme que 13a) |

## 3. Préparation et livraison

À compléter.

## 4. Ce que ce sous-lot ne prouve pas

- Que l'agent comparera vraiment ses versions à l'esquisse, ni qu'il gardera l'élément porteur : seul un run le dira.
