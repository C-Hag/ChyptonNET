#!/bin/python3

months = open('months.txt')

print(months.readlines())
months.seek(0)
print(months.readlines())

months.close()