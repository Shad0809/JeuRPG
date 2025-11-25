# src/pages/ui_widgets.py

from PIL import Image, ImageTk

# Chemins de base vers les assets images
ASSETS_PATH = "assets/images/"


def charger_assets():
    """Charge toutes les images nécessaires pour l'interface Tkinter."""

    assets = {}

    # --- Fonds d'écran (Backgrounds) ---
    assets["bg_img"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "backgrounds/fond-de-papier-grunge.jpg").resize((450, 700), Image.LANCZOS))
    assets["bg_img2"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "backgrounds/fond3.png").resize((450, 700), Image.LANCZOS))
    assets["bg_img3"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "backgrounds/fondvertfond.png").resize((450, 700), Image.LANCZOS))

    # --- Personnages (Characters/Races) ---
    assets["img1_repugnant"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "characters/image1.png").resize((100, 100), Image.LANCZOS))
    assets["img2_gamer"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "characters/image2.png").resize((100, 100), Image.LANCZOS))
    assets["img3_poidslourd"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "characters/image3.png").resize((100, 100), Image.LANCZOS))

    # --- Métiers ---
    assets["img4_purificateur"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "metiers/purificateur.png").resize((100, 100), Image.LANCZOS))
    assets["img5_negociateur"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "metiers/negociateur.png").resize((100, 100), Image.LANCZOS))
    assets["img6_mastodonte"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "metiers/mastodonte.png").resize((100, 100), Image.LANCZOS))

    # --- Compétences Race Répugnant ---
    assets["comp_repugnant_1"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "competences_race/L'Odeur de la Crainte.png").resize((70, 70), Image.LANCZOS))
    assets["comp_repugnant_2"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "competences_race/Le Repas Miasmatique.png").resize((70, 70), Image.LANCZOS))
    assets["comp_repugnant_3"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "competences_race/Le Voile de Mouches.png").resize((70, 70), Image.LANCZOS))
    assets["comp_repugnant_4"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "competences_race/La Piste Visqueuse.png").resize((70, 70), Image.LANCZOS))

    # --- Compétences Race Gamer ---
    assets["comp_gamer_1"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "competences_gamer/Le Speedrun Tactique.png").resize((70, 70), Image.LANCZOS))
    assets["comp_gamer_2"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "competences_gamer/Capture d'Écran.png").resize((70, 70), Image.LANCZOS))
    assets["comp_gamer_3"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "competences_gamer/La Lecture du Boss.png").resize((70, 70), Image.LANCZOS))
    assets["comp_gamer_4"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "competences_gamer/Le Taunt Vociférant.png").resize((70, 70), Image.LANCZOS))

    # --- Note: Réutiliser les images Gamer pour Poids Lourd si leurs images ne sont pas fournies ---
    # Pour Poids Lourd, on utilise les mêmes images que Gamer dans l'exemple initial
    # Il serait idéal de créer des assets spécifiques pour Poids Lourd si possible.
    assets["comp_poidslourd_1"] = assets["comp_gamer_1"]  # Le Dépôt de Graisse
    assets["comp_poidslourd_2"] = assets["comp_gamer_2"]  # L'Écrasement Calorique
    assets["comp_poidslourd_3"] = assets["comp_gamer_3"]  # La Réserve de Snacks
    assets["comp_poidslourd_4"] = assets["comp_gamer_4"]  # La Persistance Grasse

    # --- Boutons (Buttons) ---
    assets["btn_backgroundmenu"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "buttons/fond2.png").resize((180, 70), Image.LANCZOS))
    assets["btn_background"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "buttons/fond2.png").resize((120, 40), Image.LANCZOS))
    assets["btn_background2"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "buttons/fondnoir.png").resize((120, 40), Image.LANCZOS))
    assets["btn_background3"] = ImageTk.PhotoImage(
        Image.open(ASSETS_PATH + "buttons/fondvert.png").resize((120, 40), Image.LANCZOS))

    return assets