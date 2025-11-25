# ------------------ COMPÉTENCES ------------------

# Compétences optionnelles et automatiques pour races et métiers

# Compétences raciales / métiers automatiques (affichage seulement)
competence_raciale_auto = {
    "Gamer": "Le Mode Rage",
    "Repugnant": "Le Repoussoir Social",
    "Poids lourds": "Impact Sismique"
}

competence_metier_auto = {
    "Le Bio-Purificateur": "Purge Vitale",
    "Le Négociateur": "Manipulation de Valeur",
    "Le Mastodonte": "Protection Totale"
}

# ------------------ DONNÉES DES COMPÉTENCES OPTIONNELLES (bonus stats) ------------------

competences_optionnelles_race = {
    "Gamer": {
        "Le Speedrun Tactique": {"pv": 0, "attaque": 0, "vitesse": 4, "defense": 0},
        "Capture d'Écran": {"pv": 0, "attaque": 5, "vitesse": 0, "defense": 0},
        "La Lecture du Boss": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Taunt Vociférant": {"pv": 0, "attaque": 3, "vitesse": 0, "defense": 2},
    },
    "Repugnant": {
        "Le Repas Miasmatique": {"pv": 20, "attaque": 0, "vitesse": -1, "defense": 0},
        "Le Voile de Mouches": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 8},
        "La Piste Visqueuse": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 3},
        "L'Odeur de la Crainte": {"pv": 0, "attaque": 5, "vitesse": 0, "defense": 0},
    },
    "Poids lourds": {
        "Le Dépôt de Graisse": {"pv": 60, "attaque": 0, "vitesse": -2, "defense": 15},
        "L'Écrasement Calorique": {"pv": 20, "attaque": 10, "vitesse": -2, "defense": 0},
        "La Réserve de Snacks": {"pv": 80, "attaque": 3, "vitesse": -3, "defense": 5},
        "La Persistance Grasse": {"pv": 40, "attaque": 0, "vitesse": -1, "defense": 10},
    }
}

competences_optionnelles_metier = {
    "Le Bio-Purificateur": {
        "Le Nuage Désinfectant": {"pv": 10, "attaque": 0, "vitesse": 0, "defense": 2},
        "Le Sceau de Quarantaine": {"pv": 0, "attaque": 0, "vitesse": 0, "defense": 4},
        "La Bombe Fécale": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Laboratoire Portable": {"pv": 15, "attaque": 3, "vitesse": 0, "defense": 0},
    },
    "Le Négociateur": {
        "La Corruption Express": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Bon Deal": {"pv": 10, "attaque": 0, "vitesse": 0, "defense": 0},
        "Le Contrat Piégé": {"pv": 0, "attaque": 4, "vitesse": 0, "defense": 0},
        "L'Évasion Fiscale": {"pv": 0, "attaque": 0, "vitesse": 4, "defense": 0},
    },
    "Le Mastodonte": {
        "Le Blocage Total": {"pv": 0, "attaque": 0, "vitesse": -1, "defense": 20},
        "L'Élan Brutal": {"pv": 0, "attaque": 8, "vitesse": -1, "defense": 0},
        "Le Coup d'Estomac": {"pv": 0, "attaque": 6, "vitesse": 0, "defense": 0},
        "Le Cri de Guerre": {"pv": 0, "attaque": 2, "vitesse": 0, "defense": 10},
    }
}
