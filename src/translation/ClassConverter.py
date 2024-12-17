import sys
sys.path.append(sys.path[0] + '/..')

from translation.Node import Node
from translation.ExpressionConverter import ExpressionConverter
from translation.DeclarationConverter import DeclarationConverter
from translation.StatementConverter import StatementConverter

class ClassConverter:
    """
    Offers methods for converting class definitions to Python code
    """
    def __init__(self):
        self.expressionConverter = ExpressionConverter()
        self.declarationConverter = DeclarationConverter()
        self.statementConverter = StatementConverter()

    def convert_class(self, class_node: Node, current_vars: dict[str, str], custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """
        Converts a class definition node to Python code
        Returns a list of strings representing the Python class definition
        """
        if class_node.node_type != "classDefinition":
            raise TypeError("Class node must be of type classDefinition!")
        
        # Get class name
        class_name = class_node.children[1].value
        custom_classes.append(class_name)
        
        # Start with class definition
        py_lines = [f"class {class_name}:"]
        
        # Process class body
        class_body = class_node.children[3]  # classBody node
        if class_body.node_type != "classBody":
            raise TypeError("Invalid class body node!")
        
        # Track current access level for private member handling
        current_access = "public"
        
        # Process class members
        class_vars = {}  # Track class member variables with self. prefix
        constructor_found = False
        
        # First pass: Process all member declarations
        for child in class_body.children:
            if child.node_type == "accessSpecifier":
                current_access = child.children[0].value.lower()
                continue
            
            if child.node_type == "declaration":
                # Handle declaration with decl_ structure
                decl_node = child.children[0]  # Get decl_ node
                if decl_node.node_type == "decl_":
                    type_node = decl_node.children[0]  # typeSpecifier
                    declarator_node = decl_node.children[1]  # declarator
                    
                    cpp_type = type_node.children[0].value
                    var_name = declarator_node.children[0].value
                    py_type = self.declarationConverter.convert_type(None, cpp_type)
                    
                    # Add to class_vars with self prefix (no underscore)
                    class_var_name = f"self.{var_name}"
                    class_vars[class_var_name] = py_type
                    
                    # Add to current_vars
                    current_vars[var_name] = py_type  # Original name
        
        # Second pass: Generate Python code
        current_access = "public"  # Reset access level for second pass
        for child in class_body.children:
            if child.node_type == "accessSpecifier":
                current_access = child.children[0].value.lower()
            elif child.node_type == "constructor":
                if constructor_found:
                    raise SyntaxError("Multiple constructors are not supported!")
                constructor_found = True
                constructor_lines = self.convert_constructor(child, class_vars, current_vars, custom_classes, current_functions)
                py_lines.extend(["    " + line for line in constructor_lines])
        
        # If no constructor was defined, add a default one
        if not constructor_found:
            py_lines.extend(["    def __init__(self):", "        pass"])
        
        return py_lines

    def convert_constructor(self, constructor_node: Node, class_vars: dict[str, str], 
                           current_vars: dict[str, str], custom_classes: list[str], 
                           current_functions: list[str]) -> list[str]:
        """
        Converts a constructor node to Python __init__ method
        """
        py_lines = []
        
        # Start with constructor definition
        params = []
        if len(constructor_node.children) > 2 and constructor_node.children[2].node_type == "parameterList":
            params = self.convert_parameter_list(constructor_node.children[2])
        
        # Add self parameter
        param_str = "self" + (", " + ", ".join(params) if params else "")
        py_lines.append(f"def __init__({param_str}):")
        
        # Create a new scope with both class variables and current variables
        method_vars = {}
        
        # Add class variables to method scope
        for var_name, var_type in class_vars.items():
            # Get the variable name without self. prefix
            base_name = var_name.replace('self.', '')
            # Add both versions to method_vars
            method_vars[var_name] = var_type  # Add with self. prefix
            method_vars[base_name] = var_type  # Add without self. prefix
        
        # Add current variables
        method_vars.update(current_vars)
        
        # Add parameter variables to method scope
        if params:
            for param in params:
                name, type_hint = param.split(': ')
                method_vars[name] = type_hint
        
        # Convert constructor body
        compound_statement = constructor_node.children[-1]
        body_lines = self.statementConverter.convert_compoundStatement(
            compound_statement,
            method_vars,
            custom_classes,
            current_functions
        )
        
        # Add self. prefix to class member assignments if needed
        processed_lines = []
        for line in body_lines:
            if '=' in line:
                var_name = line.split('=')[0].strip()
                if var_name in method_vars and f"self.{var_name}" in class_vars:
                    line = f"self.{var_name}" + line[len(var_name):]
            processed_lines.append(line)
        
        py_lines.extend(["    " + line for line in processed_lines])
        
        return py_lines

    def convert_parameter_list(self, param_list_node: Node) -> list[str]:
        """
        Converts a parameter list node to a list of Python parameter strings with type hints
        """
        params = []
        for i in range(0, len(param_list_node.children), 2):  # Skip commas
            param_node = param_list_node.children[i]
            # Get parameter type from first child (typeSpecifier)
            cpp_type = param_node.children[0].children[0].value
            py_type = self.declarationConverter.convert_type(None, cpp_type)
            # Get parameter name from last child (ID)
            param_name = param_node.children[-1].value
            # Create parameter with type hint
            params.append(f"{param_name}: {py_type}")
        return params

    def convert_member_declaration(self, member_node: Node, class_vars: dict[str, str], 
                             custom_classes: list[str], current_functions: list[str], 
                             private: bool = False) -> list[str]:
        """
        Converts a member declaration to Python code
        """
        type_node = member_node.children[0]  # typeSpecifier
        declarator_node = member_node.children[1]  # declarator
        
        cpp_type = type_node.children[0].value
        var_name = declarator_node.children[0].value
        py_type = self.declarationConverter.convert_type(None, cpp_type)
        
        if private:
            var_name = '_' + var_name
        
        class_var_name = 'self.' + var_name
        class_vars[class_var_name] = py_type
        
        return [f"{class_var_name}: {py_type} = None"]

    def convert_method(self, method_node: Node, class_vars: dict[str, str], custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """
        Converts a method definition to Python code with return type hint
        """
        py_lines = []
        
        # Get method name and return type
        return_type = self.declarationConverter.convert_type(None, method_node.children[0].children[0].value)
        method_name = method_node.children[1].value
        
        # Convert parameters
        params = ["self"]
        if len(method_node.children) > 3 and method_node.children[3].node_type == "parameterList":
            params.extend(self.convert_parameter_list(method_node.children[3]))
        
        # Add method definition with return type hint
        py_lines.append(f"def {method_name}({', '.join(params)}) -> {return_type}:")
        
        # Create a new scope with class variables
        method_vars = class_vars.copy()
        
        # Convert method body using StatementConverter
        compound_statement = method_node.children[-1]
        body_lines = self.statementConverter.convert_compoundStatement(
            compound_statement,
            method_vars,  # Use the new scope with class variables
            custom_classes,
            current_functions
        )
        py_lines.extend(["    " + line for line in body_lines])
        
        return py_lines

    def convert_compound_statement(self, compound_node: Node, class_vars: dict[str, str], custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """
        Converts a compound statement to Python code
        """
        if not compound_node.children:
            return ["pass"]
        
        # Use StatementConverter to convert the compound statement
        return self.statementConverter.convert_compoundStatement(
            compound_node, 
            class_vars, 
            custom_classes, 
            current_functions
        )

# Testing code (similar to other converters)
if __name__ == "__main__":
    from antlr4 import InputStream, CommonTokenStream
    from CPPLexer import CPPLexer 
    from CPPParser import CPPParser 
    from CPPParserVisitor import CPPParserVisitor

    class_converter = ClassConverter()
    
    sample_code = """
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
    """
    
    input_stream = InputStream(sample_code)

    print("# Lexer #")

    # Create lexer
    lexer = CPPLexer(input_stream)
    
    # Get all tokens
    tokens = lexer.getAllTokens()
    
    # Print tokens
    for token in tokens:
        token_type = lexer.symbolicNames[token.type]
        token_text = token.text
        print(f"Token: {token_type:20} Text: {token_text}")

    lexer.reset()
    
    token_stream = CommonTokenStream(lexer)
    
    print("\n\n# Parser #")
    parser = CPPParser(token_stream)

    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found")
    else:
        visitor = CPPParserVisitor(parser)
        ast_tree = visitor.visit(tree)

        # Save AST to XML file
        with open("class_ast_output.xml", "w", encoding="utf-8") as file:
            file.write("<AST>\n")
            file.write(str(ast_tree)) 
            file.write("\n</AST>")
        
        print("AST has been saved to 'class_ast_output.xml'")
        
        current_vars = {}
        custom_classes = []
        current_functions = []
        
        # Find and convert class definitions
        def traverse_tree(node: Node, current_vars, custom_classes, current_functions):
            if node.node_type == "classDefinition":
                print("Found a class definition, here are the translated results:")
                for line in class_converter.convert_class(node, current_vars, custom_classes, current_functions):
                    print(line)
            else:
                for child in node.children:
                    traverse_tree(child, current_vars, custom_classes, current_functions)
        
        traverse_tree(ast_tree, current_vars, custom_classes, current_functions)
        print("\nCurrent variables:", current_vars)
        print("Custom classes:", custom_classes)
        print("Current functions:", current_functions)
