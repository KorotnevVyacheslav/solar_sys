import numpy as np
import matplotlib.pyplot as plt

from solar_objects import Body
from solar_vis import DrawableObject

class Graph:
    def __init__(self):
        self.speed_array = []
        self.distance_array = []
        self.time_array = []
        self.existion = True

    def data_add(self , time, body_1, body_2):
        velocity = np.sqrt(body_1.vx ** 2 + body_1.vy ** 2)
        distance = np.sqrt((body_1.x - body_2.x) ** 2 + (body_1.y - body_2.y) ** 2)
        self.speed_array.append(velocity)
        self.distance_array.append(distance)
        self.time_array.append(time)

    def plotting_graphs(self):
        print(1)
        plt.plot(self.speed_array, self.distance_array)
        plt.show()
        plt.plot(self.speed_array, self.time_array)
        plt.show()
        plt.plot(self.time_array, self.distance_array)
        plt.show()
