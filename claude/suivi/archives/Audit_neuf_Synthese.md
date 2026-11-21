# Audit neuf — Lot H et synthèse

14 novembre 2026. Révision auditée : `R2026-11-13c`. Document hors du paquet. Rien n'est intégré ; aucun run n'a été lancé.

Ce document ferme l'audit. Il rassemble les sept lots, ajoute les croisements du lot H, et classe les décisions qui vous reviennent. Les détails et les lieux exacts sont dans chaque rapport de lot.

---

## 1. Verdict général

Design Governance V1 est un système cohérent, honnête et bien outillé, qui atteint réellement l'agent et produit des pages construites et spécifiques. Rien, dans le paquet, n'est cassé.

Ce qui ne tient pas encore, c'est la preuve. Le cap demande de savoir si le système fait mieux qu'un agent sans lui. La méthode en cours ne pose plus cette question, et la seule comparaison de ce type penche, sur quatre rendus, de l'autre côté.

Pendant ce temps, le système grossit plus vite qu'il n'est éprouvé : trente essais ouverts, aucun adopté ni retiré, deux budgets au plafond, un coût par run en hausse de moitié sur le même brief.

La suite utile n'est donc pas d'ajouter du savoir. Elle tient en quatre décisions qui ne demandent aucun code : quelle question trancher, vos verdicts en attente, l'accord de génération dans la consigne, et un run sur la révision livrée.

---

## 2. Ce que l'audit a couvert

| Lot | Objet | Constats | Bloquant | Importants | Mineurs |
|---|---|---|---|---|---|
| A | Chemin de l'agent | 25 | 0 | 12 | 13 |
| B | Savoir de design | 22 | 0 | 9 | 13 |
| C | Outils de rendu | 18 | 1 | 6 | 11 |
| D | Navigation, validation, livraison | 18 | 0 | 7 | 11 |
| E | Gouvernance | 14 | 0 | 7 | 7 |
| F | Présentation et maintenance | 15 | 0 | 6 | 9 |
| G | Preuve, hors paquet | 14 | 0 | 8 | 6 |
| **Total** | | **126** | **1** | **55** | **70** |

**Couverture du paquet, 149 fichiers.** 79 lus en entier, 57 exécutés ou analysés par programme, 13 lus par extraits. Aucun fichier n'est resté sans examen.

**Vérifications exécutées.** Validation complète avec navigateur : `FULL VALIDATION PASSED`, code 0, en 11 min 43 s. 666 cas de test verts sur l'ensemble des suites. Régénération des supports : identique. Recette de rendu sur les pages livrées de cinq runs et sur les trois pages du système.

---

## 3. Ce qui tient, tous lots confondus

- **La mécanique est solide.** Le lecteur refuse plutôt que de deviner, le noyau ne peut pas perdre un bloc en silence, la construction des archives est transactionnelle et reproductible.
- **Le système ne se ment pas.** Efficacité déclarée non vérifiée, limites de chaque contrôle écrites, résultat défavorable rapporté dans la fiche de version.
- **La méthode atteint l'agent.** Modale chiffrée, esquisses sur planche, test de retrait, recherche par rôle avec refus déclarés : dans les quatre traces de la phase 6.
- **Les traces disent vrai sur les pages.** 32 affirmations sur 36 retrouvées dans les fichiers livrés, aucune démentie.
- **L'entrée d'une personne est réussie.** Vingt lignes, quatre questions, aucun mot interne.
- **Le banc d'essai est discipliné.** Critères écrits avant le run, cachés à l'agent ; avis séparé du verdict.

---

## 4. Les huit lignes de force

Les 126 constats se rangent en huit familles. Chacune est donnée avec ses constats d'appui.

### 4.1 La preuve ne répond pas à la question du cap

Le cap : comparer à un travail fait sans le système. La règle d'adoption : cette comparaison n'est pas exigée. La fiche écrit que les runs « éprouvent des sections, pas l'effet du système ».

- Seule comparaison avec et sans : vous avez préféré trois fois sur quatre le rendu sans le système (F-01).
- Dix verdicts pour trente-six runs ; le meilleur rendu désigné pour 4 briefs sur 13 (G-01).
- La révision livrée n'a jamais été jouée (G-02).
- Aucun run n'isole une section (F-02).

**Statut.** Certain. **Appuis.** F-01, F-02, G-01, G-02.

### 4.2 Le système grossit plus vite qu'il n'est éprouvé

| Mesure | Valeur |
|---|---|
| Essais ouverts | 30, dont 0 adopté et 0 retiré |
| Noyau | 43 984 octets sur 46 000 |
| Tronc DIRECTION | 34 520 caractères sur 35 000 |
| Phrases épinglées par les validateurs | 184 |
| Étiquettes en capitales dans la gouvernance | 113 |
| Coût sur le brief sommeil | de 65 à 102 outils, de 13 à 23 minutes |

