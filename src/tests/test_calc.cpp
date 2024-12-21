#include <iostream>
#include <cctype>
#include <string>

// 自定义栈结构
class Stack {
private:

    int data[1000];
    int top;

public:
    // 构造函数
    Stack() {
        top = -1;
        int i = 0;
        while (i<1000){
            data[i] = 0;
            i++;
        }
    }
    
    void push(int value) {
        if (top < 1000 - 1) {
            top = top + 1;
            data[top] = value;
        }
    }
    
    int pop() {
        if (!empty()) {
            int value = data[top];
            top = top - 1;
            return value;
        }
        return 0;
    }
    
    int peek() {
        if (!empty()) {
            return data[top];
        }
        return 0;
    }
    
    bool empty() {
        return top == -1;
    }
    
    int size() {
        return top + 1;
    }
};

class Calculator {
public:
    int calculate(std::string s) {
        Stack nums;    // 数字栈
        Stack ops;     // 运算符栈
        int _len = s.length();
        
        int i = 0;
        while (i < _len) {
            if (s[i] == ' ') continue;
            
            // 处理数字
            if (isdigit(s[i])) {
                int num = 0;
                std::string n = "";
                while (i < _len && isdigit(s[i])) {
                    n = n + s[i];
                    i++;
                }
                i--;
                num = std::stoi(n);
                nums.push(num);
            }
            // 处理负数
            else if (s[i] == '-' && (i == 0 || s[i-1] == '(' || s[i-1] == '+' || 
                     s[i-1] == '-' || s[i-1] == '*' || s[i-1] == '/')) {
                
                int num = 0;
                std::string n = "";
                ++i;
                while (i < _len && isdigit(s[i])) {
                    n = n + s[i];
                    i++;
                }
                i--;
                num = std::stoi(n);
                int temp = -1 * num;
                nums.push(temp);
            }
            // 处理左括号
            else if (s[i] == '(') {
                ops.push(s[i]);
            }
            // 处理右括号
            else if (s[i] == ')') {
                while (!ops.empty() && ops.peek() != '(') {
                    calculateTop(nums, ops);
                }
                if (!ops.empty()) {
                    ops.pop(); // 弹出左括号
                }
            }
            // 处理运算符
            else if (isOperator(s[i])) {
                while (!ops.empty() && ops.peek() != '(' && 
                       precedence(ops.peek()) >= precedence(s[i])) {
                    calculateTop(nums, ops);
                }
                ops.push(s[i]);
            }
            i++;
        }
        
        while (!ops.empty()) {
            calculateTop(nums, ops);
        }
        
        if (nums.empty()) {
            return 0;
        }
        return nums.peek();
    }

private:
    bool isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/';
    }
    
    int precedence(char op) {
        if (op == '*' || op == '/') {
            return 2;
        }
        if (op == '+' || op == '-') {
            return 1;
        }
        return 0;
    }
    
    void calculateTop(Stack& nums, Stack& ops) {
        if (nums.size() < 2) {
            return;
        }
        int b = nums.pop();
        int a = nums.pop();
        char op = ops.pop();
        
        int result = 0;
        if (op == '+') {
            result = a + b;
        } else if (op == '-') {
            result = a - b;
        } else if (op == '*') {
            result = a * b;
        } else if (op == '/') {
            result = a / b;
        }
        nums.push(result);
    }
};

int main() {
    Calculator calc;
    std::string expr = "";
    std::cout << "请输入字符串：";
    std::cin  >> expr;
    int result = calc.calculate(expr);
    std::cout << "Result: " << result << std::endl;
    return 0;
}