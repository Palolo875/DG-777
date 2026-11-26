# Lot 5 — Garanties vraies : rapport

15 novembre 2026. Révision livrée : `R2026-11-15d` (commit `b201929`, fusionné dans master en `795320d`). Document hors du paquet.

Les options A ont été appliquées partout. La validation complète avec navigateur passe. Les archives sont régénérées et l'archive GitHub est identique au commit, fichier par fichier.

## 1. Ce qui a changé

| Constat | Changement | Garde ou test |
|---|---|---|
| D-04 | Le résumé de la validation de structure dit désormais : « règles servies par une route, 13 obligations étiquetées avec leur plancher (noyau ou tronc) ; la lecture effective n'est pas contrôlée ». La description des gardes 19 et 20 dit la même chose. | Un test refuse le retour de « règles atteignables ». |
| D-05 | Deux gardes générales. **VOU-01** refuse « tu », « toi », « tes » et « t' » hors code, dans les guides et le README. **VAG-02** exige qu'une affirmation située dans le temps (« cette année », « de l'année », « en ce moment », « actuellement ») soit sur une ligne `[VEILLE AAAA-MM]`. Le périmètre de VAG-02 : règles, guides, références, README, SKILL. Les registres par phrases sont désormais dits « liste close » dans leurs messages. | Mutations rouges : les deux injections de l'audit sont refusées. Un cas vérifie que « factuellement » n'est pas pris pour « actuellement », un autre que le code est exempté. |
| E-07 | `DIRECTION/LECTURE-INSTRUMENTEE` cite le journal de mobilisation : c'est la base d'`ACTUAL-READ`, pas sa preuve, et une route servie n'est ni lue ni appliquée. La fiche du journal rappelle les quatre catégories. | Tests du journal : 18 cas passent. |
| D-15 | Le build copie ce que le manifeste liste, pour chaque distribution. Les 36 copies nommées une à une disparaissent. Pour ajouter un fichier, il suffit de l'ajouter au manifeste, et la maintenance le dit. | Build en copie temporaire : un fichier hors du manifeste n'entre pas dans les archives ; un fichier listé mais absent fait échouer le build. |
| E-14 | La validation d'ensemble lit `FIXTURE_TABLE` et passe les 26 fiches par la ligne de commande : 3 valides acceptées, 23 invalides refusées, chacune pour son motif. | Ligne `CLI FIXTURES PASSED` dans le journal. |
| E-02 / G-09 | Nouvelle commande `python3 scripts/parcours.py trace FICHIER`. Elle lit un fichier de trace ou l'en-tête du fichier livré. Elle **échoue** si l'une des six lignes nommées manque, est répétée ou n'est pas à sa place. Elle **signale** une ligne de plus de 600 caractères `[À ADAPTER]` et un geste seulement envisagé. Le bloc `TRACE` du noyau nomme la forme et la commande. `verifier` propose la commande quand une trace se trouve à côté de la page. | Sept cas : conforme, ligne manquante, ordre inversé, ligne trop longue, geste envisagé, trace introuvable, proposition par `verifier`. Une entrée au plancher du noyau (`CORE-01`). |
| D-17 | La validation d'ensemble lance son second build avec la variable `DG_BUILD_REPRODUCTIBILITE` : ce build saute les contrôles déjà passés et compare seulement les archives. Le contrôle des membres d'archive tourne toujours. | La reproductibilité est vérifiée comme avant, en comparant les empreintes. |

**Critère d'arrêt vérifié.** La commande `trace` accepte l'exemple de `references/examples.md` sans signal. Ce cas est le premier des tests.

## 2. Écarts par rapport aux propositions

1. **L'ancienne liste de tutoiements est gardée en complément.** La proposition disait que les gardes générales « remplacent » les listes. Mais un impératif de tutoiement sans pronom (« utilise le », « garde en tête ») échappe au contrôle du pronom. J'ai donc gardé l'ancienne liste pour le guide opérateur, sous le nom de liste close. C'est le seul reste ouvert de D-05, noté au registre. Si vous préférez la retirer, c'est une ligne.
2. **Le noyau prend 123 octets, au lieu des 110 annoncés.** La marge passe de 1 109 à 986 octets, pour 45 014 octets sur 46 000.
3. **Le gain de temps est plus faible qu'annoncé.**
   - J'avais estimé un tiers. La préparation complète a duré **11 min 32 s**.
   - J'ai mesuré séparément la part supprimée. Un build complet prend 174 s, un build de reproductibilité 1 s : le gain est d'environ **2 min 53 s par préparation**.
   - La préparation aurait donc pris environ 14 min 25 s sans ce changement. Le gain est d'environ 20 %, pas d'un tiers.
   - Le chiffre de départ de « 20 à 25 minutes » venait de préparations plus anciennes, sur une machine plus chargée. Je n'ai pas relancé l'ancienne préparation pour le mesurer : c'est une estimation, pas une mesure.

## 3. Vérification

| Contrôle | Résultat |
|---|---|
| Troncs des cinq modes | identiques, octet pour octet |
| Noyau | modifié seulement par la phrase d'E-02 ; budget passé |
| Recette de rendu | A 114, C 65, B 79 cas (navigateur) |
| Regard / parcours | 39 / 148 cas (navigateur) |
| Régressions d'audit | 125 cas, dont 9 nouveaux |
| Lecteur, journal, budget, préparation | 105, 18, 19, 10 cas |
| Déplacement, régressions de craft, rendu des supports | passés |
| Export Local, membres d'archive = manifeste, reproductibilité | passés |
| Archive GitHub comparée au commit | identique |

Empreintes :
- GitHub `0b6bc562…107b9c`
- Local `89903a2c…ffd9a`

Dans le dossier `R2026-11-15d` : les deux archives et le dépôt complet en bundle (toutes les branches).

## 4. Suite

Le prochain lot du plan est le **lot 6 — adoption des essais**. Il comprend B-19, F-12 et votre règle 6 (B-12), qui reste à trancher.

Le **lot 4 bis** (B-03, B-04, B-09 : savoir à écrire) attend toujours votre accord sur son principe.
