from antlr4 import *
from CPPParser import CPPParser
from CPPParserVisitor import CPPParserVisitor

class TemplateConverter:
    """
    Handles conversion of C++ templates to Python generic types.
    """
    def convert_template(self, template_params, class_body):
        """
        Converts C++ templates to Python generics using `typing.Generic`.
        Example:
        template <typename T>
        class MyClass { ... }
        ->
        from typing import Generic, TypeVar
        T = TypeVar('T')
        class MyClass(Generic[T]): ...
        """
        result = []

        # Import typing module
        result.append("from typing import Generic, TypeVar")

        # Define TypeVars
        type_vars = [f"{param.strip()}" for param in template_params]
        type_var_defs = [f"{param} = TypeVar('{param}')" for param in type_vars]
        result.extend(type_var_defs)

        # Define class with generics
        class_name = class_body.get('class_name')
        result.append(f"class {class_name}(Generic[{', '.join(type_vars)}]):")

        # Add class body
        body_lines = class_body.get('body', [])
        if body_lines:
            result.extend([f"    {line}" for line in body_lines])
        else:
            result.append("    pass")

        return result

    def convert_function_template(self, template_params, function_body):
        """
        Converts C++ function templates to Python generic functions.
        Example:
        template <typename T>
        T add(T a, T b) { return a + b; }
        ->
        from typing import TypeVar
        T = TypeVar('T')
        def add(a: T, b: T) -> T:
            return a + b
        """
        result = []

        # Define TypeVars
        type_vars = [f"{param.strip()}" for param in template_params]
        type_var_defs = [f"{param} = TypeVar('{param}')" for param in type_vars]
        result.extend(type_var_defs)

        # Add function definition
        func_name = function_body.get('name')
        params = function_body.get('params', [])
        return_type = function_body.get('return_type', 'Any')
        body_lines = function_body.get('body', [])

        param_list = ', '.join([f"{p}: {t}" for p, t in params])
        result.append(f"def {func_name}({param_list}) -> {return_type}:")

        if body_lines:
            result.extend([f"    {line}" for line in body_lines])
        else:
            result.append("    pass")

        return result
