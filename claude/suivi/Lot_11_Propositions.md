# Lot 11 — Propositions : le noyau-index

Rédigé le 21 novembre 2026. Base : `R2026-11-15q` (`master` `dbcfd7f`). Aucun run (décision de Junior).

Règle 1 : rien n'est intégré sans décision. « D'accord » vaut pour les options A partout.

## 0. Mesure (révision `q`)

| Mesure | Valeur |
|---|---|
| Noyau | 45 876 octets (plafond 46 000), 36 blocs, 6 962 mots |
| Obligations `[REQUIS]` | 13 : 11 tenues par un bloc du noyau, 2 par un tronc |
| Index déjà présent au noyau | La table `CHARGE-DETAILS` : 27 lignes « signal → route », 5 076 octets |
| Routes couvertes par cet index | **34 sur 85** |
| Routes citées nulle part au noyau | **40 sur 85**, dont `DIRECTION/DIVERGENCE`, `ACTION/GATE-B`, `BIBLIOTHEQUE/SECTIONS`… |
| Répartition du noyau (cartographie) | Procédure de direction 49 % ; chargement et réponse 23 % ; goût 13 % ; atelier 9 % ; gouvernance 5 % |

**Fait décisif.** Les blocs du noyau sont des **copies compilées** du texte des routes (`noyau:début` et `noyau:fin` dans les fichiers de `design/`, `agent/`, `gouvernance/`). Retirer un bloc du noyau **ne supprime aucun savoir** : son texte reste dans sa route, servi par `read_route`.

## 1. Le principe

Le noyau garde, toujours visibles :
1. **Les invariants** : rôle, absolus, données d'exemple, vérité, sortie, trace. Ils sont réécrits courts.
2. **Chaque obligation `[REQUIS]`**, en **une ligne** : quand elle s'applique, ce qu'elle exige, et la route où est son détail. Les 13 restent toujours lues.
3. **La boucle**, avec ses commandes (`chantier`, `leviers`, `captures --version`, `verifier`, `trace`).
4. **Un index complet et compressé des 85 routes** : « signal → route », avec la consigne de consulter la route plutôt que sa mémoire.
5. **Un court passage « Sans outils »** pour un agent sans exécution (profil E2) : ce qui reste obligatoire, et comment dire ce qui n'a pas été vu.

Le détail de la procédure n'est plus copié au noyau. Il reste dans les routes, lu au moment voulu.

**Appui.** Vercel (janvier 2026) a mesuré 100 % de réussite avec un index compressé toujours présent, contre 53 % pour une skill à la demande. C'est du code, pas du goût. **Sans run, l'effet sur les rendus ne sera pas mesuré** : il le sera au lot 13.

**Changement par rapport au plan de travail.** Le plan prévoyait des commandes nouvelles (`diverger`, `declarer`, `atelier`, `livrer`) pour porter la procédure. Avec le noyau-index, **les obligations restent visibles au noyau**, et leur détail est déjà dans les routes. Ces commandes ne sont donc **plus nécessaires** pour ce lot : on évite d'ajouter du code et de rendre une règle dépendante d'un outil. Elles pourront venir plus tard, si un run montre qu'elles aident.

## 2. Les sous-lots

### 11a — Garde des obligations en une ligne (aucun contenu ne bouge)

- **A (recommandée).** La garde des planchers (`PLANCHERS`, `validate_structure.py`) accepte une nouvelle forme : **« ligne d'invariant au noyau, plus détail dans la route »**.
  - Le test vérifie que la ligne porte l'étiquette `[REQUIS — portée]`, nomme la route, et que la route existe et contient le texte complet de l'obligation.
  - Les formes actuelles (bloc complet au noyau, ou tronc) restent valides.
  - Mutation rouge sur chaque forme.
- **B.** Garder seulement la forme « bloc complet ». Le noyau ne pourra alors pas descendre sous environ 35 k.

### 11b — Index complet et compressé

