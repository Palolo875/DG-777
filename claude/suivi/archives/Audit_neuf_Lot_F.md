# Audit neuf — Lot F : présentation et maintenance

14 novembre 2026. Révision auditée : `R2026-11-13c`. Document hors du paquet. Rien n'est intégré.

**Lus en entier (17 fichiers, 176 k).** `README.md`, `RELEASE_NOTES.md`, les cinq fichiers de `guides/`, les trois de `maintenance/`, `references/README.md`, `canonical_minimum.md`, `flow.md`, `examples.md`, `supports/README.md`, `.gitignore`, `.github/workflows/validate.yml`. Écart déclaré : les lignes très longues ont été lues coupées, sauf la fiche de version, lue jusqu'à 1 300 caractères par ligne.

**Lus par extraits (3 fichiers, 37 k).** `references/machine_projection.md`, `references/recettes.md`, `supports/generer.py`.

**Régénérés, comparés ou analysés par programme (22 fichiers, 608 k).** Les six SVG, les trois pages HTML, les trois JSON, les trois textes, le gabarit, le script de police et les cinq fichiers de police de `supports/`.

**Exécuté.** Régénération des supports dans une copie et comparaison ; recette de rendu du système sur ses trois pages ; captures de la carte au bureau et au mobile, regardées.

**Statuts.** Certain : lu ou mesuré. Probable : cohérent avec plusieurs observations. À vérifier : non établi. **Poids.** Bloquant, important ou mineur.

**Points de vue.** P personne, D designer, A agent, M mainteneur, T intégrité, V preuve.

---

## 1. Verdict du lot

La présentation est honnête et l'entrée est bonne. Le fond du problème est dans la fiche de version : elle dit elle-même que la méthode de preuve en cours ne peut pas répondre à la question que le système se pose.

1. **L'entrée d'une personne est réussie** (certain). Vingt lignes, quatre questions, aucun mot interne.
2. **La fiche de version rapporte un résultat défavorable sans le cacher** (certain). Sur la seule comparaison avec et sans le système, la personne qui juge a préféré trois fois sur quatre le rendu fait sans lui, pour un coût 1,7 fois plus élevé en jetons et trois à quatre fois en temps.
3. **Le cap et la preuve d'adoption ne visent pas la même comparaison** (certain). Le cap demande de comparer à un travail fait sans le système. La règle d'adoption dit que cette comparaison n'est pas exigée.
4. **Trente essais sont ouverts, aucun n'est adopté, aucun n'est retiré** (certain).
5. **Une phrase est fausse dans deux fichiers** (certain) : l'identité de marque n'aurait été éprouvée par aucun run, alors que la même fiche décrit ce run plus bas.

Aucun constat bloquant.

---

## 2. Ce qui tient

- **Le niveau 1 des guides** (`guides/1-utiliser.md`). Que demander, que fournir, que recevoir, comment poursuivre. Il annonce les questions de l'agent, l'accord demandé avant une génération, et que valider n'est pas accepter.
- **Le README dit ses limites** (`README.md:126-132`). Efficacité non vérifiée, niveau dépendant des moyens, savoir daté.
- **La fiche de version ne se flatte pas** (`maintenance/versions.md:104-115`). Elle nomme ses propres faiblesses de méthode : un run par condition, un seul juge humain non indépendant, un juge automatique de la même famille que les agents.
- **Chaque essai a sa condition de retrait** (`versions.md:69-100`). Trente lignes, trente retraits décrits.
- **Les supports se régénèrent à l'identique** (vérifié). Zéro fichier modifié après régénération. Police réduite à 11 k, licence embarquée, poids plafonné.
- **La carte du système est lisible** (regardée au bureau). Cinq blocs, une hiérarchie claire, un équivalent en texte.
- **Le glossaire traduit** (`guides/glossaire.md`). Chaque étiquette anglaise y reçoit un mot français et un renvoi.
- **L'intégration continue est épinglée** (`validate.yml`). Actions fixées par empreinte, versions des dépendances nommées.

---

## 3. Constats importants

### F-01 — Le cap et la preuve d'adoption ne mesurent pas la même chose

**Lieu.** `maintenance/versions.md:22, 67, 110-112`. **Points de vue.** V. **Statut.** Certain, lu.

