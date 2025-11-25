from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import pygame

# --- Initialisation ---
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# --- Dictionnaires de compétences ---
competences_optionnelles_race = {
    "Répugnant": {
        "L'Odeur de la Crainte": {"pv": 0, "attaque": 5, "vitesse": 0, "defense": 0},
        "Le Repas Miasmatique": {"pv": 20, "attaque": 0, "vitesse": -1, "defense": 0},
        "Le Voile de Mouches": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 8},
        "La Piste Visqueuse": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 3}
    },
    "Gamer": {
        "Le Speedrun Tactique": {"pv": 0, "attaque": 0, "vitesse": 4, "defense": 0},
        "Capture d'Écran": {"pv": 0, "attaque": 5, "vitesse": 0, "defense": 0},
        "La Lecture du Boss": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Taunt Vociférant": {"pv": 0, "attaque": 3, "vitesse": 0, "defense": 2}
    },
    "Poids Lourd": {
        "Le Dépôt de Graisse": {"pv": 60, "attaque": 0, "vitesse": -2, "defense": 15},
        "L'Écrasement Calorique": {"pv": 20, "attaque": 10, "vitesse": -2, "defense": 0},
        "La Réserve de Snacks": {"pv": 80, "attaque": 3, "vitesse": -3, "defense": 5},
        "La Persistance Grasse": {"pv": 40, "attaque": 0, "vitesse": -1, "defense": 10}
    }
}

competences_optionnelles_metier = {
    "BioPurificateur": {
        "comp1": {"pv": 10, "attaque": 5, "vitesse": 0, "defense": 0}
    },
    "Négociateur": {
        "comp1": {"pv": 0, "attaque": 2, "vitesse": 5, "defense": 0}
    },
    "Mastodonte": {
        "comp1": {"pv": 50, "attaque": 10, "vitesse": -3, "defense": 5}
    }
}

# Compétences automatiques par race/métier
competences_auto_race = {
    "Répugnant": "Puanteur Naturelle",
    "Gamer": "Réflexes Affûtés",
    "Poids Lourd": "Masse Imposante"
}

competences_auto_metier = {
    "BioPurificateur": "Purification",
    "Négociateur": "Art de la Parole",
    "Mastodonte": "Résistance"
}


# --- Classe Personnage ---
class Personnage:
    def __init__(self, race=None, comp_race_auto=None, comp_race_choisie=None,
                 metier=None, comp_metier_auto=None, comp_metier_choisie=None):
        self.race = race
        self.metier = metier

        self.comp_race_auto = comp_race_auto
        self.comp_race_choisie = comp_race_choisie
        self.comp_metier_auto = comp_metier_auto
        self.comp_metier_choisie = comp_metier_choisie

        # Stats de base
        self.pv = 100
        self.attaque = 10
        self.vitesse = 10
        self.defense = 0

        # Appliquer bonus si tout est défini
        if race and comp_race_choisie and metier and comp_metier_choisie:
            self.appliquer_bonus_optionnels()

    def appliquer_bonus_optionnels(self):
        # Bonus race
        if self.comp_race_choisie and self.race in competences_optionnelles_race:
            bonus = competences_optionnelles_race[self.race].get(self.comp_race_choisie, {})
            self.pv += bonus.get("pv", 0)
            self.attaque += bonus.get("attaque", 0)
            self.vitesse += bonus.get("vitesse", 0)
            self.defense += bonus.get("defense", 0)

        # Bonus métier
        if self.comp_metier_choisie and self.metier in competences_optionnelles_metier:
            bonus = competences_optionnelles_metier[self.metier].get(self.comp_metier_choisie, {})
            self.pv += bonus.get("pv", 0)
            self.attaque += bonus.get("attaque", 0)
            self.vitesse += bonus.get("vitesse", 0)
            self.defense += bonus.get("defense", 0)

    def recap(self):
        return (f"Race : {self.race}\n"
                f"Compétence Race : {self.comp_race_choisie}\n"
                f"Métier : {self.metier}\n"
                f"Compétence Métier : {self.comp_metier_choisie}\n\n"
                f"PV : {self.pv}\n"
                f"Attaque : {self.attaque}\n"
                f"Vitesse : {self.vitesse}\n"
                f"Défense : {self.defense}")


