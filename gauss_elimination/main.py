import choice
import time
import methods
import colorama


def gauss_elimination():
    x, y = choice.choose_a_file()
    mode = methods.check(x, y)
    match mode:
        case "determinate":
            start = time.time_ns()

            total = (time.time_ns() - start) / 1000000
            print("Algorithm uptime: " + str(total) + "ns\n")
            exit(0)
        case "indeterminate":
            print(colorama.Fore.LIGHTRED_EX +
                  "Matrix is indeterminate!"
                  + colorama.Style.RESET_ALL)
            exit(0)
        case "contradictory":
            print(colorama.Fore.LIGHTRED_EX +
                  "Matrix is contradictory!"
                  + colorama.Style.RESET_ALL)
            exit(0)



if __name__ == '__main__':
    gauss_elimination()
