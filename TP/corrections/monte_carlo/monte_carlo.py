# -*- coding: utf-8 -*-

import random as rnd
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter


def tirer_point_alea(xmin=0, xmax=1, ymin=0, ymax=1):
    """
    Fonction permettant de tirer aléatoirement un point dans un rectangle donné.
    Si les bornes du rectangle ne sont pas renseignées, par défaut, elles
    prennent les valeurs xmin=0, xmax=1, ymin=0 et ymax=1.
    """
    x = rnd.uniform(xmin, xmax)
    y = rnd.uniform(ymin, ymax)
    return x, y


def tirer_points_aleas(n, xmin=0, xmax=1, ymin=0, ymax=1):
    """
    Fonction permettant de tirer aléatoirement n points dans un rectangle donné.
    """
    return [tirer_point_alea(xmin, xmax, ymin, ymax) for _ in range(n)]


def tirer_points_aleas_avec_list_arguments(n, *args):
    """
    Fonction permettant de tirer aléatoirement n points dans un rectangle donné.
    """
    return [tirer_point_alea(*args) for _ in range(n)]


def nb_dans_sous_domaine(n):
    """
    Fonction retournant le nombre de point dans le quart de cercle de rayon 1
    et de centre (0,0) parmi un échantillon de n points.
    La fonction affiche également chaque point testé dans un graphique.

    :param n: nombre de points à tester
    :type n: integer
    :return nb: nombre de points dans le quart de cercle
    :rtype: integer
    """
    nb = 0
    for i in range(n):
        x, y = tirer_point_alea()
        if x ** 2 + y ** 2 <= 1:
            # Le point est dans le cercle
            plt.plot(x, y, 'gx')  # affichage du point en vert
            nb += 1  # on incrémente le résultat
        else:
            # Le point n'est pas dans le cercle
            plt.plot(x, y, 'rx')  # affichage du point en rouge
    return nb


def nb_dans_sous_domaine_avec_list_comphreensions(n):
    """
    Fonction retournant le nombre de point dans le quart de cercle de rayon 1
    et de centre (0,0) parmi un échantillon de n points.
    La fonction affiche également chaque point testé dans un graphique.

    Version list comphreension

    :param n: nombre de points à tester
    :type n: integer
    :return nb: nombre de points dans le quart de cercle
    :rtype: integer
    """
    return len(
        filter(
            lambda point: point[0] ** 2 + point[1] ** 2 <= 1.0,
            tirer_points_aleas(n)
        )
    )


def nb_dans_sous_domaine_avec_list_comphreensions_pour_graphique(n):
    """
    Fonction retournant le nombre de point dans le quart de cercle de rayon 1
    et de centre (0,0) parmi un échantillon de n points.
    La fonction affiche également chaque point testé dans un graphique.

    Version list comphreension
    Version pour l'affichage graphique

    :param n: nombre de points à tester
    :type n: integer
    :return nb: nombre de points dans le quart de cercle
    :rtype: integer
    """
    list_points_avec_flags = map(
        lambda point: (point, int(point[0] ** 2 + point[1] ** 2 <= 1.0)),
        tirer_points_aleas(n)
    )
    return (sum(map(itemgetter(1), list_points_avec_flags)),
            filter(lambda point_flag: point_flag[1], list_points_avec_flags),
            filter(lambda point_flag: not point_flag[1], list_points_avec_flags))


def evaluation_pi(k):
    """
    Fonction qui effectue plusieurs appriximation Pi par la méthode Monte Carlo
    """
    for i in range(1, k):
        n = 10 ** i  # int
        nb = nb_dans_sous_domaine(10 ** i)  # int
        pi = nb / float(n) * 4  # convert to float
        print(pi)


def representation_graphique(n):
    """
    Calcul d'une approximation de Pi et représentation graphique du résultat
    avec matplotlib
    """
    # Approximation de Pi par Monte Carlo avec 1000 points et affichage des points
    # nb = nb_dans_sous_domaine(n)
    nb, list_points_dans_le_quart_de_cercle, list_points_en_dehors_du_quart_de_cercle = nb_dans_sous_domaine_avec_list_comphreensions_pour_graphique(
        n)
    map(lambda point: plt.plot(point[0], point[1], 'gx'),
        map(itemgetter(0), list_points_dans_le_quart_de_cercle)
        )
    map(lambda point: plt.plot(point[0], point[1], 'rx'),
        map(itemgetter(0), list_points_en_dehors_du_quart_de_cercle)
        )
    pi = nb / n * 4
    plt.suptitle(u"Approximation de Pi par la méthode de Monte Carlo")
    plt.title(u"Tirage de {} points => Pi={}".format(n, pi))

    #
    theta = np.linspace(0, 2 * np.pi, 40)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.plot(x, y, 'b-')

    # Affichage du graphique
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def ajouter_plots(points, plot_str=""):
    """
    """
    map(lambda point: plt.plot(point[0], point[1], plot_str),
        map(itemgetter(0), points)
        )


def representation_graphique_avec_list_comphreensions(n):
    """
    Calcul d'une approximation de Pi et représentation graphique du résultat
    avec matplotlib
    """
    # Approximation de Pi par Monte Carlo avec 1000 points et affichage des points
    # nb = nb_dans_sous_domaine(n)
    nb, list_points_dans_le_quart_de_cercle, list_points_en_dehors_du_quart_de_cercle = nb_dans_sous_domaine_avec_list_comphreensions_pour_graphique(
        n)

    # Estimation de PI
    pi = nb / float(n) * 4
    plt.suptitle(u"Approximation de Pi par la méthode de Monte Carlo")
    plt.title(u"Tirage de {} points => Pi={}".format(n, pi))

    #
    ajouter_plots(list_points_dans_le_quart_de_cercle, 'gx')
    ajouter_plots(list_points_en_dehors_du_quart_de_cercle, 'rx')

    #
    theta = np.linspace(0, 2 * np.pi, 40)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.plot(x, y, 'b-')

    # Affichage du graphique
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


if __name__ == '__main__':
    # Question 3
    # evaluation_pi(5)

    # Question 4
    # representation_graphique(10000)
    representation_graphique_avec_list_comphreensions(100)
