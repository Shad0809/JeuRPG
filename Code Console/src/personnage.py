from competences import competences_optionnelles_race, competences_optionnelles_metier

# ------------------ CLASSE PERSONNAGE ------------------

class Personnage:
    def __init__(self, race, comp_race_auto, comp_race_choisie,
                 metier, comp_metier_auto, comp_metier_choisie):

        #enregistre la race et le métier dans l’objet
        self.race = race
        self.metier = metier

        # compétences (noms)
        #On stocke les noms des compétences du personnage
        self.comp_race_auto = comp_race_auto
        self.comp_race_choisie = comp_race_choisie
        self.comp_metier_auto = comp_metier_auto
        self.comp_metier_choisie = comp_metier_choisie

        # stats de base
        #Stats de base communes à tous les personnages
        self.pv = 100
        self.attaque = 10
        self.vitesse = 10
        self.defense = 0

        # Appliquer bonus des compétences optionnelles  et on applique automatiquement les bonus
        self.appliquer_bonus_optionnels()

    #Modifie les stats du personnage en fonction des compétences choisies
    def appliquer_bonus_optionnels(self): #
        # race optionnelle / on récupère l’objet bonus
        if self.comp_race_choisie:
            bonus = competences_optionnelles_race[self.race][self.comp_race_choisie]
            self.pv += bonus.get("pv", 0) #Get c'est pour rajouter sinon c'est 0 en fonction de du bonus choisi
            self.attaque += bonus.get("attaque", 0)#Idem que GET PV
            self.vitesse += bonus.get("vitesse", 0)#Idem que GET PV
            self.defense += bonus.get("defense", 0)#Idem que GET PV

        # Metier optionnel / Idem que comp_race_choisie
        if self.comp_metier_choisie:
            bonus = competences_optionnelles_metier[self.metier][self.comp_metier_choisie]
            self.pv += bonus.get("pv", 0)
            self.attaque += bonus.get("attaque", 0)
            self.vitesse += bonus.get("vitesse", 0)
            self.defense += bonus.get("defense", 0)

    def afficher_stats(self):
        from utils import afficher_title
        from competences import competences_optionnelles_race, competences_optionnelles_metier

        afficher_title("FICHE PERSONNAGE") # On rappel pour le titre stylisé

        #Affichage des informations du personnage
        print(f"Race : {self.race}")
        print(f"Compétence raciale : {self.comp_race_auto}")
        print(f"Compétence raciale choisie : {self.comp_race_choisie}\n")
        print(f"Métier : {self.metier}")
        print(f"Compétence de métier : {self.comp_metier_auto}")
        print(f"Compétence métier choisie : {self.comp_metier_choisie}\n")

        #Affichage des stats finales
        print("----- STATS FINALES -----")
        print(f"PV : {self.pv}")
        print(f"Attaque : {self.attaque}")
        print(f"Vitesse : {self.vitesse}")
        print(f"Défense : {self.defense}")

        #Affichage des bonus appliqués
        print("\n---- BONUS APPLIQUÉS ----")
        if self.comp_race_choisie:
            print(f"Bonus (race) : {competences_optionnelles_race[self.race][self.comp_race_choisie]}")
        if self.comp_metier_choisie:
            print(f"Bonus (metier) : {competences_optionnelles_metier[self.metier][self.comp_metier_choisie]}")
