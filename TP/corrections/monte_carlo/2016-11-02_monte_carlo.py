# -*- coding: utf-8 -*-

import random as rnd
import numpy as np
import matplotlib.pyplot as plt


def point_alea(xmin=0, xmax=1, ymin=0, ymax=1):
    """
	Tirage aléatoire d'un point dans un rectangle.

    Fonction permettant de tirer aléatoirement un point dans un rectangle donné.
    Si les bornes du rectangle ne sont pas renseignées, par défaut, elles
    prennent les valeurs xmin=0, xmax=1, ymin=0 et ymax=1.

	:param xmin: coordonnées x minimale du rectangle
	:param xmax: coordonnées x maximale du rectangle
	:param ymin: coordonnées y minimale du rectangle
	:param ymin: coordonnées y maximale du rectangle
	:return: coordonnées x et y du point
    """
    x = rnd.uniform(xmin, xmax)
    y = rnd.uniform(ymin, ymax)
    return x, y


def points_alea(n, xmin=0, xmax=1, ymin=0, ymax=1):
	"""
	Tirage de n points aléatoires dans un rectangle donné.

	:param n: nombre de points à tirer
	:param xmin: coordonnées x minimale du rectangle
	:param xmax: coordonnées x maximale du rectangle
	:param ymin: coordonnées y minimale du rectangle
	:param ymin: coordonnées y maximale du rectangle
	:return: liste de coordonnées (x, y) du point
	"""
	return [point_alea(xmin, xmax, ymin, ymax) for i in range(n)]


def est_dans_cercle(x, y, x0=0, y0=0, r=1):
	"""
	Indique si le point (x,y) est dans le cercle de centre (x0,y0), de rayon r.

	:param x: coordonnée x du point
	:param y: coordonnée y du point
	:param x0: coordonnée x du centre du cercle
	:param y0: coordonnée y du centre du cercle
	:param r: rayon du cercle
	:return: booléen indiquant si le point est dans le cercle
	"""
	d2 = (x-x0)**2 + (y-y0)**2
	return (d2 < r**2)


def nb_dans_sous_domaine(points):
	"""
	Fonction retournant le nombre de points dans le quart de cercle de rayon 1 
	et de centre (0,0).

    :param points: liste de coordonnées (x,y)
	:return: nombre de points dans le quart de cercle
	"""
	nb = 0
	for point in points:
		if est_dans_cercle(point[0], point[1]):
			nb += 1
	return nb


def affichage_point(x, y):
	"""
	Affichage d'un point (x, y) dans un graphique matplotlib.

	La couleur du point dépend de sa position : vert s'il est dans le 
	sous-domaine considéré, rouge sinon.
    La fonction affiche également chaque point testé dans un graphique
	matplotlib.

    :param x: coordonnée x du point
    :param y: coordonnée x du point
	"""
	if est_dans_cercle(x, y):
		# Le point est dans le cercle
		plt.plot(x, y, 'gx') # affichage du point en vert
	else:
		# Le point n'est pas dans le cercle
		plt.plot(x, y, 'rx') # affichage du point en rouge


def representation_graphique(points, nb, pi):
	"""
    Représentation graphique du résultat
    avec matplotlib
	"""
	# Affichage des points tirés
	for (x,y) in points:
		affichage_point(x, y)

	# Affichage du cercle
	theta = np.linspace(0, 2*np.pi, 50)
	x = np.cos(theta)
	y = np.sin(theta)
	plt.plot(x, y, 'b-')

	# Titre du graphique
	plt.suptitle("Approximation de Pi par la méthode de Monte Carlo")
	plt.title("Tirage de {} points => Pi={}".format(len(points), pi))

	# Affichage du graphique
	plt.xlim(0, 1)
	plt.ylim(0, 1)
	plt.show()


	
if __name__ == '__main__':
    # Question 7
	for i in range(1, 7):
		n = 10**i
		points = points_alea(n)
		nb = nb_dans_sous_domaine(points)
		pi = nb / n * 4
		print("Tirage de {} points => Pi={}".format(n, pi))

	# Affichage avec matplotlib
	n = 10000
	points = points_alea(n)
	nb = nb_dans_sous_domaine(points)
	pi = nb / n * 4
	representation_graphique(points, nb, pi)
