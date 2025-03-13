"""
Companies
Given a sorted array of distinct integers and a target value, return the index if the target 
is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List  
# Import the List type from typing module for type hints.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        div = 1
        while x>=10*div:
            div *= 10
        while x:
            right = x % 10
            left = x // div
            if left !=right:
                return False
            x = (x%div) //10
            div = div /100
        return True
    
def main():
    sln1=Solution()
    print(sln1.isPalindrome(233256))
    


if __name__=='__main__':
    main()