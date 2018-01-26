# Réponses TD3
## Exercice 4
### 4.1 Vous devriez maintenant voir à chaque itération les particules avant et après le rééchantillonage, qu’observe-t-on ?
Avant le rééchantillonage, il y a beaucoup de particules dans le monde. Après le rééchantillonage, beaucoup de particules disparaissent. En effet, pour chaque particule, une erreur est calculée en fonction de la mesure du robot et celle de la particule, avec un bruit `measure_noise`.  
Ainsi, les particules dont l'erreur est trop grande sont supprimées pour ne garder que celles dont la position est cohérente.

### 4.2 Simuler une seule itération, puis deux. Comment expliquer la différence de répartion à la fin de la première itération ?
Lors de la première itération, les particules sont uniformément réparties dans le monde. Ainsi, peu de particules sont proches de la position réelle du robot et un rééchantillonage permet d'écarter une grande partie des particules.  
A partir de la deuxième itération, les particules sont plus proches de la position du robot et on obtient une répartition gaussienne de ces particules. Le rééchantillonage des particules supprime moins de particules et le filtre converge vers la position du robot.



## Exercice 6
### 6.1 Que pouvez vous dire de l’importance de ces paramètres ?

#### Marqueurs
Le nombre de marqueurs influe sur la précision du filtre, plus ce nombre est important, plus la position estimée du robot est précise.   
Pour localiser le robot, (trouver un point), il faut au moins 2 marqueurs.  
La position des marqueurs influent peu sur le résultat.


#### Particules
Le nombre de particules influe également sur la précision du filtre, plus ce nombre est important, plus la position estimée du robot est précise.
La position des particules influent peu sur le résultat.

### 6.2 Que se passe-t-il s’il n’y a qu’un seul marqueur (utilisez beaucoup de particules), et pourquoi ?
Il n'est pas possible de localiser le robot avec un marqueur unique, sauf rare exceptions (demi-droite ayant le marqueur pour extrémité).

### 6.3 En particulier, est-ce que placer cet unique marqueur au centre de la salle est une bonne idée ?
Localiser le robot est plus difficile si on place un unique marqueur au centre du monde puisque la variation d'angle est plus rapide.  
Mettre le marqueur à une position aléatoire est plus efficace.
