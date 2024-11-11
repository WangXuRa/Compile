#include <iostream>

int main() {
    int num;
    int a[100];  // 固定大小数组

    // 输入数组长度
    std::cout << "Input the array length: ";
    std::cin >> num;

    // 输入整数
    std::cout << "Input integers: ";
    for (int i = 0; i < num; i++) {
        std::cin >> a[i];
    }

    // 使用冒泡排序对数组进行排序
    for (int i = num - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            if (a[j] > a[j + 1]) {
                // 交换两个元素
                int tmp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = tmp;
            }
        }
    }

    // 输出排序后的结果
    std::cout << "Result: ";
    for (int i = 0; i < num; i++) {
        std::cout << a[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}