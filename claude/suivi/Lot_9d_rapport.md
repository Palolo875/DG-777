# Lot 9d — Rapport

- **Révision** : `R2026-11-15n`.
- **Branche** : `lot-9d`, fusionnée dans `master` avec `--no-ff`.
- **Décision** : « Oui » au document de propositions (`Lot_9d_Propositions.md`). Les options A s'appliquent partout.
- **Runs** : aucun.

## 1. Ce qui est intégré

| Proposition | Ce qui change | Gardes |
|---|---|---|
| **P1** Fontshare dans `polices` (E-2) | Nouvelle source **Fontshare** (`api.fontshare.com`), essayée après Fontsource et Google Fonts, ou seule avec `--source fontshare`.<br>• L'italique se demande par la graisse + 1, et l'outil récupère des WOFF2 complets, sans sous-ensemble.<br>• La licence de chaque famille est rapportée. Pour la licence FFL : « ni modification, ni sous-ensemble, ni conversion de format, ni redistribution ».<br>• `--catalogue` liste les 100 familles par catégorie.<br>• Les mentions sont ajoutées dans `MOYENS`, `TYPE-VOIX`, `scripts/README.md`, l'évolution et la fiche de version.<br>• Essai réel depuis l'environnement : le catalogue est lu et Gambetta est téléchargée (normal et italique). | P38 à P41, tous hors réseau |
| **P2** Vague typographique (E-2) | Dans la ligne datée de `SAVOIR/TOOLS/CONVERGENCE`, désormais `[VEILLE 2026-11]` :<br>• « Vague 4 : police d'affichage de gabarit en titre » ;<br>• la liste Fraunces, Instrument Serif, Young Serif, Playfair Display, Bricolage Grotesque, Space Grotesk, Space Mono, avec le rappel « un candidat modal à nommer comme tel, pas un interdit » ;<br>• la source précisée : articles, détecteur de pages Show HN, relevé de galeries, 11-2026.<br>`read_route.marqueurs_de_vague` lit la liste, et `regard.py` relève la police réellement en tête de pile. Le marqueur est protégé par VAG-01. | 2 cas de `test_regard.py`, plus les gardes existantes de la liste |
| **P3** Écriture (E-1) | `SAVOIR/CRAFT/CFT-06` : « La page ne commente pas son design ». C'est un signal d'enquête : la raison va dans la trace, le marquage demandé reste, et une note d'auteur voulue est un contenu. | P23 |
| **P4** Calibration (B-5) | Bloc `ANCRE` du noyau : « Sur une surface dont la décision visuelle est ouverte » (« `DIRECTION` » retiré). | P24 |
| **B-4** | Clos sans changement : le constat n'a pas été reproduit au PILOT. | — |

**Noyau** : 45 805 octets sur 46 000, soit 12 de moins qu'au lot 9c.

## 2. Mutations rouges

Les 9 mutations rouges échouent chacune avec un échec nommé, sans plantage :
- italique non converti ;
- Fontshare retiré du repli ;
- licence FFL non rapportée ;
- phrase des polices retirée ;
- détecteur rendu muet (lancé à la main, parce que mon remplacement automatique ne trouvait pas le texte) ;
- vague 4 retirée de la liste ;
- signal d'écriture retiré ;
- calibration remise à `DIRECTION` (noyau recompilé, puis restauré).

## 3. Préparation et livraison

À compléter.

## 4. Ce que ce lot ne prouve pas

- Que les agents choisiront d'autres polices. L'outil élargit le vivier, et la vague nomme la modale. Seul un run le dira.
- **Le catalogue de Fontshare contient lui-même Space Grotesk, une police de la vague.** Le relevé de `regard` la nommera si elle est retenue.
- **La licence FFL** permet l'auto-hébergement pour son propre site, mais interdit de fournir la police à un tiers. Une page livrée à un client avec une police FFL intégrée demande que le client prenne sa propre licence, qui est gratuite, sur Fontshare. La ligne de licence rapportée le dit (« ni redistribution »).
