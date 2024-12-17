import sys
sys.path.append(sys.path[0] + '/..')

from translation.Node import Node
from translation.ExpressionConverter import ExpressionConverter
from translation.DeclarationConverter import DeclarationConverter

class StatementConverter:
    """
    Converts C++ statements to Python statements
    Handles control structures (if, while, for) and other statement types
    """
    def __init__(self):
        self.expressionConverter = ExpressionConverter()
        self.declarationConverter = DeclarationConverter()
        
    def convert_statement(self, node: Node, current_vars: dict[str, str], 
                         custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert statement node to Python code"""
        # If it's a statement wrapper node, get the actual statement
        if node.node_type == "statement":
            node = node.children[0]
        
        converters = {
            "expressionStatement": self.convert_expressionStatement,
            "compoundStatement": self.convert_compoundStatement,
            "selectionStatement": self.convert_selectionStatement,
            "iterationStatement": self.convert_iterationStatement,
            "jumpStatement": self.convert_jumpStatement
        }
        
        if node.node_type not in converters:
            raise TypeError(f"Unsupported statement type: {node.node_type}")
        
        return converters[node.node_type](node, current_vars, custom_classes, current_functions)

    def convert_expressionStatement(self, node: Node, current_vars: dict[str, str], 
                                  custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert expression statement to Python"""
        if not node.children:  # Empty statement
            return [""]
        
        expr = self.expressionConverter.convert_expression_oneline(
            node.children[0], current_vars, custom_classes, current_functions)
        return [expr]

    def convert_compoundStatement(self, node: Node, current_vars: dict[str, str], 
                                custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """
        Convert compound statement (block) to Python
        Creates a new scope for variables declared within the block
        """
        result = []
        # Create a copy of current_vars for this scope
        scope_vars = current_vars.copy()
        
        for child in node.children:
            if child.node_type == "declaration":
                result.extend(self.declarationConverter.convert_declaration(
                    child, scope_vars, custom_classes, current_functions))
            elif child.node_type == "statement":
                result.extend(self.convert_statement(
                    child, scope_vars, custom_classes, current_functions))
        
        # Update parent scope with any variables that were modified
        # but existed before this scope
        for var, type_ in scope_vars.items():
            if var in current_vars:
                current_vars[var] = type_
            
        return result

    def convert_selectionStatement(self, node: Node, current_vars: dict[str, str], 
                                 custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """
        Convert if statement to Python
        Variables declared in if/else blocks are only visible within their respective blocks
        """
        result = []
        condition = self.expressionConverter.convert_expression_oneline(
            node.children[2], current_vars, custom_classes, current_functions)
        
        result.append(f"if {condition}:")
        
        # Create new scope for if-block
        if_vars = current_vars.copy()
        if_body = self.convert_statement(
            node.children[4], if_vars, custom_classes, current_functions)
        result.extend(["    " + line for line in if_body])
        
        if len(node.children) > 5:
            result.append("else:")
            # Create new scope for else-block
            else_vars = current_vars.copy()
            else_body = self.convert_statement(
                node.children[6], else_vars, custom_classes, current_functions)
            result.extend(["    " + line for line in else_body])
        
        return result

    def convert_iterationStatement(self, node: Node, current_vars: dict[str, str], 
                                 custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert while and for loops to Python"""
        result = []
        
        if node.children[0].node_type == "WHILE":
            condition = self.expressionConverter.convert_expression_oneline(
                node.children[2], current_vars, custom_classes, current_functions)
            result.append(f"while {condition}:")
            
            loop_vars = current_vars.copy()
            body = self.convert_statement(
                node.children[4], loop_vars, custom_classes, current_functions)
            result.extend(["    " + line for line in body])
            
        elif node.children[0].node_type == "FOR":
            loop_vars = current_vars.copy()
            
            # Extract the three parts of the for loop
            init_part = node.children[2]
            condition_part = node.children[4].children[0] if node.children[4].children else None
            increment_part = node.children[5] if len(node.children) > 5 else None
            body_part = node.children[7] if len(node.children) > 7 else None

            def find_relational_expression(node):
                """Traverse down the AST to find the relational expression"""
                if not node:
                    return None
                if node.node_type == "relationalExpression":
                    return node
                if hasattr(node, 'children'):
                    for child in node.children:
                        result = find_relational_expression(child)
                        if result:
                            return result
                return None

            def find_postfix_increment(node):
                """Traverse down the AST to find postfix increment"""
                if not node:
                    return None
                if (node.node_type == "postfixExpression" and 
                    len(node.children) == 2 and 
                    node.children[1].node_type == "INCREMENT"):
                    return node
                if hasattr(node, 'children'):
                    for child in node.children:
                        result = find_postfix_increment(child)
                        if result:
                            return result
                return None

            def get_variable_name(node):
                """Helper function to extract variable name from any node type"""
                if node.node_type == "variable_":
                    return node.children[0].value
                if node.node_type == "ID":
                    return node.value
                if hasattr(node, 'children') and node.children:
                    return get_variable_name(node.children[0])
                return None

            if init_part and init_part.node_type == "decl_assign":
                try:
                    # Get initialization variable and value
                    var_name = init_part.children[1].children[0].value
                    # Add the variable to current_vars with its type
                    var_type = init_part.children[0].children[0].value
                    current_vars[var_name] = var_type
                    loop_vars[var_name] = var_type
                    
                    start_val = self.expressionConverter.convert_expression_oneline(
                        init_part.children[3], loop_vars, custom_classes, current_functions)
                    
                    # Find the relational expression in the condition part
                    rel_expr = find_relational_expression(condition_part)
                    if rel_expr:
                        left = rel_expr.children[0]
                        operator = rel_expr.children[1].value
                        right = rel_expr.children[2]
                        
                        left_var_name = get_variable_name(left)
                        
                        if (left_var_name == var_name and operator in ["<", "<="]):
                            end_val = self.expressionConverter.convert_expression_oneline(
                                right, loop_vars, custom_classes, current_functions)
                            
                            if increment_part:
                                postfix_expr = find_postfix_increment(increment_part)
                                if postfix_expr:
                                    inc_var = get_variable_name(postfix_expr.children[0])
                                    
                                    if inc_var == var_name:
                                        if operator == "<":
                                            result.append(f"for {var_name} in range({start_val}, {end_val}):")
                                        else:  # operator is <=
                                            result.append(f"for {var_name} in range({start_val}, {end_val} + 1):")
                                        
                                        if body_part:
                                            body = self.convert_statement(
                                                body_part, loop_vars, custom_classes, current_functions)
                                            result.extend(["    " + line for line in body])
                                        return result
            
                except (AttributeError, IndexError):
                    pass  # Fall back to while loop conversion
            
            # Fall back to while loop conversion
            result = []
            
            if init_part:
                if init_part.node_type == "decl_assign":
                    result.extend(self.declarationConverter.convert_decl_assign(
                        init_part, loop_vars, custom_classes, current_functions))
                else:
                    init_code = self.expressionConverter.convert_expression_oneline(
                        init_part, loop_vars, custom_classes, current_functions)
                    result.append(init_code)
            
            condition = "True"
            if condition_part:
                condition = self.expressionConverter.convert_expression_oneline(
                    condition_part, loop_vars, custom_classes, current_functions)
            
            result.append(f"while {condition}:")
            
            if body_part:
                body = self.convert_statement(body_part, loop_vars, custom_classes, current_functions)
                if increment_part:
                    inc = self.expressionConverter.convert_expression_oneline(
                        increment_part, loop_vars, custom_classes, current_functions)
                    body.append(inc)
                result.extend(["    " + line for line in body])
        
        return result

    def convert_jumpStatement(self, node: Node, current_vars: dict[str, str], 
                            custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert return and continue statements to Python"""
        if node.children[0].node_type == "RETURN":
            if len(node.children) > 1:
                expr = self.expressionConverter.convert_expression_oneline(
                    node.children[1], current_vars, custom_classes, current_functions)
                return [f"return {expr}"]
            return ["return"]
        
        elif node.children[0].node_type == "CONTINUE":
            return ["continue"]
        
        raise TypeError(f"Unsupported jump statement type: {node.children[0].node_type}")
        
# Testing code
if __name__ == "__main__":
    from antlr4 import InputStream, CommonTokenStream
    from CPPLexer import CPPLexer
    from CPPParser import CPPParser
    from CPPParserVisitor import CPPParserVisitor

    statement_converter = StatementConverter()
    
    def traverse_tree(node: Node, current_vars, custom_classes, current_functions):
        """Traverse AST and convert all statements"""
        if node.node_type == "program":
            result = []
            for child in node.children:
                if child.node_type == "statement":
                    print("\nFound a statement node, here are the translated results: ")
                    translated = statement_converter.convert_statement(
                        child, current_vars, custom_classes, current_functions)
                    for line in translated:
                        print(line)
                    result.extend(translated)
                    print("\nCurrent variables after statement: ", current_vars)
        else:
            for child in node.children:
                traverse_tree(child, current_vars, custom_classes, current_functions)

    # Test code with different types of statements
    sample_code = """
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
    """
        
    input_stream = InputStream(sample_code)
    lexer = CPPLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CPPParser(token_stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found!")
    else:
        print("Parsing successful!")
        visitor = CPPParserVisitor(parser)
        ast_tree = visitor.visit(tree)

        # Initialize context
        current_vars = {
            'x': 'int',
            'y': 'int'
        }
        custom_classes = []
        current_functions = []

        print("\n# Statement Conversion Output #")
        print("Initial variables:", current_vars)
        traverse_tree(ast_tree, current_vars, custom_classes, current_functions)
        print("\nFinal variables:", current_vars)
        print("\nCustom classes:", custom_classes)
        print("Current functions:", current_functions)

        # Save AST for debugging
        with open("statement_ast_output.xml", "w", encoding="utf-8") as file:
            file.write("<AST>\n")
            file.write(str(ast_tree)) 
            file.write("\n</AST>")
        print("\nAST has been saved to 'statement_ast_output.xml'")

        print("\nAST Structure:")
        def print_node(node, indent=0):
            if not node:
                return
            print("  " * indent + f"- {node.node_type}")
            if hasattr(node, 'value'):
                print("  " * indent + f"  value: {node.value}")
            if hasattr(node, 'children'):
                for child in node.children:
                    print_node(child, indent + 1)

    
