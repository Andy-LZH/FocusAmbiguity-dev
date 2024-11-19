import json

# Define the source file path
source_file = "submission/LIVE_2400_2520_ambiguous_results.json"

# Load the JSON data
with open(source_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Filter out entries with worker_id = "AZLZA0Q87TJZO"
filtered_data = {
    key: value
    for key, value in data.items()
    if value.get("worker_id") == "AZLZA0Q87TJZO"
}

source_file_out = "LIVE_2400_2520_ambiguous_results_cleaned.json"
# Save the filtered data back to the file
with open(source_file_out, "w", encoding="utf-8") as file:
    json.dump(filtered_data, file, indent=2, ensure_ascii=False)

print("Filtered data has been saved.")
