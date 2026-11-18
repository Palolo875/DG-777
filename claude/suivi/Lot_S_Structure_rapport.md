# Lot S — Structure : rapport

14 novembre 2026. Révision de départ : `R2026-11-14a`. Révision livrée : `R2026-11-14b`. Document hors du paquet.

Décision appliquée : « D'accord pour tout » (R1 à R10, les quatre retitrages, le lecteur sans registre).

## 1. Ce qui a changé

### Pour une personne

- **Le dossier `sections/` n'existe plus.** Ses six fichiers sont retirés (R1 à R8). Le README racine, la fiche de version, les cartes du système (supports) et le niveau 1 des guides n'y renvoient plus.
- **Les guides se parcourent en cliquant.** Les 218 adresses lisibles des guides sont devenues des liens vers la section, titrés par le titre de la section : `` `savoir/typographie` `` devient [typographie et données](…). Quatre autres README suivent (design, savoir, gouvernance, scripts).
- **Les phrases qui expliquaient les adresses sont réécrites.** Le glossaire a remplacé l'entrée « Adresse (locator) » par « Code de route (locator) ».
- **Le lecteur ne prend plus que des codes** : `python3 scripts/read_route.py SAVOIR/TYPE`. Une ancienne adresse (`savoir/typographie`) est refusée proprement : « locator inconnu », sans trace d'erreur.
- **La maintenance explique la résolution sans table** (`maintenance/README.md`, « Résolution des routes ») : le lecteur cherche le titre qui commence par le code. Elle dit aussi comment déplacer une section (§ 4).

### Ce qui s'est déplacé

| Quoi | Avant | Après |
|---|---|---|
| Rôle (bloc `ROLE`, concept ROL-01) | `sections/DIRECTION.md` | `design/direction/standard.md`, sous-titre « Rôle », en tête de `DIRECTION/STANDARD` |
| Posture (bloc `POSTURE`) | idem | même route, sous-titre « Posture » |
| Les cinq absolus | en tête de la route | même place, sous un sous-titre « Les cinq absolus » pour garder la hiérarchie |

Le sous-titre « Posture — à lire avant toute action » est devenu « Posture ». La consigne « à lire avant toute action » n'avait plus de sens au milieu d'une route. Le noyau compilé, lui, ouvre toujours sur « 1. Rôle et posture ». Ce raccourcissement a aussi un effet mesuré, décrit au § 3.

### Les quatre retitrages

`TREE — arbre de classification`, `COMPOSITION — grammaire positive de composition`, `SINGULARITE — singularité sans rejet des conventions`, `REPASSE — méthodologie studio`. Les quatre codes se résolvent sans table.

### Le lecteur, sans registre

- Un **fichier de règles** est un fichier de `agent/`, `design/`, `gouvernance/` ou `maintenance/` qui porte au moins un titre à code. Il y en a 33.
- Le lecteur cherche le titre unique qui commence par le code. Pour un sous-code (`SAVOIR/CRAFT/CFT-03`), il cherche le sous-titre dans la section parente.
- Le texte d'une famille (`DIRECTION`, `ACTION`…) est construit à partir de ses routes, pour les contrôles.
- Retirés du lecteur : la table des 95 adresses, la table des 52 lieux, les 80 marqueurs `origine:` et les bandeaux générés (R9, R10).
- `build_core.py` cherche chaque bloc du noyau dans les fichiers de règles. Son registre ne nomme plus de fichier.

### Quatre phrases de règle corrigées, parce qu'elles nommaient ce qui disparaît

Elles changent le texte servi de leur route, sans changer la règle :

| Route | Avant | Après |
|---|---|---|
| `DIRECTION/CHARGE` (deux lignes, hors noyau compilé) | connexions de `sections/READING_MAP.md` ; « les codes du noyau et les adresses lisibles servent les mêmes sections » | connexions de `design/savoir/connexions.md` ; « chaque code du noyau sert une seule section, où qu'elle soit rangée » |
| `DIRECTION/CHARGE`, ligne SYSTÈME (hors noyau compilé) | `maintenance/versions` | `CHANGELOG` |
| `ACTION/RUN_CARD` | connexions de `sections/READING_MAP.md` | `design/savoir/connexions.md` |
| `ACTION/PIPELINE-DIRECTION` | `BIBLIOTHEQUE.md` fournit… | `BIBLIOTHEQUE` fournit… |

