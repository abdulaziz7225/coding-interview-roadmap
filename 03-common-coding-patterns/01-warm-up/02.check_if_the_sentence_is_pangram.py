# Solution 1: Hash Set
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        
        for char in sentence:
          if char.isalpha():
            letters.add(char.lower())
        return len(letters) == 26

# Time Complexity: O(n)
# Space Complexity: O(26) ==> O(1)


# Solution 2: Bit Manipulation
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = (1 << 26) - 1
        temp = 0

        for char in sentence:
            if char.isalpha():
                char = char.lower()
                temp |= 1 << (ord(char) - ord("a"))
                if temp == pangram:
                    return True
        
        return False

# Time Complexity: O(n)
# Space Complexity: O(1)
