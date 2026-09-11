
class Student:

    def __init__(self, name, uid):
        self.name = name
        # self._uid = uid
        self.__uid = uid

if __name__ == "__main__":
    jeff = Student('Jeff', 1)
    # print(jeff._Student__uid)
    print(jeff.__uid)