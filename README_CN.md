# 使用ANTLR4实现的C++词法分析器和语法解析器

本项目使用ANTLR4实现了C++的词法分析器和语法解析器。词法分析器可以将C++代码标记化，并识别各种语言元素，如关键字、运算符、字面量、标识符和注释。语法解析器可以解析C++代码并识别各种语言元素，如语句、表达式和声明。

## 团队成员

- [@王旭冉](https://github.com/WangXuRa)
- [@苏伟铭](https://github.com/wms2537)
- [@汪佳宇](https://github.com/Ccindy0171)
- [@陈立心](https://github.com/tls0523)

## 项目结构
项目结构如下：
- `src/cppLexer.g4` - 定义词法分析规则的ANTLR4语法文件
- `src/cppParser.g4` - 定义语法解析规则的ANTLR4语法文件
- `src/main.py` - 使用生成的词法分析器和语法解析器的Python脚本

## 环境要求

- Python 3.6或更高版本
- Java运行环境(JRE) - 用于运行ANTLR工具

## 安装步骤

1. 克隆此仓库：
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. 安装Python依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 在`src`目录下下载ANTLR4：
   ```bash
   cd src
   curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
   ```

4. 生成词法分析器代码：
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 cppLexer.g4
   ```

5. 生成语法解析器代码：
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 cppParser.g4
   ```

## 使用方法

您可以通过两种方式运行词法分析器：

1. 使用C++文件作为输入：
   ```bash
   python main.py path/to/your/cpp/file.cpp
   ```

2. 使用默认示例代码：
   ```bash
   python main.py
   ```

词法分析器将输出每个标记的类型和文本。

### 输出示例

对于输入代码：
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```
词法分析器和语法解析器的输出如下：
```
<INCLUDE> <iostream>
<NAMESPACE> std
<INT> int
<ID> main
<LPAREN> (
<RPAREN> )
<LBRACE> {
<COUT> cout
<STRING> "Hello, World!"
<SEMICOLON> ;
<RETURN> return
<INT> 0
<RBRACE> }
```

## 讨论
### 遇到的挑战
我们面临的最大挑战是C++语言的复杂性。它有许多不同的结构和特性，使得解析变得困难。我们花费了大量时间研究和讨论不同的语言解析方法。

### 解决方案
我们使用ANTLR4来生成词法分析器和语法解析器。ANTLR4是一个强大的工具，它允许我们以易于理解和修改的方式定义语言语法。它还为我们生成词法分析器和语法解析器代码，这为我们节省了大量时间和精力。

## 测试用例
我们使用各种C++代码测试了词法分析器和语法解析器。我们还测试了语法不正确的代码，以查看它们如何处理错误。

以下是我们使用的一些测试用例：
### 正确的代码
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

### 错误的代码
```cpp
int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

### 错误处理
词法分析器和语法解析器能够处理代码中的错误。例如，如果存在语法错误，词法分析器和语法解析器都会打印错误消息。

### 结论
这个项目对我们来说是一次很好的学习经历。我们学到了很多关于C++语言及其解析方法的知识。我们还学习了如何使用ANTLR4生成词法分析器和语法解析器代码。

## 参考资料
- [ANTLR4文档](https://www.antlr.org/documentation.html)
- [C++文档](https://en.cppreference.com/w/)



