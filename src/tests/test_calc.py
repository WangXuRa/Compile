from typing import List

class Stack:
    def __init__(self):
        self.top = -1
    def push(self, value: int) -> None:
        if self.top < 1000 - 1:
            self.top = self.top + 1
            self.data[self.top] = value
    def pop(self) -> int:
        if  not self.empty():
            value = None
            value = self.data[self.top]
            self.top = self.top - 1
            return value
        return 0
    def peek(self) -> int:
        if  not self.empty():
            return self.data[self.top]
        return 0
    def empty(self) -> bool:
        return self.top == -1
    def size(self) -> int:
        return self.top + 1
class Calculator:
    def calculate(self, s: str) -> int:
        nums = Stack()
        ops = Stack()
        len = None
        len = len(s)
        for i in range(0, len):
            if s[i] == ' ':
                continue
            if s[i].isdigit():
                num = None
                num = 0
                while i < len and s[i].isdigit():
                    num = num * 10 + (s[i] - '0')
                    ((i:=i+1)-1)
                ((i:=i-1)+1)
                nums.push(num)
            else:
                if s[i] == '-' and (i == 0 or s[i - 1] == '(' or s[i - 1] == '+' or s[i - 1] == '-' or s[i - 1] == '*' or s[i - 1] == '/'):
                    num = None
                    num = 0
                    while i < len and s[i].isdigit():
                        num = num * 10 + (s[i] - '0')
                        ((i:=i+1)-1)
                    ((i:=i-1)+1)
                    temp = None
                    temp = -1 * num
                    nums.push(temp)
                else:
                    if s[i] == '(':
                        ops.push(s[i])
                    else:
                        if s[i] == ')':
                            while  not ops.empty() and ops.peek() != '(':
                                self.calculateTop(nums, ops)
                            if  not ops.empty():
                                ops.pop()
                        else:
                            if self.isOperator(s[i]):
                                while  not ops.empty() and ops.peek() != '(' and self.precedence(ops.peek()) >= self.precedence(s[i]):
                                    self.calculateTop(nums, ops)
                                ops.push(s[i])
        while  not ops.empty():
            self.calculateTop(nums, ops)
        if nums.empty():
            return 0
        return nums.peek()
    def isOperator(self, c: str) -> bool:
        return c == '+' or c == '-' or c == '*' or c == '/'
    def precedence(self, op: str) -> int:
        if op == '*' or op == '/':
            return 2
        if op == '+' or op == '-':
            return 1
        return 0
    def calculateTop(self, nums: Stack, ops: Stack) -> None:
        if nums.size() < 2:
            return 
        b = None
        b = nums.pop()
        a = None
        a = nums.pop()
        op = None
        op = ops.pop()
        result = None
        result = 0
        if op == '+':
            result = a + b
        else:
            if op == '-':
                result = a - b
            else:
                if op == '*':
                    result = a * b
                else:
                    if op == '/':
                        result = a // b
        nums.push(result)
    def __init__(self):
        pass
def main():
    calc = Calculator()
    expr = None
    expr = "1+(-5-22)*4/(2+1)"
    result = None
    result = calc.calculate(expr)
    print("Result: ", result, "\n", sep='', end='')
    return 0

if __name__ == '__main__':
    main()