#!/usr/bin/python3
"""7-add_item

This script adds all arguments to a Python list, and then save them to file.
"""
import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
args = sys.argv[1:]

if not os.path.exists(filename):
    save_to_json_file(args, filename)
else:
    obj = load_from_json_file(filename)
    obj.extend(args)
    save_to_json_file(obj, filename)
