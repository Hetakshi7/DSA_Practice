"""
Question: Print Right Half Pyramid Star Pattern
Link: https://takeuforward.org/practice/dsa/pattern-2
"""
class Solution:
    def pattern2(self, n):
        for i in range(n):
            for j in range(i+1):
                print('*',end="")
            print()