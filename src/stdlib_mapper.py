class StdLibMapper:
    """
    Maps C++ standard library components to Python equivalents.
    """
    STL_MAP = {
        "std::vector": "list",
        "std::map": "dict",
        "std::set": "set",
        "std::string": "str",
        "std::unordered_map": "dict",
        "std::unordered_set": "set"
    }

    def map_std_lib(self, cpp_type):
        """
        Maps C++ STL types to Python equivalents.
        Example:
        std::vector<int> -> list[int]
        """
        for cpp_std, py_type in self.STL_MAP.items():
            if cpp_std in cpp_type:
                # Handle template arguments
                if "<" in cpp_type and ">" in cpp_type:
                    inner_type = cpp_type[cpp_type.index("<") + 1:cpp_type.rindex(">")]
                    return f"{py_type}[{self.map_std_lib(inner_type)}]"
                return py_type
        return cpp_type  # If no match, return original type
