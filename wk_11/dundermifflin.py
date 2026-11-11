

class SuperList:

    def __init__(self, val):
        self.__lst = [x for x in range(val)]
        self.__index = 0
        self.__count = 0

    def add_to_end(self, val):
        if val < 0:
            return
        self.__lst.append(val)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__count >= len(self.__lst):
            self.__index = 0
            self.__count = 0
            raise StopIteration
        data = self.__lst[self.__index]
        self.__index += 3
        self.__index = self.__index % len(self.__lst)
        self.__count += 1
        return data

if __name__ == "__main__":
    nums = [0, 1, 2, 3]
    it_nums = iter(nums)
    print(next(it_nums))
    print(next(it_nums))
    print()
    lst = SuperList(10)
    for i in lst:
        print(i)

    for i in lst:
        print(i)