#!/usr/bin/python3
"""Contains a function that creates an obj from a json file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
