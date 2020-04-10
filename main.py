message = 'spotkanieodrugiejgodzinienaparkingu'
n = 6

tab1 = [[' ' for i in range(n)] for i in range(n)]
tab2 = [[' ' for i in range(n)] for i in range(n)]

for i in range(len(message)):
    print(i)
    tab1[i//n][i % n] = message[i]


for x in tab1:
    print(x)

x, y = 0, 0

for i in range((n+1)//2):
    x, y = i, i
    m = n-1-2*i
    for k in range(4*m):
        x0, y0 = x, y
        if k//m == 0:
            x += 1
        elif k//m == 1:
            y += 1
        elif k//m == 2:
            x -= 1
        else:
            y -= 1
        print(i, x, y, x0, y0)
        tab2[y][x] = tab1[y0][x0]

print()

for x in tab2:
    print(x)
