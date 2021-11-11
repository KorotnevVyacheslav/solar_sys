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

        self.color = (0,0,0)
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
        electric_field = gravitational_constant * self.m / distance_quadratic
        return electric_field


def collision_check(body_1 , body_2):
    return not body_1.distance_check(body_2.x , body_2.y , body_2.r)


def collision(body_1, body_2):
    body_new = Body()
    body_new.m = body_1.m + body_2.m
    body_new.r = (body_1.r ** 3 + body_2.r ** 3) ** (1/3)
    body_new.vx = (body_1.vx * body_1.m + body_2.vx * body_2.m) / body_new.m
    body_new.vy = (body_1.vy * body_1.m + body_2.vy * body_2.m) / body_new.m
    body_new.x = (body_1.x * body_1.m + body_2.m * body_2.x) / body_new.m
    body_new.y = (body_1.y * body_1.m + body_2.m * body_2.y) / body_new.m
    body_new.color = choice(body_1.color , body_2.color)
    body_new.fx = body_1.fx + body_2.fx
    body_new.fy = body_1.fy + body_2.fy
    return body_new


if __name__ == "__main__":
    print("This module is not for direct call!")