# --- Interface Tkinter ---
root = Tk()
root.geometry("450x700")
icone = PhotoImage(file="iconlogo.png")
root.iconphoto(True, icone)
root.resizable(False, False)
root.title("Menu RPG")

canvas = Canvas(root, width=450, height=700, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)

# Chargement des images
bg_img = ImageTk.PhotoImage(Image.open("fond-de-papier-grunge.jpg").resize((450, 700), Image.LANCZOS))
bg_img2 = ImageTk.PhotoImage(Image.open("fond3.png").resize((450, 700), Image.LANCZOS))
bg_img3 = ImageTk.PhotoImage(Image.open("fondvertfond.png").resize((450, 700), Image.LANCZOS))

img1 = ImageTk.PhotoImage(Image.open("image1.png").resize((100, 100), Image.LANCZOS))
img2 = ImageTk.PhotoImage(Image.open("image2.png").resize((100, 100), Image.LANCZOS))
img3 = ImageTk.PhotoImage(Image.open("image3.png").resize((100, 100), Image.LANCZOS))
img4 = ImageTk.PhotoImage(Image.open("purificateur.png").resize((100, 100), Image.LANCZOS))
img5 = ImageTk.PhotoImage(Image.open("negociateur.png").resize((100, 100), Image.LANCZOS))
img6 = ImageTk.PhotoImage(Image.open("mastodonte.png").resize((100, 100), Image.LANCZOS))
img7 = ImageTk.PhotoImage(Image.open("L'Odeur de la Crainte.png").resize((70, 70), Image.LANCZOS))
img8 = ImageTk.PhotoImage(Image.open("La Piste Visqueuse.png").resize((70, 70), Image.LANCZOS))
img9 = ImageTk.PhotoImage(Image.open("Le Repas Miasmatique.png").resize((70, 70), Image.LANCZOS))
img10 = ImageTk.PhotoImage(Image.open("Le Voile de Mouches.png").resize((70, 70), Image.LANCZOS))
img11 = ImageTk.PhotoImage(Image.open("Capture d'Écran.png").resize((70, 70), Image.LANCZOS))
img12 = ImageTk.PhotoImage(Image.open("La Lecture du Boss.png").resize((70, 70), Image.LANCZOS))
img13 = ImageTk.PhotoImage(Image.open("Le Speedrun Tactique.png").resize((70, 70), Image.LANCZOS))
img14 = ImageTk.PhotoImage(Image.open("Le Taunt Vociférant.png").resize((70, 70), Image.LANCZOS))

btn_backgroundmenu = ImageTk.PhotoImage(Image.open("fond2.png").resize((180, 70), Image.LANCZOS))
btn_background = ImageTk.PhotoImage(Image.open("fond2.png").resize((120, 40), Image.LANCZOS))
btn_background2 = ImageTk.PhotoImage(Image.open("fondnoir.png").resize((120, 40), Image.LANCZOS))
btn_background3 = ImageTk.PhotoImage(Image.open("fondvert.png").resize((120, 40), Image.LANCZOS))

# Instance personnage global
perso = Personnage()


# --- Fonctions Menu ---
def menu():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img)
    canvas.create_text(230, 80, text="Oignon Ring's Rpg",
                       font=("Calisto MT", 36), fill="#5e3a1b")
    canvas.create_text(235, 120, text="By DiapoDeMerde Studio.",
                       font=("Calisto MT", 16), fill="#5e3a1b")
    canvas.create_text(235, 660, text="Par Mattéo et Maxime️",
                       font=("Calisto MT", 15), fill="#5e3a1b")

    btn3 = Button(root, image=btn_backgroundmenu, text="Jouer", compound="center",
                  font=("Calisto MT", 28), fg="#5e3a1b", borderwidth=0, command=page_menu)
    canvas.create_window(225, 600, anchor="center", window=btn3)


