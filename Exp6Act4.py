# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:23:36 2026

@author: Pradnya Jadhav
"""

file = open("complaints.txt", "r")

print("All Complaints:")
for line in file:
    print(line.strip())

file.close()