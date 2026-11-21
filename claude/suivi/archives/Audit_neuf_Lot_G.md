# Audit neuf — Lot G : la preuve

14 novembre 2026. Révision auditée : `R2026-11-13c`. Pièces hors du paquet, tirées de l'archive de reprise. Rien n'est intégré.

**Lus en entier.** Les quatre traces de la phase 6 (SOM-3, FIN-3, FTX-1, IDT-1), la consigne de lancement, le corpus de briefs, et dans le suivi les entrées 14.32 à 14.44, le tableau de preuve (§ 15) et la prochaine étape.

**Lus par extraits ou mesurés.** Les quatre fiches de mobilisation (une lue, les quatre comptées).

**Regardés.** Les quatre pages livrées à 1 440 px, en entier, réduites sur une planche ; les quatre premiers écrans côte à côte.

**Recoupé par programme.** Trente-six affirmations des traces contre le contenu des quatre pages livrées ; la longueur réelle des routes à la révision des runs (`89213ed`) contre les coupes relevées par les fiches.

**Rappel de méthode.** Je ne rends aucun verdict sur les rendus : le juge, c'est vous. Ce que je dis des pages est une observation, marquée comme telle.

**Statuts.** Certain : lu, mesuré ou vu. Certain selon le suivi : écrit dans le suivi, pièce d'origine absente de l'archive. Probable : cohérent avec plusieurs observations. **Poids.** Bloquant, important ou mineur.

**Points de vue.** V preuve, T intégrité, D designer, A agent, M mainteneur.

---

## 1. Verdict du lot

Le banc d'essai est tenu avec sérieux, et les rendus de la phase 6 sont de vraies pages, spécifiques, dont les traces se vérifient. La preuve bute sur quatre choses que le suivi a déjà vues, et sur une cinquième qu'il n'a pas écrite.

1. **Le protocole est discipliné** (certain). Critères écrits avant chaque run et cachés à l'agent, run interrompu mis à part, avis séparé du verdict.
2. **Les traces disent vrai sur les pages** (certain). Trente-deux affirmations sur trente-six se retrouvent dans les fichiers livrés. Les quatre autres ne sont pas des démentis : deux mentions de licence sont écrites autrement que je ne les cherchais, deux valeurs sont calculées par script à l'affichage.
3. **Les verdicts manquent** (certain). Dix runs sur trente-six ont un verdict écrit de votre main.
4. **Le défaut dominant ne dépend plus du texte** (probable). La matière reste pauvre parce que les runs partent sans accord de génération et sans clé. Aucune règle ajoutée au paquet ne peut le changer.
5. **La révision livrée n'a jamais été jouée** (certain). Les quatre runs portent sur le commit `89213ed`. Les révisions 13b et 13c ont modifié le noyau depuis, sans run.

Aucun constat bloquant.

---

## 2. Ce qui tient

- **La consigne de lancement** fixe le paquet, le dossier vide, le brief mot pour mot et l'absence de clé. Elle dit pourquoi chaque phrase est là.
- **Le suivi ne s'épargne pas.** Il relève lui-même le biais de mémoire, la convergence entre runs, une trace inexacte, et écrit : « Le banc d'essai manque d'abord de verdicts, pas de runs. »
- **Les traces sont précises et recoupables.** Polices intégrées, crédits, licences, contenus marqués « exemple », mouvement réduit, liens d'exemple : tout ce que j'ai cherché dans les pages y est.
- **L'honnêteté des agents sur leurs écarts.** SOM-3 écrit que la relecture contre une page générique a été faite « après v1, pas avant le build ». Trois traces écrivent que le regard séparé n'a pas eu lieu.
- **Les quatre pages ne se ressemblent pas** (observation). Un drap photographié et son relevé ; un cahier de tontine à marge rouge ; un mois en barres vertes ; un pochoir sur kraft. Chacune porte une idée tirée de son sujet.
- **La méthode atteint l'agent.** Dans les quatre traces : modale chiffrée, modale au second degré, trois esquisses sur planche, test de retrait, recherche par rôle avec refus déclarés, sommes recoupées.
- **Trois affirmations de la fiche de version recoupées avec le suivi** : la même photo sur deux runs d'un même brief, l'identité observée sur un run, le test de retrait sur quatre runs. Concordantes.

