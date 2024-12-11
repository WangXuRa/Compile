from antlr4 import *
from CPPParser import CPPParser
from CPPParserVisitor import CPPParserVisitor

class ClassConverter:
    """
    Handles conversion of C++ classes and inheritance to Python classes.
    """
    def convert_class(self, class_name, base_classes, class_body):
        """
        Converts C++ class to Python class.
        Example:
        class MyClass : public Base { ... }
        ->
        class MyClass(Base): ...
        """
        result = []

        # Class header
        base_class_str = f"({', '.join(base_classes)})" if base_classes else ""
        result.append(f"class {class_name}{base_class_str}:")

        # Add class body
        if class_body:
            result.extend([f"    {line}" for line in class_body])
        else:
            result.append("    pass")

        return result

    def convert_member_variable(self, access_modifier, var_type, var_name):
        """
        Converts C++ member variable to Python instance variable.
        Example:
        private int x;
        ->
        self._x = None  # type: int
        """
        modifier_prefix = "_" if access_modifier in ("private", "protected") else ""
        return f"{modifier_prefix}{var_name} = None  # type: {var_type}"

    def convert_member_function(self, func_name, params, body, return_type=None):
        """
        Converts C++ member function to Python method.
        Example:
        int getValue() { return value; }
        ->
        def get_value(self) -> int:
            return self._value
        """
        param_list = ", ".join(["self"] + [f"{p}: {t}" for p, t in params])
        result = [f"def {func_name}({param_list}):"]

        if body:
            result.extend([f"    {line}" for line in body])
        else:
            result.append("    pass")

        return result

    def handle_pointer(self):
        """
        Raises an error for pointers as Python does not support them directly.
        """
        raise NotImplementedError("Pointers are not supported in Python")
