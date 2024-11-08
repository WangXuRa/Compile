from antlr4 import *
from cppLexer import cppLexer
from cppParser import cppParser
from cppParserListener import cppParserListener
from cppParserVisitor_dev import cppParserVisitor
import sys

def main():
    # Get input from a file or string
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
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
    lexer = cppLexer(input_stream)
    
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
    parser = cppParser(token_stream)

    tree = parser.translationUnit()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")

    else:
        visitor = cppParserVisitor(parser)
        astTree = visitor.visit(tree)
        print(astTree)

if __name__ == '__main__':
    main()
