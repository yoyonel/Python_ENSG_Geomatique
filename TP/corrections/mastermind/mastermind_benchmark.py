# -*- coding: utf-8 -*-

import time
import timeit

from joblib import Parallel, delayed
import matplotlib.pyplot as plt

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


def parallel_prog():
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
    # f = open("results_timing.txt", "w")
    # print("results_timings: %s" % "\n".join(map(str, results_timings)), file=f)
    # f.close()


def timeit_and_plot():
    """

    :return:

    urls:
    - http://stackoverflow.com/questions/11983024/matplotlib-legends-not-working
    - http://math.mad.free.fr/depot/numpy/courbe.html
    - http://matplotlib.org/users/pyplot_tutorial.html
    - http://stackoverflow.com/questions/12200580/numpy-function-for-simultaneous-max-and-min
    """
    timeit_sizes = [1, 5, 10, 20, 30]
    timeit_sizes += range(50, 2000, 50)
    timeit_repeat = [1]

    # timings_for_verfication = [
    #     timeit.timeit(
    #     'verification(sol, prop)',
    #     setup='from mastermind import verification, tirage_aleatoire_v2; sol = tirage_aleatoire_v2(%d, %d); prop = tirage_aleatoire_v2(%d, %d)' % (size, size, size, size),
    #     number=repeat)
    #     for size in timeit_sizes for repeat in timeit_repeat
    # ]

    # timings_for_verfication_v2 = [
    #     timeit.timeit(
    #     'verification_v2(sol, prop)',
    #     setup='from mastermind import verification_v2, tirage_aleatoire_v2; sol = tirage_aleatoire_v2(%d, %d); prop = tirage_aleatoire_v2(%d, %d)' % (size, size, size, size),
    #     number=repeat)
    #     for size in timeit_sizes for repeat in timeit_repeat
    # ]
    #
    # timings_for_verfication_v3 = [
    #     timeit.timeit(
    #     'verification_v3(sol, prop, %d)' % size,
    #     setup='from mastermind import verification_v3, tirage_aleatoire_v2; sol = tirage_aleatoire_v2(%d, %d); prop = tirage_aleatoire_v2(%d, %d)' % (size, size, size, size),
    #     number=repeat)
    #     for size in timeit_sizes for repeat in timeit_repeat
    # ]

    #
    timings_for_verfication_v4 = np.array(
        [
            timeit.timeit(
            'verification_v4(sol, prop, %d)' % size,
            setup='from mastermind import verification_v4, tirage_aleatoire_v2; sol = tirage_aleatoire_v2(%d, %d); prop = tirage_aleatoire_v2(%d, %d)' % (size, size, size, size),
            number=repeat)
            for size in timeit_sizes for repeat in timeit_repeat
        ]
    )

    timings_for_verfication_v4b = np.array(
        [
            timeit.timeit(
                'verification_v4b(sol, prop, list_empty)',
                setup="""\\
                import numpy as np;\\
                from mastermind import verification_v4b, tirage_aleatoire_v2;\\
                list_empty = np.array([0] * (%d+1));\\
                sol = tirage_aleatoire_v2(%d, %d);\\
                prop = tirage_aleatoire_v2(%d, %d)""" % (size, size, size, size, size),
                number=repeat
            )
            for size in timeit_sizes for repeat in timeit_repeat
        ]
    )

    plt.title("Timings des differentes methodes pour 'verification' (iterative, groupby, histogram, histogram_simplifie")
    plt.ylabel('Temps en secondes')
    plt.xlabel('Nb points/couleurs')
    # p1 = plt.plot(timeit_sizes, timings_for_verfication, 'r--', label='Iterative')
    # p2 = plt.plot(timeit_sizes, timings_for_verfication_v2, '-ro', label='Func_GroupBy')
    # p3 = plt.plot(timeit_sizes, timings_for_verfication_v3, '-x', label='Func_Histo')
    # p4 = plt.plot(timeit_sizes, timings_for_verfication_v4, '-g+', label='Func_Histo_Optimiz')
    # p4b = plt.plot(timeit_sizes, timings_for_verfication_v4b, '-b+', label='Func_Histo_Optimiz_Parallel')
    p = plt.plot(
        timeit_sizes,
        timings_for_verfication_v4b / timings_for_verfication_v4,
        '-bo',
        label='Ratio Func Histo with //'
    )
    print('mean: %f' % ((timings_for_verfication_v4b / timings_for_verfication_v4)[5:].mean()))
    plt.text(0, 2, r'mean: %f' % ((timings_for_verfication_v4b / timings_for_verfication_v4)[5:].mean()),
             fontsize=20, color='red', backgroundcolor='yellow')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # parallel_prog()

    timeit_and_plot()