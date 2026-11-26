# Lot 1 — Instruments justes : propositions

14 novembre 2026. Document hors du paquet. Rien n'est intégré : chaque ligne attend votre décision.

**Fait pour ce document.** Chaque constat du lot a été revérifié dans les fichiers de `R2026-11-13c`. Tous sont encore vrais. Le parcours par défaut a été relancé sur la page de FTX-1 pour lire sa sortie réelle.

**Ce que le lot change.** Du code et des tests dans `scripts/`. Trois lignes touchent un texte du corpus ; elles sont signalées. Aucun effet sur le budget du noyau ni sur celui du tronc.

**Comment répondre.** « D'accord pour tout » suffit si mes recommandations vous conviennent. Sinon, donnez les numéros à changer. Quatre lignes demandent votre choix : elles sont marquées **À trancher**.

---

## 1. Le constat bloquant

### C-01 — Largeurs vérifiées par défaut

**État.** Vrai. `parcours.py:2154` : défaut « 1440,390 ». La recette seule en vérifie trois.

**Proposition.** Le défaut de `verifier` passe à « 1440,768,390 » pour la recette. Les captures, le regard et les signaux de finition restent à 1 440 et 390 px, comme aujourd'hui.

**Test ajouté.** Une page qui ne déborde qu'à 768 px : `verifier` doit la rendre en défaut bloquant.

**Coût.** Environ un tiers de temps en plus sur la partie recette d'un appel, soit une dizaine de secondes.

**Recommandation.** Faire.

---

## 2. Mesures fausses ou trompeuses

| N° | État | Proposition | Test ajouté | Recommandation |
|---|---|---|---|---|
| **C-04** | Vrai (`parcours.py:380-383`) | Une image vectorielle sort de la mesure de densité : elle est nette à toute taille. | Un SVG de 100 px affiché à 600 px ne déclenche rien. | Faire |
| **C-03** | Vrai (`parcours.py:858` et suivantes) | `references` demande 2 560 px à Commons au lieu de 1 280, et le plus grand format permis ailleurs. La fiche écrit pour chaque image « nette jusqu'à N px affichés ». | La fiche porte la largeur utile ; la demande part avec 2 560. | Faire |
| **C-02** | Vrai (`parcours.py:971-1003`) | Voir § 5, **À trancher**. | — | — |
| **C-06** | Vrai (`check_render.py:1022`) | Dans `verifier`, quand l'arbre d'accessibilité nomme tous les contrôles, la réserve « nom accessible non vérifié » est remplacée par « noms calculés : tous nommés ». La recette lancée seule garde sa réserve. | Page aux contrôles tous nommés : plus de réserve dans la fiche du parcours. | Faire |
| **C-15** | Vrai (768 px dans un outil, 700 dans deux) | Une seule fonction de hauteur de fenêtre, seuil à 768 px, partagée par les trois outils. | Les trois outils ouvrent la même fenêtre à 720 px de large. | Faire |
| **C-11** | Vrai (contraste codé deux fois) | `regard.py` emprunte la mesure de contraste de `check_render.py`. | Les tests existants des deux outils restent verts. | Faire, avec prudence : c'est le changement le plus risqué du lot |
| **C-10** | Vrai pour le code | Quand une référence capturée fait moins d'un écran et demi, ou porte un bandeau de consentement reconnu, la fiche le signale : « à regarder avant de s'en servir ». | Une page d'attente simulée porte le signal. | Faire |

---

## 3. Le journal de mobilisation

| N° | État | Proposition | Test ajouté | Recommandation |
|---|---|---|---|---|
| **D-02** | Vrai, reproduit | Le niveau « consultée » devient « servie », avec le nombre de caractères. Avec `--fichier`, la fiche écrit « écrite dans un fichier : lecture non observée ». | Fiche d'un tronc écrit dans un fichier. | Faire |
| **D-01** | Vrai, reproduit dans les deux sens | Le journal cesse d'affirmer une lecture partielle. Il garde un indice, corrigé sur trois points : il lit le filtre de **sa propre** commande et non de la première de la ligne ; il compare `head -N` au nombre de lignes réellement sorties ; il écrit « filtre vu dans la commande », pas « lecture partielle ». | Les cinq cas reproduits à l'audit, dont deux commandes enchaînées. | Faire |
| **G-07** | Vrai : 81 appels sur 81 notés « rien à traiter » | Le journal lit la sortie réelle du parcours : sous-commande lancée, défauts bloquants, réserves, titres des signaux. | Fiche d'un `verifier` qui porte deux signaux. | Faire |
| **D-16** | Vrai | À l'appel de `--tronc`, le journal note la liste des routes du tronc. La fiche compare à cette liste, pas au tronc du paquet présent plus tard. | Fiche produite après un changement de tronc. | Faire |

**Limite à connaître.** Aucun outil ne peut savoir ce qu'un agent a lu. Après correction, le journal dira ce qui a été servi et combien, plus un indice sur un filtre. Il ne dira jamais « lu ».

---

## 4. Renvois, restes et honnêteté des outils