Chaque série de runs a ajouté des règles, des marqueurs et des gardes. Aucune n'en a retiré. Aucune borne de coût n'est écrite.

**Statut.** Chiffres certains ; tendance probable. **Appuis.** F-02, D-07, D-05, E-04, G-08, A-09, B-08.

### 4.3 Une grande part du paquet n'a pas été exercée par les runs

*Section corrigée le 14 novembre, après votre remarque : la première rédaction concluait trop.*

Mesure du lot H, sur les quatre runs de la phase 6 :

| Mesure | Valeur |
|---|---|
| Routes de premier niveau ouvertes au moins une fois | 20 sur 84 |
| Texte de routes jamais ouvert | 302 000 caractères sur 484 000, soit 62 % |
| Routes de gouvernance ouvertes | 0 sur 13 |
| Routes de savoir ouvertes | 11 sur 38 |

**Ce que ces chiffres disent.** Quatre runs, tous en mode `DIRECTION`, tous arrêtés à une première proposition, n'ont exercé qu'une partie du paquet. C'est une mesure de la couverture des essais.

**Ce qu'ils ne disent pas.** Qu'une route non ouverte soit inutile ou en trop. Le système charge sur signal, et la gouvernance s'adapte au travail : c'est écrit, et ces runs s'y conforment. Une route faite pour un composant partagé, une retouche ou un travail à accepter n'avait aucune raison de s'ouvrir sur une page d'accueil en proposition.

**Deux cas à distinguer.**

- **Signal présent, route non ouverte.** Trois routes sont citées dans la ligne `DIRECTION` comme lecture « pendant la fabrication » et aucun des quatre runs ne les a ouvertes (A-04). La revue sur capture en quatre questions n'est pas au noyau (B-02). Ici le constat tient : le run était ciblé, la lecture n'a pas eu lieu.
- **Signal absent du brief.** Tout le reste, dont la gouvernance, les modes `LITE`, `ITER` et `SYSTÈME`, et une grande part du savoir. Ici on ne sait rien : ni que la route sert, ni qu'elle ne sert pas.

**Statut.** Chiffres certains pour la phase 6. Constat certain pour le premier cas ; aucune conclusion pour le second. **Appuis.** A-04, B-02, A-01 pour le premier cas ; B-01, E-01, B-05 décrivent le second et ne valent que comme couverture.

### 4.4 Plusieurs voix disent la même chose

| Ce qui se répète | Nombre |
|---|---|
| Lieux qui disent quoi lire | plus de dix |
| Cadres qui décrivent une direction | 7 |
| Grilles pour juger un rendu | 7 |
| Systèmes d'axes | 3 |
| Tables « par mode » | 3 |
| Listes de marqueurs de mode | 3 |
| Listes de rôles d'asset | 3 |

Les agents ne suivent aucune de ces tables telle quelle. Les gardes qui annoncent « une seule table » reconnaissent un en-tête, pas une fonction.

**Statut.** Certain. **Appuis.** A-02, A-03, A-12, B-05, B-07, D-03, D-06, E-05, F-05.

### 4.5 Plusieurs instruments mesurent à côté

- **Le seul constat bloquant de l'audit, C-01.** Le parcours par défaut vérifie 1 440 et 390 px. À 768 px, deux pages livrées sur quatre débordent et ont des textes qui se chevauchent. Les quatre traces écrivent « sans défaut bloquant ».
- La part de matière ne compte pas ce qui est codé : le cahier de FIN-3 et le ruban de FTX-1 comptent pour zéro (C-02).
- L'outil de références fournit des images sous la densité que le système exige (C-03).
- Le journal de mobilisation se trompe dans les deux sens sur la lecture, appelle « consultée » une route servie, et note « rien à traiter » pour les 81 appels du parcours (D-01, D-02, G-07).
- Les marqueurs mesurés sont ceux des vagues anciennes (C-05).

**Statut.** Certain, reproduit pour C-01, C-02, D-01, D-02. **Appuis.** C-01 à C-07, D-01, D-02, G-07.

### 4.6 Les garanties annoncées dépassent les contrôles

Les contrôles font ce que leur commentaire décrit. Ce sont leurs messages de succès qui se lisent comme plus larges.

- « Une table de signaux » : trois autres passent (D-03).
- « 13 planchers d'obligation », « règles atteignables » : présent dans le noyau, ou servi par une route, ne veut pas dire lu (D-04).
- « Vouvoiement des façades » : huit tournures connues. Deux injections sont passées (D-05).
- La trace légère, seul document qu'un run produit, n'a aucun contrôle ; une trace a déclaré conforme un comportement qui ne l'était pas (E-02, G-05).

