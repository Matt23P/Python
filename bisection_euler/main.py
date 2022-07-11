from choice import *
from algorithms import *
from graphs import graph


def main():
    fn = fun_choice()
    func = locals()[f"fun{fn}"]
    met = met_choice()
    p, k = interval()
    cond, limiter = condition()

    if met == 1:
        x, i = bisection(func, p, k, cond, limiter)
    else:
        x, i = secant(func, p, k, cond, limiter)

    if x != 'err':
        print("Liczba wykonanych iteracji: ", i)
        print("x: ", x)
        print("f(x) =", func(x))
        graph(func, p, k, x, met)
    elif i == 0:
        print("Dzielenie przez 0!")
    elif i == 'outofrange':
        print("W danym przedziale nie ma miejsca zerowego!")
    else:
        print("Podany przedzial jest bledny!")

    return 0


if __name__ == '__main__':
    main()