def page_menu():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img)
    canvas.create_text(220, 70, text="⚔️ Choisir votre Race ⚔️",
                       font=("Calisto MT", 28), fill="#5e3a1b")

    # Race 1 - Répugnant
    canvas.create_image(100, 180, anchor="center", image=img1)
    canvas.create_text(220, 140, text="Répugnant", font=("Calisto MT", 20), fill="#5e3a1b")
    canvas.create_text(240, 180, text="Un homme répugnant pouvant\nattaquer avec \nson hygiène désastreuse",
                       font=("Calisto MT", 10), fill="#5e3a1b")
    btn1 = Button(root, image=btn_background, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0,
                  command=lambda: choisir_race("Répugnant"))
    canvas.create_window(380, 200, anchor="center", window=btn1)

    # Race 2 - Gamer
    canvas.create_image(100, 380, anchor="center", image=img2)
    canvas.create_text(195, 340, text="Gamer", font=("Calisto MT", 20), fill="#5e3a1b")
    canvas.create_text(230, 370, text="Un gamer prodige capable\nd'exploit grâce au tryhard",
                       font=("Calisto MT", 10), fill="#5e3a1b")
    btn2 = Button(root, image=btn_background, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0,
                  command=lambda: choisir_race("Gamer"))
    canvas.create_window(380, 400, anchor="center", window=btn2)

    # Race 3 - Poids Lourd
    canvas.create_image(100, 580, anchor="center", image=img3)
    canvas.create_text(230, 540, text="Poids Lourd", font=("Calisto MT", 20), fill="#5e3a1b")
    canvas.create_text(247, 570, text="Un homme puissant mais lourd\nfaisant de lourdes attaques",
                       font=("Calisto MT", 10), fill="#5e3a1b")
    btn3 = Button(root, image=btn_background, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0,
                  command=lambda: choisir_race("Poids Lourd"))
    canvas.create_window(380, 600, anchor="center", window=btn3)


def choisir_race(race):
    perso.race = race
    perso.comp_race_auto = competences_auto_race[race]

    if race == "Répugnant":
        comprepu_menu()
    elif race == "Gamer":
        compgamer_menu()
    elif race == "Poids Lourd":
        comppoidlourd_menu()


def comprepu_menu():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img3)
    canvas.create_text(220, 50, text="Choisir votre Compétence",
                       font=("Calisto MT", 28), fill="#0a2b13")

    # Compétence 1
    canvas.create_image(70, 140, anchor="center", image=img7)
    canvas.create_text(200, 114, text="L'odeur de la crainte", font=("Calisto MT", 16), fill="#0a2b13")
    canvas.create_text(187, 140, text="PV=0,ATQ=5,VTS=0,DEF=0", font=("Calisto MT", 9), fill="#0a2b13")
    btn1 = Button(root, image=btn_background3, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#0a2b13", borderwidth=0,
                  command=lambda: choisir_comp_race("L'Odeur de la Crainte"))
    canvas.create_window(380, 158, anchor="center", window=btn1)

    # Compétence 2
    canvas.create_image(70, 280, anchor="center", image=img9)
    canvas.create_text(210, 253, text="Le Repas Miasmatique", font=("Calisto MT", 16), fill="#0a2b13")
    canvas.create_text(192, 280, text="PV=20,ATQ=0,VTS=-1,DEF=0", font=("Calisto MT", 9), fill="#0a2b13")
    btn2 = Button(root, image=btn_background3, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#0a2b13", borderwidth=0,
                  command=lambda: choisir_comp_race("Le Repas Miasmatique"))
    canvas.create_window(380, 300, anchor="center", window=btn2)

    # Compétence 3
    canvas.create_image(70, 420, anchor="center", image=img10)
    canvas.create_text(202, 392, text="Le Voile de Mouches", font=("Calisto MT", 16), fill="#0a2b13")
    canvas.create_text(187, 415, text="PV=0,ATQ=0,VTS=0,DEF=8", font=("Calisto MT", 9), fill="#0a2b13")
    btn3 = Button(root, image=btn_background3, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#0a2b13", borderwidth=0,
                  command=lambda: choisir_comp_race("Le Voile de Mouches"))
    canvas.create_window(380, 435, anchor="center", window=btn3)

    # Compétence 4
    canvas.create_image(70, 560, anchor="center", image=img8)
    canvas.create_text(194, 533, text="La Piste Visqueuse", font=("Calisto MT", 16), fill="#0a2b13")
    canvas.create_text(190, 555, text="PV=0,ATQ=0,VTS=0,DEF=3", font=("Calisto MT", 9), fill="#0a2b13")
    btn4 = Button(root, image=btn_background3, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#0a2b13", borderwidth=0,
                  command=lambda: choisir_comp_race("La Piste Visqueuse"))
    canvas.create_window(380, 572, anchor="center", window=btn4)


