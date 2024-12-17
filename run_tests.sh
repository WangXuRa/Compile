#!/bin/bash


# Loop through all .cpp files in tests directory
for cpp_file in src/tests/*.cpp; do
    if [ -f "$cpp_file" ]; then
        echo "Processing $cpp_file..."
        
        # Get the base filename without extension
        base_name=$(basename "$cpp_file" .cpp)
        
        # Run the transpiler and save output to corresponding .py file
        python src/main.py "$cpp_file" "src/tests/${base_name}.py"
        
        echo "Generated tests/${base_name}.py"
        echo "----------------------------------------"
    fi
done

echo "All files processed!"