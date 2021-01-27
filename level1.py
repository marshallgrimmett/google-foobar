def solution(s):
    l = len(s)
    best = 1
    for i in range(2, l+1):
        if l % i == 0:
            flag = True
            parts = int(l/i)
            for j in range(i):
                if s[0:parts] != s[(j*parts):((j+1)*parts)]:
                    flag = False
                    break
            if flag:
                best = i
    return best

s = 'abcabcabcabc'
print(solution(s))
