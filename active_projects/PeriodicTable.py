from manimlib import *
from manim_projects.tony_useful.imports import *


def value_fit(arr, i_min, i_max, v_min=0.25, v_max=1.5):
    def f(x):
        return (v_max - v_min) / (i_max - i_min) * x + v_min
    res = []
    for i in arr:
        res.append(f(i))
    return res


class PeriodicTable_2D(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        boxes = ChemicalBoxes().add_label().set_block_color()
        self.add(boxes)


class PeriodicTable_2D_BLACK(PeriodicTable_2D):
    CONFIG = {
        "camera_config": {
            "background_color": BLACK
        }
    }


class PeriodicTable_3D(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        }
    }
    def construct(self):
        self.set_camera_orientation(phi=50 * DEGREES, theta=240 * DEGREES, distance=50)
        boxes = ChemicalBoxes().add_label().set_block_color()
        self.add(boxes)
        # self.begin_ambient_camera_rotation(rate=1)
        # self.wait(10)


class PeriodicTable_3D_BLACK(PeriodicTable_3D):
    CONFIG = {
        "camera_config": {
            "background_color": BLACK
        }
    }


class PeriodicTable_3D_move(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        }
    }
    def construct(self):
        self.set_camera_orientation(phi=50 * DEGREES, theta=240 * DEGREES, distance=50)
        boxes = ChemicalBoxes().add_label().set_block_color()
        self.add(boxes)
        self.begin_ambient_camera_rotation(rate=0.8)
        self.wait(15)

mass = [
    0, 1.008, 4.0026,
    6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 19.998, 20.180,
    22.990, 24.305, 26.982, 28.085, 30.974, 32.06, 35.45, 39.95,
    39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546, 65.38, 69.723, 72.630, 74.922, 78.971, 79.904, 83.798,
    85.468, 87.62, 88.906, 91.224, 92.906, 95.95, 0, 101.07, 102.91, 106.42, 107.87, 112.41, 114.82, 118.71, 121.76, 127.60, 126.90, 131.29,
    132.91, 137.33,
    138.91, 140.12, 140.91, 144.24, 0, 150.36, 151.96, 157.25, 158.93, 162.50, 164.93, 167.26, 168.93, 173.05, 174.97,
    178.49, 180.95, 183.84, 186.21, 190.23, 192.22, 195.08, 196.97, 200.59, 204.38, 207.2, 208.98, 0, 0, 0,
    0, 0,
    0, 232.04, 231.04, 238.03, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# print(len(mass))
# print(value_fit(mass, 1.008, 238.03))

class PeriodicTable_by_mass(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        }
    }
    def construct(self):
        self.set_camera_orientation(phi=50 * DEGREES, theta=240 * DEGREES, distance=50)
        height = value_fit(mass, 1.008, 238.03)
        boxes = ChemicalBoxes().set_block_color()#.set_height_by_array(height)
        boxes.set_height_by_array(height)
        boxes.add_label()
        self.add(boxes[1], boxes[0])
        # self.begin_ambient_camera_rotation(rate=0.8)
        # self.wait(15)
