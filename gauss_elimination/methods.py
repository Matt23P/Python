import numpy as np
from numpy.linalg import matrix_rank


def check(x, y):
    u = np.c_[x, y]
    rank_x = matrix_rank(x)
    rank_u = matrix_rank(u)
    if rank_x != rank_u:
        return "contradictory"
    else:
        if rank_x == len(x[0]):
            return "determinate"
        elif rank_x < len(x[0]):
            return "indeterminate"
