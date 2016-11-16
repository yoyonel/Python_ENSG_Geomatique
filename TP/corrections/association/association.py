# -*- coding: utf-8 -*-


def ajoutActivite(nom, cotisation, nom_fichier):
    """
    Méthode pour ajouter une activité dans le fichier des activités.

    Usage
    -----
    ajoutActivite(nom str, cotisation int, nomFichier str)

    """
    if existeAct(nom, nom_fichier):
        print("L'activité est déjà présente dans le fichier")
    else:
        try:
            with open(nom_fichier, 'a') as fichier:
                ligne = "{}, {}\n".format(nom, cotisation)  # ligne à écrire dans le fichier
                fichier.write(ligne)
            print("Activité {} ajoutée au fichier.".format(nom))

        except FileNotFoundError:
            print("Le fichier {} n'existe pas".format(nom_fichier))
        except IOError:
            print("Erreur à l'ouverture du fichier {}".format(nom_fichier))


def existeAct(nom_act, nom_fichier):
    """
    Méthode testant si une activité existe déjà dans un fichier

    Usage
    -----
    existeAct(nomAct str, nomFichier str) -> boolean

    """
    try:
        with open(nom_fichier, 'r') as fichier:
            txt = fichier.read()  # contenu du fichier
            if (nom_act in txt):
                return True
            else:
                return False

    except FileNotFoundError:
        print("Le fichier {} n'existe pas".format(nom_fichier))
    except IOError:
        print("Erreur à l'ouverture du fichier {}".format(nom_fichier))


def lireTarifsActivites(nom_fichier):
    """
    Méthode pour lire les tarifs des activités.
    Cette méthode retourne un dictionnaire dont les clefs sont les noms des activités
    et les valeurs les tarifs correspondants.
    """
    dico = {}
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier.readlines():  # lecture du fichier ligne par ligne
                ligne_decoupee = ligne[:-1].split(', ')
                dico[ligne_decoupee[0]] = int(ligne_decoupee[1])

    except FileNotFoundError:
        print("Le fichier {} n'existe pas".format(nom_fichier))
    except IOError:
        print("Erreur à l'ouverture du fichier {}".format(nom_fichier))

    return dico


def calculCotisation(dico_act, liste_act):
    """
    Calcul de la cotisation du par un adhérent
    en fonction des activités auxquelles il est inscrit.

    Usage
    -----
    calculCotisation(dico_act dict, liste_act str[]) -> cotisation int

    Tests
    -----
    >>> calculCotisation({'Flute': 50, 'Piano': 155, 'Theatre': 10}, ['Flute', 'Theatre'])
    60

    >>> calculCotisation({'Piano': 155, 'Flute': 50, 'Danse': 200, 'Theatre': 10}, ['Danse', 'Theatre', 'Flute', 'Piano'])
    379.5

    """
    cotisation = 0
    liste_cotis = []
    activite = None

    try:
        if len(liste_act) < 3:
            # S'il y a moins de 3 activités, il n'y a pas de réduction à appliquer
            for activite in liste_act:
                cotisation += dico_act[activite]
        else:
            # 3 activités ou plus : on applique 10% de réduction au activités les plus chères
            for activite in liste_act:
                liste_cotis.append(dico_act[activite])

            liste_cotis.sort()
            for i in range(0, 2):
                # Plein tarif pour les 2 premières activités
                cotisation += liste_cotis[i]
            for i in range(2, len(liste_cotis)):
                # Réduction de 10% pour les activités suivantes.
                cotisation += liste_cotis[i] * 0.9
    except KeyError:
        print("La clé {} n'est pas présente dans le dictionnaire des activités/cotisations.".format(activite))

    return cotisation


if __name__ == '__main__':
    ajoutActivite("Theatre", 10, "activites.txt")
    ajoutActivite("Flute", 500, "activites.txt")
    ajoutActivite("Piano", 155, "activites.txt")
    ajoutActivite("Danse", 200, "activites.txt")
    dico = lireTarifsActivites("activites.txt")
    print(dico)
    cotis = calculCotisation(dico, ['Danse', 'Theatre', 'Flute', 'Piano'])
    print(cotis)
