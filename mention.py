#-----------------------------------------------------------------------------------------------
#Programme qui donne une mention à une note
#-----------------------------------------------------------------------------------------------


print("Entrez une note")
note = int(input())
Mention1 = "Pas de mention"
Mention2 ="Mention Assez Bien"#assez bien 12 à 13.99
Mention3 ="Mention Bien"#bien 14
Mention4 ="Mention très bien"#tres bien 16 et plus

if note<0 and note>20 :
  print("tricheur")
elif note >= 18 :
  print("Mention du jury")
elif note >= 16 :
  print("Excellent")
elif note >= 14 :
  print("Très bien")
elif note >= 12 :
  print("assez bien")
elif note >= 12 :
  print("Passable")
else:
  print("Echec")
  