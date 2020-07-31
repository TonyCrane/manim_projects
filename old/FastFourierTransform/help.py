from manimlib.imports import *

#TODO, improve this scene
class ComplexNumberex(Scene):
    def construct(self):
        plane = ComplexPlane()
        plane.add_coordinates()
        self.play(ShowCreation(plane, run_time=3, lag_ratio=0.1))
        self.wait(1)
        t2c = {
            "a" : BLUE_B,
            "b" : BLUE_E,
            "i" : GOLD,
            "e" : BLUE,
            "\\theta" : YELLOW,
            "r" : GREEN
        }
        point = Dot([2.75, 2.25, 0]).set_color(RED)
        label_p = TexMobject("a", "+", "b", "i").set_color_by_tex_to_color_map(t2c)
        label_p.add_updater(lambda m: m.next_to(point, UP))
        self.play(ShowCreation(point))
        self.play(Write(label_p))
        self.wait()
        dl_a = DashedLine()
        dl_a.add_updater(lambda m: m.put_start_and_end_on(point.get_center(), [point.get_center()[0], 0, 0]))
        dl_bi= DashedLine()
        dl_bi.add_updater(lambda m: m.put_start_and_end_on(point.get_center(), [0, point.get_center()[1], 0]))
        label_a = TexMobject("a").set_color_by_tex_to_color_map(t2c)
        label_a.add_updater(lambda m: m.next_to(dl_a, DOWN))
        label_bi= TexMobject("b","i").set_color_by_tex_to_color_map(t2c)
        label_bi.add_updater(lambda m: m.next_to(dl_bi, LEFT))
        self.play(ShowCreation(dl_a), ShowCreation(dl_bi))
        self.play(Write(label_a), Write(label_bi))
        self.play(point.shift, LEFT * 4.5 + DOWN * 2, run_time=3)
        self.play(MoveAlongPath(point, ArcBetweenPoints(point.get_center(), [2.75, 2.25, 0])), run_time=3)
        self.wait(2)
        r = Line(ORIGIN, point.get_center())
        label_r = TexMobject("r").set_color(GREEN).next_to(r.get_center(), UP)
        self.play(ShowCreation(r))
        self.play(Write(label_r))
        angle = Angle([point.get_center()[0], 0, 0], ORIGIN, point.get_center(), color=YELLOW)
        label_theta = TexMobject("\\theta").set_color(YELLOW).next_to(angle, RIGHT)
        self.play(ShowCreation(angle))
        self.play(Write(label_theta))
        self.wait(2)
        zeq = TexMobject("=", "r", "e", "^{i", "\\theta}").set_color_by_tex_to_color_map(t2c).next_to(label_p, RIGHT)
        self.play(Write(zeq))
        self.wait(2)