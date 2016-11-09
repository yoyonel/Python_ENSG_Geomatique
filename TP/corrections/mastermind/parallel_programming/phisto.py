import sys
from multiprocessing import Pool
import numpy as np
import time

# Compute the histogram of a csv file with a python parallel program
# Input file format:
#   name,count\n
# Output the frequency of "count".

# Stolen from http://mikecvet.wordpress.com/2010/07/02/parallel-mapreduce-in-python/
# Adapted to histogram computation instead of word count
# And ported to python3

"""
Given a list of tokens, return a list of tuples of
titlecased (or proper noun) tokens and a count of '1'.
Also remove any leading or trailing punctuation from
each token.
"""


def Map(L):
    results = []
    for w in L:
        results.append((w, 1))
    return results


"""
Group the sublists of (token, 1) pairs into a term-frequency-list
map, so that the Reduce operation later can work on sorted
term counts. The returned result is a dictionary with the structure
{token : [(token, 1), ...] .. }
"""


def Partition(L):
    tf = {}
    for sublist in L:
        for p in sublist:
            # Append the tuple to the list in the map
            try:
                tf[p[0]].append(p)
            except KeyError:
                tf[p[0]] = [p]
    return tf


"""
Given a (token, [(token, 1) ...]) tuple, collapse all the
count tuples from the Map operation into a single term frequency
number for this token, and return a final tuple (token, frequency).
"""


def Reduce(Mapping):
    return Mapping[0], sum(pair[1] for pair in Mapping[1])


"""
Load the contents the file at the given
path into a big list and return it.
"""


def load(path):
    stars = []
    with open(path, "r") as f:
        for line in f:
            stars.append(int(line.split()[1]))

    # Efficiently concatenate Python string objects
    # return (''.join(stars)).split ()
    return stars


"""
A generator function for chopping up a given list into chunks of
length n.
"""


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def process_with_pp(list_entries, use_mp_for_reduce=True):
    """

    :param list_entries:
    :param use_mp_for_reduce:
    :return:
    """
    print("Build a pool of 8 processes", file=sys.stderr)
    pool = Pool(processes=nprocs)

    print("Fragment the string data into 8 chunks", file=sys.stderr)
    partitioned_entries = list(chunks(list_entries, len(list_entries) // nprocs))

    print("Generate count tuples for title-cased tokens", file=sys.stderr)
    single_count_tuples = pool.map(Map, partitioned_entries)

    print("Organize the count tuples; lists of tuples by token key", file=sys.stderr)
    token_to_tuples = Partition(single_count_tuples)

    print("Collapse the lists of tuples into total term frequencies", file=sys.stderr)
    if use_mp_for_reduce:
        token_to_tuples_items = token_to_tuples.items()
        term_frequencies_mp = pool.map(Reduce,token_to_tuples_items, chunksize=len(token_to_tuples_items)//8)
        #print("term_frequencies_mp: %s" % term_frequencies_mp)
        list_results = term_frequencies_mp
    else:
        term_frequencies_sp = list(map(Reduce, token_to_tuples.items()))
        list_results = term_frequencies_sp

    print("Sort the term frequencies in increasing order", file=sys.stderr)
    # term_frequencies.sort(key=lambda x: x[1]) # nb of projects
    list_results.sort(key=lambda x: x[0])  # nb of stars

    return list_results


if __name__ == '__main__':

    if (len(sys.argv) != 3):
        print("Usage: phisto file nprocs")
        sys.exit(1)

    nprocs = int(sys.argv[2])

    print("Load file, stuff it into a string", file=sys.stderr)
    # stars = load(sys.argv[1])
    stars = np.random.randint(100, size=2500000)

    start_time = time.time()

    term_frequencies = process_with_pp(stars, use_mp_for_reduce=True)

    print("--- %s seconds ---" % (time.time() - start_time))

    # for pair in term_frequencies[:20]:
    #     print("%i occurs %i times" % pair)
