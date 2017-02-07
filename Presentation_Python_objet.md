% Python objet
% Division des enseignements en informatique
% 2017



# Rappels et bonnes pratiques - l'itération #
## L'itération en Python ##

* Itérer sur les éléments pas sur les indices

``` python
liste = [2, 5, 4, 8, 1]

for e in liste:
	e += 1
```

</br>

*Est mieux que :*
``` python
liste = [2, 5, 4, 8, 1]

for i in range(len(liste)):
	liste[i] += 1
```


## L'itération en Python ##
</br>

``` python
>>> liste = [1 for i in range(10000000)]
>>> t_start = time.time()
>>> for e in liste:
...	    e += 1
...
>>> t_stop = time.time()
>>> print(t_stop - t_start)
0.6951391696929932
```


## L'itération en Python ##
</br>

``` python
>>> liste = [1 for i in range(10000000)]
>>> t_start = time.time()
>>> for i in range(len(liste):
...	    liste[i] += 1
...
>>> t_stop = time.time()
>>> print(t_stop - t_start)
1.4717938899993896
```


## L'itération en Python ##
</br>

``` python
>>> liste = [1 for i in range(10000000)]
>>> t_start = time.time()
>>> i = 0
>>> while i < len(liste):
...	    liste[i] += 1
...     i += 1
...
>>> t_stop = time.time()
>>> print(t_stop - t_start)
3.251149892807007
```


## Les listes de compréhension ##

* Appliquer un traitement sur les éléments d'un ensemble

``` python
nouvelle_liste = [e**2 for e in liste]
```

</br>

*Est mieux que :*
``` python
nouvelle_liste = []
for e in liste:
	nouvelle_liste.append(e**2)
```


## Les listes de compréhension ##
</br>

``` python
>>> liste = [1 for i in range(10000000)]
>>> t_start = time.time()
>>> liste = [e+1 for e in liste]
>>> t_stop = time.time()
>>> print(t_stop - t_start)
0.5306060314178467
```



# Rappels et bonnes pratiques - les fonctions #
## Nombre variable d'arguments ##

* Passer un nombre indéterminé d'arguments à une fonction
	* Utilisation de l'opérateur `*` avant l'argument : `*args`
	* `args` est un tuple dans la fonction

</br>

``` python
def somme(*args):
	s = 0
	for arg in args:
		s += arg
	return s
```


## Nombre variable d'arguments ##

* Passer un nombre indéterminé d'arguments nommés
	* Utilisation de l'opérateur `**` avant l'argument : `**kwargs`
	* `kwargs` est un dictionnaire dans la fonction

</br>

``` python
def presentation(**kwargs):
	for key, val in kwargs:
		print("{} = {}".format(key, value))
```

``` python
>>> presentation(nom="Mousse", prenom="Emma", age=22)
age = 22
prenom = Emma
nom = Mousse
```



# Rappels et bonnes pratiques - les exceptions #
## Les messages d'erreurs ##

* Un exemple : le fichier `script.py` contient

</br>

``` python
def une_fonction(a):
    return 1 / a
 
def une_autre_fonction():
    une_fonction(0)
 
une_autre_fonction()
```


## Les messages d'erreurs ##

* Lecture du message d'erreur de bas en haut
	* *pile des appels*

</br>

``` python
Traceback (most recent call last):
  File "script.py", line 7, in <module>
    une_autre_fonction()
  File "script.py", line 5, in une_autre_fonction
    une_fonction(0)
  File "script.py", line 2, in une_fonction
    return 1 / a
ZeroDivisionError: division by zero
```


## Les exceptions ##

> Mécanisme pour gérer des erreurs survenues lors de l'exécution d'un programme.

* Apporter une solution à un problème bloquant
* Eviter d'interrompre le programme
* D'autres solutions, mais c'est la manière de faire en Python
	* *on essaye de faire et on avisera si ça ne fonctionne pas*


## Soulever une exception ##

* Mot-clé `raise`
* Signaler volontairement une anomalie quand elle se produit 

</br>

``` python
def ma_fonction(age):
	if age < 0:
		raise ValueError("'age' doit etre positif !")
	# suite de la fonction
```

