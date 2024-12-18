from typing import List

def main():
    s = " " * 1000
    t = " " * 1000
    s, t = list(map(str, input().split()))
    m = None
    m = len(t)
    n = None
    n = len(s)
    next = [0] * 1000
    next[0] = -1
    j = None
    j = -1
    for i in range(1, m):
        while j >= 0 and t[i] != t[j + 1]:
            j = next[j]
        if t[i] == t[j + 1]:
            ((j:=j+1)-1)
        next[i] = j
    i = None
    i = 0
    k = None
    k = 0
    found = None
    found = False
    while i < n:
        if s[i] == t[k]:
            ((i:=i+1)-1)
            ((k:=k+1)-1)
        else:
            if k > 0:
                k = next[k - 1] + 1
            else:
                ((i:=i+1)-1)
        if k == m:
            print(i - m, " ", sep='', end='')
            k = next[k - 1] + 1
            found = True
    if  not found:
        print("False", sep='', end='')
    return 0

if __name__ == '__main__':
    main()