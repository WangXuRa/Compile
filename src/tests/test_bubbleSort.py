from typing import List

def main():
    num = None
    a = [0] * 100
    print("Input the array length: ", sep='', end='')
    num = int(input())
    print("Input integers: ", sep='', end='')
    for i in range(0, num):
        a[i] = int(input())
    for i in range(num - 1, 0 - 1, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                tmp = None
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
    print("Result: ", sep='', end='')
    for i in range(0, num):
        print(a[i], " ", sep='', end='')
    print("\n", sep='', end='')
    return 0

if __name__ == '__main__':
    main()