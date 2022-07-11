from choice import *
from functions import *

fn = fun_choice()
func = locals()[f"fun{fn}"]
met = met_choice()
p, k = interval()
cond, limiter = condition()

