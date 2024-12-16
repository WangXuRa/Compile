from antlr4 import *
from typing import Optional, Dict, Set
from antlr4.error.ErrorListener import ErrorListener
from CPPLexer import CPPLexer
from CPPParser import CPPParser
from CPPToPythonVisitor import CPPToPythonVisitor
from translation.ExpressionConverter import ExpressionConverter
from translation.DeclarationConverter import DeclarationConverter

class CppToPythonTranspiler:
    def __init__(self):
        # Initialize converters
        self.expression_converter = ExpressionConverter()
        self.declaration_converter = DeclarationConverter()
        
        # Initialize other attributes
        self.visitor = None
        self.output: str = ""
        self.includes: Set[str] = set()
        self.namespaces: Dict[str, Dict] = {}
        self.source_map: Dict[int, int] = {}
        
        # Standard library mappings
        self.STL_MAPPINGS = {
            "vector": "list",
            "string": "str",
            "map": "dict",
            "set": "set",
            "cout": "print",
            "endl": "\'\\n\'",
        }

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
            
            print("DEBUG: Created lexer and parser")
            
            # Create visitor and pass the converters
            self.visitor = CPPToPythonVisitor(lexer)
            self.visitor.expression_converter = self.expression_converter
            self.visitor.declaration_converter = self.declaration_converter
            
            print("DEBUG: Created and configured visitor")
            
            # Parse program and visit the parse tree
            tree = parser.program()
            print("DEBUG: Parsed program")
            
            # Explicitly call visitProgram
            print("DEBUG: Calling visitProgram")
            self.visitor.visitProgram(tree)
            
            # Get the output
            self.output = self.visitor.get_output()
            
            print(f"DEBUG: Generated output: {self.output}")
            return self.output

        except Exception as e:
            print(f"ERROR: Transpilation failed: {str(e)}")
            raise

    def _process_includes(self, tree) -> None:
        """Process include directives and map them to Python imports"""
        python_imports = []
        
        # Map C++ includes to Python imports
        include_map = {
            "iostream": ["from sys import stdout", "print = stdout.write"],
            "vector": "from typing import List",
            "string": "from typing import String",
            "map": "from typing import Dict",
            "memory": "from typing import Optional",
        }
        
        for include in self.visitor.get_includes(tree):
            if include in include_map:
                if isinstance(include_map[include], list):
                    python_imports.extend(include_map[include])
                else:
                    python_imports.append(include_map[include])
        
        self.includes = set(python_imports)
    
    def _process_namespaces(self, tree) -> None:
        """Process namespace declarations"""
        current_namespace = ""
        
        for namespace in self.visitor.get_namespaces(tree):
            current_namespace = namespace
            self.namespaces[namespace] = {}
    
    def _generate_output(self) -> str:
        """Generate the final Python code with imports and namespace handling"""
        output_lines = []
        
        # Add imports
        if self.includes:
            output_lines.extend(sorted(self.includes))
            output_lines.append("")
        
        # Add transpiled code from visitor
        if self.visitor and self.visitor.get_output():
            output_lines.append(self.visitor.get_output())
        
        return "\n".join(output_lines)

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
            int x;
    bool y, z;
    char a[10];
    std::string b[10];
    int a = 3 * 4;
    x = a++ - 10;
    std::string c;
    c = b[--x] + "hello";
    std::cin >> x;
    std::cout << x;
    std::cin >> x >> a;
    std::cout << a << " " << x << std::endl;
    """))
