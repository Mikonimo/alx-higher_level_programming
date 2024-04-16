#!/usr/bin/python3
"""Contains a func that writes an obj to a txt file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
