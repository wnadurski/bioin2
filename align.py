from functools import partial

from Bio import pairwise2


def find_alignments(algorithm, seq1, seq2, matrix, gapopen=-10, gapextend=-1):
    return algorithm(seq1, seq2, matrix, gapopen, gapextend)

find_local_alignments = partial(find_alignments, pairwise2.align.localds)
find_global_alignments = partial(find_alignments, pairwise2.align.globalds)

