# Lot 6 — Adoption des essais : rapport

15 novembre 2026. Révision livrée : `R2026-11-15e` (commit `37c947e`, fusionné dans master en `0a34072`). Document hors du paquet.

Les options A ont été appliquées partout. La validation complète avec navigateur passe. Les archives sont régénérées, et l'archive GitHub est identique au commit, fichier par fichier.

## 1. Ce qui a changé

| Sujet | Changement | Garde |
|---|---|---|
| **Socle** (F-02, H-03) | La section « Sections à l'essai » quitte la fiche de version. Les 30 sections prennent le statut `SEED`, redéfini : « route du socle de la V1 (seed d'origine et sections versées au socle), canonique, sans gain mesuré ». La fiche de version gagne une courte section « Socle de la V1 ». | — |
| **Retrait** (garde-fou 2) | La nouvelle section « Retirer une section du socle » (`maintenance/evolution.md`) contient une procédure commune en quatre étapes, puis une ligne par section : section, ce qu'elle apporte et sa limite, retrait. Chaque retrait a été revérifié contre le paquet actuel. | **SOC-01** : chaque ligne est complète ; ses routes, blocs du noyau et fichiers existent ; aucun récit de run. |
| **Essais futurs** (F-02) | Une nouvelle route entre en `PILOT`, avec au plus cinq essais ouverts à la fois `[À ADAPTER]`. Ils sont listés dans une section « Sections à l'essai » qui n'existe que tant qu'une route l'est. | **SOC-02** : au plus cinq essais ouverts, et pas de section vide. |
| **Statut d'essai dans le savoir** (B-19) | Les six mentions sortent du savoir : `PILOT`, `ADOPTED`, et « à revoir avant 2027-04 » quand il ne s'agissait pas d'une veille. « À l'essai » sort aussi du README, des notes de version, des guides, de la maintenance, du README des scripts et de l'en-tête de `regard.py`. | **SOC-03** : le statut d'essai ne se dit que dans la fiche de version et le cycle de vie. |
| **Récits de runs** (F-04, B-13), règle 3 | Ce qui sort : les 30 lignes et leurs récits ; les quatre puces d'état de la preuve ; les comptes de runs des marqueurs de vague ; la mesure des pages d'agents ; la section des anciens alias et sa garde. Les marqueurs et convergences restent, dits au présent, avec leur date et leur source. | — |
| **Règle 6** (B-12) | Ce qui sort : Tuch et al. (aussi au noyau), Norman, Ottosson, Itten, le cas Amazon/FTC et les quatre titres de presse. Ce qui reste : WCAG, AI Act, OKLab et les ressources. Les signaux de veille disent « presse design et veilles de tendances, 12-2025 à 06-2026 ». | **PRO-01** : aucune citation « (Auteur, année) » ni « et al. » hors d'une ligne `[VEILLE]`. |
| **Identifiants** (D-10) | Remplacés par leur raison, ou retirés, dans dix scripts :<br>• identifiants d'audit : `RET-1` à `RET-6`, les `INV-…`, `F-DIR-005`, `C6`, `C8 O-1` à `O-4`, `E1 O-1`, « règle A2 », « migration (12.04) », `R-6`, la colonne « constat » de `ROW_NEEDLES` ;<br>• renvois de mes propres lots : « lot 2, A-07 », « lot 4, B-02 »…, et les noms des classes de test par lot. | — |
| **F-12** | Les preuves « plusieurs personnes » sont sorties avec la colonne « preuve attendue ». | — |
| **Recette de maintenance** | « Une modification substantielle est exercée sur un run réel avant adoption élargie » devient « Une nouvelle route est exercée sur un run réel avant de quitter `PILOT` ». « Statut d'adoption » devient « statut de cycle de vie ». | — |

Rien n'est perdu : tout ce qui est sorti se trouve, verbatim, dans `Suivi_contenu_sorti_lot_6.md`. Les 30 lignes avant et après sont dans `Lot_6_annexe_avant_apres.md`.

## 2. Écarts et points à relire

1. **Correction de ma proposition.** J'avais proposé pour l'identité de marque « elle n'a pas encore servi sur un run ». C'est faux : la fiche notait un run d'agent qui l'avait parcourue. J'ai écrit « elle est moins éprouvée que le Web », dans la fiche, le README et les notes.
2. **Une limite de coût gardée.** À l'efficacité `NOT-VERIFIED`, j'ai ajouté une phrase au présent : « Un run avec le système coûte plus de jetons et de temps qu'un run sans lui. » Le chiffre (1,7 fois) est parti au suivi. Si vous la jugez de trop, c'est une phrase à retirer.
3. **Le cas Amazon** devient : « ces motifs sont sanctionnés par les autorités de protection des consommateurs ; les sanctions connues atteignent le milliard de dollars [VEILLE 2026-10] ». C'est l'ordre de grandeur, sans le nom.
4. **Ce qu'apporte chaque section** est parfois résumé plus court qu'avant, par exemple pour le parcours par défaut. Le détail reste dans la section elle-même et dans la maintenance. L'annexe montre chaque ligne, avant et après.
5. **Retraits périmés corrigés** :
   - « son adresse lisible » (écriture, identité) : ces adresses n'existent plus ;
   - « six appels » du journal : il y en a cinq, désormais nommés ;
   - « ligne de convergence datée du 29-10-2026 » : cette ligne n'existe plus ;
   - le retrait de la voix typographique nomme maintenant son bloc du noyau (`COMP-CONVERGENCE`).
6. **Hors périmètre annoncé, mais pour la même règle 3** : j'ai aussi retiré les renvois à mes propres lots, que j'avais laissés dans les scripts et dans les noms des classes de test.

## 3. Vérification

| Contrôle | Résultat |
|---|---|
| Troncs des cinq modes | identiques, octet pour octet |
| Noyau | −20 octets (Tuch) : 44 994 sur 46 000, marge de 1 006 |
| Fiche de version et cycle de vie | 53,7 k → 39,7 k |
| Recette de rendu | A 114, C 65, B 79 cas (navigateur) |
| Regard / parcours | 39 / 148 cas |
| Régressions d'audit | 134 cas, dont 9 nouveaux : mutations rouges des quatre gardes (récit de run, route inexistante, sixième essai, section vide, statut d'essai dans le savoir, « (Tuch et al., 2012) ») et acceptation d'une citation sur une ligne `[VEILLE]` |
| Lecteur, journal, budget, préparation | 105, 18, 19, 10 cas |
| Fiches par la ligne de commande | 26 sur 26 |
| Déplacement, régressions de craft, rendu des supports, export Local, reproductibilité | passés |
| Archive GitHub comparée au commit | identique |
| Durée de préparation | 11 min 41 s |

Empreintes :
- GitHub `fab5e2cd…36e0b9`
- Local `4f4d20f2…7f3e0a`

## 4. Suite

Le prochain lot du plan est le **lot 7 — poids et coût** : budgets, sorties d'outils, export, et le bruit de la préparation noté depuis le lot S.

Le **lot 4 bis** (savoir à écrire : B-03, B-04, B-09) attend toujours votre accord sur son principe. Il peut maintenant s'écrire directement dans le socle.
