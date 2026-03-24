# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:16:41 2026

@author: Pradnya Jadhav
"""

file = open("attendance.txt", "a")

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    status = input("Present/Absent: ")
    file.write(name + " - " + status + "\n")

file.close()

 
