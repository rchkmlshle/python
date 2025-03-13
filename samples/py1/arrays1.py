from typing import List 
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos= sum( 1 for x in nums if x>0)
        neg=sum(1 for x in nums if x <0)
        return(max(pos, neg))




def main():
    sln1=Solution()
    print(sln1.maximumCount([-2,-1,-1,1,2,3]))
    


if __name__=='__main__':
    main()