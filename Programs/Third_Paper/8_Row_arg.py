class Row:
    def __init__(self, **kwargs):           # this __init__ method that accepts any number of keyword arguments using the **kwargs syntax
        for key, value in kwargs.items():   # for loopis use  to iterate over all the key-value pairs in the kwargs dictionary
            setattr(self, key, value)       #Sets the named attribute on the given object to the specified value.




row = Row(a=1, b=2, c="hello")
print(row.a)                    # Output: 1
print(row.b)                    # Output: 2
print(row.c)                    # Output: hello
