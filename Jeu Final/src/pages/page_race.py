# src/pages/page_race.py
from tkinter import Button

def page_menu(root, canvas, assets, choisir_race_callback):
    """Affiche la page de choix de la race."""
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=assets["bg_img"])
    canvas.create_text(220, 70, text="⚔️ Choisir votre Race ⚔️",
                       font=("Calisto MT", 28), fill="#5e3a1b")

    # Race 1 - Répugnant
    canvas.create_image(100, 180, anchor="center", image=assets["img1_repugnant"])
    canvas.create_text(220, 140, text="Répugnant", font=("Calisto MT", 20), fill="#5e3a1b")
    canvas.create_text(240, 180, text="Un homme répugnant pouvant\nattaquer avec \nson hygiène désastreuse",
                       font=("Calisto MT", 10), fill="#5e3a1b")
    btn1 = Button(root, image=assets["btn_background"], text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0,
                  command=lambda: choisir_race_callback("Répugnant"))
    canvas.create_window(380, 200, anchor="center", window=btn1)

    # Race 2 - Gamer
    canvas.create_image(100, 380, anchor="center", image=assets["img2_gamer"])
    canvas.create_text(195, 340, text="Gamer", font=("Calisto MT", 20), fill="#5e3a1b")
    canvas.create_text(230, 370, text="Un gamer prodige capable\nd'exploit grâce au tryhard",
                       font=("Calisto MT", 10), fill="#5e3a1b")
    btn2 = Button(root, image=assets["btn_background"], text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0,
                  command=lambda: choisir_race_callback("Gamer"))
    canvas.create_window(380, 400, anchor="center", window=btn2)

    # Race 3 - Poids Lourd
    canvas.create_image(100, 580, anchor="center", image=assets["img3_poidslourd"])
    canvas.create_text(230, 540, text="Poids Lourd", font=("Calisto MT", 20), fill="#5e3a1b")
    canvas.create_text(247, 570, text="Un homme puissant mais lourd\nfaisant de lourdes attaques",
                       font=("Calisto MT", 10), fill="#5e3a1b")
    btn3 = Button(root, image=assets["btn_background"], text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0,
                  command=lambda: choisir_race_callback("Poids Lourd"))
    canvas.create_window(380, 600, anchor="center", window=btn3)