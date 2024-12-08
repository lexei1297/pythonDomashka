class StringList:
    def __init__(self, *args):
        # Initialize an empty list to store strings
        self.data = []
        # Convert all input arguments to strings and add to the list
        for item in args:
            self.data.append(str(item))

    def __iter__(self):
        # Return an iterator for the list
        return iter(self.data)

    def __repr__(self):
        # Provide a string representation of the list
        return f"StringList({self.data})"


# Usage example
my_string_list = StringList(1, 1.0, ["a", "b", "c"])

for el in my_string_list:
    assert type(el) == str
