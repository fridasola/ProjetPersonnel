# Créé par emily, le 30/12/2024 en Python 3.7
import random

#initialisation
LettreAdmisible=[chr(l) for l in range(97,123)]
print("Vous ne pouvez qu'utiliser des lettres miniscules sans accent")
NbErreur=7
print("Vous avez le droit de vous tromper que",NbErreur,"à partir de maintenant")
Gagnant=False
LettreUtilisees=[]

#Généré le mot à trouver aléatoirement à partir d'un fichier texte
FichierObjets=open('Objets.txt','r')
NumObjet=random.randrange(1,int(FichierObjets.readline()))
for i in range(1,NumObjet):
    MotATrouver=FichierObjets.readline()

MotATrouver=MotATrouver[:-1]
Mot='_' * len(MotATrouver)
FichierObjets.close()
FichierObjets=open('Objets.txt','a')
#Jeu
while not Gagnant:
    l=input("Veuillez entrer une lettre")
    if l not in LettreAdmisible:
        l=int(input("Entrer une autre lettre qui soit en minuscule et sans accent"))
    if l in MotATrouver:
        for i in range(len(MotATrouver)):
            if MotATrouver[i]==l:
                Mot=''.join([l if MotATrouver[i] == l else Mot[i] for i in range(len(MotATrouver))])
    else:
        NbErreur-=1
        LettreUtilisees.append(l)
        print("Non. Vous avez le droit de vous tromper que",NbErreur,"à partir de maintenant")
    print(Mot)
    if NbErreur<0:
        Gagnant=True
        print("Vous avez perdu")
    if Mot==MotATrouver:
        Gagnant=True
        print("Bravo vous avez gagné")
        NouveauMot=input("Pour nous aider à améliorer le jeu veuillez bien entrer le nom d'un objet en minuscule et sans accent")
        Bon=True
        for l in NouveauMot:
            if not l in LettreAdmisible:
                Bon=False
        if Bon:
            FichierObjets.write("\n"+NouveauMot)
FichierObjets.close()