def compgamer_menu():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img2)
    canvas.create_text(220, 50, text="Choisir votre Compétence",
                       font=("Calisto MT", 28), fill="#03000f")

    # Compétence 1
    canvas.create_image(70, 140, anchor="center", image=img13)
    canvas.create_text(210, 114, text="Le Speedrun Tactique", font=("Calisto MT", 16), fill="#03000f")
    canvas.create_text(187, 140, text="PV=0,ATQ=0,VTS=4,DEF=0", font=("Calisto MT", 9), fill="#03000f")
    btn1 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_comp_race("Le Speedrun Tactique"))
    canvas.create_window(380, 158, anchor="center", window=btn1)

    # Compétence 2
    canvas.create_image(70, 280, anchor="center", image=img11)
    canvas.create_text(180, 253, text="Capture d'Écran", font=("Calisto MT", 16), fill="#03000f")
    canvas.create_text(189, 280, text="PV=0,ATQ=5,VTS=0,DEF=0", font=("Calisto MT", 9), fill="#03000f")
    btn2 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_comp_race("Capture d'Écran"))
    canvas.create_window(380, 300, anchor="center", window=btn2)

    # Compétence 3
    canvas.create_image(70, 420, anchor="center", image=img12)
    canvas.create_text(192, 392, text="La Lecture du Boss", font=("Calisto MT", 16), fill="#03000f")
    canvas.create_text(185, 415, text="PV=0,ATQ=6,VTS=0,DEF=0", font=("Calisto MT", 9), fill="#03000f")
    btn3 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_comp_race("La Lecture du Boss"))
    canvas.create_window(380, 435, anchor="center", window=btn3)

    # Compétence 4
    canvas.create_image(70, 560, anchor="center", image=img14)
    canvas.create_text(196, 533, text="Le Taunt Vociférant", font=("Calisto MT", 16), fill="#03000f")
    canvas.create_text(189, 555, text="PV=0,ATQ=3,VTS=0,DEF=2", font=("Calisto MT", 9), fill="#03000f")
    btn4 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_comp_race("Le Taunt Vociférant"))
    canvas.create_window(380, 572, anchor="center", window=btn4)


