# C++ Lexer using ANTLR4

This project implements a lexer for C++ using ANTLR4. The lexer can tokenize C++ code and identify various language elements such as keywords, operators, literals, identifiers, and comments.

## Prerequisites

- Python 3.6 or higher
- Java Runtime Environment (JRE) - needed to run the ANTLR tool

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Assembly/Big
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download ANTLR4:
   ```bash
   curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
   ```

4. Generate the lexer code:
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 CPP14Lexer.g4
   ```

## Project Structure

- `CPP14Lexer.g4` - ANTLR4 grammar file defining the lexer rules
- `main.py` - Python script that uses the generated lexer
- `requirements.txt` - Python dependencies
- Generated files (after running ANTLR4):
  - `CPP14Lexer.py`
  - `CPP14Lexer.interp`
  - `CPP14Lexer.tokens`

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

## Example Output

For the input code: