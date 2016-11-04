# -*- coding: utf-8 -*-

import time
from joblib import Parallel, delayed
from mastermind import *


def launch_parallel_verification(
        func,
        nb_jobs=1,
        verbose=5,
        nb_pions=1,
        nb_couleurs=1,
        nb_verfications=1,
):
    """

    :param func:
    :param nb_jobs:
    :param verbose:
    :param nb_pions:
    :param nb_couleurs:
    :param nb_verfications:
    :return:
    """
    print("%s %s %s %s %s" % (func.__name__, nb_jobs, nb_pions, nb_couleurs, nb_verfications))
    start_time = time.clock()
    r = Parallel(n_jobs=nb_jobs, verbose=verbose)(
        delayed(func)(
            tirage_aleatoire(nb_pions, nb_couleurs, True),
            tirage_aleatoire(nb_pions, nb_couleurs, True)
        )
        for _ in range(nb_verfications)
    )
    return time.clock() - start_time

if __name__ == "__main__":

    results_timings = [
        (
            (nb_jobs, nb_pions, nb_couleurs, nb_verfications),
            launch_parallel_verification(verification, nb_jobs, 0, nb_pions, nb_couleurs, nb_verfications),
            launch_parallel_verification(verification_v2, nb_jobs, 0, nb_pions, nb_couleurs, nb_verfications),
        )
        for nb_jobs in range(1, 5)
        for nb_couleurs in (list(range(10, 200, 10)) + [500, 1000, 5000])
        for nb_pions in (list(range(10, 200, 10)) + [500, 1000, 5000])
        for nb_verfications in [10, 100, 1000]
        ]

    # save result in file
    f = open("results_timing.txt", "w")
    print("results_timings: %s" % "\n".join(map(str, results_timings)), file=f)
    f.close()


