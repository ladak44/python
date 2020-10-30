
def bmi (waga,wzrost):
    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        return bmi, "niedowaga"
    elif bmi < 25:
        return  bmi, "optymalna"
    else:
        return bmi, "nadwaga"


def krotki(pieniadze,kilometry):
    # koszt przejazu taksowka
    koszt = 5 + 2.5*kilometry
    uda_sie_przejechac = False
    ile_mamy = pieniadze - 5
    maks_km = ile_mamy/2.5

    if pieniadze > koszt:
        uda_sie_przejechac = True
        return uda_sie_przejechac, maks_km, pieniadze - koszt
    else:
        uda_sie_przejechac = False
        return uda_sie_przejechac, maks_km, pieniadze - koszt


    print('test')

if __name__ == '__main__':
    # krotki(300,30)
    wartosc, interpretacja = bmi(75,1.82)
    wynik = bmi(75,1.82)
    print(wynik[0],wynik[1])
    print("wartosc " + str(wartosc), "opis:" + interpretacja)
    # print(f"wartosc")
    print(krotki(200,20))
