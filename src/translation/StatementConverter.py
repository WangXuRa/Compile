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
            "jumpStatement": self.convert_jumpStatement,
            "forStatement": self.convert_iterationStatement  # Map forStatement to iterationStatement
        }
        
        if node.node_type not in converters:
            # Skip certain token types that don't need conversion
            if node.node_type in ["RPAREN", "LPAREN", "SEMICOLON"]:
                return [""]
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
            # Get the components of the for loop
            init = node.children[2]  # initialization
            cond = node.children[4]  # condition
            incr = node.children[5]  # increment
            body = node.children[7]  # body
            
            # Extract loop variable and range parameters
            var_name = None
            start = None
            end = None
            step = "1"
            
            # Get initialization variable and start value
            if init:
                if init.node_type == "assignmentExpression":
                    # Handle i = left case
                    var_name = init.children[0].children[0].children[0].children[0].value
                    start = self.expressionConverter.convert_expression_oneline(
                        init.children[2], current_vars, custom_classes, current_functions)
                    current_vars[var_name] = "int"
                elif init.node_type == "decl_assign":
                    # Handle int i = 0 case
                    var_name = init.children[1].children[0].value  # get the ID directly
                    start = self.expressionConverter.convert_expression_oneline(
                        init.children[3], current_vars, custom_classes, current_functions)
                    current_vars[var_name] = "int"
                else:
                    raise TypeError(f"Unsupported initialization type: {init.node_type}")
            
            # Get condition for end value
            if cond and hasattr(cond, 'children') and len(cond.children) > 0:
                # Navigate through the nested structure to get to relationalExpression
                cond_expr = cond
                if cond_expr.node_type == "expressionStatement":
                    cond_expr = cond_expr.children[0]  # expression
                if hasattr(cond_expr, 'node_type') and cond_expr.node_type == "expression":
                    cond_expr = cond_expr.children[0]  # assignmentExpression
                if hasattr(cond_expr, 'node_type') and cond_expr.node_type == "assignmentExpression":
                    cond_expr = cond_expr.children[0]  # logicalOrExpression
                if hasattr(cond_expr, 'node_type') and cond_expr.node_type == "logicalOrExpression":
                    cond_expr = cond_expr.children[0]  # logicalAndExpression
                if hasattr(cond_expr, 'node_type') and cond_expr.node_type == "logicalAndExpression":
                    cond_expr = cond_expr.children[0]  # equalityExpression
                if hasattr(cond_expr, 'node_type') and cond_expr.node_type == "equalityExpression":
                    cond_expr = cond_expr.children[0]  # relationalExpression
                
                if hasattr(cond_expr, 'node_type') and cond_expr.node_type == "relationalExpression":
                    # Get the variable being compared
                    left = self.expressionConverter.convert_expression_oneline(
                        cond_expr.children[0], current_vars, custom_classes, current_functions)
                    
                    # Find the operator (LE, LT, GE, GT)
                    for child in cond_expr.children:
                        if child.node_type in ["LE", "LT", "GE", "GT"]:
                            op = child.value
                            break
                    
                    # Get the right value from the shiftExpression after the operator
                    for i, child in enumerate(cond_expr.children):
                        if child.node_type in ["LE", "LT", "GE", "GT"]:
                            right = self.expressionConverter.convert_expression_oneline(
                                cond_expr.children[i + 1], current_vars, custom_classes, current_functions)
                            break
                    
                    # Adjust end value based on operator
                    if op == "<":
                        end = right
                    elif op == "<=":
                        end = f"{right} + 1"  # Include the end value for <=
                    elif op == ">":
                        end = f"{right} - 1"  # Include the end value for >
                        step = "-1"
                    elif op == ">=":
                        end = right  # Include the end value for >=
                        step = "-1"
            
            # Get step from increment
            if incr and hasattr(incr, 'children'):
                if incr.node_type == "expression":
                    incr_expr = incr.children[0]
                else:
                    incr_expr = incr
                
                if hasattr(incr_expr, 'node_type'):
                    if incr_expr.node_type == "unaryExpression":
                        if len(incr_expr.children) >= 2:
                            if incr_expr.children[0].node_type == "INCREMENT":
                                step = "1"
                            elif incr_expr.children[0].node_type == "DECREMENT":
                                step = "-1"
                    elif incr_expr.node_type == "assignmentExpression":
                        if len(incr_expr.children) >= 3:
                            if "+=" in incr_expr.value:
                                step = incr_expr.children[2].value
                            elif "-=" in incr_expr.value:
                                step = f"-{incr_expr.children[2].value}"
            
            # Ensure we have valid values
            if var_name is None:
                var_name = "i"
                current_vars[var_name] = "int"
            if start is None:
                start = "0"
            if end is None:
                end = "size"
            
            # Create the for loop
            if step == "1":
                result.append(f"for {var_name} in range({start}, {end}):")
            else:
                result.append(f"for {var_name} in range({start}, {end}, {step}):")
            
            # Convert body
            body_lines = []
            if body:
                if body.node_type == "compoundStatement" and body.children:
                    for stmt in body.children:
                        stmt_lines = self.convert_statement(stmt, current_vars, custom_classes, current_functions)
                        if stmt_lines:
                            body_lines.extend(stmt_lines)
                else:
                    stmt_lines = self.convert_statement(body, current_vars, custom_classes, current_functions)
                    if stmt_lines:
                        body_lines.extend(stmt_lines)
            
            # Add indentation to body
            if body_lines:
                result.extend("    " + line for line in body_lines if line.strip())
            else:
                result.append("    pass")
        
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
        
    def convert_cin_statement(self, node: Node, current_vars: dict[str, str], custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert C++ cin statements to Python input"""
        input_vars = self._extract_input_variables(node, current_vars, custom_classes, current_functions)
        result = []
        
        for var in input_vars:
            if '[' in var:  # Array element
                result.append(f"{var} = int(input())")
            else:  # Regular variable
                var_type = current_vars.get(var, 'str')
                if var_type in ['int', 'float']:
                    result.append(f"{var} = {var_type}(input())")
                else:
                    result.append(f"{var} = input()")
        
        return result

    def _extract_input_variables(self, node: Node, current_vars: dict[str, str], custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Extract variables being read from input"""
        vars_to_read = []
        
        for child in node.children:
            if child.node_type == "variable":
                var_access = self.expressionConverter.convert_variable_access(
                    child,
                    current_vars,
                    custom_classes,
                    current_functions
                )
                vars_to_read.append(var_access)
        
        return vars_to_read

    def convert_cout_statement(self, node: Node, current_vars: dict[str, str], custom_classes: list[str], current_functions: list[str]) -> list[str]:
        """Convert C++ cout statements to Python print"""
        output_exprs = []
        current = node
        
        while current:
            if hasattr(current, 'children'):
                for child in current.children:
                    if child.node_type in ["STRING_LITERAL", "variable", "expression"]:
                        expr = self.expressionConverter.convert_expression_oneline(
                            child,
                            current_vars,
                            custom_classes,
                            current_functions
                        )
                        output_exprs.append(expr)
            current = current.children[-1] if hasattr(current, 'children') and current.children else None
        
        if output_exprs:
            return [f"print({', '.join(output_exprs)}, end='')"]
        return ["print()"]

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

    
