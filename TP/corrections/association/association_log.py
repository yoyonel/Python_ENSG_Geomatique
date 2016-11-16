# -*- coding: utf-8 -*-

import logging


def log(nom_fichier, nature, message):
    """

    :param nom_fichier:
    :param nature:
    :param message:
    :return:
    """
    logging.basicConfig(filename=nom_fichier, level=logging.DEBUG, format='[%(levelname)s] %(asctime)s : %(message)s')

    if nature == 'WARNING':
        logging.warning(message)
    elif nature == 'INFO':
        logging.info(message)
    elif nature == 'DEBUG':
        logging.debug(message)
    elif nature == 'ERROR':
        logging.error(message)
    else:
        logging.error("Le type de log n'est pas pris en charge : {}. {}".format(nature, message))
