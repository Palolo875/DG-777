# Lot 9c — Propositions

Rédigé le 20 novembre 2026. Base : `R2026-11-15l` (`master` `5d11ab9`). Sources : PILOT 9b et recherche double (Exa et WebSearch). Aucun run.

Règle 1 : rien n'est intégré sans décision. « D'accord » vaut pour les options A partout.

## 1. Mesure

### Ce que les traces des quatre runs montrent

| Objet | Ce qu'ont estimé les agents | Ce qu'ils ont fait |
|---|---|---|
| Invitation | **17k** et **17l** donnent **la même modale** (fond crème, serif italique, terracotta, environ 45 %) et **la même modale au second degré** (l'enveloppe, 15 à 20 %). | Les deux gardent **la même idée** : un émail céladon qui coule et s'arrête sur le grès nu. 17l l'estimait à **environ 8 %**, et elle venait de son tirage. |
| Widget | **18l** nomme comme modale au second degré les « feux de port » (15 %). | **18k** choisit justement « Le feu du seuil ». **18l** garde « Fenêtre du seuil » (estimée à 8 %), avec la même structure que 18k : le créneau en tête, la courbe avec la ligne du seuil, le phare de Ploumanac'h en fond d'écran. |

**Certain.** Une idée qu'un agent estime rare (environ 8 %) est produite par l'autre agent sur le même brief. Les probabilités annoncées ne prédisent pas ce que fait un autre agent.

**Probable.** Les deux agents prennent la piste « sa forme ou un attribut qui le signe » par son attribut **le plus saillant** : la glaçure pour la céramique, le feu d'entrée pour un port. La piste diversifie la forme, pas le choix de l'attribut.

### Recherche

| Source | Ce qu'elle dit | Ce que ça touche |
|---|---|---|
| Jiang et al., *Artificial Hivemind*, NeurIPS 2025 (Datasets and Benchmarks) | Sur des questions ouvertes, un même modèle se répète, et des modèles différents convergent vers les mêmes idées (« time is a river »). | La convergence entre agents est un phénomène connu. |
| Schaeffer et al., arXiv 2609.33936, 2026 | Réévalue la mesure : l'effet est réel mais plus petit que dit, et **le prompting augmente bien la diversité**. | Une intervention au moment de la génération peut aider : une consigne suffit, pas besoin de réentraîner le modèle. |
| SelfReflect (arXiv 2505.20295) ; Looking Inward (ICLR 2025) ; Speak vs Know (arXiv 2610.27648) | Les modèles résument mal leur propre distribution de réponses. **Échantillonner puis résumer** donne un résumé fidèle. L'introspection marche sur des tâches simples et échoue sur des sorties longues. La réponse la plus probable selon le modèle diffère de ce qu'il produit réellement dans 37 % des cas. | Estimer la modale au second degré par une phrase n'est pas fiable. **L'observer** est mieux. |
| Deng, Brucks & Toubia, arXiv 2602.20408, 2026 | En idéation, les LLM se fixent sur leurs premières idées. Combiner plusieurs stratégies dépasse la diversité humaine. | La première idée est un échantillon de la modale, pas une idée rare. |

## 2. Propositions

### P1 — La modale au second degré s'observe, elle ne s'estime pas

**Mesure** : section 1. La règle est dans `DIR-LEVIERS`, au noyau : « nomme aussi la modale au second degré, l'idée astucieuse que tout agent trouverait ».

**Options.**
- **A (recommandée).** Avant les pistes, l'agent écrit sa **première idée astucieuse**, telle qu'elle vient : c'est elle qui est déclarée modale au second degré. Il prend ensuite l'attribut le plus saillant du sujet et le traite comme une autre modale : une piste de forme ou d'attribut part du **deuxième** attribut qui signe le sujet, pas du premier. Les probabilités restent un ordre de grandeur, jamais une preuve de rareté. Coût : environ 200 octets au noyau, sur les 401 qui restent.
- **B.** Seulement la première idée observée, sans la règle sur l'attribut.
- **C.** Rien.

### P2 — Une trace des idées qui convergent (hors paquet d'abord)

**Options.**
- **A (recommandée).** Tenir dans le suivi, pas dans le paquet, un registre des **idées** qui ont convergé entre runs : brief, idée, runs concernés (« céramique : la glaçure qui coule et s'arrête sur le grès nu » ; « marées : créneau en tête, phare en fond »). On décidera de l'entrer au paquet quand il aura plusieurs entrées, parce que deux exemples taillés pour un brief seraient des règles locales.
- **B.** L'ajouter dès maintenant à `SAVOIR/TOOLS/CONVERGENCE`, à côté des vagues de style datées.

### P3 — C-1 et C-2 : la fiche de mobilisation ne compte plus une lecture prescrite comme un manque

**Mesure, reproduite sur le journal du run 17l.** La fiche range sous « Manques » huit routes du tronc écrites avec `--tronc … --fichier`, et trois autres sous « sortie redirigée vers un fichier : lecture non observée ». Or la règle de vitesse du noyau demande justement d'écrire le tronc dans un fichier puis de le lire. Le code est dans `scripts/journal_mobilisation.py`, lignes 328 à 334.

**Options.**
- **A (recommandée).** Séparer les cas :
  - **écrit dans un fichier** (`--fichier` ou redirection) : nouvelle rubrique « Lu hors journal, non observable », hors des manques ;
  - **filtré ou jeté** (`| head`, `> /dev/null`) : reste un manque.
  - Les tests de `test_journal_mobilisation.py` sont mis à jour, avec une mutation rouge.
- **B.** Garder la classification et changer seulement le libellé.

## 3. Hors de ce lot

- **B-4 et B-5** (sources d'images, référence en `STANDARD`).
- **E-1 et E-2** (voix du designer dans la page, polices à la mode) : le carnet de goût d'abord.

## 4. Ordre proposé

1. Décision de Junior sur P1 à P3.
2. Intégration sur une branche, tests avec mutation rouge, préparation complète, puis révision `R2026-11-15m`.
3. Pas de run tant que Junior ne le demande pas.
