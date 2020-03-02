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
        
        