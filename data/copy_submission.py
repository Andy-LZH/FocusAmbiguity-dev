import json
import os
import math

# Define the source and destination file paths
source_file_ambiguous = "submission/LIVE_2400_2520_ambiguous_results.json"
source_file_unambiguous = "submission/LIVE_2400_2520_unambiguous_results.json"
min_index = math.floor(2400 / 50)
max_index = math.ceil(2520 / 50)
print("Min Index:", min_index, "Max Index:", max_index)

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
    print(
        "Processing Ambiguous Item:",
        item,
        "File to Access:",
        file_to_access,
        "Offset:",
        offset,
    )
    item_list.append(item)
    with open(
        destination_files_ambiguous[file_to_access], "r", encoding="utf-8"
    ) as file:
        dest_data_am = json.load(file)

    dest_data_am[offset]["questions"] = data["questions"]
    dest_data_am[offset]["selected_questions"] = [data["selected_question"]]
    dest_data_am[offset]["selected_objects_polygons"] = data[
        "selected_objects_polygons"
    ]
    dest_data_am[offset]["selected_parts_polygons"] = data["selected_parts_polygons"]

    with open(
        destination_files_ambiguous[file_to_access], "w", encoding="utf-8"
    ) as file:
        json.dump(dest_data_am, file, indent=2, ensure_ascii=False)

for item, data in source_data_unambiguous.items():
    file_to_access = (int(item) // 50) - min_index
    offset = int(item) % 50
    print(
        "Processing Unambiguous Item:",
        item,
        "File to Access:",
        file_to_access,
        "Offset:",
        offset,
    )
    with open(
        destination_files_unambiguous[file_to_access], "r", encoding="utf-8"
    ) as file:
        dest_data_un = json.load(file)

    dest_data_un[offset]["questions"] = data["questions"]
    dest_data_un[offset]["selected_questions"] = [data["selected_question"]]
    dest_data_un[offset]["selected_objects_polygons"] = data[
        "selected_objects_polygons"
    ]
    dest_data_un[offset]["selected_parts_polygons"] = data["selected_parts_polygons"]

    with open(
        destination_files_unambiguous[file_to_access], "w", encoding="utf-8"
    ) as file:
        json.dump(dest_data_un, file, indent=2, ensure_ascii=False)

# Save item list to a file
with open("item_list.json", "w", encoding="utf-8") as file:
    json.dump(item_list, file, indent=2, ensure_ascii=False)

print("Data has been copied and updated in the destination files.")
