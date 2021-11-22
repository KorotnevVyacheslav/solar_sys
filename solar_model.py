# coding: utf-8
# license: GPLv3

from solar_vis import DrawableObject
from solar_objects import Body
from graph import Graph
from random import choice

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.fx = 0
    body.fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        else:
            grav_field = obj.field(body.x, body.y)
            body.fx += body.m * grav_field[0]
            body.fy += body.m * grav_field[1]


def global_collision_check(space_objects, factor):
    '''
    Проверка всех планет на столкновения
    '''
    def collision_check(body_1dr , body_2dr, scale_factor):
        '''
        Проверяем, не столкнулись ли тела
        '''
        body_1 = body_1dr.obj
        body_2 = body_2dr.obj
        return not body_1.distance_check(body_2.x, body_2.y, body_2.r, scale_factor)

    def collision(body_1_, body_2_):
        '''
        Столкновение если планеты касаются
        Планеты объединяются в одну
        Учтен закон сохранения импульса
        '''
        body_1 = body_1_.obj
        body_2 = body_2_.obj
        body_new = Body()
        body_new.m = body_1.m + body_2.m
        body_new.r = (body_1.r ** 3 + body_2.r ** 3) ** (1/3)
        body_new.vx = (body_1.vx * body_1.m + body_2.vx * body_2.m) / body_new.m
        body_new.vy = (body_1.vy * body_1.m + body_2.vy * body_2.m) / body_new.m
        body_new.x = (body_1.x * body_1.m + body_2.m * body_2.x) / body_new.m
        body_new.y = (body_1.y * body_1.m + body_2.m * body_2.y) / body_new.m
        body_new.fx = body_1.fx + body_2.fx
        body_new.fy = body_1.fy + body_2.fy
        body_new.number = -1
        return body_new


    for body in space_objects:
        body_exists = True
        for obj_ in space_objects:
            if body == obj_:
                continue
            if collision_check(body , obj_, factor):
                space_objects.append(DrawableObject(collision(body, obj_)))
                space_objects.remove(body)
                space_objects.remove(obj_)
                body_exists = False
            if not body_exists:
                break


if __name__ == "__main__":
    print("This module is not for direct call!")
