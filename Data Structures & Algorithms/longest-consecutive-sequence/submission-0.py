class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #convert the list to set
        num_set = set(nums)
        max_len = 0

        #iterate through each number in the set
        for num in num_set:

            #only starts counting if the nun is in the start of the sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                #Count consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    length += 1

                #update max_len if this sequence is longer
                if length > max_len:
                    max_len = length

        return max_len