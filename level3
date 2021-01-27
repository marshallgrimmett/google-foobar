import numpy as np
import math

#########################################################################
def solution1(n):
    stairs = np.zeros(((n + 1), (n + 1)), np.int)
    stairs[3, 2] = 1
    for i in range(4, (n + 1)):
        iMinStair = minStair(i)
        for j in range(iMinStair, i):
            if j == (i - j):
                stairs[i, j] += np.sum(stairs[(i - j), :])
            elif j < (i - j):
                jMinStair = minStair(j)
                stairs[i, j] += np.sum(stairs[(i - j), jMinStair:j])
            else:
                stairs[i, j] += np.sum(stairs[(i - j), :]) + 1
    return np.sum(stairs[n])

def minStair(stair):
    return int(math.ceil((-1 + math.sqrt(1 + (8*stair))) / 2))

print(solution1(5))

#########################################################################
def solution2(x, y):
    gen = 0
    x = int(x)
    y = int(y)
    while True:
        if x == 1 and y == 1:
            return str(gen)
        if x < 1 or y < 1:
            return str(gen-1)
            # return 'impossible'
        if x > y:
            newX = x % y
            gen += (x - newX) // y
            x = newX
        elif x < y:
            newY = y % x
            gen += (y - newY) // x
            y = newY

print(solution2('4', '7'))
print(solution2('2', '1'))
print(solution2('100000000000000000000000000000000000000000000000000', '1'))

#########################################################################
def solution3(l):
    combos = {}
    count = 0
    for i in enumerate(l):
        for j in enumerate(l[(i[0] + 1):]):
            if ((j[1] % i[1]) == 0):
                key = j[0] + i[0] + 1
                if key in combos:
                    combos[key] += 1
                else:
                    combos[key] = 1
                if i[0] in combos:
                    count += combos[i[0]]
    return count

print(solution3([1, 1, 1]))
print(solution3([1, 2, 3, 4, 5, 6]))
