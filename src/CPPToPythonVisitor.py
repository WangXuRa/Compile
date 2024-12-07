from CPPParserVisitor import CPPParserVisitor
from CPPParser import CPPParser
from typing import List, Dict, Any, Optional

class CPPToPythonVisitor(CPPParserVisitor):
    def __init__(self, type_converter=None, expression_converter=None, 
                 statement_converter=None, class_converter=None, template_converter=None):
        super().__init__()
        self.type_converter = type_converter
        self.expression_converter = expression_converter
        self.statement_converter = statement_converter
        self.class_converter = class_converter
        self.template_converter = template_converter
        self.reset()
    
    def reset(self):
        """Reset the visitor's state"""
        self.indent_level: int = 0
        self.output_lines: List[str] = []
        self.current_class: Optional[str] = None
        self.current_function: Optional[str] = None
        self.symbol_table: Dict[str, Any] = {}

    def set_converters(self, type_converter, expression_converter, 
                      statement_converter, class_converter, template_converter):
        """Set all converters"""
        self.type_converter = type_converter
        self.expression_converter = expression_converter
        self.statement_converter = statement_converter
        self.class_converter = class_converter
        self.template_converter = template_converter

    # Basic utilities
    def get_output(self) -> str:
        return "\n".join(self.output_lines)
    
    def indent(self) -> str:
        return "    " * self.indent_level

    # Statement handling
    def visitCompoundStatement(self, ctx: CPPParser.CompoundStatementContext):
        return self.statement_converter.convert_compound_statement(ctx, self)

    def visitStatement(self, ctx: CPPParser.StatementContext):
        return self.statement_converter.convert_statement(ctx, self)

    def visitReturnStatement(self, ctx: CPPParser.ReturnStatementContext):
        return self.statement_converter.convert_return_statement(ctx, self)

    def visitIfStatement(self, ctx: CPPParser.IfStatementContext):
        return self.statement_converter.convert_if_statement(ctx, self)

    def visitWhileStatement(self, ctx: CPPParser.WhileStatementContext):
        return self.statement_converter.convert_while_statement(ctx, self)

    def visitForStatement(self, ctx: CPPParser.ForStatementContext):
        return self.statement_converter.convert_for_statement(ctx, self)

    # Expression handling
    def visitExpression(self, ctx: CPPParser.ExpressionContext):
        return self.expression_converter.convert_expression(ctx, self)

    def visitVariableDeclaration(self, ctx: CPPParser.VariableDeclarationContext):
        return self.statement_converter.convert_variable_declaration(ctx, self)

    # Class handling
    def visitClassDefinition(self, ctx: CPPParser.ClassDefinitionContext):
        return self.class_converter.convert_class_definition(ctx, self)

    def visitMemberAccess(self, ctx: CPPParser.MemberAccessContext):
        return self.expression_converter.convert_member_access(ctx, self)

    def visitMethodCall(self, ctx: CPPParser.MethodCallContext):
        return self.expression_converter.convert_method_call(ctx, self)

    # Template handling
    def visitTemplateDeclaration(self, ctx: CPPParser.TemplateDeclarationContext):
        return self.template_converter.convert_template_declaration(ctx, self)

    def visitTemplateParameter(self, ctx: CPPParser.TemplateParameterContext):
        return self.template_converter.convert_template_parameter(ctx, self)

    def visitTemplateArgument(self, ctx: CPPParser.TemplateArgumentContext):
        return self.template_converter.convert_template_argument(ctx, self)

    # Function handling
    def visitFunctionDefinition(self, ctx: CPPParser.FunctionDefinitionContext):
        return self.class_converter.convert_function_definition(ctx, self)

    # Utility methods for the transpiler
    def get_includes(self, tree) -> List[str]:
        """Extract include directives from the AST"""
        includes = []
        if hasattr(tree, 'includeDirective'):
            for include in tree.includeDirective():
                includes.append(include.HeaderName().getText().strip('<>"'))
        return includes

    def get_namespaces(self, tree) -> List[str]:
        """Extract namespace declarations from the AST"""
        namespaces = []
        if hasattr(tree, 'namespaceDefinition'):
            for ns in tree.namespaceDefinition():
                namespaces.append(ns.Identifier().getText())
        return namespaces

    def add_line(self, line: str):
        """Add a line of code with proper indentation"""
        self.output_lines.append(f"{self.indent()}{line}")

    def increase_indent(self):
        """Increase indentation level"""
        self.indent_level += 1

    def decrease_indent(self):
        """Decrease indentation level"""
        self.indent_level -= 1