#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 1. Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым
# элементом. Преобразованный массив вывести.

import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))
    if len(a) != 10:
        print('Список должен состоять из 10 элементов', file=sys.stderr)
        exit(1)

    i_max = a.index(max(a))
    a[0], a[i_max] = a[i_max], a[0]
    print(a)
