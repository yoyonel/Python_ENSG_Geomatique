# -*- coding: utf-8 -*-

"""
Jeu de mastermind en python.
"""

from random import randint


codesCouleurs = {"R":0, "B":1, "J":2, "V":3, "N":4, "M":5, "F":6, "O":7}
couleursCodes = {0:"R", 1:"B", 2:"J", 3:"V", 4:"N", 5:"M", 6:"F", 7:"O"}
nomsCouleurs = {"R":"Rouge", "B":"Bleu", "J":"Jaune", "V":"Vert", "N":"Noir", "M":"Marron", "F":"Fushia", "O":"Orange"}


def verification(sol, prop):
    """
    Fonction de vérification d'une combinaison.

    Retourne le nombre de pions biens placés et le nombre de pions présents
    dans la solution mais mal placés.

    Usage
    -----
    verification(int[] sol, int[] prop)


    Tests
    -----
    >>> verification([1, 4, 2, 1], [1, 2, 5, 4])
    (1, 2)

    >>> verification([1, 1, 2, 2], [1, 2, 1, 1])
    (1, 2)

    """
    nb_bien = 0 # nombre de pions bien placés
    nb_mal = 0 # nombre de pions présents mais à la mauvaise place
    n = len(sol) # taille de la combinaison

    # Détection des couleurs bien placées
    i = 0
    while i < n:
        if sol[i] == prop[i]:
            # La couleur est bien placée
            nb_bien += 1
            # On modifie les combinaisons pour éviter compter 2 fois les doubles
            sol[i] = "x"
            prop[i] = "y"
        i += 1

    # Détection des couleurs mal placées
    i = 0
    while i < n:
        j = 0
        while j < n:
            if sol[i] == prop[j]:
                # La couleur est présente dans la solution mais mal positionnnée
                nb_mal += 1
                # Modification pour éviter les erreurs dus aux doubles
                sol[i] = "x"
                prop[j] = "y"
                break
            j += 1
        i += 1

    return nb_bien, nb_mal


def copie(liste):
    """
    Fonction de copie profonde d'une liste(
    """
    copie = []
    i = 0
    while i < len(liste):
        copie.append(liste[i])
        i = i + 1
    return copie



def tirage_aleatoire(nb_pions, double = True):
    """
    Fonction de tirage alétoire de couleurs. Par défaut les tirages de couleur
    en double sont autorisés.
    """
    combi = []

    i = 0
    while (i < nb_pions):
        c = randint(0, 7)
        while (c in combi and not double):
            c = randint(0, 7)
        combi.append(c)
        i += 1

    return combi



def affiche_indications(nb_places, nb_couleurs, prop):
    """
    Fonction permettant d'afficher les indications données au joueur (nombre
    bien placés, nom mal palcés, rappel de la proposition
    """
    nb_pions = len(prop)

    msg = ""

    for i in range(nb_pions - nb_couleurs):
        msg += "   "

    for i in range(nb_couleurs):
        msg += " * "

    msg += " "

    for c in prop:
        msg += couleursCodes[c]

    msg += " "

    for i in range(nb_places):
        msg += " * "

    print(msg)



def saisie(nb_pions):
    """
    Fonction permettant la saisie d'une combinaison par l'utilisateur
    """
    saisie = input("Votre proposition ? ").upper()

    # On vérifie que la proposition comporte le bon nombre d'entrées
    if len(saisie) != nb_pions:
        print("La proposition doit contenir " + str(nb_pions) + " couleurs !")
        return None

    # On vérifie que les entrées sont bien des couleurs admises
    for c in saisie:
        if c not in codesCouleurs.keys():
            print(str(c) + " : valeur incorrect. La proposition doit contenir uniquement des couleurs de " + str(codesCouleurs.keys()))
            return None

    # La saisie est correcte : on transforme en liste d'entiers.
    prop = []
    for c in saisie:
        prop.append(codesCouleurs[c])

    return prop


def jouer(nb_pions, nb_coups, nb_couleurs = 8, double = True):
    """
    Méthode permettant de jouer.
    """

    # Préparation
    sol = tirage(nb_pions, nb_couleurs, double) # combinaison à découvrir
    print("Tirage de " + str(nb_pions) + " couleurs effectué.")
    print("Vous avez " + str(nb_coups) + " coups pour découvrir la solution.")

    # Début de la partie
    n = 0
    trouve = False
    while (n < nb_coups and trouve == False):
        # Tant que l'on a pas atteind le nombre de coups max ou touvé la solution, on continue
        prop = saisie(nb_pions) # Saisie d'une proposition
        while (prop is None):
            prop = saisie(nb_pions)

        # Vérification de la proposition par rapport à la solution
        copie_sol = copie(sol)
        copie_prop = copie(prop)

        nb_bien, nb_mal = verification(copie_sol, copie_prop)

        afficheIndications(nb_pions, nb_bien, nb_mal, prop)

        if (nb_places == nb_pions):
            # si tous les pions sont bien placés, on a trouvé la solution
            trouve = True

        n += 1

    # Fin de la partie
    if trouve == True:
        print("Bravo ! Vous avez trouvé la solution en " + str(n) + "coups")
    else:
        msg = ""
        for c in sol:
            msg += couleursCodes[c]
        print("Perdu ! La solution était : " + msg)





if __name__ == "__main__":
    pass
##    jouer(5, 12, 8, False)

