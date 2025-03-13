from typing import List 
class Solution:

    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)
        def good(start, d):
            arr = nums[:]
            current=start
            
            while 0 <= current < N:
                if arr[current] == 0:
                    current += d
                else:
                    arr[current] -= 1
                    d *= -1
                    current += d 
            return  all(x == 0 for x in arr )
        total=0
        for i in range(N):
            if nums[i]==0:
                total += int(good(i,1) + good(i, -1))
        return total

    def minOperationsEqualAmount(self, nums: List[int]) -> int:
        """
        You are given a non-negative integer array nums. In one operation, you must:

        Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
        Subtract x from every positive element in nums.
        Return the minimum number of operations to make every element in nums equal to 0.
        """
        nums.sort()
        count =0
        current=0
        for x in nums:
            x-=current
            if x >0:
                current+=x
                count+=1
        return count
        
def main():
    sln1=Solution()
    #print(sln1.countValidSelections([1,5,0,3,5]))
    print(sln1.minOperationsEqualAmount([1,5,0,3,5]))

    


if __name__=='__main__':
    main()