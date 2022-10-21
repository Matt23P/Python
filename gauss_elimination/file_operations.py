import numpy as np
import colorama as ca


def load(filename):
    try:
        xy = np.loadtxt(f'equations/{filename}.txt')
        n = len(xy[0]) - 1
        x, y = xy[:, :n], xy[:, n]
        return x, y
    except ValueError:
        print(ca.Fore.RED +
              "Matrix is not correct"
              + ca.Style.RESET_ALL)
        exit(-1)
