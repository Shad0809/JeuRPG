from tkinter import *
from PIL import Image, ImageTk





# ------------------ CLASSE PERSONNAGE ------------------
class Personnage:
    def __init__(self, race=None, metier=None):
        self.race = race
        self.metier = metier
        self.pv = 100
        self.attaque = 10
        self.vitesse = 10

    def appliquer_bonus_race(self):
        if self.race == "Gamer":
            self.attaque += 5
            self.vitesse += 2
        elif self.race == "Répugnant":
            self.pv -= 20
            self.attaque += 15
            self.vitesse += 3
        elif self.race == "Poids Lourds":
            self.pv += 100
            self.attaque += 5
            self.vitesse -= 5

    def appliquer_bonus_metier(self):
        if self.metier == "BioPurificateur":
            self.pv += 10
            self.attaque += 5
        elif self.metier == "Négociateur":
            self.vitesse += 5
            self.attaque += 2
        elif self.metier == "Mastodonte":
            self.pv += 50
            self.attaque += 10
            self.vitesse -= 3

    def calculer_stats(self):
        self.appliquer_bonus_race()
        self.appliquer_bonus_metier()

    def recap(self):
        return f"Race : {self.race}\nMétier : {self.metier}\nPV : {self.pv}\nAttaque : {self.attaque}\nVitesse : {self.vitesse}"







root = Tk()
root.geometry("450x700")
root.resizable(False, False)
root.title("Menu RPG")

canvas = Canvas(root, width=450, height=700, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)

# Charger images une seule fois
bg_img = ImageTk.PhotoImage(Image.open("fond-de-papier-grunge.jpg").resize((450, 700), Image.LANCZOS))
bg_img2 = ImageTk.PhotoImage(Image.open("fond3.png").resize((450, 700), Image.LANCZOS))

img1 = ImageTk.PhotoImage(Image.open("image1.png").resize((100, 100), Image.LANCZOS))
img2 = ImageTk.PhotoImage(Image.open("image2.png").resize((100, 100), Image.LANCZOS))
img3 = ImageTk.PhotoImage(Image.open("image3.png").resize((100, 100), Image.LANCZOS))
img4 = ImageTk.PhotoImage(Image.open("purificateur.png").resize((100, 100), Image.LANCZOS))
img5 = ImageTk.PhotoImage(Image.open("negociateur.png").resize((100, 100), Image.LANCZOS))
img6 = ImageTk.PhotoImage(Image.open("mastodonte.png").resize((100, 100), Image.LANCZOS))


btn_background = ImageTk.PhotoImage(Image.open("fond2.png").resize((120, 40), Image.LANCZOS))
btn_background2 = ImageTk.PhotoImage(Image.open("fondnoir.png").resize((120, 40), Image.LANCZOS))

# ------------------ PAGES ------------------

perso = Personnage()  # stocke le personnage choisi

# ------------------ FONCTIONS PAGES ------------------
def page_race(race):
    perso.race = race
    page_menu2()  # après choix race, on va au menu métier

def page_metier(metier):
    perso.metier = metier
    perso.calculer_stats()
    recap_page()

def recap_page():
    canvas.delete("all")
    canvas.create_text(225, 100, text="Récapitulatif de votre personnage", font=("Calisto MT", 20), fill="#5e3a1b")
    canvas.create_text(225, 300, text=perso.recap(), font=("Calisto MT", 16), fill="#5e3a1b")
    retour = Button(root, text="Retour au menu", font=("Calisto MT", 16), command=page_menu)
    canvas.create_window(225, 600, window=retour)

def page_race1():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img)

    canvas.create_text(225, 200, text="Tu as choisi :", font=("Calisto MT", 26), fill="#5e3a1b")
    canvas.create_text(225, 260, text="Répugnant", font=("Calisto MT", 30), fill="#5e3a1b")

    # Retour au menu
    retour = Button(root, text="Retour", font=("Calisto MT", 16), command=page_menu)
    canvas.create_window(225, 600, window=retour)


def page_race2():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img)

    canvas.create_text(225, 200, text="Tu as choisi :", font=("Calisto MT", 26), fill="#5e3a1b")
    canvas.create_text(225, 260, text="Gamer", font=("Calisto MT", 30), fill="#5e3a1b")

    retour = Button(root, text="Retour", font=("Calisto MT", 16), command=page_menu)
    canvas.create_window(225, 600, window=retour)


def page_race3():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=bg_img)

    canvas.create_text(225, 200, text="Tu as choisi :", font=("Calisto MT", 26), fill="#5e3a1b")
    canvas.create_text(225, 260, text="Poids Lourds", font=("Calisto MT", 30), fill="#5e3a1b")

    retour = Button(root, text="Retour", font=("Calisto MT", 16), command=page_menu)
    canvas.create_window(225, 600, window=retour)


# ------------------ MENU PRINCIPAL ------------------

def page_menu():
    canvas.delete("all")

    # Fond
    canvas.create_image(0, 0, anchor="nw", image=bg_img)

    # Titre
    canvas.create_text(210, 70, text="Choisir votre Race",
                        font=("Calisto MT", 28), fill="#5e3a1b")

    # --- Race 1 ---
    canvas.create_image(100, 180, anchor="center", image=img1)
    canvas.create_text(215, 140, text="Répugnant", font=("Calisto MT", 20), fill="#5e3a1b")

    btn1 = Button(root, image=btn_background, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0, command=page_race1)
    canvas.create_window(380, 200, anchor="center", window=btn1)

    # --- Race 2 ---
    canvas.create_image(100, 380, anchor="center", image=img2)
    canvas.create_text(195, 340, text="Gamer", font=("Calisto MT", 20), fill="#5e3a1b")

    btn2 = Button(root, image=btn_background, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0, command=page_race2)
    canvas.create_window(380, 400, anchor="center", window=btn2)

    # --- Race 3 ---
    canvas.create_image(100, 580, anchor="center", image=img3)
    canvas.create_text(230, 540, text="Poids Lourds", font=("Calisto MT", 20), fill="#5e3a1b")

    btn3 = Button(root, image=btn_background, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0, command=page_race3)
    canvas.create_window(380, 600, anchor="center", window=btn3)

    pagesui = Button(root, text="Page Suivante", font=("Calisto MT", 16), command=page_menu2)
    canvas.create_window(225, 600, window=pagesui)

def page_menu2():
    canvas.delete("all")

    # Fond
    canvas.create_image(0, 0, anchor="nw", image=bg_img2)

    # Titre
    canvas.create_text(210, 70, text="Choisir votre Métier",
                        font=("Calisto MT", 28), fill="#03000f")

    # --- Race 1 ---
    canvas.create_image(100, 180, anchor="center", image=img4)
    canvas.create_text(240, 140, text="BioPurificateur", font=("Calisto MT", 20), fill="#03000f")

    btn1 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0, command=page_race1)
    canvas.create_window(380, 200, anchor="center", window=btn1)

    # --- Race 2 ---
    canvas.create_image(100, 380, anchor="center", image=img5)
    canvas.create_text(225, 340, text="Négociateur", font=("Calisto MT", 20), fill="#03000f")

    btn2 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0, command=page_race2)
    canvas.create_window(380, 400, anchor="center", window=btn2)

    # --- Race 3 ---
    canvas.create_image(100, 580, anchor="center", image=img6)
    canvas.create_text(225, 540, text="Mastodonte", font=("Calisto MT", 20), fill="#03000f")

    btn3 = Button(root, image=btn_background2, text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0, command=page_race3)
    canvas.create_window(380, 600, anchor="center", window=btn3)

# Lancer la première page
page_menu()

root.mainloop()
