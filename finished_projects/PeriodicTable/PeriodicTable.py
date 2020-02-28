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
        old_boxes_3 = old_boxes.copy()
        boxes = ChemicalBoxes().set_block_color()
        boxes.set_height_by_array(height)
        boxes.add_label()
        boxes.scale(0.9).shift(DL * 0.5)
        self.add(old_boxes)
        self.wait()
        self.play(
            old_boxes.scale, 0.9,
            old_boxes.shift, DL * 0.5
        )
        old_boxes_2 = old_boxes.copy()
        self.wait(2)
        # self.add(boxes)

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
        self.play(Transform(old_boxes_2, old_boxes_3))
        self.wait()


energy1 = [
    0, 1312, 2372.3, 
    520.2, 899.5, 800.6, 1086.5, 1402.3, 1313.9, 1681, 2080.7, 
    495.8, 737.7, 577.5, 786.5, 1011.8, 999.6, 1251.2, 1520.6, 
    418.8, 589.8, 633.1, 658.8, 650.9, 652.9, 717.3, 762.5, 760.4, 737.1, 745.5, 906.4, 578.8, 762, 947, 941, 1139.9, 1350.8, 
    403, 549.5, 600, 640.1, 652.1, 684.3, 702, 710.2, 719.7, 804.4, 731, 867.8, 558.3, 708.6, 834, 869.3, 1008.4, 1170.4, 
    375.7, 502.9, 
    538.1, 534.4, 527, 533.1, 540, 544.5, 547.1, 593.4, 565.8, 573, 581, 589.3, 596.7, 603.4, 523.5, 
    658.5, 761, 770, 760, 840, 880, 870, 890.1, 1007.1, 589.4, 715.6, 703, 812.1, 899.003, 1037, 
    380, 509.3, 
    499, 587, 568, 597.6, 604.5, 584.7, 578, 581, 601, 608, 619, 627, 635, 642, 470, 
    580, 665, 757, 740, 730, 800, 960, 1020, 1155, 707.2, 832.2, 538.3, 663.9, 736.9, 860.1
]

energy2 = [
    0, 0, 5250.5, 
    7298.1, 1757.1, 2427.1, 2352.6, 2856, 3388.3, 3374.2, 3952.3, 
    4562, 1450.7, 1816.7, 1577.1, 1907, 2252, 2298, 2665.8, 
    3052, 1145.4, 1235, 1309.8, 1414, 1590.6, 1509, 1561.9, 1648, 1753, 1957.9, 1733.3, 1979.3, 1537.5, 1798, 2045, 2103, 2350.4, 
    2633, 1064.2, 1180, 1270, 1380, 1560, 1470, 1620, 1740, 1870, 2070, 1631.4, 1820.7, 1411.8, 1594.9, 1790, 1845.9, 2046.4, 
    2234.3, 965.2, 
    1067, 1050, 1020, 1040, 1050, 1070, 1085, 1170, 1110, 1130, 1140, 1150, 1160, 1174.8, 1340, 
    1440, 1500, 1700, 1260, 1600, 1600, 1791, 1980, 1810, 1971, 1450.5, 1610, 0, 0, 0, 
    0, 979, 
    1170, 1110, 1128, 1420, 1128, 1128, 1158, 1196, 1186, 1206, 1216, 1225, 1235, 1254, 1428, 
    1390, 1547, 1733, 1690, 1760, 1820, 1890, 2070, 2170, 2309, 1600, 1760, 1330, 1435.4, 1560
]

