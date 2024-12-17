from antlr4 import *
from typing import Optional, Dict, Set
from antlr4.error.ErrorListener import ErrorListener
from CPPLexer import CPPLexer
from CPPParser import CPPParser
from CPPToPythonVisitor import CPPToPythonVisitor
from translation.ExpressionConverter import ExpressionConverter
from translation.DeclarationConverter import DeclarationConverter
from translation.StatementConverter import StatementConverter
from translation.ClassConverter import ClassConverter
from translation.FunctionConverter import FunctionConverter
from translation.IncludeConverter import IncludeConverter

class CppToPythonTranspiler:
    def __init__(self):
        """Initialize the transpiler with all necessary converters"""
        self.expression_converter = ExpressionConverter()
        self.declaration_converter = DeclarationConverter()
        self.statement_converter = StatementConverter()
        self.class_converter = ClassConverter()
        self.function_converter = FunctionConverter()
        self.include_converter = IncludeConverter()
        self.visitor = None
        self.output = ""

    def configure_visitor(self, visitor):
        """Configure the visitor with all converters"""
        visitor.expression_converter = self.expression_converter
        visitor.declaration_converter = self.declaration_converter
        visitor.statement_converter = self.statement_converter
        visitor.class_converter = self.class_converter
        visitor.function_converter = self.function_converter
        visitor.include_converter = self.include_converter

    def transpile(self, input_code: str) -> str:
        """Transpile C++ code to Python code"""
        print("DEBUG: Starting transpilation")
        try:
            # Create lexer and parser
            input_stream = InputStream(input_code)
            lexer = CPPLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = CPPParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(TranspilerErrorListener())
            
            # Reset include converter state
            self.include_converter.reset()
            
            # Create and configure visitor
            self.visitor = CPPToPythonVisitor(lexer)
            self.configure_visitor(self.visitor)
            
            # Parse and visit
            tree = parser.program()
            self.visitor.visitProgram(tree)
            
            # Generate output with imports
            output_lines = []
            
            # Add imports first
            imports = self.include_converter.get_all_imports()
            if imports:
                output_lines.extend(imports)
                output_lines.append("")  # Empty line after imports
            
            # Add transpiled code
            if self.visitor.get_output():
                output_lines.append(self.visitor.get_output())
            
            return "\n".join(output_lines)

        except Exception as e:
            print(f"ERROR: Transpilation failed: {str(e)}")
            raise

class TranspilerError(Exception):
    """Custom exception for transpiler errors"""
    pass

class TranspilerErrorListener(ErrorListener):
    """Custom error listener for better error reporting"""
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise TranspilerError(f"Syntax error at line {line}, column {column}: {msg}")
    

if __name__ == "__main__":
    transpiler = CppToPythonTranspiler()
    print(transpiler.transpile("""
    class MyClass {
    private:
        int x;
        double y;
    public:
        MyClass(int a, double b) {
            x = a;
        }
        
        int getX() {
        }
    };
    """))
    print(transpiler.transpile("""
    int x = 0;
    int y = 1;                                                      
    if (x > 0) {
        y = x + 1;
        int z = 10;
        if(x > 2) {
            y = x + 1;
        } 
    } 
    else if(x<0){
        continue;
    }
    """))
    print(transpiler.transpile("""
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
    """))