# Pistes innovantes — être plus malin plutôt que plus gros

Rédigé le 21 novembre 2026, sur `R2026-11-15o`. Ce sont des pistes à discuter (règle 1). Chacune dit **la preuve sur laquelle elle s'appuie**, **ce qu'elle ne prouve pas** et **son coût**.

## Deux sources vérifiées qui changent l'analyse

**1. Vercel, *AGENTS.md outperforms skills in our agent evals* (27 janvier 2026).**

| Configuration | Taux de réussite |
|---|---|
| Sans documentation | 53 % |
| Skill à la demande | **53 %** (non invoquée dans 56 % des cas) |
| Skill avec consigne explicite | 79 % |
| **Index compressé de la documentation, toujours présent** | **100 %** |

- L'index faisait 8 Ko, compressé depuis 40 Ko sans perte : une ligne par dossier, avec la liste des fichiers.
- Il portait une consigne : « préfère le raisonnement par consultation à ta mémoire ».
- L'agent lisait ensuite le fichier utile.
- **Limite** : c'est du code (API Next.js, tests automatiques), pas du goût.

**2. Anthropic, *Effective harnesses for long-running agents* et *Harness design for long-running apps*.**
- Un agent d'initialisation prépare l'environnement et un fichier de progression.
- Des agents suivants repartent d'un **contexte neuf**, en lisant ce fichier et l'historique git.
- La suite de l'article rapporte que la **remise à zéro du contexte** est devenue essentielle, la compaction ne suffisant pas.
- **Limite** : c'est du développement d'applications, sur de longues tâches.

**Ce que cela corrige dans mon avis précédent.** Le noyau ne doit pas forcément être **plus court en procédure** : il doit devenir **un index compressé et toujours présent**. Toutes les obligations y restent visibles, ce qui supprime le risque « une règle passée dans une commande devient facultative ». Les détails, eux, se lisent au moment voulu. On réconcilie ainsi les deux preuves.

## Les sept pistes

### P1 — Le noyau devient un index compressé avec ses invariants

**Forme visée** : 10 à 12 Ko au lieu de 46 Ko.
- **Les invariants**, une ligne chacun : absolus, toutes les obligations `[REQUIS]`, forme de la trace et de la réponse.
- **La boucle en six étapes**, chacune avec sa commande.
- **L'index des 85 routes**, sous une forme compressée « quand → route » (une ligne par signal, comme Vercel), avec la consigne : « consulte la route plutôt que ta mémoire ».

**Pourquoi c'est malin.** On garde tout visible, on ne rend rien facultatif, on divise par quatre le texte relu à chaque tour, et on rend la bibliothèque **trouvable**. C'est sa vraie faiblesse aujourd'hui : 60 % des routes ne sont jamais touchées.

**Preuve** : Vercel, avec un écart de 47 points. **Inconnu** : l'effet sur le goût.

**Coût** : un lot, sans run pour le construire. Une garde vérifie que chaque route et chaque obligation figurent dans l'index.

### P2 — Le relais à contexte neuf

- Le run se coupe en deux agents. L'agent « direction » cadre, diverge, choisit et écrit un **dossier de reprise** (`dossier.json` : déclaration, choix, chemins, questions ouvertes).
- L'agent « construction et finition » part d'un **contexte neuf** et lit seulement ce dossier, le noyau et la page.

**Gains attendus** :
- un contexte moyen environ divisé par deux, sur le principal poste de coût (tours multipliés par le contexte) ;
- moins de dégradation liée à la longueur du contexte (Chroma) ;
- et l'agent qui finit n'a pas porté toutes les justifications de l'auteur.

**Preuve** : les deux articles d'Anthropic. **Inconnu** : la perte possible de contexte utile au passage de relais.

**Question pour Junior** : la règle 9 dit « un run, un agent neuf ». Un relais compte-t-il comme un run ?

### P3 — L'œil délégué

- Les captures ne restent plus dans le contexte de l'agent principal. Un sous-agent court les lit, sur images seules, avec la consigne existante de `parcours.py critique`, et rend une critique structurée de 300 mots au plus.
- L'agent principal garde **0 à 3 images au lieu de 13 à 29**.

**Bonus** : c'est le « regard séparé » prévu par le système (même modèle, donc nommé « non indépendant »).

**Preuve** : notre mesure, les images pesant 20 à 45 k jetons gardés jusqu'à la fin. **Inconnu** : la qualité d'un jugement par procuration. Les recherches sur les modèles comme juges d'interface donnent environ 59 % d'accord, donc on lui confie l'observation, pas la décision.

### P4 — La modale empirique (contre la convergence)

