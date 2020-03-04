from manimlib.imports import *
from manim_projects.tony_useful.imports import *


class Test2DLissajousFromLinesIntersection(Scene):
    def construct(self):
        circle_x = Circle(color=RED).shift(UP * 2.5)
        circle_y = Circle(color=RED).shift(LEFT * 2.5)

        theta = ValueTracker(0)

        point_x = Dot().add_updater(lambda m: m.move_to(circle_x.point_at_angle(1 * theta.get_value())))
        point_y = Dot().add_updater(lambda m: m.move_to(circle_y.point_at_angle(3 * theta.get_value())))

        line_x = Line(UP * 6  ,  DOWN * 6).add_updater(lambda m: m.move_to(point_x.get_center()[0] * RIGHT)).set_color(GRAY)
        line_y = Line(LEFT * 8, RIGHT * 8).add_updater(lambda m: m.move_to(point_y.get_center()[1] * UP)).set_color(GRAY)

        P = Dot(color=BLUE).add_updater(lambda m: m.move_to(line_intersection(line_x.get_start_and_end(), line_y.get_start_and_end())))

        path = TracedPath(P.get_center, stroke_width=6, stroke_color=BLUE, min_distance_to_new_point=0.01)

        self.add(circle_x, circle_y, point_x, point_y, line_x, line_y, P, path)
        self.wait()
        self.play(theta.increment_value, PI * 4, run_time=10, rate_func=linear)
        self.wait()


class Test2DLissajousFromParametricFunction(Scene):
    def construct(self):
        line = ParametricFunction(
            lambda t: [np.sin(1 * t + PI / 2), np.sin(3 * t), 0],
            t_min=0, t_max=4 * TAU, color=BLUE
        )
        w = ValueTracker(1)
        line.add_updater(
            lambda m: m.become(
                ParametricFunction(
                    lambda t: [np.sin(1 * t + PI / 2), np.sin(w.get_value() * t), 0],
                    t_min=0, t_max=4 * TAU, color=BLUE
                )
            )
        )
        self.add(line)
        self.wait()
        self.play(w.increment_value, 8, run_time=10, rate_func=linear)
        self.wait()


class Dot3D(Sphere):
    CONFIG = {
        "radius": 0.08,
        "checkerboard_colors": [WHITE, WHITE],
        "stroke_width": 0,
    }


class Line_(VGroup):
    CONFIG = {
        "nums": 100,
    }
    def __init__(self, start, end, **kwargs):
        VGroup.__init__(self)
        total = end - start
        unit  = total / self.nums
        self.add(Line(start, start + unit, **kwargs))
        for i in range(self.nums - 1):
            now_start = self[-1].get_end()
            now_end = now_start + unit
            self.add(Line(now_start, now_end, **kwargs))


class Line__(VGroup):
    CONFIG = {
        "buff_": 0.02
    }
    def __init__(self, start, end, **kwargs):
        VGroup.__init__(self)
        base = Line(start, end, **kwargs)
        if start[0] != 0:
            self.add(base.copy().shift([0, -self.buff_,  self.buff_]))
            self.add(base.copy().shift([0,  self.buff_, -self.buff_]))
            self.add(base.copy().shift([0,  self.buff_,  self.buff_]))
            self.add(base.copy().shift([0, -self.buff_, -self.buff_]))
        elif start[1] != 0:
            self.add(base.copy().shift([-self.buff_, 0,  self.buff_]))
            self.add(base.copy().shift([ self.buff_, 0, -self.buff_]))
            self.add(base.copy().shift([ self.buff_, 0,  self.buff_]))
            self.add(base.copy().shift([-self.buff_, 0, -self.buff_]))
        else:
            self.add(base.copy().shift([-self.buff_,  self.buff_, 0]))
            self.add(base.copy().shift([ self.buff_, -self.buff_, 0]))
            self.add(base.copy().shift([ self.buff_,  self.buff_, 0]))
            self.add(base.copy().shift([-self.buff_, -self.buff_, 0]))


