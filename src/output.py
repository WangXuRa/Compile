class InsertionSort:
    def sort(self, arr: int, size: int) -> None:
        i = None
        i = 1
        while i < size:
            key = None
            key = arr[i]
            j = None
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                (j:=j-1)
            arr[j + 1] = key
            (i:=i+1)
    def __init__(self):
        pass
def main():
    arr = [0] * 6
    size = None
    size = 6
    arr[0] = 12
    arr[1] = 11
    arr[2] = 13
    arr[3] = 5
    arr[4] = 6
    arr[5] = 7
    print("Original array: ", sep='', end='')
    i = None
    i = 0
    while i < size:
        print(arr[i], " ", sep='', end='')
        (i:=i+1)
    print("\n", sep='', end='')
    sorter = InsertionSort()
    sorter.sort(arr, size)
    print("Sorted array: ", sep='', end='')
    i = None
    i = 0
    while i < size:
        print(arr[i], " ", sep='', end='')
        (i:=i+1)
    print("\n", sep='', end='')
    return 0

if __name__ == '__main__':
    main()