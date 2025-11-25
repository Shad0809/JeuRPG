# src/audio_manager.py
import pygame

def initialiser_audio():
    """Initialise le mixeur Pygame et lance la musique en boucle."""
    try:
        pygame.mixer.init()
        # Chemin corrigé: assets/audio/music.mp3
        pygame.mixer.music.load("assets/audio/music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("Audio initialisé et musique lancée.")
    except pygame.error as e:
        print(f"Erreur lors de l'initialisation audio ou du chargement de la musique: {e}")