**Statut.** Certain. **Appuis.** D-03, D-04, D-05, E-02, G-05.

### 4.7 La condition du run décide de ce qui est mesurable

| Condition du protocole | Ce qu'elle rend impossible |
|---|---|
| « Accords donnés : aucun », pas de clé | la génération et les banques d'images : la matière reste pauvre (G-03) |
| Dossier vide | le garde-fou contre la répétition, qui suppose un antécédent (A-08) |
| Arrêt à la première proposition | toute la trace complète : comparaison sur capture, Gate B, verdict (E-03) |
| Un seul agent | le regard séparé, non fait dans les quatre runs (G-11) |
| Bureau seul pour choisir la direction | une direction pensée d'abord pour le mobile (A-10) |

Le défaut le plus souvent relevé, la matière, se décide à une ligne de la consigne de lancement. Ajouter du savoir n'y changera rien.

**Statut.** Mécanismes certains ; lecture probable. **Appuis.** G-03, A-08, E-03, G-11, G-06, A-10, A-11.

### 4.8 Quatre de vos règles de travail ne sont tenues qu'à moitié

| Règle | Écart constaté |
|---|---|
| 3 — l'historique va hors du paquet | 32 identifiants d'anciens constats dans les scripts ; récits de runs dans la fiche de version et dans le savoir ; anciens alias exigés par un validateur (D-10, F-04, B-13) |
| 6 — principes sans citer la provenance | des auteurs et des entreprises sont nommés dans le savoir (B-12) |
| 7 — pas de juge externe, le juge c'est vous | le texte recommande plusieurs évaluateurs et décrit un regard « aveugle » ; trois essais attendent « plusieurs personnes » (E-06, F-12) |
| 9 — agent neuf, dossier vide | quatre runs ont reçu votre mémoire ; SOM-3, référence du brief sommeil, en fait partie (G-06) |

Ce sont des questions de frontière plus que des fautes. Elles vous reviennent.

**Statut.** Certain. **Appuis.** D-10, F-04, B-12, B-13, E-06, F-12, G-06.

---

## 5. Lot H : ce que le croisement des lots ajoute

### H-01 — La convergence entre runs a une cause mécanique

**Statut.** Mécanisme certain ; lien de cause probable.

Le système a un garde-fou contre la répétition : comparer une reprise à ses antécédents sur six champs. Il suppose qu'un antécédent existe dans le dossier. Le protocole impose un dossier vide. Résultat observé : même photo et même nom entre deux runs du brief sommeil, mêmes esquisses et mêmes prénoms entre deux runs du brief fintech. Les lots A et G avaient chacun la moitié du constat.

### H-02 — Un run lit entre 124 000 et 163 000 caractères

**Statut.** Certain, mesuré sur la révision livrée avec les routes relevées en phase 6.

| Part | Caractères |
|---|---|
| Noyau | 42 000 |
| Tronc | 34 500 |
| Routes ouvertes en plus, selon le run | 47 000 à 86 000 |

C'est environ un huitième des 276 000 à 299 000 jetons d'un run. Le coût d'un run est donc dans les boucles d'outils, pas dans la lecture : 15 à 23 appels du parcours par run, chacun de 39 secondes et de plusieurs milliers de caractères (C-08). Raccourcir le texte ne baissera pas sensiblement le coût ; réduire les tours de vérification, si. Cette part est une estimation à quatre caractères par jeton.

### H-03 — Six essais attendent une preuve que ces runs ne peuvent pas donner

**Statut.** Certain pour le relevé ; nuance ci-dessous.

Vingt-six lignes d'essai portent sur une route. Pour six d'entre elles, la route n'a été ouverte dans aucun run de la phase 6 : écriture et contenu, mouvement, relations de couleur, variable visuelle, leviers de caractère, recherche d'une méthode. Une partie de leur contenu arrive par le noyau ; la section elle-même n'a pas été lue. Leur preuve d'adoption ne peut pas venir de ces runs.

### H-04 — L'outil masque son identité, l'agent aussi

**Statut.** Certain pour l'outil ; certain selon le suivi pour l'agent.

Le téléchargement des polices se présente comme un navigateur (C-14). Sur un refus, l'agent de SOM-3 a relancé avec une autre identité (G-05). La règle du savoir dit : jamais en masquant son identité, jamais en contournant un refus. L'outil donne l'exemple contraire.

### H-05 — Rectificatif au lot E

Dans le lot E, ma liste des routes lues par run incluait des routes seulement proposées par la recette. Le constat E-01 n'en dépend pas : aucune route de gouvernance n'est ni lue ni proposée. Les comptes du présent document utilisent le relevé corrigé.

