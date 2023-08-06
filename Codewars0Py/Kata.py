import math
import copy

class Fib:
    #https://www.codewars.com/kata/52549d3e19453df56f0000fe

    def fib(n):
        a = 0
        b = 1
        for i in range(n - 1):
            temp = a
            a = b
            b = temp + a
        return a

class SquareSumSimple:
    #https://www.codewars.com/kata/5a6b24d4e626c59d5b000066
    #def square_sums_row(n):

    #    def dfs():
    #        if not inp: yield res
    #        for v in tuple(inp):
    #            if not res or not ((res[-1]+v)**.5 % 1):
    #                res.append(v)
    #                inp.discard(v)
    #                yield from dfs()
    #                inp.add(res.pop())

    #    inp, res = set(range(1,n+1)), []
    #    return next(dfs(), False)

    #from math import sqrt
    #def square_sums_row(n, lst=[0]):
    #    if len(lst) == n+1: return lst[1:]
    #    for i in range(1, n+1):
    #        if i in lst: continue
    #        if sqrt(lst[-1]+i).is_integer(): 
    #            res = square_sums_row(n, lst+[i])
    #            if res: return res
    #    return False



    def FindNextPower(number, pow = 2):
        root = math.pow(number + 1, 1./pow)
        ceilRoot = math.ceil(root)
        nextPower = ceilRoot ** pow
        return int(nextPower)

    def IsNumberInArr(arr, n):
        if (len(arr) == 0): return False
        for item in arr:
            if (item == n): return True
        return False

    def SquareSumRec(a, n, arr):
        b = 0
        c = a
        while True:
            c = FindNextPower(c)
            b = c - a
            if b == a or IsNumberInArr(arr, b): continue 
            if b > n: break 
            arrNext = list(arr)
            arrNext.append(b) 
            if len(arrNext) == n: return arrNext 
            resultArr = SquareSumRec(b, n, arrNext) 
            if resultArr != False: return resultArr 
        return False

    def square_sums_row(n):
        for a in range(1, n + 1):
            arr = list()
            arr.append(a)
            resultArr = SquareSumRec(a, n, arr)
            if resultArr != False: return resultArr
        return False


class RemoveEveryOther:
    #def remove_every_other(my_list):
    #return my_list[::2]
    def remove_every_other(my_list):
        tmp_list = []
        for i in range(0, len(my_list), 2):
            tmp_list.append(my_list[i])
        my_list[:] = tmp_list
        return my_list

class StringyString:
    #https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python
    #def stringy(size):
    #    return ('10' * size)[:size]
    def stringy(size):
        list = []
        for i in range(1, size + 1, 2):
            list.append('10')
        if size % 2 != 0:
            list[len(list) - 1] = '1'
        return ''.join(list)


            