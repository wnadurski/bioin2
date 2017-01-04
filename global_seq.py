import Bio
from Bio import SeqIO
from Bio import pairwise2

from align import find_global_alignments
from utils import get_input


def parse_matrix_file(filename):
    file = open(filename, "r")


def run_global_sequence_algorithm():
    filename1 = get_input("Podaj plik z pierwsza sekwencja:")
    seq1 = SeqIO.read(filename1, "fasta")

    filename2 = get_input("Podaj plik z druga sekwencja:")
    seq2 = SeqIO.read(filename2, "fasta")

    filename3 = get_input("Podaj plik z macierza podobienstwa:")
    matrix = parse_matrix_file(filename3)

    gapopen_text = get_input("Podaj wartosc kary dla rozpoczecia przerwy:")
    gapopen = int(gapopen_text)

    gapextend_text = get_input("Podaj wartosc kary dla kontynuowania przerwy:")
    gapextend = int(gapextend_text)

    alignments = find_global_alignments(seq1, seq2, matrix, gapopen, gapextend)
