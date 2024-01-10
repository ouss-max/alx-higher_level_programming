#!/usr/bin/python3
"""Function to insert text into a file."""


def append_after(filename="", search="", new_text=""):
    """Insert text after each line containing a given string.

    """
    text = ""
    
    with open(filename) as file_read:
        for line in file_read:
            text += line
            if search in line:
                text += new_text
    with open(filename, "w") as file_write:
        file_write.write(text)