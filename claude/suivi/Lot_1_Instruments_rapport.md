# Lot 1 — Instruments justes : rapport

14 novembre 2026. Révision livrée : `R2026-11-14a` (commit `35a89f0`, `master`). Document hors du paquet.

## 1. Résultat

**Validation.** Préparation de livraison complète avec navigateur : `LIVRAISON PRÉPARÉE`, code 0, en 16 min 9 s. Deux constructions identiques. Noyau inchangé : 43 984 octets sur 46 000. Tronc inchangé.

**Tests.** Toutes les suites passent.

| Suite | Avant | Après |
|---|---|---|
| Parcours par défaut | 128 cas | 141 cas |
| Journal de mobilisation | 12 cas | 18 cas |
| Régressions | 98 cas | 101 cas |
| Recette de rendu, regard, lecteur, noyau, préparation | 114 + 65 + 79, 39, 103, 18, 10 | inchangés, tous verts |
| Cartes du système passées à la recette | — | 3 pages, aucun défaut |

**Archives.**

| Fichier | Empreinte SHA-256 (début) |
|---|---|
| `Design_Governance_V1_GITHUB_R2026-11-14a.zip` | `3dc0bac24e8e582d8c11…` |
| `Design_Governance_V1_LOCAL_R2026-11-14a.zip` | `ee7d5021b6f99d3de407…` |

L'export Local a été extrait et rejoué : révision affichée, lecteur fonctionnel, validation Local verte.

---

## 2. Ce qui a été corrigé

### Le constat bloquant

**C-01, largeurs.** `verifier` passe désormais 1440, 768 et 390 px à la recette. Rejoué sur la page livrée de FTX-1 : les deux défauts invisibles jusqu'ici sont relevés (débordement de 1 185 px à 768 px, textes qui se chevauchent). Un test le garde.

### Les mesures

| N° | Correction | Vérifié par |
|---|---|---|
| C-04 | Une image vectorielle sort de la mesure de densité. | un SVG de 100 px affiché à 600 px ne déclenche rien |
| C-03 | Les collections sont interrogées à 2 560 px (Commons, Unsplash), en grand format d'abord (Openverse, Art Institute, Poly Haven). Chaque image porte « nette jusqu'à N px de large affichés », et l'original quand il est plus grand. | test sur une image simulée |
| C-02 | La part d'image s'appelle « image ou média, matière codée non comptée ». Quand l'objet de preuve déclaré est construit en code, la fiche dit que l'écart d'image peut être voulu, au lieu d'envoyer chercher de la matière. | deux tests |
| C-06 | Dans `verifier`, quand l'arbre d'accessibilité nomme tous les contrôles, la réserve « nom accessible non vérifié » est levée et la fiche le dit. | rejoué sur FTX-1 ; test |
| C-15 | Une seule hauteur de fenêtre, seuil à 768 px, partagée par la recette, le parcours et le regard. | test |
| C-10 | Une référence capturée qui fait moins d'un écran et demi, ou qu'un bandeau de consentement couvre, est marquée « à regarder avant de s'en servir ». | page avec bandeau simulé |
| C-07 | La fiche donne le poids du fichier, des images et des polices. Information, sans seuil. | test |

### Le journal de mobilisation

Les cinq cas reproduits à l'audit sont maintenant justes, et chacun a son test.

| Commande | Avant | Après |
|---|---|---|
| `A \| head -3 ; B` | A et B « lecture partielle » | A : filtre vu (`head -3`) ; B : servie |
| `A ; B \| head -3` | A et B « consultée » | A : servie ; B : filtre vu |
| `A \| wc -l` | « consultée » | filtre vu (`wc -l`) |
| `A \| head -200`, route de 78 lignes | « lecture partielle » | servie : le filtre ne coupe rien |
| `--tronc DIRECTION --fichier` | huit routes « consultées » | écrites dans un fichier : lecture non observée |

S'y ajoutent : la destination de la sortie (fichier, `/dev/null`) ; le tronc noté au moment de l'appel, auquel la fiche se compare (D-16) ; la sous-commande du parcours et ses défauts, réserves et signaux, là où la fiche notait « rien à traiter » 81 fois sur 81 (G-07).

Le mot « consultée » a disparu. La fiche dit « servie », et rappelle en tête qu'une route servie n'est pas une route lue.

### Le reste du lot

