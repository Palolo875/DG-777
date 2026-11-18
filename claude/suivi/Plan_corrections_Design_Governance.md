# Plan de corrections — Design Governance V1

14 novembre 2026. Document hors du paquet. Point de départ : `R2026-11-13c` et l'audit neuf (126 constats). Rien n'est intégré tant que ce plan et chaque lot ne sont pas décidés.

## 1. Cadre fixé par vous

- Le chantier porte sur **le système lui-même**. Les questions de runs et vos verdicts sont mis de côté pour l'instant.
- **Ce qui est à l'essai sera adopté.**
- On corrige et on améliore **sans négligence** : chaque constat de l'audit reçoit un sort écrit.

Vos règles de travail s'appliquent : discussion et décision avant toute intégration ; corrections en V1.0 avec révision à identifiant neutre ; vérification dans les fichiers avant de proposer ; validation complète et régénération avant chaque livraison.

## 1 bis. Exigence de livraison, ajoutée le 14 novembre

Le système doit pouvoir être livré et utilisé tel quel : présentable, bien organisé, avec une hiérarchie et une navigation claires, une charge de lecture et de procédure réduite, compréhensible et professionnel. Pas un brouillon.

Cette exigence ne forme pas un lot de plus. Elle devient **un critère de sortie de chaque lot**, et elle donne au lot 8 son vrai contenu : une passe de livraison, pas une retouche.

**Sept critères vérifiables.**

| Critère | Ce qui se vérifie |
|---|---|
| **Entrée** | Une personne, un agent et un mainteneur trouvent chacun leur point de départ depuis le README, sans lire autre chose. |
| **Un lieu par sujet** | Chaque sujet a un propriétaire ; les autres lieux y renvoient. Plus de table concurrente. |
| **Aucun reste** | Plus de titre sans contenu, d'étiquette définie et jamais employée, de renvoi périmé, de trace de l'ancien rangement. |
| **Lisibilité** | Aucune cellule de table ni paragraphe illisible d'un seul tenant dans un texte destiné aux personnes ; seuils fixés au lot 8. |
| **Langue** | Un mot français pour chaque notion qu'une personne rencontre ; les codes en capitales restent là où une machine les lit. |
| **Charge de procédure** | Ce qu'un agent doit lire et faire avant le premier rendu est compté, puis réduit ; même chose pour ce qu'un mainteneur doit faire pour ajouter une règle. |
| **Prêt à l'usage** | Installation rejouée depuis une copie propre, commandes du README exécutées, un exemple complet qui correspond à ce que le système produit réellement. |

**Tension à garder visible.** Réduire la charge veut dire retirer ou fusionner du texte. « Sans négligence » veut dire ne rien perdre d'utile. Chaque retrait est donc montré avant d'être fait, avec ce qu'il devient.

**Question d'organisation à trancher au lot 8.** Le paquet porte deux systèmes de noms pour les mêmes sections : les codes (`DIRECTION/START`) et les adresses lisibles (`agent/chemins#classer`), plus un dossier `sections/` hérité de l'ancien rangement et une table de correspondance dans le lecteur. C'est la source principale de l'effet « brouillon » pour qui ouvre le dépôt. La décision est lourde ; elle se prépare, constat par constat, à l'ouverture du lot 8.

## 2. Ce qui sort du chantier

Ces constats décrivent le protocole de mesure, pas le paquet. Ils restent au registre, sans action.

| Constats | Sujet |
|---|---|
| F-01, G-01, G-02 | Question du cap, verdicts, run sur la révision livrée |
| G-03, G-04, G-06, G-08 | Accords de la consigne, convergence entre runs, mémoire, coût mesuré |
| A-08, E-03, G-11 | Ce que la condition de run rend impossible |
| G-05, G-12, G-13, G-14 | Observations sur des runs passés |

Conséquence à garder en tête : sans run, chaque correction se vérifie par les tests, la validation et la relecture, pas par son effet sur un rendu.

## 3. Deux contraintes qui fixent l'ordre

1. **Les deux budgets sont pleins** : noyau à 96 %, tronc DIRECTION à 99 %. Faire arriver plus de savoir à l'agent (lot 4) exige d'abord de libérer de la place (lot 3).
2. **Les instruments d'abord.** Un outil qui mesure à côté fausse la vérification de tout ce qui suit.

## 4. Les lots

