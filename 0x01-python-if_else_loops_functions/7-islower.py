#!/bin/bash
def islowe(c):
    if ord(c) <= ord('Z') and ord(c) >= ord('A'):
        return False
    else:
        return True
