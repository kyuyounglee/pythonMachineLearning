class CustomException(Exception):
    def __init__(self, message, value):
        # Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return "{} : {}".format(self.message, self.value)

try:
    print(1+2)
    print(1+2)
    print(1/0)
    print(1+2)
except Exception as e:
    print(e)
    raise CustomException("페이지 찾을수 없음", 404)


