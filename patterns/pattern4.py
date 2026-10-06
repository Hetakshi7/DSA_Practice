"""
Question: Pattern
1
22
333 for n=3
Link: https://takeuforward.org/practice/dsa/pattern-4
"""
class Solution:
    def pattern4(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(i, end="")
            print()