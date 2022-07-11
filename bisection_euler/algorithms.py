import numpy

from functions import *


def bisection(f, p, k, cond, limiter):
    if (f(p) * f(k)) > 0:
        return 'err', 'err'
    iter = 1
    while True:
        x = (p + k) / 2
        if f(x) == 0:
            return x, iter
        if cond == 1:
            if iter == limiter:
                return x, iter
        else:
            if abs(f(x)) < limiter:
                return x, iter
        if f(x) * f(k) < 0:
            p = x
        elif f(x) * f(p) < 0:
            k = x
        iter += 1


def secant(f, p, k, cond, limiter):
    if (f(p) * f(k)) > 0:
        return 'err', 'err'
    iter = 1
    while True:
        if (f(k) - f(p)) == 0:
            return 'err', 0
        x = p - (f(p) * (k - p)) / (f(k) - f(p))
        if x < p or x > k:
            return 'err', 'outofrange'
        if cond == 1:
            if iter == limiter:
                return x, iter
        else:
            if abs(f(x)) < limiter:
                return x, iter
        if f(p) * f(x) > 0:
            p = x
        else:
            k = x
        iter += 1
