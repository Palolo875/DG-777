# Lecture du système — V1.8.0 (`R2026-11-25k`)

Lecture faite le 26 novembre 2026, avec Junior, après le run 26. Le point de départ est la question de Junior : « Tout c'est ajouts et modifications me fatigue déjà […] explique-moi si nos méthodes, outils, architecture […] sont les bonnes, voire les meilleures possibles. »

Aucune modification du paquet. Aucun run. Ce document consigne ce qui a été lu, ce qui en ressort et les directions possibles, en attente de décision.

## 1. Méthode

- **Lu en entier** : tout ce que l'agent consulte, soit environ 470 ko :
  - `SKILL.md` ;
  - le tronc DIRECTION et l'étape CONSTRUCTION ;
  - `design/` (direction, savoir, formes, produit) ;
  - `agent/` et `references/`, recettes comprises (échantillon de trois, puis l'en-tête) ;
  - `gouvernance/` (95 ko).
- **Lu en partie** :
  - `maintenance/` : fiche de version, cycle de vie et procédure de retrait ;
  - les fichiers racine : README, README.en, CHANGELOG, notes de version, CONTRIBUTING ;
  - les guides 1 à 3 (le 1 en entier, des extraits du 2, le plan du 3) ;
  - un extrait du glossaire et les cartes ;
  - tous les README de dossiers ;
  - les scripts : la liste des commandes de `parcours.py` et le nombre de lignes.
- **Mesure grossière** : pour chaque fichier, nombre de valeurs concrètes (px, %, ms, ratios), de codes de route, de mots de gouvernance et de tournures de précaution, rapporté à 1 000 caractères.
  - Les recettes portent environ 5 valeurs pour 1 000 caractères.
  - Presque tout le reste en porte 0 à 0,5.
  - Les mots de gouvernance sont 3 à 7 fois plus fréquents que les valeurs.

## 2. Constats par couche

| Couche | Part utile au rendu (estimée) | Ce qui est bon | Ce qui pose problème |
|---|---|---|---|
| **Noyau** `SKILL.md` | Moins d'un dixième sur le métier | Posture « Un vrai produit d'abord », « Pousser le geste » | Vocabulaire de gouvernance partout ; une phrase de divergence de 900 caractères ; table des signaux peu servie |
| **Tronc DIRECTION** | Environ un tiers | TYPE, SEQUENCE | Une même idée déclarée quatre fois (noyau, boot, cible, premier objet), plus la déclaration en 9 lignes et la trace en 6 lignes |
| **Étape CONSTRUCTION** | Environ deux tiers | Table des gestes de STATE, CFT-05 (couleur chiffrée), CFT-03, SECTIONS | Le savoir **répare** (symptôme → geste) au lieu de **viser** ; chaque consigne est suivie de sa nuance ; contrat d'OBJECT ; une quarantaine de renvois ; aucune image hors 5 planches |
| **`qualite-creative.md`** | Environ la moitié | CFT-06 (écriture), CFT-01 (inventaire, phrase d'idée, test du concurrent), revue sur capture | Six grilles de revue et une table pour les réconcilier ; ambition en adjectifs ; CFT-04 fait surtout de précautions |
| **Formes** | 30 à 35 % | Table « caractère → leviers → piège » (×2 à ×2,5, ×4, 45 à 65 signes), SEQUENCE, test de trame | Une ontologie (`SUPPORT/…`, `SCENE/…`) plutôt qu'un savoir de composition ; fiches de 450 caractères sans proportion ni image ; contrats de 13 à 17 champs ; catalogue B2B |
| **Savoir (autres)** | 10 à 85 % selon la route | **IDENTITY**, la mieux écrite (livrables, construction, épreuves, seuils) ; CONTEXT ; SOURCE (routes par rôle, atmosphère) ; vagues et moyens | STYLE, CONNEXIONS, ATLAS : correspondances de champs et index de renvois |
| **Direction** | 30 à 50 % | Posture ; déclaration `ASSET` / `COMPOSANT` / `FINITION` ; test de résilience ; prise de brief | Divergence très lourde (inventaire, 5 directions, 4 premiers écrans, sources par piste) ; statuts répétés à chaque absolu ; ancre réduite à 2 ou 3 références par run, quand le réseau le permet |
| **Produit** | 20 à 70 % | Gate C (critère → geste) ; atelier (retrait, intensification, planche, test du produit fini) | **Barre interne** : chaque version se juge contre l'esquisse de l'agent ; regard séparé facultatif |
| **Recettes** | Élevée par recette | `details-composants` (valeurs de finition) ; vérifiées dans le navigateur | « Jamais une apparence » : les grilles sont des boîtes grises, un savoir que le modèle a déjà |
| **Agent, références** | — | Réponse en quatre rubriques ; trace en six lignes | Exemples de runs à trous, « pour qu'ils ne soient pas recopiés » |
| **Gouvernance** | Quasi nulle | Rigueur et honnêteté (pas de faux « vérifié ») ; test anti-slop procédural | Machinerie d'entreprise (états, issues, verdicts, réserves à 7 attributs, regard externe à 8 champs) pour des runs en trace légère |
| **Maintenance, racine** | — | Procédure « Retirer une section du socle », prête | « Efficacité : `NOT-VERIFIED` » ; chaque version du CHANGELOG dit « aucune mesure sur des rendus » |
| **Façades** | — | Navigation propre ; guide 1 très clair ; table des deux boucles dans `design/README.md` | Le nom et la description de la skill mettent la gouvernance en avant ; avertissements répétés ; `references/README.md` périmé (5 recettes citées sur 25) |
| **Scripts** | — | 15 commandes utiles dans `parcours.py` | Environ 5 500 lignes de tests et 5 600 de validation et construction, contre 7 800 d'outils de rendu et de lecture |

Estimation d'ensemble : le savoir de métier directement utile au rendu représente **environ un quart du texte du paquet**. C'est une estimation tirée des lectures, pas une mesure.

## 3. Pourquoi les rendus plafonnent

1. **Aucun canal ne montre le niveau visé, et c'est voulu (certain).**
   - Recettes : « jamais une apparence ».
   - Exemples : des traces à trous.
   - STANDARD : « les exemples du système […] repris tels quels […] sont une convergence ».
   - CFT-00 : l'ambition en adjectifs.
   - Pourtant SOURCE dit : « une description textuelle ne transmet pas seule masse, lumière, densité ».
2. **Le juge est interne (certain).** L'atelier compare l'agent à lui-même ; seul `verifier --refs` compare des chiffres, et seulement si le run a trouvé des références.
3. **L'effort est mal réparti (probable).** La divergence est lourde ; la construction de la page gardée repose sur un diagnostic. Le système a investi là où il était déjà fort (l'idée).
4. **L'accrétion pèse (certain).** Six grilles, trois cadres réconciliés par une table, des formulaires de 12 à 17 champs, des nuances partout. Le système l'écrit : « plus facile à satisfaire qu'à honorer ».
5. **Des contradictions alimentent les défauts observés (probable).**
   - « Objets imprimés de son monde » et la liste « objet du métier » nourrissent le gadget du run 25.
   - « Spontanéité : 1 à 3° » nourrit les blocs inclinés.
   - « Intimité : papier, grain » nourrit le refuge papier + serif du run 26.
   - La vague 2 de CONVERGENCE nomme pourtant ce refuge : « fond beige ou crème, brun, serif de caractère ».
6. **Le refus du goût est fondateur (certain).**
   - « BIBLIOTHEQUE ne devient ni galerie d'assets, ni archive de références visuelles, ni corpus de goût » (`structure.md`).
   - « Le système n'installe pas mécaniquement le goût » (`integrite.md`).
   - « Pas de matériau d'essai dans le paquet » (`CONTRIBUTING.md`).
7. **Le système ne s'est jamais mesuré, alors que sa fiche le demande (certain).** Le « Cap » dit : « Chaque question se juge par comparaison avec un travail fait sans lui, sur des demandes comparables. » Le contrat `EVALUATION_CASE` existe et n'a jamais servi. Vingt lots se sont décidés sur l'impression laissée par un run isolé.
8. **Le cycle de vie ne capte pas nos ajouts (certain).** Il soumet une nouvelle route au statut `PILOT` et à un run réel. Nos lots ont surtout ajouté des lignes et des recettes dans des routes `SEED`, « sans gain mesuré ».

## 4. Ce que le système fait bien

- **Trouver une idée** : tirage, inventaire classé, planche face à la modale.
- **L'honnêteté** : contenu d'exemple, droits, vérité de scène, flux d'engagement, aucune vérification inventée.
- **Quelques routes écrites comme des manuels de métier** : IDENTITY, CFT-06, CFT-05, SECTIONS, SEQUENCE, la table des leviers, `details-composants`.
- **L'outillage de mesure et de comparaison** : `verifier`, planche, `regard`, `identite`.
- **Les deux outils qui manquent en pratique sont déjà là** : `EVALUATION_CASE` pour mesurer, la procédure de retrait pour simplifier.

## 5. Directions possibles (non décidées)

- **A. Banc fixe** : 3 ou 4 briefs identiques à chaque version, couvrant plusieurs types d'objets (site, application, affiche ou invitation, éventuellement identité). Junior les juge côte à côte avec la version précédente et avec des références, à l'aveugle si possible. Le coût est relevé à chaque passage. C'est ce que demande le « Cap ».
- **B. Exemplaires** : par type d'objet, quelques objets de niveau pro jugés par Junior, servis comme cible visuelle et mesurée. Trois points sont à trancher :
  - **droits** : pas d'images tierces dans le paquet ; on peut garder des décompositions et des mesures (`Reverse_2/`) ou fabriquer nos propres exemplaires ;
  - **convergence** : plusieurs exemplaires par type, présentés comme un niveau et non comme un style ;
  - **principes** : le refus du goût et la règle « pas de matériau d'essai » sont à revoir.
- **C. Simplification**, par la procédure de retrait existante :
  - séparer l'appareil de preuve du chemin de création ;
  - alléger la divergence ;
  - retirer les contradictions ;
  - réécrire les routes de registre sur le modèle d'IDENTITY.
- **Dernier geste, si le cap change** : le nom, la description de la skill et les façades.

**Recommandation de Claude** : A d'abord, puisque sans banc on ne saura pas si B ou C aident. Une pause est aussi possible. **Décision de Junior : en attente.**
