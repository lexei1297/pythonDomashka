class StringList:
    def __init__(self, *args):
        self._data = [str(arg) for arg in args]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        return str(self._data)

my_string_list = StringList(3, 4.0, ["d", "f", "y"])

for el in my_string_list:
    assert type(el) == str

print(my_string_list)