``` python
>>> ma_fonction(-2)
Traceback (most recent call last):
  File "<interactive input>", line 1, in <module>
  File "<interactive input>", line 3, in ma_fonction
ValueError: 'age' doit etre positif !
```


## Traiter d'une exception ##

* Mots-clé `try / except`

``` python
try:
	# ce qui peut produire une exception
except NomException:
	# ce qu'il faut faire si l'exception se déclanche
```

</br>

``` python
liste = ['toto', 'titi', 'tata'...]
try:
	choix = liste[10 // i]
except ZeroDivisionError:
	print("Division par zero impossible")
	choix = liste[0]
except IndexError:
	print("Probleme d'index")
	choix = liste[len(liste)]
```


## Traiter d'une exception ##

* `finally` et `else`

``` python
try:
	# ce qui peut produire une exception
except NomException:
	# ce qu'il faut faire si l'exception se déclanche
else:
	# ce qu'il faut faire si aucune exception n'a été levée
finally:
	# ce qui sera exécuté dans tous les cas, qu'une exception ait eu lieu ou pas
```


## Traiter une exception ##
</br>

``` python
try:
	f = open('fichier.txt', 'w')
	# écriture dans le fichier
except IOError:
	print("Probleme lors de l'écriture du fichier")
else:
	print("Ecriture OK")
finally:
	f.close()
```


## Remarque ##

* Astuce contre les oublis de fermeture de fichier

``` python
try:
    with open('fichier.txt', 'w') as f:
        # écriture dans le fichier
except (IOError, FileNotFoundError):
    # gérer l'erreur
```


## Exceptions fréquentes ##

* Ce que signifient les exceptions courantes :
	* `NameError`
		* variable ou fonction manipulée non déclarée
	* `TypeError`
		* type de la variable incohérent avec l'opération demandée
	* `ValueError`
		* le type est correct, mais pas la valeur
	* `ZeroDivisionError`
		* division par zéro
	* `IndexError` / `KeyError`
		* tentative d'accès à une séquence/dictionnaire avec un indice/clé inexistant 
	* `FileNotFoundError`
		* le fichier n'existe pas
	* `IOError`
		* erreur lors de la manipulation d'un fichier
	* `SyntaxError`
		* erreur de syntaxe (indentation, parenthèse...)



# Rappels et bonnes pratiques - doctest #
## Documentation ##
* Expliquer ce que font les fonctions, classes, modules...
* Indispensable pour rendre le code exploitable par d'autres

``` python
def ma_fonction(a, b):
	"""
	Ligne générale de description de ce que fait la fonction

	Description plus détaillé, si besoin, de comment la fonction
	fait ce qu'elle fait, de ce qu'elle utilise...

	:param a: description de ce que contient a
	:type a: type de la valeur attendue dans a
	:param b: description de ce que contient b
	:type b: type de la valeur attendue dans b
	:return: description de ce que retourne la fonction
	:returntype: type de la valeur retournée par la fonction 
	"""
```


## Les tests unitaires ##



# Rappels et bonnes pratiques - en vrac #
## Modules et imports ##

* `import math`
	* importe l'espace de nom du module `math`
	* => `math.cos(x)`
* `from math import *`
	* importe les fonctions du module `math` dans l'espace de nom courant
	* => `cos(x)`
		* attention aux conflits si deux fonctions portent le même nom !
* `from math import cos`
	* import la fonction `cos()` du module `math` dans l'espace de nom courant
	* => `cos(x)`


## Modules et imports ##

