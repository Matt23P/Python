import file_operations as fo
import colorama as ca


def choose_a_file():
    try:
        name = input("Please insert a name of file with matrix: ")
        return fo.load(name)
    except FileNotFoundError:
        print(ca.Fore.RED +
              "Wrong file name"
              + ca.Style.RESET_ALL)
        return choose_a_file()
