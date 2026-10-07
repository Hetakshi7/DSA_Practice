"""
Question: Pattern
***
**
* n=3
Link: https://takeuforward.org/practice/dsa/pattern-5
"""
class Solution:
    def pattern5(self, n):
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end="")
            print()