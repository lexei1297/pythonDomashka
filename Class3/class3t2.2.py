from typing import List, Union
import json


class FlowersDataset:
    def __init__(self, json_file: str):
        # Load the dataset from the JSON file
        with open(json_file, "r") as f:
            self.data = json.load(f)["flowers"]

    def get_items(self, properties: dict) -> Union[List[str], str]:
        # Prepare filters
        types = properties.get("type", [])
        colors = properties.get("color", [])

        # Ensure both are lists for easy filtering
        if not isinstance(types, list):
            types = [types]
        if not isinstance(colors, list):
            colors = [colors]

        # Filter dataset based on the properties
        result = []
        for flower in self.data:
            if (not types or flower["type"] in types) and (not colors or flower["color"] in colors):
                result.append(flower["path"])

        return result