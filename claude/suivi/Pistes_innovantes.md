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
