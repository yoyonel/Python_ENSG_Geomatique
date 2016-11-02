# -*- coding: utf-8 -*-

import random as rnd
import numpy as np
import matplotlib.pyplot as plt


def tirer_point_alea(xmin=0, xmax=1, ymin=0, ymax=1):
    """
    Fonction permettant de tirer aléatoirement un point dans un rectangle donné.
    Si les bornes du rectangle ne sont pas renseignées, par défaut, elles
    prennent les valeurs xmin=0, xmax=1, ymin=0 et ymax=1.
    """
    x = rnd.uniform(xmin, xmax)
    y = rnd.uniform(ymin, ymax)
    return x, y



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
        if x**2 + y**2 <= 1:
            # Le point est dans le cercle
            plt.plot(x, y, 'gx') # affichage du point en vert
            nb += 1 # on incrémente le résultat
        else:
            # Le point n'est pas dans le cercle
            plt.plot(x, y, 'rx') # affichage du point en rouge
    return nb



def evaluation_pi(k):
    """
    Fonction qui effectue plusieurs appriximation Pi par la méthode Monte Carlo
    """
    for i in range(1, k):
        n = 10**i
        nb = nb_dans_sous_domaine(10**i)
        pi = nb / 10**i * 4
        print(pi)


def representation_graphique(n):
    """
    Calcul d'une approximation de Pi et représentation graphique du résultat
    avec matplotlib
    """
    # Approximation de Pi par Monte Carlo avec 1000 points et affichage des points
    nb = nb_dans_sous_domaine(n)
    pi = nb / n * 4
    plt.suptitle("Approximation de Pi par la méthode de Monte Carlo")
    plt.title("Tirage de {} points => Pi={}".format(n, pi))

    #
    theta = np.linspace(0, 2*np.pi, 40)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.plot(x, y, 'b-')

    # Affichage du graphique
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


if __name__ == '__main__':
    # Question 3
    evaluation_pi(7)

    # Question 4
    representation_graphique(10000)
