# !/usr/bin/env python3
# -*- config: utf-8 -*-

# Ваиант 10. В списке, состоящем из вещественных элементов, вычислить:
# 1) номер минимального по модулю элемента списка;
# 2) сумму модулей элементов списка, расположенных после первого отрицательного элемента.
# Сжать список, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце списка элементы заполнить нулями.

import sys

if __name__ == '__main__':
    x = list(map(float, input().split()))
    a = float(input('Введите a: '))
    b = float(input('Введите b: '))
    if not x:
        print('Заданный список пуст', file=sys.stderr)
        exit(1)
    if a > b:
        print('a не может быть больше b', file=sys.stderr)
        exit(1)

    new_x = [i for i in x if not a <= i <= b]
    z = len(x) - len(new_x)
    arr_z = [0]
    new_z = arr_z * z
    result = new_x + new_z
    print(result)
