# src/main.py

from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import pygame

# Importation des modules locaux
from personnage import Personnage
from competences import (
    competences_optionnelles_race, competences_optionnelles_metier,
    competences_auto_race, competences_auto_metier
)
from audio_manager import initialiser_audio # Utilisation d'une fonction dédiée
from pages.page_menu import menu
from pages.page_race import page_menu as page_menu_race
# --- CORRECTION DE L'ERREUR D'IMPORTATION (1/2) : choisir_comp_race_handler n'existe pas dans le module ---
from pages.page_comp_race import (
    comprepu_menu, compgamer_menu, comppoidlourd_menu # , choisir_comp_race_handler <--- RÉTIRÉ
)
# --- CORRECTION DE L'ERREUR D'IMPORTATION (2/2) : choisir_metier_handler n'existe pas dans le module ---
from pages.page_metier import page_menu2 as page_menu_metier # , choisir_metier_handler <--- RÉTIRÉ
from pages.page_recap import page_recap
from pages.ui_widgets import charger_assets


# --- 1. Initialisation Globale ---

# Initialiser l'audio (Doit être appelé avant tout chargement de fichier audio)
initialiser_audio()


# Instance personnage global
perso = Personnage()

# --- 2. Interface Tkinter (Root et Canvas) ---
root = Tk()
root.geometry("450x700")

# Utilisation du chemin corrigé pour l'icône
icone_path = "assets/images/icons/iconlogo.png"
try:
    # Tkinter peut avoir du mal avec PhotoImage sur certains formats ou avec PIL si non adapté
    # On utilise PIL pour une meilleure compatibilité de chargement
    icone_pil = Image.open(icone_path)
    icone = ImageTk.PhotoImage(icone_pil)
    root.iconphoto(True, icone)
except Exception as e:
    print(f"Erreur lors du chargement de l'icône: {e}")
    # Tentative d'utilisation de PhotoImage standard comme fallback
    try:
        icone = PhotoImage(file=icone_path)
        root.iconphoto(True, icone)
    except:
        print("L'icône n'a pas pu être chargée via PIL ni PhotoImage standard.")

root.resizable(False, False)
root.title("Menu RPG")

canvas = Canvas(root, width=450, height=700, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)

# --- 3. Chargement des Assets Visuels ---
# Cette fonction charge et stocke toutes les images nécessaires
assets = charger_assets()


# --- 4. Fonctions de Navigation et Logique de Jeu ---

def recommencer():
    """Réinitialise le personnage et retourne au menu principal."""
    global perso
    perso = Personnage()
    menu(root, canvas, assets, perso, navigate_to)

def choisir_race(race):
    """
    Sélectionne la race du personnage et navigue vers le menu des compétences de race.
    """
    perso.race = race
    perso.comp_race_auto = competences_auto_race.get(race)

    if race == "Répugnant":
        navigate_to('comprepu_menu')
    elif race == "Gamer":
        navigate_to('compgamer_menu')
    elif race == "Poids Lourd":
        navigate_to('comppoidlourd_menu')

def choisir_comp_race(competence):
    """
    Sélectionne la compétence de race et navigue vers le menu des métiers.
    Cette fonction est le *callback* passé aux pages de compétences.
    """
    perso.comp_race_choisie = competence
    navigate_to('page_menu_metier')

def choisir_metier(metier):
    """
    Sélectionne le métier, applique les bonus et affiche le récapitulatif.
    Cette fonction est le *callback* passé à la page de métier.
    """
    perso.metier = metier
    perso.comp_metier_auto = competences_auto_metier.get(metier)
    # Dans la structure actuelle, la compétence métier est fixe ("comp1")
    perso.comp_metier_choisie = "comp1"

    # Important: Appliquer les bonus une fois que la race et le métier sont choisis
    perso.appliquer_bonus_optionnels(
        competences_optionnelles_race, competences_optionnelles_metier
    )

    navigate_to('page_recap')


# Dictionnaire de navigation pour gérer les transitions de manière centralisée
navigation_map = {
    'menu': lambda: menu(root, canvas, assets, perso, navigate_to),
    'page_menu_race': lambda: page_menu_race(root, canvas, assets, choisir_race),
    'comprepu_menu': lambda: comprepu_menu(root, canvas, assets, choisir_comp_race),
    'compgamer_menu': lambda: compgamer_menu(root, canvas, assets, choisir_comp_race),
    'comppoidlourd_menu': lambda: comppoidlourd_menu(root, canvas, assets, choisir_comp_race),
    'page_menu_metier': lambda: page_menu_metier(root, canvas, assets, choisir_metier),
    'page_recap': lambda: page_recap(root, canvas, assets, perso, recommencer)
}

def navigate_to(page_name):
    """Fonction pour naviguer vers une nouvelle page."""
    if page_name in navigation_map:
        navigation_map[page_name]()
    else:
        print(f"Page inconnue: {page_name}")


# --- 5. Lancement de l'Application ---
navigate_to('menu')
root.mainloop()