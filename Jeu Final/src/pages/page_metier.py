# src/pages/page_metier.py
from tkinter import Button

def page_menu2(root, canvas, assets, choisir_metier_callback):
    """Affiche la page de choix du métier."""
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=assets["bg_img2"])
    canvas.create_text(220, 70, text="⚒Choisir votre Métier⚒",
                       font=("Calisto MT", 28), fill="#03000f")

    # Métier 1 - BioPurificateur
    canvas.create_image(100, 180, anchor="center", image=assets["img4_purificateur"])
    canvas.create_text(240, 140, text="BioPurificateur", font=("Calisto MT", 20), fill="#03000f")
    canvas.create_text(230, 180, text="Un métier ayant pour\nbut de purifier ces ennemies\net faire de lourds dégats",
                       font=("Calisto MT", 10), fill="#03000f")
    btn1 = Button(root, image=assets["btn_background2"], text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_metier_callback("BioPurificateur"))
    canvas.create_window(380, 200, anchor="center", window=btn1)

    # Métier 2 - Négociateur
    canvas.create_image(100, 380, anchor="center", image=assets["img5_negociateur"])
    canvas.create_text(225, 340, text="Négociateur", font=("Calisto MT", 20), fill="#03000f")
    canvas.create_text(215, 380, text="Un métier ayant pour\ncapacité la facilité\nà négocier/ruser",
                       font=("Calisto MT", 10), fill="#03000f")
    btn2 = Button(root, image=assets["btn_background2"], text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_metier_callback("Négociateur"))
    canvas.create_window(380, 400, anchor="center", window=btn2)

    # Métier 3 - Mastodonte
    canvas.create_image(100, 580, anchor="center", image=assets["img6_mastodonte"])
    canvas.create_text(225, 540, text="Mastodonte", font=("Calisto MT", 20), fill="#03000f")
    canvas.create_text(213, 580, text="Un métier ayant la\ncapacité de résister\nà de lourds attaques",
                       font=("Calisto MT", 10), fill="#03000f")
    btn3 = Button(root, image=assets["btn_background2"], text="Choisir", compound="center",
                  font=("Calisto MT", 14), fg="#03000f", borderwidth=0,
                  command=lambda: choisir_metier_callback("Mastodonte"))
    canvas.create_window(380, 600, anchor="center", window=btn3)