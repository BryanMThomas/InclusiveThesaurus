import json

# Initialize an empty list to store the combined data
data = json.load(open("output.json", "r"))
new_data = []

for item in data:
    for term in item["non_inclusive_term"]:
        new_item = {
            "non_inclusive_term": term,
            "inclusive_alternatives": item["inclusive_alternatives"],
            "note": item["note"]
        }
        new_data.append(new_item)

# Output new_data as a new JSON file
with open("output_converted.json", "w") as outfile:
    json.dump(new_data, outfile, indent=2)
