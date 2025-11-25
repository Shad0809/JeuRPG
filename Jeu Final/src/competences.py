# src/competences.py

# --- Dictionnaires de compétences optionnelles ---
competences_optionnelles_race = {
    "Répugnant": {
        "L'Odeur de la Crainte": {"pv": 0, "attaque": 5, "vitesse": 0, "defense": 0},
        "Le Repas Miasmatique": {"pv": 20, "attaque": 0, "vitesse": -1, "defense": 0},
        "Le Voile de Mouches": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 8},
        "La Piste Visqueuse": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 3}
    },
    "Gamer": {
        "Le Speedrun Tactique": {"pv": 0, "attaque": 0, "vitesse": 4, "defense": 0},
        "Capture d'Écran": {"pv": 0, "attaque": 5, "vitesse": 0, "defense": 0},
        "La Lecture du Boss": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Taunt Vociférant": {"pv": 0, "attaque": 3, "vitesse": 0, "defense": 2}
    },
    "Poids Lourd": {
        "Le Dépôt de Graisse": {"pv": 60, "attaque": 0, "vitesse": -2, "defense": 15},
        "L'Écrasement Calorique": {"pv": 20, "attaque": 10, "vitesse": -2, "defense": 0},
        "La Réserve de Snacks": {"pv": 80, "attaque": 3, "vitesse": -3, "defense": 5},
        "La Persistance Grasse": {"pv": 40, "attaque": 0, "vitesse": -1, "defense": 10}
    }
}

competences_optionnelles_metier = {
    "BioPurificateur": {
        "comp1": {"pv": 10, "attaque": 5, "vitesse": 0, "defense": 0}
    },
    "Négociateur": {
        "comp1": {"pv": 0, "attaque": 2, "vitesse": 5, "defense": 0}
    },
    "Mastodonte": {
        "comp1": {"pv": 50, "attaque": 10, "vitesse": -3, "defense": 5}
    }
}

# --- Compétences automatiques par race/métier ---
competences_auto_race = {
    "Répugnant": "Puanteur Naturelle",
    "Gamer": "Réflexes Affûtés",
    "Poids Lourd": "Masse Imposante"
}

competences_auto_metier = {
    "BioPurificateur": "Purification",
    "Négociateur": "Art de la Parole",
    "Mastodonte": "Résistance"
}