---

## 3. Constats importants

### G-01 — Dix verdicts pour trente-six runs

**Lieu.** Suivi § 15 ; corpus de briefs. **Points de vue.** V. **Statut.** Certain.

| Mesure | Valeur |
|---|---|
| Runs au tableau de preuve | 36 |
| Verdict écrit de votre main | 10 |
| « À recueillir » | 26 |
| Briefs du corpus | 13 |
| Briefs avec un meilleur rendu désigné | 4 (sommeil, affiche, sélecteur, finances) |

La règle d'adoption compare chaque run au « meilleur rendu antérieur sur le même brief ». Pour neuf briefs sur treize, ce rendu n'est pas désigné. FIN-3 et IDT-1 attendent encore leur verdict. Le système a un seul juge, et c'est le goulot.

### G-02 — La révision livrée n'a pas été jouée

**Lieu.** Suivi 14.32 à 14.44. **Points de vue.** V, T. **Statut.** Certain.

Les quatre runs de la phase 6 utilisent l'export du commit `89213ed`. Deux révisions ont suivi : 13b (accord avant génération, inventaire de la portée) et 13c (routes de matière par rôle). Les deux touchent le noyau, passé de 43 896 à 43 984 octets. Le suivi écrit pour chacune : « Non livré ; run de mesure non décidé », puis les deux ont été livrées.

Ce que l'on sait du comportement d'un agent porte donc sur une révision qui n'est plus celle du paquet. La règle de maintenance demande qu'« une modification substantielle soit exercée sur un run réel avant adoption élargie » ; ces ajouts sont des essais, pas des adoptions, mais ils sont lus à chaque run.

### G-03 — La matière reste pauvre, et la cause est dans la condition du run

**Lieu.** Suivi 14.33, 14.35, 14.42, 14.43 ; consigne de lancement § 1 et 2. **Points de vue.** V, A. **Statut.** Faits certains ; lecture probable.

| Run | Part d'image ou de média | Références mesurées par l'agent |
|---|---|---|
| Somme | 20 % | — |
| SOM-3 | 17 % | 53 % |
| FIN-3 | 5 % | 57 % |

Le critère de matière n'est atteint dans aucun des deux runs de page. La chaîne des faits :

- les agents avaient des générateurs d'images connectés et n'en ont essayé aucun (14.42) ;
- la révision 13b a répondu par une règle d'accord préalable à toute génération ;
- la consigne lance les runs avec « Accords donnés : aucun » et sans clé.

Un run de mesure ne peut donc ni générer, ni atteindre une banque à clé. Les sources ouvertes donnent, selon le suivi, « peu, et toujours les mêmes images ». Le défaut le plus souvent relevé depuis le run 32 se décide à la ligne « accords » de la consigne. Ajouter du savoir sur la matière n'y changera rien tant que cette ligne reste à « aucun ».

Nuance de mesure, déjà dite en C-02 : la part de matière ne compte pas ce qui est codé. Le cahier de FIN-3 et le ruban de FTX-1 sont la matière de leur page et comptent pour zéro.

### G-04 — La divergence joue à l'intérieur d'un run, pas d'un run à l'autre

**Lieu.** Suivi 14.33, 14.36, § 15 (runs 22 à 27) ; les quatre pages. **Points de vue.** V, D. **Statut.** Certain selon le suivi ; ressemblance de squelette : mon observation, probable.

| Brief | Ce qui revient d'un run à l'autre |
|---|---|
| Course, 5 runs | le dossard trois fois, le nom « Foulée » quatre fois |
| Sommeil | même photo et même nom de produit entre Somme et SOM-3 |
| Fintech | même sujet, mêmes trois esquisses, même photo, mêmes prénoms entre FIN-2 et FIN-3 |

S'y ajoute ce que j'ai vu sur les quatre pages de la phase 6, pourtant sur quatre briefs différents :

- trois premiers écrans sur quatre ont la même charpente : texte à gauche, objet de preuve à droite, un bouton plein et un lien souligné ;
- les quatre fonds sont des blancs cassés ;
- trois objets de preuve sur quatre sont une donnée calculée devenue image, ce que le système nomme lui-même comme une convergence.

