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


def switch_rows(m, i, j):
    temp = m[i].copy()
    m[i] = m[j]
    m[j] = temp


def check_diagonal(a, b):
    n = len(a)
    for j in range(n):
        max_el, index = a[0][j], 0
        for i in range(1, n):
            if abs(a[i][j]) > abs(max_el):
                max_el, index = a[i][j], i
        switch_rows(a, j, index)
        switch_rows(b, j, index)


def gaussian(a, b):
    n = len(a)
    check_diagonal(a, b)
    for k in range(n - 1):
        for i in range(k + 1, n):
            m = a[i, k] / a[k, k]
            for j in range(k, n):
                a[i, j] -= m * a[k, j]
            b[i] -= m * b[k]

    x = np.zeros(n)
    for k in range(n - 1, -1, -1):
        rest = a[k, k + 1, n] @ x[k + 1:n]
        x[k] = (b[k] - rest) / a[k, k]

    return x
