#-----------------------------------------------------------------------------------------------
#Ecrire un algorithme qui demande en entrée deux variables et qui calcule la puissance des deux variables (a puissance b)(***)
#-----------------------------------------------------------------------------------------------
[ ]
#demande deux chiffres
print("entrez nombre a")
a = int(input())
print("entrez nombre b")
b = int(input())
#on va mettre un compteur qui va faire le calcul de sorte que le calcul se fasse jusqu'à ce qu'on atteigne b
compteur = 0
resultat = 1#parce que la multiplication par 0 sera 0
while compteur <b:
  resultat = resultat * a
  compteur = compteur +1
print(resultat)
#autre solution en python 
#resultat = 5**4