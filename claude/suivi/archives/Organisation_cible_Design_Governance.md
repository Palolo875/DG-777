# Organisation cible — Design Governance V1

14 novembre 2026. Révision de départ : `R2026-11-14a`. Document hors du paquet, sur papier : **aucun fichier du paquet n'est modifié par cette étape.**

**But.** Fixer, avant de corriger les textes, l'arborescence, le système de noms, ce qui est livré et les trois parcours d'entrée. Les lots 2 à 8 corrigeront ensuite vers cette cible, pour ne pas corriger deux fois.

**Méthode.** Tous les chiffres viennent des fichiers de `R2026-11-14a`. Les propositions sont marquées comme telles ; quatre décisions vous reviennent (section 7).

---

## 1. Ce qui fait « brouillon » aujourd'hui

Six faits mesurés. Les trois premiers ont une seule et même cause.

### 1.1 Deux noms pour chaque section

| | Codes (`DIRECTION/START`) | Adresses lisibles (`agent/chemins#classer`) |
|---|---|---|
| Nombre | 84 routes de premier niveau | 95 adresses, tenues dans une table du lecteur |
| Citations dans le paquet | 945 | 230, dont 218 dans les guides |
| Lecteur | l'agent, les outils, les validateurs | une personne |

Une personne qui lit un guide voit des adresses ; quand elle ouvre la section, elle y trouve des codes. Elle apprend deux vocabulaires pour une seule chose.

Et dans les guides, ces adresses sont du texte entre accents graves, **pas des liens** : 218 citations, 19 vrais liens. Sur GitHub, une personne ne peut pas cliquer pour aller à la section ; il lui faut le lecteur en ligne de commande.

### 1.2 Le code ne dit plus où vit la section

Les préfixes des codes (`DIRECTION`, `ACTION`, `SAVOIR`, `BIBLIOTHEQUE`) sont les noms des cinq fichiers d'origine. Les sections ont depuis été rangées par thème. `ACTION/GATE-A` vit dans `design/produit/plancher.md` ; `agent/chemins.md` porte des sections de trois origines.

Pour retrouver une section, le système tient donc :

- une table des lieux de 52 entrées dans le lecteur ;
- 80 marqueurs `<!-- origine:… -->` dans les fichiers ;
- des bandeaux générés en tête de `sections/` ;
- 99 appels à cette mécanique dans 8 scripts.

Déplacer une section demande de mettre la table à jour, puis de régénérer.

### 1.3 Le dossier `sections/` n'est pas ce que son nom promet

« Sections de référence » : on s'attend à y trouver les règles. Il contient 31 k de choses différentes :

- deux blocs du noyau (le rôle, la posture) ;
- la table des routes, dont le lecteur a besoin ;
- des tables de routage qui doublent celles d'ailleurs (constats A-12, F-05, à fusionner au lot 3) ;
- un titre sans contenu (A-19) ;
- des pages « responsabilité » qui redisent les README des dossiers.

### 1.4 Quatorze README

Un par dossier, plus `sections/README.md`, qui fait sommaire général en concurrence avec le README racine.

### 1.5 Les entrées sont longues

| Qui | Entre par | Doit lire avant d'agir |
|---|---|---|
| Une personne | `README.md`, 132 lignes : installation, contenu, règles, limites | puis le niveau 1 des guides, 20 lignes, la vraie entrée |
| Un agent | `SKILL.md`, 213 lignes | plus le tronc de son mode : 78 000 caractères avant le premier rendu en `DIRECTION` |
| Un mainteneur | `maintenance/README.md`, 125 lignes | puis `scripts/README.md`, dont une cellule de table fait 3 842 caractères |

### 1.6 L'installation de l'agent emporte tout

L'export Local, installé chez l'agent : 144 fichiers, 2,45 Mo. Les cartes destinées aux personnes en font 26 %, les tests 10 %, les validateurs 8 %.

---

## 2. Proposition : un nom, trouvé sans registre

### 2.1 Le code reste l'identifiant, et le seul

Le code est déjà ce que lisent l'agent, les outils et les validateurs : 945 citations, le noyau entier. Le changer coûterait tout et ne servirait personne.

