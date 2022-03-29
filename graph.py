import math

import matplotlib.pyplot as plt


class MyCircle:
    def __init__(self, x, y, radius, diameter=0, color="red"):
        self.position = x, y
        self.radius = radius

        if diameter != 0:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            self.diameter = radius * 2
        self.area = math.pi * (pow(radius, 2))
        self.color = color

    def __add__(self, other):
        x1, y1 = self.position
        x2, y2 = other.position
        return MyCircle(x1 + x2, y1 + y2, self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


circles = []


def sort_circles():
    circles.sort()
    y = 0
    for i in range(len(circles)):
        circles[i].position = 0, y
        next_r = circles[i+1].radius if i+1 < len(circles) else 0
        y += circles[i].radius + next_r + 0.1


def add_circle(circle: MyCircle):
    circles.append(circle)


def draw_figure():
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    ax.margins(0.05)
    for c in circles:
        to_draw = plt.Circle(c.position, c.radius, color=c.color, fill=False)
        ax.add_patch(to_draw)
    plt.show()
