from manimlib import *
from manim_projects.tony_useful.imports import *


def value_fit(arr, i_min, i_max, v_min=0.25, v_max=2):
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
        self.set_camera_orientation(phi=45 * DEGREES, theta=240 * DEGREES, distance=50)
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
        # self.set_camera_orientation(phi=45 * DEGREES, theta=240 * DEGREES, distance=50)
        boxes = ChemicalBoxes().add_label().set_block_color()
        self.add(boxes)
        self.wait(3)
        self.move_camera(phi=45 * DEGREES, theta=-120 * DEGREES, distance=50)
        self.wait(2)
        fps = 60
        for i in range(361):
            self.set_camera_orientation(theta=240 * DEGREES + i * DEGREES)
            self.wait(1 / fps)
        self.wait()


mass = [
    0, 1.008, 4.0026,
    6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 19.998, 20.180,
    22.990, 24.305, 26.982, 28.085, 30.974, 32.06, 35.45, 39.95,
    39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546, 65.38, 69.723, 72.630, 74.922, 78.971, 79.904, 83.798,
    85.468, 87.62, 88.906, 91.224, 92.906, 95.95, 97.5, 101.07, 102.91, 106.42, 107.87, 112.41, 114.82, 118.71, 121.76, 127.60, 126.90, 131.29,
    132.91, 137.33,
    138.91, 140.12, 140.91, 144.24, 145, 150.36, 151.96, 157.25, 158.93, 162.50, 164.93, 167.26, 168.93, 173, 174.97,
    178.49, 180.95, 183.84, 186.21, 190.23, 192.22, 195.08, 196.97, 200.59, 204.38, 207.2, 208.98, 209, 210, 222,
    223, 226,
    227, 232.04, 231.04, 238.03, 237, 244, 243, 247, 247, 251, 252, 257, 258, 259, 262, 
    267, 269, 270, 271, 270, 277, 280.5, 281.5, 285, 286, 289, 289, 293, 294, 294
]

class PeriodicTable_by_mass(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        },
        "move": True,
    }
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=240 * DEGREES, distance=50)
        height = value_fit(mass, 1.008, 294)

        old_boxes = ChemicalBoxes().set_block_color()
        old_boxes.add_label()
        old_boxes_2 = old_boxes.copy()
        boxes = ChemicalBoxes().set_block_color()
        boxes.set_height_by_array(height)
        boxes.add_label()
        boxes[1][70].move_to(boxes[0][70][1].get_center())
        self.add(old_boxes)
        self.wait(2)

        text = Text("高度由 相对原子质量 决定", font="Source Han Serif CN", t2c={"高度由": BLUE, "相对原子质量": ORANGE, "决定": BLUE}).scale(0.5)
        data = Text("数据来自于 IUPAC/CIAAW", font="Source Han Serif CN", t2c={"数据来自于": BLACK, "IUPAC/CIAAW": RED}).scale(0.25)
        self.camera.add_fixed_in_frame_mobjects(text, data)
        text.to_corner(UL, buff=0.25)
        data.to_corner(DR, buff=0.25)

        self.play(FadeIn(text), FadeIn(data))
        self.play(ReplacementTransform(old_boxes, boxes), run_time=3)

        if self.move:
            self.wait(3)
            fps = 60
            for i in range(361):
                self.set_camera_orientation(theta=240 * DEGREES + i * DEGREES)
                self.wait(1 / fps)
            self.wait(3)
            self.play(
                FadeOut(text), 
                FadeOut(data), 
                ReplacementTransform(boxes, old_boxes_2)
            )
            self.wait()


radius = [
    0, 32, 46,
    133, 102, 85, 75, 71, 63, 64, 67,
    155, 139, 126, 116, 111, 103, 99, 96,
    196, 171, 148, 136, 134, 122, 119, 116, 111, 110, 112, 118, 124, 121, 121, 116, 114, 117,
    210, 185, 163, 154, 147, 138, 128, 125, 125, 120, 128, 136, 142, 140, 140, 136, 133, 131,
    232, 196,
    180, 163, 176, 174, 173, 172, 168, 169, 168, 167, 166, 165, 164, 170, 162,
    152, 146, 137, 131, 129, 122, 123, 124, 133, 144, 144, 151, 145, 147, 142,
    223, 201,
    186, 175, 169, 170, 171, 172, 166, 166, 168, 168, 165, 167, 173, 176, 161,
    157, 149, 143, 141, 134, 129, 128, 121, 122, 136, 143, 162, 175, 165, 157
]

