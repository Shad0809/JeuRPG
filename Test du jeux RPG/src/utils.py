# ------------------ AIDES UTILITAIRES ------------------

def afficher_title(txt):
    print("\n" + "-" * 12 + " " + txt + " " + "-" * 12 + "\n")


def choix_numero(prompt, n):
    """Retourne un int valide entre 1 et n."""
    while True:
        rep = input(prompt).strip()
        if rep.isdigit():
            val = int(rep)
            if 1 <= val <= n:
                return val
        print(f"Entrée invalide. Tape un nombre entre 1 et {n}.")
