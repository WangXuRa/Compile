环境要求
- Python 3.9或更高版本
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
使用C++文件作为输入：
   ```bash
   python3 main.py path/to/your/cpp/file.cpp path/to/your/python/file.py
   ```
程序将生成python代码
通过python path/to/your/python/file.py 测试翻译生成的python文件是否正确