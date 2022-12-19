class ParentClass:
    @classmethod
    def metod(cls, arg):
        print("%s classmetod. %d " % (cls.__name__,arg))
    @classmethod
    def call_original_metod(cls):
        cls.metod(5)
    def call_class_metod(self):
        self.metod(10)
class ChildClass(ParentClass):
    @classmethod
    def call_original_metod(cls):
        cls.metod(6)

ParentClass.metod(0)
ParentClass.call_original_metod()

ChildClass.metod(0)
ChildClass.call_original_metod()

my_obj = ParentClass()
my_obj.metod(1)
my_obj.call_class_metod()

