"""Leap Year"""

def print_learyear(year):
    if (year%400 == 0) or (year%4 == 0) and (year%100 !=0):
        return "Leap Year"
    else:
        return "Not Leap Year"    