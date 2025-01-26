import pygame
import random

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Dimensions de la fenêtre
LARGEUR_FENETRE = 1200
HAUTEUR_FENETRE = 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("Jeu du Pendu")

# Police d'écriture
police = pygame.font.Font(None, 74)
petite_police = pygame.font.Font(None, 36)

# Initialisation des variables du jeu
LettreAdmisible = [chr(l) for l in range(97, 123)]
NbErreur = 7
Gagnant = False
LettreUtilisees = []

# Généré le mot à trouver aléatoirement à partir d'un fichier texte
with open('Objets.txt', 'r') as FichierObjets:
    NumObjet = random.randrange(1, int(FichierObjets.readline()))
    for i in range(1, NumObjet):
        MotATrouver = FichierObjets.readline().strip()

Mot = '_' * len(MotATrouver)

# Fonction pour afficher le texte à l'écran
def afficher_texte(texte, x, y, police=police, couleur=NOIR):
    surface_texte = police.render(texte, True, couleur)
    fenetre.blit(surface_texte, (x, y))

# Fonction pour dessiner le pendu en fonction du nombre d'erreurs
def dessiner_pendu(erreurs):
    if erreurs <= 6:
        pygame.draw.line(fenetre, NOIR, (550, 250), (750, 250), 5)  # Base
    if erreurs <= 5:
        pygame.draw.line(fenetre, NOIR, (625, 250), (625, 100), 5)  # Poteau vertical
    if erreurs <= 4:
        pygame.draw.line(fenetre, NOIR, (625, 100), (725, 100), 5)  # Poteau horizontal
    if erreurs <= 3:
        pygame.draw.line(fenetre, NOIR, (725, 100), (725, 150), 5)  # Corde
    if erreurs <= 2:
        pygame.draw.circle(fenetre, NOIR, (725, 160), 10, 5)        # Tête
    if erreurs <= 1:
        pygame.draw.line(fenetre, NOIR, (725, 170), (725, 200 ), 5)  # Corps
    if erreurs == 0:
        pygame.draw.line(fenetre, NOIR, (725, 170), (700, 180), 5)  # Bras gauche
        pygame.draw.line(fenetre, NOIR, (725, 170), (750, 180), 5)  # Bras droit
        pygame.draw.line(fenetre, NOIR, (725, 200), (700, 210), 5)  # Jambe gauche
        pygame.draw.line(fenetre, NOIR, (725, 200), (750, 210), 5)  # Jambe droite

# Boucle principale du jeu
clock = pygame.time.Clock()
jeu_en_cours = True

while jeu_en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_en_cours = False
        elif event.type == pygame.KEYDOWN:
            l = chr(event.key)
            if l in LettreAdmisible and l not in LettreUtilisees:
                LettreUtilisees.append(l)
                if l in MotATrouver:
                    Mot = ''.join([l if MotATrouver[i] == l else Mot[i] for i in range(len(MotATrouver))])
                else:
                    NbErreur -= 1

    # Affichage de l'état actuel du jeu
    fenetre.fill(BLANC)
    afficher_texte(Mot, 150, 200)
    afficher_texte(f"Erreurs restantes: {NbErreur}", 150, 300)
    afficher_texte(f"Lettres utilisées: {', '.join(LettreUtilisees)}", 150, 400)
    dessiner_pendu(NbErreur)
    pygame.display.flip()

    # Vérification des conditions de victoire ou de défaite
    if NbErreur < 0:
        jeu_en_cours = False
        fenetre.fill(BLANC)
        afficher_texte("Vous avez perdu", 150, 200, couleur=ROUGE)
        dessiner_pendu(0) # Dessiner le pendu complet en cas de défaite
        pygame.display.flip()
        pygame.time.wait(3000) # Attendre avant de fermer la fenêtre

    if Mot == MotATrouver:
        jeu_en_cours = False
        fenetre.fill(BLANC)
        afficher_texte("Bravo vous avez gagné", 150, 200, couleur=VERT)
        afficher_texte("Entrez un nouvel objet en minuscule et sans accent:", 150, 300, police=petite_police)
        pygame.display.flip()

        # Attendre que l'utilisateur entre un nouveau mot
        nouveau_mot_entree = False
        NouveauMot = ""
        while not nouveau_mot_entree:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    nouveau_mot_entree = True
                    jeu_en_cours = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        nouveau_mot_entree = True
                    else:
                        NouveauMot += chr(event.key)

            # Afficher le mot saisi par l'utilisateur en temps réel
            fenetre.fill(BLANC)
            afficher_texte("Bravo vous avez gagné", 150, 200, couleur=VERT)
            afficher_texte("Entrez un nouvel objet en minuscule et sans accent:", 150, 300, police=petite_police)
            afficher_texte(NouveauMot, 150, 400, police=petite_police)
            pygame.display.flip()

        Bon = all(l in LettreAdmisible for l in NouveauMot)
        if Bon:
            with open('Objets.txt', 'a') as FichierObjets:
                FichierObjets.write("\n" + NouveauMot)
            with open('Objets.txt', 'r') as fichier:
                lignes = fichier.readlines()
            nouveau_nombre = len(lignes)
            lignes[0] = f"{nouveau_nombre}\n"
            with open('Objets.txt', 'w') as fichier:
                fichier.writelines(lignes)

    clock.tick(30)

pygame.quit()