| Ligne | Ce qu'elle dit |
|---|---|
| 22, le cap | « Chaque question se juge par comparaison avec un travail fait sans lui, sur des demandes comparables. » |
| 67, la preuve d'adoption | La référence est « le meilleur rendu antérieur sur le même brief » ; « une comparaison avec et sans la section n'est pas exigée ». |
| 112, l'état de la preuve | Les runs jugés « éprouvent des sections, pas l'effet du système ». |
| 110, la seule comparaison avec et sans | Juge automatique : 8 sur 8 pour le système. Personne qui pilote : 3 sur 4 pour le rendu fait sans lui. Coût : 1,7 fois plus de jetons, trois à quatre fois plus de temps. |

La méthode en cours compare le système à ses versions précédentes. Elle peut dire qu'une révision fait mieux que la précédente. Elle ne peut pas lever « efficacité non vérifiée », et la fiche le sait. Le seul indice sur la question du cap penche, côté humain, contre le système. Il est mince : quatre rendus notés.

### F-02 — Trente essais ouverts, aucun adopté, aucun retiré

**Lieu.** `maintenance/versions.md:63-102`. **Points de vue.** M, V. **Statut.** Compte certain ; tendance probable.

| Mesure | Valeur |
|---|---|
| Lignes d'essai | 30, dont 25 au statut d'essai formel |
| « Pas encore éprouvé sur un run » | 5 |
| « Observé » ou « exécuté » sur des runs | 12, le plus souvent sur un à quatre runs |
| Adoptées | 0 |
| Retirées | 0 |
| Échéance de revue | une seule, globale : avant avril 2027 |

Un run de phase 6 éprouve une dizaine de sections à la fois. La fiche l'écrit pour l'une d'elles : le rendu a été jugé meilleur « avec d'autres changements en même temps : l'effet propre de cette section n'est pas isolé » (`versions.md:97`). Dans ces conditions, une section ne peut ni gagner son adoption ni la perdre. Les essais s'accumulent, et le tronc comme le noyau sont déjà au plafond (D-07).

### F-03 — Une phrase fausse sur l'identité de marque, dans deux fichiers

**Lieu.** `README.md:7` ; `maintenance/versions.md:14` et `:99`. **Points de vue.** T, P. **Statut.** Certain, lu.

Le README et l'en-tête de la fiche disent : « aucun run ne l'a encore éprouvée ». La même fiche dit à sa ligne 99 : « Observé sur un run d'agent neuf : route lue, esquisses en signes noirs face à la modale, signe monochrome tenu de 16 à 256 px, système complet. » Le run IDT-1 existe dans l'archive de reprise.

Une lecture possible : « éprouvée » voudrait dire « jugée par vous », et ce verdict est en attente. La phrase ne le dit pas.

### F-04 — La fiche « ne retrace pas son histoire », mais elle raconte les runs

**Lieu.** `maintenance/versions.md:8, 69-100` ; `maintenance/evolution.md:113-127` ; `scripts/validate_design_governance.py:411-417`. **Points de vue.** T, M. **Statut.** Certain.

La table des essais pèse 25 k sur les 39 k de la fiche. Elle contient des récits : « exécuté sans être demandé par six agents neufs sur trois briefs courts », « sur un brief joué trois fois », « deux runs sur un même brief retiennent la même photo ». Les pièces de ces runs sont hors du paquet. Un lecteur du paquet ne peut en vérifier aucune.

Second cas : `evolution.md` écrit que « l'historique de conception n'est pas livré avec le paquet », puis garde une section sur les alias « issus des brouillons antérieurs à V1 ». Un validateur exige la présence de ces cinq alias.

Avec D-10, cela fait trois endroits où votre règle 3 n'est tenue qu'à moitié. C'est une question de frontière : l'état de la preuve est-il de l'histoire ?

### F-05 — Trois tables d'orientation de plus, dont une servie à l'agent

**Lieu.** `guides/2-comprendre.md:23-69, 72-90, 111-127`. **Points de vue.** A, M. **Statut.** Certain.

| Table | Lignes |
|---|---|
| Carte des sujets : où lire d'abord, voir aussi | 41 |
| Combinaisons par résultat recherché | 9 |
| Angles à examiner | 11 |

Elles sont écrites pour les personnes. La carte des sujets est pourtant affichée à l'agent en tête de chaque recherche `--trouver` qui nomme un sujet. Avec A-12, D-03 et E-05, le compte des lieux qui disent quoi lire dépasse la dizaine. La garde « une seule table de signaux » ne regarde pas ce fichier.

### F-06 — 69 k de texte dérivé à tenir en accord avec les sources

