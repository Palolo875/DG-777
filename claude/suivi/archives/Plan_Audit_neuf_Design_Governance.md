# Plan — audit neuf de Design Governance V1, R2026-11-13c

13 novembre 2026. Document hors du paquet, à joindre à l'archive de reprise avec `Registre_couverture_audit_neuf.md`.

## 1. Objet

Un audit à neuf de tous les fichiers du système, sous plusieurs points de vue, sans rien négliger.

**Ce qu'il n'est pas.** Il ne s'appuie ni sur l'audit du 11 novembre ni sur celui du 13 novembre (`Audit_Design_Governance_R2026-11-13c.md`). Leurs constats ne servent pas de preuve : chacun se retrouve à neuf dans les fichiers, ou tombe.

**Ce qu'il ne fait pas.** Il n'intègre rien au système. Il produit des constats et des propositions, à discuter et à décider.

## 2. Décisions prises (13 novembre)

| Sujet | Décision |
|---|---|
| Périmètre | Les 149 fichiers suivis du dépôt, lus en entier |
| Points de vue | Les sept de la section 3 |
| Rythme | Un lot à la fois, arrêt et discussion après chaque lot |
| Lire ou exécuter | Les deux : validation complète, tests, outils sur des pages pièges |
| Runs et rendus | Dans le périmètre (lot G), bien qu'ils soient hors du paquet |

**Ouvert.** Un lecteur neuf pour le lot A (un agent qui reçoit le paquet seul, sans le suivi ni les audits). Non lancé tant que tu ne le demandes pas.

## 3. Les sept points de vue

| Code | Point de vue | Question posée à chaque fichier |
|---|---|---|
| A | L'agent qui exécute | Est-ce lisible, applicable, sans ambiguïté ni contradiction, au moment où il le lit ? |
| D | Le designer senior | Le savoir est-il juste, complet, au niveau professionnel ? Que manque-t-il ? |
| P | La personne qui demande | La promesse, les guides et la réponse reçue sont-ils clairs et tenus ? |
| M | Le mainteneur | Propriétaire unique, redondance, budgets, cycle de vie des essais |
| I | L'ingénieur | Les scripts mesurent-ils juste ? Robustesse, cas non testés, faux positifs |
| V | La preuve | Qu'est-ce qui est prouvé, affirmé, ou jamais éprouvé ? |
| T | L'intégrité | Vérité, droits, licences, accords, mémoire |

Tous les points de vue ne s'appliquent pas à tous les fichiers. Le registre note ceux qui ont été appliqués à chacun.

## 4. Les lots

| Lot | Contenu | Fichiers | Taille | Points de vue dominants |
|---|---|---|---|---|
| A. Chemin de l'agent | `SKILL.md`, `agent/`, `sections/`, `design/direction/`, `design/README.md` | 17 | 209 k | A, D, M |
| B. Savoir de design | `design/savoir/`, `design/formes/`, `design/produit/` | 22 | 295 k | D, A, T |
| C. Outils de rendu | `parcours.py`, `check_render.py`, `regard.py`, `planche.py` et leurs trois tests | 7 | 442 k | I, V |
| D. Navigation, validation, livraison | Le reste de `scripts/` | 17 | 411 k | I, M |
| E. Gouvernance | Documents, schémas, exemples, fixtures, deux validateurs | 44 | 307 k | M, T, V |
| F. Présentation et maintenance | `README.md`, `RELEASE_NOTES.md`, guides, références, maintenance, supports, CI | 42 | 249 k lus, 572 k vérifiés autrement | P, M |
| G. La preuve | Runs, traces, fiches, rendus ouverts au navigateur, mesures refaites | hors paquet | — | V, D |
| H. Transversal et synthèse | Validation complète, `pytest`, contradictions croisées, simulation d'un run de bout en bout | — | — | tous |

**Ordre proposé.** A, B, C, D, E, F, G, H. Le lot A passe en premier parce que c'est ce que l'agent lit d'abord ; les lots C et D sont les plus lourds.

**Fichiers vérifiés autrement que par lecture** (11 sur 149) : les six cartes SVG et les trois pages HTML générées se vérifient en les régénérant et en comparant ; les deux polices par leur licence et leur couverture.

**Ordre de grandeur.** La lecture seule représente environ 600 000 jetons. Elle ne tient pas dans une session : compter plusieurs sessions.

## 5. Méthode d'un lot

1. **Lire** chaque fichier du lot en entier, dans l'ordre du registre.
2. **Noter** les constats au fil de la lecture, au format ci-dessous.
3. **Exécuter** ce qui se vérifie par l'exécution (une commande citée, un test, un outil sur une page piège).
4. **Remplir le registre** : date, points de vue appliqués, identifiants des constats.
5. **Écrire le rapport du lot** dans son fichier, puis s'arrêter pour discussion.

**Format d'un constat.**

| Champ | Contenu |
|---|---|
| Identifiant | Lot et numéro : `A-01` |
| Lieu | Fichier et ligne, ou adresse de route |
| Point de vue | Un code de la section 3 |
| Constat | Ce qui est observé, en une ou deux phrases |
| Statut | **Certain** (lu ou mesuré), **probable**, **hypothèse**, **à vérifier** |
| Poids | **Bloquant**, **important**, **mineur** |

Les propositions sont séparées des constats, à la fin du rapport de lot, et aucune n'est intégrée.

## 6. Ce qui garantit que rien n'est négligé

- **Le registre de couverture** : une ligne par fichier. L'audit n'est complet que lorsque les 149 lignes portent une date.
- **Un lieu par constat** : pas de constat sans fichier et ligne.
- **Aucun constat hérité** : un constat des audits précédents ne compte que s'il est retrouvé.
- **Un fichier sans constat se dit** : « lu en entier, rien à signaler », avec les points de vue appliqués.
- **La section « non vérifié »** de chaque rapport de lot.

## 7. Critères

**Réussite de l'audit.**
- 149 fichiers sur 149 faits au registre.
- La validation complète avec navigateur et `pytest` relancés au lot H.
- Une synthèse qui répond point de vue par point de vue, avec les constats classés par poids.

**Arrêt d'un lot.**
- Si le lot dépasse la session, il se coupe à une frontière de fichier ; le registre dit où reprendre.
- Si des constats se répètent pour une même cause, ils se regroupent sous cette cause au lieu de s'empiler.

**Hors périmètre.** Toute modification du paquet, tout nouveau run d'agent.

## 8. Livrables

| Fichier | Rôle |
|---|---|
| `Plan_Audit_neuf_Design_Governance.md` | Ce plan |
| `Registre_couverture_audit_neuf.md` | Les 149 fichiers et leur avancement |
| `Audit_neuf_Lot_A.md` à `Audit_neuf_Lot_H.md` | Un rapport par lot |
| `Audit_neuf_Synthese.md` | La synthèse, à la fin |

## 9. Reprise entre sessions

Déposer dans la nouvelle session l'archive de reprise, ce plan, le registre et les rapports de lots déjà écrits, puis dire : « Lis le plan de l'audit neuf et le registre, puis continue au lot suivant. » La session ne lit pas les audits précédents avant d'avoir fini son lot.
