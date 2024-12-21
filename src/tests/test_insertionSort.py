from typing import List

class InsertionSort:
    def sort(self, arr: int, size: int) -> None:
        for i in range(1, size):
            key = None
            key = arr[i]
            j = None
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                (j:=j-1)
            arr[j + 1] = key
    def __init__(self):
            pass
def main():
    arr = [0] * 100
    size = None
    size = 0
    print("Input the array length: ", sep='', end='')
    size = int(input())
    print("Input integers: ", sep='', end='')
    for i in range(0, size):
        arr[i] = int(input())
    print("Original array: ", sep='', end='')
    for i in range(0, size):
        print(arr[i], " ", sep='', end='')
    print("\n", sep='', end='')
    sorter = InsertionSort()
    sorter.sort(arr, size)
    print("Sorted array: ", sep='', end='')
    for i in range(0, size):
        print(arr[i], " ", sep='', end='')
    print("\n", sep='', end='')
    return 0

if __name__ == '__main__':
    main()