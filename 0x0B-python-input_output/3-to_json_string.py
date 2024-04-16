#!/usr/bin/python3
"""Contains a func that returns a JSON repr. of an object"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)"""
    return json.dumps(my_obj)
