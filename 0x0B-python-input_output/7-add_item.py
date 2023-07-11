#!/usr/bin/python3
"""implementation of 7-add_item"""

import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# add the program's arguments to a list
args = []
for x in argv[1:]:
    args.append(x)

filename = "add_item.json"

# save the args to a json file
save_to_json_file(args, filename)
load_from_json_file(filename)
