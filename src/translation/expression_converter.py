from translation.node import Node

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

def convert_function(scope, func_name):
    if scope in CPP_TO_PYTHON_FUNCTIONS.keys():
        if func_name in CPP_TO_PYTHON_FUNCTIONS[scope].keys():
            return CPP_TO_PYTHON_FUNCTIONS[scope][func_name]
    
    raise SyntaxError(f"cpp function {scope}::{func_name} not supported!")

def convert_variable_(variable_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]):
    """
    returns return the converted python variable
    """
    if not variable_node.node_type != "variable_":
        raise TypeError("variable_ node must by of a type variable_!")

    # ID
    if len(variable_node.children) == 1:
        return variable_node.children[0].value
    # ID LBRACK expression RBRACK
    elif len(variable_node.children) == 4:
        return variable_node.children[0].value + '[' \
            + convert_expression(variable_node.children[2], current_vars, custom_classes, current_functions) + ']'
    # ID DOT variable_
    elif len(variable_node.children) == 3:
        right = convert_variable_(variable_node.children[2], current_vars, custom_classes, current_functions)
        return variable_node.children[0].value + '.' + right
    else:
        raise SyntaxError("invalid variable_ node!")

def convert_variable(variable_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]):
    """
    converts a variable node, which could, under the current parser rules, be `std::cin` and `std::cout`, which are translated into input and print
    """
    if not variable_node.node_type != "variable":
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
            return convert_variable_(variable_, current_vars, custom_classes, current_functions)
        else:
            raise SyntaxError(f"variable {root_var} referenced before declaration!")
    else:
        raise SyntaxError("invalid variable node!")

def convert_function_(function_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]) -> str:
    if not function_node.node_type.endswith("function_"):
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
        return function_node.children[0].value + '.' + convert_function_(function_node.children[2], current_vars, custom_classes, current_functions)
    else:
        raise SyntaxError("invalid function_ node!")
    

def convert_function(function_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]) -> str:
    if not function_node.node_type.endswith("function"):
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
        return convert_function_(function_node, current_vars, custom_classes, current_functions)

def is_input_op(shift_operator_node:Node):
    if shift_operator_node.children[0].value == '>':
        return True
    else:
        return False

def process_input(shift_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]):
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
        if not is_input_op(shift_node.children[i-1]):
            raise SyntaxError("cannot use << with std::cin!")
        var_name = convert_expression(shift_node.children[i])
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


def convert_expression(expression_node:Node, current_vars:dict[str, str], custom_classes:list[str], current_functions : list[str]) -> str:
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
            return convert_variable(first_child, current_vars, custom_classes, current_functions)
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
            func = convert_function(first_child.children[0],  current_vars, custom_classes, current_functions)
            if first_child.children[2].node_type == 'expression':
                return func + '(' + convert_expression(first_child.children[0]) + ')'
            else:
                return func + '()'
            
        # LPAREN expression RPAREN
        if first_child.node_type == 'LPAREN':
            return '(' + convert_expression(expression_node.children[1]) + ')'

    # if it only has one child, just process that
    if len(expression_node.children) == 1:
        return convert_expression(expression_node.children[0])
    
    #--- three special cases that don't fit into the common case ..Expression OPERATOR ..Expression ---#
    # additiveExpression (shiftOperator additiveExpression)*
    if expression_node.node_type == "shiftExpression":
        # get the left side first to see if it is print or input statement
        left = convert_expression(first_child, current_vars, custom_classes, current_functions)

        if left == 'print':
            py_statement = "print("
            for i in range(2, len(expression_node.children), 2):
                # check that the shiftOperator is the correct operator
                if is_input_op(expression_node.children[i-1]):
                    raise SyntaxError("cannot use >> with std::cout!")

                print_elem = convert_expression(expression_node.children[i], current_vars, custom_classes, current_functions)
                py_statement += print_elem + ", "
            py_statement += "sep='', end='')" # change seperator and endto empty string to mimic behavior of std::cout
            return py_statement
        
        elif left == 'input':
            return process_input(expression_node)
        
        # not input or print, so just regular bitshift
        else:
            py_statement = left
            for i in range(2, len(expression_node.children), 2):
                # check that the shiftOperator is the correct operator
                if is_input_op(expression_node.children[i-1]):
                    py_statement += " >> "
                else:
                    py_statement += " << "

                py_statement += convert_expression(expression_node.children[i], current_vars, custom_classes, current_functions)
            return py_statement
            
    if expression_node.node_type == "unaryExpression":
        if expression_node.children[0].node_type == 'referenceOp':
            raise SyntaxError("pointer-related operations not supported in expressions!")
        
        right = convert_expression(expression_node.children[1])
        if expression_node.children[0].node_type == 'NOT':
            return ' not ' + right
        
        py_statement = '(' + right + ' := ' + right
        # ++/-- unaryExpression
        if expression_node.children[0].node_type == 'INCREMENT':
            py_statement += ' + 1)'
            return py_statement
        elif expression_node.children[0].node_type == 'DECREMENT':
            py_statement += ' - 1)'
            return py_statement
        else:
            raise SyntaxError("invalid unaryExpression node!")
        
    if expression_node.node_type == "postfixExpression":
        py_statement = '( (' + right + ' := ' + right
        # unaryExpression ++/--
        if expression_node.children[0].node_type == 'INCREMENT':
            py_statement += ' + 1) - 1)'
            return py_statement
        elif expression_node.children[0].node_type == 'DECREMENT':
            py_statement += ' - 1) + 1)'
            return py_statement
        else:
            raise SyntaxError("invalid unaryExpression node!")
        
    # common case
    if len(expression_node.children) == 3:
        left = convert_expression(expression_node.children[0], current_vars, custom_classes, current_functions)
        right = convert_expression(expression_node.children[2], current_vars, custom_classes, current_functions)
        cpp_op = expression_node.children[1].value
        if cpp_op in CPP_TO_PYTHON_EXPRESSIONS.keys():
            py_op = CPP_TO_PYTHON_EXPRESSIONS[cpp_op]
            return left + " " + py_op + " " + right
        else:
            raise SyntaxError(f"c++ operator {cpp_op} not supported by this translator!")