class Test3DLissajousFromPlaneIntersection(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        },
        "dot_class": Dot3D,
        "plane_use_ploygon": False,
        "line_class": Line,
    }
    def construct(self):
        axes = ThreeDAxes()
        # self.add(axes)
        self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)
        # self.set_camera_orientation(distance=1000000)
        self.begin_ambient_camera_rotation(rate=0.5)

        circle_x = Circle(color=RED).rotate(PI / 2, RIGHT).shift(DOWN * 2.5).set_shade_in_3d()
        circle_y = Circle(color=RED).rotate(PI / 2, DOWN).shift(LEFT * 2.5).set_shade_in_3d()
        circle_z = Circle(color=RED).shift(IN * 2.5).set_shade_in_3d()

        theta = ValueTracker(0)

        point_x = self.dot_class().add_updater(lambda m: m.move_to(circle_x.point_at_angle(1 * theta.get_value()))).set_shade_in_3d().set_color(GREEN)
        point_y = self.dot_class().add_updater(lambda m: m.move_to(circle_y.point_at_angle(2 * theta.get_value()))).set_shade_in_3d().set_color(ORANGE)
        point_z = self.dot_class().add_updater(lambda m: m.move_to(circle_z.point_at_angle(3 * theta.get_value()))).set_shade_in_3d().set_color(PURPLE)

        if self.plane_use_ploygon:
            plane_x = Polygon(
                np.array([ 2.5,  2.5, 0]),
                np.array([-2.5,  2.5, 0]),
                np.array([-2.5, -2.5, 0]),
                np.array([ 2.5, -2.5, 0]),
                fill_color=GREEN,
                fill_opacity=0.3,
                stroke_width=0
            ).set_shade_in_3d().add_updater(lambda m: m.move_to(point_x.get_center()[2] * OUT))
            plane_y = Polygon(
                np.array([ 2.5, 0,  2.5]),
                np.array([-2.5, 0,  2.5]),
                np.array([-2.5, 0, -2.5]),
                np.array([ 2.5, 0, -2.5]),
                fill_color=ORANGE,
                fill_opacity=0.3,
                stroke_width=0
            ).set_shade_in_3d().add_updater(lambda m: m.move_to(point_y.get_center()[1] * UP))
            plane_z = Polygon(
                np.array([0,  2.5,  2.5]),
                np.array([0, -2.5,  2.5]),
                np.array([0, -2.5, -2.5]),
                np.array([0,  2.5, -2.5]),
                fill_color=PURPLE,
                fill_opacity=0.3,
                stroke_width=0
            ).set_shade_in_3d().add_updater(lambda m: m.move_to(point_z.get_center()[0] * RIGHT))
        else:
            plane_x = ParametricSurface(
                lambda u, v: np.array([u, v, 0]),
                u_min=-2.5, u_max=2.5, v_min=-2.5, v_max=2.5,
                checkerboard_colors=None,
                fill_color=GREEN, fill_opacity=0.3,
                stroke_width=0
            ).add_updater(lambda m: m.move_to(point_x.get_center()[2] * OUT))
            plane_y = ParametricSurface(
                lambda u, v: np.array([u, 0, v]),
                u_min=-2.5, u_max=2.5, v_min=-2.5, v_max=2.5,
                checkerboard_colors=None,
                fill_color=ORANGE, fill_opacity=0.3,
                stroke_width=0
            ).add_updater(lambda m: m.move_to(point_y.get_center()[1] * UP))
            plane_z = ParametricSurface(
                lambda u, v: np.array([0, u, v]),
                u_min=-2.5, u_max=2.5, v_min=-2.5, v_max=2.5,
                checkerboard_colors=None,
                fill_color=PURPLE, fill_opacity=0.3,
                stroke_width=0
            ).add_updater(lambda m: m.move_to(point_z.get_center()[0] * RIGHT))
        

        line_x = self.line_class(
            np.array([-2.5, 0, 0]),
            np.array([ 2.5, 0, 0]),
            fill_color=GOLD_E,
            stroke_width=2
        ).add_updater(lambda m: m.move_to(point_y.get_center()[1] * UP + point_x.get_center()[2] * OUT))
        line_y = self.line_class(
            np.array([0, -2.5, 0]),
            np.array([0,  2.5, 0]),
            fill_color=GOLD_E,
            stroke_width=2
        ).add_updater(lambda m: m.move_to(point_z.get_center()[0] * RIGHT + point_x.get_center()[2] * OUT))
        line_z = self.line_class(
            np.array([0, 0, -2.5]),
            np.array([0, 0,  2.5]),
            fill_color=GOLD_E,
            stroke_width=2
        ).add_updater(lambda m: m.move_to(point_z.get_center()[0] * RIGHT + point_y.get_center()[1] * UP))

        P = self.dot_class().set_shade_in_3d(False)
        P.add_updater(lambda m: m.move_to(np.array([point_z.get_center()[0], point_y.get_center()[1], point_x.get_center()[2]])))

        path = TracedPath(P.get_center, stroke_width=6, stroke_color=BLUE, min_distance_to_new_point=0.01)

        self.add(circle_x, circle_y, circle_z, point_x, point_y, point_z, P, path, plane_x, plane_y, plane_z, line_x, line_y, line_z)
        self.wait()
        self.play(theta.increment_value, PI * 4, run_time=10, rate_func=linear)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.wait()
        self.move_camera(phi=0, theta=TAU, distance=10000)
        self.wait(2)
        self.move_camera(phi=PI/2, theta=TAU, distance=10000)
        self.wait(2)
        self.move_camera(phi=PI/2, theta=TAU+PI/2, distance=10000)
        self.wait(2)
        self.move_camera(phi=70*DEGREES, theta=TAU+45*DEGREES)
        self.wait()