* Python recherche les modules dans le PYTHONPATH (variable d'environnement)
	* `sys.path` en Python

``` python
>>> import sys
>>> sys.path
['',
 'C:\\Windows\\system32\\python34.zip',
 'C:\\Python34\\Lib',
 'C:\\Python34\\DLLs',
 'C:\\Python34',
 'C:\\Python34\\lib\\site-packages']
```

* Contenu du PYTHONPATH :
	* **répertoire courant**
	* `sites-packages`
	* ...
		* c'est une liste => `append(...)` possibles


## Modules et imports ##

* Package
	* Ensemble de modules
	* Répertoire avec un fichier `__init__.py`

```
--repertoire_courant
   |--package
      |-- __init__.py
      |-- module2.py
   |--repertoire
      |-- module1.py
```

</br>

<p style="font-size:16pt">avec Python lancé depuis `repertoire_courant`</p>

``` python
>>> import package           # on importe tous le package
>>> import package.module1   # on importe module1 seulement
>>> import repertoire
ImportError: No module named repertoire
>>> import repertoire.module2
ImportError: No module named repertoire.module2
```


## Bonnes pratiques ##

* Utilisation de la documentation
	* comment utiliser une fonction ? `help(fonction)`
	* quelles sont les fonctions de ce module ? `dir(module)`
	* où trouver de la doc en ligne ? <https://docs.python.org/3.5/>


## Bonnes pratiques ##

* 20 lignes max par fonction
	* au delà cela devient souvent trop compliqué !
* 1 fonction = 1 tâche
	* découper en sous-fonctions pour rendre maintenable et testable
* 1 fichier = 1 classe
	* séparer les éléments qui ne sont pas liés
* Utiliser `if __name__ == '__main__':` pour exécuter le code
	* la console ne sauvegarde pas vos tests
	* code à la racine exécuté lors d'un import
* Testez votre code *en live*
	* profitez que Python ne soit pas compilé pour exécuter facilement le code


## Conventions ##

Respecter les conventions pour faciliter la lecture et la compréhension

``` python
nom_de_variable
nom_de_fonction
NomDeClasse
```


## Conventions ##

``` python
a = b + c
```

</br>

*Est mieux que :*
``` python
a=b+c
```


## Conventions ##

``` python
dict = {'a': 1, 'b': 2, 'c': 3*4}
```

</br>

*Est mieux que :*
``` python
dict={'a':1 , 'b':2,'c':3 * 4}
```


## Conventions ##

``` python
def fonction_qui_compare(a, b=0):
    if a > b:
        return True
    else:
        return False
```

</br>

*Est mieux que :*
``` python
def fonctionQuiCompare ( a , b = 0 ) :

    if (a>b):
        return True

    else:
        return False
```



# Python objet #

## Déclaration d'une classe ##

* Utilisation du mot-clé `class`

``` python
class MaClasse(object):
	...
	...
```

* Convention : 
	* 1ère lettre des mots en majuscule
	* pas d'espace, tiret, underscore...
	* `MonNomDeClasse`


## Instanciation d'un objet ##

> L'objet est une instance de classe.

* On en crée autant que l'on veut

</br>

``` python
mon_objet1 = MaClasse()
mon_objet2 = MaClasse()
mon_objet3 = MaClasse()
```


## Les méthodes ##

> Une méthode est une fonction définie à l'intérieur d'une classe.

* Pour l'utiliser
	* on fait précéder le nom de la méthode du nom de l'objet

</br>

``` python
>>> class MaClasse(object):
... 	def une_methode(param):
... 		print("Une méthode qui fait quelque chose")
...
>>> mon_objet = MaClasse()
>>> mon_objet.une_methode()
Une méthode qui fait quelque chose
``` 


## Les méthodes ##

* Instance appelant la méthode = 1er paramètre de la méthode 
	* nommé `self` par convention
	* spécificité de Python

</br>

``` python
>>> class MaClasse(object):
...     def une_methode(self):
...         print(self)
...
>>> mon_objet = MaClasse()
>>> print(mon_objet)
<__main__.DescriptionDeLObjet object at 0x059F0190>
>>> mon_objet.une_methode()
<__main__.DescriptionDeLObjet object at 0x059F0190>
```


## Les attributs ##

> Un attribut est une variable définie à l'intérieur d'une classe.

* Pour y accéder
	* on fait précéder le nom de l'attribut du nom de l'instance
	* ou de `self` si on est dans la classe

``` python
>>> class MaClasse(object):
...     def afficher(self):
...         print(self.un_attribut)
...
>>> mon_objet = MaClasse()
>>> mon_objet.un_attribut = 48
>>> mon_objet.afficher()
48
>>> un_attribut  # n'existe pas en dehors de la classe
NameError: name 'un_attribut' is not defined
```


## Le constructeur ##

* Méthode appelée lors de la création des objets
	* initialise les valeurs des attributs

</br>

``` python
>>> class MaClasse(object):
... 	def __init__(self):
... 		self.un_attribut = "valeur initiale"
... 		print("Objet créé. Attributs initialisés.")
...
>>> mon_objet = MaClasse()
Objet créé. Attributs initialisés.
>>> mon_objet.un_attribut
"valeur initiale"
```


## Le constructeur ##

* Possibilité de passer des paramètres pour personnaliser les objets

</br>

``` python
>>> class MaClasse(object):
... 	def __init__(self, valeur):
... 		self.un_attribut = valeur
...
>>> mon_objet = MaClasse("valeur personnalisée")
>>> mon_objet.un_attribut
"valeur personnalisée"
```


## Méthodes spéciales ##

> Nous appelerons méthodes spéciale une méthode exécutée sans qu'on ai besoin de l'appeller explicitement.

* `__init__()` par exemple
* Leur nom commence et termine par `__` (deux underscores)
* Utile pour personnaliser le comportement d'un objet


## Méthodes spéciales ##

``` python
>>> class MaClasse(object):
... 	def __init__(self, valeur):
... 		self.un_attribut = valeur
...
>>> mon_objet = MaClasse("17")
>>> print(mon_objet)
<__main__.MaClasse object at 0x051D5DF0>
```

``` python
>>> class MaClasse(object):
... 	def __init__(self, valeur):
... 		self.un_attribut = valeur
...     def __str__(self):
...         print("Instance de MaClasse (valeur de un_attribut = {})".format(self.un_attribut)
...
>>> mon_objet = MaClasse("17")
>>> print(mon_objet)
Instance de MaClasse (valeur de un_attribut = 17)
```


## Méthodes spéciales ##

* Quelques méthodes spéciales
	* `__str__()` appelée suite à un `print(objet)`
	* `__add__()` pour pouvoir écrire `objet1 + objet2`
	* `__eq__()` pour pouvoir comparer deux objets (`objet1 == objet2`)
	* `__ne__()` pour tester si deux objets sont différents (`objet1 != objet2`)
	* `__len__()` pour pouvoir calculer `len(objet)`
	* ...


## L'héritage ##

> Principe permettant de créer une classe à partir d'une autre.

* Nom de la classe mère entre parenthèses lors de la définition
	* *toutes les classes héritent (indirectement) d'une classe `object`*
* Méthodes et attributs transmis à la classe fille

``` python
class ClasseFille(ClasseMere):
	...
```


## L'héritage ##
</br>

``` python
>>> class ClasseMere(object):
... 	def une_methode(self):
...         print("Je suis dans la classe mère")
... 
>>> class ClasseFille(ClasseMere):
...     pass
...
>>> ClasseFille().une_methode()
Je suis dans la classe mère
```


## L'héritage ##

* Possibilité d'appeler une méthode de la classe mère
	* `ClasseMere.methode(self, param...)`

``` python
>>> class Article(object):
...     def __init__(self, prix):
...         self.prix = prix
...
>>> class ArticleEnPromotion(Article):
...     def __init__(self, prix, rabais):
...         Article.__init__(self, prix)
...         self.prix *= (1 - rabais / 100)
...
>>> Article(10).prix
10
>>> ArticleEnPromotion(10, 20).prix
8
```

## Le polymorphisme ##

> Principe permettant de donner plusieurs définitions à une méthode.

* Dans le cadre de l'héritage
	* Possibilité de redéfinir une méthode héritée
	* Python se charge de trouver la bonne méthode à utiliser lors de l'appel 

``` python
>>> class ClasseMere(object):
... 	def une_methode(self):
...         print("Je suis dans la classe mère")
... 
>>> class ClasseFille(ClasseMere):
...     def une_methode(self):
...         print("Je suis dans la classe fille")
...
>>> ClasseMere().une_methode()
Je suis dans la classe mère
>>> ClasseFille().une_methode()
Je suis dans la classe fille
```


## L'encapsulation ##

> Principe visant à cacher les détails de l'implémentation à l'utilisateur

* Notion inexistante en Python : **tout est public**
* Convention : 
	* `_` avant le nom de l'attribut pour faire comme s'il était privé

``` python
>>> class MaClasse(object):
... 	def __init__(self, valeur1, valeur2):
... 		self.attribut_public = valeur1
...         self._attribut_prive = valeur2

```


## Lecture/écriture d'attributs ##

* Comment lire/écrire les valeurs des attributs privés ?
	* Utiliser des méthodes spécifiques

``` python
class Rectangle(object):
	def __init__(self, longueur, largeur):
        self._longueur = longueur
		self._largeur = largeur
    
    def get_longueur(self):
		return self._longueur

	def set_longueur(self, valeur):
		if valeur >= self._largeur:
            self._longueur = valeur
        else:
            self._longueur = self._largeur
			self._largeur = valeur
```

``` python
>>> rect = Rectangle(5, 4)
>>> rect.set_longueur(3)
>>> rect.get_longueur()
4
```

## Lecture/écriture d'attributs ##

Ca marche, mais on voudrait faire mieux et pouvoir écrire :

``` python
>>> rect = Rectangle(5, 4)
>>> rect.longueur = 3
>>> rect.longueur
4
```

* Décorateur sur les fonctions
	* `@property` pour faire comme si la méthode était un attribut
	* `@attribut.setter` pour faire comme si l'on affectait une valeur à l'attribut

<br/>

<p style="font-size:16pt">Remarque : plus généralement, un décorateur est quelque chose que l'on ajoute à une fonction pour en personnaliser le comportement (pré ou post-traitements, initialisation de paramètres...). Il en existe plein et on peut en définir soi-même.</p>


## Lecture/écriture d'attributs ##

Le code devient :

``` python
class Rectangle(object):
	def __init__(self, longueur, largeur):
        self._longueur = longueur
		self._largeur = largeur
    
    @property
    def longueur(self):
		return self._longueur

    @longueur.setter
	def longueur(self, valeur):
		if valeur >= self._largeur:
            self._longueur = valeur
        else:
            self._longueur = self._largeur
			self._largeur = valeur
```

## Les classes abstraites ##

> Une classe abstraite est une classe qui ne peut être instanciée.

* Notion difficile à mettre en oeuvre en Python
* Astuce : 
	* lever une exception dans le constructeur

``` python
class MaClasseAbstraite(object):
	def __init__(self, param1, param2...):
		raise NotImplementedError

    def methode1(self, param...):
        # methode1 est une méthode abstraite
        raise NotImplementedError

    def methode2(self, param...):
        # methode2 est une méthode concrète : on l'implémente ici
        ... 
```



# Bases de données #

## Pourquoi ? Quoi ? ##

* Persistance des données
* Données structurées

* Différents systèmes de gestion de bases de données
* Librairies Python pour manipuler les plus courants
	* `sqlite`, `psycopg`, `mysql.connector`...
	* fonctionnement équivalent pour chacune d'elles
* Object Relationnal Model (ORM) pour s'abstraire du SGBD
	* SQLAlchemy


## SQLite ##

* Moteur de BDDR
* Moteur intégré au programme
* BDD dans un seul fichier indépendant de la plateforme
* Librairie standard de Python

``` python
import sqlite3
```

## L'objet connexion ##

* Représente une connexion à une base de données
* Interface pour valider (commit) ou annuler (rollback) les transactions
* Génère les curseurs

``` python
conn = sqlite3.connect("user/password@database")

conn.commit()  # valider transaction
conn.rollback()  # annuler transaction
conn.close()  # fermer la connection
```

## Syntaxe avec with ##

* Idem que pour les fichiers
* Pour éviter d'oublier de refermer la connexion

``` python
with sqlite3.connect("user/password@database") as conn:
    # on effectue nos requêtes dans la BDD
```

## L'objet curseur ##

* Représente une instruction SQL sous format texte
* Utilisé pour parcourir les résultats d'une requête SQL

``` python
curs = conn.cursor()

curs.execute(sql_string [, parameters])  # execute requete sql
```

## Les requêtes prises en charge ##

* Tous types de requêtes SQL acceptés

``` python
curs.execute("CREATE TABLE ...")
curs.execute("UPDATE ...")
curs.execute("INSERT INTO ...")
curs.execute("SELECT ...")

```

## Passage de paramètres ##

* Utilisation du caractère `?`
* Valeur des paramètres sous forme de tuple

``` python
query = "SELECT nom, prenom FROM personne WHERE naissance > ? AND sexe = ?"
curs.execute(query, (2000, 'M'))
```

## Résultats des requêtes SQL ##

* Séquence d'objets Python

``` python
curs.execute(select_query)
results = curs.fetchall()
for row in results:
    ...
```

## Exemples ##

``` python
>>> import sqlite3
>>> conn = sqlite3.connect('dbase1')
>>> curs = conn.cursor()
>>> curs.execute('insert into people values (?, ?, ?)', ('Bob', 'dev', 5000))
>>> curs.rowcount
1
```

## Exemples ##

``` python
>>> rows = [['Tom', 'mgr', 100000],
...         ['Kim', 'adm', 30000],
...         ['Pat', 'dev', 90000]]

>>> for row in rows:
...     curs.execute('insert into people values (? , ?, ?)', row)
...

>>> conn.commit()
```

## Exemples ##

* Utilisation de `fetchall()` pour avoir tous les résultats d'un coup

``` python
>>> curs.execute('select * from people')
>>> for row in curs.fetchall():
...     print(row)
...
('Bob', 'dev', 5000)
('Sue', 'mus', 70000)
('Ann', 'mus', 60000)
('Tom', 'mgr', 100000)
('Kim', 'adm', 30000)
('Pat', 'dev', 90000)
```

## Exemples ##

* Possibilité de ne retenir que certaines colonnes en Python (semblable aux dictionnaires)

``` python
>>> curs.execute('select * from people')
>>> for (name, job, pay) in curs.fetchall():
...     print(name, ':', pay)
...
Bob : 5000
Sue : 70000
Ann : 60000
Tom : 100000
Kim : 30000
Pat : 90000
```

## Exemples ##

* Idem en utilisant la position des colonnes

``` python
>>> curs.execute('select * from people')
>>> names = [rec[0] for rec in curs.fetchall()]
>>> names
['Bob', 'Sue', 'Ann', 'Tom', 'Kim', 'Pat']
```

## Exemples ##

* Utilisation fe `fetchone()` pour n'avoir qu'une ligne de résultat à la fois

``` python
>>> curs.execute('select * from people')
>>> while True:
...     row = curs.fetchone()
...     if not row:
...         break
...     print(row)
...
('Bob', 'dev', 5000)
('Sue', 'mus', 70000)
('Ann', 'mus', 60000)
('Tom', 'mgr', 100000)
('Kim', 'adm', 30000)
('pat', 'dev', 90000)
```

## Exemples ##

* `rowcount` indique le nombre de lignes impactées par la requête

``` python
>>> curs.execute('update people set pay=? where pay <= ?', [65000, 60000])
>>> curs.rowcount
3
>>> curs.execute('select * from people')
>>> curs.fetchall()
[('Bob', 'dev', 65000), ('Sue', 'mus', 70000), ('Ann', 'mus', 65000), ('Tom', 'mgr',
100000), ('Kim', 'adm', 65000), ('pat', 'dev', 90000)]
```

## Exemples ##

* Accès à la description des colonnes (`curs.description`)

``` python
>>> curs.execute('select * from people')
>>> colnames = [desc[0] for desc in curs.description]
>>> for row in curs.fetchall():
...     for name, value in zip(colnames, row):
...         print(name, '\t=>', value)
...     print()
...
name => Sue
job  => mus
pay  => 70000

name => Ann
job  => mus
pay  => 65000

```

## Exemples ##

* Possible de faire en Python ce que font de grosses requêtes compliquées

``` python
>>> query = ("select name from people where job = 'devel' and "
...                "pay > (select avg(pay) from people where job = 'devel')")
>>> curs.execute(query)
>>> curs.fetchall()
[('kim',)]
```

```
>>> curs.execute("select name, pay from people where job = 'devel'")
>>> result = curs.fetchall()
>>> avg = sum(rec[1] for rec in result) / len(result)
>>> print([rec[0] for rec in result if rec[1] > avg])
['kim']
```


## Mapping classes-bdd ##
* Classiquement
    * Classe = table
    * Objet = ligne
    * Attribut = colonne


