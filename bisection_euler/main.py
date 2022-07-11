from choice import *
from functions import *
from algorithms import *

fn = fun_choice()
func = locals()[f"fun{fn}"]
met = met_choice()
p, k = interval()
cond, limiter = condition()

if met == 1:
    x, i = bisection(func, p, k, cond, limiter)
else:
    x, i = secant(func, p, k, cond, limiter)