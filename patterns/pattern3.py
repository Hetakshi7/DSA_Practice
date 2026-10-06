"""
Question: Pattern
1
12
123 for n=3
Link: https://takeuforward.org/practice/dsa/pattern-3
"""
class Solution:
    def pattern3(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j ,end="")
            print()