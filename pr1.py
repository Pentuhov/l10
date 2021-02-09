#!/usr/bin/evn python3
# -*- config: utf-8 -*-


def rand(A):
    if A >= 0:
        positive()
    elif A < 0:
        negative()


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


if __name__ == '__main__':
    a = int(input('Введите целое число: '))

    rand(a)
