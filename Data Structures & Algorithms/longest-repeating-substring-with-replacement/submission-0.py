class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_count = 0
        left = 0
        result = 0

        for right in range(len(s)):

            idx = ord(s[right]) - ord('A')
            count[idx] += 1

            if count[idx] > max_count:
                max_count = count[idx]

            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            if (right- left + 1) > result:
                result = right - left + 1

        return result

