def czslowo(slowo):
    wagi = []
    x = 1
    for i in range(len(slowo)):
        if len(slowo) % 2 == 0 and i == len(slowo)//2:
            x -= 1
        wagi += [x]
        if i+1 > len(slowo)//2:
            x -= 1
        else:
            x += 1
    return wagi


def czslowo2(slowo):
    wagi = czslowo(slowo)
    wagi2 = []
    for i in range(len(wagi)):
        if slowo[i] in "aeiouy":
            wagi2 += [wagi[i]-1]
        else:
            wagi2 += [wagi[i]+1]
    return sum(wagi2)


def wagi(zdanie):
    zdanie = zdanie.split()
    tab = []
    slowo = ""
    maks = 0
    for i in range(len(zdanie)):
        tab += [(czslowo2(zdanie[i]), zdanie[i])]
    tab2 = []
    for i in range(len(tab)):
        tab2 += [max(tab)]
        tab.remove(max(tab))
    slowo2 = ""
    tab2 = tab2[::-1]
    for i in range(len(tab2)):
        x, y = tab2[i]
        slowo2 += y
        if i != len(tab2)-1:
            slowo2 += " "

    return slowo2


assert wagi("ala ma kota") == "ma ala kota"

assert czslowo2("ala") == 3
assert czslowo2("ma") == 2
assert czslowo2("kota") == 6
assert czslowo2("")