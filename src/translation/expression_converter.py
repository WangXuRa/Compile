from translation.node import Node

CPP_TO_PYTHON_EXPRESSIONS = {
    '&&': 'and',
    '||': 'or',
    '!': 'not',
    '!=': '!=',
    '==': '=='
}

def convert_assignment_expression(expression_node:Node) -> str:
    if expression_node.node_type != "assignmentExpression":
        return TypeError("assignment expression node must be of type assignmentExpression!")
    final_expr = ""
    # TODO: handle the logic for converting the expression

    return final_expr
