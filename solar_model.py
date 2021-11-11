# coding: utf-8
# license: GPLv3

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
        electric_field = obj.field(body.x, body.y)
        body.fx += body.m * electric_field[0]
        body.fy += body.m * electric_field[1]


def global_collision_check(space_objects):
    '''
    Проверка всех планет на столкновения
    '''
    def collision_check(body_1 , body_2):
        '''
        Проверяем, не столкнулись ли тела
        '''
        return not body_1.distance_check(body_2.x , body_2.y , body_2.r)

    def collision(body_1, body_2):
        '''
        Столкновение если планеты касаются
        Планеты объединяются в одну
        Учтен закон сохранения импульса
        '''
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


    for body in space_objects:
        body_exists = True
        for obj in space_objects:
            if body == obj:
                continue
            if collision_check(body , obj):
                space_objects.append(collision(body, obj))
                space_objects.remove(body)
                space_objects.remove(obj)
                body_exists = False
            if not body_exists:
                break


if __name__ == "__main__":
    print("This module is not for direct call!")
