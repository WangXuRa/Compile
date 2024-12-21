#include <iostream>

class InsertionSort {
public:
    void sort(int* arr, int size) {
        for (int i = 1; i < size; ++i) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                --j;
            }
            arr[j + 1] = key;
        }
    }
};

int main() {
    int arr[100];
    int size = 0;

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

    InsertionSort sorter;
    sorter.sort(arr, size);

    std::cout << "Sorted array: ";
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
