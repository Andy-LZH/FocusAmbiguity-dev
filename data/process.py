import json
import os

# Path to your JSON file
data_file_paths = ["ivc-unambigous", "ivc-ambigous"]

# range is 0 to 50 with ivc-ambigous-0.json and ivc-unambigous-0.json

# Iterate over each file
for data_file_path in data_file_paths:
    # Read the JSON data
    for i in range(0, 51):
        data_file_path_r = f"{data_file_path}-{i}.json"
        print(data_file_path_r)
        with open(data_file_path_r, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(len(data))

        # Iterate over each entry in the data
        for entry in data:
            length_of_subparts = len(entry["parts_polygons"]["polygons"])
            length_of_objects = len(entry["objects_polygons"])

            entry["selected_objects_polygons"] = []
            entry["selected_parts_polygons"] = []

            for i in range(length_of_subparts):
                entry["selected_parts_polygons"].append(i)

            for i in range(length_of_objects):
                entry["selected_objects_polygons"].append(i)

        # Write the updated data back to the file
        with open(data_file_path_r, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Processed file: {data_file_path}")
