# coding: utf-8
# license: GPLv3

from solar_objects import Body
from solar_vis import DrawableObject

COLORS = {
            'red' : (255, 0, 0),
            'black' : (0, 0, 0),
            'green' : (0, 255, 0),
            'blue' : (0, 0, 255),
            'orange' : (255, 165, 0),
            'yellow' : (255, 255, 0),
            'white' : (255, 255, 255),
            'gray' : (128, 128, 128)
        }


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            body = Body()
            parse_parameters(line, body)

    return [DrawableObject(obj) for obj in objects]


def parse_parameters(line, body):
    """Считывает данные о звезде из строки.

    Входная строка должна иметь слеюущий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.

    **star** — объект звезды.
    """

    body.type = line[0]
    body.r = line[1]
    color = line[2]
    body.color = COLORS.get(color)
    body.m = line[3]
    body.x = line[4]
    body.y = line[5]
    body.vx = line[6]
    body.vy = line[7]


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            line = [] * 8
            line[0] = body.type
            line[1] = body.r
            line[2] = body.color
            line[3] = body.m
            line[4] = body.x
            line[5] = body.y
            line[6] = body.vx
            line[7] = body.vy
            print(out_file, line)


if __name__ == "__main__":
    print("This module is not for direct call!")
