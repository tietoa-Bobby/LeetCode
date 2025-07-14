class Solution(object):
    def romanToInt(self, s):
        # Map of Roman numerals to their values
        roman_values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        # Initialise results
        result = 0
        # Iterate through the string
        for i in range(len(s)):
            # If this is not the last character and the current character is less than the next character
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i+1]]:
                # Subtract the value
                result -= roman_values[s[i]]
            else:
                # Add the value
                result += roman_values[s[i]]
        return result