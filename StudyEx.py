from manimlib.imports import *
from manim_projects.tony_useful.imports import *

class RateFunctions(Scene):
    def construct(self):
        title = VGroup(
            Text("linear", font="Monaco for Powerline").scale(0.5),
            Text("smooth", font="Monaco for Powerline").scale(0.5),
            Text("rush_into", font="Monaco for Powerline").scale(0.5),
            Text("rush_from", font="Monaco for Powerline").scale(0.5),
            Text("slow_into", font="Monaco for Powerline").scale(0.5),
            Text("double_smooth", font="Monaco for Powerline").scale(0.5),
            Text("there_and_back", font="Monaco for Powerline").scale(0.5)
        ).arrange_submobjects(
            DOWN, aligned_edge=RIGHT, buff=0.55
        ).move_to(LEFT*7, aligned_edge=LEFT)
        dots = VGroup(
            *[
                Dot(color=BLUE).move_to([-2.5, i, 0])
                for i in range(3, -4, -1)
            ]
        )
        transform_dots = VGroup(
            *[
                Dot(color=BLUE).move_to([6, i, 0], aligned_edge=DOWN)
                for i in range(3, -4, -1)
            ]
        )
        self.add(title, dots)
        self.wait(2)
        self.play(TransformFromCopy(dots[0], transform_dots[0], rate_func=linear))
        self.play(TransformFromCopy(dots[1], transform_dots[1], rate_func=smooth))
        self.play(TransformFromCopy(dots[2], transform_dots[2], rate_func=rush_into))
        self.play(TransformFromCopy(dots[3], transform_dots[3], rate_func=rush_from))
        self.play(TransformFromCopy(dots[4], transform_dots[4], rate_func=slow_into))
        self.play(TransformFromCopy(dots[5], transform_dots[5], rate_func=double_smooth))
        self.play(TransformFromCopy(dots[6], transform_dots[6], rate_func=there_and_back))
        self.wait(2)
        self.play(
            ReplacementTransform(dots[0], transform_dots[0], rate_func=linear),
            ReplacementTransform(dots[1], transform_dots[1], rate_func=smooth),
            ReplacementTransform(dots[2], transform_dots[2], rate_func=rush_into),
            ReplacementTransform(dots[3], transform_dots[3], rate_func=rush_from),
            ReplacementTransform(dots[4], transform_dots[4], rate_func=slow_into),
            ReplacementTransform(dots[5], transform_dots[5], rate_func=double_smooth),
            ReplacementTransform(dots[6], transform_dots[6], rate_func=there_and_back),
            run_time=3
        )
        self.wait(2)


class RateFunctions2(Scene):
    def construct(self):
        title = VGroup(
            Text("there_and_back_with_pause", font="Monaco for Powerline").scale(0.3),
            Text("running_start", font="Monaco for Powerline").scale(0.3),
            Text("wiggle", font="Monaco for Powerline").scale(0.3),
            Text("lingering", font="Monaco for Powerline").scale(0.3),
            Text("exponential_decay", font="Monaco for Powerline").scale(0.3)
        ).arrange_submobjects(
            DOWN, aligned_edge=RIGHT, buff=0.65
        ).move_to(LEFT*7, aligned_edge=LEFT)
        dots = VGroup(
            *[
                Dot(color=BLUE).move_to([-2, i, 0])
                for i in range(2, -3, -1)
            ]
        )
        transform_dots = VGroup(
            *[
                Dot(color=BLUE).move_to([6, i, 0], aligned_edge=DOWN)
                for i in range(2, -3, -1)
            ]
        )
        self.add(title, dots)
        self.wait(2)
        self.play(
            Transform(dots[0], transform_dots[0], rate_func=there_and_back_with_pause),
            Transform(dots[1], transform_dots[1], rate_func=running_start),
            Transform(dots[2], transform_dots[2], rate_func=wiggle),
            Transform(dots[3], transform_dots[3], rate_func=lingering),
            Transform(dots[4], transform_dots[4], rate_func=exponential_decay),
            run_time=3
        )
        self.wait(2)


class RateFunctions3(Scene):
    def construct(self):
        mover = Dot(color=BLUE).move_to(UR)
        targets = [
            Dot(color=BLUE).move_to(DR),
            Dot(color=BLUE).move_to(DL),
            Dot(color=BLUE).move_to(UL)
        ]
        self.wait()
        self.add(mover)
        self.wait(2)
        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets
            ],
            run_time = 5
        ))
        self.wait(2)


