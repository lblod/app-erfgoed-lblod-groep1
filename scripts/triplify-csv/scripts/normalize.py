# This file normalizes the json output files for provincies and gemeenten produced by Virtuoso to become
# more streamlined and easy to use.

import json

# Load mapping config from JSON file
with open("config/config.json", "r") as json_file:
    mapping_rules = json.load(json_file)