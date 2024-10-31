import json

def extract_json_blocks(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = []
        buffer = ""
        bracket_count = 0
        inside_block = False

        for line in file:
            for char in line:
                if char == '[':
                    if not inside_block:
                        inside_block = True  
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1

                if inside_block:
                    buffer += char  

                if inside_block and bracket_count == 0:
                    try:
                        json_object = json.loads(buffer)
                        data.extend(json_object)  
                    except json.JSONDecodeError:
                        print("JSON decoding error for a block.")
                    
                    buffer = ""
                    inside_block = False

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)
    
    print(f"Valid JSON file successfully created: {output_file_path}")


file_path = 'file/imput.txt'
output_file_path = 'file/output.json'
extract_json_blocks(file_path, output_file_path)
