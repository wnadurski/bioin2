import re
from functools import partial

import Bio
from Bio import SeqIO
from Bio import pairwise2
from Bio.Seq import Seq

import align
from utils import get_input, get_command

DNA_ALIGNMENT = "1"
RNA_ALIGNMENT = "2"


def get_inputs():
    """

    :return: (str, Bio.SeqIO.Seq
    """
    print "1 - Zestawienie sekwencji DNA"
    print "2 - Zestawienie sekwencji kodonow (mRNA jako sekwencje wejsciowe)"

    command = get_command(["1", "2"])

    return tuple([command] + map(get_sequence, [
        "Podaj plik z pierwsza sekwencja:",
        "Podaj plik z druga sekwencja:",
        ("Podaj plik z macierza podobienstwa:", parse_matrix_file)
    ]))


def get_sequence(obj):
    if isinstance(obj, str):
        message, parser = obj, read_sequence
    else:
        message, parser = obj

    filename = get_input(message)
    try:
        with open(filename, "r") as f:
            return parser(f)
    except IOError as e:
        print "Nie udalo sie zaladowac pliku '%s'." % filename
        return get_sequence(obj)
    except Exception as e:
        print "Nie poprawny format pliku '%s'." % filename
        return get_sequence(obj)


def read_sequence(file):
    return SeqIO.read(file, "fasta").seq


def parse_matrix_file(f):
    line = f.readline()
    chars = line.split()
    matrix = []

    for row in range(len(chars)):
        line = f.readline()
        matrix.append([int(value) for value in line.split()])

    result = {}

    for row in range(len(chars)):
        for col in range(len(chars)):
            result[(chars[row], chars[col])] = matrix[row][col]

    return result


def alignment(algorithm):
    seq_type, seq1, seq2, matrix = get_inputs()

    if (seq_type == RNA_ALIGNMENT):
        seq1 = seq1.translate()
        seq2 = seq2.translate()

        seq1 = Seq("".join(filter(lambda aminoacid: aminoacid != "*", seq1)), seq1.alphabet)
        seq2 = Seq("".join(filter(lambda aminoacid: aminoacid != "*", seq2)), seq1.alphabet)

    result = algorithm(seq1, seq2, matrix)

    align = result[0]

    if (seq_type == RNA_ALIGNMENT):
        pass #align1, align2 = protein_to_RNA(align1), protein_to_RNA(align2)

    print "Najlepsze dopasowanie:"
    print(pairwise2.format_alignment(*align))
    # print "Podobienstwo: %f" % (result[1][0], result[1][1])
    print "\n"


global_alignment = partial(alignment, align.find_global_alignments)
local_alignment = partial(alignment, align.find_local_alignments)