energy3 = [
    0, 0, 0, 
    11815, 14848.70, 3659.7, 4620.5, 4578.1, 5300.5, 6050.4, 6122, 
    6910.3, 7732.7, 2744.8, 3231.6, 2914.1, 3357, 3822, 3931, 
    4420, 4912.4, 2388.6, 2652.5, 2830, 2987, 3248, 2957, 3232, 3395, 3555, 3833, 2963, 3302.1, 2735, 2973.7, 3470, 3565, 
    3860, 4138, 1980, 2218, 2416, 2618, 2850, 2747, 2997, 3177, 3361, 3616, 2704, 2943, 2440, 2698, 3180, 3099.4, 
    3400, 3600, 
    1850.3, 1949, 2086, 2130, 2150, 2260, 2404, 1990, 2114, 2200, 2204, 2194, 2285, 2417, 2022.3, 
    2250, 0, 0, 2510, 0, 0, 0, 0, 3300, 2878, 3081.5, 2466, 0, 0, 0, 
    0, 0, 
    1900, 1978, 1814, 1900, 1997, 2084, 2132, 2026, 2152, 2267, 2334, 2363, 2470, 2643, 2228, 
    2300, 2378, 2484, 2570, 2830, 2900, 3030, 3080, 3160, 3226, 3370, 2650, 2850, 2161.9, 0
]

class PeriodicTable_by_ionization_energy(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        },
        "move": True,
    }
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=240 * DEGREES, distance=50)

        height1 = value_fit(energy1, 375.7, 2372.3, v_max=2)
        height2 = value_fit(energy2, 965.2, 7298.1, v_max=2.5)
        height3 = value_fit(energy3, 1814, 14848.7, v_max=4)

        old_boxes = ChemicalBoxes().set_block_color()
        old_boxes.add_label()
        old_boxes_3 = old_boxes.copy()

        boxes1 = ChemicalBoxes().set_block_color()
        boxes1.set_height_by_array(height1)
        boxes1.add_label()
        boxes1.scale(0.85).shift(DL * 0.8)
        boxes2 = ChemicalBoxes().set_block_color()
        boxes2.set_height_by_array(height2)
        boxes2.add_label()
        boxes2.scale(0.85).shift(DL * 0.8)
        boxes3 = ChemicalBoxes().set_block_color()
        boxes3.set_height_by_array(height3)
        boxes3.add_label()
        boxes3.scale(0.85).shift(DL * 0.8)
        self.add(old_boxes)
        self.wait()
        self.play(
            old_boxes.scale, 0.85,
            old_boxes.shift, DL * 0.8
        )
        old_boxes_2 = old_boxes.copy()
        self.wait(2)
        # self.add(boxes2)

        text1 = Text("高度由 第一电离能 决定", font="Source Han Serif CN", t2c={"高度由": BLUE, "第一电离能": ORANGE, "决定": BLUE}).scale(0.5)
        data = Text("数据来自于 Wikipedia", font="Source Han Serif CN", t2c={"数据来自于": BLACK, "Wikipedia": RED}).scale(0.25)
        text2 = Text("高度由 第二电离能 决定", font="Source Han Serif CN", t2c={"高度由": BLUE, "第二电离能": ORANGE, "决定": BLUE}).scale(0.5)
        text3 = Text("高度由 第三电离能 决定", font="Source Han Serif CN", t2c={"高度由": BLUE, "第三电离能": ORANGE, "决定": BLUE}).scale(0.5)
        self.camera.add_fixed_in_frame_mobjects(text1, data, text2, text3)
        text1.to_corner(UL, buff=0.25)
        text2.to_corner(UL, buff=0.25)
        text3.to_corner(UL, buff=0.25)
        data.to_corner(DR, buff=0.25)

        self.play(FadeIn(text1), FadeIn(data))
        self.play(ReplacementTransform(old_boxes, boxes1), run_time=3)

        if self.move:
            self.wait(3)
            fps = 60
            for i in range(361):
                self.set_camera_orientation(theta=240 * DEGREES + i * DEGREES)
                self.wait(1 / fps)
            self.wait(3)

        self.play(
            ReplacementTransform(boxes1, boxes2),
            ReplacementTransform(text1, text2),
            run_time=2
        )
        self.wait(3)
        self.play(
            ReplacementTransform(boxes2, boxes3),
            ReplacementTransform(text2, text3),
            run_time=2
        )
        self.wait(3)

        self.play(
            FadeOut(text3), 
            FadeOut(data), 
            ReplacementTransform(boxes3, old_boxes_2)
        )
        self.wait()
        
        self.wait()
        self.play(Transform(old_boxes_2, old_boxes_3))
        self.wait()


