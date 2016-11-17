# -*- coding: utf-8 -*-

import doctest

import association


def test():
    return doctest.testmod(association)


if __name__ == "__main__":
    print(test())

"""

Pour générer la documentation html avec sphinx :

1. Installer sphinx : pip3 install Sphinx
2. Créer un répertoire docs dans le répertoire du projet : mkdir docs
3. Dans le répertoire du projet : sphinx-quickstart
    * choisir de séparer les répertoires build et source
    * activer l'extension autodoc (taper y)
4. Editer le fichier docs/source/conf.py pour :
    * decommenter les lignes suivantes et ajouter le chemin erlatif vers votre projet
    * import os / import sys / sys.path.append(0, os.path.abspath('../../..'))
5. Exécuter la récupération automatique de la doc à partir des docstrings : sphinx-apidoc -f -o docs/source/ /
6. Générer la doc en html, depuis le répertoire docs : make html

Liens:
- http://gisellezeno.com/tutorials/sphinx-for-python-documentation.html
- https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
- http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
- http://stackoverflow.com/questions/15972544/how-to-document-an-exception-using-sphinx
"""
