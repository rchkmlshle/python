
from collections import defaultdict
class SortLikeAGenius:
    def bubble_sort(nums, order):
        """
        Sorts a list of elements using the Comb Sort algorithm.

        Args:
            nums (list): A list of comparable elements.

        Returns:
            list: The sorted list in ascending order.
            
        """
        if order=="asc":
            for iter_ in range(len(nums)):
                #[41, 32, 15, 19, 22] 0-41
                for idx in range(iter_):
                    if nums[idx] > nums[iter_]:
                            temp=nums[idx] 
                            nums[idx] = nums[iter_]
                            nums[iter_] = temp
        else:
             for iter_ in range(len(nums)):
                #[41, 32, 15, 19, 22] 0-41
                for idx in range(iter_):
                    if nums[idx] < nums[iter_]:
                            temp=nums[idx] 
                            nums[idx] = nums[iter_]
                            nums[iter_] = temp
             
        return nums
    def arrayhashmap(arr1, arr2):
        arr2_set=set(arr2)
        arr1_count=defaultdict(int)
        print(arr1_count)
        end = []
        for n in arr1:
            if n not in arr2_set:
                end.append(n) #items not requiring precedence.
            arr1_count[n] += 1 #count instances
        print(arr1_count)
        end.sort()
        res=[]
        for n in arr2: # items requiring precedence
            for _ in range(arr1_count[n]):
                 res.append(n)
        return res + end
                 

def main():             
    grads=[2,3,1,2,2,4,6,7,9,2,19]
    grad_power=[2,1,4,3,9,6] #result [2,2,2,1,4,3,3,9,6,7,19] O(n)
    print(SortLikeAGenius.arrayhashmap(grads, grad_power))

    #[55, 64, 19, 28]
    #print(SortLikeAGenius.bubble_sort(grads, "asc"))

if __name__=='__main__':
     main()