class EndScene(ThreeDScene):
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
        self.wait(3)

        bg = Rectangle(width=16, height=10).set_fill(color=BLACK, opacity=0.8)
        self.camera.add_fixed_in_frame_mobjects(bg)
        self.play(FadeIn(bg))

        thanks = Group(
            Text("特别鸣谢", font="Source Han Sans CN").scale(0.5).set_color(RED),
            ImageMobject("cigar.png").scale(0.35),
            Text("@cigar666", font="Source Han Serif CN").scale(0.35).set_color(BLUE)
        )
        self.camera.add_fixed_in_frame_mobjects(thanks)
        thanks[0].to_corner(UR)
        thanks[2].next_to(thanks[0], DOWN, aligned_edge=RIGHT)
        thanks[1].next_to(thanks[2], LEFT)

        refer = VGroup(
            Text("参考", font="Source Han Sans CN").scale(0.5).set_color(RED),
            Text("[1] IUPAC原子量表(2019) https://iupac.org/what-we-do/periodic-table-of-elements/", font="Source Han Serif CN").scale(0.2),
            Text("[2] CIAAW放射性元素质量数 https://ciaaw.org/radioactive-elements.htm", font="Source Han Serif CN").scale(0.2),
            Text("[3] Wikipedia原子共价半径 https://en.wikipedia.org/wiki/Covalent_radius", font="Source Han Serif CN").scale(0.2),
            Text("[4] Wikipedia原子半径(数据页) https://en.wikipedia.org/wiki/Atomic_radii_of_the_elements_(data_page)", font="Source Han Serif CN").scale(0.2),
            Text("[5] Wikipedia电负性 https://en.wikipedia.org/wiki/Electronegativity", font="Source Han Serif CN").scale(0.2),
            Text("[6] Wikipedia电负性(数据页) https://en.wikipedia.org/wiki/Electronegativities_of_the_elements_(data_page)", font="Source Han Serif CN").scale(0.2),
            Text("[7] Wikipedia电离能 https://en.wikipedia.org/wiki/Ionization_energy", font="Source Han Serif CN").scale(0.2),
            Text("[8] Wikipedia电离能表 https://en.wikipedia.org/wiki/Molar_ionization_energies_of_the_elements", font="Source Han Serif CN").scale(0.2),
        )
        self.camera.add_fixed_in_frame_mobjects(refer)
        refer.arrange(DOWN, aligned_edge=LEFT)
        refer.to_corner(DL)

        self.wait()
        self.play(FadeInFromDown(thanks))
        self.play(FadeIn(refer))
        self.wait(5)


class VideoCover(Scene):
    def construct(self):
        background = Rectangle(width=18, height=3.5, fill_opacity=0.7, fill_color=BLACK, stroke_width=0)
        title = VGroup(
            Text("可视化", font="Source Han Serif CN", color=BLUE).scale(1.2),
            Text("元素周期表", font="Source Han Serif CN", color=RED).scale(1.4)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title_bg = VGroup(
            Text("可视化", font="Source Han Serif CN", color=BLUE_B).scale(1.2).set_stroke(width=12, opacity=0.4),
            Text("元素周期表", font="Source Han Serif CN", color=RED_B).scale(1.4).set_stroke(width=12, opacity=0.4)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title.to_edge(RIGHT, buff=1.5)
        title_bg.to_edge(RIGHT, buff=1.5)
        author = TextMobject("@鹤翔万里", background_stroke_width=0).scale(1.2).set_color([BLUE, YELLOW, ORANGE, RED])
        author.shift(LEFT * 3.2)
        self.add(background, title_bg, title, author)


class VideoCoverBackground(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        }
    }
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=240 * DEGREES, distance=50)

        height1 = value_fit(energy1, 375.7, 2372.3, v_max=2)

        boxes1 = ChemicalBoxes().set_block_color()
        boxes1.set_height_by_array(height1)
        boxes1.add_label()
        boxes1.scale(0.85).shift(DL * 0.8)
        self.wait(2)
        self.add(boxes1)

