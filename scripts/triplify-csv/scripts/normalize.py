# This file normalizes the json output files for provincies and gemeenten produced by Virtuoso to become
# more streamlined and easy to use.

import json


def normalize(file_name):
    # Load mapping config from JSON file
    with open(f"preprocessing/{file_name}", "r") as file:
        data = json.load(file)

    # Transform the city data into the desired dictionary format
    data_normalized = {item["label"]["value"]: item["s"]["value"] for item in data}

    # Write the transformed mapping to a JSON file
    with open(f"preprocessing/normalized-{file_name}", "w") as json_file:
        json.dump(data_normalized, json_file, indent=4)


def main():
    normalize("province.json")


if __name__ == "__main__":
    main()