def comppoidlourd_menu():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img2)
    canvas.create_text(220, 50, text="Choisir votre Compétence",
                       font=("Calisto MT", 28), fill="#03000f")

    # Compétence 1
    canvas.create_image(70, 140, anchor="center", image=img13)
    canvas.create_text(196, 114, text="Le Dépôt de Graisse", font=("Calisto MT", 16), fill="#03000f")
    canvas.create_text(192, 140, text="PV=60,ATQ=0,VTS=-2,DEF=15", font=("Calisto MT", 9), fill="#03000f")
    btn1 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_comp_race("Le Dépôt de Graisse"))
    canvas.create_window(380, 158, anchor="center", window=btn1)

    # Compétence 2
    canvas.create_image(70, 280, anchor="center", image=img11)
    canvas.create_text(215, 253, text="L'Écrasement Calorique", font=("Calisto MT", 16), fill="#03000f")
    canvas.create_text(194, 280, text="PV=20,ATQ=10,VTS=-2,DEF=0", font=("Calisto MT", 9), fill="#03000f")
    btn2 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_comp_race("L'Écrasement Calorique"))
    canvas.create_window(380, 300, anchor="center", window=btn2)

    # Compétence 3
    canvas.create_image(70, 420, anchor="center", image=img12)
    canvas.create_text(202, 392, text="La Réserve de Snacks", font=("Calisto MT", 16), fill="#03000f")
    canvas.create_text(190, 415, text="PV=80,ATQ=3,VTS=-3,DEF=5", font=("Calisto MT", 9), fill="#03000f")
    btn3 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_comp_race("La Réserve de Snacks"))
    canvas.create_window(380, 435, anchor="center", window=btn3)

    # Compétence 4
    canvas.create_image(70, 560, anchor="center", image=img14)
    canvas.create_text(201, 533, text="La Persistance Grasse", font=("Calisto MT", 16), fill="#03000f")
    canvas.create_text(194, 555, text="PV=40,ATQ=0,VTS=-1,DEF=10", font=("Calisto MT", 9), fill="#03000f")
    btn4 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 12), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_comp_race("La Persistance Grasse"))
    canvas.create_window(380, 572, anchor="center", window=btn4)


def choisir_comp_race(competence):
    perso.comp_race_choisie = competence
    page_menu2()


def page_menu2():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img2)
    canvas.create_text(220, 70, text="⚒Choisir votre Métier⚒",
                       font=("Calisto MT", 28), fill="#03000f")

    # Métier 1 - BioPurificateur
    canvas.create_image(100, 180, anchor="center", image=img4)
    canvas.create_text(240, 140, text="BioPurificateur", font=("Calisto MT", 20), fill="#03000f")
    canvas.create_text(230, 180, text="Un métier ayant pour\nbut de purifier ces ennemies\net faire de lourds dégats",
                       font=("Calisto MT", 10), fill="#03000f")
    btn1 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_metier("BioPurificateur"))
    canvas.create_window(380, 200, anchor="center", window=btn1)

    # Métier 2 - Négociateur
    canvas.create_image(100, 380, anchor="center", image=img5)
    canvas.create_text(225, 340, text="Négociateur", font=("Calisto MT", 20), fill="#03000f")
    canvas.create_text(215, 380, text="Un métier ayant pour\ncapacité la facilité\nà négocier/ruser",
                       font=("Calisto MT", 10), fill="#03000f")
    btn2 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_metier("Négociateur"))
    canvas.create_window(380, 400, anchor="center", window=btn2)

    # Métier 3 - Mastodonte
    canvas.create_image(100, 580, anchor="center", image=img6)
    canvas.create_text(225, 540, text="Mastodonte", font=("Calisto MT", 20), fill="#03000f")
    canvas.create_text(213, 580, text="Un métier ayant la\ncapacité de résister\nà de lourds attaques",
                       font=("Calisto MT", 10), fill="#03000f")
    btn3 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_metier("Mastodonte"))
    canvas.create_window(380, 600, anchor="center", window=btn3)


def choisir_metier(metier):
    perso.metier = metier
    perso.comp_metier_auto = competences_auto_metier[metier]
    perso.comp_metier_choisie = "comp1"

    perso.appliquer_bonus_optionnels()

    # Afficher le récapitulatif
    page_recap()


def page_recap():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img)
    canvas.create_text(220, 50, text="🎉 Personnage Cré ! 🎉",
                       font=("Calisto MT", 28), fill="#5e3a1b")

    recap_text = perso.recap()
    canvas.create_text(220, 350, text=recap_text, font=("Calisto MT", 16), fill="#5e3a1b")

    btn_recommencer = Button(root, image=btn_background, text="Recommencer", compound="center",
                             font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0,
                             command=recommencer)
    canvas.create_window(220, 650, anchor="center", window=btn_recommencer)


def recommencer():
    global perso
    perso = Personnage()
    menu()


# Lancement
menu()
root.mainloop()