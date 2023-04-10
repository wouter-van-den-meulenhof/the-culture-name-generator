"""
This script utilizes the asset_randomizer class to randomize a provided number
of names and outputs them to the screen in the desired format.

Usage:
    python3 ./main.py \
        --count 10 \
        --format json

Author:
    Wouter van den Meulenhof, 9th of april 2023
"""

import argparse
from classes import asset_randomizer

# Process script input
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-c", "--count", type = int,
    help = "Amount of names to generate, using this script."
)
arg_parser.add_argument(
    "-f", "--format", type = str,
    help = "Desired format for return value: semicolon_delimited_string, comma_delimited_string or json."
)
arguments = arg_parser.parse_args()

# Generate names
names_generated = asset_randomizer.assets.generate_names(
    amount = arguments.count,
    desired_format = arguments.format
)

# Output names
print(names_generated)
