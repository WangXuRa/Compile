# 使用ANTLR4实现的C++词法分析器和语法解析器

本项目使用ANTLR4实现了C++的词法分析器和语法解析器。词法分析器可以将C++代码标记化，并识别各种语言元素，如关键字、运算符、字面量、标识符和注释。语法解析器可以解析C++代码并识别各种语言元素，如语句、表达式和声明。

## 团队成员

- [@王旭冉](https://github.com/WangXuRa)
- [@苏伟铭](https://github.com/wms2537)
- [@汪佳宇](https://github.com/Ccindy0171)
- [@陈立心](https://github.com/tls0523)

## 项目结构
项目结构如下：
- `src/CPPLexer.g4` - 定义词法分析规则的ANTLR4语法文件
- `src/CPPParser.g4` - 定义语法解析规则的ANTLR4语法文件
- `src/main.py` - 使用生成的词法分析器和语法解析器的Python脚本
- `src/test_KMP.cpp` - KMP字符串匹配算法的测试用例
- `src/test_bubbleSort.cpp` - 冒泡排序算法的测试用例
- `src/cppParserBase.py` - 解析器基类实现
- `src/CPPParserVisitor.py` - 访问者模式实现，用于生成AST

## 环境要求

- Python 3.6或更高版本
- Java运行环境(JRE) - 用于运行ANTLR工具
- ANTLR4 Python运行时库

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

4. 生成词法分析器和解析器代码：
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 CPPLexer.g4
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 CPPParser.g4
   ```

## 使用方法

您可以通过两种方式运行词法分析器和解析器：

1. 使用C++文件作为输入：
   ```bash
   python main.py path/to/your/cpp/file.cpp
   ```

2. 使用默认示例代码：
   ```bash
   python main.py
   ```

程序将生成两种输出：
- 词法分析结果：显示所有识别的标记
- 语法分析结果：生成AST（抽象语法树）并保存到ast_output.xml文件中

## 测试用例

### 1. KMP字符串匹配算法 (test_KMP.cpp)
实现了经典的KMP字符串匹配算法，包含：
- 部分匹配表(next数组)的计算
- 字符串匹配过程
- 多重匹配支持
- 错误处理

### 2. 冒泡排序算法 (test_bubbleSort.cpp)
实现了基础的冒泡排序算法，特点：
- 动态数组输入
- 整数排序
- 结果可视化输出
- 交换操作优化

### 输出示例

对于冒泡排序测试用例(test_bubbleSort.cpp)：

输入（C++源代码）：
```cpp
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
    // ... 代码其余部分
}
```

词法分析输出：
```
Token: INCLUDE              Text: #include
Token: LT                   Text: <
Token: ID                   Text: iostream
Token: GT                   Text: >
Token: INT                  Text: int
Token: ID                   Text: main
Token: LPAREN               Text: (
Token: RPAREN               Text: )
Token: LBRACE               Text: {
Token: INT                  Text: int
Token: ID                   Text: num
Token: SEMICOLON            Text: ;
...
```

语法分析输出（AST节选）：
```xml
<AST>
<program>
  <includeStatement>
    <INCLUDE>#include</INCLUDE>
    <LT><</LT>
    <includeID>
      <ID>iosteam</ID>
    </includeID>
    <GT>></GT>
  </includeStatement>
  <includeStatement>
    <INCLUDE>#include</INCLUDE>
      ...
```

## 特性支持

当前版本支持以下C++语言特性：
- 基本数据类型 (int, char, bool等)
- 控制流语句 (if-else, for, while)
- 数组操作
- 基本输入输出
- 函数定义和调用
- 运算符和表达式
- 变量声明和赋值

## 错误处理

解析器能够处理多种错误情况：
- 语法错误检测
- 输入文件错误处理
- 解析过程错误报告
- AST生成异常处理

## 后续开发计划

1. 增加对类和对象的支持
2. 实现更多C++11特性
3. 优化AST生成效率
4. 添加更多测试用例
5. 改进错误提示信息

## 讨论
### 遇到的挑战
我们面临的最大挑战是C++语言的复杂性。它有许多不同的结构和特性，使得解析变得困难。我们花费了大量时间研究和讨论不同的语言解析方法。

### 解决方案
我们使用ANTLR4来生成词法分析器和语法解析器。ANTLR4是一个强大的工具，它允许我们以易于理解和修改的方式定义语言语法。它还为我们生成词法分析器和语法解析器代码，这为我们节省了大量时间和精力。

访问者模式的实现帮助我们生成了一个清晰的AST结构，可以轻松遍历和分析。我们还实现了细致的错误处理，使解析器更加健壮。

## 实验思路

### 1. 语法设计
- 从核心C++语法元素开始
  * 定义基本标记（关键字、运算符、标识符）
  * 实现带有适当优先级的表达式语法
  * 添加语句语法规则
  * 集成类型系统基础
- 将语法分为词法和语法解析规则
  * 词法分析器处理源代码的标记化
  * 语法解析器构建语法结构
  * 分离关注点以便于维护
- 仔细处理运算符优先级
  * 实现优先级爬升方法
  * 处理结合性规则
  * 管理复合运算符
- 实现基本C++结构的支持
  * 函数声明和定义
  * 变量声明
  * 控制结构
  * 数组声明和访问

### 2. AST构建
- 使用访问者模式构建语法树
  * 实现CPPParserVisitor类
  * 为每个语法构造创建节点类型
  * 构建层次结构
  * 维护源代码位置信息
- 设计节点结构以表示C++元素
  * 具有通用属性的基础Node类
  * 针对不同构造的专用节点
  * 类型信息的属性存储
  * 支持注释和注解
- 实现适当的父子关系
  * 双向节点引用
  * 作用域管理
  * 符号表集成
  * 交叉引用支持
- 添加代码块作用域支持
  * 块级符号表
  * 变量遮蔽处理
  * 作用域进入/退出跟踪
  * 声明/引用解析

### 3. 开发过程
1. 语法开发：
   - 首先实现基本表达式
     * 算术和逻辑运算符
     * 函数调用
     * 变量引用
     * 字面值
   - 添加语句支持
     * If-else条件
     * 循环（for, while）
     * Return语句
     * 表达式语句
   - 实现函数定义
     * 参数列表
     * 返回类型
     * 函数体
     * 前向声明
   - 添加数组支持
     * 数组声明
     * 数组访问
     * 多维数组
     * 数组初始化
   - 集成错误处理
     * 语法错误恢复
     * 错误消息
     * 警告生成
     * 错误位置跟踪

2. 测试策略：
   - 单个语法规则的单元测试
     * 表达式解析测试
     * 语句解析测试
     * 声明测试
     * 类型系统测试
   - 完整程序的集成测试
     * 完整函数测试
     * 程序结构测试
     * 多文件解析
     * Include处理
   - 错误处理的边缘情况测试
     * 无效语法恢复
     * 错误消息准确性
     * 解析器健壮性
     * 内存管理
   - 大文件的性能测试
     * 内存使用监控
     * 解析时间测量
     * AST大小优化
     * 标记流效率

3. 优化：
   - 改进语法规则以提高性能
     * 消除左递归
     * 规则因子化
     * 前瞻优化
     * 回溯减少
   - 优化访问者模式实现
     * 节点访问缓存
     * 延迟计算
     * 内存池化
     * 引用计数
   - 增强错误报告
     * 上下文错误消息
     * 建议生成
     * 错误恢复策略
     * 调试信息
   - 减少AST构建中的内存使用
     * 节点共享
     * 属性压缩
     * 内存池
     * 垃圾回收


## 参考资料
- [ANTLR4文档](https://www.antlr.org/documentation.html)
- [C++文档](https://en.cppreference.com/w/)