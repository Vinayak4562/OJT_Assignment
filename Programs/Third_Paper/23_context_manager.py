class suppress:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return self

    def __exit__(self, exc_value, exc_type, traceback):
        if exc_type == self.exc_type:
            return True

with suppress(NameError):
    print("Hi!")
    print("It's nice to meet you,", name)
    print("Goodbye!")

with suppress(TypeError):
    print("Hi!")
    print("It's nice to meet you,", name)
    print("Goodbye!")