class RotateAndRotating(Scene):
    def construct(self):
        title = TextMobject("Rotate").scale(2).to_corner(UL)
        dot = Dot(color=BLUE).scale(2).move_to(RIGHT * 2.5)
        self.wait()
        self.play(Write(title), ShowCreation(dot))
        self.wait(2)
        self.play(Rotate(dot, 2 * PI, about_point=ORIGIN), run_time=2)
        self.wait(2)
        title2 = TextMobject("Rotating").scale(2).to_corner(UL)
        self.play(Transform(title, title2))
        self.wait(2)
        self.play(Rotating(dot, about_point=ORIGIN), run_time=2)
        self.wait(2)
        title3 = TextMobject("Rotate", "(rate\_func=linear)").scale(2).to_corner(UL)
        title3[1].scale(0.4).next_to(title3[0], RIGHT, aligned_edge=DOWN)
        self.play(Transform(title, title3))
        self.wait(2)
        self.play(Rotate(dot, 2 * PI, about_point=ORIGIN, rate_func=linear), run_time=2)
        self.wait(3)


class Changing(Scene):
    def construct(self):
        sq = Square()
        test = AnimatedBoundary(sq)
        self.add(sq, test)
        self.wait(10)
        self.remove(sq, test)
        self.wait(2)
        point = Dot(color=BLUE)
        point.move_to(RIGHT*3)
        point.add_updater(lambda m, dt: m.rotate(dt * 20 * DEGREES, about_point=ORIGIN))
        test2 = TracedPath(point.get_center, stroke_width=4, stroke_color=RED)
        angle = Angle(RIGHT * 3, ORIGIN, point.get_center())
        angle.add_updater(lambda m: m.become(Angle(RIGHT * 3, ORIGIN, point.get_center())))
        line1 = Line(ORIGIN, RIGHT * 3)
        line2 = Line(ORIGIN, point.get_center())
        line2.add_updater(lambda m: m.put_start_and_end_on(ORIGIN, point.get_center()))
        degree = DecimalNumber(0, edge_to_fix=RIGHT).scale(2).to_corner(UR)
        degree.add_updater(lambda m: m.set_value(line2.get_angle() * 180 / PI))
        self.add(test2, angle, degree, line1, line2)
        self.add(point)
        self.wait(9.19)


class ParaFunction(Scene):
    def construct(self):
        grid = NumberPlane()
        grid.add_coordinates()
        func1 = ParametricFunction(
            lambda t: [t - 1, t, 0],
            t_min = -7,
            t_max = 7,
            color = RED
        )
        func2 = ParametricFunction(
            lambda t: [4 * np.cos(t), 2 * np.sin(t), 0],
            t_min = 0,
            t_max = 2 * PI,
            color = ORANGE
        )
        points2 = func2.points
        points3 = []
        for point in points2:
            d = abs(point[0] - point[1] + 1) / np.sqrt(2)
            if d < 0.005:
                points3.append(point)
        for point in points3:
            self.add(Dot(point))
        self.add(grid, func1, func2)


class AlwaysMove(Scene):
    def construct(self):
        text = VGroup(
            Text("cigar666", font="Source Han Sans CN").scale(0.5),
            Text("pdcxs", font="Source Han Sans CN").scale(0.5),
            Text("鹤翔万里", font="Source Han Sans CN").scale(0.5),
            Text("有一种悲伤叫颓废", font="Source Han Sans CN").scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT)
        self.add(text)
        always_shift(text, UP, 0.5)
        self.wait(5)


class TryThreeD(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=30 * DEGREES, theta=PI / 3)
        cube = Cube()
        self.add(cube)


class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u)*np.cos(v),
                np.cosh(u)*np.sin(v),
                np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        ellipsoid=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere,ellipsoid))
        self.wait()
        self.play(ReplacementTransform(ellipsoid,cone))
        self.wait()
        self.play(ReplacementTransform(cone,hip_one_side))
        self.wait()
        self.play(ReplacementTransform(hip_one_side,para_hyp))
        self.wait()
        self.play(ReplacementTransform(para_hyp,paraboloid))
        self.wait()
        self.play(ReplacementTransform(paraboloid,cylinder))
        self.wait()
        self.play(FadeOut(cylinder))


class MoveCamera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES)           
        self.play(ShowCreation(circle),ShowCreation(axes))
        #Start move camera
        self.begin_ambient_camera_rotation(rate=0.1)            
        self.wait(5)
        #Stop move camera
        self.stop_ambient_camera_rotation()                     
        #Return the position of the camera
        self.move_camera(phi=80*DEGREES,theta=-PI/2)            
        self.wait()


