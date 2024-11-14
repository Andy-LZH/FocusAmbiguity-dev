import json
import os
import math

# Define the source and destination file paths

source_file_ambiguous = "submission/LIVE_2400_2520_ambiguous_results.json"
source_file_unambiguous = "submission/LIVE_2400_2520_unambiguous_results.json"
min_index = math.floor(2400 / 50)
max_index = math.ceil(2520 / 50)
print(min_index, max_index)
destination_files_ambiguous = [
    f"ivc-ambigous-{i}.json" for i in range(min_index, max_index)
]  # Adjust the range as needed
destination_files_unambiguous = [
    f"ivc-unambigous-{i}.json" for i in range(min_index, max_index)
]  # Adjust the range as needed

# Load the source data
with open(source_file_ambiguous, "r", encoding="utf-8") as file:
    source_data_ambiguous = json.load(file)

with open(source_file_unambiguous, "r", encoding="utf-8") as file:
    source_data_unambiguous = json.load(file)


item_list = []

for item, data in source_data_ambiguous.items():
    file_to_access = (int(item) // 50) - min_index
    offset = int(item) % 50
    print(item, file_to_access, offset)
    item_list.append(item)
    with open(
        destination_files_ambiguous[file_to_access], "r", encoding="utf-8"
    ) as file:
        dest_data = json.load(file)
    dest_data[offset]["questions"] = data["questions"]
    dest_data[offset]["selected_questions"] = [data["selected_question"]]
    dest_data[offset]["selected_objects_polygons"] = data["selected_objects_polygons"]
    dest_data[offset]["selected_parts_polygons"] = data["selected_parts_polygons"]

    json.dump(
        dest_data,
        open(destination_files_ambiguous[file_to_access], "w"),
        indent=2,
        ensure_ascii=False,
    )

for item, data in source_data_unambiguous.items():
    file_to_access = (int(item) // 50) - min_index
    offset = int(item) % 50
    print(item, file_to_access, offset)
    with open(
        destination_files_unambiguous[file_to_access], "r", encoding="utf-8"
    ) as file:
        dest_data = json.load(file)
    dest_data[offset]["questions"] = data["questions"]
    dest_data[offset]["selected_questions"] = [data["selected_question"]]
    dest_data[offset]["selected_objects_polygons"] = data["selected_objects_polygons"]
    dest_data[offset]["selected_parts_polygons"] = data["selected_parts_polygons"]

    json.dump(
        dest_data,
        open(destination_files_unambiguous[file_to_access], "w"),
        indent=2,
        ensure_ascii=False,
    )

# save item list to a file
with open("item_list.json", "w") as file:
    json.dump(item_list, file, indent=2, ensure_ascii=False)
print("Data has been copied and updated in the destination files.")
