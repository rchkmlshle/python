from typing import List
import operator
from collections import Counter
class Solution:
    def sortArrayByParity( nums: List[int]) -> List[int]:
        head= [x for x in nums if x%2 ==0]
        end=[x for x in nums if x%2 !=0]
        return head+end
    
    def sortArrayByParityII(nums: List[int]) -> List[int]:
        even= [x for x in nums if x%2 ==0]
        odd=[x for x in nums if x%2 !=0]
        res=[]
        for i in range(len(nums)):
            if i%2==0:
                res.append(even[i//2])
            else:
                res.append(odd[i//2])
        
        return res

    def frequencySort(nums: List[int]) -> List[int]:
        """
        set_nums=set(nums)
        count_nums={}
        for item in set_nums:
            count_nums[item]=nums.count(item)
            print(count_nums)
        count_nums_sorted=sorted(count_nums.items(),
                                 key=lambda x: (x[1], -x[0])) #x[0]:key desc, list of lists
        print(count_nums_sorted)
        #[(1,1),(3,2),(2,2)]
        res=[]
        for item in count_nums_sorted:
            for i in range(item[1]):
                res.append(item[0])
        return res
        """
        count=Counter(nums)
        #Counter({2: 2, 3: 2, 1: 1}
        sorted_num=sorted(count.items(), key=lambda x:(x[1],-x[0]))
        
        ans=[]
        for num, val in sorted_num:
            ans.extend([num]*val)

        return ans

def main():
    listA=[3,1,2,4]
    listB=[4,2,5,7]
    listC=[2,3,1,3,2]
    #print(Solution.sortArrayByParity(listA))
    #print(Solution.sortArrayByParityII(listB))
    #print(Solution.frequencySort(listC))

if __name__=='__main__':
    main()