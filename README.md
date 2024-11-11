# C++ Lexer and Parser using ANTLR4

This project implements a lexer and parser for C++ using ANTLR4. The lexer can tokenize C++ code and identify various language elements such as keywords, operators, literals, identifiers, and comments. The parser can parse C++ code and identify various language elements such as statements, expressions, and declarations.

## Team

- [@王旭冉](https://github.com/WangXuRa)
- [@苏伟铭](https://github.com/wms2537)
- [@汪佳宇](https://github.com/Ccindy0171)
- [@陈立心](https://github.com/tls0523)

## Project Structure
The project structure is as follows:
- `src/cppLexer.g4` - ANTLR4 grammar file defining the lexer rules
- `src/cppParser.g4` - ANTLR4 grammar file defining the parser rules
- `src/main.py` - Python script that uses the generated lexer and parser


## Prerequisites

- Python 3.6 or higher
- Java Runtime Environment (JRE) - needed to run the ANTLR tool

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

4. Generate the lexer code:
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 CPPLexer.g4
   ```

5. Generate the parser code:
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 CPPParser.g4
   ```
## Usage

You can run the lexer in two ways:

1. With a C++ file as input:
   ```bash
   python main.py path/to/your/cpp/file.cpp
   ```

2. With the default example code:
   ```bash
   python main.py
   ```

The lexer will output each token's type and text.

### Example Output

For the input code:
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```
The following is the output of the lexer and parser:
```
<INCLUDE> <iostream>
<NAMESPACE> std
<INT> int
<ID> main
<LPAREN> (
<RPAREN> )
<LBRACE> {
<COUT> cout
<STRING> "Hello, World!"
<SEMICOLON> ;
<RETURN> return
<INT> 0
<RBRACE> }
```


## Discussion
### Challenges
The biggest challenge we faced was the complexity of the C++ language. It has a lot of different constructs and features that make it difficult to parse. We had to spend a lot of time researching and discussing different approaches to parsing the language.

### Solutions
We used ANTLR4 to generate the lexer and parser. ANTLR4 is a powerful tool that allows us to define the grammar of the language in a way that is easy to understand and modify. It also generates the lexer and parser code for us, which saves us a lot of time and effort.

## Test Cases
We have tested the lexer and parser with a variety of C++ code. We have also tested them with code that is syntactically incorrect to see how they handle errors.

Below are some test cases that we have used:
### Correct Code
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```  

### Incorrect Code
```cpp
int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```   

### Error Handling
The lexer and parser are able to handle errors in the code. For example, if there is a syntax error, the lexer will print an error message and the parser will print an error message.


### Conclusion
This project was a great learning experience for us. We learned a lot about the C++ language and how to parse it. We also learned a lot about ANTLR4 and how to use it to generate lexer and parser code.


## References
- [ANTLR4 Documentation](https://www.antlr.org/documentation.html)
- [C++ Documentation](https://en.cppreference.com/w/)