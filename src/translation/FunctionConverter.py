import sys
sys.path.append(sys.path[0] + '/..')

from translation.Node import Node
from translation.ExpressionConverter import ExpressionConverter
from translation.DeclarationConverter import DeclarationConverter
from translation.StatementConverter import StatementConverter
from typing import List

class FunctionConverter:
    """
    Converts C++ function definitions to Python function definitions
    """
    def __init__(self):
        self.expression_converter = ExpressionConverter()
        self.declaration_converter = DeclarationConverter()
        self.statement_converter = StatementConverter()

    def convert_function(self, function_node: Node, current_vars: dict[str, str], 
                        custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert a function definition to Python code"""
        if function_node.node_type != "functionDefinition":
            raise TypeError("Expected functionDefinition node!")

        result = []
        
        # Get function name
        func_name = function_node.children[1].value
        current_functions.append(func_name)
        
        # Handle main function specially
        if func_name == "main":
            result.append("def main():")
        else:
            # Get return type and parameters (for future use)
            return_type = function_node.children[0].children[0].value
            result.append(f"def {func_name}():")  # TODO: Add parameter handling
        
        # Convert function body
        body_node = function_node.children[-1]  # Last child is compound statement (function body)
        if body_node.node_type == "compoundStatement":
            body_lines = self.statement_converter.convert_statement(
                body_node,
                current_vars,
                custom_classes,
                current_functions
            )
            # Indent function body
            result.extend(["    " + line for line in body_lines])
        
        # For main function, add the calling boilerplate
        if func_name == "main":
            result.extend([
                "",
                "if __name__ == '__main__':",
                "    main()"
            ])
        
        return result

    def convert_return_statement(self, return_node: Node, current_vars: dict[str, str],
                               custom_classes: list[str], current_functions: list[str]) -> str:
        """Convert a return statement to Python"""
        if not return_node.children:
            return "return"
        
        expression = self.expression_converter.convert_expression_oneline(
            return_node.children[0],
            current_vars,
            custom_classes,
            current_functions
        )
        return f"return {expression}" 

    def convert_function_definition(self, node: Node, current_vars: dict[str, str], 
                                  custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert C++ function definition to Python"""
        if node.node_type != "functionDefinition":
            raise TypeError("Node must be a functionDefinition")

        # Get function name and add to current_functions
        func_name = node.children[1].value
        if func_name not in current_functions:
            current_functions.append(func_name)

        # Convert function signature
        signature = self.convert_function_signature(node, current_vars)
        
        # Convert function body
        body = self.convert_function_body(node.children[-1], current_vars, custom_classes, current_functions)
        
        # Combine signature and body
        result = [signature]
        result.extend(['    ' + line for line in body])
        
        return result

    def convert_function_signature(self, function_node: Node, current_vars: dict[str, str]) -> str:
        """Convert function signature including parameters"""
        # Get function name
        func_name = function_node.children[1].value
        
        # Get return type
        return_type = self.convert_type(function_node.children[0].children[0].value)
        
        # Process parameters
        params = []
        if len(function_node.children) > 2:  # Has parameters
            param_list = function_node.children[2]  # Parameter list node
            if param_list.node_type == "parameterList":
                for param in param_list.children:
                    if param.node_type != "COMMA":  # Skip commas
                        params.append(self.convert_parameter(param, current_vars))
        
        # Build function signature
        param_str = ", ".join(params)
        if return_type == "None":
            return f"def {func_name}({param_str}) -> None:"
        else:
            return f"def {func_name}({param_str}) -> {return_type}:"

    def convert_function_body(self, node: Node, current_vars: dict[str, str], 
                            custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert function body"""
        result = []
        
        if node.node_type == "compoundStatement":
            for child in node.children:
                if child.node_type in ["statement", "declaration"]:
                    # Convert each statement/declaration
                    # Add appropriate conversion logic here
                    result.append("pass")  # Placeholder
        
        if not result:
            result = ["pass"]
            
        return result

    def convert_parameter(self, param_node: Node, current_vars: dict[str, str]) -> tuple[str, str]:
        """Convert a function parameter to Python format"""
        if not param_node or len(param_node.children) < 2:
            raise SyntaxError("Invalid parameter node")
        
        type_node = param_node.children[0]  # Type specifier
        declarator_node = param_node.children[1]  # Declarator
        
        # Get base type
        cpp_type = type_node.children[0].value
        py_type = self.convert_type(cpp_type)
        
        # Get parameter name
        param_name = declarator_node.children[0].value
        
        # Check if it's an array parameter
        is_array = False
        if len(declarator_node.children) > 1 and declarator_node.children[1].node_type == "LBRACK":
            is_array = True
            py_type = f"List[{py_type}]"
        
        # Add to current variables
        current_vars[param_name] = py_type
        
        # Return parameter declaration
        return f"{param_name}: {py_type}"

    def convert_type(self, cpp_type: str) -> str:
        """Convert C++ type to Python type"""
        type_map = {
            'int': 'int',
            'bool': 'bool',
            'char': 'str',
            'float': 'float',
            'double': 'float',
            'string': 'str',
            'void': 'None'
        }
        return type_map.get(cpp_type.lower(), cpp_type)