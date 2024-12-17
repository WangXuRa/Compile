from typing import List

class MergeSort:
    def merge(self, arr: int, left: int, mid: int, right: int, temp: int) -> None:
        i = None
        i = left
        j = None
        j = mid + 1
        k = None
        k = left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[((k:=k+1)-1)] = arr[((i:=i+1)-1)]
            else:
                temp[((k:=k+1)-1)] = arr[((j:=j+1)-1)]
        while i <= mid:
            temp[((k:=k+1)-1)] = arr[((i:=i+1)-1)]
        while j <= right:
            temp[((k:=k+1)-1)] = arr[((j:=j+1)-1)]
        for i in range(left, right + 1):
            arr[i] = temp[i]
    def mergeSort(self, arr: int, left: int, right: int, temp: int) -> None:
        if left >= right:
            return 
        mid = None
        mid = left + (right - left) // 2
        self.mergeSort(arr, left, mid, temp)
        self.mergeSort(arr, mid + 1, right, temp)
        self.merge(arr, left, mid, right, temp)
    def sort(self, arr: int, size: int) -> None:
        temp = [0] * 100
        self.mergeSort(arr, 0, size - 1, temp)
    def __init__(self):
        pass
def main():
    arr = [0] * 8
    size = None
    size = 7
    arr[0] = 38
    arr[1] = 27
    arr[2] = 43
    arr[3] = 3
    arr[4] = 9
    arr[5] = 82
    arr[6] = 10
    print("Original array: ", sep='', end='')
    for i in range(0, size):
        print(arr[i], " ", sep='', end='')
    print("\n", sep='', end='')
    sorter = MergeSort()
    sorter.sort(arr, size)
    print("Sorted array: ", sep='', end='')
    for i in range(0, size):
        print(arr[i], " ", sep='', end='')
    print("\n", sep='', end='')
    return 0

if __name__ == '__main__':
    main()