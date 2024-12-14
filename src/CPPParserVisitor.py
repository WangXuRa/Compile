# Generated from CPPParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CPPParser import CPPParser
else:
    from CPPParser import CPPParser

# This class defines a complete generic visitor for a parse tree produced by CPPParser.

from translation.node import Node

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


    # Visit a parse tree produced by CPPParser#decl_.
    def visitDecl_(self, ctx:CPPParser.Decl_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#decl_assign.
    def visitDecl_assign(self, ctx:CPPParser.Decl_assignContext):
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


    # Visit a parse tree produced by CPPParser#includeStatement.
    def visitIncludeStatement(self, ctx:CPPParser.IncludeStatementContext):
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


    # Visit a parse tree produced by CPPParser#shiftExpression.
    def visitShiftExpression(self, ctx:CPPParser.ShiftExpressionContext):
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


    # Visit a parse tree produced by CPPParser#postfixExpression.
    def visitPostfixExpression(self, ctx:CPPParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CPPParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#functionCall.
    def visitFunctionCall(self, ctx:CPPParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#number.
    def visitNumber(self, ctx:CPPParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#declarator.
    def visitDeclarator(self, ctx:CPPParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#shiftOperator.
    def visitShiftOperator(self, ctx:CPPParser.ShiftOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#includeID.
    def visitIncludeID(self, ctx:CPPParser.IncludeIDContext):
        return self.visitChildren(ctx)



del CPPParser