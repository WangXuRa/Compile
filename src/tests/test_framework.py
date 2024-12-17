import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from pathlib import Path
from cpp_to_python_transpiler import CppToPythonTranspiler, TranspilerError

class TestCppToPythonTranspiler(unittest.TestCase):
    def setUp(self):
        self.transpiler = CppToPythonTranspiler()
    
    # Basic Tests
    def test_empty_file(self):
        """Test transpiling an empty file"""
        result = self.transpiler.transpile("")
        self.assertEqual(result.strip(), "")
    
    # Include Tests
    def test_includes(self):
        """Test handling of include directives"""
        cpp_code = """
        #include <iostream>
        #include <vector>
        #include <string>
        
        int main() {
            return 0;
        }
        """
        result = self.transpiler.transpile(cpp_code)
        self.assertIn("from sys import stdout", result)
        self.assertIn("from typing import List", result)
    
    # Class Hierarchy Tests
    def test_class_inheritance(self):
        """Test class inheritance handling"""
        cpp_code = """
        class Animal {
        public:
            virtual void speak() = 0;
        };
        
        class Dog : public Animal {
        public:
            void speak() override { cout << "Woof"; }
        };
        """
        result = self.transpiler.transpile(cpp_code)
        self.assertIn("class Animal:", result)
        self.assertIn("class Dog(Animal):", result)
    
    # Template Tests
    def test_template_class(self):
        """Test template class conversion"""
        cpp_code = """
        template<typename T>
        class Container {
        public:
            T value;
            void setValue(T v) { value = v; }
        };
        """
        result = self.transpiler.transpile(cpp_code)
        self.assertIn("from typing import TypeVar, Generic", result)
        self.assertIn("T = TypeVar('T')", result)
        self.assertIn("class Container(Generic[T]):", result)
    
    # STL Tests
    def test_stl_vector(self):
        """Test STL vector conversion"""
        cpp_code = """
        vector<int> numbers;
        numbers.push_back(1);
        """
        result = self.transpiler.transpile(cpp_code)
        self.assertIn("numbers: List[int] = []", result)
        self.assertIn("numbers.append(1)", result)
    
    # Error Cases
    def test_syntax_error(self):
        """Test handling of syntax errors"""
        with self.assertRaises(TranspilerError) as context:
            self.transpiler.transpile("class {")
        self.assertIn("Syntax error", str(context.exception))
    
    def test_undefined_type(self):
        """Test handling of undefined types"""
        cpp_code = """
        UndefinedType var;
        """
        with self.assertRaises(TranspilerError):
            self.transpiler.transpile(cpp_code)
    
    # Edge Cases
    def test_nested_templates(self):
        """Test nested template handling"""
        cpp_code = """
        vector<vector<int>> matrix;
        """
        result = self.transpiler.transpile(cpp_code)
        self.assertIn("List[List[int]]", result)
    
    def test_multiple_inheritance(self):
        """Test multiple inheritance"""
        cpp_code = """
        class A {};
        class B {};
        class C : public A, public B {};
        """
        result = self.transpiler.transpile(cpp_code)
        self.assertIn("class C(A, B):", result)
    
    def test_namespace_handling(self):
        """Test namespace handling"""
        cpp_code = """
        namespace outer {
            namespace inner {
                class MyClass {};
            }
        }
        """
        result = self.transpiler.transpile(cpp_code)
        self.assertIn("class outer_inner_MyClass:", result)

if __name__ == '__main__':
    unittest.main()