#!/bin/bash
	for i in range(10):
        for j in range(10):
            if i < j:
                print("{:d}{:d}".format(i, j), end="\n" if i ==8 and j ==9 else " ")
       