class Test3DLissajousFromParametricFunction(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90*DEGREES, theta=45*DEGREES, distance=10000)
        line = ParametricFunction(
            lambda t: np.array([np.sin(2 * t + PI / 2), np.sin(2 * t), np.sin(3 * t)]),
            t_min=0, t_max=4 * TAU, color=BLUE
        ).scale(2.5)
        self.add(line)
        self.wait()
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(10)
        

class Intro2DLissajous(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        para = TexMobject("(", "\\cos \\theta", ",", "\\sin 3\\theta", ")").set_color(BLACK)
        para.scale(1.7).to_corner(DR)

        circle_x = Circle(color=RED)#.shift(UP * 2.5)
        circle_y = Circle(color=RED)#.shift(LEFT * 2.5)

        self.wait()
        self.play(ShowCreation(VGroup(circle_x, circle_y)))
        self.wait()
        self.play(
            circle_x.shift, UP * 2.5,
            circle_y.shift, LEFT * 2.5
        )
        self.wait()
        
        theta = ValueTracker(0)
        theta_label = TexMobject("\\theta = ").scale(1.7).to_corner(DL).set_color(BLACK)
        theta_value = DecimalNumber(0, num_decimal_places=2).set_color(BLACK).scale(1.7).next_to(theta_label, RIGHT)

        def updater_of_point_x(obj):
            obj.move_to(circle_x.point_at_angle(1 * theta.get_value()))

        point_x = Dot(color=GOLD).add_updater(updater_of_point_x)
        point_y = Dot(color=GOLD).add_updater(lambda m: m.move_to(circle_y.point_at_angle(3 * theta.get_value())))

        line_x = Line(UP * 6  ,  DOWN * 6, stroke_width=2).add_updater(lambda m: m.move_to(point_x.get_center()[0] * RIGHT)).set_color(GRAY).set_opacity(0.6)
        line_y = Line(LEFT * 8, RIGHT * 8, stroke_width=2).add_updater(lambda m: m.move_to(point_y.get_center()[1] * UP)).set_color(GRAY).set_opacity(0.6)

        self.play(ShowCreation(point_x))
        self.play(ShowCreation(line_x))
        self.wait()
        self.play(theta.increment_value, PI * 2, run_time=5, rate_func=linear)
        self.play(Write(para[1]))

        theta.set_value(0)
        point_x.remove_updater(updater_of_point_x)

        self.wait()
        self.play(ShowCreation(point_y))
        self.play(ShowCreation(line_y))
        self.wait()
        self.play(theta.increment_value, PI * 2, run_time=5, rate_func=linear)
        self.play(Write(para[3]))
        self.wait()

        theta.set_value(0)
        point_x.add_updater(updater_of_point_x)

        P = Dot(color=BLUE).add_updater(lambda m: m.move_to([point_x.get_center()[0], point_y.get_center()[1], 0]))

        path = TracedPath(P.get_center, stroke_width=6, stroke_color=BLUE, min_distance_to_new_point=0.01)

        self.wait()
        self.play(
            ShowCreation(P), 
            FadeIn(VGroup(para[0], para[2], para[4])), 
            FadeIn(VGroup(theta_label, theta_value))
        )
        theta_value.add_updater(lambda m: m.set_value(theta.get_value()))
        self.add(path)
        self.wait()
        self.play(theta.increment_value, PI * 4, run_time=10, rate_func=linear)
        self.wait(3)


class ALotOf2DLissajous(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        w = ValueTracker(1)

        label = VGroup(
            DecimalNumber(0).set_color(BLACK).scale(2),
            TexMobject(":").set_color(BLACK).scale(2),
            TexMobject("3").set_color(BLACK).scale(2)
        ).arrange(RIGHT)
        label.to_corner(UL, buff=1)
        label[0].add_updater(lambda m: m.set_value(w.get_value()))

        line = ParametricFunction(
            lambda t: [np.cos(1 * t), np.sin(3 * t), 0],
            t_min=0, t_max=6*TAU, color=BLUE
        )
        
        def updater_of_line(obj):
            new = ParametricFunction(
                lambda t: [np.cos(w.get_value() * t), np.sin(3 * t), 0],
                t_min=0, t_max=6*TAU, color=BLUE
            )
            obj.become(new)
        
        self.play(FadeIn(line), FadeIn(label))
        self.wait()
        for i in range(6):
            line.add_updater(updater_of_line)
            self.play(w.increment_value, 1, run_time=1, rate_func=linear)
            line.remove_updater(updater_of_line)
            self.wait()
        self.wait()
        line.add_updater(updater_of_line)
        self.play(w.set_value, 1)
        line.remove_updater(updater_of_line)
        self.wait(2)


def smooth2(t, inflection=6):
    error = sigmoid(-inflection / 2)
    return np.clip(
        (sigmoid(inflection * (t - 0.5)) - error) / (1 - 2 * error),
        0, 1,
    )

class From2DTo3DLissajous(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        axes = ThreeDAxes(number_line_config={"include_tip": False})
        self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES, distance=10000)
        line = ParametricFunction(
            lambda t: np.array([np.cos(1 * t), np.sin(3 * t), np.sin(2 * t)]),
            t_min=0, t_max=4 * TAU, color=BLUE
        )
        self.add(line)
        self.wait()
        self.play(FadeIn(axes))
        self.wait()
        self.move_camera(phi=70*DEGREES, theta=135*DEGREES, rate_func=smooth2, run_time=5)
        self.begin_ambient_camera_rotation(rate=0.8)
        self.wait(10)
        self.play(FadeOut(axes), FadeOut(line))
        self.wait()


class ReadyTo3DLissajous(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        },
        "dot_class": Dot3D,
        "line_class": Line,
    }
    def construct(self):
        axes = ThreeDAxes()
        # self.add(axes)
        self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)
        # self.set_camera_orientation(distance=1000000)
        self.begin_ambient_camera_rotation(rate=0.25)

        circle_x = Circle(color=RED).rotate(PI / 2, RIGHT).shift(DOWN * 2.5).set_shade_in_3d()
        circle_y = Circle(color=RED).rotate(PI / 2, DOWN).shift(LEFT * 2.5).set_shade_in_3d()
        circle_z = Circle(color=RED).shift(IN * 2.5).set_shade_in_3d()

        self.wait()
        self.play(
            ShowCreation(VGroup(circle_x, circle_y, circle_z))
        )

        theta = ValueTracker(0)

        def updater_of_point_x(m):
            m.move_to(circle_x.point_at_angle(1 * theta.get_value()))
        def updater_of_point_y(m):
            m.move_to(circle_y.point_at_angle(2 * theta.get_value()))
        def updater_of_point_z(m):
            m.move_to(circle_z.point_at_angle(3 * theta.get_value()))


        point_x = self.dot_class().add_updater(updater_of_point_x).set_color(GREEN)
        def updater_of_plane_x(m):
            m.move_to(point_x.get_center()[2] * OUT)
        plane_x = ParametricSurface(
            lambda u, v: np.array([u, v, 0]),
            u_min=-2.5, u_max=2.5, v_min=-2.5, v_max=2.5,
            checkerboard_colors=None,
            fill_color=GREEN, fill_opacity=0.3,
            stroke_width=0
        ).add_updater(updater_of_plane_x)
        
        self.wait()
        self.play(ShowCreation(point_x))
        self.play(ShowCreation(plane_x))
        self.wait()
        self.play(theta.increment_value, PI*2, run_time=5, rate_func=linear)
        self.wait()
        point_x.remove_updater(updater_of_point_x)
        plane_x.remove_updater(updater_of_plane_x)
        theta.set_value(0)

        point_y = self.dot_class().add_updater(updater_of_point_y).set_color(ORANGE)
        def updater_of_plane_y(m):
            m.move_to(point_y.get_center()[1] * UP)
        plane_y = ParametricSurface(
            lambda u, v: np.array([u, 0, v]),
            u_min=-2.5, u_max=2.5, v_min=-2.5, v_max=2.5,
            checkerboard_colors=None,
            fill_color=ORANGE, fill_opacity=0.3,
            stroke_width=0
        ).add_updater(updater_of_plane_y)

        line_x = self.line_class(
            np.array([-2.5, 0, 0]),
            np.array([ 2.5, 0, 0]),
            fill_color=GOLD_E,
            stroke_width=2
        ).add_updater(lambda m: m.move_to(point_y.get_center()[1] * UP + point_x.get_center()[2] * OUT))

        self.wait()
        self.play(ShowCreation(point_y))
        self.play(ShowCreation(plane_y))
        self.play(ShowCreation(line_x))
        self.wait()
        self.play(theta.increment_value, PI*2, run_time=5, rate_func=linear)
        self.wait()
        point_y.remove_updater(updater_of_point_y)
        plane_y.remove_updater(updater_of_plane_y)
        theta.set_value(0)

        point_z = self.dot_class().add_updater(updater_of_point_z).set_color(PURPLE)
        def updater_of_plane_z(m):
            m.move_to(point_z.get_center()[0] * RIGHT)
        plane_z = ParametricSurface(
            lambda u, v: np.array([0, u, v]),
            u_min=-2.5, u_max=2.5, v_min=-2.5, v_max=2.5,
            checkerboard_colors=None,
            fill_color=PURPLE, fill_opacity=0.3,
            stroke_width=0
        ).add_updater(updater_of_plane_z)

        line_y = self.line_class(
            np.array([0, -2.5, 0]),
            np.array([0,  2.5, 0]),
            fill_color=GOLD_E,
            stroke_width=2
        ).add_updater(lambda m: m.move_to(point_z.get_center()[0] * RIGHT + point_x.get_center()[2] * OUT))
        line_z = self.line_class(
            np.array([0, 0, -2.5]),
            np.array([0, 0,  2.5]),
            fill_color=GOLD_E,
            stroke_width=2
        ).add_updater(lambda m: m.move_to(point_z.get_center()[0] * RIGHT + point_y.get_center()[1] * UP))

        self.wait()
        self.play(ShowCreation(point_z))
        self.play(ShowCreation(plane_z))
        self.play(ShowCreation(line_y), ShowCreation(line_z))
        self.wait()
        self.play(theta.increment_value, PI*2, run_time=5, rate_func=linear)
        self.wait()
        theta.set_value(0)

        P = self.dot_class().set_shade_in_3d(False)
        P.add_updater(lambda m: m.move_to(np.array([point_z.get_center()[0], point_y.get_center()[1], point_x.get_center()[2]])))

        self.wait()
        self.play(ShowCreation(P))
        self.stop_ambient_camera_rotation()
        self.wait()
        self.move_camera(phi=70*DEGREES, theta=405*DEGREES)


