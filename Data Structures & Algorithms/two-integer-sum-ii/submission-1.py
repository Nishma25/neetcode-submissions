class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap = {}
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in hashmap:
        #         return [hashmap[diff]+1, i+1]
        #     hashmap[numbers[i]] = i

        left, right = 0,len(numbers)-1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum > target:
                right = right -1
            
            elif curr_sum < target:
                left = left + 1
            
            else:
                return [left+1,right+1]
            
        return []
            