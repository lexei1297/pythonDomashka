def can_shift_to_goal(s, goal):
    # Check if the lengths of the strings are the same
    if len(s) != len(goal):
        return False

    # Create a new string by repeating s twice
    double_s = s + s

    # Check if goal is a substring of the new string
    if goal in double_s:
        return True
    else:
        return False


# Example usage
s = "abcde"
goal = "bcdea"
print(can_shift_to_goal(s, goal))  # Output: True