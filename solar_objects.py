# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11

class Body:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self):

        self.type = "planet"

        self.m = 1
        """Масса звезды"""

        self.x = 0
        """Координата по оси **x**"""

        self.y = 0
        """Координата по оси **y**"""

        self.vx = 0
        """Скорость по оси **x**"""

        self.vy = 0
        """Скорость по оси **y**"""

        self.fx = 0
        """Сила по оси **x**"""

        self.fy = 0
        """Сила по оси **y**"""

        self.r = 5
        """Радиус звезды"""

        self.color = (255,0,0)
        """Цвет звезды"""

    def move(self, dt):
        '''Меняет скорость и координату за малый промежуток dt'''

        self.vy += self.fy / self.m * dt
        self.vx += self.fx / self.m * dt
        self.y += self.vy * dt
        self.x += self.vx * dt

    def distance_check(self, x , y , rad):
        '''
        Считает расстояние от тела до тела
        '''
        distance_q = (x - self.x) ** 2 + (y - self.y) ** 2
        if distance_q < (self.r + rad) ** 2:
            return False
        else:
            return True

    def field(self , x , y):
        '''
        Считает поле в заданной точке
        x, y - координаты точки
        '''
        distance_q = (x - self.x) ** 2 + (y - self.y) ** 2
        ex = (self.x - x) / (distance_q)**(0.5)
        ey = (self.y - y) / (distance_q)**(0.5)
        grav_field = gravitational_constant * self.m / (distance_q)
        return [grav_field * ex, grav_field * ey]


if __name__ == "__main__":
    print("This module is not for direct call!")