| Lot | Objet | Constats couverts | Nature |
|---|---|---|---|
| **1** | **Instruments justes** | C-01 (bloquant), C-02, C-03, C-04, C-05, C-06, C-07, C-10 à C-17, D-01, D-02, D-11, D-14, D-16, G-07, H-04, F-07 | Code et tests |
| **1 bis** | **Organisation cible** | prépare A-22, F-05, F-06, D-08, F-08 et la question des deux systèmes de noms | Sur papier, sans modifier le paquet : arborescence, noms, ce qui est livré, les trois parcours d'entrée |
| **S** | **Structure** — fait, `R2026-11-14b` | A-19, A-22 ; en partie A-12 (R3 à R6 avancés depuis le lot 3) | Lecteur sans registre, `sections/` retiré, codes seuls et liens dans les guides ; rapport : `Lot_S_Structure_rapport.md` |
| **2** | **Erreurs et contradictions de texte** — fait, `R2026-11-15a` ; B-19 et F-12 reportés au lot 6 | A-05, A-06, A-07, A-14, A-16 à A-23, B-06, B-14 à B-19, C-12, C-13, E-05, E-08, E-13, F-03, F-12, F-15, D-09 | Texte, corrections sûres |
| **3** | **Une seule voix** — fait, `R2026-11-15b` ; F-05 écarté avec raison | A-02, A-03, A-12, B-05, B-07, B-10, B-11, D-03, D-06, D-12, F-05, A-15 | Réduction des doublons ; libère de la place |
| **4** | **Ce qui doit arriver à l'agent** — fait, `R2026-11-15c` ; A-01 et B-01 reportés au run de contrôle ; B-03, B-04, B-09 proposés en lot 4 bis | B-01, B-02, B-03, B-04, B-09, A-01, A-04, A-10, A-11, C-18, A-24 | Carte des déclencheurs d'abord, puis acheminement du savoir, noyau et tronc |
| **4 bis** | **Savoir à écrire** — fait : `R2026-11-15f` (B-09), `R2026-11-15g` (B-04), `R2026-11-15h` (B-03) | B-09, B-04, B-03 | Trois sous-lots : accessibilité et performance ; sections ordinaires ; planches de principes |
| **5** | **Garanties vraies** — fait, `R2026-11-15d` ; D-03 déjà corrigé au lot 3 | D-03, D-04, D-05, E-02, G-09, E-07, D-15, D-17, E-14 | Gardes, messages, contrôle de la trace légère |
| **6** | **Adoption des essais** — fait, `R2026-11-15e` ; règle 6 tranchée (option A) | F-02, B-19, H-03, F-04, D-10, B-13, B-12, E-06 | Statuts, fiche de version, vos règles 3, 6, 7 |
| **7** | **Poids et coût** — fait, `R2026-11-15i` ; D-08 et F-08 écartés avec raison ; B-20 au lot 8 | D-07, A-09, A-13, A-25, C-08, D-08, F-08, B-20, B-22 | Budgets, sorties d'outils, export |
| **8** | **Passe de livraison** — fait : 8a `R2026-11-15j`, 8b `R2026-11-15k` (sept critères ; ANC-01 existait déjà) | F-06, F-09, F-10, F-11, F-13, E-04, E-09, E-11, E-12, D-13, D-18, A-22, D-09, et les sept critères de la section 1 bis | Organisation, navigation, noms, guides, glossaire, fiche lisible ; parcours des trois entrées avant livraison |

| **9** | **Run de contrôle** | G-02 | Un run sur le système corrigé, avant de le présenter comme prêt à d'autres que vous |

Les 126 constats sont tous dans l'une de ces lignes ou dans la section 2. Le détail constat par constat se fait à l'ouverture de chaque lot.

## 5. Déroulement d'un lot

1. **Relecture dans les fichiers** de chaque constat du lot : toujours vrai, déjà corrigé, ou à écarter.
2. **Proposition écrite**, constat par constat : le changement exact, ce qu'il coûte en budget, ce qu'il risque.
3. **Votre décision**, ligne par ligne.
4. **Intégration** sur une branche, tests ajoutés pour chaque défaut d'instrument.
5. **Validation complète avec navigateur, régénération des archives**, puis révision à identifiant neutre.
6. **Mise à jour du registre** : chaque constat passe à « corrigé », « écarté, avec raison » ou « reporté ».

**Critère de réussite d'un lot.** Validation verte, budgets respectés, chaque constat du lot a un sort écrit, et aucun des sept critères de livraison n'a reculé.

