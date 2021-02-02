def szereg(liczba):
    liczba2 =str(liczba)
    lista = []
    lista2 = []
    for i in range(len(liczba2)):
        lista += [int(liczba2[i])]
   
    for i in range(len(lista)):
        lista2 += [max(lista)]
        lista.remove(max(lista))
    sl = ""
    for i in range(len(lista2)):
       sl += str(lista2[i])
    
    return sl
def szereg2(liczba):
    liczba2 =str(liczba)
    lista = []
    lista2 = []
    for i in range(len(liczba2)):
        lista += [int(liczba2[i])]
   
    for i in range(len(lista)):
        lista2 += [min(lista)]
        lista.remove(min(lista))
    sl = ""
    
    if 0 in lista2:
        for i in range(lista2.count(0)):
            lista2.remove(0)
    
    for i in range(len(lista2)):
        sl += str(lista2[i])
    
    return sl
def cztero(liczba):
    lista = []
    flag = False
    i = 0
    while flag == False:
        liczba = int(szereg(liczba)) - int(szereg2(liczba))
        
        if liczba in lista:
            flag = True
        else:
            lista += [liczba]
        print(lista)
        i += 1
        if liczba == 0:
            return i
    return i-1

        
assert cztero("1234") == 3
assert cztero("2222") == 1
assert cztero("1224") == 6
assert cztero("9999") == 1
assert cztero("5665") == 4