| N° | État | Proposition | Recommandation |
|---|---|---|---|
| **C-13** | Vrai, trois renvois périmés | `regard.py:636, 836` : « Réutilisation située » pointe vers `DIRECTION/REUSE`. `parcours.py:1107` : « Chercher par rôle » devient « Routes par rôle ». | Faire |
| **C-12** | Vrai : l'outil et le savoir ne posent pas la même espace | Voir § 5, **À trancher**. | — |
| **C-14, H-04** | Vrai (`parcours.py:160`) | Voir § 5, **À trancher**. | — |
| **C-17** | Vrai : le tirage lit ses pistes dans la prose d'une règle | La liste des pistes reçoit deux balises invisibles dans sa route ; l'outil lit entre elles. **Touche un texte du corpus**, sans en changer un mot visible. | Faire |
| **C-05, D-06** | Vrai : trois listes de marqueurs | Le validateur lit la liste datée du corpus par la même fonction que l'outil de regard. Une vague ajoutée au corpus est alors protégée et signalée d'un seul geste. Les convergences écrites en prose : voir § 5. | Faire pour le code |
| **D-11** | Vrai | Retirer du compilateur les « colonnes gardées », jamais utilisées. | Faire |
| **D-14** | Vrai | Le résumé de la préparation de livraison affiche les neuf bilans de tests, pas cinq. | Faire |
| **F-07** | Vrai : la recette rend un retour sur la carte du système | Écarter de 4 px le libellé « CONCEVOIR » de « Design » dans le gabarit, régénérer, et faire passer la recette sur les trois pages de supports dans la validation avec navigateur. | Faire |
| **C-07** | Vrai : aucun contrôle de poids | `verifier` affiche le poids du fichier, des images et le nombre de polices, **sans seuil ni signal**. Une information, pas un contrôle : un seuil serait une règle nouvelle, à décider plus tard. | Faire en information seule |
| **C-16** | Vrai, déjà déclaré par l'outil | Aucun changement : la fiche dit déjà « signal faible ». | Écarter |

---

## 5. À trancher

### C-02 — Que mesure la « part de matière » ?

Aujourd'hui elle compte les images, vidéos, canevas et SVG. Une atmosphère codée, un cahier ou un ruban de données construits en HTML comptent pour zéro.

- **Option A, minimale (recommandée).** La mesure garde son calcul et change de nom : « part d'image ou de média, matière codée non comptée ». Le signal ne propose plus de « chercher la matière » quand l'objet de preuve déclaré est construit en code.
- **Option B.** Une seconde mesure, sur capture : part de la page qui n'est pas un aplat uni. Plus fidèle à ce qu'on voit, mais c'est une mesure nouvelle, avec un seuil à régler sans run pour le caler.

### C-12 — Quelle espace dans les guillemets français ?

Le savoir donne deux règles (B-17) et l'outil en applique une troisième.

- **Option A (recommandée).** L'usage typographique courant : espace fine insécable avant « ; ! ? », espace insécable normale avant « : » et à l'intérieur des guillemets. L'outil et les deux passages du savoir s'alignent dessus. **Touche deux textes du corpus.**
- **Option B.** Espace fine insécable partout, comme le fait l'outil aujourd'hui.

### C-14, H-04 — L'outil se présente comme un navigateur

Le téléchargement des polices s'annonce « Mozilla/5.0 … Chrome/124 ». La règle du savoir dit : jamais en masquant son identité.

- **Option A (recommandée).** L'outil s'annonce par son nom. Risque connu : le service de polices de repli répond selon le navigateur annoncé et peut alors servir un format plus lourd. Je le vérifie à l'intégration et vous dis ce que ça coûte avant de livrer.
- **Option B.** Garder l'annonce actuelle et écrire dans le savoir que ce cas technique est une exception voulue.

### C-05 — Les convergences écrites en prose

L'outil de regard ne mesure que les marqueurs écrits sous la forme « Vague N : … ». Les convergences plus récentes (donnée devenue image, grotesque condensée, fiche à filets, capitales espacées) sont en prose : ni listées, ni protégées, ni mesurées.

- **Option A (recommandée).** Les laisser en prose dans ce lot. Les mettre en liste est une décision de contenu : elle se prend au lot 3, avec les autres doublons de marqueurs.
- **Option B.** Les ajouter dès maintenant comme « Vague 4 », en marqueurs « non mesurés » : l'outil les rappelle sans les relever.

---

## 6. Vérification et livraison du lot

1. Une branche `instruments`.
2. Un test par défaut corrigé, écrit avant la correction quand le défaut se reproduit.
3. Validation complète avec navigateur, puis régénération des deux archives.
4. Révision à identifiant neutre, proposée : `R2026-11-14a`.
5. Registre mis à jour : chaque constat du lot passe à « corrigé » ou « écarté, avec raison ».

**Critère de réussite.** Validation verte ; les cinq cas du journal et la page à 768 px sont couverts par un test ; aucun budget touché.

**Critère d'arrêt.** Si l'unification du contraste (C-11) fait bouger un seul résultat de test existant, je l'arrête et vous la rapporte au lieu de régler les tests.

**Ce que ce lot ne fait pas.** Il ne change aucune règle de design, ne touche ni au noyau ni au tronc, et ne dit rien de l'effet sur un rendu.
