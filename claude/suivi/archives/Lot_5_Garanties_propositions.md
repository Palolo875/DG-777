# Lot 5 — Garanties vraies : propositions

15 novembre 2026. Révision de départ : `R2026-11-15c`. Document hors du paquet. Rien n'est intégré.

Le principe du lot : une garde dit exactement ce qu'elle garantit, et ce qui est produit à chaque run est contrôlé. J'ai relu les neuf constats dans les fichiers actuels.

| Sort | Constats |
|---|---|
| Déjà corrigé | D-03 (lot 3) |
| À corriger, sans choix à faire | D-04, D-05, E-07, D-15, E-14 |
| À corriger, avec un choix | E-02 avec G-09, D-17 |

**Ce que cela coûte.** Seule l'option A d'E-02 touche le noyau, d'environ 110 octets, sur une marge de 1 109. Aucun tronc ne change, et aucune règle ne change de sens.

---

## 1. Corrections sans choix

### D-04 — le résumé des gardes se lit comme une garantie de lecture

**Constat vérifié.** La validation de structure annonce « règles atteignables, 13 planchers d'obligation ». En réalité :
- « atteignable » veut dire qu'une route sert la ligne, pas qu'un mode la charge ;
- un « plancher » ne couvre que les obligations étiquetées `[REQUIS PAR LE MODULE]`.

**Changement.** Le message devient « règles servies par une route, 13 obligations étiquetées avec leur plancher (noyau ou tronc) ; la lecture effective n'est pas contrôlée ». La description des gardes 19 et 20 dit la même chose.

### D-05 — des gardes qui ne reconnaissent que les phrases déjà vues

**Constat vérifié.** J'ai rejoué les deux injections de l'audit dans une copie, et les deux passent. La garde du vouvoiement connaît huit tournures. Celle des affirmations de mode non datées connaît dix-huit marqueurs.

**Changement.** Deux gardes générales remplacent la reconnaissance par liste, là où c'est possible sans fausse alerte :
- **Vouvoiement des textes pour les personnes** (guides, README) : tout pronom de la deuxième personne du singulier (« tu », « toi », « tes », « t' ») est refusé, hors bloc de code. Il n'y en a aucun aujourd'hui.
- **Affirmation de mode datée** : dans les règles, les guides, le README et la skill, une phrase qui situe une tendance dans le temps (« cette année », « de l'année », « en ce moment », « actuellement ») doit être dans une ligne `[VEILLE AAAA-MM]`. Aucune occurrence aujourd'hui.

Les autres registres sont des listes par nature : vocabulaire retiré, résumés fidèles, conditions de façade. Leurs messages le disent désormais (« liste close »). Chaque nouvelle garde a sa mutation rouge : l'injection de l'audit.

### E-07 — deux instruments de lecture qui ne se connaissent pas

**Changement.**
- `DIRECTION/LECTURE-INSTRUMENTEE` cite le journal de mobilisation : il observe ce que les outils ont servi, ce qui sert de base à `ACTUAL-READ` ; une route servie n'est ni lue ni appliquée.
- L'en-tête de la fiche du journal rappelle les quatre catégories.

### D-15 — ajouter un fichier demande trois gestes

**Constat vérifié.** `build_distributions.sh` copie 36 fichiers ou dossiers nommés un à un. Le manifeste les liste aussi, deux fois.

**Changement.** Le build copie ce que le manifeste liste pour chaque distribution. Ajouter un fichier demande alors un seul geste : l'ajouter au manifeste, une fois par distribution.

Les variantes Local du README restent dans le script. Elles sont courtes et contrôlées : une balise sans variante fait échouer le build.

### E-14 — deux lieux pour la liste des fiches invalides

**Constat vérifié.** La validation d'ensemble teste 4 des 23 fiches invalides par la ligne de commande. Le validateur de fiches tient pourtant la table complète, avec le motif attendu de chacune.

**Changement.** La validation d'ensemble lit cette table et passe les 26 fiches par la ligne de commande : les 23 invalides avec leur motif, les 3 valides. Une seule liste.

---

## 2. Corrections avec un choix

### E-02 et G-09 — la seule trace produite n'est jamais contrôlée

**Constat vérifié.**
- La trace complète a un validateur de 1 099 lignes, mais aucun run de la phase 6 n'en a produit.
- La trace légère a été produite à chaque run et n'est jamais contrôlée. Elle doit tenir en « six lignes au plus » ; elle a fait 1 100 à 1 740 mots.
- Rien ne vérifie non plus que le défaut dominant décrit un geste appliqué plutôt qu'envisagé.
- La forme existe pourtant déjà, dans l'exemple de la skill : six lignes nommées, de `RUN:` à `PROCHAINE PREUVE:`.

| Option | Changement |
|---|---|
| **A (recommandée)** | Une sous-commande `python3 scripts/parcours.py trace FICHIER` lit la trace (fichier de trace, ou en-tête du fichier livré) et vérifie trois choses. Les six lignes nommées doivent être présentes, dans l'ordre, une fois chacune : sinon, échec. La longueur est un signal, pas un verdict : au-delà de 600 caractères par ligne `[À ADAPTER]`, la ligne est signalée. Une ligne `DÉFAUT DOMINANT RESTANT` qui dit seulement « envisagé » est signalée. Le noyau (bloc `TRACE`) nomme la forme et la commande, pour environ 110 octets. La commande de vérification de la page la propose quand une trace se trouve à côté de la page. |
| B | La même commande, sans la citer au noyau. L'agent ne la connaîtrait que par le savoir. |

### D-17 — les suites tournent trois fois par validation

**Constat vérifié.** La validation complète construit deux fois pour vérifier que les archives sont reproductibles. Chaque construction relance les contrôles de l'export Local : les suites sans navigateur tournent donc trois fois. Une préparation prend 20 à 25 minutes.

| Option | Changement |
|---|---|
| **A (recommandée)** | La seconde construction ne sert qu'à comparer les archives : elle saute les contrôles, déjà passés sur le même contenu. Une variable d'environnement, posée par la validation seule, déclenche ce mode. La reproductibilité reste vérifiée de la même façon, empreintes comparées. Gain estimé : un tiers du temps de préparation. |
| B | Ne rien changer. |

---

## 3. Vérification prévue

1. Branche `garanties`.
2. Tests :
   - les mutations rouges des deux gardes de D-05, sur les injections de l'audit ;
   - six cas pour la commande `trace` : conforme, ligne manquante, ordre inversé, ligne trop longue, geste envisagé, trace introuvable ;
   - la copie par manifeste : un fichier absent du manifeste n'entre pas dans les archives.
3. Le noyau ne change que par la phrase d'E-02 ; les troncs restent identiques.
4. Validation complète avec navigateur, archives régénérées, révision `R2026-11-15d`. Je mesurerai le temps de préparation avant et après.
5. Registre mis à jour.

**Critère d'arrêt.** Si la commande `trace` refuse l'exemple de la skill, c'est la commande qui est fausse, pas l'exemple : je m'arrête et je vous le montre.

## 4. Ce qu'il faut me dire

« D'accord, options A partout » suffit. Sinon : les corrections du § 1 à écarter, et l'option choisie pour E-02 et D-17.
