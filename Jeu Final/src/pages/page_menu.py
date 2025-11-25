# src/pages/page_menu.py
from tkinter import Button

def menu(root, canvas, assets, perso, navigate_to):
    """Affiche la page de menu de départ."""
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=assets["bg_img"])
    canvas.create_text(230, 80, text="Oignon Ring's Rpg",
                       font=("Calisto MT", 36), fill="#5e3a1b")
    canvas.create_text(235, 120, text="By DiapoDeMerde Studio.",
                       font=("Calisto MT", 16), fill="#5e3a1b")
    canvas.create_text(235, 660, text="Par Mattéo et Maxime",
                       font=("Calisto MT", 15), fill="#5e3a1b")

    btn3 = Button(root, image=assets["btn_backgroundmenu"], text="Jouer", compound="center",
                  font=("Calisto MT", 28), fg="#5e3a1b", borderwidth=0, 
                  command=lambda: navigate_to('page_menu_race'))
    canvas.create_window(225, 600, anchor="center", window=btn3)