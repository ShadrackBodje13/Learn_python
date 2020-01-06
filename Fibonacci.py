#-----------------------------------------------------------------------------------------------
#Exercice: Ecrire un programme qui calcule la 20e valeur de la suite de Fibonacci 
#c'est faire un calcul de sorte que le premier est additionné au deuxieme et le dernier resultat par exemple : 1+1+2(=1+1)+3(=2+1)+5(=3+2)...
#C'est comme un exercice de permutation et d'addition (****)
#-----------------------------------------------------------------------------------------------

a=1
b=1
compteur=2#le compteur commence à deux parce qu'on à deja notre premiere valeur donc si on veut la 20e valeur on fait les 18prochains calculs
while compteur <20:
  somme = a+b
  a=b#a devient b
  b=somme#b devient ma somme
  compteur = compteur +1 #le compteur prend une valeur de plus
print(b)#afficher b
