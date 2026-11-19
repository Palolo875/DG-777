# Lecture du système, étape 7 : savoir/qualite-creative.md, CFT-02 à CFT-06 (19 novembre 2026)

Lu : de la ligne 140 à la fin du fichier (335 lignes). Le fichier est maintenant lu en entier.

## Ce qui existe déjà et répond à nos constats
| Constat des runs | Ce que le savoir dit déjà | Où |
|---|---|---|
| Le diagramme pris comme objet principal (A-3) | « Le premier contact peut mettre au premier plan soit un geste ou une promesse, soit un objet de preuve concret. **Aucun des deux ne gagne par défaut.** Privilégie le geste… lorsque le contexte exige… une présence éditoriale. » | CFT-04a, lignes 238 à 251 |
| Une palette non justifiée (E-3) | « Couleur située… prélève les teintes dans l'image ou la matière du produit… **Deux ou trois couleurs tenues valent souvent mieux qu'une palette complète.** » | CFT-05, ligne 265 |
| Une rampe qui invente un ordre (Resource overview) | « Une rampe rouge, orange, jaune sur des catégories sans ordre invente un ordre. » | CFT-05, ligne 301 |
| Le manque de contraste d'échelle | « Échelle et champ calme. Une seule opération poussée loin, par exemple un objet très petit face à un titre très grand. » | CFT-03, ligne 198 |
| La voix du designer dans la page (E-1) | En partie : « étiquettes éditoriales de pure forme », « texte de mobilier ». Rien ne vise expressément le raisonnement de l'agent écrit dans la page. | CFT-06, ligne 319 |
| Varier | « Fais varier **un axe situé à la fois**. » | CFT-02, ligne 164 |

## Vérifié dans les fichiers et les journaux
- **Le noyau (`SKILL.md`), lu à chaque run,** dit 5 fois « objet de preuve ». Il ne contient ni CFT-04a, ni « champ calme », ni « couleur située », ni « deux ou trois couleurs » (0 occurrence de chacun).
- **Journaux des runs 9, 10, 12, 14, 15 et 16 :**
  - **CFT-04a n'a jamais été lu,** alors que les outils l'ont **proposé** 2 à 5 fois dans les runs 9, 10, 12 et 15 ;
  - **CFT-03 et CFT-05 n'ont été lus dans aucun run,** le mien compris.
  - Limite : le journal ne voit que ce qui passe par le lecteur de routes. Un agent qui ouvrirait le fichier directement n'y apparaîtrait pas.

## Recherche faite à côté
- **Vercel**, *AGENTS.md outperforms skills in our agent evals* (27 janvier 2026, https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals) :
  - **dans 56 % des cas, l'agent n'a jamais chargé la documentation disponible à la demande**, et le taux de réussite est resté celui de l'absence de documentation (53 %) ;
  - une consigne explicite fait monter ce taux à 79 % ;
  - un index court **toujours présent dans le contexte** atteint 100 %.
- **Limite :** c'est une affirmation d'éditeur, sans méthode ni données publiées (signalé par https://agentexperience.tech/evidence/ev-0032/). Elle porte sur du code Next.js, pas sur du design.

## Ce que j'en tire (probable, plus solide qu'aux étapes précédentes)
1. **Ce qui manque au goût existe déjà, mais n'est jamais mobilisé.** Le savoir qui répond à nos constats (le contrepoids à l'objet de preuve, la couleur tirée du sujet en deux ou trois encres, le contraste d'échelle, les rampes) se trouve dans des routes « lues selon le signal ». Les runs ne les ouvrent pas, même quand un outil les propose.
2. **Ce qui est toujours dans le contexte gagne.** Le noyau pousse cinq fois vers l'objet de preuve, et son contrepoids n'y figure pas. Ce déséquilibre suffit à expliquer le réflexe du diagramme, sans même avoir besoin de la phrase d'idée (étape 6).
3. **La recherche de Vercel va dans le même sens :** les agents chargent mal ce qui est disponible à la demande, et ce qui est présent en permanence l'emporte. C'est une indication, pas une preuve.

## Conséquence pour les pistes (à discuter)
- **Le levier principal n'est sans doute pas d'ajouter du savoir, mais de rééquilibrer le noyau.** Quelques lignes déjà écrites dans les routes pourraient y monter (« aucun des deux ne gagne par défaut », « deux ou trois couleurs tirées du sujet », « une seule opération poussée loin »), et des lignes de procédure à faible effet en sortir. C'est l'esprit de la règle du README : « une étape qui ne change rien est retirée ».
- **Les « savoirs proposés » par les outils ne sont pas suivis.** Si une route proposée est utile, elle pourrait être servie d'office, par exemple en affichant directement sa ligne clé dans la fiche de `verifier`, au lieu de la nommer seulement.
- Tout cela se teste dans le cadre `PILOT`, en comparant avec et sans le changement, à l'aveugle.

## Suite proposée
Lire `design/direction/premier-objet.md` (`DIRECTION/FIRST-OBJECT`), pour voir comment l'objet de preuve y est formulé et s'il y renvoie à CFT-04a.
