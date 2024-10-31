# Bracketed JSON Transformer

## Project Overview

This project aims to convert a poorly formatted database, such as a text file with JSON-like entries, into a well-structured JSON file. The code processes the file by identifying and extracting JSON blocks that are enclosed by global separators, which are square brackets (`[` and `]`) by default. These separators can be adjusted as needed to fit other data formats.

The script reads a source file, isolates JSON blocks by counting opening and closing brackets, and writes the combined, validated JSON content to a new output file. This allows for improved data formatting and easier integration with other systems that require JSON inputs.

## How It Works

1. **Read the Source File:** The script reads a line-by-line input file that contains JSON data but lacks a consistent structure.
2. **Extract JSON Blocks:** It identifies complete JSON blocks using brackets to balance and determine valid JSON objects.
3. **Validate and Save Data:** After parsing and validating each JSON block, the script appends it to a master list, which is then saved as a single, well-formatted JSON file.

## Example Transformation

Suppose you have a source file, `sample_free.txt`, with the following content:

```plaintext
[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
[{"name": "Charlie", "age": 35}]
```

Running the script with this file would produce an `output.json` file as follows:

```json
[
    {
        "name": "Alice",
        "age": 25
    },
    {
        "name": "Bob",
        "age": 30
    },
    {
        "name": "Charlie",
        "age": 35
    }
]
```

## How to Use

1. Place the file you want to convert in the same directory as the script or specify its path.
2. Set the `file_path` to the location of your source file and `output_file_path` to the desired output location.
3. Run the script to generate a clean JSON file.

```python
# Example usage
file_path = 'file/input.txt'  # Path to the source file
output_file_path = 'file/output.json'  # Path to the output JSON file
extract_json_blocks(file_path, output_file_path)
```

After running the code, you should see a message confirming that the JSON file was successfully created.

## Notes

- **Customizing Separators**: By default, this script uses square brackets (`[` and `]`) as block delimiters. You can modify the code if your data requires different separators.
- **Error Handling**: If a block is not valid JSON, an error message will be displayed, but processing will continue for subsequent blocks.

## Requirements

- Python 3.x