- Au lieu d'**estimer** ce que tout agent ferait, on le **mesure** : 8 à 10 tirages très courts et parallèles (une phrase de direction chacun, texte seul, modèle léger) sur le même brief.
- On regroupe les tirages, et la direction la plus fréquente est **la** modale à battre.
- C'est ce qui a manqué au PILOT : les deux agents ont trouvé l'émail, que l'un estimait à 8 %.

**Preuve** :
- *Artificial Hivemind* (NeurIPS 2025, relativisé par Schaeffer 2026) ;
- SelfReflect (« échantillonner puis résumer » est fidèle, estimer ne l'est pas) ;
- notre registre des convergences.

**Coût** : quelques milliers de jetons par run, avec un modèle léger.

### P5 — Le carnet de goût devient des spécimens servis

- Chaque choix de Junior (paire de captures, choix, raison) devient un **spécimen**.
- Au moment de choisir sur la planche, `diverger` sert les 2 ou 3 spécimens les plus proches du type d'objet.

**Preuve** : PRISM (le savoir de style tiré de vrais exemples bat le style décrit en texte).

**Limite** : c'est le goût d'une personne. Pour la version publique, il faut un jeu de spécimens neutre et documenté (galeries, prix), et le carnet personnel reste privé.

### P6 — Une évaluation sobre et séquentielle

- **Micro-runs** : premier écran et un état seulement, pas la page entière. Environ 4 à 5 fois moins coûteux, mais le générique sous le premier écran (A-2) n'est pas mesuré : c'est à dire.
- **Modèle** : les deux conditions sur un modèle moins coûteux (Sonnet), et **une** paire de confirmation sur le modèle de référence.
- **Arrêt anticipé** : on s'arrête dès que 2 paires concordent ; on ajoute une paire seulement s'il y a désaccord.
- **Effet attendu** : une réponse à « avec ou sans système ? » pour le prix d'environ 1 à 2 runs complets, au lieu de 7 à 9.

**Inconnu** : un modèle moins coûteux peut changer la taille de l'effet. C'est pour cela qu'il y a une paire de confirmation.

### P7 — Des budgets visibles

Les outils affichent un compteur discret : images lues, appels de `verifier`, captures produites. Ce sont des repères, pas des interdits.

**Preuve** : notre mesure (17k a lancé `verifier` 11 fois et a perdu). **Inconnu** : l'effet sur le comportement.

## Ce que je propose de faire, dans l'ordre

1. **Lot 10A, propreté** : inchangé, sûr.
2. **Lot 10X, prototype** : P1 (noyau en index), P3 (œil délégué), P4 (modale empirique) et P7 (budgets). Tout se construit **sans run** : tests, gardes, mesures sur les pages du PILOT.
3. **Mesure P6** : sans système, `o` et 10X ; en micro-runs, sur un modèle moins coûteux, avec arrêt anticipé et une paire de confirmation. **C'est le seul passage de runs avant la fin**, et il coûte peu.
4. **Selon le résultat** : on généralise ce qui gagne (P2, le relais, en même temps ou juste après), puis la documentation de publication. Le lot 13 complet sert de confirmation finale.

## Décisions pour Junior

1. Une **mesure sobre avant la fin** (P6), au lieu de « tous les runs à la fin » ?
2. Le **relais** (P2) et l'**œil délégué** (P3) : sont-ils compatibles avec la règle 9 (« un run, un agent neuf ») ?
3. Un **modèle moins coûteux** pour l'essentiel des micro-runs, avec une paire de confirmation sur le modèle de référence ?
4. Le **carnet de goût** (P5) : spécimens privés pour toi, et un jeu neutre pour la version publique ?

## Sources

- Vercel, *AGENTS.md outperforms skills in our agent evals* (janvier 2026) : https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
- Anthropic, *Effective harnesses for long-running agents* : https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic, *Harness design for long-running apps* : https://www.anthropic.com/engineering/harness-design-long-running-apps
- Chroma, *Context Rot* (2025) : https://www.trychroma.com/research/context-rot
- Jiang et al., *Artificial Hivemind*, NeurIPS 2025 ; Schaeffer et al., arXiv 2609.33936 (réévaluation)
- SelfReflect, arXiv 2505.20295 ; PRISM, arXiv 2601.11747

---

## Révision du 21 novembre : un système qui s'adapte à son environnement

**Critique de Junior, juste.** P2, P3 et P6 reposaient sur des sous-agents. Or le système doit marcher :
- pour **un agent seul** ;
- dans **un autre environnement**, y compris **sans exécution de code** ;
- pour **une personne sans agent**.

Les sous-agents ne doivent être qu'un accélérateur.

### Règle proposée

**Chaque fonction a un chemin de base qui marche partout. Les moyens plus riches sont des accélérateurs optionnels.**

Ce n'est pas une idée nouvelle pour le système : il a déjà le profil de capacités (`CAPABILITY-PROFILE`) et le tableau « Mode agent seul et preuve dégradée » (`gouvernance/travail.md`). **Mais le noyau ne dit rien du cas sans outils** (vérifié : aucune phrase « sans navigateur » ou « sans exécution » au noyau).

### Quatre profils d'environnement

| Profil | Exemple | Ce qui est possible |
|---|---|---|
| **E1 — Une personne sans agent** | Un designer qui suit la méthode | Lire les guides, l'index, les planches ; faire et juger à la main |
| **E2 — Un agent sans exécution** | Une conversation, avec ou sans fichiers lisibles | Lire le noyau, et peut-être les routes ; écrire le code ; **pas** de capture ni de script |
| **E3 — Un agent seul avec exécution** | Claude Code, Codex, ou moi dans cette session | Tout l'outillage : scripts, navigateur, captures, Internet selon l'environnement |
| **E4 — Un agent qui peut déléguer** | Sous-agents ou appels parallèles | E3, plus le travail en parallèle et les contextes neufs |

L'agent dit son profil sur la ligne `RUN` de la trace : une capacité déclarée, jamais supposée.

### Les pistes revues, du profil E1 au profil E4

| Piste et principe | E1 personne | E2 sans exécution | E3 agent seul avec outils | E4 délégation (bonus) |
|---|---|---|---|---|
| **P1 Noyau-index** : tout l'essentiel visible, le détail à la demande | L'index sert de table des matières | Le noyau seul suffit à faire juste, l'index dit quoi lire si les fichiers sont lisibles | Idem, et les commandes servent les lignes utiles | Idem |
| **P2 Contexte frais** : l'état du travail vit dans un fichier, pas dans la mémoire de la conversation | Une fiche de reprise à remplir | Un bloc « dossier » réécrit en fin de chaque étape, à reprendre si la conversation repart | Un fichier `dossier.json` écrit par les commandes ; les outils écrivent dans des fichiers et n'affichent qu'un résumé ; la compaction de la conversation perd moins | Relais vers un agent neuf qui ne lit que le dossier |
| **P3 Regarder peu et bien** : une image par décision, au bon format | Une planche imprimée | Pas de capture : ce que l'agent n'a pas vu est déclaré `NOT-VERIFIED`, et il pose à la personne une question de vérification précise | Une planche en 1× au lieu de plusieurs captures ; zoom recadré sur un détail ; mesures en texte par les outils | Œil délégué : un sous-agent lit les images et rend 300 mots |
| **P4 Nommer la modale sans l'estimer seul** | Le registre des convergences et des exemples de genre | Le registre des convergences servi en texte : les idées déjà vues par type d'objet, avec date ; la première idée écrite est déclarée modale | Idem, plus une recherche d'images du genre (piste en attente) avec `references` | Tirages parallèles courts pour mesurer la modale |
| **P5 Goût par l'exemple** | La planche de spécimens | Description courte des spécimens dans la route | Planche de spécimens servie au moment du choix | Idem |
| **P7 Budgets visibles** | — | Une ligne au noyau : peu d'itérations, chacune doit changer quelque chose | Compteurs affichés par les outils | Idem |

**P6 (évaluation sobre)** n'est pas une fonction du produit : c'est **notre banc d'essai**. Il peut utiliser des sous-agents, puisque c'est Junior qui organise les runs. Mais l'évaluation finale doit tester **au moins deux profils du produit** : E3 (agent seul avec outils) et E2 (sans exécution). Ainsi, la version publiée n'est pas validée seulement dans le cas le plus favorable.

### Ce que ça change au prototype 10X

1. **P1 d'abord**, avec une section « Sans outils » au noyau : ce qui reste obligatoire, comment déclarer ce qui n'a pas été vu, quelle question poser à la personne.
2. **P2 en version de base** : `dossier.json` écrit et relu par les commandes, et des sorties d'outils courtes (sortie complète dans un fichier). Le relais vers un agent neuf reste en option.
3. **P3 en version de base** : planche unique, zoom recadré ; l'œil délégué reste en option.
4. **P4 en version de base** : le registre des convergences devient un savoir servi en texte, daté, hors des noms de briefs de Junior. Les tirages parallèles restent en option.
5. **Gardes sans run** :
   - le noyau seul couvre toutes les obligations (test du profil E2) ;
   - chaque commande a un équivalent en texte cité au noyau ou dans l'index ;
   - aucune consigne du noyau ne suppose un sous-agent.

### Ce qui reste incertain

- **Un agent sans exécution produit-il un rendu jugeable sans jamais le voir ?** Probablement moins bon. Le système doit le **dire** plutôt que le cacher.
- **Le registre des convergences** (P4, version de base) **vieillit vite**. Il porte une date et une échéance, comme la veille.
- **Tester E2 demande des runs dans un autre environnement** (une conversation sans exécution). Je ne peux pas tous les simuler ici. Ce sera un choix à faire au lot 13.
