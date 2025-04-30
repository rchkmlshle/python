"""
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.
"""
from typing import List 
import bisect
class Solution:
    #o[n], sliding window
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_=max(nums)
        count=0
        left=0
        total=0

        for right in range(len(nums)):
            if nums[right]==max_:
                count+=1

            #valid window until value of k
            # slide left to find additional subarrays
            while count >=k:
                if nums[left] ==max_:
                    count -=1
                left+=1
            total+=left
        return total

    #binary search, constraint sorted array
    #https://docs.python.org/3/library/bisect.html
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left=bisect.bisect_left(nums, target)
        right=bisect.bisect_right(nums, target)

        return(right-left)*2 >len(nums)

    def findInteger25pc(self, arr: List[int]) -> int:
        n=len(arr)
        candidates=[arr[n//4], arr[2*n//4], arr[3*n//4]]
        def count(x):
            first=bisect.bisect_left(arr,x)
            last=bisect.bisect_right(arr,x) - 1
            return last-first +1
        for x in candidates:
            if count(x)*4 >n:
                return x
        assert(False)


def main():
    nums = [1,3,2,3,3]
    k = 2   
    sln1=Solution.countSubarrays(nums, k)
    sln2=Solution.isMajorityElement(nums,k)

if __name__== '__main__':
    main()
    