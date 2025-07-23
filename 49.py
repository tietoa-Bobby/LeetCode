from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # A dictionary where keys are sorted strings (the canonical form)
        # and values are lists of the original strings that match that form.
        # defaultdict(list) simplifies appending to lists for new keys.
        anagram_groups = defaultdict(list)

        for s in strs:
            # Sort the string to get its canonical representation.
            key = "".join(sorted(s))
            anagram_groups[key].append(s)

        # The values of the dictionary are the grouped anagrams.
        return list(anagram_groups.values())