from antlr4 import TerminalNode
from CPPParserVisitor import CPPParserVisitor
from CPPParser import CPPParser
from typing import List, Dict, Any, Optional
from translation.Node import Node
from translation.ExpressionConverter import ExpressionConverter
from translation.DeclarationConverter import DeclarationConverter
from translation.StatementConverter import StatementConverter
from translation.ClassConverter import ClassConverter
from translation.FunctionConverter import FunctionConverter

class CPPToPythonVisitor(CPPParserVisitor):
    def __init__(self, lexer):
        self.lexer = lexer
        self.output_lines = []
        self.symbol_table = {}
        self.custom_classes = []
        self.current_functions = []
        self.expression_converter = None
        self.declaration_converter = None
        self.statement_converter = None
        self.class_converter = None
        self.function_converter = None
        self.in_class = False
        self.current_class = None
        self.in_function = False
        self.current_function = None
    
    def visitChildren(self, ctx):
        """Override visitChildren to create Node objects"""
        rule_name = CPPParser.ruleNames[ctx.getRuleContext().getRuleIndex()]
        node = Node(rule_name)
        
        if ctx.children:
            for child in ctx.children:
                # For terminal nodes (tokens)
                if isinstance(child, TerminalNode):
                    token_type = self.lexer.symbolicNames[child.symbol.type]
                    child_node = Node(token_type, child.getText())
                    node.add_child(child_node)
                else:
                    # For parser rule nodes
                    result = self.visit(child)
                    if result is not None:
                        node.add_child(result)
        return node

    def visitTerminal(self, node):
        """Handle terminal nodes"""
        token_type = self.lexer.symbolicNames[node.symbol.type]
        return Node(token_type, node.getText())

    def visitProgram(self, ctx):
        """Visit the root program node"""
        node = Node("program")
        if ctx.children:
            for child in ctx.children:
                result = self.visit(child)
                if result:
                    node.add_child(result)
                    
                    if result.node_type == "declaration":
                        if self.declaration_converter:
                            declarations = self.declaration_converter.convert_declaration(
                                result,
                                self.symbol_table,
                                self.custom_classes,
                                self.current_functions
                            )
                            if declarations:
                                self.output_lines.extend(declarations)
                    
                    elif result.node_type == "classDefinition":
                        self.in_class = True
                        if self.class_converter:
                            # Get class name from the node
                            self.current_class = result.children[1].value
                            
                            # Process class body to add member variables to symbol table
                            class_body = result.children[3]  # classBody node
                            for member in class_body.children:
                                if member.node_type == "declaration":
                                    decl_node = member.children[0]  # Get decl_ node
                                    if decl_node.node_type == "decl_":
                                        type_node = decl_node.children[0]  # typeSpecifier
                                        declarator_node = decl_node.children[1]  # declarator
                                        var_name = declarator_node.children[0].value
                                        var_type = type_node.children[0].value
                                        # Add both forms to symbol table
                                        self.symbol_table[var_name] = var_type  # Regular form
                                        self.symbol_table[f"self.{var_name}"] = var_type  # Class member form
                            
                            # Convert class definition
                            class_lines = self.class_converter.convert_class(
                                result,
                                self.symbol_table,
                                self.custom_classes,
                                self.current_functions
                            )
                            if class_lines:
                                self.output_lines.extend(class_lines)
                            
                            self.in_class = False
                            self.current_class = None
                    
                    elif result.node_type == "statement":
                        # Let visitStatement handle the statement conversion
                        # The conversion is already done in visitStatement, 
                        # so we don't need to do anything here
                        pass
                    
                    elif result.node_type == "expression":
                        if self.expression_converter:
                            expressions = self.expression_converter.convert_expression(
                                result,
                                self.symbol_table,
                                self.custom_classes,
                                self.current_functions
                            )
                            if expressions:
                                self.output_lines.extend(expressions)
                    
                    elif result.node_type == "functionDefinition":
                        if self.function_converter:
                            function_lines = self.function_converter.convert_function(
                                result,
                                self.symbol_table,
                                self.custom_classes,
                                self.current_functions
                            )
                            if function_lines:
                                self.output_lines.extend(function_lines)
        
        return node

    def visitDeclaration(self, ctx):
        """Visit a declaration node"""
        node = Node("declaration")
        # Process declaration children
        for child in ctx.children:
            result = self.visit(child)
            if result:
                node.add_child(result)
        return node

    def visitExpression(self, ctx):
        """Visit an expression node"""
        node = Node("expression")
        # Process expression children
        for child in ctx.children:
            result = self.visit(child)
            if result:
                node.add_child(result)
        return node

    def visit(self, tree):
        """Override visit to ensure proper node creation"""
        result = super().visit(tree)
        if isinstance(result, str):
            # Create a node for terminal values
            return Node("terminal", value=result)
        return result

    def convert_type(self, cpp_type: str) -> str:
        """Convert C++ type to Python type"""
        type_map = {
            'int': 'int',
            'bool': 'bool',
            'char': 'str',
            'float': 'float',
            'double': 'float',
            'string': 'str'
        }
        return type_map.get(cpp_type.lower(), 'None')

    def extract_value(self, assign_expr_node) -> str:
        """Extract value from assignment expression"""
        try:
            if assign_expr_node.children:
                # Handle basic numeric values
                if assign_expr_node.children[0].node_type == "number":
                    return assign_expr_node.children[0].value
                # Handle expressions (like 3 * 4)
                elif assign_expr_node.children[0].node_type == "multiplicativeExpression":
                    left = self.extract_value(assign_expr_node.children[0])
                    op = assign_expr_node.children[1].value
                    right = self.extract_value(assign_expr_node.children[2])
                    return f"{left} {op} {right}"
        except Exception as e:
            print(f"Error extracting value: {e}")
        return "None"

    def is_cout_statement(self, node) -> bool:
        """Check if node is a cout statement"""
        try:
            return "cout" in str(node)
        except:
            return False

    def is_cin_statement(self, node) -> bool:
        """Check if node is a cin statement"""
        try:
            return "cin" in str(node)
        except:
            return False

    def convert_cout(self, node) -> str:
        """Convert cout statement to print"""
        try:
            # Extract all printable items
            items = []
            current = node
            while current:
                if hasattr(current, 'children'):
                    for child in current.children:
                        if child.node_type == "STRING_LITERAL":
                            items.append(child.value)
                        elif child.node_type == "variable_":
                            items.append(child.children[0].value)
                current = current.children[-1] if hasattr(current, 'children') and current.children else None
            return f"print({', '.join(items)})"
        except Exception as e:
            print(f"Error converting cout: {e}")
            return "print()"

    def convert_cin(self, node) -> str:
        """Convert cin statement to input"""
        try:
            # Extract variables being read
            vars_to_read = []
            current = node
            while current:
                if hasattr(current, 'children'):
                    for child in current.children:
                        if child.node_type == "variable_":
                            vars_to_read.append(child.children[0].value)
                current = current.children[-1] if hasattr(current, 'children') and current.children else None
            if vars_to_read:
                return f"{', '.join(vars_to_read)} = input().split()"
            return "input()"
        except Exception as e:
            print(f"Error converting cin: {e}")
            return "input()"

    def get_output(self) -> str:
        """Get the generated Python code"""
        return '\n'.join(self.output_lines)

    def get_includes(self, tree) -> List[str]:
        """Extract include statements"""
        includes = []
        # Implementation to extract includes from the AST
        return includes

    def get_namespaces(self, tree) -> List[str]:
        """Extract namespace declarations"""
        namespaces = []
        # Implementation to extract namespaces from the AST
        return namespaces

    def add_line(self, line: str):
        """Add a line of code with proper indentation"""
        self.output_lines.append(f"{self.indent()}{line}")

    def indent(self) -> str:
        return "    " * self.indent_level

    def visitStatement(self, ctx):
        """Visit a statement node"""
        node = Node("statement")
        
        if self.statement_converter:
            # Determine statement type
            if ctx.getText().startswith("cin"):
                statements = self.statement_converter.convert_cin_statement(
                    ctx,
                    self.symbol_table,
                    self.custom_classes,
                    self.current_functions
                )
            elif ctx.getText().startswith("cout"):
                statements = self.statement_converter.convert_cout_statement(
                    ctx,
                    self.symbol_table,
                    self.custom_classes,
                    self.current_functions
                )
            else:
                statements = self.statement_converter.convert_statement(
                    ctx,
                    self.symbol_table,
                    self.custom_classes,
                    self.current_functions
                )
                
            if statements:
                self.output_lines.extend(statements)
        
        return node

    # ... (keep other utility methods)