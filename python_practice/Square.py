class Square:
    _a=None
    def __init__(self,a):
        if a>0:
            self._a = a**2
    @property
    def a(self) ->int:
        return self._a

    @a.setter
    def a(self, value):
        if value>0:
            self._a = value


if __name__=="__main__":
    stor = Square(33)
    ss = stor._a

    print(ss)

