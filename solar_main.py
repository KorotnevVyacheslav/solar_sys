# coding: utf-8
# license: GPLv3

import pygame as pg
from solar_vis import *
from solar_model import *
from solar_input import *
from solar_objects import *
from graph import *
import thorpy
import time
import numpy as np

#хуй
#возмущен непониманием этого кода


timer = None

alive = True

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

model_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

scale_factor = 1

time_scale = 400000.0
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
space_graphs = []
"""Список космических объектов."""

def execution(delta, screen):
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global model_time
    global displayed_time
    global space_objects
    global scale_factor

    global_collision_check(space_objects, scale_factor)
    for dr in space_objects:
        calculate_force(dr.obj , [spobj.obj for spobj in space_objects])
    for dr in space_objects:
        dr.move(delta)
        dr.draw(screen)
    model_time += delta
    iter = 0
    for graph in space_graphs:
        for body_1 in space_objects:
            if body_1.obj.number == iter:
                graph.data_add(model_time, body_1.obj, space_objects[0].obj)

        iter += 1




def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True

def pause_execution():
    print(1)
    for graph in space_graphs:
        graph.plotting_graphs()
    #space_graphs[0].plotting_graphs()
    global perform_execution
    perform_execution = False

def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """

    global alive
    alive = False

def open_file():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global browser
    global model_time
    global scale_factor

    model_time = 0.0
    in_filename = "solar_system.csv"
    space_objects = read_space_objects_data_from_file(in_filename)

    #space_graphs = [Graph()] * len(space_objects)
    for i in range(len(space_objects)):
        space_graphs.append(Graph())

    distances = []
    for obj in space_objects:
        distances.append
    max_distance = max([max(abs(obj.obj.x), abs(obj.obj.y)) for obj in space_objects])
    scale_factor = calculate_scale_factor(max_distance)

def handle_events(events, menu):
    global alive
    for event in events:
        menu.react(event)
        if event.type == pg.QUIT:
            alive = False

def slider_to_real(val):
    return np.exp(5 + val)

def slider_reaction(event):
    global time_scale
    time_scale = slider_to_real(event.el.get_value())

def init_ui(screen):
    global browser
    slider = thorpy.SliderX(100, (-10, 10), "Simulation speed")
    slider.user_func = slider_reaction
    button_stop = thorpy.make_button("Quit", func=stop_execution)
    button_pause = thorpy.make_button("Pause", func=pause_execution)
    button_play = thorpy.make_button("Play", func=start_execution)
    timer = thorpy.OneLineText("Seconds passed")

    button_load = thorpy.make_button(text="Load a file", func=open_file)

    box = thorpy.Box(elements=[
        slider,
        button_pause,
        button_stop,
        button_play,
        button_load,
        timer])
    reaction1 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=slider_reaction,
                                event_args={"id":thorpy.constants.EVENT_SLIDE},
                                params={},
                                reac_name="slider reaction")
    box.add_reaction(reaction1)

    menu = thorpy.Menu(box)
    for element in menu.get_population():
        element.surface = screen

    box.set_topleft((0,0))
    box.blit()
    box.update()
    return menu, box, timer

def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """

    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button
    global perform_execution
    global timer

    print('Modelling started!')
    physical_time = 0

    pg.init()

    width = 1000
    height = 700
    screen = pg.display.set_mode((width, height))
    last_time = time.perf_counter()
    drawer = Drawer(screen)
    menu, box, timer = init_ui(screen)
    perform_execution = True

    while alive:
        handle_events(pg.event.get(), menu)
        cur_time = time.perf_counter()
        if perform_execution:
            execution((cur_time - last_time) * time_scale, screen)
            text = "%d seconds passed" % (int(model_time))
            timer.set_text(text)

        last_time = cur_time
        drawer.update(space_objects, box)
        time.sleep(1.0 / 60)

    print('Modelling finished!')

if __name__ == "__main__":
    main()