La connexion C06 cite aussi `CHANGELOG` au lieu de `maintenance/versions`. Les notes de version, la fiche de version et la skill portent désormais la mention « expérimentation maintenue ».

## 2. Ce qui a été vérifié

| Contrôle | Résultat |
|---|---|
| Noyau compilé, octet par octet | **Identique** (41 544 octets). `SKILL.md` complet : 44 015 / 46 000 octets ; les 31 octets de plus sont la mention « une expérimentation maintenue ». |
| Sorties du lecteur, avant et après (100 codes, repliés et complets, troncs, modes, connexions) | **185 sorties identiques sur 220.** Les 35 autres sont toutes attendues : les 4 retitrages, le Rôle et la Posture en tête de `DIRECTION/STANDARD`, les 4 phrases du § 1, la fiche de version, et les numéros de ligne des connexions, qui bougent parce que les marqueurs ont disparu. |
| Troncs des cinq modes | Identiques ; DIRECTION reste à 34 520 / 35 000 caractères. |
| Trouvabilité (jeux de réglage et témoin) | 18/30 et 10/15, comme avant. |
| Test de déplacement (nouveau, § 4) | Passe. |
| Tests | Lecteur 105, régressions d'audit 101, budget 18, préparation 10, journal 18, recette, parcours et regard. |
| Validation complète avec navigateur, archives régénérées | Passe (`preparer_livraison.py --require-browser`, code 0) : recette de rendu 79 cas navigateur, regard 39, parcours 141, cartes du système à 390, 768 et 1440 px, build reproductible, export Local validé seul. Police des cartes vérifiée avec ses versions d'outils. |

## 3. Ce que j'ai trouvé en route

- **Le Rôle et la Posture sont devenus cherchables.** Avant, ils vivaient hors de toute route et `--trouver` ne les voyait pas. Avec le sous-titre « Posture — à lire avant toute action », la requête témoin « les sections sont toutes pareilles » remontait `DIRECTION/STANDARD` en tête, à cause du mot « toute » dans un titre. Le jeu témoin descendait de 10 à 9 sur 15. Le sous-titre raccourci (§ 1) le ramène à 10.
- **La recherche rattache mieux certaines lignes.** Sans table, le lecteur reconnaît les sous-sections écrites « CODE — titre » partout, et non plus seulement sous les 30 lignes de l'ancienne table. Une ligne de Gate B se rattache maintenant à `ACTION/GATE-B/B3`, une ligne de cadrage à `SAVOIR/FRAME/FND-03`. Cela concerne 29 sous-routes, dont B1 à B6, FND-01 à FND-03, les identifiants de structure et `ACTION/OVERRIDE/FAIL-ASSUMED`. Un faux code (« PASS technique ≠ … ») est écarté par la règle d'écriture « CODE — titre ».
- **Un code dupliqué ne fait plus tomber toute la validation.** Avant, deux titres pour un même code arrêtaient plusieurs contrôles avec une trace Python. Maintenant, chaque contrôle nomme le code et ses deux emplacements. `--trouver` refuse toujours de chercher tant que le doublon existe.

## 4. Un écart à mon document de propositions

J'avais écrit que le test de déplacement vérifierait qu'une section déplacée « reste servie, sans rien toucher d'autre ». **C'est vrai pour le lecteur, le noyau et la structure, pas pour les liens des guides.** Un lien nomme un fichier. Quand la section change de fichier, le lien vise encore l'ancien. C'est le prix des liens cliquables : c'est vous qui les avez choisis, et je ne l'avais pas dit clairement.

Ce qui se passe maintenant quand on déplace `SAVOIR/TYPE` dans un autre fichier :

1. Le lecteur la sert depuis son nouveau fichier ; la skill compilée ne change pas ; la validation de structure reste verte.
2. La validation nomme **chaque lien** qui vise encore l'ancien fichier, et rien d'autre.
3. Une fois le nom du fichier remplacé dans ces liens, tout est vert.
4. Deux témoins doivent échouer, et échouent : le même code porté par deux titres, et une section déplacée sans son code.

La maintenance l'écrit en une phrase. **Décision possible, plus tard :** un petit outil qui réécrit ces liens tout seul. Je ne l'ai pas ajouté, faute de décision.

## 5. Les gardes

