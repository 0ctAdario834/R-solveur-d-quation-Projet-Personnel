# Résolveur d'Équations
Ce programme a été réalisé dans le cadre de mon "Projet Personnel".
Il permet de trouver les solutions d'équations quadratiques, valeur absolue, racine carrée et rationnelles.

## Dépendances

Pour exécuter ce programme, vous devez d'abord avoir Python installé, ainsi que la bibliothèque Python "matplotlib".

Cette étape ne doit être effectuée qu'une seule fois.

Téléchargez la dernière version de Python sur : https://www.python.org/downloads/

Une fois Python installé, ouvrez votre terminal et exécutez la commande suivante : `pip install matplotlib`



# Comment Utiliser

Téléchargez le code source et extrayez le fichier ZIP

Pour lancer le programme, exécutez simplement le fichier `run.bat`.


## Sélectionner une équation

Lorsque vous ouvrez le programme, une page d’accueil vous invite à "Sélectionner un onglet pour commencer".
Les onglets se trouvent en haut de la fenêtre (Accueil, Quadratique, Valeur Absolue, Racine Carrée, Rationnelle).
Tous les onglets sont actifs en même temps : il n’est pas nécessaire de les ouvrir ou fermer manuellement à chaque utilisation.
Ils conservent également les valeurs saisies et les réponses lorsque vous passez de l’un à l’autre (les données sont conservées uniquement tant que le programme reste ouvert).

# Equations

Ce résolveur prend en charge 4 types d’équations :

 - Quadratique
 - Valeur Absolue
 - Racine Carrée
 - Rationnelle

En plus de cela, vous pouvez définir le nombre de chiffres significatifs à afficher dans les réponses.
Si vous laissez ce champ vide, le programme affichera simplement autant de décimales que nécessaire.

En haut de l’onglet d’accueil, vous pouvez choisir le format d’affichage des résultats.
Par défaut, les réponses sont affichées en format décimal.

Il est déconseillé de demander plus de 16 chiffres significatifs en format décimal, en raison des limites de précision des ordinateurs (les nombres décimaux ne peuvent pas être stockés parfaitement, ce qui entraîne de petites erreurs d’arrondissement au-delà d’un certain seuil).

## Quadratique

Le programme permet de résoudre une équation quadratique de la forme :

$$
y=ax²+bx+c
$$

Une image de référence est fournie pour illustrer la forme.

Pour saisir les valeurs de votre équation, entrez-les simplement dans les champs prévus.
Si vous ne remplissez pas un champ, la valeur par défaut sera utilisée :
1 pour a, 0 pour b, c et y.

## Valeur Absolue

Le programme permet de résoudre une équation de valeur absolue de la forme :

$$
y=a|bx-h|+k
$$

Une image de référence est fournie pour illustrer la forme.

Pour saisir les valeurs de votre équation, entrez-les simplement dans les champs prévus.
Si vous ne remplissez pas un champ, la valeur par défaut sera utilisée :
1 pour a et b, 0 pour h, k et y.

## Square Root

Le programme permet de résoudre une équation de racine carrée de la forme :

$$
 y=a\sqrt{b\left(x-h\right)}+k
$$

Une image de référence est fournie pour illustrer la forme.

Pour saisir les valeurs de votre équation, entrez-les simplement dans les champs prévus.
Si vous ne remplissez pas un champ, la valeur par défaut sera utilisée :
1 pour a et b, 0 pour h, k et y.

## Rationnelle

Le programme permet de résoudre une équation rationnelle de la forme :

$$
 y=\frac{a}{b(x-h)}+k
$$

Une image de référence est fournie pour illustrer la forme.

Pour saisir les valeurs de votre équation, entrez-les simplement dans les champs prévus.
Si vous ne remplissez pas un champ, la valeur par défaut sera utilisée :
1 pour a et b, 0 pour h, k et y.


## Results box

En bas de chaque onglet de résolution, une zone affiche les réponses obtenues

Le boutton `Copier les résultats` permet de copier tous les résultats actuellement affichés.

Le boutton `Effacer les résultats` efface, comme son nom l’indique, tous les résultats affichés dans la zone.
‎ 
‎ 
‎ 
# ***-** 834*

## License

Code: MIT License  
Documentation and visuals: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)  
See the [LICENSE](LICENSE) file for full details.









