from turtle import *
from math import *


def kwadrat():
    fillcolor("green")
    begin_fill()
    for i in range(4):
        fd(50)
        rt(90)
    end_fill()


def skok(a, b):
    pu()
    fd(a)
    rt(90)
    fd(b)
    lt(90)
    pd()


def wieza(n):
    for i in range(n):
        kwadrat()
        skok(0, -50)
    skok(0, 50)


def fig1():
    fillcolor("lightgray")
    begin_fill()
    for i in range(3):
        fd(50)
        lt(120)
    end_fill()


def fig2():
    fillcolor("lightgray")
    begin_fill()
    fd(50)
    lt(90)
    fd(50)
    lt(150)
    fd(50)
    rt(120)
    fd(50)
    lt(150)
    fd(50)
    lt(90)
    end_fill()


def fig3():
    fillcolor("lightgray")
    begin_fill()
    fd(50)
    lt(90)
    fd(50)
    lt(135)
    fd(50*sqrt(2))
    lt(135)
    end_fill()


def fig4():
    fillcolor("lightgray")
    begin_fill()
    fd(50)
    lt(135)
    fd(50*sqrt(2))
    lt(135)
    fd(50)
    lt(90)
    end_fill()


def schemat(lista):
    skok(-50*len(lista)/2, 50*len(lista)/2)
    for i in range(len(lista)):
        wieza(lista[i])
        if i == 0 and len(lista)-1 != i:
            if lista[i] < lista[i+1]:
                fig3()
        if i != 0 and len(lista)-1 != i:
            if lista[i-1] < lista[i] and lista[i+1] < lista[i]:
                fig1()
        if i != 0 and len(lista)-1 != i:
            if lista[i-1] < lista[i] and lista[i+1] > lista[i]:
                fig3()
        if i == len(lista)-1:
            if lista[i-1] == lista[i]:
                fig3()
            # zestaw 1
        if i != 0 and len(lista)-1 != i:
            if lista[i-1] > lista[i] and lista[i+1] > lista[i]:
                fig2()
        if i == len(lista)-1:
            if lista[i-1] > lista[i]:
                fig4()
        if i != len(lista)-1 and i != 0:
            if lista[i+1] <= lista[i] and lista[i-1] > lista[i]:
                fig4()
        if i == 0:
            if lista[i+1] < lista[i]:
                fig1()
# if i != 0 and i != len(lista)-1:
# if lista[i-1] > lista[i] and lista[i+1]
            # zestaw 2

        skok(50, 50*(lista[i]-1))


speed(0)
schemat([2,1,2])
pu()
home()
done()
