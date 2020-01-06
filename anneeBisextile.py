
#-----------------------------------------------------------------------------------------------
#Programme qui détece si une année est bisextile
#-----------------------------------------------------------------------------------------------
[ ]
print("Vous voulez savoir si votre année est bisextile ?")
print("Entrez année")
# une année est dite bisextile si le reste de celle ci est = 0
annee = int(input())
print("reste est ")
bisext = annee % 4
bisext1 = annee %400
print(bisext)
print(bisext1)
if bisext == 0 :
  print("Votre année est dite bisextile")
else :
  print("Votre année est non bisextile")
​