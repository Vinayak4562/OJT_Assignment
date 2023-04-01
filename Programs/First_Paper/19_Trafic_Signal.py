def traffic_signal_decorator(func):
    def wrapper():
        print("RED : STOP")
        func()
        print("YELLOW : SLOW DOWN")
        func()
        print("GREEN : GO")
    return wrapper

@traffic_signal_decorator
def traffic_signal():
    pass

traffic_signal()


# RED : STOP
# YELLOW : SLOW DOWN
# RED : STOP
# GREEN : GO
# YELLOW : SLOW DOWN
# GREEN : GO