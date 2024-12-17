from antlr4 import *
from CPPLexer import CPPLexer 
from CPPParser import CPPParser 
from CPPParserListener import CPPParserListener 
from CPPParserVisitor import CPPParserVisitor
from cpp_to_python_transpiler import CppToPythonTranspiler
import sys
import os

def read_input_from_file(filename):
    # Get input from a file 
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return InputStream(file.read())
    except IOError:
        print(f"无法读取文件: {filename}")
        sys.exit(1) 

def get_default_output_path(input_path):
    # Get the directory and filename without extension
    directory = os.path.dirname(input_path)
    basename = os.path.splitext(os.path.basename(input_path))[0]
    # Create output path with .py extension in same directory
    return os.path.join(directory, f"{basename}.py")

def main():
    # Check arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else get_default_output_path(input_file)

    # Get input from file
    input_stream = read_input_from_file(input_file)
    cpp_code = input_stream.strdata

    # Create transpiler instance
    transpiler = CppToPythonTranspiler()
    
    try:
        # Transpile the code
        python_code = transpiler.transpile(cpp_code)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Save the transpiled code to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(python_code)
        
        print(f"Successfully transpiled C++ to Python!")
        print(f"Output saved to '{output_file}'")
        print("\nTranspiled Python code:")
        print("-" * 40)
        print(python_code)
            
    except Exception as e:
        print(f"Transpilation error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
