import numpy as np
from stl import mesh
import random


def triangle_func():
    data = np.zeros(1, dtype=mesh.Mesh.dtype)
    data['vectors'][0] = [[0, 0, 0], [1, 0, 0], [0, 1, 0]]
    mesh.Mesh(data).save('stls/triangle.stl')


def square_func():
    data = np.zeros(2, dtype=mesh.Mesh.dtype)
    data['vectors'][0] = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
    data['vectors'][1] = [[0, 0, 0], [1, 1, 0], [0, 1, 0]]
    mesh.Mesh(data).save('stls/square.stl')


def circle_func():
    num_points = 64
    radius = 1.0

    data = np.zeros(num_points, dtype=mesh.Mesh.dtype)
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)

    for i in range(num_points):
        j = (i + 1) % num_points
        data['vectors'][i] = [
            [0, 0, 0],
            [radius * np.cos(angles[i]), radius * np.sin(angles[i]), 0],
            [radius * np.cos(angles[j]), radius * np.sin(angles[j]), 0],
        ]

    mesh.Mesh(data).save('stls/circle.stl')


def main() :
    shapes = [triangle_func, square_func, circle_func]
    random.choice(shapes)()

if __name__ == '__main__':
    main()