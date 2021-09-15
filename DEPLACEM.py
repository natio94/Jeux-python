global pion
from TESTDAM2 import plateau
nbPionNoir=0
nbPionBlanc=0
for i in range (len(plateau)):
  for j in range(len(plateau[i])):

    if plateau[i][j]=="N":
      nbPionNoir+=1
    elif plateau[i][j]=="B":
      nbPionBlanc+=1
    while nbPionNoir>0 and nbPionBlanc>0:
      tour="B"
      def deplacement(i_pion,j_pion,i_endroit,j_endroit):
        print("Les Blancs commencent.")
        pion=plateau[i_pion][j_pion]
        endroit=plateau[i_endroit][j_endroit]
        print(pion)
        print(endroit)
        if pion!=tour:
          print("Vous ne pouvez bouger que vos propres pions.")
        if i_pion==i_endroit-1 and tour == "B" and pion=="B" and i_endroit<11 and j_pion == j_endroit-1 or j_pion == j_endroit+1 and i_pion==i_endroit-1 and tour == "B" and pion=="B" and i_endroit<11:
          print("Vous pouvez vous deplacer.")
     #     print("z")
          #tour="N"
        elif i_pion==i_endroit+1 and pion == "N" and tour=="N" and i_endroit>0 and j_pion == j_endroit+1 or j_pion == j_endroit-1 and i_pion==i_endroit+1 and pion == "N" and tour=="N" and i_endroit>0:
          print("Vous pouvez vous deplacer.")
      #    print("u")
          #tour="B"
        else:
          print("Vous ne pouvez pas vous deplacer.")
        if tour=="B":
          print("Tour des Blancs")
      #    tour="B"
        if tour=="N":
          print("Tour des Noirs")
     #     tour="N"
      nbPionNoir-=1
      print(nbPionNoir)
if nbPionNoir==0:
  gagnant="Blancs"
if nbPionBlanc==0:
  gagnant="Noirs"
print("Victoire des "+gagnant)
