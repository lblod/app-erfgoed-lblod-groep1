import csv
import json

# Load mapping config from JSON file
with open("config/config.json", "r") as json_file:
    mapping_rules = json.load(json_file)


# Transform CSV to Turtle
def csv_to_turtle(csv_file_path, turtle_file_path):
    with open(csv_file_path, "r") as csv_file, open(
        turtle_file_path, "w"
    ) as turtle_file:
        reader = csv.DictReader(csv_file, delimiter="\t")

        for row in reader:
            subject = f"<http://example.com/{row['id']}>"
            turtle_lines = [f"{subject} rdf:type owl:NamedIndividual ;"]

            for column, value in row.items():
                if column in mapping_rules:
                    predicate = mapping_rules[column]["predicate"]
                    turtle_lines.append(f'    {predicate} "{value}" ;')

            # Remove the last semicolon and add a period
            turtle_lines[-1] = turtle_lines[-1].rstrip(" ;") + " ."
            turtle_file.write("\n".join(turtle_lines) + "\n")


def parse_csv(file_path):
    data = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file, delimiter="\t")
        for row in reader:
            item = {
                "id": row["id"],
                "naam": row["naam"],
                "locatie": row["locatie"],
                "provincie": row["provincie"],
                "gemeente": row["gemeente"],
                "is_vastgesteld": row["is_vastgesteld"],
                "is_beschermd": row["is_beschermd"],
                "datering": row["datering"],
                "gebeurtenissen": row["gebeurtenissen"],
                "disciplines": row["disciplines"],
                "dataverantwoordelijke": row["dataverantwoordelijke"],
            }
            data.append(item)

    return data


def main():
    print("main")


if __name__ == "__main__":
    main()
