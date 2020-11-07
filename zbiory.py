def main():
    pass
    zbior_p = set()

    zbior = {2,4,5}

    baza_danych = {"1": ["Marcin","Ladak",45],
                   "2": ["Eliza","Ladak",46]}


    baza_danych["2"] = ["aaaa","eeeee","wwwww","qqq","cccc"]
    baza_danych["3"] = ["lola"]
    baza_danych["a"] = ["ola lola"]

    # print(baza_danych["1"])
    # print(baza_danych)
    # for i in baza_danych.keys():
    #     print(i)
    #
    # for w in baza_danych.values():
    #     print(w)

    # for i,w in baza_danych.items():
    #     print(i)
    #     print(w)

def palindrom(slowo):
    pass
    n = len(slowo)//2
    for i in range(0,n):
        k = -i-1
        if slowo[i] != slowo[k]:
            print(f"f1 {slowo[i]}")
            print(f"f2 {slowo[k]}")
            return False
    print("Palindrom")
    return True

def test():
    slowo = "kajak"
    for i in range(0,len(slowo)//2):
        print(f"minus : {slowo[-i-1]}")
        print(f"plus : {slowo[i]}")
        print("==========")


def test2(slowo):
    return slowo == slowo[::-1]

if __name__ == '__main__':
    # palindrom("kajak")
    print(test2("kajak"))
    # main()