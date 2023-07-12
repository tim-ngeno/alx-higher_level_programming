#!/usr/bin/python3
"""implementation of 7-add_item"""

import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

for x in argv[1:]:
    json_list.append(x)
# save the args to a json file
save_to_json_file(json_list, filename)
