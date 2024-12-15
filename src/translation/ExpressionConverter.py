"""
Features:
* supports in-place incrementation (++/--), ++x and x++ behaves as would in a cpp program
* supports cin operations separated by a space only
    * ex. translation of `std::cin >> a >> b` would still be able to read "10 20" as a=10 and b=20
    * although all variables used in a single std::cin needs to be of the same basic type
"""


import sys
sys.path.append(sys.path[0] + '/..')
from translation.Node import Node

CPP_TO_PYTHON_EXPRESSIONS = {
    '&&': 'and',
    '||': 'or',
    '!': 'not',
    '!=': '!=',
    '==': '==',
    '=': '=',
    '<': '<',
    '>': '>',
    '<=': '<=',
    '>=': '>=',
    '+' : '+',
    '-' : '-',
    '*' : '*',
    '/' : '/'
}

CPP_TO_PYTHON_FUNCTIONS = {
    'default' : {},
    'std' : {
        'strlen' : 'len',
        'cout' : 'print',
        'cin' : 'input'
    }
}

STD_VARS = {
    'cout' : 'print',
    'cin' : 'input',
    'endl' : '\\n'
}

BASIC_TYPES = ['int', 'float', 'str', 'bool']

class ExpressionConverter:
    """
    offers method for converting `expression` node, returns list[str]
    also offers `convert_expression_oneline`, which returns str
    """

    def convert_expression(self, expression_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]) -> str:
        if expression_node.node_type != 'expression':
            raise TypeError("expression node for processing must by of type expression!")
        
        return [self.convert_expression_oneline(expression_node, current_vars, custom_classes, current_functions)]
    
    def convert_function(self, scope, func_name):
        if scope in CPP_TO_PYTHON_FUNCTIONS.keys():
            if func_name in CPP_TO_PYTHON_FUNCTIONS[scope].keys():
                return CPP_TO_PYTHON_FUNCTIONS[scope][func_name]
        
        raise SyntaxError(f"cpp function {scope}::{func_name} not supported!")

    def convert_variable_(self, variable_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]):
        """
        returns return the converted python variable
        """
        if variable_node.node_type != "variable_":
            raise TypeError("variable_ node must by of a type variable_!")

        # ID
        if len(variable_node.children) == 1:
            return variable_node.children[0].value
        # ID LBRACK expression RBRACK
        elif len(variable_node.children) == 4:
            return variable_node.children[0].value + '[' \
                + self.convert_expression_oneline(variable_node.children[2], current_vars, custom_classes, current_functions) + ']'
        # ID DOT variable_
        elif len(variable_node.children) == 3:
            right = self.convert_variable_(variable_node.children[2], current_vars, custom_classes, current_functions)
            return variable_node.children[0].value + '.' + right
        else:
            raise SyntaxError("invalid variable_ node!")

    def convert_variable(self, variable_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]):
        """
        converts a variable node, which could, under the current parser rules, be `std::cin` and `std::cout`, which are translated into input and print
        """
        if variable_node.node_type != "variable":
            raise TypeError("variable node must by of a type variable!")

        py_var = ""
        # ID SCOPE variable_
        if len(variable_node.children) == 3:
            scope = variable_node.children[0].value
            if scope != 'std':
                raise SyntaxError(f"scope {scope} not supported by this translator!")
            if len(variable_node.children[2].children) != 1:
                raise SyntaxError(f"indexing or referencing of attributes for variables in std scope not supported by this translator!")
            cpp_var = variable_node.children[2].children[0].value
            if cpp_var not in STD_VARS.keys():
                raise SyntaxError(f"{scope}::{cpp_var} not supported by this translator!")
            return STD_VARS[cpp_var]
        # variable_
        elif len(variable_node.children) == 1:
            # check if the variable is contained in variable list
            variable_ = variable_node.children[0]
            root_var = variable_.children[0].value
            if root_var in current_vars:
                return self.convert_variable_(variable_, current_vars, custom_classes, current_functions)
            else:
                raise SyntaxError(f"variable {root_var} referenced before declaration!")
        else:
            raise SyntaxError("invalid variable node!")

    def convert_function_(self, function_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]) -> str:
        if function_node.node_type != ("function_"):
            raise TypeError("function_ node must by of a type function_!")

        # ID
        if len(function_node.children) == 1:
            func = function_node.children[0].value
            if func in current_functions:
                return func
            elif func in CPP_TO_PYTHON_FUNCTIONS['default'].keys():
                return CPP_TO_PYTHON_FUNCTIONS['default'][func]
            else:
                return TypeError(f"function {func} referenced before declaration")
        # ID DOT function
        elif len(function_node.children) == 3:
            return function_node.children[0].value + '.' + self.convert_function_(function_node.children[2], current_vars, custom_classes, current_functions)
        else:
            raise SyntaxError("invalid function_ node!")
        

    def convert_function(self, function_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]) -> str:
        if function_node.node_type != ("function"):
            raise TypeError("function node must by of a type function!")
        
        py_func = ""
        # ID SCOPE function_
        if len(function_node.children) == 3:
            scope = function_node.children[0].value
            if scope != 'std':
                raise SyntaxError(f"scope {scope} not supported by this translator!")
            if len(function_node.children[2].children) != 1:
                raise SyntaxError(f"indexing or referencing of attributes for variables in std scope not supported by this translator!")
            cpp_function = function_node.children[2].children[0].value
            if cpp_function in CPP_TO_PYTHON_FUNCTIONS['std'].keys():
                return CPP_TO_PYTHON_FUNCTIONS['std'][cpp_function]
            else:
                raise SyntaxError(f"{scope}::{cpp_function} not supported by this translator!")
        # function_
        elif len(function_node.children) == 1:
            return self.convert_function_(function_node, current_vars, custom_classes, current_functions)

    def is_input_op(self, shift_operator_node:Node):
        if shift_operator_node.children[0].value == '>':
            return True
        else:
            return False

    def process_input(self, shift_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]):
        """
        shift_node: additiveExpression (shiftOperator additiveExpression)*
        the additiveExpression MUST evaluate to 'input'
        all variables following std::cin MUST be of the same type, and must be contained in `current_vars`
        """
        if not shift_node.node_type == 'shiftExpression':
            raise TypeError("shiftExpression node for processing must by of a type that ends in shiftExpression!")
        
        var_type = None
        py_statement = ""
        for i in range(2, len(shift_node.children), 2):
            # check that the shiftOperator is the correct operator
            if not self.s_input_op(shift_node.children[i-1]):
                raise SyntaxError("cannot use << with std::cin!")
            var_name = self.convert_expression_oneline(shift_node.children[i])
            if not (var_name in current_vars.keys()):
                raise SyntaxError(f"variable {var_name} used in input statement referenced before declaration!")
            curr_type = current_vars[var_name]
            if curr_type not in BASIC_TYPES:
                raise SyntaxError(f"variables used in std::cin should be of a basic type (not {curr_type})!")
            if (var_type is not None) and (var_type != curr_type):
                raise SyntaxError("all variables used in a single std::cin statement must be of the same type")
            var_type = curr_type
            py_statement += var_name + ", "
        
        py_statement = py_statement[:-2] # get rid of the last `, `
        py_statement += f" = map({var_type}, input().split())"
        return py_statement


    def convert_expression_oneline(self, expression_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]) -> str:
        """
        converts any `expression` type node or node type ending in `Expression` into their python string
        returns a string
        """
        if not (expression_node.node_type.endswith("Expression") or expression_node.node_type == 'expression'):
            raise TypeError("expression node for processing must by of a type that ends in Expression!")
        
        # special case of primaryExpression (which can have 1~6 children)
        if expression_node.node_type == "primaryExpression":
            first_child = expression_node.children[0]
            # CHAR_LITERAL, STRING_LITERAL, and BOOL_LITERAL
            if first_child.value is not None and first_child.node_type!='LPAREN':
                return first_child.value
            # variable
            if first_child.node_type == 'variable':
                return self.convert_variable(first_child, current_vars, custom_classes, current_functions)
            # number
            if first_child.node_type == 'number':
                # (MINUS | PLUS)? NUMBER
                number = ""
                for child in first_child.children:
                    number += child.value
                return number
            # functionCall
            if first_child.node_type == 'functionCall':
                # function LPAREN expression? RPAREN
                func = self.convert_function(first_child.children[0], current_vars, custom_classes, current_functions)
                if first_child.children[2].node_type == 'expression':
                    return func + '(' + self.convert_expression_oneline(first_child.children[0]) + ')'
                else:
                    return func + '()'
                
            # LPAREN expression RPAREN
            if first_child.node_type == 'LPAREN':
                return '(' + self.convert_expression_oneline(expression_node.children[1]) + ')'

        # if it only has one child, just process that
        if len(expression_node.children) == 1:
            return self.convert_expression_oneline(expression_node.children[0], current_vars, custom_classes, current_functions)
        
        #--- three special cases that don't fit into the common case ..Expression OPERATOR ..Expression ---#
        # additiveExpression (shiftOperator additiveExpression)*
        if expression_node.node_type == "shiftExpression":
            # get the left side first to see if it is print or input statement
            left = self.convert_expression_oneline(first_child, current_vars, custom_classes, current_functions)

            if left == 'print':
                py_statement = "print("
                for i in range(2, len(expression_node.children), 2):
                    # check that the shiftOperator is the correct operator
                    if self.is_input_op(expression_node.children[i-1]):
                        raise SyntaxError("cannot use >> with std::cout!")

                    print_elem = self.convert_expression_oneline(expression_node.children[i], current_vars, custom_classes, current_functions)
                    py_statement += print_elem + ", "
                py_statement += "sep='', end='')" # change seperator and endto empty string to mimic behavior of std::cout
                return py_statement
            
            elif left == 'input':
                return self.rocess_input(expression_node)
            
            # not input or print, so just regular bitshift
            else:
                py_statement = left
                for i in range(2, len(expression_node.children), 2):
                    # check that the shiftOperator is the correct operator
                    if self.is_input_op(expression_node.children[i-1]):
                        py_statement += " >> "
                    else:
                        py_statement += " << "

                    py_statement += self.convert_expression_oneline(expression_node.children[i], current_vars, custom_classes, current_functions)
                return py_statement
                
        if expression_node.node_type == "unaryExpression":
            if expression_node.children[0].node_type == 'referenceOp':
                raise SyntaxError("pointer-related operations not supported in expressions!")
            
            right = self.convert_expression_oneline(expression_node.children[1], current_vars, custom_classes, current_functions)
            if expression_node.children[0].node_type == 'NOT':
                return ' not ' + right
            
            py_statement = '(' + right + ':=' + right
            # ++/-- unaryExpression
            if expression_node.children[0].node_type == 'INCREMENT':
                py_statement += '+1)'
                return py_statement
            elif expression_node.children[0].node_type == 'DECREMENT':
                py_statement += '-1)'
                return py_statement
            else:
                raise SyntaxError("invalid unaryExpression node!")
            
        if expression_node.node_type == "postfixExpression":
            left = self.convert_expression_oneline(expression_node.children[0], current_vars, custom_classes, current_functions)

            py_statement = '((' + left + ':=' + left
            # unaryExpression ++/--
            if expression_node.children[1].node_type == 'INCREMENT':
                py_statement += '+1)-1)'
                return py_statement
            elif expression_node.children[1].node_type == 'DECREMENT':
                py_statement += '-1)+1)'
                return py_statement
            else:
                raise SyntaxError("invalid unaryExpression node!")
            
        # common case
        if len(expression_node.children) == 3:
            left = self.convert_expression_oneline(expression_node.children[0], current_vars, custom_classes, current_functions)
            right = self.convert_expression_oneline(expression_node.children[2], current_vars, custom_classes, current_functions)
            cpp_op = expression_node.children[1].value
            if cpp_op in CPP_TO_PYTHON_EXPRESSIONS.keys():
                py_op = CPP_TO_PYTHON_EXPRESSIONS[cpp_op]
                return left + " " + py_op + " " + right
            else:
                raise SyntaxError(f"c++ operator {cpp_op} not supported by this translator!")

