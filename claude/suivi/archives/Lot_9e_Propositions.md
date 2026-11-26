# Lot 9e — Propositions (clôture du lot 9)

Rédigé le 20 novembre 2026. Base : `R2026-11-15n` (`master` `7446fdc`). Aucun run.

Règle 1 : rien n'est intégré sans décision. « D'accord » vaut pour les options A partout.

## 0. Relecture de tous les constats restants (règle 4)

Les preuves viennent du paquet et des quatre runs du PILOT (17k, 17l, 18k, 18l).

| Constat | État | Preuve |
|---|---|---|
| **A-1** Gadget : un plan vu de dessus comme image | **Traité par le lot 9b, non reproduit.** Au PILOT, sur l'invitation, aucun agent n'a pris de diagramme ; 17k a même écarté sa piste « Défournement » parce qu'elle « se lisait diagramme ». | Traces 17k et 17l |
| **A-3** Le diagramme comme objet principal | **Traité par le lot 9b** (signal de SELECT, servi par `verifier`). Sur le widget, la courbe est légitime : elle porte la tâche. | Lot 9b, P2 ; traces 18k et 18l |
| **A-2** Générique sous le premier écran | **Pas relevé par Junior au PILOT** : ses raisons portent sur la structure, la lisibilité et les cas limites, en faveur des rendus `l`. Les outils existent : la séquence (`BIBLIOTHEQUE/SEQUENCE`) et le geste « Partie ordinaire » servi par `verifier`. **Je propose de le clore, et de le suivre au carnet de goût.** | `Carnet_de_gout.md` |
| **A-4** Les briefs qui vivent de l'image plafonnent | **Limite assumée de la série** : génération d'images interdite. La piste « accord pour la génération quand personne n'est là » reste une décision de Junior, hors de ce lot. | Règles de la série |
| **B-1** Références pas au niveau visé | **Encore partiel.** Pour le widget, les références sont des sites de données (maree.info, SHOM) et des photos ; aucune n'est un widget ou une app de marées de haut niveau. Ces sites calibrent le contenu, pas le niveau. | `refs.md` de 18k et 18l |
| **B-2** Le niveau visé n'est défini nulle part | **Déjà corrigé en partie** : la ligne `NIVEAU` de la déclaration de direction en fait un test vérifiable sur capture (depuis `R2026-11-11b`). **Reste** : la calibration (`ANCRE`) parle du « niveau de finition visé » sans renvoyer à cette ligne. | `DIR-DECLARATION` ; bloc `ANCRE` |
| **B-3** Le jugement des références n'est pas écrit | **Confirmé dans les 4 runs du PILOT.** Les lignes « Change : … ; ne se transfère pas : … » que `parcours.py references` écrit dans `refs.md` restent **vides** : 10 dans 17k, 3 dans 17l, 4 dans 18k et 5 dans 18l. Rien ne le signale. | `refs.md` des quatre runs |
| **B-6** Références non transformées | **Non reproduit.** 17k a tiré l'émail d'un bol réel (AIC) ; 18k et 18l ont tiré leurs chiffres serrés de l'annuaire des marées. | Traces |
| **C-3** Lignes de trace trop longues | **Non reproduit** (déjà noté au lot 9). | — |
| **C-4** Réserves non nommées | **Non reproduit** : aucune trace du PILOT n'annonce de réserve sans la nommer. | Traces du PILOT |
| **D-1** Paramètres du run 9 non consignés | **Corrigé** : le registre des runs les consigne depuis le run 10. | `Registre_des_runs.md` |
| **E-3** Palette non justifiée | **Non reproduit.** Les quatre palettes sont justifiées dans les traces : céladon de l'émail, papier contre bleu nuit, feux de port. | Traces |
| **E-4** Accent incohérent | **Non reproduit.** Le rouge porte une seule information : la limite, ou le seuil fermé. Le geste « Accent » de `verifier` existe. | Captures et traces 18k, 18l |

## 1. Propositions

### P1 — Signaler les références sans jugement (B-3)

- **A (recommandée).** `parcours.py verifier` cherche les `refs.md` écrits par `references` à côté de la page : dans le dossier de `--refs`, ou à défaut dans le dossier de la page et son parent, sur trois niveaux au plus, sans le dossier de la skill. Il compte les lignes « Change : … ; ne se transfère pas : … » restées vides et ajoute un signal : « N références sans jugement : pour chacune, ce qu'elle change dans le build et ce qui ne se transfère pas (bloc `ANCRE`). » C'est un signal, pas un échec. Test avec mutation rouge.
- **B.** Seulement un rappel à la fin de la sortie de `references`.

### P2 — Une référence de niveau vient d'une source éditée (B-1, B-2)

- **A (recommandée).**
  - Dans `SAVOIR/TOOLS/MOYENS`, « Références à observer » : « Pour calibrer le niveau, une référence au moins est du même type d'objet et vient d'une source éditée (galerie de sites, prix, collection, fonderie, Fonts In Use) ; un site d'information du sujet calibre le contenu, pas le niveau. »
  - Dans le bloc `ANCRE` du noyau, « au niveau de finition visé » devient « au niveau visé (ligne `NIVEAU`) ». Coût : environ 10 octets.
  - Tests de présence, avec mutation rouge.
- **B.** Seulement la phrase dans `MOYENS`.

### Clôtures sans changement

**A-1, A-2, A-3, A-4, B-6, C-3, C-4, D-1, E-3 et E-4**, pour les raisons de la section 0. A-2 reste suivi au carnet de goût, et A-4 reste une décision de Junior.

## 2. Ordre proposé

1. Décision de Junior.
2. Intégration, tests avec mutation rouge, préparation complète, puis révision `R2026-11-15o`.
3. Clôture du lot 9 dans le plan et le registre. Aucun run.