**Lieu.** `guides/3-maitriser.md` (30 k), `guides/glossaire.md` (23 k), `guides/2-comprendre.md` (16 k). **Points de vue.** M, P. **Statut.** Tailles certaines ; public réel : question.

Le niveau 3 redit le système en 296 lignes : classement, table des modes, contrat du premier objet, une passe, clôture. Le glossaire porte 95 termes. Ces textes ne créent aucune règle, et c'est pour cela qu'ils coûtent : une bonne part des 56 conditions de façade (D-05) existe pour empêcher ces redites de diverger.

Le niveau 3 s'adresse à qui « pilote un travail, seul avec un agent ou à plusieurs ». La fiche de version, l'évolution et la gouvernance parlent d'équipe, de consommateurs, de responsable de maintenance, de revue communautaire. Le système est tenu et jugé par une personne.

---

## 4. Constats mineurs

| N° | Lieu | Constat | Vue | Statut |
|---|---|---|---|---|
| F-07 | `supports/index.html` | La recette de rendu du système, passée sur sa propre carte, rend un retour à 1 440 px : « CONCEVOIR » et « Design » se chevauchent de 4 px. À l'œil, rien ne gêne. Soit un défaut minime, soit un faux positif de la recette. Le contrôle des supports déclare « rendu non évalué » : le système ne passe pas sa recette sur ses pages. | D | certain |
| F-08 | `supports/` | 629 k, soit 26 % de l'export installé chez l'agent, pour trois cartes destinées aux personnes. | P, A | certain |
| F-09 | carte au mobile | La note « Carte de responsabilités, pas un ordre fixe d'exécution » se place en retrait, mal alignée sous son titre. | D | certain, vu |
| F-10 | `references/examples.md` | Quatre exemples sur cinq montrent une trace complète avec verdict. Les runs produisent tous une trace légère. | A | certain |
| F-11 | `maintenance/versions.md:69-100` | Des cellules de table de 1 100 à 1 630 caractères. Illisible pour une personne. | P | certain |
| F-12 | `versions.md:76, 77` | Deux preuves attendues demandent « plusieurs personnes » et une « avec et sans le tableau », contre la règle d'adoption de la ligne 67 et contre votre règle 7. | T | certain |
| F-13 | `README.md:42` | L'installation par `npx skills add` est dite « vérifiée le 14 octobre 2026 depuis une copie locale ». Non vérifiable ici. | P | à vérifier |
| F-14 | `evolution.md:20` | « Une modification substantielle est exercée sur un run réel avant adoption élargie. » Les révisions 13b et 13c n'ont pas eu de run. | T | à vérifier au lot G |
| F-15 | `README.md`, guides, `maintenance/README.md` | « package » et « paquet » alternent : 7 et 14 occurrences dans les textes d'entrée. | P | certain |

---

## 5. Propositions (non intégrées)

Chacune se décide à part.

1. **F-01.** Votre décision la plus structurante de tout l'audit : quelle question les runs doivent-ils trancher ? Soit « le système fait-il mieux que sans lui », et il faut des paires avec et sans. Soit « cette révision fait-elle mieux que la précédente », et le cap se réécrit pour le dire.
2. **F-02.** Décider un plafond d'essais ouverts, ou un run par essai isolé pour les plus coûteux en place. Sans l'un des deux, la liste ne peut que grandir.
3. **F-03.** Corriger la phrase dans le README et dans la fiche.
4. **F-04.** Trancher la frontière de la règle 3 : l'état de la preuve reste-t-il dans la fiche, ou devient-il un renvoi vers le suivi ?
5. **F-05, F-06.** À discuter : ce que le niveau 3 et les tables du niveau 2 apportent à leur seul lecteur réel.
6. **F-07.** Passer la recette sur les trois pages de supports dans la validation, et régler soit la page, soit le seuil.

---

## 6. Ce que ce lot n'a pas vérifié

- `machine_projection.md`, `recettes.md` et `generer.py` n'ont pas été lus en entier.
- Les pages `parcours.html` et `boucle.html` ont passé la recette sans retour ; je ne les ai pas regardées.
- Les SVG clairs et sombres n'ont pas été regardés un à un.
- Aucun des runs que la fiche de version raconte n'a été recoupé avec les pièces de l'archive : c'est l'objet du lot G.
- L'installation par l'outil `skills` et le dépôt public n'ont pas été essayés.
- Le thème sombre, l'export SVG et le choix d'une entrée dans les pages interactives n'ont pas été essayés.
