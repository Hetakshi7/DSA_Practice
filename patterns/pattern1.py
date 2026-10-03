"""
Pattern 1: Print Solid Square 
Link: https://www.geeksforgeeks.org/problems/print-square-wall-1605682270/1
"""
n = int(input())
for i in range(n):
    for j in range(n):
        print("* ",end="")
    print()