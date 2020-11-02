def main():
    # print(czy_wszystkie_dodatnie([1,2,3,-4]))
    #print(srednia([1,3,4,-20]))
    # print(skumulowana([1,2,4,4,7]))
    print(suma_list([1,4,5],[5,2,1]))

def suma_list(lista1,lista2):
    wynik = [None] * len(lista1)
    for i in range(len(lista1)):
        wynik[i] = lista1[i] + lista2[i]
    return wynik

def skumulowana(lista):
    wynik = [None] * len(lista)
    poprzedni = 0
    for index, element in enumerate(lista):
        wynik[index] = poprzedni + element
        poprzedni = wynik[index]
    # wynik = len(lista)
    return wynik

def czy_wszystkie_dodatnie(lista):
    rozmiar = len(lista)
    for el in lista:
        if el <= 0:
            return False
    return True

def srednia(lista):
    sum = 0
    for el in lista:
        sum += el

    return sum / len(lista)
    # lista = [1,3,3,-5]
    # print(len(lista))

if __name__ == '__main__':
    main()


