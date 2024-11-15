项目结构如下：
- `src/CPPLexer.g4` - 定义词法分析规则的ANTLR4语法文件
- `src/CPPParser.g4` - 定义语法解析规则的ANTLR4语法文件
- `src/main.py` - 使用生成的词法分析器和语法解析器的Python脚本
- `src/test_KMP.cpp` - KMP字符串匹配算法的测试用例
- `src/test_bubbleSort.cpp` - 冒泡排序算法的测试用例
- `src/cppParserBase.py` - 解析器基类实现
- `src/CPPParserVisitor.py` - 访问者模式实现，用于生成AST

环境要求
- Python 3.6或更高版本
- Java运行环境(JRE) - 用于运行ANTLR工具
- ANTLR4 Python运行时库

安装步骤
1. 在文件夹内打开代码：

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

使用方法
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