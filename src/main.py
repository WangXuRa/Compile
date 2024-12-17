from antlr4 import *
from CPPLexer import CPPLexer 
from CPPParser import CPPParser 
from CPPParserListener import CPPParserListener 
from CPPParserVisitor import CPPParserVisitor
from cpp_to_python_transpiler import CppToPythonTranspiler
import sys

def read_input_from_file(filename):
    # Get input from a file 
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return InputStream(file.read())
    except IOError:
        print(f"无法读取文件: {filename}")
        sys.exit(1) 

def main():
    # Get input from a file or string
    if len(sys.argv) > 1:
        input_stream = read_input_from_file(sys.argv[1])
        cpp_code = input_stream.strdata
    else:
        # Example C++ code for testing
        cpp_code = """
        #include <iosteam>
        #include <stdio.h>
        int main() {
            std::cout << "43";
            int x = 42;
            x++;
            ++x;
            int y = --x;
            bool z = false;
            if (x > 0) {
                return x;
            }
            return 0;
        }
        """

    # Create transpiler instance
    transpiler = CppToPythonTranspiler()
    
    try:
        # Transpile the code
        python_code = transpiler.transpile(cpp_code)
        
        # Save the transpiled code to a file
        with open("output.py", "w", encoding="utf-8") as file:
            file.write(python_code)
        
        print("Successfully transpiled C++ to Python!")
        print("Output saved to 'output.py'")
        print("\nTranspiled Python code:")
        print("-" * 40)
        print(python_code)
        
    except Exception as e:
        print(f"Transpilation error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
