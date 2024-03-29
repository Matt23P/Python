def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


def findDuplicates(array, numberOfDuplicates):
    result = []
    history = []
    intToCheck = 0
    for i in range(len(array)):
        occurances = 0
        intToCheck = array[i]
        flag = False

        if intToCheck == None:
            continue
        for k in range(len(history)):
            if history[k] == intToCheck:
                flag = True
        if flag:
            continue
        else:
            history.append(intToCheck)

        for j in range(len(array)):
            if array[j] == intToCheck:
                occurances += 1
        if occurances == numberOfDuplicates:
            result.append(intToCheck)
    return result


if __name__ == '__main__':
    lista = [1, 1, 6, 5, 7, 11, 7, 3, 3, 3, 9, None, 8]
    wynik1 = findDuplicates(lista, 2)
    print(wynik1)
