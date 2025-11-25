# 🛡️ Oignon Ring's RPG : La Création du Héros 🧅

## ✨ Description du Projet

Oignon Ring's RPG est un jeu de rôle (RPG) axé sur la création de personnage, développé entièrement en Python avec l'interface graphique Tkinter. Le joueur est guidé à travers un processus de sélection engageant :

* Choix d'une **Race** unique (Répugnant, Gamer, Poids Lourd).
* Sélection d'une **Compétence Raciale** offrant des bonus spécifiques.
* Choix d'un **Métier** (BioPurificateur, Négociateur, Mastodonte).

Le jeu calcule automatiquement les statistiques finales de votre héros et inclut une interface utilisateur complète ainsi qu'une musique d'ambiance immersive gérée par Pygame.

---

## 📂 Structure du Projet

Le projet est organisé de manière modulaire pour une meilleure maintenabilité, avec l'intégralité du code source et des assets contenus dans `src/`.

/projet_rpg/ ├── src/ │ ├── main.py # 🚀 Point d'entrée et gestion de la navigation. │ ├── personnage.py # 📊 Classe Personnage, gestion des statistiques. │ ├── competences.py # 📚 Dictionnaires des bonus et définitions des compétences. │ ├── audio_manager.py # 🎵 Module d'initialisation et de contrôle de la musique. │ ├── pages/ # 🖼️ Dossier regroupant la logique de chaque écran de l'interface. │ │ ├── page_menu.py │ │ ├── page_race.py │ │ ├── page_comp_race.py │ │ ├── page_metier.py │ │ ├── page_recap.py │ │ └── ui_widgets.py # Helpers pour le chargement des images et des composants UI. │ └── assets/ # Toutes les ressources (images, audio, polices). │ ├── images/ │ ├── audio/ │ └── fonts/ ├── tests/ # 🧪 Dossier pour les tests unitaires. ├── docs/ # 📄 Documentation et schémas (ex: diagrammes UML). └── README.md


---

## ⚙️ Installation et Lancement

Pour lancer Oignon Ring's RPG, suivez ces étapes simples :

1.  **Clonage du Dépôt :**

    ```bash
    git clone <lien_du_repo>
    cd projet_rpg
    ```

2.  **Installation des Dépendances :**

    ```bash
    # Assurez-vous d'avoir Python 3.10 ou supérieur
    pip install -r requirements.txt
    ```

3.  **Lancement du Jeu :**

    ```bash
    python src/main.py
    ```

---

## 🌟 Fonctionnalités Clés

| Catégorie | Description |
| :--- | :--- |
| **Création du Héros** | Choix parmi 3 Races (Répugnant, Gamer, Poids Lourd) et 3 Métiers (BioPurificateur, Négociateur, Mastodonte). |
| **Système de Stats** | Application dynamique des bonus de compétence et de métier aux PV, Attaque, Vitesse et Défense. |
| **Interface** | Utilisation de Tkinter et Pillow pour une interface graphique complète avec chargement d'assets thématiques. |
| **Audio** | Musique d'ambiance en boucle gérée par Pygame pour immerger le joueur. |
| **Récapitulatif** | Affichage de l'ensemble des choix et des statistiques finales sur la page récap. |

---

## 💻 Technologies Utilisées

| Technologie | Rôle |
| :--- | :--- |
| **Python** 3.10+ | Langage de programmation principal. |
| **Tkinter** | Framework pour le développement de l'interface graphique (GUI). |
| **Pillow (PIL)** | Essentiel pour la manipulation, le redimensionnement et l'affichage des images (assets). |
| **Pygame** | Utilisé spécifiquement pour la gestion simple de la lecture audio (musique). |

---

## 🧪 Tests

La fiabilité du calcul des statistiques est primordiale. Les tests unitaires se trouvent dans le dossier `tests/` et couvrent :

* `test_personnage.py` : Vérification que la classe `Personnage` applique correctement les bonus de compétences.
* `test_competences.py` : Assurance de la bonne structure et du contenu des dictionnaires de compétences.

---

## ✍️ Auteurs

Ce projet a été développé par :

* **Mattéo**
* **Maxime**

Studio : *DiapoDeMerde Studio*

---

## ⚖️ Licence

Ce projet est **libre** pour un usage personnel et pédagogique.