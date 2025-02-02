# coding: utf-8
# license: GPLv3

from solar_objects import Body
from solar_vis import DrawableObject
import csv

COLORS = {
            'red' : (255, 0, 0),
            'black' : (0, 0, 0),
            'green' : (0, 255, 0),
            'blue' : (0, 0, 255),
            'orange' : (255, 165, 0),
            'yellow' : (255, 255, 0),
            'white' : (255, 255, 255),
            'gray' : (128, 128, 128),
            'cyan' : (0, 255, 255)
        }


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    number = 0
    array = []
    with open(input_filename, newline="\n") as csvfile:
        ar = csv.reader(csvfile, delimiter=" ")
        for row in ar:
            if len(row) == 0:
                continue
            elif (list(row))[0] == "#":
                continue
            array.append(row)

    #print(array)

    objects = []
    for line in array:
        body = Body()
        parse_parameters(line, body, number)
        objects.append(body)
        number += 1

    return [DrawableObject(obj) for obj in objects]


def parse_parameters(line, body, number):
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
    body.r = float(line[1])
    color = line[2]
    body.color = COLORS.get(color)
    body.m = float(line[3])
    body.x = float(line[4])
    body.y = float(line[5])
    body.vx = float(line[6])
    body.vy = float(line[7])
    body.number = number


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
        for body in space_objects:
            line = ""
            line += body.type + " " + str(body.r) + " " + str(body.color) + " " + str(body.m) + " " + str(body.x) + " " + str(body.y) + " " + str(body.vx) + " " + str(body.vy)
            out_file.write(line + "\n")

#read_space_objects_data_from_file("solar_system.csv")

if __name__ == "__main__":
    print("This module is not for direct call!")
