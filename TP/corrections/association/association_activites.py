# -*- coding: utf-8 -*-
from association.association_log import log

log_nom_fichier = "association.log"


# 1 Utilisation du fichier des activités
# Q1.1
######
def construireLigneActivite(nom, cotisation, sep_col=', ', sep_ligne='\n'):
    """

    :param nom:
    :type nom: str
    :param cotisation:
    :type cotisation: float
    :param sep_col:
    :type sep_col: str
    :param sep_ligne:
    :type sep_ligne: str
    :return:
    :rtype: str

    :Example:
        >>> construireLigneActivite("natation", 100, ', ', '')
        'natation, 100'

    """

    return "{}{}{}{}".format(nom, sep_col, cotisation, sep_ligne)


def ajoutActivite(nom, cotisation, nom_fichier, separateur=', '):
    """

    :param nom:
    :param cotisation:
    :param nom_fichier:
    :param separateur:
    :return:
    """
    # Q 1.3
    if existeAct(nom, nom_fichier):
        print("L'activité est déjà présente dans le fichier")
    else:
        try:
            with open(nom_fichier, 'a') as fichier:
                # ligne à écrire dans le fichier
                ligne = construireLigneActivite(nom, cotisation, separateur)
                # ecriture de la ligne
                fichier.write(ligne)
            print("Activité {} ajoutée au fichier.".format(nom))

        except FileNotFoundError:
            print("Le fichier {} n'existe pas".format(nom_fichier))
        except IOError:
            print("Erreur à l'ouverture du fichier {}".format(nom_fichier))
######


# Q1.2
def existeAct_with_fo(fichier, nom_act):
    """

    :param fichier:
    :return:

    """
    # lecture du contenu du fichier
    txt = fichier.read()
    # on test si nom_act est présent dans le fichier activité
    # i.e. on test la présence de la chaine de caractère représentant l'activité
    # dans la chaine de caractère représentant le contenu du fichier (activités)
    return nom_act in txt


def existeAct(nom_act, nom_fichier):
    """
    Méthode testant si une activité existe déjà dans un fichier

    :param nom_act:
    :param nom_fichier:
    :return:

    """
    try:
        # ouverture du fichier en lecture 'r'
        with open(nom_fichier, 'r') as fichier:
            return existeAct_with_fo(fichier, nom_act)
    # gestion des exceptions
    except FileNotFoundError:
        # print("Le fichier {} n'existe pas".format(nom_fichier))
        log(log_nom_fichier, 'ERROR', "Le fichier {} n'existe pas".format(nom_fichier))
    except IOError:
        # print("Erreur à l'ouverture du fichier {}".format(nom_fichier))
        log(log_nom_fichier, 'ERROR', "Erreur à l'ouverture du fichier {}".format(nom_fichier))


# Q 1.4
def retourne_colonnes_a_partir_de_ligne(ligne, sep_col=', ', sep_ligne='\n'):
    """

    :param ligne:
    :type ligne: str
    :param sep_col:
    :type sep_col: str
    :param sep_ligne:
    :type sep_ligne: str
    :return:

    :Example:
        >>> retourne_colonnes_a_partir_de_ligne("Flute, 500")
        ('Flute', 500.0)
        >>> retourne_colonnes_a_partir_de_ligne("Piano, 155.0")
        ('Piano', 155.0)
    """
    ligne_decoupee = ligne.split(sep_ligne)[0].split(sep_col)
    try:
        return ligne_decoupee[0], float(ligne_decoupee[1])
    except ValueError:
        # print("Problème pour caster {} en floattant".format(ligne_decoupee[1]))
        log(log_nom_fichier, 'ERROR', "Problème pour caster {} en floattant".format(ligne_decoupee[1]))


def lireTarifsActivites_with_fo(fichier):
    """

    :param fichier:
    :return:
    """
    dico_activites_tarifs = {}
    for ligne in fichier.readlines():  # lecture du fichier ligne par ligne
        key, value = retourne_colonnes_a_partir_de_ligne(ligne)
        dico_activites_tarifs[key] = value
    return dico_activites_tarifs


def lireTarifsActivites(nom_fichier):
    """
    Méthode pour lire les tarifs des activités.
    Cette méthode retourne un dictionnaire dont les clefs sont les noms des activités
    et les valeurs les tarifs correspondants.

    :param nom_fichier:
    :return:
    """
    log(log_nom_fichier, 'INFO', "lireTarifsActivites({})".format(nom_fichier))
    try:
        with open(nom_fichier, 'r') as fichier:
            return lireTarifsActivites_with_fo(fichier)
    except FileNotFoundError:
        # print("Le fichier {} n'existe pas".format(nom_fichier))
        log(log_nom_fichier, 'ERROR', "Le fichier {} n'existe pas".format(nom_fichier))
    except IOError:
        # print("Erreur à l'ouverture du fichier {}".format(nom_fichier))
        log(log_nom_fichier, 'ERROR', "Erreur à l'ouverture du fichier {}".format(nom_fichier))
