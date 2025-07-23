class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Combine position and speed into pairs (position, speed).
        cars = zip(position, speed)
        
        # Sort cars by position in descending order (closest to target first).
        sorted_cars = sorted(cars, key=lambda x: x[0], reverse=True)

        # Stack to store the arrival times of the fleets.
        # The top of the stack is the arrival time of the most recently formed fleet.
        stack = []

        for p, s in sorted_cars:
            # Calculate time for the current car to reach the target.
            time_to_arrive = float(target - p) / s

            # If the stack is empty, this is the first fleet.
            # If the current car takes longer to arrive than the fleet ahead of it,
            # it cannot catch up and thus forms a new fleet.
            if not stack or time_to_arrive > stack[-1]:
                stack.append(time_to_arrive)
        
        # The number of elements in the stack is the number of fleets.
        return len(stack)