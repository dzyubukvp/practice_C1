# класс, который представляет собой значение угла

class Angle:
    def __init__(self, angle = 0) -> None:
        self.__angle = angle
    @property
    def angle(self):
        return self.__angle
    @angle.setter
    def angle(self, angle):
        self.__angle = angle
    @property
    def rad(self):
        return (self.__angle/180.0)*3.14

if __name__=="__main__":
    angle = Angle(30)

    print(f'{angle.angle} : {angle.rad}')