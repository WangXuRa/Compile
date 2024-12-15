import sys
sys.path.append(sys.path[0] + '/..')

from translation.node import Node
from translation.expression_converter import convert_expression

from antlr4 import InputStream, CommonTokenStream
from CPPLexer import CPPLexer 
from CPPParser import CPPParser 
from CPPParserListener import CPPParserListener 
from CPPParserVisitor import CPPParserVisitor

CPP_TO_PYTHON_TYPES = {
    'int': 'int',
    'double': 'float',
    'bool': 'bool',
    'void': 'None',
    'char': 'str'
}

CPP_TO_PYTHON_SCOPES = {
    'std' : {
        'vector' : 'list',
        'string' : 'str'
    }
}

DEFAULT_LIST_VALUE = {
    'int': '0',
    'float': '0.0',
    'str': '""',
    'bool': 'False',
    'char' : '" "'
}

def convert_type(scope: str|None, type: str) -> str:
    if scope is not None:
        if scope in CPP_TO_PYTHON_SCOPES.keys() and type in CPP_TO_PYTHON_SCOPES[scope].keys():
            return CPP_TO_PYTHON_SCOPES[scope][type]
        else:
            raise SyntaxError(f"type {type} of scope {scope} had not been declared or is not supported!")
    elif type in CPP_TO_PYTHON_TYPES.keys():
        return CPP_TO_PYTHON_TYPES[type]
    
    raise SyntaxError(f"type {type} is not supported!")

def convert_single_decl(typeSpecifier: Node, declarator: Node, custom_types:list[str]) -> str:
    """
    completes declaration conversion, list types are initialized according to DEFAULT_LIST_VALUE
    returns a string containing the python translation of the declaration (without any indentation!)
    """
    if typeSpecifier.node_type != "typeSpecifier":
        raise TypeError("type specifier node must be of type typeSpecifier!")
    if declarator.node_type != "declarator":
        raise TypeError("declarator node must of type declaractor!")

    scope = None
    cpp_type = None
    py_type = None
    # is a basic type
    if len(typeSpecifier.children) == 1:
        type_node = typeSpecifier.children[0]
        # is a custom type
        if type_node.node_type == "ID":
            # this is a valid custom type, no need to convert
            if type_node.value in custom_types:
                py_type = type_node.value
            else:
                raise SyntaxError(f"invalid syntax, variable type {type_node.value} has not been declared or is not supported!")
        else:
            cpp_type = type_node.value
    # is of the form ID SCOPE ID
    elif len(typeSpecifier.children) == 3:
        scope_node = typeSpecifier.children[0]
        type_node = typeSpecifier.children[2]
        scope = scope_node.value
        cpp_type = type_node.value
    else:
        raise SyntaxError("invalid typeSpecifier node!")

    if py_type is None:
        # this may throw errors during conversion
        py_type = convert_type(scope, cpp_type)
    
    var_name = ""
    is_list = False
    list_len = None
    # only ID
    if len(declarator.children) == 1:
        var_name = declarator.children[0].value
    # ID LBRACK NUMBER RBRACK
    elif len(declarator.children) == 4:
        is_list = True
        var_name = declarator.children[0].value
        list_len = declarator.children[2].value

        try:
            a = (int)(list_len)
            assert a>0
        except Exception as e:
            raise SyntaxError(f"invalid length '{list_len}' for array!")
    
    final_expr = var_name + " : "
    # is it is a list, then it needs to be initialized to its desired length
    if is_list:
        # handle special case of a list of char, which is just a string of certain length
        if cpp_type == "char":
            final_expr += "str = "
            final_expr += DEFAULT_LIST_VALUE['char']
        # other normal cases
        else:
            final_expr += "list[" + py_type + "]" + " = "
            final_expr += "[" + DEFAULT_LIST_VALUE[py_type] + "]"
        final_expr += " * " + list_len
    # if it is not a list, we still need to declare AND initialize it
    # because Python does not allow for declaration of a variable without initialization
    else:
        final_expr += py_type + " = None"
    
    return final_expr

def convert_decl_(decl_node:Node, custom_types:list[str]) -> list[str]:
    if decl_node.node_type != "decl_":
        return TypeError("decl_ node must be of type decl_!")
    
    py_declarations = []
    type_specifier_node = decl_node.children[0]
    # decl_ is of the format `typeSpecifier declarator (COMMA declarator)*`
    # so every second child node must be a declarator
    for i in range(1, len(decl_node.children), 2):
        declarator_node = decl_node.children[i]
        py_declarations.append(convert_single_decl(type_specifier_node, declarator_node, custom_types))
    
    return py_declarations

def convert_decl_assign(decl_assign_node:Node, custom_types:list[str]) -> list[str]:
    if decl_assign_node.node_type != "decl_assign":
        raise TypeError("decl_assign node must be of type decl_assign!")
    py_declarations = []
    py_assginments = []
    type_specifier_node = decl_assign_node.children[0]

    # decl_assign node is of the form typeSpecifier declarator ASSIGN assignmentExpression (COMMA declarator ASSIGN assignmentExpression)*
    # so every third child starting from the second one is a declarator
    for i in range(1, len(decl_assign_node.children), 3):
        declarator_node = decl_assign_node.children[i]
        expression_node = decl_assign_node.children[i+2]
        py_declarations.append(convert_single_decl(type_specifier_node, declarator_node, custom_types))
        var_name = declarator_node.children[0].value
        assignment_expr = var_name + " = " + convert_expression(expression_node)
        py_assginments.append(assignment_expr)


if __name__ == "__main__":
    def traverse_tree(node:Node):
        if node.node_type == "decl_":
            print("found a decl_ node, here are the translated results: ")
            for line in convert_decl_(node, []):
                print(line)
        else:
            for child in node.children:
                traverse_tree(child)

    sample_code = """
    int x;
    bool y, z;
    char a[10];
    std::string b[10];
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

        traverse_tree(astTree)