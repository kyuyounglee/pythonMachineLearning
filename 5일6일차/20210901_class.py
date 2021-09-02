class Test:
    name = "test"  # class variable
    def __init__(self):
        self.name2 = 'name'  # instance variable
        self.name = 'abc'
        # Test.name = 'abc'

t = Test()
print(t.name, t.name2)
print(Test.name)
