class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Anagrams must have the same length.
        if len(s) != len(t):
            return False

        # Create a frequency map of characters in s.
        s_counts = {}
        for char in s:
            s_counts[char] = s_counts.get(char, 0) + 1

        # Decrement the frequency for each character in t.
        # If a character in t is not in our map or its count is
        # already zero, they are not anagrams.
        for char in t:
            if s_counts.get(char, 0) == 0:
                return False
            s_counts[char] -= 1

        return True