# -*- coding:utf8 -*-

def caracteres(messages):
    message_ok = ""
    for lettre in messages:
        if ord(lettre) in range(97, 123):
            message_ok += lettre
    return message_ok


def recherche_motifs(message):
    dico = {}

    # Recherche des répétitions de 3 lettres
    dico = recherche_repetitions(message, 3, dico)

    # Recherche des répétitions de 4 lettres
    dico = recherche_repetitions(message, 4, dico)

    # Recherche des répétitions de 5 lettres
    dico = recherche_repetitions(message, 5, dico)

    # Recherche des répétitions de 6 lettres
    dico = recherche_repetitions(message, 6, dico)

    # Recherche des répétitions de 7 lettres
    dico = recherche_repetitions(message, 7, dico)

    return dico


def recherche_repetitions(message, taille, dico):
    for i in range(len(message) - taille):
        motif = message[i:i+taille]
        for j in range(i+1, len(message)-taille+1):
            if motif == message[j:j+taille]:
                if motif in dico.keys():
                    if not j in dico[motif]:
                        dico[motif].append(j)
                else:
                    dico[motif] = [i, j]
    return dico


a = "p'vflseegxviai p'wyx qw re osrpr. gt c ssox qwy xemiw cjgxviaif egmf xgyg soqrj rif egxuÃ©egxviaif."
b = caracteres(a)
dico = recherche_motifs(b)
print(dico)

