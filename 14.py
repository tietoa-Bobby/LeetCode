class Solution(object):
    def longestCommonPrefix(self, strs):
        # Edge case: if the list is empty, return an empty string
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for string in strs[1:]:
            #Trim the prefix until it matches the start of teh current string
            while not string.startswith(prefix):
                # Reduce the prefix by removing the last character
                prefix = prefix[:-1]
                # If the prefix is reduced to an empty string, no common prefix exists
                if not prefix:
                    return ""
        return prefix
        
        