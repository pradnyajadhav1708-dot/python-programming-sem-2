# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:58:12 2026

@author: Pradnya Jadhav
"""
# Inventory dictionary
inventory = {
    "apple": 10,
    "banana": 20
}

item = input("Enter item name: ")
quantity = int(input("Enter quantity to add: "))

if item in inventory:
    inventory[item] += quantity
else:
    inventory[item] = quantity

print("Updated inventory:", inventory)

