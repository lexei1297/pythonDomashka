import os
import json
import re

def convert_to_json(path_to_dataset: str = "class_3/hw2/t2_data/flowers", json_path: str = "class_3/hw2/t2_data/flowers/flowers.json") -> str:

    Args:
        path_to_dataset: Path to the dataset directory.
        json_path: Path to save the JSON file.

    Returns:
        Path to the created JSON file.  Returns an error message if the directory is not found or if an error occurs during JSON creation.
    if not os.path.exists(path_to_dataset):
        return f"Error: Dataset directory '{path_to_dataset}' not found."

    flowers_data = []
    for type_folder in os.listdir(path_to_dataset):
        type_path = os.path.join(path_to_dataset, type_folder)
        if os.path.isdir(type_path):
            for filename in os.listdir(type_path):
                if filename.endswith(".jpeg"):
                    match = re.search(r"(\w+)_(\w+)\.jpeg", filename)
                    if match:
                        color = match.group(2)
                        path = os.path.join(type_folder, filename)
                        flowers_data.append({
                            "path": path,
                            "color": color,
                            "type": type_folder
                        })
                    else:
                        print(f"Warning: Could not extract color from filename: {filename}")


    try:
        with open(json_path, 'w') as json_file:
            json.dump({"flowers": flowers_data}, json_file, indent=4)
        return json_path
    except Exception as e:
        return f"Error creating JSON file: {e}"


#Example usage:
result = convert_to_json()
print(result)

os.makedirs("class_3/hw2/t2_data/flowers/daisy", exist_ok=True)
os.makedirs("class_3/hw2/t2_data/flowers/rose", exist_ok=True)

with open("class_3/hw2/t2_data/flowers/daisy/african_daisy_yellow.jpeg", "w") as f: f.write("")
with open("class_3/hw2/t2_data/flowers/rose/red_rose.jpeg", "w") as f: f.write("")
with open("class_3/hw2/t2_data/flowers/rose/white_rose.jpeg", "w") as f: f.write("")
with open("class_3/hw2/t2_data/flowers/daisy/white_daisy.jpeg", "w") as f: f.write("")


result = convert_to_json()
print(result)
