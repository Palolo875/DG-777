# Lot 2 — Erreurs et contradictions de texte : rapport

15 novembre 2026. Révision de départ : `R2026-11-14b`. Révision livrée : `R2026-11-15a`. Document hors du paquet.

Décision appliquée : « Vas-y », c'est-à-dire les corrections du § 3 des propositions et l'option A pour A-05, B-14, B-18, E-08 et D-09.

## 1. Le sort de chaque constat

| Constat | Sort | Ce qui a changé |
|---|---|---|
| A-05 | Corrigé (A) | La ligne `REGISTRE` (noyau) compose le registre avec les dimensions listées à « Échantillonner ». La table des signaux envoie à `SAVOIR/STYLE` pour un profil de style, une famille, une technique ou un médium, et non plus pour chaque registre. |
| A-06 | Corrigé | `DIRECTION/DOUBLE-LOOP` : la revue sur capture en quatre questions est la grille avant de présenter ; le contrat du premier objet sert sur faiblesse, et en trace complète. « Contrôle des huit dimensions » devient « revue sur capture ». |
| A-07 | Corrigé | `DIRECTION/ASSET-ROUTE` s'ouvre sur l'accord : toute génération, asset ou ancre `ANCHOR-GENERATED`, attend l'accord de la personne, même pour une démonstration. |
| A-14 | Corrigé | Noyau : la déclaration se relit « dès qu'elle est fixée, avant de construire la suite ». |
| A-16 | Corrigé | « Prochaine preuve » partout pour la case de la ligne `RUN` : absolu 4 (noyau), gabarit de `DIRECTION/START`, rappel de l'absolu 4, `NEXT-PROOF` de Gate A, vue d'exécution. « Preuve minimale sans rituel » (FAST-PATH) et la preuve minimale de B1b gardent leur sens. |
| A-17 | Corrigé | `[FORCÉ]`, `[RECOMMANDÉ]` et `[DÉPRÉCIÉ]` sont retirés des légendes. |
| A-18 | Corrigé | « P1 » et « P0–P3 » renvoient à `SAVOIR/TECH`. |
| A-19 | Déjà corrigé | Lot S. |
| A-20 | Corrigé | `identite.md` figure dans la liste du savoir. |
| A-21 | Déjà corrigé | Lot S. |
| A-22 | Corrigé | Fait en grande partie au lot S. La phrase restante sur « les anciennes références de section » est retirée d'`ACTION/ROUTING`. |
| A-23 | Corrigé | `TRUTH/ILLUSTRATIVE` se porte « en trace », avec « à l'écran une mention en langage produit ». La phrase est 6 caractères plus courte qu'avant. |
| B-06 | Corrigé | Un seul quota : deux ou trois requêtes tirées de l'inventaire du sujet, par rôle qui change la décision ; les autres passages y renvoient. |
| B-14 | Corrigé (A) | L'approbation vaut pour une dépendance ajoutée au projet livré. Un paquet installé dans l'environnement de travail de l'agent suit la ligne « script local ». |
| B-15 | Corrigé | Connexion C05 : `DIRECTION/REUSE`. |
| B-16 | Corrigé | `SAVOIR/IDENTITY` renvoie à la planche de grammaire de marque et à la couche `LAYER/BRAND_GRAMMAR`. |
| B-17 | Déjà corrigé | Lot 1. |
| B-18 | Corrigé (A) | La ponctuation (tiret cadratin) passe dans `SAVOIR/CRAFT/CFT-06`, à côté de la micro-typographie française ; le test anti-slop procédural passe dans `SAVOIR/INTEGRITY`. Le texte n'a pas changé, seulement sa place. |
| B-19 | Reporté au lot 6 | Lignes réécrites par la décision « socle de la V1 ». |
| C-12, C-13 | Déjà corrigés | Lot 1. |
| D-09 | Corrigé (A) | `parcours.py` tient sur une ligne courte, suivie d'une table de ses douze sous-commandes. Les trois fichiers propres à la distribution GitHub sont ajoutés, marqués comme tels. Plus aucune cellule ne dépasse 700 caractères. |
| E-05 | Corrigé | Sous la table des conditions de départ : elle décrit la trace complète ; en trace légère, ce que la ligne du mode charge d'abord suffit. |
| E-08 | Corrigé (A) | Le « principe positif de qualité » est retiré des statuts : il redisait la boucle et le noyau. |
| E-13 | Corrigé | `validate_contracts.py` parle français : « valide », puis « contrats de domaine, de recherche, de direction créative, de réalité UI/UX et d'évaluation ». |
| F-03 | Corrigé | README et fiche de version : « un run d'agent neuf l'a parcourue de bout en bout, et elle reste à l'essai ». |
| F-12 | Reporté au lot 6 | Table des sections à l'essai, refaite au lot 6. |
| F-15 | Corrigé | « Paquet » pour Design Governance, dans les guides, la maintenance et les règles (10 occurrences). « Package » reste pour un paquet logiciel. |

