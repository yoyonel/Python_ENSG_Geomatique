# -*- coding: utf-8 -*-
from association.association_log import log

log_nom_fichier = "association.log"

default_separateurs = {
    'sep_col': ', ',
    'sep_act': ';',
    'sep_ligne': '\n'
}


def unpack_separateurs(dict_separateurs):
    """

    :param dict_separateurs:
    :return:

    :Example:
    >>> unpack_separateurs(default_separateurs)
    (', ', ';', '\\n')
    """
    return dict_separateurs['sep_col'], dict_separateurs['sep_act'], dict_separateurs['sep_ligne']


# 1 Utilisation du fichier des adhérents
# Q
######
def construireLigneAdherent(nom, liste_activites, dict_separateurs=default_separateurs):
    """

    :param nom:
    :param liste_activites:
    :param dict_separateurs:
    :return:

    :Exemple:
    >>> construireLigneAdherent("Dupont", ['Theatre', 'Piano'])
    'Dupont, Theatre;Piano\\n'
    """
    sep_col, sep_activites, sep_ligne = unpack_separateurs(dict_separateurs)
    #
    return "{}{}{}{}".format(
        nom,
        sep_col,
        sep_activites.join(liste_activites),
        sep_ligne
    )


def ajoutAdherent(nom_adherent, liste_activites, nom_fichier, dict_separateurs=default_separateurs):
    """
    Méthode pour ajouter une activité dans le fichier des activités.

    Usage
    -----
    ajoutAdherent(nom str, liste_activites list, nomFichier str)

    """
    # Q 1.3
    if existeAdherent(nom_adherent, nom_fichier):
        print("L'adhérent {} est déjà présent dans le fichier".format(nom_adherent))
    else:
        try:
            with open(nom_fichier, 'a') as fichier:
                # ligne à écrire dans le fichier
                ligne = construireLigneAdherent(nom_adherent, liste_activites, dict_separateurs)
                # ecriture de la ligne
                fichier.write(ligne)
            print("Adhérent {} ajouté au fichier.".format(nom_adherent))

        except FileNotFoundError:
            print("Le fichier {} n'existe pas".format(nom_fichier))
        except IOError:
            print("Erreur à l'ouverture du fichier {}".format(nom_fichier))
######


# # Q1.2
def existeAdherent_with_fo(fichier, nom_adherent):
    """

    :param fichier:
    :return:
    """
    # lecture du contenu du fichier
    txt = fichier.read()
    # on test si nom_adherent est présent dans le fichier des adhérents
    # i.e. on test la présence de la chaine de caractère représentant le nom de l'adhérent
    # dans la chaine de caractère représentant le contenu du fichier (adhérents)
    return nom_adherent in txt


def existeAdherent(nom_adherent, nom_fichier):
    """
    Méthode testant si un adhérent est déjà présent dans un fichier

    Usage
    -----
    existeAdherent(nom_adherent str, nom_fichier str) -> boolean

    """
    try:
        # ouverture du fichier en lecture 'r'
        with open(nom_fichier, 'r') as fichier:
            return existeAdherent_with_fo(fichier, nom_adherent)
    # gestion des exceptions
    except FileNotFoundError:
        print("Le fichier {} n'existe pas".format(nom_fichier))
    except IOError:
        print("Erreur à l'ouverture du fichier {}".format(nom_fichier))


# Q 1.4
def decoupage_ligne(ligne, dict_separateurs=default_separateurs):
    """

    :param ligne:
    :param dict_separateurs:
    :return:

    :Example:
    >>> decoupage_ligne("Dupont, Theatre;Piano\\n")
    ['Dupont', 'Theatre;Piano']
    """
    sep_col, sep_activites, sep_ligne = unpack_separateurs(dict_separateurs)
    return ligne.split(sep_ligne)[0].split(sep_col)


def extraction_nom_adherent_a_partir_d_une_ligne(ligne, dict_separateurs=default_separateurs):
    """

    :param ligne:
    :param dict_separateurs:
    :return:

    :Example:
    >>> extraction_nom_adherent_a_partir_d_une_ligne("Dupont, Theatre;Piano\\n")
    'Dupont'
    """
    return decoupage_ligne(ligne, dict_separateurs)[0]


def extraction_liste_actitivites_a_partir_d_une_ligne(ligne, dict_separateurs=default_separateurs):
    """

    :param ligne:
    :param dict_separateurs:
    :return:

    :Example:
    >>> extraction_liste_actitivites_a_partir_d_une_ligne("Dupont, Theatre;Piano\\n")
    ['Theatre', 'Piano']
    """
    str_activites = decoupage_ligne(ligne, dict_separateurs)[1]
    sep_col, sep_activites, sep_ligne = unpack_separateurs(dict_separateurs)
    return str_activites.split(sep_activites)


def lireActivitesAdherent_with_fo(nom_adherent, fichier):
    """

    :param nom_adherent:
    :param fichier:
    :return:

    :Example:
    """

    # dico_activites_tarifs = {}
    for ligne in fichier.readlines():  # lecture du fichier ligne par ligne
        nom_adherent_courant = extraction_nom_adherent_a_partir_d_une_ligne(ligne)
        if nom_adherent_courant == nom_adherent:
            return extraction_liste_actitivites_a_partir_d_une_ligne(ligne)
    # LOG
    log(log_nom_fichier, 'WARNING',
        "L'adhérent {} n'est pas présent dans le fichier adhérent".format(nom_adherent))
    #
    return []


def lireActivitesAdherent(nom_adherent, nom_fichier):
    """
    Méthode pour lire les activités d'un adhérent
    Cette méthode retourne un dictionnaire dont les clefs sont les noms des activités
    et les valeurs les tarifs correspondants.
    """
    try:
        with open(nom_fichier, 'r') as fichier:
            return lireActivitesAdherent_with_fo(nom_adherent, fichier)
    except FileNotFoundError:
        log(log_nom_fichier, 'ERROR', "Le fichier {} n'existe pas".format(nom_fichier))
    except IOError:
        log(log_nom_fichier, 'ERROR', "Erreur à l'ouverture du fichier {}".format(nom_fichier))


def suppression_adherent(nom_adherent, nom_fichier):
    """

    :param nom_adherent:
    :param nom_fichier:
    :return:
    """
    adherent_trouve = False
    try:
        with open(nom_fichier, "r+") as fichier:
            d = fichier.readlines()
            fichier.seek(0)
            for line in d:
                if extraction_nom_adherent_a_partir_d_une_ligne(line) != nom_adherent:
                    fichier.write(line)
                else:
                    log(log_nom_fichier, 'INFO', "Suppression de l'adherent {} du fichier {}".format(nom_adherent, nom_fichier))
                    adherent_trouve = True
            fichier.truncate()
    except FileNotFoundError:
        log(log_nom_fichier, 'ERROR', "Le fichier {} n'existe pas".format(nom_fichier))
    except IOError:
        log(log_nom_fichier, 'ERROR', "Erreur à l'ouverture du fichier {}".format(nom_fichier))

    if not adherent_trouve:
        log(log_nom_fichier, 'WARNING',
            "L'adhérent {} n'a pas été trouvé dans le fichier {}".format(nom_adherent, nom_fichier)
            )
    #
    return adherent_trouve
