#-----------------------------------------------------------------------------------------------
#Calcul la factorielle
#-----------------------------------------------------------------------------------------------

compteur = 1
factorielle = 1
print("Entrez un nombre")
nombre = int(input())
while(compteur <= nombre):#Tant que mon compteur est inferieur ou egale au nombre faire
  factorielle = factorielle * compteur #factorielle egale à 
  compteur = compteur+1
print("la factorielle de",nombre,"est ",factorielle)