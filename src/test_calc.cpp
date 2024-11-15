#include <iostream>
#include <string>

class Stack {
private:
    std::string elements[100];  // 假设栈最多能存储 100 个元素
    int topIndex = -1;

public:
    void push(std::string &val) {
        if (topIndex < 99) {  // 确保不越界
            elements[++topIndex] = val;
        } else {
            std::cerr << "Stack overflow!" << std::endl;
        }
    }

    void pop() {
        if (!empty()) {
            --topIndex;
        }
    }

    std::string top() {
        if (!empty()) {
            return elements[topIndex];
        } else {
            return "";
        }
    }

    bool empty() {
        return topIndex == -1;
    }

    int size() {
        return topIndex + 1;
    }
};

// 自定义判断字符是否为空格
bool isSpace(char c) {
    return c == ' ' || c == '\t' || c == '\n' || c == '\r';
}

// 自定义判断字符是否是数字
bool isDigit(char c) {
    return c >= '0' && c <= '9';
}

// 判断运算符优先级
int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

// 中缀表达式转换为逆波兰表达式（后缀表达式）
Stack toRPN(std::string &s) {
    Stack rpn;
    Stack ops;
    int n = s.size();

    for (int i = 0; i < n; ++i) {
        if (isSpace(s[i])) continue;

        if (isDigit(s[i]) || (s[i] == '-' && (i == 0 || s[i - 1] == '('))) {
            std::string num;
            num = num + s[i++];
            while (i < n && isDigit(s[i])) {
                num = num + s[i++];
            }
            i--;
            rpn.push(num);
        } else if (s[i] == '(') {
            std::string temp;
            temp.push_back(s[i]);
            ops.push(temp);
        } else if (s[i] == ')') {
            while (!ops.empty() && ops.top() != "(") {
                std::string top = ops.top(); 
                rpn.push(top);  
                ops.pop();
            }
            ops.pop();
        } else {
            while (!ops.empty()) {
                std::string top = ops.top();  // 获取栈顶的字符串
                if (precedence(top[0]) >= precedence(s[i])) {  // 比较栈顶字符的优先级
                    rpn.push(top);  // 如果优先级大或等于，则将栈顶元素推入rpn
                    ops.pop();      // 从操作符栈中弹出栈顶元素
                } else {
                    break;  // 如果当前操作符优先级较低，跳出循环
                }
            }
            std::string temp;
            temp.push_back(s[i]);
            ops.push(temp);
        }
    }

    while (!ops.empty()) {
        std::string temp = ops.top(); 
        rpn.push(temp);  
        ops.pop();
    }
    return rpn;
}

// 计算逆波兰表达式的值
int evalRPN(Stack &rpn) {
    Stack values;
    while (!rpn.empty()) {
        std::string token = rpn.top();
        rpn.pop();

        if (isDigit(token[0]) || (token.size() > 1 && token[0] == '-')) {
            values.push(token);
        } else {
            int b = std::stoi(values.top()); values.pop();
            int a = std::stoi(values.top()); values.pop();
            if (token == "+") {
                std::string result = std::to_string(a + b); // 使用 std::to_string 计算并创建字符串
                values.push(result);  // 将 result 推入栈中
            } else if (token == "-") {
                std::string result = std::to_string(a - b); // 同样处理减法
                values.push(result);
            } else if (token == "*") {
                std::string result = std::to_string(a * b); // 同样处理乘法
                values.push(result);
            } else if (token == "/") {
                std::string result = std::to_string(a / b); // 同样处理除法
                values.push(result);
            }
        }
    }
    return std::stoi(values.top());
}

// 计算表达式的最终值
int calculate(std::string &s) {
    Stack rpn = toRPN(s);
    Stack reversedRPN;
    while (!rpn.empty()) {
        std::string temp = rpn.top(); 
        reversedRPN.push(temp);        
        rpn.pop();
    }
    return evalRPN(reversedRPN);
}

int main() {
    std::string s = "1+(-5-22)*4/(2+1)";
    std::cout << calculate(s) << std::endl;  // 输出: -35
    return 0;
}
