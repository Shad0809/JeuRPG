# src/pages/page_recap.py
from tkinter import Button

def page_recap(root, canvas, assets, perso, recommencer_callback):
    """Affiche le récapitulatif du personnage créé."""
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=assets["bg_img"])
    canvas.create_text(220, 50, text="🎉 Personnage Créé ! 🎉",
                       font=("Calisto MT", 28), fill="#5e3a1b")

    recap_text = perso.recap()
    canvas.create_text(220, 350, text=recap_text, font=("Calisto MT", 16), fill="#5e3a1b")

    btn_recommencer = Button(root, image=assets["btn_background"], text="Recommencer", compound="center",
                             font=("Calisto MT", 14), fg="#5e3a1b", borderwidth=0,
                             command=recommencer_callback)
    canvas.create_window(220, 650, anchor="center", window=btn_recommencer)