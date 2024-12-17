from typing import Set, List
from antlr4 import ParserRuleContext
from translation.Node import Node

class IncludeConverter:
    """Handles C++ include directives and converts them to Python imports"""
    
    # Map of C++ headers to Python imports
    INCLUDE_MAP = {
        "iostream": [
            "from sys import stdout",
            "print = stdout.write"
        ],
        "vector": [
            "from typing import List"
        ],
        "string": [
            "from typing import String"
        ],
        "map": [
            "from typing import Dict"
        ],
        "memory": [
            "from typing import Optional"
        ],
        "cstring": [
            "from typing import List"
        ],
        "algorithm": [
            "from typing import List",
            "from itertools import *"
        ],
        "set": [
            "from typing import Set"
        ],
        "queue": [
            "from collections import deque"
        ],
        "stack": [
            "from collections import deque"
        ],
        # C headers
        "stdio.h": [],  # No direct mapping needed
        "stdlib.h": [],
        "string.h": ["from typing import List"],
        "math.h": ["import math"],
        "time.h": ["import time"],
    }

    def __init__(self):
        self.processed_includes: Set[str] = set()
        self.python_imports: List[str] = []

    def convert_include(self, include_node: Node) -> List[str]:
        """Convert a single include directive to Python import(s)"""
        if include_node.node_type != "include":
            raise TypeError("Expected include node!")

        # Extract header name from the node
        header = include_node.children[0].value.strip('<>"\n')
        base_header = header.split('/')[-1].split('.')[0]

        # Check if we've already processed this include
        if base_header in self.processed_includes:
            return []

        self.processed_includes.add(base_header)

        # Get corresponding Python imports
        if base_header in self.INCLUDE_MAP:
            imports = self.INCLUDE_MAP[base_header]
            self.python_imports.extend(imports)
            return imports

        return []

    def get_all_imports(self) -> List[str]:
        """Get all processed imports in sorted order"""
        return sorted(list(set(self.python_imports)))

    def reset(self):
        """Reset the converter state"""
        self.processed_includes.clear()
        self.python_imports.clear()

    @staticmethod
    def is_system_include(include_str: str) -> bool:
        """Check if this is a system include (<>) vs local include ("")"""
        return include_str.startswith('<') and include_str.endswith('>') 