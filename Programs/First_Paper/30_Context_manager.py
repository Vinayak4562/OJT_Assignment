# Context managers are used to set up and tear down temporary contexts
# The enter (setup) logic - this runs right before the nested code block executes
# The exit (teardown) logic - this runs right after the nested code block is done

# obj = open(r"C:\Users\vinay\OneDrive\Desktop\OJT_ASSIGNMENT\Programs\First_Paper\newFile.txt","r")
# # print(obj.closed())
# print(obj.read())
# obj.close()
# # print(obj.closed())


# with open(r"C:\Users\vinay\OneDrive\Desktop\OJT_ASSIGNMENT\Programs\First_Paper\newFile.txt", "r") as obj:
#     print(obj.read())    

# with open(r"C:\Users\vinay\OneDrive\Desktop\OJT_ASSIGNMENT\Programs\First_Paper\newFile.txt", "w") as obj:
#     obj.write("hi this is from w mode")

# with open(r"C:\Users\vinay\OneDrive\Desktop\OJT_ASSIGNMENT\Programs\First_Paper\newFile.txt", "a") as obj:
#     print("This will append in file....")  

class Context_manager:
    def __init__(self):
        print("init method called here...!")

    def __enter__(self):
        print("Enter method is calledhere...!")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exit method called here...!")

with Context_manager() as manager:
    print("Context manager called here....!")
    