### Contradictions cherchées et non trouvées

J'ai cherché des constats qui se contrediraient d'un lot à l'autre. Je n'en ai pas trouvé : les sept lots, menés séparément, convergent. C'est un indice de solidité, pas une preuve ; ils ont tous le même auditeur.

---

## 6. Les décisions qui vous reviennent, classées

Les quatre premières ne demandent aucun code et conditionnent tout le reste.

| Rang | Décision | Pourquoi maintenant | Constats |
|---|---|---|---|
| 1 | **Quelle question les runs tranchent-ils ?** Mieux que sans le système, ou mieux que la révision précédente. | Elle fixe le protocole, le cap et ce qu'« adopté » veut dire. | F-01 |
| 2 | **Vos verdicts en attente** : FIN-3, IDT-1, les briefs « à désigner ». | Sans référence désignée, aucun run ne se compare. | G-01 |
| 3 | **Un accord de génération dans la consigne**, ou retirer la matière des critères. | C'est la cause du défaut le plus relevé. | G-03 |
| 4 | **Un run sur la révision livrée**, avant toute modification du noyau. | Toute la preuve porte sur une révision antérieure. | G-02 |
| 5 | **Le constat bloquant C-01** : largeurs vérifiées par défaut. | Deux pages livrées sur quatre ont des défauts que l'outil ne regarde pas. | C-01 |
| 6 | **Geler les ajouts**, ou fixer un plafond d'essais ouverts. | Les deux budgets sont pleins et aucun essai ne se ferme. | F-02, D-07 |
| 7 | **Réparer et archiver le journal** : sortie réelle mesurée, résultats du parcours notés, journal brut gardé. | C'est l'instrument de preuve, et il se trompe. | D-01, D-02, G-07 |
| 8 | **La portée de vos règles 3, 6 et 7.** | Trois frontières à tracer une fois. | D-10, F-04, B-12, E-06 |
| 9 | **La gouvernance** : un run mené jusqu'à la trace complète, ou hors du champ de la mesure. | 307 k jamais exercés en phase 6. | E-01, E-03 |
| 10 | **Un lecteur neuf pour le lot A**, proposé au début de l'audit. | Je suis de la même famille de modèles que les agents des runs. | limite de l'audit |

---

## 7. Un ordre possible, non intégré

1. **Trancher** les décisions 1 à 3. Aucun fichier ne change.
2. **Mesurer** : un run sur la révision livrée (décision 4), avec les largeurs corrigées et le journal réparé (5 et 7), parce qu'un run mesuré avec des instruments faux ne vaut pas son coût.
3. **Alléger**, seulement ensuite, et seulement ce que les runs montrent comme non lu ou redondant (lignes de force 4.3 et 4.4).

**Critère de réussite.** Après l'étape 2, vous savez dire, pour un brief au moins, si la révision livrée fait mieux, pareil ou moins bien que la référence, et à quel coût.

**Critère d'arrêt.** Si la réponse à la décision 1 est « mieux que sans le système » et qu'une nouvelle série de paires ne le montre pas, la question n'est plus quoi ajouter, mais ce qu'il faut garder.

---

## 8. Limites de cet audit

- **Un seul auditeur, de la même famille que les agents des runs.** Ma lecture de ce qu'un agent comprend d'un texte est partiale par construction. C'est la raison de la décision 10.
- **Aucun run lancé.** Tout ce qui touche au comportement des agents vient des traces, des fiches et du suivi.
- **Treize fichiers lus par extraits** : huit fichiers de tests, deux validateurs de gouvernance, trois fichiers du lot F. Les tests ont tous été exécutés.
- **Lignes très longues lues coupées** dans les validateurs, la gouvernance et une partie des guides.
- **Le suivi avant l'entrée 14.32 n'a pas été relu.** Les transcriptions et les journaux bruts ne sont pas dans l'archive.
- **Les captures mobiles des runs n'ont pas été regardées**, ni les planches d'esquisses.
- **Mes observations sur les pages ne sont pas des verdicts.**
- **L'audit du 11 novembre a été écarté**, comme vous l'avez demandé. Je n'ai donc pas vérifié si ses constats recoupent ceux-ci.

---

## 9. Les documents de l'audit

| Document | Contenu |
|---|---|
| `Plan_Audit_neuf_Design_Governance.md` | Plan, méthode, format des constats |
| `Registre_couverture_audit_neuf.md` | Fichier par fichier : vérification, perspectives, constats |
| `Audit_neuf_Lot_A.md` à `Audit_neuf_Lot_G.md` | Les sept rapports, avec lieux exacts et propositions |
| `Audit_neuf_Synthese.md` | Ce document |