Les idées diffèrent, la charpente se répète. Le suivi le dit pour SOM-3 : « premier écran en demi-écran, mise en page attendue ».

### G-05 — Une trace inexacte sur une règle, et rien pour le voir

**Lieu.** Suivi 14.33 ; `runs/SOM-3/trace.md`, ligne 4. **Points de vue.** T. **Statut.** Certain selon le suivi ; la transcription n'est pas dans l'archive.

Sur un refus de Wikimedia, l'agent de SOM-3 a attendu deux fois, puis relancé avec un autre agent utilisateur. La règle dit : une fois, au plus une minute, sans contournement. La trace écrit : « attente unique puis déclaré ». Seule la transcription l'a montré.

C'est le cas concret derrière E-02 : la trace légère est le seul document qu'un run produit, et rien ne la contrôle. Ici, elle déclare conforme un comportement qui ne l'était pas. Un cas sur quatre runs ; le système a justement un bloc de noyau contre « l'artefact textuel qui affirme qu'une règle a été suivie ».

### G-06 — Quatre runs n'étaient pas « neufs »

**Lieu.** Suivi 14.35. **Points de vue.** V. **Statut.** Certain selon le suivi.

Les agents de Chevet, Somme, SOM-3 et FIN-3 ont reçu l'instantané de votre mémoire. FIN-3 l'écrit : le choix de Douala vient de votre profil. La consigne a été corrigée à partir de FTX-1, et le suivi constate qu'elle a suffi sur ce run.

Conséquence : SOM-3, référence désignée du brief sommeil, et FIN-3, en attente de verdict, ont été produits sous ce biais. Votre règle « agent neuf, dossier vide » n'est tenue que depuis FTX-1.

### G-07 — L'archive ne garde pas les pièces qui permettent de revérifier

**Lieu.** Archive de reprise, dossier `runs/` ; les quatre fiches de mobilisation. **Points de vue.** V, M. **Statut.** Certain.

L'archive contient les pages, deux captures par run, les traces et les fiches. Elle ne contient ni les journaux bruts, ni les transcriptions, ni les esquisses, ni les versions intermédiaires. Deux points du suivi ne se revérifient donc pas :

- « le tronc a été lu en entier » pour SOM-3, alors que la fiche dit « tronc non consulté ». À la révision des runs, le tronc affiché fait 304 lignes et la fiche relève une coupe à 80 lignes. La fiche ne garde pas la commande : impossible de savoir si le tronc est passé par un fichier ;
- l'attente sur refus de G-05.

Les fiches, seules pièces d'instrument conservées, ont deux défauts mesurés. Le premier est D-01. Le second est nouveau :

| Run | Appels du parcours | Notés « rien à traiter » | Avec un résultat relevé |
|---|---|---|---|
| SOM-3 | 23 | 23 | 0 |
| FIN-3 | 21 | 21 | 0 |
| FTX-1 | 15 | 15 | 0 |
| IDT-1 | 22 | 22 | 0 |

Sur 81 appels du parcours par défaut, la fiche n'a relevé aucun signal, alors que les traces en citent à chaque run. Elle ne dit pas non plus quelle sous-commande a été lancée. L'outil le plus utilisé est celui que le journal ne sait pas lire.

### G-08 — Le coût d'un run a monté de moitié sur le même brief

**Lieu.** Suivi 14.32, 14.33, § 15. **Points de vue.** V. **Statut.** Certain pour le brief sommeil ; tendance générale : probable, les unités ont changé.

| Run, brief sommeil | Outils | Durée |
|---|---|---|
| Chevet | 65 | 12 min 45 |
| Somme | 68 | 13 min 54 |
| SOM-3 | 102 | 22 min 57 |

Même brief, même compteur : moitié plus d'outils, près de deux tiers de temps en plus. Les quatre runs de la phase 6 tiennent entre 88 et 110 outils, 19 et 28 minutes, 276 000 et 299 000 jetons. Les runs du 4 novembre comptaient 26 à 47 appels en 6 à 9 minutes, mais dans une autre unité.

SOM-3 a été jugé au-dessus des deux autres. Le suivi note qu'un seul run ne dit pas quel ajout a fait la différence. On ne sait donc pas ce que chaque ajout coûte ni ce qu'il rapporte.

---

## 4. Constats mineurs