- **A (recommandée).**
  - `CHARGE-DETAILS` devient un index de **toutes** les routes : une ligne par signal, des routes groupées, au format compact (`signal → ROUTE, ROUTE`).
  - En tête, la consigne : « consulte la route plutôt que ta mémoire ; `read_route.py CODE` ».
  - **Garde** : chaque route du sommaire de `read_route` figure dans l'index (mutation rouge).
  - **Cible** : 85 routes sur 85, en 8 000 octets au plus (5 076 aujourd'hui pour 34 routes).
- **B.** Compléter l'index sans le compresser : environ 12 000 octets.

### 11c — Les blocs de procédure deviennent des lignes d'invariant

- **A (recommandée).** Pour chaque bloc de procédure, le marquage `noyau` est retiré : le texte reste dans sa route, et une ligne d'invariant le remplace au noyau.
  - Blocs concernés : `DIR-LEVIERS` (4 973 o), `DIR-DECLARATION` (2 897), `MOY-PLAFOND` (3 444), `BOUCLE-ATELIER` (3 904), `ANCRE` (2 078), `STRUCT-TRAME`, `COMP-*`, `BOUCLE-CAPTURE`, `VER-SCENE`, `VER-AUDIENCE`, `REGISTRES`.
  - Les blocs à obligation gardent leur ligne `[REQUIS]` (11a).
  - **Exemple pour `DIR-LEVIERS`** : « [REQUIS — premier écran, identité ou scène DIRECTION à décision visuelle ouverte] Avant le build, diverge sur image : cinq directions avec leur probabilité ; ta première idée astucieuse est la modale au second degré ; trois esquisses face à la modale, choisies sur planche. Détail : `DIRECTION/DIVERGENCE`. »
  - **Cible** : noyau de **25 000 octets au plus** (−45 %).
  - Lecture fixe d'un run DIRECTION : de 77 000 à environ 56 000 caractères.
- **B.** Commencer par les seuls blocs sans obligation : environ 35 000 octets.

### 11d — Passage « Sans outils » et réécriture courte des invariants

- **A (recommandée).**
  - Le passage « Sans outils » au noyau (profil E2) : quoi faire sans capture ni script, et comment le déclarer `NOT-VERIFIED`.
  - **Garde** : aucune consigne du noyau ne suppose un sous-agent.
  - Puis réécriture courte des blocs gardés (`TRACE`, `SORTIE`, `ABSOLUS`, `BRIEF`…), à sens constant.
  - **Cible finale** : **18 000 octets au plus** (−60 %).
  - Lecture fixe d'un run DIRECTION : environ 49 000 caractères.
- **B.** S'arrêter à 11c.

## 3. Gardes communes à chaque sous-lot

- Budget du noyau abaissé à la cible du sous-lot (garde `CORE`).
- Toutes les obligations `[REQUIS]` sont tenues (11a), avec mutation rouge.
- Tous les tests existants passent. Les gardes qui exigent un texte exact au noyau (comme CORE-01) sont revues **une par une**, et le rapport le dit : elles sont gardées, adaptées ou déplacées vers la route.
- Le rapport donne pour chaque bloc retiré : la ligne qui le remplace, et la route où son texte reste servi.

## 4. Ce qui est risqué, et la parade

| Risque | Parade |
|---|---|
| Une nuance du bloc se perd dans la ligne d'invariant | La route garde le texte entier ; la ligne nomme la route ; la relecture de Junior porte sur ces lignes |
| L'agent ne lit plus le détail | L'obligation reste visible ; l'index dit où lire ; **un run seul peut le mesurer** (lot 13) |
| Des gardes existantes exigent le texte au noyau | Revue une par une, et chaque adaptation est dite dans le rapport |
| Trop gros pour une session | Un sous-lot par session, chacun livrable et réversible |

## 5. Ordre proposé

1. **11a** : la garde d'abord. Aucun contenu ne bouge, révision `r`.
2. **11b** : l'index complet, révision `s`.
3. **11c** : les blocs de procédure deviennent des lignes, révision `t`.
4. **11d** : le passage sans outils et la réécriture courte, révision `u`.

**Pour chaque sous-lot, Junior relit les lignes d'invariant** : ce sont elles que tout agent lira.