### Retirées, parce qu'elles gardaient un texte retiré

| Garde | Ce qu'elle protégeait |
|---|---|
| MNT-01 | Le préambule de `BIBLIOTHEQUE` (R1). |
| LCF-25 | La carte de lecture par mode d'`ACTION` (R1). |
| LCF-C1 | La copie du handoff (R6). |
| Contrat de lecture d'`ACTION` (trois contrôles : modes, « Carte de lecture par mode », « sixième voie ») | La carte de lecture d'`ACTION` (R1). La proposition en comptait deux ; le troisième, sur les modes, gardait la même carte. |
| Trois résumés fidèles (« carte d'ACTION », « ACTION, responsabilité », « READING_MAP : sortie par défaut ») | Des phrases de R1 et R5. Sans leur texte, ces entrées ne contrôlaient plus rien. |
| Partie « carte » de LCF-01, LCF-07, LCF-56 et de CHG-06 | Les lignes de R5 et R6. La partie qui porte sur les sources reste. |
| Éléments obligatoires de la carte (« Chemin canonique », « Routage minimal », « Handoff minimal commun », « Locators principaux », statut de READING_MAP) | Les sections R3 à R7 elles-mêmes. |

### Refondées, même protection

| Garde | Aujourd'hui |
|---|---|
| Propriété des concepts | La famille de la route qui contient la définition. Le contrôle est plus précis qu'avant : il travaille à la ligne, et non plus au fichier. |
| Vocabulaire retiré, ses exemptions | Par famille, à la ligne. |
| Blocs du noyau | Une balise hors d'une route est refusée. |
| Table de chargement | Admise seulement dans une route `DIRECTION` ou dans la skill. |
| ORD-01 | Le rôle puis la posture ouvrent le noyau compilé, et leurs blocs vivent dans une route `DIRECTION`. |
| ATT-01 | Toute ligne d'un fichier de règles, hors en-tête et zones d'orientation. Les sections de maintenance (`maintenance/`) se lisent par leur fichier. |
| MAP-01 | Une seule section « Combinaisons », au niveau 2 des guides. |
| Contrôle des lieux | Chaque famille a des routes. Aucun marqueur `origine:` ou `lieux:` ne revient, et aucun dossier `sections/` non plus. |
| Unicité des titres à code ; codes cités résolus | Dans tous les fichiers de règles. Les codes sont relevés aussi dans la skill et le README. |
| Témoin du lecteur | Un code porté par deux titres, ou sans titre, est refusé. |
| Carte des sujets | Chaque lien mène à une route qui traite le sujet. Une ancre inconnue est signalée. |
| Façades (LCF) | Les guides sont lus avec leurs liens convertis en codes, comme les adresses l'étaient avant. |
| Adresse lisible dans un texte | Signalée comme « adresse lisible retirée ». |
| Marqueur « expérimentation maintenue » | README, notes de version, fiche de version, skill et guide opérateur. |
| Test de déplacement | Décrit au § 4. |

Aucune garde n'a dû être affaiblie pour passer. Le critère d'arrêt n'a pas servi.

## 6. Livraison

- Dépôt : commit `adc17bc` sur la branche `structure`, fusionné dans `master`. Le contenu de l'archive GitHub est identique à ce commit.
- Dossier `R2026-11-14b/` : `Design_Governance_V1_GITHUB_R2026-11-14b.zip` (sha256 `5ae1ec2e…`), `Design_Governance_V1_LOCAL_R2026-11-14b.zip` (sha256 `6155d71c…`) et `design-governance-depot.bundle`.
- **Parcours de présentation de l'export Local.** Je l'ai fait.
  - À la racine : README, notes de version, skill et sept dossiers. Il n'y a plus de `sections/`.
  - `--sommaire` liste les 84 routes, fichier par fichier.
  - `SAVOIR/TYPE` se lit par son code ; `savoir/typographie` est refusé proprement.
  - `--trouver couleur` met en tête le sujet de la carte et son propriétaire (`SAVOIR/CRAFT/CFT-05`).
- **Bruit connu, laissé au lot 7** : les journaux du serveur de test et « journal introuvable » apparaissent encore dans le résumé de préparation.

## 7. La suite

Le lot 2 (erreurs et contradictions de texte), selon le plan. Une décision reste possible quand vous voulez : l'outil de réécriture des liens après un déplacement (§ 4).