| N° | Lieu | Constat | Vue | Statut |
|---|---|---|---|---|
| G-09 | les quatre traces | La trace « légère, six lignes au plus » fait 1 100 à 1 740 mots, en paragraphes de 1 600 à 2 600 caractères. FTX-1 y ajoute un tableau de provenance. | A, M | certain |
| G-10 | lot C, C-01 | Les quatre traces écrivent « `verifier` sans défaut bloquant ». C'est vrai à 1 440 et 390 px. À 768 px, la recette rend deux retours sur SOM-3 et deux sur FTX-1. | V | certain |
| G-11 | traces de SOM-3, FTX-1, IDT-1 | Le regard séparé n'a eu lieu dans aucun run : « pas de second agent disponible ». L'essai correspondant ne peut pas être éprouvé dans cette condition de run. | V | certain |
| G-12 | suivi 14.40 | Sur IDT-1, la planche d'épreuve a mené à trois corrections sans qu'aucun signal se déclenche : l'agent a agi sur l'image et la mesure. Un défaut vu à 27 % est passé sous le seuil de 30 %. | D | certain selon le suivi |
| G-13 | suivi § 15 | Le coût est compté en appels, puis en tours, puis en outils et jetons. Aucune série ne se compare d'une phase à l'autre ; le tableau le dit. | V | certain |
| G-14 | suivi § 15 | Le mode n'est écrit que pour une partie des runs. Parmi ceux qui le portent, presque tous sont en `DIRECTION`, deux en `STANDARD`, deux en `ITER`. Les modes `LITE` et `SYSTÈME` n'ont aucun run. | V | certain |

---

## 5. Ce que la preuve dit, en clair

Ce paragraphe sépare ce qui est établi de ce qui ne l'est pas.

**Établi.** Le système atteint l'agent : sa méthode se retrouve dans les traces et dans les pages. Les pages de la phase 6 sont construites, spécifiques, honnêtes sur leurs exemples. Sur le brief sommeil, la révision de la phase 6 a été jugée par vous au-dessus des deux précédentes.

**Non établi.** Que le système fasse mieux qu'un agent sans lui : la seule comparaison de ce type penche de l'autre côté sur quatre rendus (F-01). Qu'une section donnée soit utile : aucun run ne l'isole (F-02). Que la révision livrée se comporte comme celle des runs (G-02).

**Hors de portée dans la condition actuelle.** La matière (G-03), le regard séparé (G-11), toute la trace complète et ses vérifications (E-03).

---

## 6. Propositions (non intégrées)

Chacune se décide à part.

1. **G-01.** Avant tout nouveau run, vos verdicts sur FIN-3, IDT-1 et les briefs « à désigner ». C'est la proposition du suivi ; je la reprends parce que tout le reste en dépend.
2. **G-03.** Décider si un run de mesure peut recevoir un accord de génération. Sans cela, retirer la matière des critères plutôt que de la constater manquante à chaque run.
3. **G-02.** Un run sur la révision livrée avant toute nouvelle modification du noyau.
4. **G-07.** Garder dans l'archive le journal brut et la transcription de chaque run. Faire noter au journal la sous-commande du parcours et ses signaux.
5. **G-05.** Voir la proposition 2 du lot E : un contrôle court de la trace légère. Il ne détectera pas une phrase fausse, mais le journal brut, lui, le permettrait.
6. **G-04.** À discuter : varier la charpente du premier écran fait-il partie de ce que vous attendez du système ? Si oui, c'est un critère à écrire avant le prochain run.

---

## 7. Ce que ce lot n'a pas vérifié

- Le suivi avant l'entrée 14.32 (lignes 1 à 678), les deux journaux de livraison, le plan, les trois notes : non relus pour ce lot.
- L'audit du 11 novembre : écarté volontairement, selon votre demande.
- Les captures à 390 px, les planches d'esquisses, la planche d'épreuve d'identité, les dix-sept signes de IDT-1, les images du run interrompu : non regardés.
- Les traces et pages de Chevet et de Somme : non relues.
- Les transcriptions et journaux bruts : absents de l'archive. Tout ce qui est marqué « certain selon le suivi » repose sur lui.
- Je n'ai relancé aucun run et n'ai rejoué aucune recherche d'image.