## 2. Les gardes ajoutées

Chacune a son test, qui la fait échouer sur le défaut qu'elle refuse (`TextLotTwoTests`, 7 cas).

| Garde | Ce qu'elle refuse |
|---|---|
| Vocabulaire retiré | Le retour de « contrôle des huit dimensions », de « [preuve suivante] », de « preuve minimale et condition d'arrêt », de « porte près de l'objet le marquage » et de « du / le / au / ce package ». Un « package » logiciel reste admis, et ce point a son propre test. |
| Résumés fidèles | La connexion C05 sans `DIRECTION/REUSE`, et une phrase d'accord avant génération qui perd « accord de la personne ». |
| ACC-01 (nouvelle) | Une route de production qui ne dit plus que toute génération, ancre comprise, attend l'accord. |
| Sortie en français | Le validateur des contrats qui reparlerait anglais. |

## 3. Ce qui a été vérifié

| Contrôle | Résultat |
|---|---|
| Noyau compilé | Exactement quatre lignes changent : l'absolu 4, la ligne `REGISTRE`, la relecture de la déclaration et la ligne de la table des signaux. `SKILL.md` : 44 027 / 46 000 octets (+12). |
| Tronc DIRECTION | 34 515 / 35 000 caractères, 5 de moins qu'avant. Les autres troncs ne bougent que de la ligne `NEXT-PROOF` de Gate A (+1 caractère). |
| Sorties du lecteur | 162 sur 220 identiques. Les 58 autres correspondent toutes aux corrections du § 1. S'y ajoutent la révision dans les connexions et la ligne de Gate A présente dans chaque tronc. |
| Trouvabilité | 18/30 et 10/15, inchangés. |
| Tests | Lecteur 105, régressions d'audit 107, budget 18, préparation 10, journal 18. |
| Validation complète avec navigateur, archives | Passe (`preparer_livraison.py --require-browser`, code 0) : recette 79 cas navigateur, regard 39, parcours 141, cartes du système, build reproductible, export Local validé seul, test de déplacement. |

## 4. Livraison

- Dépôt : commit `60df5c2` sur la branche `texte`, fusionné dans `master`. Le contenu de l'archive GitHub est identique à ce commit.
- Dossier `R2026-11-15a/` : archives GitHub (sha256 `a484283d…`) et Local (sha256 `b64cb3c3…`), et le dépôt (`design-governance-depot.bundle`).
- **Un incident pendant la validation, corrigé.** La première passe a échoué sur l'export Local : la nouvelle ligne du README des outils citait `preparer_livraison.py` par son seul nom, et le Local ne contient pas ce fichier. La ligne cite maintenant les chemins complets, marqués « distribution GitHub seulement ». La seconde passe est verte.
- **Bruit connu, toujours laissé au lot 7** : journaux du serveur de test, « journal introuvable ».

## 5. La suite

Le lot 3 : une seule voix, c'est-à-dire la réduction des doublons. Il reprend B-07 (trois listes de rôles d'asset) et le fait que la table des conditions de départ soit une troisième table « par mode » (E-05, avec A-12).
