#include <iostream>
#include <string>

int main() {
    int strLength;
    std::cout << "Please enter the length of the string: ";
    std::cin >> strLength;

    // 使用 std::string 来代替 char 数组
    std::string inputStr;
    std::cout << "Please enter the string: ";
    std::cin >> inputStr;

    // 判断回文
    int midPoint = strLength / 2;
    for (int i = 0; i < midPoint; ++i) {
        // 比较字符串前后对应字符
        if (inputStr[i] != inputStr[strLength - 1 - i]) {
            std::cout << "The string is not a palindrome." << std::endl;
            return 0;
        }
    }

    std::cout << "The string is a palindrome." << std::endl;
    return 0;
}
