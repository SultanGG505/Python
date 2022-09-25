class Point():
    pos_x = 0
    pos_y = 0

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def show_pos(self):
        print("Точка находится в", self.pos_x, "-", self.pos_y)

    def del_pos(self):  # обнулить точку
        self.pos_x = 0
        self.pos_y = 0

    def setPosX(self, x):  # изменить x отдельно
        self.pos_x = x

    def setPosY(self, y):  # изменить y отдельно
        self.pos_y = y

    def setPoint(self, x, y):  # задать точку целиком
        self.pos_x = x
        self.pos_y = y


newPoint = Point(1, 4)
newPoint.show_pos()
newPoint.del_pos()
newPoint.show_pos()
newPoint.setPosX(10)
newPoint.show_pos()
newPoint.setPosY(10)
newPoint.show_pos()
newPoint.setPoint(1000, 1000)
newPoint.show_pos()
