#include <iostream>

class QuickSort {
public:
    void sort(int* arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);

            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }

private:
    int partition(int* arr, int low, int high) {
        int pivot = arr[high]; 
        int i = low - 1;      

        for (int j = low; j < high; ++j) {
            if (arr[j] < pivot) {
                ++i;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }
};

int main() {
    int arr[8];
    int size = 8;

    arr[0] = 38;
    arr[1] = 27;
    arr[2] = 43;
    arr[3] = 3;
    arr[4] = 9;
    arr[5] = 82;
    arr[6] = 10;
    arr[7] = 19;

    std::cout << "Original array: ";
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    QuickSort sorter;
    sorter.sort(arr, 0, size - 1);

    std::cout << "Sorted array: ";
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
