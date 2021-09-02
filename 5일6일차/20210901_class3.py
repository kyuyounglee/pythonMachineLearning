class Animal:
    count = 0
    def __init__(self, name, type, number =0):
        self.name = name
        self.type = type
        self.number = number
        Animal.count += 1
        # self.count = count

    # return 문을 사용해야 한다
    def __str__(self):
        return "name : {}, type : {}".format(self.name,self.type)

    def __eq__(self, other):
        return self.name == other.name
aa = Animal("개", "아메리카블리", 120)
a = Animal("개", "아메리카블리", 1)
b = Animal("개", "불독", 2)
print(str(a))
print(a == b)
print(a.number)  # 1
print(b.number)  # 2
a.number = 100
Animal.count = 100
print(b.number)
print(b.count)

