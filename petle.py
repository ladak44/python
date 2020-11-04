def do_sth():
    # pass
    # for i in range(0,101):
    #     if i % 2 == 0:
    #         print(i,end=",")

    # for i in range(0,9):
    #     print(2**i)

    # liczba = 32
    #
    # for i in range(2,liczba):
    #     if liczba % i == 0:
    #         print("To nie jest liczba pierwsza.")
    #
    # print("To jest liczba pierwsza")

    napis = "\t  \n To jest moj test. \t  \n"

    # for i in enumerate(napis):
    #     print(i)

    for i in range(len(napis.strip())):
        if napis[i].isupper() :
            print(f"Duża lista {napis[i]}")

    # print(napis.strip())

if __name__ == '__main__':
    do_sth()