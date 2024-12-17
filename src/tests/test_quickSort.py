from typing import List

class QuickSort:
    def sort(self, arr: int, low: int, high: int) -> None:
        if low < high:
            pi = None
            pi = self.partition(arr, low, high)
            self.sort(arr, low, pi - 1)
            self.sort(arr, pi + 1, high)
    def partition(self, arr: int, low: int, high: int) -> int:
        pivot = None
        pivot = arr[high]
        i = None
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                (i:=i+1)
                temp = None
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        temp = None
        temp = arr[i + 1]
        arr[i + 1] = arr[high]
        arr[high] = temp
        return i + 1
    def __init__(self):
        pass
def main():
    arr = [0] * 8
    size = None
    size = 8
    arr[0] = 38
    arr[1] = 27
    arr[2] = 43
    arr[3] = 3
    arr[4] = 9
    arr[5] = 82
    arr[6] = 10
    arr[7] = 19
    print("Original array: ", sep='', end='')
    for i in range(0, size):
        print(arr[i], " ", sep='', end='')
    print("\n", sep='', end='')
    sorter = QuickSort()
    sorter.sort(arr, 0, size - 1)
    print("Sorted array: ", sep='', end='')
    for i in range(0, size):
        print(arr[i], " ", sep='', end='')
    print("\n", sep='', end='')
    return 0

if __name__ == '__main__':
    main()