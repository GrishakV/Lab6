#!/usr/bin/env python3
# -*- config: utf-8 -*-

import sys


if __name__ == '__main__':
    a = list(map(int, input().split()))
    if not a:
        print('Заданный список пуст', file=sys.stderr)
        exit(1)

    a_min = a_max = a[0]
    i_min = i_max = 0
    for i, item in enumerate(a):
        if item < a_min:
            i_min, a_min = i, item
        elif item >= a_max:
            i_max, a_max = i, item

    if i_min > i_max:
        i_min, i_max = i_max, i_min

    count = 0
    for item in a[i_min+1:i_max]:
        if item > 0:
            count += 1

    print(count)
