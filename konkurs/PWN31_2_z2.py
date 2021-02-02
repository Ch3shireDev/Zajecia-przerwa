def papadam(slowo):
    lista = []
    suma = 0
    for i in range(len(slowo)):
        c = slowo[i]
        if lista == ["p", "a", "p", "a", "d", "a", "m"]:
            suma += 1
            lista = []
        if len(lista) % 7 == 0 and c == "p":
            lista += [c]
        if c == "a" and len(lista) % 7 == 1:
            lista += [c]
        if len(lista) % 7 == 2 and c == "p":
            lista += [c]
        if len(lista) % 7 == 3 and c == "a":
            lista += [c]
        if len(lista) % 7 == 4 and c == "d":
            lista += [c]
        if len(lista) % 7 == 5 and c == "a":
            lista += [c]
        if len(lista) % 7 == 6 and c == "m":
            lista += [c]
    if lista == ["p", "a", "p", "a", "d", "a", "m"]:
        suma += 1
        lista = []
    return suma


assert papadam("papadam") == 1
assert papadam("papada") == 0
assert papadam("papadampapa") == 1
assert papadam("papadampapaaaaaaaaaaaadam") == 2
assert papadam("aaaaaaaaaaaaapapadampapaaaaaaaaaaaadam") == 2
assert papadam("papapapapapapapapadam") == 1

# print(papadam(input()))
