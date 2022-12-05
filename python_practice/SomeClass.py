from REOP import ParentClass
class SomeClass:
    def __init__(self, someData) -> None:
        self.__internalData = someData
    @property
    def data(self):
        return self.__internalData-3
    @data.setter
    def data(self, value):
        self.__internalData = value ** 2

if __name__=="__main__":
    abr = SomeClass(5)

print(abr.data)
abr.data = 6
print(abr.data)
# Вызов через импорт из файла REOP.py класса ParentClass
ParentClass.metod(3)
ParentClass.call_original_metod()