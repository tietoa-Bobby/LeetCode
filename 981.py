class TimeMap(object):

    def __init__(self):
        # Dictionary to store key -> list of (timestamp, value) pairs
        self.data = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.data:
            self.data[key] = []
        # Since timestamps are strictly increasing, we can just append
        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.data:
            return ""
        
        values = self.data[key]
        
        # Binary search for the largest timestamp <= given timestamp
        left, right = 0, len(values) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            
            if values[mid][0] <= timestamp:
                # This timestamp is valid, store the value and search for larger timestamp
                result = values[mid][1]
                left = mid + 1
            else:
                # This timestamp is too large, search smaller timestamps
                right = mid - 1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)