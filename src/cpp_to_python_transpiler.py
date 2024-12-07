from antlr4 import *
from typing import Optional, Dict, Set
from antlr4.error.ErrorListener import ErrorListener  # Add this import
from CPPLexer import CPPLexer
from CPPParser import CPPParser
from CPPToPythonVisitor import CPPToPythonVisitor
from TypeConverter import TypeConverter
from ExpressionConverter import ExpressionConverter
from StatementConverter import StatementConverter
from ClassConverter import ClassConverter
from TemplateConverter import TemplateConverter

class CppToPythonTranspiler:
    def __init__(self):
        self.type_converter = TypeConverter()
        self.expression_converter = ExpressionConverter()
        self.statement_converter = StatementConverter()
        self.class_converter = ClassConverter()
        self.template_converter = TemplateConverter()
        
        self.visitor = CPPToPythonVisitor()
        self.visitor.set_converters(
            type_converter=self.type_converter,
            expression_converter=self.expression_converter,
            statement_converter=self.statement_converter,
            class_converter=self.class_converter,
            template_converter=self.template_converter
        )
        
        self.output: str = ""
        self.includes: Set[str] = set()
        self.namespaces: Dict[str, Dict] = {}
        self.source_map: Dict[int, int] = {}  # Maps Python line numbers to C++ line numbers
        
        # Standard library mappings
        self.STL_MAPPINGS = {
            "vector": "list",
            "string": "str",
            "map": "dict",
            "set": "set",
            "cout": "print",
            "endl": "\'\\n\'",
        }
        
    def transpile_file(self, input_file: str) -> str:
        """
        Transpile a C++ file to Python code
        Args:
            input_file: Path to the C++ source file
        Returns:
            Transpiled Python code as string
        """
        try:
            input_stream = FileStream(input_file)
            return self._transpile_stream(input_stream)
        except FileNotFoundError:
            raise TranspilerError(f"File not found: {input_file}")
        except Exception as e:
            raise TranspilerError(f"Failed to transpile file {input_file}: {str(e)}")
    
    def transpile_string(self, input_code: str) -> str:
        """
        Transpile C++ code string to Python code
        Args:
            input_code: C++ source code as string
        Returns:
            Transpiled Python code as string
        """
        try:
            input_stream = InputStream(input_code)
            return self._transpile_stream(input_stream)
        except Exception as e:
            raise TranspilerError(f"Failed to transpile code: {str(e)}")
    
    def _transpile_stream(self, input_stream: InputStream) -> str:
        """
        Internal method to handle the actual transpilation
        """
        try:
            # Create the lexer and parser with error handling
            lexer = CPPLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(TranspilerErrorListener())
            
            stream = CommonTokenStream(lexer)
            parser = CPPParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(TranspilerErrorListener())
            
            # Parse the input
            tree = parser.translationUnit()
            
            # Process includes and namespaces first
            self._process_includes(tree)
            self._process_namespaces(tree)
            
            # Walk the tree with our visitor
            self.visitor.reset()
            self.visitor.visit(tree)
            
            # Generate the final Python code
            return self._generate_output()
            
        except Exception as e:
            raise TranspilerError(f"Transpilation error: {str(e)}")
    
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
        
        # Add transpiled code
        output_lines.append(self.visitor.get_output())
        
        return "\n".join(output_lines)

class TranspilerError(Exception):
    """Custom exception for transpiler errors"""
    pass

class TranspilerErrorListener(ErrorListener):
    """Custom error listener for better error reporting"""
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise TranspilerError(f"Syntax error at line {line}, column {column}: {msg}")