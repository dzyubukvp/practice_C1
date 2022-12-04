class A:
    def getVal(self):
        return 5


class B(A):
    def getVal(self):
        return super().getVal() * 2


class C(B):
    def getVal(self):
        return super().getVal() * 2 * 2


class D(A):
    def getVal(self):
        return super().getVal() * 2 * 3


if __name__ == "__main__":
    a = D()
    print(a.getVal())