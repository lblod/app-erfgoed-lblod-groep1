# This file normalizes the json output files for provincies and gemeenten produced by Virtuoso to become
# more streamlined and easy to use.

import json
import re

def sparql_escape_uri(obj):
    """Converts the given URI to a SPARQL-safe RDF object string with the right RDF-datatype. """
    obj = str(obj)
    return '<' + re.sub(r'[\\"<>]', lambda s: "\\" + s.group(0), obj) + '>'

def normalize(file_name):
    data_normalized = {}

    # Load mapping config from JSON file
    with open(f"preprocessing/{file_name}", "r") as file:
        data = json.load(file)

    # Transform the city data into the desired dictionary format
    # data_normalized = {item["label"]["value"]: f"<{item["s"]["value"]}>" for item in data}
    for item in data:
        data_normalized[item["label"]["value"]] = sparql_escape_uri(item["s"]["value"])

    # Write the transformed mapping to a JSON file
    with open(f"preprocessing/normalized-{file_name}", "w") as json_file:
        json.dump(data_normalized, json_file, indent=4)


def main():
    normalize("province.json")
    normalize("gemeente.json")


if __name__ == "__main__":
    main()
