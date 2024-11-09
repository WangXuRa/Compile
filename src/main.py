from antlr4 import *
# from CPPLexer import CPPLexer 
# from CPPParser import CPPParser 
# from CPPParserListener import CPPParserListener 
# from CPPParserVisitor_dev import CPPParserVisitor

from CPPLexer import CPPLexer 
from CPPParser import CPPParser 
from CPPParserListener import CPPParserListener 
from CPPParserVisitor import CPPParserVisitor
import sys

def read_input_from_file(filename):
    # Get input from a file 
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return InputStream(file.read())
    except IOError:
        print(f"无法读取文件: {filename}")
        sys.exit(1) 

def main():
    # Get input from a file or string
    if len(sys.argv) > 1:
        input_stream = read_input_from_file(sys.argv[1])
    else:
        # Example C++ code for testing
        sample_code = """
        int main() {
            int x = 42;
            if (x > 0) {
                return x;
            }
            return 0;
        }
        """
        input_stream = InputStream(sample_code)

    print("# Lexer #")

    # Create lexer
    lexer = CPPLexer(input_stream)
    
    # Get all tokens
    tokens = lexer.getAllTokens()
    
    # Print tokens
    for token in tokens:
        token_type = lexer.symbolicNames[token.type]
        token_text = token.text
        print(f"Token: {token_type:20} Text: {token_text}")

    lexer.reset()
    
    token_stream = CommonTokenStream(lexer)
    
    print("\n\n# Parser #")
    parser = CPPParser(token_stream)

    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")

    else:
        visitor = CPPParserVisitor(parser)
        astTree = visitor.visit(tree)
        print(astTree)

if __name__ == '__main__':
    main()
