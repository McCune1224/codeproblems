class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        
        for letter in s:
            if letter not in substring:
                substring += letter
                print(f"Added {letter}")
            else:
                print(f"{letter} is in substring already")
                break
        print(len(substring))
        return len(substring)
       
sol = Solution()

sol.lengthOfLongestSubstring("abccfouhr")
