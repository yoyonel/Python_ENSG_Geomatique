# -*- coding: utf-8 -*-
# Python 3.x
import sys
# from pathlib import Path # if you haven't already done so
# root = str(Path(__file__).resolve().parents[1])
# Or
from os.path import dirname, abspath
root = dirname(dirname(abspath(__file__)))
sys.path.append(root)
#
from association.association_activites import ajoutActivite, lireTarifsActivites
from association.association_adherent import ajoutAdherent, lireActivitesAdherent, \
    suppression_adherent, changer_liste_activites_adherent
from association.association_cotisation import calculCotisation
from association.association_log import log


log_nom_fichier = "association.log"


def association_activites():
    """

    :return:
    """
    # Activités
    # Ajout des activités
    ajoutActivite("Theatre", 10, "activites.txt")
    ajoutActivite("Flute", 500, "activites.txt")
    ajoutActivite("Piano", 155, "activites.txt")
    ajoutActivite("Danse", 200, "activites.txt")
    # On récupère le dictionnaire des tarifs des activités
    dict_tarifs_activites = lireTarifsActivites("activites.txt")
    # Affichage des résultats/logs
    # print(dico)
    log(log_nom_fichier, 'INFO',
        'Dictionnaire des tarifs des activités: {}'.format(dict_tarifs_activites)
        )

    return dict_tarifs_activites


def association_adherents():
    """

    """
    ajoutAdherent('Dupont', ['Theatre', 'Flute'], "adherents.txt")
    ajoutAdherent('Bob', ['Danse', 'Piano', 'Theatre'], "adherents.txt")
    ajoutAdherent('Alice', ['Danse', 'Theatre'], "adherents.txt")
    #
    liste_activites_pour_alice = lireActivitesAdherent('Alice', 'adherents.txt')
    log(log_nom_fichier, 'INFO',
        "Liste des activités d'Alice: {}".format(liste_activites_pour_alice)
        )
    #
    suppression_adherent('Bob', 'adherents.txt')
    #
    changer_liste_activites_adherent('Alice', ['Piano', 'Flute'], 'adherents.txt')
    liste_activites_pour_alice = lireActivitesAdherent('Alice', 'adherents.txt')
    log(log_nom_fichier, 'INFO',
        "Liste des activités d'Alice après maj: {}".format(liste_activites_pour_alice)
        )
    # print("Liste des activités d'Alice: {}".format(liste_activites_pour_alice))


def association_cotisations(
        dict_tarifs_activites,
        liste_activites=('Danse', 'Theatre', 'Flute', 'Piano')

):
    """

    :param dict_tarifs_activites:
    :param liste_activites:
    :return:
    """
    #
    cotis = calculCotisation(dict_tarifs_activites, liste_activites)
    #
    # print(cotis)
    log(log_nom_fichier, 'INFO',
        "Cotisation pour la liste d'activités {} = {}".format(liste_activites, cotis)
        )

if __name__ == '__main__':
    # Activités
    dict_tarifs_activites = association_activites()

    # Adherents
    association_adherents()

    # Cotisations
    association_cotisations(dict_tarifs_activites)
