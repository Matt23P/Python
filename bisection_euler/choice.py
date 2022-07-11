from numpy import double
from functions import arr_fn


def fun_choice():
    try:
        print("Wybierz funkcje z ponizszych: ")
        for i in range(len(arr_fn)):
            print(f'{i + 1}.', arr_fn[i])
        choice = int(input("$> "))
        if choice in [1, 2, 3, 4, 5]:
            return choice
        print("Funkcja spoza dostepnych!")
    except ValueError:
        print("Nieprawidlowa wartosc")
    return fun_choice()


def met_choice():
    try:
        choice = int(input("Wybierz metode: \n"
                           "1. Metoda bisekcji, \n"
                           "2. Metoda siecznych, \n"
                           "$> "))
        if choice in [1, 2]:
            return choice
        print("Metoda spoza dostepnych!")
    except ValueError:
        print("Nieprawidlowa wartosc")
    return met_choice()


def interval():
    pocz, kon = 1, 0
    while pocz > kon:
        try:
            pocz = double(input("Poczatek przedzialu: "))
            kon = double(input("Koniec przedzialu: "))
            if pocz < kon:
                return pocz, kon
            print("Przedzial wprowadzony niepoprawnie!")
            print("Poczatek przedzialu > koniec przedzialu")
        except ValueError:
            print("Nieprawidlowa wartosc")
            pocz, kon = 1, 0


def condition():
    cond = int
    while cond not in [1, 2]:
        try:
            cond = int(input("Algorytm ma zatrzymac sie gdy: \n"
                             "1. Zostanie osiagnieta podana liczba iteracji, \n"
                             "2. Zostanie osiagnieta podana wartosc eps. \n"
                             "$> "))
        except ValueError:
            print("Nieprawidlowa wartosc")

        if cond == 1:
            iter = 0
            while iter <= 0:
                try:
                    iter = int(input("Podaj liczbe iteracji: "))
                except ValueError:
                    print("Nieprawidlowa wartosc")
            return cond, iter
        else:
            eps = 0
            while eps <= 0:
                try:
                    eps = double(input("Podaj wartosc eps: "))
                except ValueError:
                    print("Nieprawidlowa wartosc")
            return cond, eps
