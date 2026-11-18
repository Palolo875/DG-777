# Lot S — Structure : propositions

14 novembre 2026. Révision de départ : `R2026-11-14a`. Document hors du paquet. Rien n'est intégré : ce lot attend votre accord, parce qu'il déplace et retire des textes.

## 1. Les décisions de départ

| Sujet | Décision |
|---|---|
| Noms | **Codes seuls.** Les adresses lisibles disparaissent ; dans les textes pour les personnes, une section se cite par son titre, en lien cliquable. |
| Lecteur | **Sans registre** : c'est le choix que vous m'avez laissé, justifié ci-dessous. |
| Export Local | Tel quel. |
| Moment | Maintenant, avant le lot 2. |

### Pourquoi le lecteur sans registre

Je l'ai vérifié dans les fichiers avant de choisir.

- **Le lecteur n'a presque pas besoin de sa table.** Sur les 30 lignes de la table des routes, 26 se retrouvent déjà par leur seul titre. Les 4 autres sont des sous-sections dont le titre ne commence pas par leur code ; un retitrage suffit (§ 3).
- **Hors des pages de `sections/`, tout le texte normatif est déjà dans une route.** Je l'ai mesuré : un texte « de famille » construit seulement à partir des routes ne perd aucune règle. Il ne perd que les préambules de `sections/` et les deux blocs du rôle et de la posture, qui déménagent.
- **Les gardes qui tomberaient sont peu nombreuses.** Dans une copie, j'ai retiré les préambules de `sections/` et relancé les validateurs. Quatre conditions échouent, et chacune garde le préambule lui-même, rien d'autre.

Le gain est durable : déplacer une section ne demandera plus de tenir un registre. Le risque est connu : c'est le plus gros chantier technique du plan.

---

## 2. Ce qui change, vu par une personne

**Les guides deviennent cliquables.** Les 218 citations d'adresses deviennent des liens vers la section.