class DualAxisIllusion(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        self.set_camera_orientation(phi=90*DEGREES, theta=45*DEGREES, distance=10000, gamma=90*DEGREES)
        line = ParametricFunction(
            lambda t: np.array([np.cos(2 * t), np.sin(2 * t), 0.6 * np.sin(3 * t)]),
            t_min=0, t_max=4 * TAU, color=BLUE, stroke_width=20
        ).scale(2)
        self.add(line)
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.8)
        self.wait(10)


class EndScene(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        self.set_camera_orientation(phi=90*DEGREES, theta=45*DEGREES, distance=10000, gamma=90*DEGREES)
        line = ParametricFunction(
            lambda t: np.array([np.cos(2 * t), np.sin(2 * t), 0.6 * np.sin(3 * t)]),
            t_min=0, t_max=4 * TAU, color=BLUE, stroke_width=20
        ).scale(2)
        self.play(FadeIn(line))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(6)

        bg = Rectangle(width=16, height=10).set_fill(color=BLACK, opacity=0.8)
        self.camera.add_fixed_in_frame_mobjects(bg)
        self.wait()
        self.play(FadeIn(bg))

        thanks = Group(
            Text("特别鸣谢", font="Source Han Sans CN").scale(0.55).set_color(RED),
            ImageMobject("GZTime.png").scale(0.3),
            Text("@GZTime", font="Source Han Serif CN").scale(0.35).set_color(BLUE),
            ImageMobject("cigar.png").scale(0.3),
            Text("@cigar666", font="Source Han Serif CN").scale(0.35).set_color(BLUE)
        )
        self.camera.add_fixed_in_frame_mobjects(thanks)
        thanks[0].to_corner(UR)
        thanks[2].next_to(thanks[0], DOWN, aligned_edge=RIGHT)
        thanks[1].next_to(thanks[2], LEFT)
        thanks[3].next_to(thanks[1], DOWN)
        thanks[4].next_to(thanks[3], RIGHT)
        thanks[1:].next_to(thanks[0], DOWN, aligned_edge=RIGHT)
        thanks[1].scale(1.5, about_point=thanks[1].get_center())

        refer = VGroup(
            Text("参考", font="Source Han Sans CN").scale(0.55).set_color(RED),
            Text("[1] Wikipedia利萨茹曲线 https://en.wikipedia.org/wiki/Lissajous_curve", font="Source Han Serif CN").scale(0.3),
            Text("[2] processing利萨如图形 https://www.bilibili.com/video/av33110155", font="Source Han Serif CN").scale(0.3),
            Text("[3] 双轴错觉 https://killedbyapixel.github.io/Dual-Axis-Illusion/", font="Source Han Serif CN").scale(0.3),
            Text("[4] 双周错觉代码仓库 https://github.com/KilledByAPixel/Dual-Axis-Illusion", font="Source Han Serif CN").scale(0.3),
        )
        self.camera.add_fixed_in_frame_mobjects(refer)
        refer.arrange(DOWN, aligned_edge=LEFT)
        refer.to_corner(DL)

        self.wait()
        self.play(FadeInFromDown(thanks))
        self.play(FadeIn(refer))
        self.wait(10)


class VideoCover(Scene):
    def construct(self):
        background = Rectangle(width=18, height=3.5, fill_opacity=0.7, fill_color=BLACK, stroke_width=0).shift(DOWN*0.5)
        title = VGroup(
            Text("可视/三维", font="Source Han Serif CN", color=BLUE).scale(1),
            Text("Lissajous图形", font="Source Han Serif CN", color=RED).scale(1.2)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title_bg = VGroup(
            Text("可视/三维", font="Source Han Serif CN", color=BLUE_B).scale(1).set_stroke(width=12, opacity=0.4),
            Text("Lissajous图形", font="Source Han Serif CN", color=RED_B).scale(1.2).set_stroke(width=12, opacity=0.4)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title.to_edge(RIGHT, buff=1.3).shift(DOWN*0.5)
        title_bg.to_edge(RIGHT, buff=1.3).shift(DOWN*0.5)
        author = VGroup(
            TextMobject("@鹤翔万里", background_stroke_width=0).scale(1.2).set_color([YELLOW, RED]),
            TextMobject("@\ GZTime", background_stroke_width=0).scale(1.2).set_color([WHITE, BLUE])
        ).arrange(DOWN, aligned_edge=LEFT)
        author.shift(LEFT*4 + DOWN*0.5)
        self.add(background, title_bg, title, author)

