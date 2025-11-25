# src/pages/page_comp_race.py
from tkinter import Button


# Fonction générique pour un affichage de compétence
def _afficher_competence(canvas, root, assets, image_key, text_name, text_stats, y_pos, btn_key, choisir_callback,
                         comp_name):
    """Fonction utilitaire pour dessiner une compétence sur le canvas."""
    btn_background = assets[btn_key]
    canvas.create_image(70, y_pos - 40, anchor="center", image=assets[image_key])
    canvas.create_text(200, y_pos - 66, text=text_name, font=("Calisto MT", 16),
                       fill="#0a2b13" if btn_key == "btn_background3" else "#03000f")
    canvas.create_text(187, y_pos - 40, text=text_stats, font=("Calisto MT", 9),
                       fill="#0a2b13" if btn_key == "btn_background3" else "#03000f")

    btn = Button(root, image=btn_background, text="Choisir", compound="center",
                 font=("Calisto MT", 12), fg="#0a2b13" if btn_key == "btn_background3" else "#03000f",
                 borderwidth=0, command=lambda: choisir_callback(comp_name))
    canvas.create_window(380, y_pos - 22, anchor="center", window=btn)


def comprepu_menu(root, canvas, assets, choisir_comp_race_callback):
    """Affiche le menu des compétences pour la race Répugnant."""
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=assets["bg_img3"])
    canvas.create_text(220, 50, text="Choisir votre Compétence",
                       font=("Calisto MT", 28), fill="#0a2b13")

    _afficher_competence(canvas, root, assets, "comp_repugnant_1", "L'odeur de la crainte", "PV=0,ATQ=5,VTS=0,DEF=0",
                         200, "btn_background3", choisir_comp_race_callback, "L'Odeur de la Crainte")
    _afficher_competence(canvas, root, assets, "comp_repugnant_2", "Le Repas Miasmatique", "PV=20,ATQ=0,VTS=-1,DEF=0",
                         340, "btn_background3", choisir_comp_race_callback, "Le Repas Miasmatique")
    _afficher_competence(canvas, root, assets, "comp_repugnant_3", "Le Voile de Mouches", "PV=0,ATQ=0,VTS=0,DEF=8", 480,
                         "btn_background3", choisir_comp_race_callback, "Le Voile de Mouches")
    _afficher_competence(canvas, root, assets, "comp_repugnant_4", "La Piste Visqueuse", "PV=0,ATQ=0,VTS=0,DEF=3", 620,
                         "btn_background3", choisir_comp_race_callback, "La Piste Visqueuse")


def compgamer_menu(root, canvas, assets, choisir_comp_race_callback):
    """Affiche le menu des compétences pour la race Gamer."""
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=assets["bg_img2"])
    canvas.create_text(220, 50, text="Choisir votre Compétence",
                       font=("Calisto MT", 28), fill="#03000f")

    _afficher_competence(canvas, root, assets, "comp_gamer_1", "Le Speedrun Tactique", "PV=0,ATQ=0,VTS=4,DEF=0", 200,
                         "btn_background2", choisir_comp_race_callback, "Le Speedrun Tactique")
    _afficher_competence(canvas, root, assets, "comp_gamer_2", "Capture d'Écran", "PV=0,ATQ=5,VTS=0,DEF=0", 340,
                         "btn_background2", choisir_comp_race_callback, "Capture d'Écran")
    _afficher_competence(canvas, root, assets, "comp_gamer_3", "La Lecture du Boss", "PV=0,ATQ=6,VTS=0,DEF=0", 480,
                         "btn_background2", choisir_comp_race_callback, "La Lecture du Boss")
    _afficher_competence(canvas, root, assets, "comp_gamer_4", "Le Taunt Vociférant", "PV=0,ATQ=3,VTS=0,DEF=2", 620,
                         "btn_background2", choisir_comp_race_callback, "Le Taunt Vociférant")


def comppoidlourd_menu(root, canvas, assets, choisir_comp_race_callback):
    """Affiche le menu des compétences pour la race Poids Lourd."""
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=assets["bg_img2"])
    canvas.create_text(220, 50, text="Choisir votre Compétence",
                       font=("Calisto MT", 28), fill="#03000f")

    _afficher_competence(canvas, root, assets, "comp_poidslourd_1", "Le Dépôt de Graisse", "PV=60,ATQ=0,VTS=-2,DEF=15",
                         200, "btn_background2", choisir_comp_race_callback, "Le Dépôt de Graisse")
    _afficher_competence(canvas, root, assets, "comp_poidslourd_2", "L'Écrasement Calorique",
                         "PV=20,ATQ=10,VTS=-2,DEF=0", 340, "btn_background2", choisir_comp_race_callback,
                         "L'Écrasement Calorique")
    _afficher_competence(canvas, root, assets, "comp_poidslourd_3", "La Réserve de Snacks", "PV=80,ATQ=3,VTS=-3,DEF=5",
                         480, "btn_background2", choisir_comp_race_callback, "La Réserve de Snacks")
    _afficher_competence(canvas, root, assets, "comp_poidslourd_4", "La Persistance Grasse",
                         "PV=40,ATQ=0,VTS=-1,DEF=10", 620, "btn_background2", choisir_comp_race_callback,
                         "La Persistance Grasse")