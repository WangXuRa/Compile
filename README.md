# C++ Lexer and Parser using ANTLR4

This project implements a lexer and parser for C++ using ANTLR4. The lexer can tokenize C++ code and identify various language elements such as keywords, operators, literals, identifiers, and comments. The parser can parse C++ code and identify various language elements such as statements, expressions, and declarations.

## Team

- [@王旭冉](https://github.com/WangXuRa)
- [@苏伟铭](https://github.com/wms2537)
- [@汪佳宇](https://github.com/Ccindy0171)
- [@陈立心](https://github.com/tls0523)

## Project Structure
The project structure is as follows:
- `src/CPPLexer.g4` - ANTLR4 grammar file defining the lexer rules
- `src/CPPParser.g4` - ANTLR4 grammar file defining the parser rules
- `src/main.py` - Python script that uses the generated lexer and parser
- `src/test_KMP.cpp` - KMP string matching algorithm test case
- `src/test_bubbleSort.cpp` - Bubble sort algorithm test case
- `src/cppParserBase.py` - Parser base class implementation
- `src/CPPParserVisitor.py` - Visitor pattern implementation for AST generation

## Prerequisites

- Python 3.6 or higher
- Java Runtime Environment (JRE) - needed to run the ANTLR tool
- ANTLR4 Python runtime library

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download ANTLR4 in the `src` directory:
   ```bash
   cd src
   curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
   ```

4. Generate the lexer and parser code:
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 CPPLexer.g4
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 CPPParser.g4
   ```

## Usage

You can run the lexer and parser in two ways:

1. With a C++ file as input:
   ```bash
   python main.py path/to/your/cpp/file.cpp
   ```

2. With the default example code:
   ```bash
   python main.py
   ```

The program generates two outputs:
- Lexer output: Shows all recognized tokens
- Parser output: Generates AST (Abstract Syntax Tree) and saves it to ast_output.xml

## Test Cases

### 1. KMP String Matching Algorithm (test_KMP.cpp)
Implements the classic KMP string matching algorithm, including:
- Partial match table (next array) calculation
- String matching process
- Multiple match support
- Error handling

### 2. Bubble Sort Algorithm (test_bubbleSort.cpp)
Implements the basic bubble sort algorithm, featuring:
- Dynamic array input
- Integer sorting
- Result visualization
- Swap operation optimization

### Example Output

For the bubble sort test case (test_bubbleSort.cpp):

Input (C++ source code):
```cpp
#include <iostream>

int main() {
    int num;
    int a[100];  // Fixed size array

    // Input array length
    std::cout << "Input the array length: ";
    std::cin >> num;

    // Input integers
    std::cout << "Input integers: ";
    for (int i = 0; i < num; i++) {
        std::cin >> a[i];
    }
    // ... rest of the code
}
```

Lexer Output:
```
Token: INCLUDE              Text: #include
Token: LT                   Text: <
Token: ID                   Text: iostream
Token: GT                   Text: >
Token: INT                  Text: int
Token: ID                   Text: main
Token: LPAREN               Text: (
Token: RPAREN               Text: )
Token: LBRACE               Text: {
Token: INT                  Text: int
Token: ID                   Text: num
Token: SEMICOLON            Text: ;
...
```

Parser Output (excerpt from AST):
```xml
<AST>
<program>
  <includeStatement>
    <INCLUDE>#include</INCLUDE>
    <LT><</LT>
    <includeID>
      <ID>iosteam</ID>
    </includeID>
    <GT>></GT>
  </includeStatement>
  <includeStatement>
    <INCLUDE>#include</INCLUDE>
      ...
```

## Features Support

Current version supports the following C++ language features:
- Basic data types (int, char, bool, etc.)
- Control flow statements (if-else, for, while)
- Array operations
- Basic input/output
- Function definitions and calls
- Operators and expressions
- Variable declarations and assignments

## Error Handling

The parser can handle various error scenarios:
- Syntax error detection
- Input file error handling
- Parsing process error reporting
- AST generation exception handling

## Future Development Plans

1. Add support for classes and objects
2. Implement more C++11 features
3. Optimize AST generation efficiency
4. Add more test cases
5. Improve error messages

## Discussions
### Challenges
The biggest challenge we faced was the complexity of the C++ language. It has many different constructs and features that make it difficult to parse. We had to spend significant time researching and discussing different approaches to parsing the language.

### Solutions
We used ANTLR4 to generate the lexer and parser. ANTLR4 is a powerful tool that allows us to define the language grammar in a way that is easy to understand and modify. It also generates the lexer and parser code for us, which saves us a lot of time and effort.

The visitor pattern implementation helped us generate a clean AST structure that can be easily traversed and analyzed. We also implemented careful error handling to make the parser more robust.

## Implementation Approach

### 1. Grammar Design
- Started with core C++ syntax elements
  * Defined basic tokens (keywords, operators, identifiers)
  * Implemented expression grammar with proper precedence
  * Added statement grammar rules
  * Integrated type system basics
- Divided grammar into lexer and parser rules
  * Lexer handles tokenization of source code
  * Parser builds syntactic structure
  * Separated concerns for better maintenance
- Carefully handled operator precedence
  * Implemented precedence climbing method
  * Handled associativity rules
  * Managed compound operators
- Implemented support for basic C++ constructs
  * Function declarations and definitions
  * Variable declarations
  * Control structures
  * Array declarations and access

### 2. AST Construction
- Used visitor pattern for tree construction
  * Implemented CPPParserVisitor class
  * Created node types for each grammar construct
  * Built hierarchical structure
  * Maintained source location information
- Designed node structure to represent C++ elements
  * Base Node class with common attributes
  * Specialized nodes for different constructs
  * Attribute storage for type information
  * Support for comments and annotations
- Implemented proper parent-child relationships
  * Bidirectional node references
  * Scope management
  * Symbol table integration
  * Cross-reference support
- Added support for code block scoping
  * Block-level symbol tables
  * Variable shadowing handling
  * Scope entry/exit tracking
  * Declaration/reference resolution

### 3. Development Process
1. Grammar Development:
   - First implemented basic expressions
     * Arithmetic and logical operators
     * Function calls
     * Variable references
     * Literal values
   - Added support for statements
     * If-else conditions
     * Loops (for, while)
     * Return statements
     * Expression statements
   - Implemented function definitions
     * Parameter lists
     * Return types
     * Function bodies
     * Forward declarations
   - Added array support
     * Array declarations
     * Array access
     * Multi-dimensional arrays
     * Array initialization
   - Integrated error handling
     * Syntax error recovery
     * Error messages
     * Warning generation
     * Error location tracking

2. Testing Strategy:
   - Unit tests for individual grammar rules
     * Expression parsing tests
     * Statement parsing tests
     * Declaration tests
     * Type system tests
   - Integration tests with complete programs
     * Full function tests
     * Program structure tests
     * Multi-file parsing
     * Include handling
   - Edge case testing for error handling
     * Invalid syntax recovery
     * Error message accuracy
     * Parser robustness
     * Memory management
   - Performance testing with large files
     * Memory usage monitoring
     * Parse time measurements
     * AST size optimization
     * Token stream efficiency

3. Optimization:
   - Improved grammar rules for better performance
     * Left recursion elimination
     * Rule factoring
     * Lookahead optimization
     * Backtracking reduction
   - Optimized visitor pattern implementation
     * Cached node access
     * Lazy evaluation
     * Memory pooling
     * Reference counting
   - Enhanced error reporting
     * Contextual error messages
     * Suggestion generation
     * Error recovery strategies
     * Debug information
   - Reduced memory usage in AST construction
     * Node sharing
     * Attribute compression
     * Memory pools
     * Garbage collection

## References
- [ANTLR4 Documentation](https://www.antlr.org/documentation.html)
- [C++ Documentation](https://en.cppreference.com/w/)