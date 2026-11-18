# Lot 6 — Adoption des essais : propositions

15 novembre 2026. Révision de départ : `R2026-11-15d`. Document hors du paquet. Rien n'est intégré.

J'ai pris le lot 6 plutôt que le lot 4 bis, pour suivre l'ordre du plan : le lot 4 bis ajoute du savoir, et il vaut mieux l'écrire dans un paquet déjà passé au socle.

J'ai relu les neuf constats dans les fichiers actuels : F-02, F-04, F-12, H-03, B-12, B-13, B-19, D-10 et E-06. La plupart sont **déjà tranchés** par vos décisions du 14 novembre (plan, § 6) ; il reste à les appliquer. **Une seule question reste vraiment ouverte : votre règle 6 (B-12).** Deux autres choix sont des conséquences, à confirmer.

| Sort | Constats |
|---|---|
| Décidé le 14 novembre, à appliquer | F-02, F-04, B-13, B-19, D-10 (socle de la V1, règle 3 « tout sortir ») ; F-12 (règle 7) |
| Résolu par le passage au socle, sans geste propre | H-03 |
| Décidé : gardé tel quel | E-06 (regard externe gardé pour d'autres) |
| À trancher | B-12 (règle 6) ; deux conséquences : statut du socle, essais futurs |

**Ce que cela coûte.**
- **Noyau.** Il ne bouge que si la règle 6 s'applique : il perd alors environ 22 octets, la référence « (Tuch et al., 2012) ».
- **Troncs.** Aucun ne change : aucun ne contient de vocabulaire d'essai.
- **Fiche de version.** Elle passe d'environ 41 k à environ 15 k ; la maintenance gagne environ 6 k pour le mode d'emploi des retraits.

---

## 1. Ce qui s'applique sans choix

### 1.1 Le passage au socle (F-02, H-03, B-19)

**État vérifié.**
- La fiche de version tient 30 lignes d'essai : 28 au statut `PILOT` ou « méthode », aucune adoptée, aucune retirée.
- Dans le savoir, six endroits disent encore le statut d'essai :
  - trois lignes « passage en `ADOPTED` seulement avec un gain observé » dans `qualite-creative.md` ;
  - « Statut de route : `PILOT` » pour l'écriture ;
  - « Méthode en `PILOT` » dans `identite.md` et dans `images-et-sources.md`.
- Ils renvoient tantôt à `evolution.md`, tantôt à `versions.md` : c'est le constat B-19.
- Hors du savoir, « à l'essai » qualifie encore :
  - l'identité de marque, dans le README, les notes de version et le glossaire ;
  - la planche, le regard, le journal et le parcours, dans la maintenance, le guide 3 et l'en-tête de `regard.py`.

**Changement.**
- La section « Sections à l'essai » quitte la fiche de version. Les mentions d'essai sortent du savoir, des guides, du README, des notes et des scripts.
- La phrase d'efficacité reste partout où elle est : « Efficacité : `NOT-VERIFIED` ». Sa garde (LCF-21) reste aussi. C'est votre premier garde-fou.
- Le périmètre garde une phrase de fait. Par exemple, pour l'identité de marque : « sa méthode et sa planche d'épreuve existent ; elle n'a pas encore servi sur un run ». Ce n'est plus un statut d'essai, c'est une limite.

**H-03** (six essais dont la route n'a été ouverte par aucun run) n'a plus d'objet : le socle ne dépend pas des runs. La carte des déclencheurs du lot 4 a déjà vérifié que ces six routes ont un déclencheur.

### 1.2 Chaque section reste retirable (votre deuxième garde-fou)

La colonne « Retrait » de la table devient un mode d'emploi dans `maintenance/evolution.md`, nouvelle section « Retirer une section du socle ».

Chaque ligne y garde ce que la section apporte, sa limite et la façon de la retirer, **sans récit de run**. Chaque procédure est revérifiée contre le paquet actuel. Plusieurs sont périmées : par exemple, « Retirer la section et son adresse lisible » cite des adresses qui n'existent plus depuis le lot S.

Exemple, l'écriture et le contenu :

| | Avant (fiche de version) | Après (maintenance) |
|---|---|---|
| Statut | `PILOT` | — |
| Ce qu'elle apporte, sa limite | Forme et spécificité du texte… Ne juge ni la justesse commerciale, ni la conformité légale, ni la conversion. | Identique. |
| Preuve attendue avant adoption | Contrat de gain réel : runs jugés sur des briefs contrastés… | — (sort avec le statut) |
| Retrait | Retirer la section et son adresse lisible. | Retirer la section `SAVOIR/CRAFT/CFT-06`, ses renvois et ses tests ; relancer la compilation du noyau et la validation. |

Les 30 lignes réécrites vous seront montrées dans le rapport, avant et après.

### 1.3 Les récits de runs sortent (F-04, B-13), règle 3 « tout sortir »

| Lieu | Ce qui sort | Ce qui reste |
|---|---|---|
| Fiche de version, colonnes « couvre » et « preuve attendue » | Les récits : « exécuté sans être demandé par six agents neufs… », « sur un brief joué trois fois »… | Ce que fait la section et sa limite |
| Fiche de version, « Ce qui est vérifié » | Les quatre puces d'état de la preuve : comparaison à l'aveugle, convergence, runs jugés, niveau mesuré | La phrase `NOT-VERIFIED`, plus une phrase d'état : « Les essais internes faits jusqu'ici ne l'établissent pas ; leur relevé est tenu hors du paquet. » |
| `gout-et-tendances.md`, marqueurs de vague (B-13) | « Convergence produite avec le système (29-10-2026, six agents neufs, trois briefs) : … dans six runs sur six », et les autres comptes de runs | La liste des marqueurs et des convergences, dite au présent, avec sa date et sa source (« essais internes, 09 à 11-2026 ») et son échéance de revue |
| `images-et-sources.md`, repères mesurés (B-13) | « Des pages d'accueil d'agents mesurées de même se tenaient entre 0 et 26 % » | La mesure des cinq pages de produits réelles : c'est un repère, pas un run |
| `evolution.md` (F-04, second cas) | La section « Migration des anciens aliases », le paragraphe qui l'annonce et la garde qui exige les cinq alias | — |

Rien n'est perdu : tout ce qui sort est rassemblé dans un fichier de suivi livré avec le rapport, hors du paquet.

### 1.4 F-12 : les preuves « plusieurs personnes »

Elles étaient dans la colonne « Preuve attendue avant adoption », qui disparaît avec le passage au socle. Rien d'autre à faire. Le regard externe décrit dans la gouvernance reste en place (E-06, votre décision « garder pour d'autres »).

### 1.5 D-10 : les identifiants d'anciens constats dans les scripts

**État vérifié.** Les identifiants qui ne se résolvent nulle part dans le paquet :
- `RET-1` à `RET-6` ;
- `INV-C1-1`, `INV-B2-9` et cinq autres ;
- `F-DIR-005`, `C6` ;
- `C8 O-1` à `O-4`, `E1 O-1` ;
- « règle A2 », « migration (12.04) » ;
- la colonne « constat » de `ROW_NEEDLES` (« C04 »…).

Ils sont répartis dans sept scripts.

**Changement.** Chacun est remplacé par sa raison en clair, ou par la route propriétaire quand elle existe.

Les noms de cas définis dans le fichier même restent : `U-22`, `B1-3a`, `LCF-23`. Ils se lisent sur place et servent d'étiquettes de test.

### 1.6 Une incohérence à corriger au passage

La recette de maintenance dit : « Une modification substantielle est exercée sur un run réel avant adoption élargie. » Le socle est prononcé sans run.

Je propose : « Une nouvelle route est exercée sur un run réel avant de quitter `PILOT`. » Cette formulation reste vraie pour l'avenir, et elle ne prétend rien sur le socle.

---

## 2. Ce qui se décide

### 2.1 B-12 — votre règle 6

**État vérifié.** Six lieux nomment une provenance.

| Lieu | Ce qui est nommé | Nature |
|---|---|---|
| `fondements.md` et le noyau | « (Tuch et al., 2012) » après la première impression | Auteurs d'un principe |
| `qualite-creative.md`, émotion | « Ces trois niveaux viennent de Donald Norman (*Emotional Design*, 2004) » | Auteur d'un principe |
| `qualite-creative.md`, couleur | « OKLab (Ottosson, 2020) », « contrastes de couleur de Johannes Itten » ; WCAG 2.2 | Auteurs ; une norme |
| `interface.md`, flux d'engagement | Un accord d'Amazon avec la FTC (2025), en `[VEILLE]` | Précédent nommé |
| `images-et-sources.md`, étiquetage | L'article 50 de l'AI Act, le règlement (UE) 2026/1744 | Loi applicable |
| `gout-et-tendances.md`, signaux | Creative Bloq, Dezeen, wwwatch, 925 Studios, en `[VEILLE]` | Source d'une observation datée |

Votre règle dit : les références nourrissent le système comme principes, sans citer leur provenance. Le système dit de son côté qu'une affirmation datée porte sa source et sa date. Les deux se heurtent seulement sur la dernière ligne.

| Option | Ce qu'elle fait |
|---|---|
| **A (recommandée)** | La règle 6 vaut pour les **principes** : aucun auteur, ouvrage, studio ni entreprise derrière une règle de design. Le principe est dit seul. Trois sortes de noms restent, parce que le nom y est le contenu, pas la provenance : les **normes et lois** à appliquer (WCAG, AI Act) ; les **ressources** à atteindre (polices, banques d'images, collections) ; la **source d'une observation `[VEILLE]`**, dite par son type et sa date (« presse design, 12-2025 à 06-2026 »), les titres partant au suivi. Le précédent Amazon devient : « ces motifs sont sanctionnés par les autorités de protection des consommateurs [VEILLE 2026-10] ». En tout : Tuch, Norman, Ottosson, Itten, Amazon/FTC et les quatre titres de presse sortent. OKLab reste, comme nom d'outil. |
| B | Comme A, mais les `[VEILLE]` gardent leurs titres de presse. L'observation reste vérifiable dans le paquet, au prix d'une exception à la règle. |
| C | La règle 6 ne s'applique pas au paquet : les noms restent où ils sont. |

**Pourquoi A.** Elle tient votre règle là où elle a un sens : un principe se défend par ce qu'il fait faire, pas par son auteur. Elle ne touche pas ce que l'agent doit appliquer (une loi) ou atteindre (une ressource). Pour la veille, la date et le type de source suffisent à dire qu'une observation vieillit. Les titres restent consultables dans le suivi.

### 2.2 Le statut des sections versées au socle (conséquence de votre décision)

Le cycle de vie du paquet prévoit déjà un statut qui dit exactement « socle sans preuve de gain » : **`SEED`**, « canonique, sans gain mesuré ». `ADOPTED`, lui, exige un gain observé.

| Option | Changement |
|---|---|
| **A (recommandée)** | Les sections versées au socle prennent le statut `SEED`. Sa définition devient : « route du socle V1 (seed d'origine et sections versées au socle), canonique, sans gain mesuré ». Aucun statut nouveau, et aucune prétention de gain. |
| B | Un statut nouveau, `SOCLE`. Un mot de plus pour la même chose. |

### 2.3 Les essais futurs (F-02 : empêcher la liste de regrossir)

Le constat ne demande pas seulement de vider la liste, mais d'éviter qu'elle se remplisse sans fin.

| Option | Changement |
|---|---|
| **A (recommandée)** | Une nouvelle route entre en `PILOT`, avec au plus **cinq essais ouverts** à la fois `[À ADAPTER]`. Ils sont listés dans la fiche de version, dans une section qui n'existe que s'il y en a. Une garde compte les essais ouverts. Une sixième nouveauté attend qu'un essai soit tranché : versé au socle ou retiré. |
| B | Pas de `PILOT` pour l'instant : toute nouveauté entre directement au socle, avec sa ligne de retrait. C'est plus simple, mais rien ne distingue alors une section éprouvée d'une section jamais exercée. |
| C | Ne rien changer : la liste peut regrossir. |

---

## 3. Vérification prévue

1. Branche `adoption`.
2. Tests :
   - aucune mention de statut d'essai dans le savoir, les guides, le README, les notes ni les scripts, sauf la section des essais ouverts (vide aujourd'hui) ;
   - chaque section versée au socle a sa ligne de retrait, et chaque procédure de retrait nomme des fichiers qui existent ;
   - la phrase d'efficacité `NOT-VERIFIED` reste à ses quatre endroits ;
   - selon les choix : la garde des cinq essais ouverts, avec sa mutation rouge (un sixième), et la garde de la règle 6 sur les principes (aucune citation « (Auteur, année) » hors `[VEILLE]`), avec sa mutation rouge (l'injection de « (Tuch et al., 2012) »).
3. Le noyau ne change que par la règle 6, et les troncs restent identiques.
4. Validation complète avec navigateur, archives régénérées, révision `R2026-11-15e`.
5. Livrés avec le rapport : les 30 lignes avant et après, et le fichier de suivi qui recueille tout ce qui sort du paquet.

**Critère d'arrêt.** Si une procédure de retrait ne peut pas être écrite juste, par exemple parce qu'une section est trop mêlée au noyau pour se retirer proprement, je ne l'invente pas : je m'arrête et je vous la montre.

## 4. Ce qu'il faut me dire

« D'accord, options A partout » suffit. Sinon, pour chaque choix, l'option retenue : la règle 6 (§ 2.1), le statut du socle (§ 2.2), les essais futurs (§ 2.3).
