# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:01:20 2026

@author: Pradnya Jadhav
"""

# List of purchased items
items = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Item frequency:", frequency)

