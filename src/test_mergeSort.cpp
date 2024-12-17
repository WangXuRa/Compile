#include <iostream>

class MergeSort {
private:
    void merge(int* arr, int left, int mid, int right, int* temp) {
        int i = left;
        int j = mid + 1;
        int k = left;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (i = left; i <= right; ++i) {
            arr[i] = temp[i];
        }
    }

    void mergeSort(int* arr, int left, int right, int* temp) {
        if (left >= right) return;

        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid, temp);
        mergeSort(arr, mid + 1, right, temp);
        merge(arr, left, mid, right, temp);
    }

public:
    void sort(int* arr, int size) {
        int temp[100];
        mergeSort(arr, 0, size - 1, temp);
    }
};

int main() {
    int arr[8];
    int size = 7;

    arr[0] = 38;
    arr[1] = 27;
    arr[2] = 43;
    arr[3] = 3;
    arr[4] = 9;
    arr[5] = 82;
    arr[6] = 10;

    std::cout << "Original array: ";
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    MergeSort sorter;
    sorter.sort(arr, size);

    std::cout << "Sorted array: ";
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
