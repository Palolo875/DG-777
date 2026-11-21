# Lot 3 — Une seule voix : rapport

15 novembre 2026. Révision de départ : `R2026-11-15a`. Révision livrée : `R2026-11-15b`. Document hors du paquet.

Décision appliquée : « Allons-y », c'est-à-dire les corrections du § 2 et l'option A partout.

## 1. Le sort de chaque constat

| Constat | Sort | Ce qui a changé |
|---|---|---|
| A-02 | Corrigé | `DIRECTION/CADRES` gagne une colonne « Déclaration » : `VISION`, `ASSET`. Elle gagne aussi cinq lignes pour ce que seule la déclaration porte : registre, niveau, composants et finition, mouvement, mobile. Une phrase dit que la déclaration est la vue écrite à chaque run où la décision visuelle est ouverte, et que les autres vues gardent leurs propres règles de moment et de niveau de trace. |
| A-03, B-10 | Corrigé | La taxonomie de `SAVOIR/STYLE` relie chaque dimension du registre aux axes de `CFT-02`. `DIRECTION/DIVERGENCE` dit lequel sert à quoi : le registre pour diverger, `CFT-02` pour une alternative située, la tension pour la structure. `CFT-02` cite les dimensions du registre parmi ce qui y renvoie. La liste partielle de `DIVERGENCE` est présentée comme exemples (« notamment »). |
| A-12 | Corrigé | `SAVOIR/READ` : « au-delà du tronc de ton mode, charge typiquement zéro à deux routes de SAVOIR ». Une phrase restante sur les « anciens identifiants de section » est retirée. |
| B-05 | Corrigé | La table « Rattachement des grilles » gagne la colonne « Revue sur capture », et ses quatre questions y sont rattachées. Une phrase situe le jugement visuel situé et le premium perçu. Gate C s'ouvre sur sa portée : obligatoire en DIRECTION en trace complète, sans verdict en trace légère. |
| B-07 | Corrigé | L'atlas devient le seul vocabulaire des rôles d'asset. Chaque ligne de « Routes par rôle » nomme le rôle de l'atlas qu'elle sert. Une phrase traite l'orientation, le média temporel et le modèle spatial : leur route se décide selon le médium. La liste de six rôles est retirée. |
| B-11 | Corrigé | Une phrase, sous l'ordre de décision de `SAVOIR/FRAME`, situe les cinq ordres. `RUN-PRIORITY` et `P0–P3` y renvoient. |
| D-03 | Corrigé (A) | Le principe est écrit dans `ACTION/ROUTING` : une table qui renvoie d'un critère à sa route est un renvoi local, lu pendant la route. La garde SIG-01 reconnaît ces tables et exige qu'elles soient déclarées avec leur raison. Les trois tables actuelles le sont : critères de Gate C, vocabulaire de `SAVOIR/STATE`, familles de l'atlas. |
| A-15, D-12 | Corrigé (A) | Les 31 blocs différés portent la balise `différé`, et les 35 blocs compilés gardent `noyau`. `build_core.py` refuse une balise contraire à son registre. |
| D-06 | Déjà corrigé | Lot 1. |
| E-05 (table) | Corrigé (A) | La table des conditions de départ est retirée. Deux renvois la remplacent : ce qu'un mode charge, `DIRECTION/CHARGE` ; ce qu'il établit et livre en trace complète, `ACTION/CLOSE-PACKAGE`. La règle HON-06 reste. |
| F-05 | Écarté, avec raison (A) | La ligne « SUJET » de `--trouver` reste, parce qu'elle fait monter le propriétaire du sujet sur les termes larges. `DIRECTION/CHARGE` dit désormais qu'elle n'ajoute aucune lecture au-delà de la règle de `SAVOIR/READ`. |

## 2. Une précision par rapport aux propositions

J'avais écrit que les dimensions du registre « regroupent sept » axes de `CFT-02`. En construisant la table, j'ai compté autrement : les sept dimensions regroupent **dix** des douze axes. Seuls « Contraste » et « Convention ↔ écart » n'y entrent pas. Le texte livré donne le bon compte.

## 3. Les gardes ajoutées

| Garde | Ce qu'elle refuse | Tests |
|---|---|---|
| SIG-01, élargie | Une table de renvoi vers des routes non déclarée, ou une déclaration sans table | 2 mutations rouges |
| REG-01 (nouvelle) | Une dimension du registre nommée au noyau sans sa ligne dans `SAVOIR/STYLE`, ou reliée à un axe inconnu de `CFT-02` | 2 mutations rouges |
| Balise et registre (`build_core.py`) | Un bloc compilé marqué « différé », ou l'inverse | 2 cas |

## 4. Ce qui a été vérifié

| Contrôle | Résultat |
|---|---|
| Noyau compilé, et `SKILL.md` entier | **Identiques, octet par octet** (44 027 / 46 000) |
| Troncs des cinq modes | **Identiques** ; DIRECTION reste à 34 515 / 35 000 |
| Sorties du lecteur | 182 sur 220 identiques. Les 38 autres correspondent toutes aux corrections du § 1, auxquelles s'ajoutent des numéros de ligne dans quatre connexions. |
| Trouvabilité | 18/30 et 10/15, inchangés |
| Tests | Lecteur 105, régressions d'audit 112, budget 19, préparation 10, journal 18 |
| Validation complète avec navigateur, archives | Passe (`preparer_livraison.py --require-browser`, code 0) : recette 79 cas navigateur, regard 39, parcours 141, cartes du système, build reproductible, export Local validé seul, test de déplacement et régressions de craft. |

## 5. Livraison

- Dépôt : commit `e403236` sur la branche `voix`, fusionné dans `master`. Le contenu de l'archive GitHub est identique à ce commit.
- Dossier `R2026-11-15b/` : archives GitHub (sha256 `7735d299…`) et Local (sha256 `11cd6614…`), et le dépôt (`design-governance-depot.bundle`).
- **Un incident pendant la validation, corrigé.** Une régression de craft fait de `SAVOIR/STATE` le mauvais propriétaire dans `CFT-00` et attend que la garde le voie. Elle ne remplaçait qu'un des deux renvois ; la phrase ajoutée pour B-05 en crée un second. La garde restait donc satisfaite par ce second renvoi, et la mutation ne la faisait plus tomber. Elle remplace maintenant les deux renvois, et la garde tombe comme attendu.
- **Bruit connu, toujours laissé au lot 7.**

## 6. La suite

Le lot 4 : ce qui doit arriver à l'agent. Il commence par la carte des déclencheurs, puis traite l'acheminement du savoir, le noyau et le tronc. C'est là que se décident A-01 (le Creative Boot et la cible deviennent-ils des vues de trace complète ?) et l'arrivée au noyau des critères de Gate C (B-05). Ce lot change ce que l'agent lit ; chaque proposition y aura sa mesure de budget.
