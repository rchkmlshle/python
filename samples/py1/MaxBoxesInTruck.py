from typing import List 
"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

"""
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        capacity = 0
        
        for box, unit in boxTypes:
            if truckSize >= box:
                truckSize -= box
                capacity += box*unit
            else:
                print(capacity)

                capacity += truckSize*unit
                break
        return capacity
    
def main():
    sln1=Solution()
    print( sln1.maximumUnits(
        #[[1,3],[2,2],[3,1]], 4
        [[5,10],[2,5],[4,7],[3,9]], 10
    ))
   


if __name__=='__main__':
    main()