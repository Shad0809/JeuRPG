# ------------------ COMPÉTENCES ------------------

def competence():
    # Affiche les compétences des races
    print("------------- Compétences selon les races -------------\n")

    print("Gamer : L'Esprit AFK")
    print("Effet : Déconnexion Mentale — Lorsqu'il subit des dégâts, le Gamer a une chance")
    print("        d'activer un état qui réduit les dégâts subis de 50% pendant 1 tour.\n")

    print("Repugnant : Le Repoussoir Social")
    print("Effet : Éloignement Forcé — Peut pousser immédiatement une cible proche de 2 cases,")
    print("        sans dégâts et en ignorant la résistance des non-Boss.\n")

    print("Poids lourds : Impact Sismique")
    print("Effet : Onde de Choc — Les ennemis proches doivent faire un jet d'Agilité ou être étourdis 1 tour.\n")

    # Compétences des métiers
    print("------------- Compétences selon les métiers -------------\n")

    print("Le Bio-Purificateur : Purge Vitale")
    print("Effet : Absorption — Inflige des dégâts légers mais soigne le lanceur d'une petite partie du total.\n")

    print("Le Négociateur : Manipulation de Valeur")
    print("Effet : L'Offre Qu'on Ne Refuse Pas — Oblige un ennemi à rater son prochain jet d'attaque ou à cibler un allié précis (si applicable).\n")

    print("Le Mastodonte : Protection Totale")
    print("Effet : Bouclier Brut — Confère un bouclier temporaire de 40 PV pendant 2 tours.\n")

    print("-------------------------------------------------------\n")

    # Pause et retour au menu
    input("Appuie sur Entrée pour retourner au menu...")
    return menu()   # Retourne au menu principal


# ------------------ SÉLECTION PERSONNAGE ------------------

def personnage():
    # Menu des races
    print("Choisissez votre race")
    print("1 - Gamer")
    print("2 - Repugnant")
    print("3 - Poids lourds\n")

    choix = input("Choisis la race: ")

    # Renvoie la race choisie
    if choix == "1":
        return "Gamer"
    elif choix == "2":
        return "Repugnant"
    elif choix == "3":
        return "Poids lourds"
    else:
        # Recommence si mauvais choix
        print("Choix invalide, réessaie !\n")
        return personnage()


def metier():
    # Menu des métiers
    print("Maintenant choisissez votre metier")
    print("1 - Le Bio-Purificateur")
    print("2 - Le Négaciateur")
    print("3 - Le Mastodonte")

    choix = input("Choisissez le metier : ")

    # Renvoie le métier choisi
    if choix == "1":
        return "Le Bio-Purificateur"
    elif choix == "2":
        return "Le Négociateur"
    elif choix == "3":
        return "Le Mastodonte"
    else:
        # Recommence si mauvais choix
        print("Choix invalide, réessaie !\n")
        return metier()


# ------------------ CLASSE PERSONNAGE ------------------

class Personnage:
    def __init__(self, race, metier):
        # Stocke race + métier
        self.race = race
        self.metier = metier

        # Stats de base
        self.pv = 100
        self.attaque = 10
        self.vitesse = 10

        # Applique les bonus en fonction de la race et du métier
        self.appliquer_bonus_race()
        self.appliquer_bonus_metier()

    def appliquer_bonus_race(self):
        # Bonus du Gamer
        if self.race == "Gamer":
            self.attaque += 5
            self.vitesse += 2

        # Bonus du Repugnant
        elif self.race == "Repugnant":
            self.pv -= 20
            self.attaque += 15
            self.vitesse += 3

        # Bonus Poids Lourds
        elif self.race == "Poids lourds":
            self.pv += 100
            self.attaque += 5
            self.vitesse -= 5

    def appliquer_bonus_metier(self):
        # Bonus Bio-Purificateur
        if self.metier == "Le Bio-Purificateur":
            self.pv += 10
            self.attaque += 5

        # Bonus Négociateur
        elif self.metier == "Le Négaciateur":
            self.vitesse += 5
            self.attaque += 2

        # Bonus Mastodonte
        elif self.metier == "Le Mastodonte":
            self.pv += 50
            self.attaque += 10
            self.vitesse -= 3

    def afficher_stats(self):
        # Affiche la fiche du personnage
        print("\n----- FICHE PERSONNAGE -----")
        print(f"Race : {self.race}")
        print(f"Métier : {self.metier}")
        print(f"PV : {self.pv}")
        print(f"Attaque : {self.attaque}")
        print(f"Vitesse : {self.vitesse}")
        print("-----------------------------\n")


# ------------------ MENU PRINCIPAL ------------------

def menu():
    print("---------Menu---------")
    print("1 - Information sur les compétences et les races")
    print("2 - Commencer à jouer\n")

    choix = input("Choir 1 pour voir les compétences ou 2 pour commencer : ")

    # Affichage des compétences
    if choix == "1":
        return competence()

    # Lancer le jeu
    elif choix == "2":
        race = personnage()     # Choix de la race
        met = metier()          # Choix du métier

        # Associe race → compétence raciale
        competences_race = {
            "Gamer": "L'Esprit AFK",
            "Repugnant": "Le Repoussoir Social",
            "Poids lourds": "Impact Sismique"
        }

        # Résumé du choix du joueur
        print("\nVous avez choisi :", race, "et", met)
        print("La compétence raciale associée est :", competences_race[race])

        # Crée le personnage avec OOP
        perso = Personnage(race, met)
        perso.afficher_stats()

    else:
        # Mauvais choix → retour menu
        print("Choix invalide !\n")
        return menu()


# ------------------ BOUCLE DE LANCEMENT ------------------

while True:
    # Menu de début
    a = input("Menu initial : 1 pour lancer le jeu, 2 pour quitter : ")

    if a == "1":
        menu()  # Ouvre le menu principal

    elif a == "2":
        break   # Quitte le jeu