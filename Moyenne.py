
#-----------------------------------------------------------------------------------------------
#Exercice: Programme qui demande à l'utilisateur 10 notes et affiche la moyenne
#-----------------------------------------------------------------------------------------------

compteur = 0
somme = 0 #ici quand on ajoute un nombre, on la stocke ici et on l'additione avec le prochain
while(compteur<10):#tant que le nombre de note n'est pas egale à 10 faire ce qui suit
  print("Entrez note")
  note = int(input())
  somme = somme + note #la variable somme initialisé à 0 sera le stock de des notes, à somme on ajoute somme(son ancienne valeur) + la note rentrée
  compteur = compteur +1 #Compteur augmente de 1
​
print("la moyenne des notes est",(somme/10),)