**Critère d'arrêt.** Si une correction demande de dépasser un budget ou de toucher une règle absolue, elle s'arrête et revient en discussion.

## 6. Décisions prises le 14 novembre

| Sujet | Décision |
|---|---|
| Forme de l'adoption | **Socle de la V1.** Les sections perdent leur statut d'essai et deviennent le contenu normal de la V1. Le vocabulaire d'essai et d'adoption sort de ces lignes. L'efficacité reste déclarée non vérifiée. |
| Règle 3, historique | **Tout sortir.** Les récits de runs quittent la fiche de version et le savoir pour le suivi. Les identifiants d'anciens constats dans les scripts sont remplacés par la raison en clair. Les anciens alias et leur garde sont retirés. |
| Règle 7, regard externe | **Garder pour d'autres.** Le regard externe reste une possibilité. Seuls les essais qui attendaient « plusieurs personnes » comme preuve sont corrigés, avec le lot 6. |
| Doublons | **Fusionner, retraits montrés.** Un propriétaire par sujet ; les autres lieux deviennent des renvois ou sont retirés. Chaque retrait est montré avant d'être fait. |

**Ordre retenu.** Les défauts des sections à l'essai se corrigent aux lots 1 à 5 ; le passage au socle se prononce au lot 6, sur des sections réparées.

**Règle 6, tranchée le 15 novembre (lot 6, option A).** Un principe se dit sans son auteur ; les normes, lois et ressources à atteindre restent nommées ; une observation `[VEILLE]` garde son type de source et sa date.

## 6 bis. Garde-fous retenus le 14 novembre

Vous avez accepté mon désaccord sur la mise à l'écart des runs et m'avez demandé d'en tirer ce qui est juste. Quatre garde-fous entrent au plan. Aucun ne rouvre la question des runs ni de vos verdicts pendant le chantier.

| Garde-fou | Ce qu'il fait | Où |
|---|---|---|
| **L'efficacité reste dite non vérifiée** | Le passage des essais au socle ne change pas cette phrase. Elle reste dans le README, les notes de version et la fiche de version, et sa garde reste dans la validation. | Lot 6 |
| **Une section reste retirable** | En passant au socle, chaque section perd son statut d'essai mais garde sa procédure de retrait, rangée dans la maintenance comme un mode d'emploi, pas comme une histoire. Le socle n'est pas un point de non-retour. | Lot 6 |
| **Une carte des déclencheurs, sans supposer** | Pour chaque route : où son signal est écrit, quel type de demande le déclenche, et si elle a déjà été exercée. Trois cas : déclencheur clair, déclencheur mal formulé ou introuvable, aucun déclencheur. Seuls les deux derniers sont des défauts. Une route non ouverte par les runs n'en est pas un. | Ouvre le lot 4 |
| **Un run avant de dire « prêt pour d'autres »** | Un seul run de contrôle sur le système corrigé, à la fin. Il ne conditionne aucun lot et ne demande aucun verdict avant. Tant qu'il n'a pas eu lieu, la livraison dit : corrigé et cohérent, non rejoué. | Lot 9 |

**Ce que j'ai retiré de mon avis.** L'idée que le système a « trop » : elle reposait sur des routes non ouvertes par quatre runs qui ne les appelaient pas. Reste le constat de texte : plusieurs lieux disent la même chose (lot 3).


## 6 ter. Organisation cible : décisions du 14 novembre

| Sujet | Décision |
|---|---|
| Noms | Codes seuls ; dans les textes pour les personnes, une section se cite par son titre, en lien cliquable. |
| Lecteur | Sans registre (choix laissé à Claude, justifié dans `Lot_S_Structure_propositions.md`). |
| Export Local | Tel quel. |
| Moment | Lot S, avant le lot 2. Fait : `R2026-11-14b`. |
| Retraits R1 à R10, retitrages | Acceptés tels que proposés (« D'accord pour tout »). |

Détail : `Organisation_cible_Design_Governance.md`.

## 7. Ce que ce plan ne promet pas

- Il ne dit pas que le système sera meilleur après : sans run, on saura qu'il est plus juste, plus cohérent et plus léger, pas qu'il produit de meilleures pages.
- Le lot 3 retire des doublons. Chaque retrait vous sera montré avant d'être fait.
- Le nombre de révisions n'est pas fixé : une par lot au plus, moins si deux lots se livrent ensemble.
