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
    int arr[100];
    int size = 8;

    // 输入数组长度
    std::cout << "Input the array length: ";
    std::cin >> size;

    // 输入整数
    std::cout << "Input integers: ";
    for (int i = 0; i < size; i++) {
        std::cin >> arr[i];
    }

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
