import numpy as np

#########################################################################
def solution1(n, b):
    prevIds = [int(n)]
    while True:
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        xInt = int(x, b)
        yInt = int(y, b)
        nInt = xInt - yInt
        n = np.base_repr(nInt, base=b)
        if int(n) in prevIds:
            break
        prevIds.append(int(n))
    return len(prevIds[prevIds.index(int(n)):])

print(solution1('1211', 10))

#########################################################################
def solution2(h, q):
    converters = []
    for i in q:
        left = 1
        root = (2**h) - 1
        if (i >= root) or (i < 1):
            converters.append(-1)
        else:
            while True:
                if i < ((left // 2) + (root // 2)):
                    root = ((left // 2) + (root // 2))
                elif i == ((left // 2) + (root // 2)):
                    converters.append(root)
                    break
                elif i < (root - 1):
                    left = ((left // 2) + (root // 2))
                    root = root - 1
                elif i == (root - 1):
                    converters.append(root)
                    break
    return converters

print(solution2(5, [19, 14, 28]))
