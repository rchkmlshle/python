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
    def __init__(self, nums: List[int], target: int) -> int:
        self.nums=nums
        self.target=target
    def searchInsert(self) -> int:
        left, right = 0, len(self.nums)-1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] < self.target:
                left = mid +1
            elif self.nums[mid] > self.target:
                right = mid - 1
            else:
                return mid
        if self.nums[mid] < self.target:
            return mid + 1
        else:
            return mid
def main():
    listA=[1,3,5,6]
    sln1=Solution(listA, target=5)
    print(sln1.searchInsert())
    


if __name__=='__main__':
    main()