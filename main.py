from antlr4 import *
from CPP14Lexer import CPP14Lexer
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

    # Create lexer
    lexer = CPP14Lexer(input_stream)
    
    # Get all tokens
    tokens = lexer.getAllTokens()
    
    # Print tokens
    for token in tokens:
        token_type = lexer.symbolicNames[token.type]
        token_text = token.text
        print(f"Token: {token_type:20} Text: {token_text}")

if __name__ == '__main__':
    main()
