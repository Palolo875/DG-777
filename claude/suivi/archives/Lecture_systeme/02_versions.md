# Lecture du système, étape 2 : maintenance/versions.md (19 novembre 2026)

Le fichier est lu en entier (83 lignes).

## Ce qu'il dit
- **Le cap.** Trois questions : le système oriente-t-il les choix ? Mobilise-t-il les bons moyens ? Conduit-il au niveau visé ? Elles se jugent « par comparaison avec un travail fait sans lui, sur des demandes comparables ». Et : « Toute évolution du système dit quelle question elle sert et comment on le saura. »
- **Ce que le système sait faire (lignes 39 à 61).** Le texte décrit exactement la séquence que nous avons observée dans les runs : 5 directions avec leurs probabilités, 3 esquisses et la modale, atelier, passe de finition « jusqu'à ce que `verifier` ne laisse aucun signal sans correction ni raison ».
- **Le contrat `EVALUATION_CASE`** porte « la condition (avec ou sans le système), la campagne et le cas apparié, l'évaluateur et son indépendance ». Un gain affirmé doit y citer sa référence. Il est défini dans `gouvernance/schemas/production_contracts.schema.json`. **Le cadre d'une comparaison avec et sans le système existe donc déjà dans le paquet.**
- **Le socle de la V1.** Toutes les sections sont au statut `SEED` : canoniques, sans gain mesuré, et retirables. Une nouvelle route entre au statut `PILOT`, au plus cinq à la fois. Ce cadre permet d'essayer un ajout sans l'intégrer.
- **Ce qui est vérifié.** « Efficacité : `NOT-VERIFIED`. Aucune mesure comparative n'établit une amélioration… Un run avec le système coûte plus de jetons et de temps qu'un run sans lui. »

## Ce que le suivi ajoute (le relevé est tenu hors du paquet)
- **La seule comparaison avec et sans le système date du 29 octobre 2026** (`Audit_Design_Governance_R2026-11-13c.md`, `Audit_neuf_Lot_F.md`, constat F-01) :
  - **Junior a préféré le rendu fait sans le système sur trois briefs sur quatre ;**
  - le run avec le système coûtait **1,7 fois plus** de jetons et **3 à 4 fois plus** de temps.
- **Depuis, rien n'a été remesuré.** Les lots S et 1 à 8b ont été livrés, puis les runs 9 à 16 ont été faits, tous avec le système.
- L'audit relevait déjà que « le cap et la règle d'adoption ne visent pas la même comparaison » (F-03).

## Recherche faite à côté : comment se mesure la qualité d'un rendu de design généré
- **Design Arena** (https://www.designarena.ai/about, https://www.designarena.ai/blog/methodology) :
  - des votes humains à l'aveugle, sur deux rendus anonymes faits à partir du même brief ;
  - des scores calculés par le modèle de Bradley-Terry ;
  - une marge d'erreur (intervalle de Wilson) ;
  - environ 200 comparaisons avant de juger un modèle fiable.
- **Selon une page secondaire** (GenMagic, https://genmagic.co/benchmarks/da-ui), dans la catégorie « UI Component », les dix premiers modèles se tiennent en 48 points Elo, et les modèles Claude récents sont en tête. Ce chiffre n'a pas été vérifié sur le site de Design Arena lui-même.
- **La limite déclarée par ces mesures :** la préférence humaine peut récompenser l'effet tape-à-l'œil.

## Ce que j'en retiens
1. **La question de fond reste la même qu'au 29 octobre** (*correction du 21 novembre : ce point de mesure porte sur une révision d'octobre et ne vaut plus pour la version actuelle ; il n'y a simplement aucune comparaison avec et sans système pour celle-ci*). Les runs 9 à 16 ont jugé le système contre lui-même, jamais contre un rendu sans lui.
2. **Probable :** le modèle seul est déjà fort en composants d'interface (Design Arena, source secondaire). La skill doit donc battre un modèle de base déjà très bon. Cela pourrait expliquer la préférence de trois sur quatre pour le rendu sans le système. C'est à vérifier, pas à affirmer.
3. **La bonne méthode de comparaison est connue, et le paquet en a le contrat :** des paires à l'aveugle, même brief, avec et sans le système, jugées par Junior sans savoir quelle version est laquelle, et assez de paires pour que ce soit plus qu'une impression. Quatre briefs, c'est très peu.
4. **Le statut `PILOT` permettrait d'essayer le kit** (contraintes, spécimens, variantes, comparaison finale) sans l'intégrer, si on le décide.

## Suite proposée
Lire `maintenance/evolution.md` : le cycle de vie, la règle d'adoption et la procédure de retrait. C'est là que se décide comment un essai est adopté ou retiré.
