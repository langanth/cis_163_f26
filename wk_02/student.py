
class Student:

    def __init__(self, name: str, uid: int):
        self.name = name
        # self._uid = uid
        self.__uid = uid

    def set_uid(self, val: int) -> None:
        if not isinstance(val, int):
            raise TypeError
        if 10000000 <= val <= 99999999:
            self.__uid = val
        else:
            raise ValueError

    def get_uid(self) -> int:
        return self.__uid

    @property
    def name(self):
        if len(self.__middle_name) >= 1:
            st = f'{self.__last_name}, {self.__first_name} {self.__middle_name}'
        else:
            st = f'{self.__last_name}, {self.__first_name}'
        return st

    @name.setter
    def name(self, val):
        if isinstance(val, str):
            if len(val) >= 1:
                split_name = val.split()
                if len(split_name) > 2:
                    self.__first_name, self.__middle_name, self.__last_name = split_name
                else:
                    self.__first_name, self.__last_name = split_name
                    self.__middle_name = ''
            else:
                raise ValueError
        else:
            raise TypeError

    @name.deleter
    def name(self):
        self.__first_name = '*'
        self.__last_name = '*'
        self.__middle_name = '*'

    @property
    def email(self):
        return f'{self.__last_name.lower()}{self.__first_name.lower()[:2]}@mail.gvsu.edu'

if __name__ == "__main__":
    '''jeff = Student('Jeff', 1)
    # print(jeff._Student__uid)
    # print(jeff.__uid)
    jeff.set_uid(12345678)
    print(jeff._Student__uid)
    jeff.name = "Jeff Gerstmann"
    print(jeff.name)'''

    anthony = Student('Anthony W. Langley', 1)
    print(anthony.name)
    print(anthony.email)
    del anthony.name
    print(anthony.name)