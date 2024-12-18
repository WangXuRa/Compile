# C++ to Python Transpiler: Design and Implementation

### Abstract

This report presents the design and implementation of a C++ to Python source code transpiler using ANTLR4. The transpiler performs lexical analysis, parsing, and code generation to convert C++ programs into semantically equivalent Python code while maintaining Python's idioms and best practices. The system successfully handles basic C++ constructs, including control structures, functions, classes, and fundamental data types.

### Table of Contents
- [C++ to Python Transpiler: Design and Implementation](#c-to-python-transpiler-design-and-implementation)
    - [Abstract](#abstract)
    - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [1.1 Background and Motivation](#11-background-and-motivation)
    - [1.2 Project Objectives](#12-project-objectives)
    - [1.3 Scope and Limitations](#13-scope-and-limitations)
  - [2. System Architecture](#2-system-architecture)
    - [2.1 High-Level Design](#21-high-level-design)
    - [2.2 Core Components](#22-core-components)
      - [2.2.1 ANTLR4 Grammar](#221-antlr4-grammar)
      - [2.2.2 AST Node System](#222-ast-node-system)
      - [2.2.3 Translation Components](#223-translation-components)
  - [3. Implementation Details](#3-implementation-details)
    - [3.1 Lexical Analysis and Parsing](#31-lexical-analysis-and-parsing)
      - [3.1.1 Grammar Design](#311-grammar-design)
      - [3.1.2 AST Construction](#312-ast-construction)
    - [3.2 Type System](#32-type-system)
      - [3.2.1 Type Mapping](#321-type-mapping)
      - [3.2.2 Container Types](#322-container-types)
    - [3.3 Core Transpiler Implementation](#33-core-transpiler-implementation)
      - [3.3.1 CppToPythonTranspiler Class](#331-cpptopythontranspiler-class)
    - [3.4 AST Construction and Visitor Pattern](#34-ast-construction-and-visitor-pattern)
      - [3.4.1 Node System](#341-node-system)
      - [3.4.2 CPPToPythonVisitor Implementation](#342-cpptopythonvisitor-implementation)
    - [3.5 Converter Components](#35-converter-components)
      - [3.5.1 Expression Converter](#351-expression-converter)
      - [3.5.2 Declaration Converter](#352-declaration-converter)
      - [3.5.3 Statement Converter](#353-statement-converter)
      - [3.5.4 Class Converter](#354-class-converter)
      - [3.5.5 Include Converter](#355-include-converter)
    - [3.6 Translation Flow](#36-translation-flow)
    - [3.7 Error Handling](#37-error-handling)
  - [4. Testing and Validation](#4-testing-and-validation)
    - [4.1 Test Cases](#41-test-cases)
      - [4.1.1 Bubble Sort Algorithm](#411-bubble-sort-algorithm)
      - [4.1.2 KMP String Matching](#412-kmp-string-matching)
    - [4.2 Results Analysis](#42-results-analysis)
  - [5. Challenges and Solutions](#5-challenges-and-solutions)
    - [5.1 AST Construction Challenges](#51-ast-construction-challenges)
      - [5.1.1 Complex Expression Handling](#511-complex-expression-handling)
      - [5.1.2 Scope Management](#512-scope-management)
    - [5.2 Type System Challenges](#52-type-system-challenges)
      - [5.2.1 Template Translation](#521-template-translation)
      - [5.2.2 Reference and Pointer Handling](#522-reference-and-pointer-handling)
    - [5.3 Control Flow Challenges](#53-control-flow-challenges)
      - [5.3.1 Loop Translation](#531-loop-translation)
    - [5.4 Memory Management Challenges](#54-memory-management-challenges)
      - [5.4.1 Array Management](#541-array-management)
      - [5.4.2 Resource Management](#542-resource-management)
    - [5.5 Standard Library Challenges](#55-standard-library-challenges)
      - [5.5.1 IO Stream Translation](#551-io-stream-translation)
      - [5.5.2 STL Container Translation](#552-stl-container-translation)
    - [5.6 Performance Challenges](#56-performance-challenges)
      - [5.6.1 Code Optimization](#561-code-optimization)
    - [5.8 Type System and Arithmetic Operation Challenges](#58-type-system-and-arithmetic-operation-challenges)
      - [5.8.1 Integer Division and Type Conversion](#581-integer-division-and-type-conversion)
      - [5.8.2 Type Checking and Validation](#582-type-checking-and-validation)
  - [6. Future Work](#6-future-work)
    - [6.1 Planned Improvements](#61-planned-improvements)
  - [7. Conclusion](#7-conclusion)
  - [8. References](#8-references)
    - [Appendix A: Installation and Usage](#appendix-a-installation-and-usage)
      - [A.1 Environment Setup](#a1-environment-setup)
      - [A.2 Running the Transpiler](#a2-running-the-transpiler)
    - [Appendix B: Code Examples](#appendix-b-code-examples)


## 1. Introduction

### 1.1 Background and Motivation

Source code translation between programming languages is a fundamental challenge in software engineering. This project addresses the specific need for converting C++ code to Python, facilitating the migration of legacy systems and enabling cross-language development.

### 1.2 Project Objectives

- Develop a robust C++ to Python transpiler using ANTLR4
- Maintain semantic equivalence between source and target code
- Support core C++ language features
- Generate readable and maintainable Python code
- Provide clear error reporting and recovery mechanisms

### 1.3 Scope and Limitations

The current implementation focuses on:
- Basic C++ language constructs
- Standard control flow structures
- Function and class definitions
- Fundamental data types and operations

## 2. System Architecture

### 2.1 High-Level Design

The transpiler follows a four-stage pipeline:
1. Lexical Analysis
2. Parsing
3. Semantic Analysis
4. Code Generation

### 2.2 Core Components

#### 2.2.1 ANTLR4 Grammar
````python
# CPPLexer.g4 excerpt
INCLUDE      : '#include';
WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;
````

#### 2.2.2 AST Node System
````python
class Node:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []
        self.parent = None
````

#### 2.2.3 Translation Components
- ExpressionConverter
- DeclarationConverter
- StatementConverter
- ClassConverter
- FunctionConverter
- IncludeConverter

## 3. Implementation Details

### 3.1 Lexical Analysis and Parsing

#### 3.1.1 Grammar Design
````antlr
// CPPParser.g4 excerpt
program : (includeStatement)* 
          (classDefinition | functionDefinition | declaration | statement)* ;

classDefinition
    : CLASS ID LBRACE classBody RBRACE SEMICOLON
    ;
````

#### 3.1.2 AST Construction
The parser generates an Abstract Syntax Tree (AST) that represents the program structure hierarchically.

### 3.2 Type System

#### 3.2.1 Type Mapping
````python
TYPE_MAPPING = {
    'int': 'int',
    'char': 'str',
    'bool': 'bool',
    'std::string': 'str',
    'void': 'None'
}
````

#### 3.2.2 Container Types
- Arrays → Python Lists
- Vectors → Python Lists
- Maps → Python Dictionaries

### 3.3 Core Transpiler Implementation

#### 3.3.1 CppToPythonTranspiler Class
````python
class CppToPythonTranspiler:
    def __init__(self):
        self.include_converter = IncludeConverter()
        self.expression_converter = ExpressionConverter()
        self.declaration_converter = DeclarationConverter()
        self.statement_converter = StatementConverter()
        self.class_converter = ClassConverter()
        self.function_converter = FunctionConverter()
        
    def transpile(self, cpp_code: str) -> str:
        # 1. Create input stream
        input_stream = InputStream(cpp_code)
        
        # 2. Create lexer
        lexer = CPPLexer(input_stream)
        stream = CommonTokenStream(lexer)
        
        # 3. Create parser and build AST
        parser = CPPParser(stream)
        tree = parser.program()
        
        # 4. Visit AST and generate Python code
        visitor = CPPToPythonVisitor(parser)
        return visitor.visit(tree)
````

The transpiler class orchestrates the entire translation process through these main steps:
1. Lexical analysis of C++ code
2. Parsing and AST construction
3. AST traversal and Python code generation
4. Code optimization and formatting

### 3.4 AST Construction and Visitor Pattern

#### 3.4.1 Node System
````python
class Node:
    def __init__(self, node_type, value=None):
        self.node_type = node_type  # e.g., "functionDefinition", "expression"
        self.value = value          # Actual value for literals/identifiers
        self.children = []          # Child nodes
        self.parent = None          # Parent node reference
        self.line_number = None     # Source code line number
        self.symbol_table = {}      # Local symbol table for scope
        
    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)
````

#### 3.4.2 CPPToPythonVisitor Implementation
````python
class CPPToPythonVisitor(CPPParserVisitor):
    def __init__(self, parser):
        self.parser = parser
        self.symbol_table = {}
        self.current_scope = []
        self.indent_level = 0
        self.output_lines = []
        
    def visitFunctionDefinition(self, ctx):
        # Create function node
        func_node = Node("functionDefinition")
        
        # Process return type
        return_type = self.visit(ctx.typeSpecifier())
        func_node.add_child(return_type)
        
        # Process function name
        name_node = Node("identifier", ctx.ID().getText())
        func_node.add_child(name_node)
        
        # Process parameters
        if ctx.parameterList():
            params = self.visit(ctx.parameterList())
            func_node.add_child(params)
            
        # Process function body
        body = self.visit(ctx.compoundStatement())
        func_node.add_child(body)
        
        return func_node
````

### 3.5 Converter Components

#### 3.5.1 Expression Converter
Handles all C++ expressions and operators.

````python
class ExpressionConverter:
    def convert_binary_operation(self, node, current_vars):
        left = self.convert_expression(node.children[0], current_vars)
        operator = node.value
        right = self.convert_expression(node.children[1], current_vars)
        
        # Handle special cases
        if operator == '<<' and 'cout' in left:
            return f"print({right}, sep='', end='')"
            
        # Normal binary operations
        op_map = {
            '+': '+', '-': '-', '*': '*', '/': '/',
            '==': '==', '!=': '!=', '<': '<', '>': '>'
        }
        return f"{left} {op_map[operator]} {right}"
        
    def convert_increment_decrement(self, node, current_vars):
        var_name = node.children[0].value
        if node.value == '++':
            return f"(({var_name}:={var_name}+1)-1)"
        else:
            return f"(({var_name}:={var_name}-1)+1)"
````

#### 3.5.2 Declaration Converter
Manages variable declarations and initializations.

````python
class DeclarationConverter:
    def convert_declaration(self, node, current_vars):
        type_name = node.children[0].value
        var_name = node.children[1].value
        
        # Handle array declarations
        if '[' in var_name:
            base_name, size = self.parse_array_declaration(var_name)
            return f"{base_name} = [0] * {size}"
            
        # Handle basic declarations
        if len(node.children) > 2:  # Has initializer
            initializer = self.convert_initializer(node.children[2])
            return f"{var_name} = {initializer}"
        else:
            return f"{var_name} = None"
````

#### 3.5.3 Statement Converter
Processes control flow and other statements.

````python
class StatementConverter:
    def convert_if_statement(self, node, current_vars):
        condition = self.expression_converter.convert_expression(
            node.children[0], current_vars)
        
        then_body = self.convert_compound_statement(
            node.children[1], current_vars)
            
        python_code = [f"if {condition}:"]
        python_code.extend(then_body)
        
        # Handle else clause if present
        if len(node.children) > 2:
            else_body = self.convert_compound_statement(
                node.children[2], current_vars)
            python_code.append("else:")
            python_code.extend(else_body)
            
        return python_code
        
    def convert_for_loop(self, node, current_vars):
        # Extract loop components
        init = node.children[0]
        condition = node.children[1]
        increment = node.children[2]
        body = node.children[3]
        
        # Convert to Python range-based for loop
        if self.is_countable_loop(init, condition, increment):
            return self.convert_to_range_loop(
                init, condition, increment, body)
        else:
            return self.convert_to_while_loop(
                init, condition, increment, body)
````

#### 3.5.4 Class Converter
Handles class definitions and methods.

````python
class ClassConverter:
    def convert_class(self, node, current_vars):
        class_name = node.children[0].value
        python_code = [f"class {class_name}:"]
        
        # Process class body
        for child in node.children[1].children:
            if child.node_type == "functionDefinition":
                method_code = self.convert_method(child)
                python_code.extend(method_code)
            elif child.node_type == "declaration":
                field_code = self.convert_field(child)
                python_code.extend(field_code)
                
        return python_code
        
    def convert_method(self, node):
        # Add self parameter
        params = ["self"]
        if node.children[2].children:  # Has parameters
            params.extend(self.convert_parameters(node.children[2]))
            
        method_name = node.children[1].value
        body = self.convert_method_body(node.children[3])
        
        return [
            f"def {method_name}({', '.join(params)}):",
            *body
        ]
````

#### 3.5.5 Include Converter
Manages header file imports and standard library mappings.

````python
class IncludeConverter:
    INCLUDE_MAP = {
        "iostream": [
            "from sys import stdout",
            "print = stdout.write"
        ],
        "vector": ["from typing import List"],
        "string": ["from typing import String"],
        "map": ["from typing import Dict"],
        "memory": ["from typing import Optional"],
        "algorithm": [
            "from typing import List",
            "from itertools import *"
        ]
    }
    
    def convert_include(self, node):
        header = node.value.strip('<>')
        if header in self.INCLUDE_MAP:
            return self.INCLUDE_MAP[header]
        return []
````

### 3.6 Translation Flow

1. **Source Code Parsing**
   - Lexical analysis breaks code into tokens
   - Parser builds AST using grammar rules
   - AST nodes are created with type and scope information

2. **Scope Analysis**
   - Symbol table tracks variables and their types
   - Scope stack manages nested blocks
   - Type inference for variables and expressions

3. **Type Resolution**
   - C++ types are mapped to Python equivalents
   - Container types are transformed
   - Type checking for operations

4. **Code Generation**
   - AST is traversed using visitor pattern
   - Each node type has specific conversion logic
   - Python code is generated with proper indentation

5. **Optimization**
   - Redundant code elimination
   - Expression simplification
   - Import optimization

### 3.7 Error Handling

````python
class TranspilerError(Exception):
    def __init__(self, message, line_number=None):
        self.message = message
        self.line_number = line_number
        
class ErrorListener(ANTLRErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise TranspilerError(
            f"Syntax error at line {line}, column {column}: {msg}",
            line
        )
````


## 4. Testing and Validation

### 4.1 Test Cases

#### 4.1.1 Bubble Sort Algorithm
````cpp
// test_bubbleSort.cpp
int main() {
    int num;
    int a[100];
    std::cout << "Input the array length: ";
    std::cin >> num;
    // ... sorting implementation
}
````

#### 4.1.2 KMP String Matching
Tests complex string operations and array manipulations.

### 4.2 Results Analysis

Performance metrics and translation accuracy for different test cases.

## 5. Challenges and Solutions

### 5.1 AST Construction Challenges

#### 5.1.1 Complex Expression Handling
**Challenge:** C++ expressions can be deeply nested and have complex operator precedence rules.

**Example:**
````cpp
a = b++ * (c-- + d) / e--;  // Complex expression with multiple operators
````

**Solution:**
1. Implemented a precedence-aware expression parser
````python
class ExpressionConverter:
    def handle_complex_expression(self, node):
        # Track operator precedence
        PRECEDENCE = {
            '++': 1, '--': 1,
            '*': 2, '/': 2,
            '+': 3, '-': 3,
            '=': 4
        }
        
        def parse_with_precedence(expr_node, min_precedence):
            left = self.parse_atom(expr_node)
            while True:
                op = self.get_next_operator()
                if not op or PRECEDENCE[op] < min_precedence:
                    break
                right = parse_with_precedence(
                    expr_node.right, 
                    PRECEDENCE[op]
                )
                left = self.combine(left, op, right)
            return left
````

#### 5.1.2 Scope Management
**Challenge:** Maintaining correct variable scope and handling nested blocks.

**Solution:**
1. Implemented a scope stack system
````python
class ScopeManager:
    def __init__(self):
        self.scope_stack = [{}]  # Stack of symbol tables
        self.current_scope = 0
        
    def enter_scope(self):
        self.scope_stack.append({})
        self.current_scope += 1
        
    def exit_scope(self):
        self.scope_stack.pop()
        self.current_scope -= 1
        
    def add_symbol(self, name, symbol_type):
        self.scope_stack[self.current_scope][name] = symbol_type
        
    def lookup_symbol(self, name):
        # Search from inner to outer scope
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        return None
````

### 5.2 Type System Challenges

#### 5.2.1 Template Translation
**Challenge:** C++ templates have no direct equivalent in Python.

**Example:**
````cpp
template<typename T>
class Vector {
    T* data;
    size_t size;
public:
    void push_back(T element);
};
````

**Solution:**
1. Generic type translation using Python's typing module
````python
def convert_template_class(self, node):
    class_name = node.name
    type_params = node.template_params
    
    return [
        "from typing import TypeVar, Generic",
        f"T = TypeVar('T')",
        f"class {class_name}(Generic[T]):",
        "    def __init__(self):",
        "        self.data: List[T] = []"
    ]
````

#### 5.2.2 Reference and Pointer Handling
**Challenge:** Python lacks direct pointer arithmetic and reference semantics.

**Solution:**
1. Wrapper classes for pointer-like behavior
````python
class PointerWrapper:
    def __init__(self, target):
        self.target = target
        self.offset = 0
        
    def dereference(self):
        if isinstance(self.target, list):
            return self.target[self.offset]
        return self.target
        
    def increment(self):
        self.offset += 1
        
    def decrement(self):
        self.offset -= 1
````

### 5.3 Control Flow Challenges

#### 5.3.1 Loop Translation
**Challenge:** Converting C-style for loops to Python's range-based loops.

**Example:**
````cpp
for(int i = 0; i < n; i += 2) {
    // Complex increment
}
````

**Solution:**
1. Loop analysis and transformation system
````python
class LoopConverter:
    def analyze_loop_pattern(self, init, condition, increment):
        # Extract loop components
        init_var = init.variable
        init_value = init.value
        condition_limit = condition.right_value
        step = self.extract_step(increment)
        
        return {
            'var': init_var,
            'start': init_value,
            'end': condition_limit,
            'step': step
        }
        
    def convert_to_range(self, loop_info):
        return f"for {loop_info['var']} in range({loop_info['start']}, {loop_info['end']}, {loop_info['step']}):"
````

### 5.4 Memory Management Challenges

#### 5.4.1 Array Management
**Challenge:** Converting C++ fixed-size arrays to Python lists while maintaining performance.

**Solution:**
1. Optimized array initialization
````python
def convert_array_declaration(self, node):
    size = self.evaluate_constant_expression(node.size)
    element_type = node.type
    
    if self.is_numeric_type(element_type):
        # Use list comprehension for better performance
        return f"{node.name} = [0] * {size}"
    else:
        # Use proper initialization for complex types
        return f"{node.name} = [{element_type}() for _ in range({size})]"
````

#### 5.4.2 Resource Management
**Challenge:** Translating RAII patterns to Python context managers.

**Solution:**
1. Context manager conversion system
````python
def convert_raii_pattern(self, node):
    resource_type = node.type
    
    return [
        f"class {resource_type}Manager:",
        "    def __enter__(self):",
        "        # Resource acquisition",
        "        return self",
        "    def __exit__(self, exc_type, exc_val, exc_tb):",
        "        # Resource cleanup"
    ]
````

### 5.5 Standard Library Challenges

#### 5.5.1 IO Stream Translation
**Challenge:** Converting C++ streams to Python's print/input system.

**Solution:**
1. Stream operation mapping
````python
class StreamConverter:
    def convert_output_stream(self, node):
        elements = []
        for child in node.children:
            if child.value == '<<':
                continue
            elif child.value == 'endl':
                elements.append('"\\n"')
            else:
                elements.append(self.convert_expression(child))
                
        return f"print({', '.join(elements)}, sep='', end='')"
````

#### 5.5.2 STL Container Translation
**Challenge:** Mapping C++ STL containers to Python equivalents.

**Solution:**
1. Container mapping system
````python
STL_CONTAINER_MAP = {
    'vector': {
        'import': 'from typing import List',
        'type': 'List',
        'methods': {
            'push_back': 'append',
            'size': '__len__',
            'empty': 'lambda x: len(x) == 0'
        }
    },
    'map': {
        'import': 'from typing import Dict',
        'type': 'Dict',
        'methods': {
            'insert': '__setitem__',
            'find': 'get',
            'erase': 'pop'
        }
    }
}
````

### 5.6 Performance Challenges

#### 5.6.1 Code Optimization
**Challenge:** Generating efficient Python code from C++ constructs.

**Solution:**
1. Optimization passes
````python
class CodeOptimizer:
    def optimize_expressions(self, node):
        if self.is_constant_expression(node):
            return self.evaluate_constant_expression(node)
            
        if self.can_use_list_comprehension(node):
            return self.convert_to_list_comprehension(node)
            
        return self.default_conversion(node)
````

I'll add these important challenges to the section. Here's the addition:

````markdown
### 5.7 Object-Oriented Programming Challenges

#### 5.7.1 Class Structure Translation
**Challenge:** Converting C++ class structures with different access modifiers and member types to Python's simpler class model.

**Example C++ Class:**
````cpp
class Rectangle {
private:
    int width;
    int height;
    static int count;

public:
    Rectangle(int w, int h): width(w), height(h) {
        count++;
    }
    
    int getArea() const {
        return width * height;
    }
    
protected:
    void validate() {
        if (width < 0 || height < 0) {
            throw std::invalid_argument("Invalid dimensions");
        }
    }
};
````

**Solution:**
1. Access Modifier Translation
````python
class AccessModifierTranslator:
    def translate_class(self, node):
        private_members = []
        protected_members = []
        
        class_code = ["class Rectangle:"]
        
        # Add name mangling for private members
        for member in private_members:
            member.name = f"_{class_name}__{member.name}"
            
        # Add single underscore for protected members
        for member in protected_members:
            member.name = f"_{member.name}"
            
        # Generate __init__ with proper initialization
        init_code = [
            "    def __init__(self, w: int, h: int):",
            "        self.__width = w",
            "        self.__height = h",
            "        Rectangle.__count += 1"
        ]
        
        return class_code + init_code
````

2. Static Member Handling
````python
class StaticMemberHandler:
    def handle_static_members(self, class_node):
        static_members = []
        
        # Collect static members
        for member in class_node.members:
            if member.is_static:
                static_members.append(member)
                
        # Generate static member initialization
        static_init = []
        for member in static_members:
            static_init.append(f"    {member.name} = {member.initial_value}")
            
        return static_init
````

3. Method Decorator System
````python
class MethodDecorator:
    def generate_method_decorators(self, method_node):
        decorators = []
        
        if method_node.is_static:
            decorators.append("@staticmethod")
        elif method_node.is_class_method:
            decorators.append("@classmethod")
            
        if method_node.is_property:
            decorators.append("@property")
            
        return decorators
````

### 5.8 Type System and Arithmetic Operation Challenges

#### 5.8.1 Integer Division and Type Conversion
**Challenge:** C++ and Python handle integer division and type conversion differently.

**Example:**
````cpp
// C++ code
int a = 5;
int b = 2;
int result = a / b;  // result = 2 (integer division)
double dresult = a / b;  // dresult = 2.0 (still integer division)
double correct = static_cast<double>(a) / b;  // correct = 2.5
````

**Solution:**
1. Division Operation Handler
````python
class DivisionHandler:
    def convert_division(self, node, symbol_table):
        left_type = self.get_expression_type(node.left, symbol_table)
        right_type = self.get_expression_type(node.right, symbol_table)
        
        if left_type == 'int' and right_type == 'int':
            # Force integer division in Python
            return f"({node.left} // {node.right})"
        else:
            # Regular division
            return f"({node.left} / {node.right})"
````

2. Type Inference System
````python
class TypeInference:
    def __init__(self):
        self.type_map = {
            'int': int,
            'double': float,
            'float': float,
            'bool': bool,
            'string': str
        }
        
    def infer_type(self, expr_node, symbol_table):
        if expr_node.is_literal:
            return self.infer_literal_type(expr_node.value)
            
        if expr_node.is_binary_op:
            return self.infer_operation_type(
                expr_node.operator,
                expr_node.left,
                expr_node.right,
                symbol_table
            )
            
    def infer_operation_type(self, operator, left, right, symbol_table):
        left_type = self.infer_type(left, symbol_table)
        right_type = self.infer_type(right, symbol_table)
        
        if operator in ['/', '%']:
            if left_type == 'int' and right_type == 'int':
                return 'int' if operator == '//' else 'float'
        
        # Type promotion rules
        if 'double' in (left_type, right_type):
            return 'double'
        return left_type
````

3. Explicit Type Conversion Handler
````python
class TypeConversionHandler:
    def convert_cast_expression(self, node):
        target_type = node.target_type
        expression = node.expression
        
        if target_type == 'int':
            return f"int({expression})"
        elif target_type == 'double':
            return f"float({expression})"
        elif target_type == 'string':
            return f"str({expression})"
            
    def handle_implicit_conversion(self, value, from_type, to_type):
        if from_type == 'int' and to_type == 'double':
            return f"float({value})"
        if from_type == 'double' and to_type == 'int':
            return f"int({value})"
        return value
````

#### 5.8.2 Type Checking and Validation
**Challenge:** Maintaining type safety in Python's dynamic typing system.

**Solution:**
1. Runtime Type Checking
````python
def add_type_checks(self, function_node):
    """Add runtime type checking to function parameters"""
    params = function_node.parameters
    type_checks = []
    
    for param in params:
        if param.type_annotation:
            check = f"""
    if not isinstance({param.name}, {param.type_annotation}):
        raise TypeError(f"Expected {param.type_annotation.__name__} for {param.name}, got {{{param.name}.__class__.__name__}}")
            """
            type_checks.append(check)
            
    return type_checks

# Usage example:
def convert_function(self, node):
    func_name = node.name
    params = node.parameters
    
    # Generate function signature with type hints
    signature = f"def {func_name}("
    signature += ", ".join(f"{p.name}: {p.type_annotation}" for p in params)
    signature += f") -> {node.return_type}:"
    
    # Add type checking code
    type_checks = self.add_type_checks(node)
    
    return [signature] + type_checks + self.convert_body(node.body)
````

2. Type Hint Generation
````python
class TypeHintGenerator:
    def generate_type_hints(self, node):
        """Generate Python type hints from C++ types"""
        cpp_to_python_types = {
            'int': 'int',
            'double': 'float',
            'string': 'str',
            'vector<int>': 'List[int]',
            'map<string, int>': 'Dict[str, int]'
        }
        
        if node.is_template:
            return self.generate_template_type_hint(node)
        
        base_type = cpp_to_python_types.get(node.type_name, 'Any')
        
        if node.is_array:
            return f'List[{base_type}]'
        if node.is_pointer:
            return f'Optional[{base_type}]'
        
        return base_type
````


## 6. Future Work

### 6.1 Planned Improvements

1. Extended Language Features
   - Template support
   - Exception handling
   - Smart pointer translation

2. Optimization Opportunities
   - AST optimization
   - Code generation optimization
   - Performance improvements

## 7. Conclusion

This project successfully demonstrates the feasibility of automated C++ to Python translation while maintaining code readability and semantic equivalence. The modular architecture allows for future extensions and improvements.

## 8. References

1. ANTLR4 Documentation (https://www.antlr.org/documentation.html)
2. C++ Reference (https://en.cppreference.com/w/)
3. Python Documentation (https://docs.python.org/3/)

### Appendix A: Installation and Usage

#### A.1 Environment Setup
````bash
pip install -r requirements.txt
cd src
curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
````

#### A.2 Running the Transpiler
````bash
python src/main.py path/to/your/cpp/file.cpp [output_file.py]
````

### Appendix B: Code Examples

[Additional code examples and test cases]