class PeriodicTable_by_covalent_radius(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        },
        "move": True,
    }
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=240 * DEGREES, distance=50)
        height = value_fit(radius, 32, 223, v_max=1.8)

        old_boxes = ChemicalBoxes().set_block_color()
        old_boxes.add_label()
        old_boxes_2 = old_boxes.copy()
        boxes = ChemicalBoxes().set_block_color()
        boxes.set_height_by_array(height)
        boxes.add_label()
        self.add(old_boxes)
        self.wait(2)
        # self.add(boxes)

        text = Text("高度由 原子共价半径 决定", font="Source Han Serif CN", t2c={"高度由": BLUE, "原子共价半径": ORANGE, "决定": BLUE}).scale(0.5)
        data = Text("数据来自于 P.Pyykkö, M.Atsumi", font="Source Han Serif CN", t2c={"数据来自于": BLACK, "P.Pyykkö, M.Atsumi": RED}).scale(0.25)
        self.camera.add_fixed_in_frame_mobjects(text, data)
        text.to_corner(UL, buff=0.25)
        data.to_corner(DR, buff=0.25)

        self.play(FadeIn(text), FadeIn(data))
        self.play(ReplacementTransform(old_boxes, boxes), run_time=3)

        if self.move:
            self.wait(3)
            fps = 60
            for i in range(361):
                self.set_camera_orientation(theta=240 * DEGREES + i * DEGREES)
                self.wait(1 / fps)
            self.wait(3)
            self.play(
                FadeOut(text), 
                FadeOut(data), 
                ReplacementTransform(boxes, old_boxes_2)
            )
            self.wait()


elec = [
    0, 2.2, 0,
    0.98, 1.57, 2.04, 2.55, 3.04, 3.44, 3.98, 0,
    0.93, 1.31, 1.61, 1.90, 2.19, 2.58, 3.16, 3.20,
    0.82, 1.00, 1.36, 1.54, 1.63, 1.66, 1.55, 1.83, 1.88, 1.91, 1.90, 1.65, 1.81, 2.01, 2.18, 2.55, 2.96, 3.00,
    0.82, 0.95, 1.22, 1.33, 1.60, 2.16, 1.90, 2.20, 2.28, 2.20, 1.93, 1.69, 1.78, 1.96, 2.05, 2.10, 2.66, 2.60,
    0.79, 0.89,
    1.10, 1.12, 1.13, 1.14, 1.13, 1.17, 1.20, 1.20, 1.10, 1.22, 1.23, 1.24, 1.25, 1.10, 1.27,
    1.30, 1.50, 2.36, 1.90, 2.20, 2.20, 2.28, 2.54, 2.00, 1.62, 2.33, 2.02, 2.00, 2.20, 2.20,
    0.80, 0.90,
    1.10, 1.30, 1.50, 2.38, 1.36, 1.28, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30,
       0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0
]

class PeriodicTable_by_electronegativity(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        },
        "move": True,
    }
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=240 * DEGREES, distance=50)
        height = value_fit(elec, 0.79, 3.98, v_max=1.8)

        old_boxes = ChemicalBoxes().set_block_color()
        old_boxes.add_label()
        boxes = ChemicalBoxes().set_block_color()
        boxes.set_height_by_array(height)
        boxes.add_label()
        boxes.scale(0.9)
        self.add(old_boxes)
        self.wait()
        self.play(old_boxes.scale, 0.9)
        old_boxes_2 = old_boxes.copy()
        self.wait(2)
        self.move_camera(frame_center=DR * 0.8)
        self.wait()
        self.add(boxes)

        text = Text("高度由 电负性(鲍林标度) 决定", font="Source Han Serif CN", t2c={"高度由": BLUE, "电负性(鲍林标度)": ORANGE, "决定": BLUE}).scale(0.5)
        data = Text("数据来自于 Wikipedia", font="Source Han Serif CN", t2c={"数据来自于": BLACK, "Wikipedia": RED}).scale(0.25)
        self.camera.add_fixed_in_frame_mobjects(text, data)
        text.to_corner(UL, buff=0.25)
        data.to_corner(DR, buff=0.25)

        self.play(FadeIn(text), FadeIn(data))
        self.play(ReplacementTransform(old_boxes, boxes), run_time=3)

        if self.move:
            self.wait(3)
            fps = 60
            for i in range(361):
                self.set_camera_orientation(theta=240 * DEGREES + i * DEGREES)
                self.wait(1 / fps)
            self.wait(3)
            self.play(
                FadeOut(text), 
                FadeOut(data), 
                ReplacementTransform(boxes, old_boxes_2)
            )
            self.wait()
        
        self.wait()
        self.move_camera(frame_center=ORIGIN)
        self.play(old_boxes_2.scale, 1.1111111)
        self.wait()
        