| Aujourd'hui | Après |
|---|---|
| `` `savoir/typographie` `` | [Typographie](../design/savoir/typographie.md#…) |
| `` `agent/chemins#classer` `` | [Classer avant d'agir](../agent/chemins.md#…) |

**Le lecteur ne prend plus que des codes.** `python3 scripts/read_route.py SAVOIR/TYPE` ; les exemples du README et des guides sont réécrits ainsi.

**Le dossier `sections/` disparaît.** Le README racine et les guides n'y renvoient plus.

---

## 3. Ce qui se déplace

Rien de ce tableau ne change de sens. Seule la place change.

| Quoi | D'où | Vers |
|---|---|---|
| Rôle (bloc du noyau, concept ROL-01) | `sections/DIRECTION.md` | `design/direction/standard.md`, en tête de la route des cinq règles absolues |
| Posture (bloc du noyau) | `sections/DIRECTION.md` | même lieu, après le rôle |
| Carte des sujets, combinaisons, angles, quand s'arrêter | `guides/2-comprendre.md` | sur place ; les adresses deviennent des liens |
| Résolution des routes | `maintenance/README.md` | sur place, réécrite : le lecteur cherche le titre |

Le noyau compilé ne change pas : il compile les mêmes blocs, dans le même ordre. Je le vérifierai octet par octet.

**Quatre sous-sections retitrées**, pour que le lecteur les trouve sans table. La convention existe déjà ailleurs (« B1b — … », « CFT-01 — … »).

| Code | Titre aujourd'hui | Titre proposé |
|---|---|---|
| `DIRECTION/START/TREE` | Arbre de classification | TREE — arbre de classification |
| `SAVOIR/FRAME/COMPOSITION` | Grammaire positive de composition | COMPOSITION — grammaire positive de composition |
| `SAVOIR/FRAME/SINGULARITE` | Singularité sans rejet des conventions | SINGULARITE — singularité sans rejet des conventions |
| `SAVOIR/INTEGRITY/REPASSE` | Méthodologie studio | REPASSE — méthodologie studio |

Les liens vers leurs anciennes ancres sont corrigés en même temps ; la validation les contrôle.

---

## 4. Ce qui est retiré — à valider ligne par ligne

Ce sont des doublons ou des textes d'orientation. Pour chacun, je dis où vit déjà ce qu'il dit.

| N° | Texte retiré | Taille | Ce qu'il dit, et où cela vit déjà |
|---|---|---|---|
| R1 | Les pages « responsabilité » de `ACTION`, `SAVOIR`, `BIBLIOTHEQUE` (`sections/`) | 13 k | Rôle de chaque famille et ce qu'elle « ne remplace pas » : déjà dans les README de `design/`, `agent/`, `gouvernance/`. Leur table « Document : `DIRECTION.md` » cite des fichiers qui n'existent plus (A-22). La carte de lecture par mode d'`ACTION` redit `DIRECTION/CHARGE` (A-12). |
| R2 | « Réconciliation des vues de direction » (`sections/DIRECTION.md`) | titre seul | Rien : titre sans contenu (A-19). |
| R3 | Chemin canonique de démarrage (`sections/READING_MAP.md`) | 1 k | Redit `DIRECTION/START` et `DIRECTION/CHARGE`, et le niveau 3 des guides. |
| R4 | Constitution minimale (idem) | 0,3 k | Un renvoi vers les cinq règles du README. |
| R5 | Routage minimal par décision (idem) | 1,5 k | Une septième table « quoi lire » (A-12) ; `DIRECTION/CHARGE` fait foi. |
| R6 | Handoff minimal commun (idem) | 1,2 k | Une copie du handoff d'`ACTION/HANDOFF`, que le validateur doit garder égale à l'original. |
| R7 | Table des routes (idem) | 3,5 k | Le lecteur la remplace : `--sommaire` liste déjà toutes les routes. |
| R8 | `sections/README.md`, sommaire des sources | 4 k | Le README racine, les README de dossier et la fiche de version. |
| R9 | La table des 95 adresses lisibles (lecteur) | — | Remplacée par les liens. |
| R10 | La table des lieux (52 entrées), les 80 marqueurs de provenance, les bandeaux générés | — | Le lecteur trouve chaque section par son titre. |

R3 à R6 appartenaient au lot 3 (doublons). Je les avance parce qu'ils vivent dans le dossier qui disparaît : les garder demanderait de leur trouver une place, puis de les retirer un lot plus tard.

---

## 5. Les gardes qui changent

### Quatre gardes retirées, parce qu'elles gardent un texte retiré

| Garde | Ce qu'elle protégeait |
|---|---|
| MNT-01 | Le préambule de `BIBLIOTHEQUE` (R1) |
| LCF-25 | La carte de lecture par mode d'`ACTION` (R1) |
| « Orientation ACTION » (deux contrôles) | La même carte, et une phrase sur la vue courte (R1) |

### Gardes qui tombent avec les copies retirées

LCF-C1, la copie du handoff, et la partie de LCF-01, LCF-07, LCF-56 qui vérifiait les lignes de R5 et R6. La partie de ces conditions qui porte sur les sources reste.

### Gardes refondées, même protection

| Garde | Aujourd'hui | Après |
|---|---|---|
| Propriété des concepts (une définition chez son propriétaire) | fichier d'origine, lu dans les marqueurs | famille du code de la route qui contient la définition |
| Atteignabilité ATT-01 (toute règle est servie) | lignes de provenance normative | toute ligne d'un fichier de règles, hors en-tête et zones d'orientation |
| Ordre ORD-01 (le rôle avant tout) | ordre dans `DIRECTION.md` | le rôle ouvre le noyau compilé |
| Une seule définition par locator | table et porteurs | titres uniques dans tous les fichiers de règles |
| Test de déplacement | déplacement, puis mise à jour de la table | déplacement seul : tout reste vert, sans toucher à rien d'autre |
| Textes lus par les gardes de façade | sources historiques recomposées | familles construites à partir des routes ; guides, glossaire et fiche de version lus par leur fichier |
| Marqueur « expérimentation maintenue » | dans chaque source historique | README, notes de version, fiche de version et skill |

**Critère d'arrêt.** Si une garde ne peut pas se refonder sans perdre ce qu'elle protège, je m'arrête et vous la montre avant de continuer.

---

## 6. Vérification et livraison

1. Une branche `structure`.
2. Le noyau compilé comparé octet par octet avant et après.
3. Les 84 routes servies par le lecteur, avant et après, comparées texte pour texte.
4. Tests adaptés, puis un test nouveau : une section déplacée dans un autre fichier reste servie, sans rien toucher d'autre.
5. Validation complète avec navigateur, archives régénérées, parcours de présentation de l'export Local.
6. Révision proposée : `R2026-11-14b`.

**Critère de réussite.** Validation verte ; noyau identique ; les 84 routes servies à l'identique ; plus aucune adresse lisible, aucun marqueur de provenance, aucun fichier dans `sections/` ; les guides se parcourent en cliquant.

**Ce que ce lot ne fait pas.** Il ne change aucune règle, ne raccourcit pas le README (lot 8) et ne fusionne pas les autres doublons (lot 3).

---

## 7. Ce qu'il faut me dire

- **D'accord pour tout**, ou les numéros de R1 à R10 à garder.
- Une remarque sur les quatre retitrages, si leur forme ne vous convient pas.