# testing/demonstration code
if __name__ == "__main__":
    from antlr4 import InputStream, CommonTokenStream
    from CPPLexer import CPPLexer 
    from CPPParser import CPPParser 
    from CPPParserListener import CPPParserListener
    from CPPParserVisitor import CPPParserVisitor
    
    from translation.DeclarationConverter import DeclarationConverter

    dcl_converter = DeclarationConverter()
    exp_converter = ExpressionConverter()
    def traverse_tree(node:Node, current_vars, custom_classes, current_functions):
        if node.node_type == "declaration":
            # print("found a declaration node, here are the translated results: ")
            for line in dcl_converter.convert_declaration(node, current_vars, custom_classes, current_functions):
                print(line)
        elif node.node_type == "expression":
            print("found an expression node, here are the translated results: ")
            for line in exp_converter.convert_expression(node, current_vars, custom_classes, current_functions):
                print(line)
        else:
            for child in node.children:
                traverse_tree(child, current_vars, custom_classes, current_functions)

    sample_code = """
    int x;
    bool y, z;
    char a[10];
    std::string b[10];
    int a = 3 * 4;
    x = a++ - 10;
    std::string c;
    c = b[--x] + "hello";
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
        print("syntax errors")

    else:
        visitor = CPPParserVisitor(parser)
        astTree = visitor.visit(tree)

        with open("ast_output.xml", "w", encoding="utf-8") as file:
            file.write("<AST>\n")
            file.write(str(astTree)) 
            file.write("\n</AST>")
        
        print("AST has been saved to 'ast_output.xml'")

        current_vars = {}
        custom_classes = []
        current_functions = []
        traverse_tree(astTree, current_vars, custom_classes, current_functions)
        print("current variables: \n", current_vars)
        print("custom classes: \n", custom_classes)
        print("current functions: \n", current_functions)
