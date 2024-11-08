# Generated from cppParser.g4 by ANTLR 4.13.2
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

    # Visit a parse tree produced by cppParser#translationUnit.
    def visitTranslationUnit(self, ctx:cppParser.TranslationUnitContext):
        print("starting parser")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:cppParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#idExpression.
    def visitIdExpression(self, ctx:cppParser.IdExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#unqualifiedId.
    def visitUnqualifiedId(self, ctx:cppParser.UnqualifiedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#qualifiedId.
    def visitQualifiedId(self, ctx:cppParser.QualifiedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#nestedNameSpecifier.
    def visitNestedNameSpecifier(self, ctx:cppParser.NestedNameSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#lambdaExpression.
    def visitLambdaExpression(self, ctx:cppParser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#lambdaIntroducer.
    def visitLambdaIntroducer(self, ctx:cppParser.LambdaIntroducerContext):
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


    # Visit a parse tree produced by cppParser#initcapture.
    def visitInitcapture(self, ctx:cppParser.InitcaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#lambdaDeclarator.
    def visitLambdaDeclarator(self, ctx:cppParser.LambdaDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#postfixExpression.
    def visitPostfixExpression(self, ctx:cppParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeIdOfTheTypeId.
    def visitTypeIdOfTheTypeId(self, ctx:cppParser.TypeIdOfTheTypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#expressionList.
    def visitExpressionList(self, ctx:cppParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#pseudoDestructorName.
    def visitPseudoDestructorName(self, ctx:cppParser.PseudoDestructorNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#unaryExpression.
    def visitUnaryExpression(self, ctx:cppParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#unaryOperator.
    def visitUnaryOperator(self, ctx:cppParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#newExpression_.
    def visitNewExpression_(self, ctx:cppParser.NewExpression_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#newPlacement.
    def visitNewPlacement(self, ctx:cppParser.NewPlacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#newTypeId.
    def visitNewTypeId(self, ctx:cppParser.NewTypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#newDeclarator_.
    def visitNewDeclarator_(self, ctx:cppParser.NewDeclarator_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#noPointerNewDeclarator.
    def visitNoPointerNewDeclarator(self, ctx:cppParser.NoPointerNewDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#newInitializer_.
    def visitNewInitializer_(self, ctx:cppParser.NewInitializer_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#deleteExpression.
    def visitDeleteExpression(self, ctx:cppParser.DeleteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#noExceptExpression.
    def visitNoExceptExpression(self, ctx:cppParser.NoExceptExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#castExpression.
    def visitCastExpression(self, ctx:cppParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#pointerMemberExpression.
    def visitPointerMemberExpression(self, ctx:cppParser.PointerMemberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:cppParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:cppParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#shiftExpression.
    def visitShiftExpression(self, ctx:cppParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#shiftOperator.
    def visitShiftOperator(self, ctx:cppParser.ShiftOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#relationalExpression.
    def visitRelationalExpression(self, ctx:cppParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#equalityExpression.
    def visitEqualityExpression(self, ctx:cppParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#andExpression.
    def visitAndExpression(self, ctx:cppParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:cppParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:cppParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:cppParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:cppParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:cppParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:cppParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:cppParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#expression.
    def visitExpression(self, ctx:cppParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#constantExpression.
    def visitConstantExpression(self, ctx:cppParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#statement.
    def visitStatement(self, ctx:cppParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#labeledStatement.
    def visitLabeledStatement(self, ctx:cppParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#expressionStatement.
    def visitExpressionStatement(self, ctx:cppParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#compoundStatement.
    def visitCompoundStatement(self, ctx:cppParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#statementSeq.
    def visitStatementSeq(self, ctx:cppParser.StatementSeqContext):
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


    # Visit a parse tree produced by cppParser#forRangeDeclaration.
    def visitForRangeDeclaration(self, ctx:cppParser.ForRangeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#forRangeInitializer.
    def visitForRangeInitializer(self, ctx:cppParser.ForRangeInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#jumpStatement.
    def visitJumpStatement(self, ctx:cppParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:cppParser.DeclarationStatementContext):
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


    # Visit a parse tree produced by cppParser#aliasDeclaration.
    def visitAliasDeclaration(self, ctx:cppParser.AliasDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#simpleDeclaration.
    def visitSimpleDeclaration(self, ctx:cppParser.SimpleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx:cppParser.StaticAssertDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#emptyDeclaration_.
    def visitEmptyDeclaration_(self, ctx:cppParser.EmptyDeclaration_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#attributeDeclaration.
    def visitAttributeDeclaration(self, ctx:cppParser.AttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declSpecifier.
    def visitDeclSpecifier(self, ctx:cppParser.DeclSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declSpecifierSeq.
    def visitDeclSpecifierSeq(self, ctx:cppParser.DeclSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:cppParser.StorageClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx:cppParser.FunctionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typedefName.
    def visitTypedefName(self, ctx:cppParser.TypedefNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:cppParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#trailingTypeSpecifier.
    def visitTrailingTypeSpecifier(self, ctx:cppParser.TrailingTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeSpecifierSeq.
    def visitTypeSpecifierSeq(self, ctx:cppParser.TypeSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#trailingTypeSpecifierSeq.
    def visitTrailingTypeSpecifierSeq(self, ctx:cppParser.TrailingTypeSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#simpleTypeLengthModifier.
    def visitSimpleTypeLengthModifier(self, ctx:cppParser.SimpleTypeLengthModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#simpleTypeSignednessModifier.
    def visitSimpleTypeSignednessModifier(self, ctx:cppParser.SimpleTypeSignednessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#simpleTypeSpecifier.
    def visitSimpleTypeSpecifier(self, ctx:cppParser.SimpleTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#theTypeName.
    def visitTheTypeName(self, ctx:cppParser.TheTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#decltypeSpecifier.
    def visitDecltypeSpecifier(self, ctx:cppParser.DecltypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#elaboratedTypeSpecifier.
    def visitElaboratedTypeSpecifier(self, ctx:cppParser.ElaboratedTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumName.
    def visitEnumName(self, ctx:cppParser.EnumNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:cppParser.EnumSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumHead.
    def visitEnumHead(self, ctx:cppParser.EnumHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#opaqueEnumDeclaration.
    def visitOpaqueEnumDeclaration(self, ctx:cppParser.OpaqueEnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumkey.
    def visitEnumkey(self, ctx:cppParser.EnumkeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumbase.
    def visitEnumbase(self, ctx:cppParser.EnumbaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumeratorList.
    def visitEnumeratorList(self, ctx:cppParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumeratorDefinition.
    def visitEnumeratorDefinition(self, ctx:cppParser.EnumeratorDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#enumerator.
    def visitEnumerator(self, ctx:cppParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#namespaceName.
    def visitNamespaceName(self, ctx:cppParser.NamespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#originalNamespaceName.
    def visitOriginalNamespaceName(self, ctx:cppParser.OriginalNamespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#namespaceDefinition.
    def visitNamespaceDefinition(self, ctx:cppParser.NamespaceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#namespaceAlias.
    def visitNamespaceAlias(self, ctx:cppParser.NamespaceAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#namespaceAliasDefinition.
    def visitNamespaceAliasDefinition(self, ctx:cppParser.NamespaceAliasDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#qualifiednamespacespecifier.
    def visitQualifiednamespacespecifier(self, ctx:cppParser.QualifiednamespacespecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#usingDeclaration.
    def visitUsingDeclaration(self, ctx:cppParser.UsingDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#usingDirective.
    def visitUsingDirective(self, ctx:cppParser.UsingDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#asmDefinition.
    def visitAsmDefinition(self, ctx:cppParser.AsmDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#linkageSpecification.
    def visitLinkageSpecification(self, ctx:cppParser.LinkageSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#attributeSpecifierSeq.
    def visitAttributeSpecifierSeq(self, ctx:cppParser.AttributeSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#attributeSpecifier.
    def visitAttributeSpecifier(self, ctx:cppParser.AttributeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#alignmentspecifier.
    def visitAlignmentspecifier(self, ctx:cppParser.AlignmentspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#attributeList.
    def visitAttributeList(self, ctx:cppParser.AttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#attribute.
    def visitAttribute(self, ctx:cppParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#attributeNamespace.
    def visitAttributeNamespace(self, ctx:cppParser.AttributeNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#attributeArgumentClause.
    def visitAttributeArgumentClause(self, ctx:cppParser.AttributeArgumentClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#balancedTokenSeq.
    def visitBalancedTokenSeq(self, ctx:cppParser.BalancedTokenSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#balancedtoken.
    def visitBalancedtoken(self, ctx:cppParser.BalancedtokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:cppParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initDeclarator.
    def visitInitDeclarator(self, ctx:cppParser.InitDeclaratorContext):
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


    # Visit a parse tree produced by cppParser#parametersAndQualifiers.
    def visitParametersAndQualifiers(self, ctx:cppParser.ParametersAndQualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#trailingReturnType.
    def visitTrailingReturnType(self, ctx:cppParser.TrailingReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#pointerOperator.
    def visitPointerOperator(self, ctx:cppParser.PointerOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#cvqualifierseq.
    def visitCvqualifierseq(self, ctx:cppParser.CvqualifierseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#cvQualifier.
    def visitCvQualifier(self, ctx:cppParser.CvQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#refqualifier.
    def visitRefqualifier(self, ctx:cppParser.RefqualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declaratorid.
    def visitDeclaratorid(self, ctx:cppParser.DeclaratoridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#theTypeId.
    def visitTheTypeId(self, ctx:cppParser.TheTypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:cppParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#pointerAbstractDeclarator.
    def visitPointerAbstractDeclarator(self, ctx:cppParser.PointerAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#noPointerAbstractDeclarator.
    def visitNoPointerAbstractDeclarator(self, ctx:cppParser.NoPointerAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#abstractPackDeclarator.
    def visitAbstractPackDeclarator(self, ctx:cppParser.AbstractPackDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#noPointerAbstractPackDeclarator.
    def visitNoPointerAbstractPackDeclarator(self, ctx:cppParser.NoPointerAbstractPackDeclaratorContext):
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


    # Visit a parse tree produced by cppParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:cppParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#functionBody.
    def visitFunctionBody(self, ctx:cppParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initializer.
    def visitInitializer(self, ctx:cppParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#braceOrEqualInitializer.
    def visitBraceOrEqualInitializer(self, ctx:cppParser.BraceOrEqualInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initializerClause.
    def visitInitializerClause(self, ctx:cppParser.InitializerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initializerList.
    def visitInitializerList(self, ctx:cppParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#bracedInitList.
    def visitBracedInitList(self, ctx:cppParser.BracedInitListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#className.
    def visitClassName(self, ctx:cppParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#classSpecifier.
    def visitClassSpecifier(self, ctx:cppParser.ClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#classHead.
    def visitClassHead(self, ctx:cppParser.ClassHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#classHeadName.
    def visitClassHeadName(self, ctx:cppParser.ClassHeadNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#classVirtSpecifier.
    def visitClassVirtSpecifier(self, ctx:cppParser.ClassVirtSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#classKey.
    def visitClassKey(self, ctx:cppParser.ClassKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#memberSpecification.
    def visitMemberSpecification(self, ctx:cppParser.MemberSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#memberdeclaration.
    def visitMemberdeclaration(self, ctx:cppParser.MemberdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#memberDeclaratorList.
    def visitMemberDeclaratorList(self, ctx:cppParser.MemberDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#memberDeclarator.
    def visitMemberDeclarator(self, ctx:cppParser.MemberDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#virtualSpecifierSeq.
    def visitVirtualSpecifierSeq(self, ctx:cppParser.VirtualSpecifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#virtualSpecifier.
    def visitVirtualSpecifier(self, ctx:cppParser.VirtualSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#pureSpecifier.
    def visitPureSpecifier(self, ctx:cppParser.PureSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#baseClause.
    def visitBaseClause(self, ctx:cppParser.BaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#baseSpecifierList.
    def visitBaseSpecifierList(self, ctx:cppParser.BaseSpecifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#baseSpecifier.
    def visitBaseSpecifier(self, ctx:cppParser.BaseSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#classOrDeclType.
    def visitClassOrDeclType(self, ctx:cppParser.ClassOrDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#baseTypeSpecifier.
    def visitBaseTypeSpecifier(self, ctx:cppParser.BaseTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:cppParser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#conversionFunctionId.
    def visitConversionFunctionId(self, ctx:cppParser.ConversionFunctionIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#conversionTypeId.
    def visitConversionTypeId(self, ctx:cppParser.ConversionTypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#conversionDeclarator.
    def visitConversionDeclarator(self, ctx:cppParser.ConversionDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#constructorInitializer.
    def visitConstructorInitializer(self, ctx:cppParser.ConstructorInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#memInitializerList.
    def visitMemInitializerList(self, ctx:cppParser.MemInitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#memInitializer.
    def visitMemInitializer(self, ctx:cppParser.MemInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#meminitializerid.
    def visitMeminitializerid(self, ctx:cppParser.MeminitializeridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#operatorFunctionId.
    def visitOperatorFunctionId(self, ctx:cppParser.OperatorFunctionIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#literalOperatorId.
    def visitLiteralOperatorId(self, ctx:cppParser.LiteralOperatorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateDeclaration.
    def visitTemplateDeclaration(self, ctx:cppParser.TemplateDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateparameterList.
    def visitTemplateparameterList(self, ctx:cppParser.TemplateparameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateParameter.
    def visitTemplateParameter(self, ctx:cppParser.TemplateParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeParameter.
    def visitTypeParameter(self, ctx:cppParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#simpleTemplateId.
    def visitSimpleTemplateId(self, ctx:cppParser.SimpleTemplateIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateId.
    def visitTemplateId(self, ctx:cppParser.TemplateIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateName.
    def visitTemplateName(self, ctx:cppParser.TemplateNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateArgumentList.
    def visitTemplateArgumentList(self, ctx:cppParser.TemplateArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateArgument.
    def visitTemplateArgument(self, ctx:cppParser.TemplateArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeNameSpecifier.
    def visitTypeNameSpecifier(self, ctx:cppParser.TypeNameSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#explicitInstantiation.
    def visitExplicitInstantiation(self, ctx:cppParser.ExplicitInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#explicitSpecialization.
    def visitExplicitSpecialization(self, ctx:cppParser.ExplicitSpecializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#tryBlock.
    def visitTryBlock(self, ctx:cppParser.TryBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#functionTryBlock.
    def visitFunctionTryBlock(self, ctx:cppParser.FunctionTryBlockContext):
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


    # Visit a parse tree produced by cppParser#throwExpression.
    def visitThrowExpression(self, ctx:cppParser.ThrowExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#exceptionSpecification.
    def visitExceptionSpecification(self, ctx:cppParser.ExceptionSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#dynamicExceptionSpecification.
    def visitDynamicExceptionSpecification(self, ctx:cppParser.DynamicExceptionSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeIdList.
    def visitTypeIdList(self, ctx:cppParser.TypeIdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#noeExceptSpecification.
    def visitNoeExceptSpecification(self, ctx:cppParser.NoeExceptSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#theOperator.
    def visitTheOperator(self, ctx:cppParser.TheOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#literal.
    def visitLiteral(self, ctx:cppParser.LiteralContext):
        return self.visitChildren(ctx)



del cppParser