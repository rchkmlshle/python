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

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_names=dict(zip(heights,names))
        sorted_heights=sorted(height_names.items(),  key=lambda x:-x[0])
        names_sorted=[item[1] for item in sorted_heights]
        return names_sorted
    
    def sortbyIndex(nums: List[int]):
        """
        Input: nums = [3,4,5,1,2]
        Output: 2
        Explanation: 
        After the first right shift, nums = [2,3,4,5,1].
        After the second right shift, nums = [1,2,3,4,5].
        Now nums is sorted; therefore the answer is 2.
        """
        nums_sorted=sorted(nums)
        if nums==nums_sorted:
            return 0

        for i in range(len(nums)):
            nums=nums[-1:]+nums[:-1]
            if nums==nums_sorted:
                return i+1
        return -1
    
    def mergeSort(nums1: List[int], nums2: List[int]) -> None:
        m=len(nums1)
        n=len(nums2)
        nums1[m:]=nums2
        nums1.sort()

    def sortSentence(s: str) -> str:
        list1=s.split(" ")
        s_dict={}
        for item in list1:
            
            s_dict[item[-1]]=item[:-1]
        sorted_list=sorted(s_dict.items(), key=lambda x:x[0] )
        words=[item[1] for item in sorted_list]
        words_=" ".join(words)
        
        return words_
       
def main():
    listA=[3,1,2,4]
    listB=[4,2,5,7]
    listC=[2,3,1,3,2]
    list_sentence="is2 sentence4 This1 a3"
    #print(Solution.sortArrayByParity(listA))
    #print(Solution.sortArrayByParityII(listB))
    #print(Solution.frequencySort(listC))
    print(Solution.sortSentence(list_sentence))

if __name__=='__main__':
    main()