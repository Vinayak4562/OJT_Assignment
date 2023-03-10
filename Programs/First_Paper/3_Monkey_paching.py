class test:
    def get_data(self):
        print("Printing from test Class....!")
    def f1(self):
        self.get_data()

    def f2(self):
        self.get_data()
a = test()
# a.f1()
# a.f2()
def new_get_data(self):
    print("Printing from new_ger_data outside the Class....!")

test.get_data = new_get_data
print("After Monkey Paching....!")
a.f1()
a.f2()