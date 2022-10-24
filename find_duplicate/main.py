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

    return result, history


if __name__ == '__main__':
    lista = [1, 1, 6, 5, 7, 11, 7, 3, 3, 3, 9, None, 8]
    wynik1, hist = findDuplicates(lista, 2)
    print(wynik1)
    print(hist)
