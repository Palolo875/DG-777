# Lot 13 — Évaluation finale, étape 1 : non-régression de la V1.1.0

- **Lancé le** 25 novembre 2026. **Décision** de Junior : « Option B, je juge seul. Attention à mes limites. »
- **But** : savoir si la V1.1.0 (`R2026-11-15x`) tient la qualité de `R2026-11-15l` (préférée au PILOT), et si elle coûte moins.
- **Option B** : cette étape (2 runs) d'abord ; l'étape 2 (sans système et V1.1.0 sur un objet neuf, 2 runs) seulement si celle-ci ne montre pas de régression, et après décision de Junior.

## Conditions

| Run | Objet | Paquet | Référence |
|---|---|---|---|
| 19x | Objet 1 : carton d'invitation à un vernissage | `R2026-11-15x` (V1.1.0) | 17l du PILOT |
| 20x | Objet 2 : widget « marées du jour » d'un club de voile | `R2026-11-15x` (V1.1.0) | 18l du PILOT |

**Règles communes, identiques au PILOT :**
- un agent neuf (sous-agent `general-purpose`, modèle de la session, effort par défaut), un dossier vide, le paquet installé depuis l'archive Local livrée ;
- `DG_JOURNAL` activé ;
- **le prompt des runs 17l et 18l, mot pour mot**, au chemin du dossier près (brief compris, avec son erreur d'arrondissement) ;
- le mode est laissé à l'agent, comme au PILOT : c'est la condition de la comparaison (écart assumé à la règle 8, qui vaudra pour l'objet neuf de l'étape 2) ;
- ressources : Internet gratuit et sans compte ; ni génération d'images, ni outil branché, ni service payant.

## Jugement à l'aveugle

- Pour chaque objet, Junior voit deux rendus, nommés A et B (objet 1) et C et D (objet 2), recapturés **aux mêmes réglages**, et choisit, avec sa raison en une phrase.
- La correspondance a été tirée au sort **avant** les runs. Empreinte sha256 : `544ff43ffb1b9ff3abe57fcd60e0dda85b18f30a7b50a67779960382625840ea`.
- **Limite connue** : Junior a déjà vu les rendus de `l` au PILOT ; il peut en reconnaître un.

## Mesures

- Coût de chaque run par `Pilot_9b/cout_des_runs.py` : tours, sortie, lecture de cache, contexte maximal, images, appels par outil ; comparé à 17l et 18l.
- Relevés : mode choisi, outils de la boucle servis (`chantier`, `captures --version`, `verifier` différentiel), lignes du noyau suivies (diverger sur image, déclarer la direction, atelier), trace.

## Règle de décision (étape 1)

- **Pas de régression** si la V1.1.0 n'est pas moins bien jugée que `l` sur les deux objets.
- **Coût** : la baisse attendue se lit en tours et en lecture de cache ; le plan visait −30 %.
- Une paire perdue : on en cherche la cause dans la transcription avant l'étape 2.

## Limite

Deux paires montrent une tendance ; elles ne prouvent ni gain ni perte.

## Résultats (25 novembre 2026)

**Correspondance révélée** (empreinte vérifiée `544ff43f…`) : objet 1, A = V1.1.0 (19x), B = `l` (17l) ; objet 2, C = `l` (18l), D = V1.1.0 (20x).

**Jugement de Junior** :
- **Widget : D (V1.1.0)**, « avantage fonctionnel » : état « non actualisé » qui retire les comptes à rebours périmés, créneaux, hauteur instantanée et tirant d'eau affichés ensemble, mortes-eaux justifiées. **Régression visuelle notée** : trois colonnes denses, couleurs multipliées (rose pâle peu contrasté sur la courbe), moins de respiration et de sobriété.
- **Invitation : B (`l`)**, « avantage éditorial » : typographie expressive, vert émaillé décliné, accroche sur la cuisson, bandeau final. A (V1.1.0) gagne en clarté pratique (bloc « Venir », coupon, champ nom, « par courriel ») mais **régresse esthétiquement** : linéale neutre au lieu d'une police à empattements, reflet d'émail plus artificiel, tampon retiré.
- Junior compare aussi aux rendus du PILOT (« X », « Y ») : la limite de mémoire s'est réalisée.

**Coût** (`cout_des_runs.py`) :

| Run | Tours | Sortie | Cache lu | Images | Durée |
|---|---|---|---|---|---|
| 17l → 19x (invitation, DIRECTION) | 163 → 141 (−13 %) | 190 k → 150 k (−21 %) | 36,6 M → 33,5 M (−8 %) | 29 → 22 | 22 → 18 min |
| 18l → 20x (widget, STANDARD) | 208 → 122 (−41 %) | 300 k → 145 k (−52 %) | 45,3 M → 22,5 M (−50 %) | 24 → 18 | 21 → 16 min |
| **Ensemble** | **371 → 263 (−29 %)** | **−39 %** | **81,9 M → 56,0 M (−32 %)** | 53 → 40 | 43 → 34 min |

**Ce que les transcriptions montrent** :
- **Le noyau-index sert** : les deux agents ont ouvert les routes que nomment les lignes (19x : `DIRECTION/DIVERGENCE`, `DIRECTION/DIRECTION-ATELIER`, `ACTION/ATELIER-EDITION`, `SAVOIR/CRAFT/CFT-00`, `CFT-01`, `SAVOIR/TYPE-VOIX`… ; 20x : `DIRECTION/DIVERGENCE`, `SAVOIR/TYPE-VOIX`, `ACTION/UI-UX-REALITY`…). Les deux ont divergé sur planche face à la modale.
- **20x (STANDARD) n'a pas ouvert l'atelier** (`ACTION/ATELIER-EDITION` : test de retrait, passe de finition). La ligne le réserve aux surfaces `DIRECTION` ; en `l`, le bloc entier était au noyau et se lisait dans tous les modes. Hypothèse pour la densité du widget.
- **19x a comparé 8 voix sur le vrai titre** et a nommé la serif italique « modale », puis s'en est écarté : la pression contre la modale a écarté le choix que Junior préfère. `l` avait la même question au noyau.

**Lecture** : une paire gagnée, une perdue. Selon la règle du PILOT, deux paires opposées ne permettent pas de conclure sur la qualité. Le coût baisse d'environ un tiers. Le jugement montre un déplacement : **plus de fonction et de robustesse, moins de retenue et d'expression**.
