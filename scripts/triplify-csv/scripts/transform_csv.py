import csv
import json
import uuid

# Load mapping config from JSON file
with open("config/config.json", "r") as json_file:
    mapping_rules = json.load(json_file)


# Transform CSV to Turtle
def csv_to_turtle(csv_file_path, turtle_file_path):
    with open(csv_file_path, "r") as csv_file, open(
        turtle_file_path, "w"
    ) as turtle_file, open("ttl/location.ttl", "w") as location_turtle_file:
        reader = csv.DictReader(csv_file, delimiter="\t")

        for row in reader:
            subject = f"<http://mu.semte.ch/vocabularies/ext/erfGoed/{uuid.uuid4()}>"
            turtle_lines = [f"{subject} a ext:erfGoed ;"]

            for column, value in row.items():
                if column in mapping_rules:
                    if "data-type" in mapping_rules[column]:
                        predicate = mapping_rules[column]["predicate"]
                        if mapping_rules[column]["data-type"] == "URI":
                            turtle_lines.append(
                                f'    {predicate} {value} ;'
                            )
                        elif (
                            mapping_rules[column]["data-type"]
                            == "^^<http://mu.semte.ch/vocabularies/typed-literals/boolean>"
                        ):
                            turtle_lines.append(
                                f'    {predicate} "{value.lower()}"{mapping_rules[column]["data-type"]} ;'
                            )
                        else:
                            turtle_lines.append(f'    {predicate} "{value}" ;')
                    # We have encountered a "deep" instance which needs its own URI.
                    elif "type" in mapping_rules[column]:
                        inner_subject = (
                            f"<http://data.lblod.info/id/locaties/{uuid.uuid4()}>"
                        )
                        turtle_lines.append(f'    {mapping_rules[column]["predicate"]} {inner_subject} ;')
                        location_lines = [f"{inner_subject} a prov:Location ;"]
                        location_lines.append(
                            f'    {mapping_rules[column]["class"]["predicate"]} "{value}" ;'
                        )
                        # Remove the last semicolon and add a period
                        location_lines[-1] = location_lines[-1].rstrip(" ;") + " ."
                        location_turtle_file.write("\n".join(location_lines) + "\n")

            # Remove the last semicolon and add a period
            turtle_lines[-1] = turtle_lines[-1].rstrip(" ;") + " ."
            turtle_file.write("\n".join(turtle_lines) + "\n")


def main():
    csv_to_turtle("csv/modified.csv", "ttl/output.ttl")


if __name__ == "__main__":
    main()
