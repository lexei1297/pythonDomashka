import os
import json


def convert_to_json(path_to_dataset: str = "E:/folder_for_PY_hw/pythonDomashka/Class3/hw2/t2_data/flowers",
                    json_path: str = "E:/folder_for_PY_hw/pythonDomashka/Class3/hw2/t2_data/flowers/flowers.json") -> str:
    # Dictionary to hold the data
    dataset_dict = {"flowers": []}

    # Traverse the directory structure
    for root, dirs, files in os.walk(path_to_dataset):
        for file in files:
            if file.endswith(".jpeg"):
                # Extract flower type (folder name) and color (from filename)
                folder_name = os.path.basename(root)
                color_part = file.split('_')[-1].replace('.jpeg', '')

                # Create an entry for the flower
                flower_entry = {
                    "path": os.path.join(root, file).replace("\\", "/"),  # Normalize path for all platforms
                    "color": color_part,
                    "type": folder_name
                }
                dataset_dict["flowers"].append(flower_entry)

    # Write to JSON file
    with open(json_path, "w") as json_file:
        json.dump(dataset_dict, json_file, indent=4)

    return json_path
