#!/usr/bin/python3
# 6-from_json_string.py
"""SON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object"""
    return json.loads(my_str)