- **C-12, espaces du français.** Une seule règle, dans l'outil et dans les deux passages du savoir : fine insécable avant ; ! ? et insécable avant : et à l'intérieur des guillemets.
- **C-14, identité de l'outil.** Les polices se téléchargent sous le nom de l'outil, plus sous celui d'un navigateur.
- **C-13.** Trois renvois périmés corrigés, vers `DIRECTION/REUSE` et « Routes par rôle ».
- **C-05, D-06.** La liste datée des marqueurs est lue par une seule fonction, partagée par le regard et le validateur. Une nouvelle garde (VAG-01) échoue si un nom de la liste n'est ni protégé ni déclaré. Trois marqueurs qui n'étaient pas protégés le sont maintenant : brun, libellés mono, repères de recadrage. « Gravures » est déclaré non protégé : les gravures des collections ouvertes sont une matière légitime.
- **D-11.** Les colonnes gardées, jamais utilisées, quittent le compilateur.
- **D-14.** Le résumé de la préparation affiche toutes les suites, y compris celles qui ne sont pas vérifiées.
- **F-07.** Le libellé « CONCEVOIR » ne touche plus le titre « Design » de la carte. Les trois cartes passent désormais la recette dans la validation avec navigateur.

### Les textes alignés

Le README des scripts, la maintenance, le niveau 3 des guides, le glossaire, la fiche de version et un exemple décrivent désormais ce que les outils font réellement : « servie », trois largeurs, poids, largeur utile des images.

---

## 3. Ce qui a changé en route

Je vous les signale parce qu'ils s'écartent de ce que le document de propositions annonçait.

**C-14 : le repli Google Fonts ne fonctionnait pas, avec ou sans l'identité de navigateur.** Vérifié en direct : Google Fonts sert un TrueType complet à l'identité actuelle comme à une identité honnête. L'outil n'acceptait que du WOFF2 et rendait donc toujours « introuvable » par ce repli. Il lit maintenant le TrueType, le déclare comme tel et signale qu'il est plus lourd. Le changement d'identité ne coûte donc rien.

**C-17 : écarté.** La liste des pistes est une phrase à l'intérieur d'un bloc compilé dans le noyau. Des balises invisibles s'y retrouveraient dans `SKILL.md`, à 4 % du plafond. Un test existant échoue déjà si la phrase change de forme : le garde-fou est là.

**C-11 : non fait.** Les deux mesures de contraste ne sont pas écrites dans la même langue : l'une tourne dans le navigateur, l'autre en Python sur capture. Les unifier revient à en réécrire une. C'est hors de la portée d'un lot de corrections. Je propose au lot 5 un test de concordance entre les deux, plutôt qu'une fusion.

**C-05, partie contenu : reportée au lot 3**, comme décidé. Tirer les motifs de protection des noms actuels de la liste aurait affaibli la garde : « Inter » seul, « beige » et « hero SaaS » n'auraient plus été protégés. La liste et ses noms se reprennent avec les autres doublons de marqueurs.

**C-16 : écarté**, comme prévu : l'outil dit déjà « signal faible ».

---

## 4. Ce que le lot a fait apparaître

Trois choses à traiter plus tard, inscrites ici pour ne pas les perdre :

1. **Bruit dans la sortie de la préparation** : des lignes de serveur et de tests passent dans le résumé (« journal introuvable », « GET /propre.html »). Le test du parcours croit couper le journal du serveur mais ne le coupe pas. Lot 7.
2. **Une partie du savoir mentionne encore « gravures » hors date** : c'est voulu, et désormais déclaré. À revoir avec la liste au lot 3.
3. **Le nom accessible n'est calculé qu'à 1 440 px.** La fiche le dit ; un contrôle visible seulement en mobile (un menu) n'est pas couvert. Lot 5.

---

## 5. Sort des constats du lot

| Constat | Sort |
|---|---|
| C-01, C-02 (option A), C-03, C-04, C-06, C-07, C-10, C-12 (option A), C-13, C-14 (option A), C-15 | corrigé |
| D-01, D-02, D-11, D-14, D-16, G-07, F-07 | corrigé |
| C-05, D-06 | code corrigé ; contenu de la liste reporté au lot 3 |
| C-11 | reporté au lot 5 : test de concordance |
| C-16, C-17 | écarté, avec raison |
| H-04 | corrigé (identité de l'outil) |

**Hors du lot, inchangé.** Aucune règle de design, ni le noyau, ni le tronc. Le seul texte normatif touché est la règle des espaces du français, alignée sur celle qui existait déjà.

**Suite.** L'étape « organisation cible » : arborescence, système de noms, ce qui est livré, les trois parcours d'entrée, sur papier, sans modifier le paquet.
