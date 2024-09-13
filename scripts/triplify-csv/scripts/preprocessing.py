import csv
import json


# Load city to URI mapping from JSON file
def load_gemeente_mapping(json_file_path):
    with open(json_file_path, "r") as json_file:
        return json.load(json_file)


# Replace city names with URIs in the CSV file
def replace_gemeente_in_csv(csv_file_path, city_mapping, province_mapping):
    # Read the existing CSV data
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter="\t")
        rows = list(reader)

    # Replace city names with their corresponding URIs
    for row in rows:
        if "gemeente" in row:
            gemeenten = row["gemeente"].split(",")  # Split gemeente by comma
            # Strip whitespace and replace with URIs
            uris = [
                city_mapping.get(gemeente.strip(), gemeente.strip())
                for gemeente in gemeenten
            ]
            row["gemeente"] = ", ".join(uris)  # Join URIs back into a string
        if "provincie" in row:
            provincies = row["provincie"].split(",")  # Split gemeente by comma
            # Strip whitespace and replace with URIs
            uris = [
                province_mapping.get(provincie.strip(), provincie.strip())
                for provincie in provincies
            ]
            row["provincie"] = ", ".join(uris)  # Join URIs back into a string

    # Write the modified data back to the same CSV file
    with open(f"csv/modified.csv", "w", newline="") as csv_file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main():
    city_mapping = load_gemeente_mapping("preprocessing/normalized-gemeente.json")
    province_mapping = load_gemeente_mapping("preprocessing/normalized-province.json")
    replace_gemeente_in_csv("csv/erfgoed_test.csv", city_mapping, province_mapping)


if __name__ == "__main__":
    main()
