# Generated from CPPParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CPPParser import CPPParser
else:
    from CPPParser import CPPParser

# This class defines a complete generic visitor for a parse tree produced by cppParser.
class Node:
    def __init__(self, node_type, value=None):
        self.node_type = node_type  # Type of node (e.g., "PROGRAM", "STATEMENT")
        self.value = value          # Value for terminal nodes (e.g., identifier, number)
        self.children : list[Node] = []          # List of child nodes
        self.parent = None

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        # if it is not a leaf node, recursively print its leaves
        if self.children:
            ret = "  " * level + "<" + self.node_type + ">" + "\n"
            for child in self.children:
                # print(ret)
                ret += child.__repr__(level + 1)
            ret += "  " * level + "</" + self.node_type + ">" + "\n"
            return ret
        # if it is a leaf node, then only print one line for the node
        else:
            ret = "  " * level + "<" + self.node_type + ">"
            if self.value:
                ret += repr(self.value)[1:-1]
            ret += "</" + self.node_type + ">" + "\n"
            return ret
        
# This class defines a complete generic visitor for a parse tree produced by CPPParser.

class CPPParserVisitor(ParseTreeVisitor):
    def __init__(self, lexer):
        self.lexer = lexer
        
    def visitTerminal(self, node):
        # Access the token associated with the terminal node
        token = node.getSymbol()

        # Get the token type (numeric value)
        token_type = token.type

        token_name = self.lexer.symbolicNames[token_type]
        
        # print("visited terminal node: ", token_name)
        
        
        node = Node(token_name, str(token.text))
        # print(node)
        return node
    
    def visitChildren(self, node):
        if isinstance(node, ParserRuleContext):
            # print("visited children")
            # print(node.getRuleIndex(), node.getText())
            rule_idx = node.getRuleIndex()
            if 0 <= rule_idx <= len(node.parser.ruleNames):
                result = Node(node.parser.ruleNames[node.getRuleIndex()])
            else:
                print(f"Error: {rule_idx} is our of bounds")
                return None
            # result = Node(node.GetType().Name)
            n = node.getChildCount()
            for i in range(n):
                if not self.shouldVisitNextChild(node, result):
                    return result

                c = node.getChild(i)
                childResult = c.accept(self)
                if childResult is not None:
                    result.add_child(childResult)

            # print(result)
            return result
        return None

    # Visit a parse tree produced by CPPParser#program.
    def visitProgram(self, ctx:CPPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#classDefinition.
    def visitClassDefinition(self, ctx:CPPParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#classBody.
    def visitClassBody(self, ctx:CPPParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:CPPParser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:CPPParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CPPParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#declaration.
    def visitDeclaration(self, ctx:CPPParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:CPPParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#parameterList.
    def visitParameterList(self, ctx:CPPParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#parameter.
    def visitParameter(self, ctx:CPPParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#compoundStatement.
    def visitCompoundStatement(self, ctx:CPPParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#statement.
    def visitStatement(self, ctx:CPPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CPPParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#selectionStatement.
    def visitSelectionStatement(self, ctx:CPPParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#iterationStatement.
    def visitIterationStatement(self, ctx:CPPParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#jumpStatement.
    def visitJumpStatement(self, ctx:CPPParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#expression.
    def visitExpression(self, ctx:CPPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:CPPParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:CPPParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:CPPParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#equalityExpression.
    def visitEqualityExpression(self, ctx:CPPParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#relationalExpression.
    def visitRelationalExpression(self, ctx:CPPParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:CPPParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:CPPParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#unaryExpression.
    def visitUnaryExpression(self, ctx:CPPParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CPPParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#declarator.
    def visitDeclarator(self, ctx:CPPParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#ioStatement.
    def visitIoStatement(self, ctx:CPPParser.IoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#outputStatement.
    def visitOutputStatement(self, ctx:CPPParser.OutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#inputStatement.
    def visitInputStatement(self, ctx:CPPParser.InputStatementContext):
        return self.visitChildren(ctx)



del CPPParser