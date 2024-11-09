# Generated from cppParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .cppParser import cppParser
else:
    from cppParser import cppParser

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
        

# This class defines a complete generic visitor for a parse tree produced by cppParser.

class cppParserVisitor(ParseTreeVisitor):
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

    # Visit a parse tree produced by cppParser#compilationUnit.
    def visitCompilationUnit(self, ctx:cppParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#preprocessorDeclaration.
    def visitPreprocessorDeclaration(self, ctx:cppParser.PreprocessorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#translationUnit.
    def visitTranslationUnit(self, ctx:cppParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declarationseq.
    def visitDeclarationseq(self, ctx:cppParser.DeclarationseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declaration.
    def visitDeclaration(self, ctx:cppParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#blockDeclaration.
    def visitBlockDeclaration(self, ctx:cppParser.BlockDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#simpleDeclaration.
    def visitSimpleDeclaration(self, ctx:cppParser.SimpleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declSpecifierSeq.
    def visitDeclSpecifierSeq(self, ctx:cppParser.DeclSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declSpecifier.
    def visitDeclSpecifier(self, ctx:cppParser.DeclSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:cppParser.StorageClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:cppParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#elaboratedTypeSpecifier.
    def visitElaboratedTypeSpecifier(self, ctx:cppParser.ElaboratedTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumDefinition.
    def visitEnumDefinition(self, ctx:cppParser.EnumDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumeratorList.
    def visitEnumeratorList(self, ctx:cppParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumerator.
    def visitEnumerator(self, ctx:cppParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#simpleTypeSpecifier.
    def visitSimpleTypeSpecifier(self, ctx:cppParser.SimpleTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:cppParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#functionBody.
    def visitFunctionBody(self, ctx:cppParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#classDefinition.
    def visitClassDefinition(self, ctx:cppParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#classBase.
    def visitClassBase(self, ctx:cppParser.ClassBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#baseSpecifierList.
    def visitBaseSpecifierList(self, ctx:cppParser.BaseSpecifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#baseSpecifier.
    def visitBaseSpecifier(self, ctx:cppParser.BaseSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:cppParser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#memberSpecification.
    def visitMemberSpecification(self, ctx:cppParser.MemberSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:cppParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#statement.
    def visitStatement(self, ctx:cppParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:cppParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#labeledStatement.
    def visitLabeledStatement(self, ctx:cppParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#compoundStatement.
    def visitCompoundStatement(self, ctx:cppParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#statementSeq.
    def visitStatementSeq(self, ctx:cppParser.StatementSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#expressionStatement.
    def visitExpressionStatement(self, ctx:cppParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#selectionStatement.
    def visitSelectionStatement(self, ctx:cppParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#condition.
    def visitCondition(self, ctx:cppParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#iterationStatement.
    def visitIterationStatement(self, ctx:cppParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#forInitStatement.
    def visitForInitStatement(self, ctx:cppParser.ForInitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#jumpStatement.
    def visitJumpStatement(self, ctx:cppParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#newExpression.
    def visitNewExpression(self, ctx:cppParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#deleteExpression.
    def visitDeleteExpression(self, ctx:cppParser.DeleteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#expression.
    def visitExpression(self, ctx:cppParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:cppParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:cppParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:cppParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:cppParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:cppParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:cppParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:cppParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#andExpression.
    def visitAndExpression(self, ctx:cppParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#equalityExpression.
    def visitEqualityExpression(self, ctx:cppParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#relationalExpression.
    def visitRelationalExpression(self, ctx:cppParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:cppParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:cppParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#unaryExpression.
    def visitUnaryExpression(self, ctx:cppParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#unaryOperator.
    def visitUnaryOperator(self, ctx:cppParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#postfixExpression.
    def visitPostfixExpression(self, ctx:cppParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:cppParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#expressionList.
    def visitExpressionList(self, ctx:cppParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#literal.
    def visitLiteral(self, ctx:cppParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#lambdaExpression.
    def visitLambdaExpression(self, ctx:cppParser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#lambdaCapture.
    def visitLambdaCapture(self, ctx:cppParser.LambdaCaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#captureDefault.
    def visitCaptureDefault(self, ctx:cppParser.CaptureDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#captureList.
    def visitCaptureList(self, ctx:cppParser.CaptureListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#capture.
    def visitCapture(self, ctx:cppParser.CaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#simpleCapture.
    def visitSimpleCapture(self, ctx:cppParser.SimpleCaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initCapture.
    def visitInitCapture(self, ctx:cppParser.InitCaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#lambdaBody.
    def visitLambdaBody(self, ctx:cppParser.LambdaBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateDeclaration.
    def visitTemplateDeclaration(self, ctx:cppParser.TemplateDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateParameterList.
    def visitTemplateParameterList(self, ctx:cppParser.TemplateParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateParameter.
    def visitTemplateParameter(self, ctx:cppParser.TemplateParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeParameter.
    def visitTypeParameter(self, ctx:cppParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#namespaceDefinition.
    def visitNamespaceDefinition(self, ctx:cppParser.NamespaceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#usingDeclaration.
    def visitUsingDeclaration(self, ctx:cppParser.UsingDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#operatorOverloadingDeclaration.
    def visitOperatorOverloadingDeclaration(self, ctx:cppParser.OperatorOverloadingDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#overloadableOperator.
    def visitOverloadableOperator(self, ctx:cppParser.OverloadableOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#friendDeclaration.
    def visitFriendDeclaration(self, ctx:cppParser.FriendDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#friendDeclaratorList.
    def visitFriendDeclaratorList(self, ctx:cppParser.FriendDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#smartPointerType.
    def visitSmartPointerType(self, ctx:cppParser.SmartPointerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#smartPointerCreation.
    def visitSmartPointerCreation(self, ctx:cppParser.SmartPointerCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#forRangeDeclaration.
    def visitForRangeDeclaration(self, ctx:cppParser.ForRangeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#forRangeInitializer.
    def visitForRangeInitializer(self, ctx:cppParser.ForRangeInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#bracedInitList.
    def visitBracedInitList(self, ctx:cppParser.BracedInitListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declarator.
    def visitDeclarator(self, ctx:cppParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#pointerDeclarator.
    def visitPointerDeclarator(self, ctx:cppParser.PointerDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#noPointerDeclarator.
    def visitNoPointerDeclarator(self, ctx:cppParser.NoPointerDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declaratorId.
    def visitDeclaratorId(self, ctx:cppParser.DeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#parametersAndQualifiers.
    def visitParametersAndQualifiers(self, ctx:cppParser.ParametersAndQualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeQualifierSeq.
    def visitTypeQualifierSeq(self, ctx:cppParser.TypeQualifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#parameterDeclarationClause.
    def visitParameterDeclarationClause(self, ctx:cppParser.ParameterDeclarationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#parameterDeclarationList.
    def visitParameterDeclarationList(self, ctx:cppParser.ParameterDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:cppParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#cvQualifierSeq.
    def visitCvQualifierSeq(self, ctx:cppParser.CvQualifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#cvQualifier.
    def visitCvQualifier(self, ctx:cppParser.CvQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:cppParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#pointerAbstractDeclarator.
    def visitPointerAbstractDeclarator(self, ctx:cppParser.PointerAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#constantExpression.
    def visitConstantExpression(self, ctx:cppParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:cppParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initDeclarator.
    def visitInitDeclarator(self, ctx:cppParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initializer.
    def visitInitializer(self, ctx:cppParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initializerClause.
    def visitInitializerClause(self, ctx:cppParser.InitializerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initializerList.
    def visitInitializerList(self, ctx:cppParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#type.
    def visitType(self, ctx:cppParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#pointerOperators.
    def visitPointerOperators(self, ctx:cppParser.PointerOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#tryBlock.
    def visitTryBlock(self, ctx:cppParser.TryBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#handlerSeq.
    def visitHandlerSeq(self, ctx:cppParser.HandlerSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#handler.
    def visitHandler(self, ctx:cppParser.HandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#exceptionDeclaration.
    def visitExceptionDeclaration(self, ctx:cppParser.ExceptionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#exceptionSpecification.
    def visitExceptionSpecification(self, ctx:cppParser.ExceptionSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeIdList.
    def visitTypeIdList(self, ctx:cppParser.TypeIdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#ioStatement.
    def visitIoStatement(self, ctx:cppParser.IoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#outputStatement.
    def visitOutputStatement(self, ctx:cppParser.OutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#inputStatement.
    def visitInputStatement(self, ctx:cppParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#getlineStatement.
    def visitGetlineStatement(self, ctx:cppParser.GetlineStatementContext):
        return self.visitChildren(ctx)



del cppParser