global plateau
rep=-1
#if rep=2:
#  lignes=int(input("Nombre de lignes : "))
#  colonnes=int(input("Nombre de colonnes : "))
print("Voulez vous jouer au dame(1), au puissance 4 (2), ou au echecs(3)")
rep=int(input())
if rep==1:
  lignes=10
  colonnes=10
  plateau=[[0]*colonnes for i in range(lignes)]
  plateau
  for i in range (len(plateau)):
    for j in range(len(plateau[i])):
      if j%2==1 and i%2==0 and i<4 or j%2==0 and i%2==1 and i<4 :
        plateau[i][j]="N"
      if j%2==1 and i%2==0 and i>5 or j%2==0 and i%2==1 and i>5 :
        plateau[i][j]="B"
from DEPLACEM import *
def affichage():
  for i in range (len(plateau)):
    for j in range(len(plateau[i])):
      print(plateau[i][j],end=" ")
    print()
affichage()
if rep == 2 or rep==3:
  print("En cours de developpement.")
