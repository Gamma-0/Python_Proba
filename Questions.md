# Réponse aux TD
## TD1
### 2. Image composée uniquement de deux couleurs, pourquoi ?
Le déplacement du robot suit une loi de Bernouilli, soit il se déplace, soit il ne se déplace pas. Ainsi, lors du premier déplacement, on passe d'une distribution uniforme à une matrice contenant deux probabilités : une pour la zone où il ne peut pas se déplacer et une autre pour la zone où il peut se déplacer (où il a également plus de chance de s'y trouver).

### 4. Conclusion liée à sensor_right.
En passant sensor_right à 1 dans l’exemple fournit, , le robot ne se trouve nul part à la fin.
En effet, si l'on regarde ses déplacements et mesures par rapport à la grille, on voit qu'en prenant en compte la probabilité qu'il ne se déplace pas, en se déplacant sur la grille, les couleurs mesurées forment un chemin qui n'existe pas sur la grille.
De ce fait, si l'on considère que le robot peut se tromper en mesurant les couleurs, un chemin peut être trouvé. Dans le cas contraire, si l'on admet que le robot ne peut pas se tromper, les couleurs mesurées forment un chemin qui n'existent pas.
Comme le chemin n'existe pas et que le robot ne s'est pas trompé, alors il est nul part dans la grille.

## TD2
### 1. Déduction sur la matrice P (incertitude).
On peut en déduire qu'au début du test, nous sommes plutôt surs de la position du robot (à 5 près), cependant, concernant la vitesse du robot en x et en y, les conditions initiales sont plutôt obscures, puisque l'incertitude est de 100.

### 2. Evolution de la précision du filtre.
La distribution représentant la position du robot se déplace et s'élargit. Cet élargissement représente une augmentation de l'écart-type de la loi normale, ce qui signifie que la précision du filtre diminue.

### 3.
#### Efficacité de filtre ?
Le test 1 est exempt d'erreur de mesure, le test 2 en contient.
- Erreur de position test 1 : 4.122347013
- Erreur de position test 2 : 5.17399239095

La différence entre l'erreur de position avec et sans erreur de mesure n'est que de 1, les résultats obtenus restent très proches des résultats attendus. Le filtre est donc plutôt efficace
#### Précision du capteur GPS diffère suivant les axes.
Seul l'axe dont la précision change verra son résultat changer. Mais cela affecte l'erreur de position.

### 4.
Augmenter l'incertitude liée au déplacement augmente l'erreur de position. Augmenter la précision (diminuer l'incertitude sur la mesure) fait baisser l'erreur de position.
