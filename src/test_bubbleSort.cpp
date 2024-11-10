int main() {
    int num;
    int a[100];  // 固定大小数组

    // 输入数组长度
    cout << "Input the array length: ";
    cin >> num;

    // 输入整数
    cout << "Input integers: ";
    for (int i = 0; i < num; i++) {
        cin >> a[i];
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
    cout << "Result: ";
    for (int i = 0; i < num; i++) {
        cout << a[i] << " ";
    }
    cout << endl;

    return 0;
}