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


class Test3DLissajousFromPlaneIntersection(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # self.add(axes)
        self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)

        circle_x = Circle(color=RED).rotate(PI / 2, RIGHT).shift(DOWN * 1.4).set_shade_in_3d()
        circle_y = Circle(color=RED).rotate(PI / 2, DOWN).shift(LEFT * 1.4).set_shade_in_3d()
        circle_z = Circle(color=RED).shift(IN * 1.4).set_shade_in_3d()

        theta = ValueTracker(0)

        point_x = Dot().add_updater(lambda m: m.move_to(circle_x.point_at_angle(1 * theta.get_value()))).set_shade_in_3d()
        point_y = Dot().add_updater(lambda m: m.move_to(circle_y.point_at_angle(2 * theta.get_value()))).set_shade_in_3d()
        point_z = Dot().add_updater(lambda m: m.move_to(circle_z.point_at_angle(3 * theta.get_value()))).set_shade_in_3d()

        P = Dot(color=BLUE).set_shade_in_3d()
        P.add_updater(lambda m: m.move_to(np.array([point_z.get_center()[0], point_y.get_center()[1], point_x.get_center()[2]])))

        path = TracedPath(P.get_center, stroke_width=6, stroke_color=BLUE, min_distance_to_new_point=0.01)

        self.add(circle_x, circle_y, circle_z, point_x, point_y, point_z, P, path)
        self.wait()
        self.play(theta.increment_value, PI * 4, run_time=10, rate_func=linear)
        self.wait()

        