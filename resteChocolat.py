#-----------------------------------------------------------------------------------------------
#Exercice de recap : programme qui demande à l'utilisateur une quantité de chocolat et 
#qui retourne error si il ya moins de 200g de chocolat ou sinon le nombre de gateau possible avec cette quantité, sachant que chaque gateau prend 200g
#-----------------------------------------------------------------------------------------------
[ ]
print("Entrez une quantite de chocolat")
quantite = int(input())
if quantite < 200 :
  print("Error")
elif quantite >= 200 :
  nombre_gateau = int(quantite/200)
  print("vous pouvez faire",nombre_gateau,"gateaux")
  #reste de chocolat restant
  resteChoco = quantite%200
  print("il vous reste",resteChoco,"grammes de chocolat")
​