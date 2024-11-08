# Generated from cppParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cppParser import cppParser
else:
    from cppParser import cppParser

# This class defines a complete listener for a parse tree produced by cppParser.
class cppParserListener(ParseTreeListener):

    # Enter a parse tree produced by cppParser#translationUnit.
    def enterTranslationUnit(self, ctx:cppParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by cppParser#translationUnit.
    def exitTranslationUnit(self, ctx:cppParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by cppParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:cppParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:cppParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#idExpression.
    def enterIdExpression(self, ctx:cppParser.IdExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#idExpression.
    def exitIdExpression(self, ctx:cppParser.IdExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#unqualifiedId.
    def enterUnqualifiedId(self, ctx:cppParser.UnqualifiedIdContext):
        pass

    # Exit a parse tree produced by cppParser#unqualifiedId.
    def exitUnqualifiedId(self, ctx:cppParser.UnqualifiedIdContext):
        pass


    # Enter a parse tree produced by cppParser#qualifiedId.
    def enterQualifiedId(self, ctx:cppParser.QualifiedIdContext):
        pass

    # Exit a parse tree produced by cppParser#qualifiedId.
    def exitQualifiedId(self, ctx:cppParser.QualifiedIdContext):
        pass


    # Enter a parse tree produced by cppParser#nestedNameSpecifier.
    def enterNestedNameSpecifier(self, ctx:cppParser.NestedNameSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#nestedNameSpecifier.
    def exitNestedNameSpecifier(self, ctx:cppParser.NestedNameSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:cppParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:cppParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#lambdaIntroducer.
    def enterLambdaIntroducer(self, ctx:cppParser.LambdaIntroducerContext):
        pass

    # Exit a parse tree produced by cppParser#lambdaIntroducer.
    def exitLambdaIntroducer(self, ctx:cppParser.LambdaIntroducerContext):
        pass


    # Enter a parse tree produced by cppParser#lambdaCapture.
    def enterLambdaCapture(self, ctx:cppParser.LambdaCaptureContext):
        pass

    # Exit a parse tree produced by cppParser#lambdaCapture.
    def exitLambdaCapture(self, ctx:cppParser.LambdaCaptureContext):
        pass


    # Enter a parse tree produced by cppParser#captureDefault.
    def enterCaptureDefault(self, ctx:cppParser.CaptureDefaultContext):
        pass

    # Exit a parse tree produced by cppParser#captureDefault.
    def exitCaptureDefault(self, ctx:cppParser.CaptureDefaultContext):
        pass


    # Enter a parse tree produced by cppParser#captureList.
    def enterCaptureList(self, ctx:cppParser.CaptureListContext):
        pass

    # Exit a parse tree produced by cppParser#captureList.
    def exitCaptureList(self, ctx:cppParser.CaptureListContext):
        pass


    # Enter a parse tree produced by cppParser#capture.
    def enterCapture(self, ctx:cppParser.CaptureContext):
        pass

    # Exit a parse tree produced by cppParser#capture.
    def exitCapture(self, ctx:cppParser.CaptureContext):
        pass


    # Enter a parse tree produced by cppParser#simpleCapture.
    def enterSimpleCapture(self, ctx:cppParser.SimpleCaptureContext):
        pass

    # Exit a parse tree produced by cppParser#simpleCapture.
    def exitSimpleCapture(self, ctx:cppParser.SimpleCaptureContext):
        pass


    # Enter a parse tree produced by cppParser#initcapture.
    def enterInitcapture(self, ctx:cppParser.InitcaptureContext):
        pass

    # Exit a parse tree produced by cppParser#initcapture.
    def exitInitcapture(self, ctx:cppParser.InitcaptureContext):
        pass


    # Enter a parse tree produced by cppParser#lambdaDeclarator.
    def enterLambdaDeclarator(self, ctx:cppParser.LambdaDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#lambdaDeclarator.
    def exitLambdaDeclarator(self, ctx:cppParser.LambdaDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#postfixExpression.
    def enterPostfixExpression(self, ctx:cppParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#postfixExpression.
    def exitPostfixExpression(self, ctx:cppParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#typeIdOfTheTypeId.
    def enterTypeIdOfTheTypeId(self, ctx:cppParser.TypeIdOfTheTypeIdContext):
        pass

    # Exit a parse tree produced by cppParser#typeIdOfTheTypeId.
    def exitTypeIdOfTheTypeId(self, ctx:cppParser.TypeIdOfTheTypeIdContext):
        pass


    # Enter a parse tree produced by cppParser#expressionList.
    def enterExpressionList(self, ctx:cppParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by cppParser#expressionList.
    def exitExpressionList(self, ctx:cppParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by cppParser#pseudoDestructorName.
    def enterPseudoDestructorName(self, ctx:cppParser.PseudoDestructorNameContext):
        pass

    # Exit a parse tree produced by cppParser#pseudoDestructorName.
    def exitPseudoDestructorName(self, ctx:cppParser.PseudoDestructorNameContext):
        pass


    # Enter a parse tree produced by cppParser#unaryExpression.
    def enterUnaryExpression(self, ctx:cppParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#unaryExpression.
    def exitUnaryExpression(self, ctx:cppParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#unaryOperator.
    def enterUnaryOperator(self, ctx:cppParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by cppParser#unaryOperator.
    def exitUnaryOperator(self, ctx:cppParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by cppParser#newExpression_.
    def enterNewExpression_(self, ctx:cppParser.NewExpression_Context):
        pass

    # Exit a parse tree produced by cppParser#newExpression_.
    def exitNewExpression_(self, ctx:cppParser.NewExpression_Context):
        pass


    # Enter a parse tree produced by cppParser#newPlacement.
    def enterNewPlacement(self, ctx:cppParser.NewPlacementContext):
        pass

    # Exit a parse tree produced by cppParser#newPlacement.
    def exitNewPlacement(self, ctx:cppParser.NewPlacementContext):
        pass


    # Enter a parse tree produced by cppParser#newTypeId.
    def enterNewTypeId(self, ctx:cppParser.NewTypeIdContext):
        pass

    # Exit a parse tree produced by cppParser#newTypeId.
    def exitNewTypeId(self, ctx:cppParser.NewTypeIdContext):
        pass


    # Enter a parse tree produced by cppParser#newDeclarator_.
    def enterNewDeclarator_(self, ctx:cppParser.NewDeclarator_Context):
        pass

    # Exit a parse tree produced by cppParser#newDeclarator_.
    def exitNewDeclarator_(self, ctx:cppParser.NewDeclarator_Context):
        pass


    # Enter a parse tree produced by cppParser#noPointerNewDeclarator.
    def enterNoPointerNewDeclarator(self, ctx:cppParser.NoPointerNewDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#noPointerNewDeclarator.
    def exitNoPointerNewDeclarator(self, ctx:cppParser.NoPointerNewDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#newInitializer_.
    def enterNewInitializer_(self, ctx:cppParser.NewInitializer_Context):
        pass

    # Exit a parse tree produced by cppParser#newInitializer_.
    def exitNewInitializer_(self, ctx:cppParser.NewInitializer_Context):
        pass


    # Enter a parse tree produced by cppParser#deleteExpression.
    def enterDeleteExpression(self, ctx:cppParser.DeleteExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#deleteExpression.
    def exitDeleteExpression(self, ctx:cppParser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#noExceptExpression.
    def enterNoExceptExpression(self, ctx:cppParser.NoExceptExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#noExceptExpression.
    def exitNoExceptExpression(self, ctx:cppParser.NoExceptExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#castExpression.
    def enterCastExpression(self, ctx:cppParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#castExpression.
    def exitCastExpression(self, ctx:cppParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#pointerMemberExpression.
    def enterPointerMemberExpression(self, ctx:cppParser.PointerMemberExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#pointerMemberExpression.
    def exitPointerMemberExpression(self, ctx:cppParser.PointerMemberExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:cppParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:cppParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:cppParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:cppParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#shiftExpression.
    def enterShiftExpression(self, ctx:cppParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#shiftExpression.
    def exitShiftExpression(self, ctx:cppParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#shiftOperator.
    def enterShiftOperator(self, ctx:cppParser.ShiftOperatorContext):
        pass

    # Exit a parse tree produced by cppParser#shiftOperator.
    def exitShiftOperator(self, ctx:cppParser.ShiftOperatorContext):
        pass


    # Enter a parse tree produced by cppParser#relationalExpression.
    def enterRelationalExpression(self, ctx:cppParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#relationalExpression.
    def exitRelationalExpression(self, ctx:cppParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#equalityExpression.
    def enterEqualityExpression(self, ctx:cppParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#equalityExpression.
    def exitEqualityExpression(self, ctx:cppParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#andExpression.
    def enterAndExpression(self, ctx:cppParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#andExpression.
    def exitAndExpression(self, ctx:cppParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:cppParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:cppParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:cppParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:cppParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:cppParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:cppParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:cppParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:cppParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:cppParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:cppParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:cppParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:cppParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:cppParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by cppParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:cppParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by cppParser#expression.
    def enterExpression(self, ctx:cppParser.ExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#expression.
    def exitExpression(self, ctx:cppParser.ExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#constantExpression.
    def enterConstantExpression(self, ctx:cppParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#constantExpression.
    def exitConstantExpression(self, ctx:cppParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#statement.
    def enterStatement(self, ctx:cppParser.StatementContext):
        pass

    # Exit a parse tree produced by cppParser#statement.
    def exitStatement(self, ctx:cppParser.StatementContext):
        pass


    # Enter a parse tree produced by cppParser#labeledStatement.
    def enterLabeledStatement(self, ctx:cppParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by cppParser#labeledStatement.
    def exitLabeledStatement(self, ctx:cppParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by cppParser#expressionStatement.
    def enterExpressionStatement(self, ctx:cppParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by cppParser#expressionStatement.
    def exitExpressionStatement(self, ctx:cppParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by cppParser#compoundStatement.
    def enterCompoundStatement(self, ctx:cppParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by cppParser#compoundStatement.
    def exitCompoundStatement(self, ctx:cppParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by cppParser#statementSeq.
    def enterStatementSeq(self, ctx:cppParser.StatementSeqContext):
        pass

    # Exit a parse tree produced by cppParser#statementSeq.
    def exitStatementSeq(self, ctx:cppParser.StatementSeqContext):
        pass


    # Enter a parse tree produced by cppParser#selectionStatement.
    def enterSelectionStatement(self, ctx:cppParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by cppParser#selectionStatement.
    def exitSelectionStatement(self, ctx:cppParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by cppParser#condition.
    def enterCondition(self, ctx:cppParser.ConditionContext):
        pass

    # Exit a parse tree produced by cppParser#condition.
    def exitCondition(self, ctx:cppParser.ConditionContext):
        pass


    # Enter a parse tree produced by cppParser#iterationStatement.
    def enterIterationStatement(self, ctx:cppParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by cppParser#iterationStatement.
    def exitIterationStatement(self, ctx:cppParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by cppParser#forInitStatement.
    def enterForInitStatement(self, ctx:cppParser.ForInitStatementContext):
        pass

    # Exit a parse tree produced by cppParser#forInitStatement.
    def exitForInitStatement(self, ctx:cppParser.ForInitStatementContext):
        pass


    # Enter a parse tree produced by cppParser#forRangeDeclaration.
    def enterForRangeDeclaration(self, ctx:cppParser.ForRangeDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#forRangeDeclaration.
    def exitForRangeDeclaration(self, ctx:cppParser.ForRangeDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#forRangeInitializer.
    def enterForRangeInitializer(self, ctx:cppParser.ForRangeInitializerContext):
        pass

    # Exit a parse tree produced by cppParser#forRangeInitializer.
    def exitForRangeInitializer(self, ctx:cppParser.ForRangeInitializerContext):
        pass


    # Enter a parse tree produced by cppParser#jumpStatement.
    def enterJumpStatement(self, ctx:cppParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by cppParser#jumpStatement.
    def exitJumpStatement(self, ctx:cppParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by cppParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:cppParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by cppParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:cppParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by cppParser#declarationseq.
    def enterDeclarationseq(self, ctx:cppParser.DeclarationseqContext):
        pass

    # Exit a parse tree produced by cppParser#declarationseq.
    def exitDeclarationseq(self, ctx:cppParser.DeclarationseqContext):
        pass


    # Enter a parse tree produced by cppParser#declaration.
    def enterDeclaration(self, ctx:cppParser.DeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#declaration.
    def exitDeclaration(self, ctx:cppParser.DeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#blockDeclaration.
    def enterBlockDeclaration(self, ctx:cppParser.BlockDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#blockDeclaration.
    def exitBlockDeclaration(self, ctx:cppParser.BlockDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#aliasDeclaration.
    def enterAliasDeclaration(self, ctx:cppParser.AliasDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#aliasDeclaration.
    def exitAliasDeclaration(self, ctx:cppParser.AliasDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#simpleDeclaration.
    def enterSimpleDeclaration(self, ctx:cppParser.SimpleDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#simpleDeclaration.
    def exitSimpleDeclaration(self, ctx:cppParser.SimpleDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:cppParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:cppParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#emptyDeclaration_.
    def enterEmptyDeclaration_(self, ctx:cppParser.EmptyDeclaration_Context):
        pass

    # Exit a parse tree produced by cppParser#emptyDeclaration_.
    def exitEmptyDeclaration_(self, ctx:cppParser.EmptyDeclaration_Context):
        pass


    # Enter a parse tree produced by cppParser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:cppParser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:cppParser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#declSpecifier.
    def enterDeclSpecifier(self, ctx:cppParser.DeclSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#declSpecifier.
    def exitDeclSpecifier(self, ctx:cppParser.DeclSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#declSpecifierSeq.
    def enterDeclSpecifierSeq(self, ctx:cppParser.DeclSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cppParser#declSpecifierSeq.
    def exitDeclSpecifierSeq(self, ctx:cppParser.DeclSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cppParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:cppParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:cppParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:cppParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:cppParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#typedefName.
    def enterTypedefName(self, ctx:cppParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by cppParser#typedefName.
    def exitTypedefName(self, ctx:cppParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by cppParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:cppParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:cppParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#trailingTypeSpecifier.
    def enterTrailingTypeSpecifier(self, ctx:cppParser.TrailingTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#trailingTypeSpecifier.
    def exitTrailingTypeSpecifier(self, ctx:cppParser.TrailingTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#typeSpecifierSeq.
    def enterTypeSpecifierSeq(self, ctx:cppParser.TypeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cppParser#typeSpecifierSeq.
    def exitTypeSpecifierSeq(self, ctx:cppParser.TypeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cppParser#trailingTypeSpecifierSeq.
    def enterTrailingTypeSpecifierSeq(self, ctx:cppParser.TrailingTypeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cppParser#trailingTypeSpecifierSeq.
    def exitTrailingTypeSpecifierSeq(self, ctx:cppParser.TrailingTypeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cppParser#simpleTypeLengthModifier.
    def enterSimpleTypeLengthModifier(self, ctx:cppParser.SimpleTypeLengthModifierContext):
        pass

    # Exit a parse tree produced by cppParser#simpleTypeLengthModifier.
    def exitSimpleTypeLengthModifier(self, ctx:cppParser.SimpleTypeLengthModifierContext):
        pass


    # Enter a parse tree produced by cppParser#simpleTypeSignednessModifier.
    def enterSimpleTypeSignednessModifier(self, ctx:cppParser.SimpleTypeSignednessModifierContext):
        pass

    # Exit a parse tree produced by cppParser#simpleTypeSignednessModifier.
    def exitSimpleTypeSignednessModifier(self, ctx:cppParser.SimpleTypeSignednessModifierContext):
        pass


    # Enter a parse tree produced by cppParser#simpleTypeSpecifier.
    def enterSimpleTypeSpecifier(self, ctx:cppParser.SimpleTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#simpleTypeSpecifier.
    def exitSimpleTypeSpecifier(self, ctx:cppParser.SimpleTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#theTypeName.
    def enterTheTypeName(self, ctx:cppParser.TheTypeNameContext):
        pass

    # Exit a parse tree produced by cppParser#theTypeName.
    def exitTheTypeName(self, ctx:cppParser.TheTypeNameContext):
        pass


    # Enter a parse tree produced by cppParser#decltypeSpecifier.
    def enterDecltypeSpecifier(self, ctx:cppParser.DecltypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#decltypeSpecifier.
    def exitDecltypeSpecifier(self, ctx:cppParser.DecltypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#elaboratedTypeSpecifier.
    def enterElaboratedTypeSpecifier(self, ctx:cppParser.ElaboratedTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#elaboratedTypeSpecifier.
    def exitElaboratedTypeSpecifier(self, ctx:cppParser.ElaboratedTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#enumName.
    def enterEnumName(self, ctx:cppParser.EnumNameContext):
        pass

    # Exit a parse tree produced by cppParser#enumName.
    def exitEnumName(self, ctx:cppParser.EnumNameContext):
        pass


    # Enter a parse tree produced by cppParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:cppParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:cppParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#enumHead.
    def enterEnumHead(self, ctx:cppParser.EnumHeadContext):
        pass

    # Exit a parse tree produced by cppParser#enumHead.
    def exitEnumHead(self, ctx:cppParser.EnumHeadContext):
        pass


    # Enter a parse tree produced by cppParser#opaqueEnumDeclaration.
    def enterOpaqueEnumDeclaration(self, ctx:cppParser.OpaqueEnumDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#opaqueEnumDeclaration.
    def exitOpaqueEnumDeclaration(self, ctx:cppParser.OpaqueEnumDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#enumkey.
    def enterEnumkey(self, ctx:cppParser.EnumkeyContext):
        pass

    # Exit a parse tree produced by cppParser#enumkey.
    def exitEnumkey(self, ctx:cppParser.EnumkeyContext):
        pass


    # Enter a parse tree produced by cppParser#enumbase.
    def enterEnumbase(self, ctx:cppParser.EnumbaseContext):
        pass

    # Exit a parse tree produced by cppParser#enumbase.
    def exitEnumbase(self, ctx:cppParser.EnumbaseContext):
        pass


    # Enter a parse tree produced by cppParser#enumeratorList.
    def enterEnumeratorList(self, ctx:cppParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by cppParser#enumeratorList.
    def exitEnumeratorList(self, ctx:cppParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by cppParser#enumeratorDefinition.
    def enterEnumeratorDefinition(self, ctx:cppParser.EnumeratorDefinitionContext):
        pass

    # Exit a parse tree produced by cppParser#enumeratorDefinition.
    def exitEnumeratorDefinition(self, ctx:cppParser.EnumeratorDefinitionContext):
        pass


    # Enter a parse tree produced by cppParser#enumerator.
    def enterEnumerator(self, ctx:cppParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by cppParser#enumerator.
    def exitEnumerator(self, ctx:cppParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by cppParser#namespaceName.
    def enterNamespaceName(self, ctx:cppParser.NamespaceNameContext):
        pass

    # Exit a parse tree produced by cppParser#namespaceName.
    def exitNamespaceName(self, ctx:cppParser.NamespaceNameContext):
        pass


    # Enter a parse tree produced by cppParser#originalNamespaceName.
    def enterOriginalNamespaceName(self, ctx:cppParser.OriginalNamespaceNameContext):
        pass

    # Exit a parse tree produced by cppParser#originalNamespaceName.
    def exitOriginalNamespaceName(self, ctx:cppParser.OriginalNamespaceNameContext):
        pass


    # Enter a parse tree produced by cppParser#namespaceDefinition.
    def enterNamespaceDefinition(self, ctx:cppParser.NamespaceDefinitionContext):
        pass

    # Exit a parse tree produced by cppParser#namespaceDefinition.
    def exitNamespaceDefinition(self, ctx:cppParser.NamespaceDefinitionContext):
        pass


    # Enter a parse tree produced by cppParser#namespaceAlias.
    def enterNamespaceAlias(self, ctx:cppParser.NamespaceAliasContext):
        pass

    # Exit a parse tree produced by cppParser#namespaceAlias.
    def exitNamespaceAlias(self, ctx:cppParser.NamespaceAliasContext):
        pass


    # Enter a parse tree produced by cppParser#namespaceAliasDefinition.
    def enterNamespaceAliasDefinition(self, ctx:cppParser.NamespaceAliasDefinitionContext):
        pass

    # Exit a parse tree produced by cppParser#namespaceAliasDefinition.
    def exitNamespaceAliasDefinition(self, ctx:cppParser.NamespaceAliasDefinitionContext):
        pass


    # Enter a parse tree produced by cppParser#qualifiednamespacespecifier.
    def enterQualifiednamespacespecifier(self, ctx:cppParser.QualifiednamespacespecifierContext):
        pass

    # Exit a parse tree produced by cppParser#qualifiednamespacespecifier.
    def exitQualifiednamespacespecifier(self, ctx:cppParser.QualifiednamespacespecifierContext):
        pass


    # Enter a parse tree produced by cppParser#usingDeclaration.
    def enterUsingDeclaration(self, ctx:cppParser.UsingDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#usingDeclaration.
    def exitUsingDeclaration(self, ctx:cppParser.UsingDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#usingDirective.
    def enterUsingDirective(self, ctx:cppParser.UsingDirectiveContext):
        pass

    # Exit a parse tree produced by cppParser#usingDirective.
    def exitUsingDirective(self, ctx:cppParser.UsingDirectiveContext):
        pass


    # Enter a parse tree produced by cppParser#asmDefinition.
    def enterAsmDefinition(self, ctx:cppParser.AsmDefinitionContext):
        pass

    # Exit a parse tree produced by cppParser#asmDefinition.
    def exitAsmDefinition(self, ctx:cppParser.AsmDefinitionContext):
        pass


    # Enter a parse tree produced by cppParser#linkageSpecification.
    def enterLinkageSpecification(self, ctx:cppParser.LinkageSpecificationContext):
        pass

    # Exit a parse tree produced by cppParser#linkageSpecification.
    def exitLinkageSpecification(self, ctx:cppParser.LinkageSpecificationContext):
        pass


    # Enter a parse tree produced by cppParser#attributeSpecifierSeq.
    def enterAttributeSpecifierSeq(self, ctx:cppParser.AttributeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cppParser#attributeSpecifierSeq.
    def exitAttributeSpecifierSeq(self, ctx:cppParser.AttributeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cppParser#attributeSpecifier.
    def enterAttributeSpecifier(self, ctx:cppParser.AttributeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#attributeSpecifier.
    def exitAttributeSpecifier(self, ctx:cppParser.AttributeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#alignmentspecifier.
    def enterAlignmentspecifier(self, ctx:cppParser.AlignmentspecifierContext):
        pass

    # Exit a parse tree produced by cppParser#alignmentspecifier.
    def exitAlignmentspecifier(self, ctx:cppParser.AlignmentspecifierContext):
        pass


    # Enter a parse tree produced by cppParser#attributeList.
    def enterAttributeList(self, ctx:cppParser.AttributeListContext):
        pass

    # Exit a parse tree produced by cppParser#attributeList.
    def exitAttributeList(self, ctx:cppParser.AttributeListContext):
        pass


    # Enter a parse tree produced by cppParser#attribute.
    def enterAttribute(self, ctx:cppParser.AttributeContext):
        pass

    # Exit a parse tree produced by cppParser#attribute.
    def exitAttribute(self, ctx:cppParser.AttributeContext):
        pass


    # Enter a parse tree produced by cppParser#attributeNamespace.
    def enterAttributeNamespace(self, ctx:cppParser.AttributeNamespaceContext):
        pass

    # Exit a parse tree produced by cppParser#attributeNamespace.
    def exitAttributeNamespace(self, ctx:cppParser.AttributeNamespaceContext):
        pass


    # Enter a parse tree produced by cppParser#attributeArgumentClause.
    def enterAttributeArgumentClause(self, ctx:cppParser.AttributeArgumentClauseContext):
        pass

    # Exit a parse tree produced by cppParser#attributeArgumentClause.
    def exitAttributeArgumentClause(self, ctx:cppParser.AttributeArgumentClauseContext):
        pass


    # Enter a parse tree produced by cppParser#balancedTokenSeq.
    def enterBalancedTokenSeq(self, ctx:cppParser.BalancedTokenSeqContext):
        pass

    # Exit a parse tree produced by cppParser#balancedTokenSeq.
    def exitBalancedTokenSeq(self, ctx:cppParser.BalancedTokenSeqContext):
        pass


    # Enter a parse tree produced by cppParser#balancedtoken.
    def enterBalancedtoken(self, ctx:cppParser.BalancedtokenContext):
        pass

    # Exit a parse tree produced by cppParser#balancedtoken.
    def exitBalancedtoken(self, ctx:cppParser.BalancedtokenContext):
        pass


    # Enter a parse tree produced by cppParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:cppParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by cppParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:cppParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by cppParser#initDeclarator.
    def enterInitDeclarator(self, ctx:cppParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#initDeclarator.
    def exitInitDeclarator(self, ctx:cppParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#declarator.
    def enterDeclarator(self, ctx:cppParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#declarator.
    def exitDeclarator(self, ctx:cppParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#pointerDeclarator.
    def enterPointerDeclarator(self, ctx:cppParser.PointerDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#pointerDeclarator.
    def exitPointerDeclarator(self, ctx:cppParser.PointerDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#noPointerDeclarator.
    def enterNoPointerDeclarator(self, ctx:cppParser.NoPointerDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#noPointerDeclarator.
    def exitNoPointerDeclarator(self, ctx:cppParser.NoPointerDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#parametersAndQualifiers.
    def enterParametersAndQualifiers(self, ctx:cppParser.ParametersAndQualifiersContext):
        pass

    # Exit a parse tree produced by cppParser#parametersAndQualifiers.
    def exitParametersAndQualifiers(self, ctx:cppParser.ParametersAndQualifiersContext):
        pass


    # Enter a parse tree produced by cppParser#trailingReturnType.
    def enterTrailingReturnType(self, ctx:cppParser.TrailingReturnTypeContext):
        pass

    # Exit a parse tree produced by cppParser#trailingReturnType.
    def exitTrailingReturnType(self, ctx:cppParser.TrailingReturnTypeContext):
        pass


    # Enter a parse tree produced by cppParser#pointerOperator.
    def enterPointerOperator(self, ctx:cppParser.PointerOperatorContext):
        pass

    # Exit a parse tree produced by cppParser#pointerOperator.
    def exitPointerOperator(self, ctx:cppParser.PointerOperatorContext):
        pass


    # Enter a parse tree produced by cppParser#cvqualifierseq.
    def enterCvqualifierseq(self, ctx:cppParser.CvqualifierseqContext):
        pass

    # Exit a parse tree produced by cppParser#cvqualifierseq.
    def exitCvqualifierseq(self, ctx:cppParser.CvqualifierseqContext):
        pass


    # Enter a parse tree produced by cppParser#cvQualifier.
    def enterCvQualifier(self, ctx:cppParser.CvQualifierContext):
        pass

    # Exit a parse tree produced by cppParser#cvQualifier.
    def exitCvQualifier(self, ctx:cppParser.CvQualifierContext):
        pass


    # Enter a parse tree produced by cppParser#refqualifier.
    def enterRefqualifier(self, ctx:cppParser.RefqualifierContext):
        pass

    # Exit a parse tree produced by cppParser#refqualifier.
    def exitRefqualifier(self, ctx:cppParser.RefqualifierContext):
        pass


    # Enter a parse tree produced by cppParser#declaratorid.
    def enterDeclaratorid(self, ctx:cppParser.DeclaratoridContext):
        pass

    # Exit a parse tree produced by cppParser#declaratorid.
    def exitDeclaratorid(self, ctx:cppParser.DeclaratoridContext):
        pass


    # Enter a parse tree produced by cppParser#theTypeId.
    def enterTheTypeId(self, ctx:cppParser.TheTypeIdContext):
        pass

    # Exit a parse tree produced by cppParser#theTypeId.
    def exitTheTypeId(self, ctx:cppParser.TheTypeIdContext):
        pass


    # Enter a parse tree produced by cppParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:cppParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:cppParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#pointerAbstractDeclarator.
    def enterPointerAbstractDeclarator(self, ctx:cppParser.PointerAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#pointerAbstractDeclarator.
    def exitPointerAbstractDeclarator(self, ctx:cppParser.PointerAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#noPointerAbstractDeclarator.
    def enterNoPointerAbstractDeclarator(self, ctx:cppParser.NoPointerAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#noPointerAbstractDeclarator.
    def exitNoPointerAbstractDeclarator(self, ctx:cppParser.NoPointerAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#abstractPackDeclarator.
    def enterAbstractPackDeclarator(self, ctx:cppParser.AbstractPackDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#abstractPackDeclarator.
    def exitAbstractPackDeclarator(self, ctx:cppParser.AbstractPackDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#noPointerAbstractPackDeclarator.
    def enterNoPointerAbstractPackDeclarator(self, ctx:cppParser.NoPointerAbstractPackDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#noPointerAbstractPackDeclarator.
    def exitNoPointerAbstractPackDeclarator(self, ctx:cppParser.NoPointerAbstractPackDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#parameterDeclarationClause.
    def enterParameterDeclarationClause(self, ctx:cppParser.ParameterDeclarationClauseContext):
        pass

    # Exit a parse tree produced by cppParser#parameterDeclarationClause.
    def exitParameterDeclarationClause(self, ctx:cppParser.ParameterDeclarationClauseContext):
        pass


    # Enter a parse tree produced by cppParser#parameterDeclarationList.
    def enterParameterDeclarationList(self, ctx:cppParser.ParameterDeclarationListContext):
        pass

    # Exit a parse tree produced by cppParser#parameterDeclarationList.
    def exitParameterDeclarationList(self, ctx:cppParser.ParameterDeclarationListContext):
        pass


    # Enter a parse tree produced by cppParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:cppParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:cppParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:cppParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by cppParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:cppParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by cppParser#functionBody.
    def enterFunctionBody(self, ctx:cppParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by cppParser#functionBody.
    def exitFunctionBody(self, ctx:cppParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by cppParser#initializer.
    def enterInitializer(self, ctx:cppParser.InitializerContext):
        pass

    # Exit a parse tree produced by cppParser#initializer.
    def exitInitializer(self, ctx:cppParser.InitializerContext):
        pass


    # Enter a parse tree produced by cppParser#braceOrEqualInitializer.
    def enterBraceOrEqualInitializer(self, ctx:cppParser.BraceOrEqualInitializerContext):
        pass

    # Exit a parse tree produced by cppParser#braceOrEqualInitializer.
    def exitBraceOrEqualInitializer(self, ctx:cppParser.BraceOrEqualInitializerContext):
        pass


    # Enter a parse tree produced by cppParser#initializerClause.
    def enterInitializerClause(self, ctx:cppParser.InitializerClauseContext):
        pass

    # Exit a parse tree produced by cppParser#initializerClause.
    def exitInitializerClause(self, ctx:cppParser.InitializerClauseContext):
        pass


    # Enter a parse tree produced by cppParser#initializerList.
    def enterInitializerList(self, ctx:cppParser.InitializerListContext):
        pass

    # Exit a parse tree produced by cppParser#initializerList.
    def exitInitializerList(self, ctx:cppParser.InitializerListContext):
        pass


    # Enter a parse tree produced by cppParser#bracedInitList.
    def enterBracedInitList(self, ctx:cppParser.BracedInitListContext):
        pass

    # Exit a parse tree produced by cppParser#bracedInitList.
    def exitBracedInitList(self, ctx:cppParser.BracedInitListContext):
        pass


    # Enter a parse tree produced by cppParser#className.
    def enterClassName(self, ctx:cppParser.ClassNameContext):
        pass

    # Exit a parse tree produced by cppParser#className.
    def exitClassName(self, ctx:cppParser.ClassNameContext):
        pass


    # Enter a parse tree produced by cppParser#classSpecifier.
    def enterClassSpecifier(self, ctx:cppParser.ClassSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#classSpecifier.
    def exitClassSpecifier(self, ctx:cppParser.ClassSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#classHead.
    def enterClassHead(self, ctx:cppParser.ClassHeadContext):
        pass

    # Exit a parse tree produced by cppParser#classHead.
    def exitClassHead(self, ctx:cppParser.ClassHeadContext):
        pass


    # Enter a parse tree produced by cppParser#classHeadName.
    def enterClassHeadName(self, ctx:cppParser.ClassHeadNameContext):
        pass

    # Exit a parse tree produced by cppParser#classHeadName.
    def exitClassHeadName(self, ctx:cppParser.ClassHeadNameContext):
        pass


    # Enter a parse tree produced by cppParser#classVirtSpecifier.
    def enterClassVirtSpecifier(self, ctx:cppParser.ClassVirtSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#classVirtSpecifier.
    def exitClassVirtSpecifier(self, ctx:cppParser.ClassVirtSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#classKey.
    def enterClassKey(self, ctx:cppParser.ClassKeyContext):
        pass

    # Exit a parse tree produced by cppParser#classKey.
    def exitClassKey(self, ctx:cppParser.ClassKeyContext):
        pass


    # Enter a parse tree produced by cppParser#memberSpecification.
    def enterMemberSpecification(self, ctx:cppParser.MemberSpecificationContext):
        pass

    # Exit a parse tree produced by cppParser#memberSpecification.
    def exitMemberSpecification(self, ctx:cppParser.MemberSpecificationContext):
        pass


    # Enter a parse tree produced by cppParser#memberdeclaration.
    def enterMemberdeclaration(self, ctx:cppParser.MemberdeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#memberdeclaration.
    def exitMemberdeclaration(self, ctx:cppParser.MemberdeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#memberDeclaratorList.
    def enterMemberDeclaratorList(self, ctx:cppParser.MemberDeclaratorListContext):
        pass

    # Exit a parse tree produced by cppParser#memberDeclaratorList.
    def exitMemberDeclaratorList(self, ctx:cppParser.MemberDeclaratorListContext):
        pass


    # Enter a parse tree produced by cppParser#memberDeclarator.
    def enterMemberDeclarator(self, ctx:cppParser.MemberDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#memberDeclarator.
    def exitMemberDeclarator(self, ctx:cppParser.MemberDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#virtualSpecifierSeq.
    def enterVirtualSpecifierSeq(self, ctx:cppParser.VirtualSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cppParser#virtualSpecifierSeq.
    def exitVirtualSpecifierSeq(self, ctx:cppParser.VirtualSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cppParser#virtualSpecifier.
    def enterVirtualSpecifier(self, ctx:cppParser.VirtualSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#virtualSpecifier.
    def exitVirtualSpecifier(self, ctx:cppParser.VirtualSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#pureSpecifier.
    def enterPureSpecifier(self, ctx:cppParser.PureSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#pureSpecifier.
    def exitPureSpecifier(self, ctx:cppParser.PureSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#baseClause.
    def enterBaseClause(self, ctx:cppParser.BaseClauseContext):
        pass

    # Exit a parse tree produced by cppParser#baseClause.
    def exitBaseClause(self, ctx:cppParser.BaseClauseContext):
        pass


    # Enter a parse tree produced by cppParser#baseSpecifierList.
    def enterBaseSpecifierList(self, ctx:cppParser.BaseSpecifierListContext):
        pass

    # Exit a parse tree produced by cppParser#baseSpecifierList.
    def exitBaseSpecifierList(self, ctx:cppParser.BaseSpecifierListContext):
        pass


    # Enter a parse tree produced by cppParser#baseSpecifier.
    def enterBaseSpecifier(self, ctx:cppParser.BaseSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#baseSpecifier.
    def exitBaseSpecifier(self, ctx:cppParser.BaseSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#classOrDeclType.
    def enterClassOrDeclType(self, ctx:cppParser.ClassOrDeclTypeContext):
        pass

    # Exit a parse tree produced by cppParser#classOrDeclType.
    def exitClassOrDeclType(self, ctx:cppParser.ClassOrDeclTypeContext):
        pass


    # Enter a parse tree produced by cppParser#baseTypeSpecifier.
    def enterBaseTypeSpecifier(self, ctx:cppParser.BaseTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#baseTypeSpecifier.
    def exitBaseTypeSpecifier(self, ctx:cppParser.BaseTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:cppParser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:cppParser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#conversionFunctionId.
    def enterConversionFunctionId(self, ctx:cppParser.ConversionFunctionIdContext):
        pass

    # Exit a parse tree produced by cppParser#conversionFunctionId.
    def exitConversionFunctionId(self, ctx:cppParser.ConversionFunctionIdContext):
        pass


    # Enter a parse tree produced by cppParser#conversionTypeId.
    def enterConversionTypeId(self, ctx:cppParser.ConversionTypeIdContext):
        pass

    # Exit a parse tree produced by cppParser#conversionTypeId.
    def exitConversionTypeId(self, ctx:cppParser.ConversionTypeIdContext):
        pass


    # Enter a parse tree produced by cppParser#conversionDeclarator.
    def enterConversionDeclarator(self, ctx:cppParser.ConversionDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#conversionDeclarator.
    def exitConversionDeclarator(self, ctx:cppParser.ConversionDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#constructorInitializer.
    def enterConstructorInitializer(self, ctx:cppParser.ConstructorInitializerContext):
        pass

    # Exit a parse tree produced by cppParser#constructorInitializer.
    def exitConstructorInitializer(self, ctx:cppParser.ConstructorInitializerContext):
        pass


    # Enter a parse tree produced by cppParser#memInitializerList.
    def enterMemInitializerList(self, ctx:cppParser.MemInitializerListContext):
        pass

    # Exit a parse tree produced by cppParser#memInitializerList.
    def exitMemInitializerList(self, ctx:cppParser.MemInitializerListContext):
        pass


    # Enter a parse tree produced by cppParser#memInitializer.
    def enterMemInitializer(self, ctx:cppParser.MemInitializerContext):
        pass

    # Exit a parse tree produced by cppParser#memInitializer.
    def exitMemInitializer(self, ctx:cppParser.MemInitializerContext):
        pass


    # Enter a parse tree produced by cppParser#meminitializerid.
    def enterMeminitializerid(self, ctx:cppParser.MeminitializeridContext):
        pass

    # Exit a parse tree produced by cppParser#meminitializerid.
    def exitMeminitializerid(self, ctx:cppParser.MeminitializeridContext):
        pass


    # Enter a parse tree produced by cppParser#operatorFunctionId.
    def enterOperatorFunctionId(self, ctx:cppParser.OperatorFunctionIdContext):
        pass

    # Exit a parse tree produced by cppParser#operatorFunctionId.
    def exitOperatorFunctionId(self, ctx:cppParser.OperatorFunctionIdContext):
        pass


    # Enter a parse tree produced by cppParser#literalOperatorId.
    def enterLiteralOperatorId(self, ctx:cppParser.LiteralOperatorIdContext):
        pass

    # Exit a parse tree produced by cppParser#literalOperatorId.
    def exitLiteralOperatorId(self, ctx:cppParser.LiteralOperatorIdContext):
        pass


    # Enter a parse tree produced by cppParser#templateDeclaration.
    def enterTemplateDeclaration(self, ctx:cppParser.TemplateDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#templateDeclaration.
    def exitTemplateDeclaration(self, ctx:cppParser.TemplateDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#templateparameterList.
    def enterTemplateparameterList(self, ctx:cppParser.TemplateparameterListContext):
        pass

    # Exit a parse tree produced by cppParser#templateparameterList.
    def exitTemplateparameterList(self, ctx:cppParser.TemplateparameterListContext):
        pass


    # Enter a parse tree produced by cppParser#templateParameter.
    def enterTemplateParameter(self, ctx:cppParser.TemplateParameterContext):
        pass

    # Exit a parse tree produced by cppParser#templateParameter.
    def exitTemplateParameter(self, ctx:cppParser.TemplateParameterContext):
        pass


    # Enter a parse tree produced by cppParser#typeParameter.
    def enterTypeParameter(self, ctx:cppParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by cppParser#typeParameter.
    def exitTypeParameter(self, ctx:cppParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by cppParser#simpleTemplateId.
    def enterSimpleTemplateId(self, ctx:cppParser.SimpleTemplateIdContext):
        pass

    # Exit a parse tree produced by cppParser#simpleTemplateId.
    def exitSimpleTemplateId(self, ctx:cppParser.SimpleTemplateIdContext):
        pass


    # Enter a parse tree produced by cppParser#templateId.
    def enterTemplateId(self, ctx:cppParser.TemplateIdContext):
        pass

    # Exit a parse tree produced by cppParser#templateId.
    def exitTemplateId(self, ctx:cppParser.TemplateIdContext):
        pass


    # Enter a parse tree produced by cppParser#templateName.
    def enterTemplateName(self, ctx:cppParser.TemplateNameContext):
        pass

    # Exit a parse tree produced by cppParser#templateName.
    def exitTemplateName(self, ctx:cppParser.TemplateNameContext):
        pass


    # Enter a parse tree produced by cppParser#templateArgumentList.
    def enterTemplateArgumentList(self, ctx:cppParser.TemplateArgumentListContext):
        pass

    # Exit a parse tree produced by cppParser#templateArgumentList.
    def exitTemplateArgumentList(self, ctx:cppParser.TemplateArgumentListContext):
        pass


    # Enter a parse tree produced by cppParser#templateArgument.
    def enterTemplateArgument(self, ctx:cppParser.TemplateArgumentContext):
        pass

    # Exit a parse tree produced by cppParser#templateArgument.
    def exitTemplateArgument(self, ctx:cppParser.TemplateArgumentContext):
        pass


    # Enter a parse tree produced by cppParser#typeNameSpecifier.
    def enterTypeNameSpecifier(self, ctx:cppParser.TypeNameSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#typeNameSpecifier.
    def exitTypeNameSpecifier(self, ctx:cppParser.TypeNameSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#explicitInstantiation.
    def enterExplicitInstantiation(self, ctx:cppParser.ExplicitInstantiationContext):
        pass

    # Exit a parse tree produced by cppParser#explicitInstantiation.
    def exitExplicitInstantiation(self, ctx:cppParser.ExplicitInstantiationContext):
        pass


    # Enter a parse tree produced by cppParser#explicitSpecialization.
    def enterExplicitSpecialization(self, ctx:cppParser.ExplicitSpecializationContext):
        pass

    # Exit a parse tree produced by cppParser#explicitSpecialization.
    def exitExplicitSpecialization(self, ctx:cppParser.ExplicitSpecializationContext):
        pass


    # Enter a parse tree produced by cppParser#tryBlock.
    def enterTryBlock(self, ctx:cppParser.TryBlockContext):
        pass

    # Exit a parse tree produced by cppParser#tryBlock.
    def exitTryBlock(self, ctx:cppParser.TryBlockContext):
        pass


    # Enter a parse tree produced by cppParser#functionTryBlock.
    def enterFunctionTryBlock(self, ctx:cppParser.FunctionTryBlockContext):
        pass

    # Exit a parse tree produced by cppParser#functionTryBlock.
    def exitFunctionTryBlock(self, ctx:cppParser.FunctionTryBlockContext):
        pass


    # Enter a parse tree produced by cppParser#handlerSeq.
    def enterHandlerSeq(self, ctx:cppParser.HandlerSeqContext):
        pass

    # Exit a parse tree produced by cppParser#handlerSeq.
    def exitHandlerSeq(self, ctx:cppParser.HandlerSeqContext):
        pass


    # Enter a parse tree produced by cppParser#handler.
    def enterHandler(self, ctx:cppParser.HandlerContext):
        pass

    # Exit a parse tree produced by cppParser#handler.
    def exitHandler(self, ctx:cppParser.HandlerContext):
        pass


    # Enter a parse tree produced by cppParser#exceptionDeclaration.
    def enterExceptionDeclaration(self, ctx:cppParser.ExceptionDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#exceptionDeclaration.
    def exitExceptionDeclaration(self, ctx:cppParser.ExceptionDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#throwExpression.
    def enterThrowExpression(self, ctx:cppParser.ThrowExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#throwExpression.
    def exitThrowExpression(self, ctx:cppParser.ThrowExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#exceptionSpecification.
    def enterExceptionSpecification(self, ctx:cppParser.ExceptionSpecificationContext):
        pass

    # Exit a parse tree produced by cppParser#exceptionSpecification.
    def exitExceptionSpecification(self, ctx:cppParser.ExceptionSpecificationContext):
        pass


    # Enter a parse tree produced by cppParser#dynamicExceptionSpecification.
    def enterDynamicExceptionSpecification(self, ctx:cppParser.DynamicExceptionSpecificationContext):
        pass

    # Exit a parse tree produced by cppParser#dynamicExceptionSpecification.
    def exitDynamicExceptionSpecification(self, ctx:cppParser.DynamicExceptionSpecificationContext):
        pass


    # Enter a parse tree produced by cppParser#typeIdList.
    def enterTypeIdList(self, ctx:cppParser.TypeIdListContext):
        pass

    # Exit a parse tree produced by cppParser#typeIdList.
    def exitTypeIdList(self, ctx:cppParser.TypeIdListContext):
        pass


    # Enter a parse tree produced by cppParser#noeExceptSpecification.
    def enterNoeExceptSpecification(self, ctx:cppParser.NoeExceptSpecificationContext):
        pass

    # Exit a parse tree produced by cppParser#noeExceptSpecification.
    def exitNoeExceptSpecification(self, ctx:cppParser.NoeExceptSpecificationContext):
        pass


    # Enter a parse tree produced by cppParser#theOperator.
    def enterTheOperator(self, ctx:cppParser.TheOperatorContext):
        pass

    # Exit a parse tree produced by cppParser#theOperator.
    def exitTheOperator(self, ctx:cppParser.TheOperatorContext):
        pass


    # Enter a parse tree produced by cppParser#literal.
    def enterLiteral(self, ctx:cppParser.LiteralContext):
        pass

    # Exit a parse tree produced by cppParser#literal.
    def exitLiteral(self, ctx:cppParser.LiteralContext):
        pass


