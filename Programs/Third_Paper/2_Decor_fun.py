def record_calls(func):
    def wrapper():
        wrapper.call_count += 1
        return func()
    wrapper.call_count = 0
    return wrapper

@record_calls
def my_function():
    print("Decorator Called Here...")



# my_function()
# my_function()
print(my_function.call_count)  # Output: 2