- **Les adresses lisibles disparaissent** : la table de 95 entrées, leurs 230 citations, l'option du lecteur.
- **Dans les textes pour les personnes**, une section se cite par **son titre, en lien cliquable** vers son fichier et son ancre : « [Classer avant d'agir](../agent/chemins.md#…) ». Une personne clique ; elle n'a besoin ni du lecteur ni d'un code.
- **Dans les textes pour l'agent**, rien ne change : le code.

### 2.2 Le lecteur trouve la section par son titre

Les titres porteurs d'un code sont déjà uniques dans tout le paquet : un validateur l'exige. Le lecteur peut donc chercher le titre `## ACTION/GATE-A` dans tous les fichiers de règles, sans savoir d'avance où il est.

Ce qui disparaît alors :

- la table des lieux (52 entrées) ;
- les 80 marqueurs de provenance ;
- les bandeaux générés de `sections/` ;
- la table des routes de `sections/READING_MAP.md`, qui devient une liste produite par le lecteur (`--sommaire` le fait déjà).

Ce qui reste : le préfixe du code, comme nom de famille de la règle (décision, livraison, savoir, structure). **Déplacer une section revient à déplacer son texte.**

**Coût, à dire franchement.** C'est le plus gros chantier technique du plan. Le lecteur, le compilateur du noyau et trois validateurs s'appuient sur cette mécanique. Les gardes « une règle vit chez son propriétaire » se fondent sur la provenance ; elles se fonderont sur le préfixe du code de la section qui contient la règle. Environ 600 tests existants servent de filet. Durée estimée : une longue session.

### 2.3 Le dossier `sections/` disparaît

| Ce qu'il contient | Où cela va |
|---|---|
| Rôle et posture (blocs du noyau) | `design/direction/`, avec les cinq règles absolues, dont ils sont la tête |
| Table des routes | produite par le lecteur ; plus de table écrite |
| Routage, chemin de démarrage, sortie minimale | fusion avec leurs propriétaires au lot 3 (doublons déjà relevés) |
| Pages « responsabilité » | les README des dossiers, qui disent déjà la même chose |
| `sections/README.md` | absorbé par le README racine |

---

## 3. L'arborescence cible

```text
README.md            Une page : ce que c'est, les trois portes, installer, les cinq règles, les limites
SKILL.md             L'entrée de l'agent (inchangée, sauf ce que les lots y corrigent)
RELEASE_NOTES.md

guides/              Pour les personnes
  1-utiliser.md        la vraie entrée, vingt lignes
  2-comprendre.md      sujets, combinaisons, angles ; sections citées par liens
  3-maitriser.md
  glossaire.md

design/              Le savoir-faire, inchangé dans son principe
  direction/           + rôle et posture (venus de sections/)
  savoir/
  formes/
  produit/

agent/               Chemins par mode, forme de la réponse
gouvernance/         Trace, preuve, clôture ; schemas/ et outils/
references/          Exemples, recettes de procédé, projection machine (convention Agent Skills)
supports/            Les trois cartes
scripts/             Outils et contrôles
maintenance/         Version, évolution, validation, préparation
```

**Disparaissent :** `sections/` (six fichiers), la table des lieux, les marqueurs de provenance, la table des adresses.

**README :** de quatorze à douze. Les README de dossier restent courts : une phrase de rôle, la liste des fichiers, le retour.

**Ne bougent pas :** les noms des dossiers `design/`, `agent/`, `gouvernance/`, `scripts/`. Les renommer casserait des chemins partout sans rien clarifier.

---

## 4. Les trois parcours d'entrée

### Une personne

`README.md` → [Commencer](guides/1-utiliser.md#commencer) → le niveau 2 si elle veut comprendre.

Le README devient une page d'accueil : ce que fait le système en trois phrases, trois portes (« Je veux un résultat », « Je branche un agent », « Je fais évoluer le système »), l'installation, les cinq règles, les limites. Le détail du contenu du dépôt passe à la maintenance. Cible : **moins de 70 lignes**, contre 132.

### Un agent

`SKILL.md` → `read_route.py --tronc MODE --fichier` → les routes que leur signal appelle.

L'organisation ne change rien à son chemin. Sa charge (78 000 caractères avant le premier rendu en `DIRECTION`) se traite aux lots 3, 4 et 7, pas ici.

### Un mainteneur

`maintenance/README.md` → la recette d'une modification → la validation.

Le mainteneur gagne le plus à la section 2 : plus de registre à tenir. `scripts/README.md` redevient une table lisible, une ligne courte par outil, le détail passant dans l'aide de chaque commande (lot 8).

---

## 5. Ce qui est livré

| Distribution | Contenu aujourd'hui | Proposition |
|---|---|---|
| GitHub | tout | inchangé |
| Local, installée chez l'agent | tout, sauf la préparation et l'intégration continue | voir la décision 3 |

Deux voies honnêtes pour l'export Local :

- **Tel quel.** L'agent garde de quoi valider son installation. 2,45 Mo.
- **Allégé.** Sans les tests et les sources des cartes ; les cartes restent en HTML. Environ 1,5 Mo, plus simple à parcourir. Ce que l'agent perd : les tests du paquet. Les outils qu'il appelle restent entiers.

---

## 6. Ce que cette cible ne change pas

- Aucune règle de design, aucun mode, aucun statut.
- Les codes, le noyau compilé et son budget.
- Les noms des dossiers principaux.
- Les décisions déjà prises : socle de la V1, règle 3, regard externe, fusion des doublons.

---

## 7. Décisions à prendre

1. **Le système de noms** : codes seuls, sections citées par lien dans les textes pour les personnes (recommandé) ; ou garder les deux.
2. **Le lecteur sans registre** : le faire (recommandé : c'est ce qui rend l'organisation simple à tenir) ; ou garder la table des lieux et seulement dissoudre `sections/`.
3. **L'export Local** : tel quel (recommandé tant qu'il n'y a pas eu de run sur l'export allégé) ; ou allégé.
4. **Le moment** : faire le chantier de structure tout de suite, comme un lot à part avant le lot 2 (recommandé : les lots suivants corrigent alors les fichiers à leur place définitive) ; ou à la fin, au lot 8.

---

## 8. Ordre qui en découle, si vous suivez les recommandations

| Étape | Contenu |
|---|---|
| **Lot S, structure** | Lecteur sans registre ; disparition de `sections/`, des marqueurs et des adresses ; liens dans les guides ; validateurs adaptés |
| Lot 2 | Erreurs et contradictions de texte, à leur place définitive |
| Lot 3 | Une seule voix : fusion des doublons, dont les restes de `sections/READING_MAP.md` |
| Lots 4 à 7 | Comme prévu |
| Lot 8 | Passe de livraison : README d'accueil, guides, glossaire, aide des outils ; parcours des trois entrées |
| Lot 9 | Run de contrôle |

**Critère de réussite du lot S.** Validation complète verte ; le lecteur sert les 84 routes depuis leur place, sans table ; déplacer une section dans une copie ne demande que de déplacer son texte (un test le prouve, à la place de l'actuel test de déplacement) ; aucune adresse lisible ni marqueur de provenance ne reste.

**Critère d'arrêt.** Si une garde du système ne peut pas se refonder sur le préfixe du code sans perdre ce qu'elle protège, je m'arrête et vous la montre.
