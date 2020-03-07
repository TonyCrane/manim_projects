from manimlib.imports import *
from manim_projects.tony_useful.imports import *


class LinearBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([-1.5,  1.5, 0]))
        P1 = Dot(np.array([ 1.5, -1.5, 0]))
        P = VGroup(P0, P1).set_color(GRAY)

        P0_P1 = Line(P0, P1).set_color(GRAY)

        t = ValueTracker(0)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("线性贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P0_P1, B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class QuadraticBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([ -3, -1.5, 0]))
        P1 = Dot(np.array([  0,  1.5, 0]))
        P2 = Dot(np.array([1.5, -1.5, 0]))
        P = VGroup(P0, P1, P2).set_color(GRAY)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P_lines = VGroup(P0_P1, P1_P2).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q = VGroup(Q0, Q1)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center())).set_color(YELLOW)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("二次贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q0_Q1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class CubicBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([  -3, -1.5, 0]))
        P1 = Dot(np.array([-3.6,  1.5, 0]))
        P2 = Dot(np.array([   0,  1.5, 0]))
        P3 = Dot(np.array([   3, -1.5, 0]))
        P = VGroup(P0, P1, P2, P3).set_color(GRAY)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q = VGroup(Q0, Q1, Q2)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R = VGroup(R0, R1)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("三次贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R0_R1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class FourthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([-3.6, -1.5, 0]))
        P1 = Dot(np.array([-4.2,  1.5, 0]))
        P2 = Dot(np.array([   0,  1.5, 0]))
        P3 = Dot(np.array([   2, -1.5, 0]))
        P4 = Dot(np.array([   3,  0.5, 0]))
        P = VGroup(P0, P1, P2, P3, P4).set_color(GRAY)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R = VGroup(R0, R1, R2)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center())).set_color(PURPLE)
        R_lines = VGroup(R0_R1, R1_R2)

        S0 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S = VGroup(S0, S1)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center())).set_color(GOLD)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("四次贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S0_S1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class FifthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([  -3,   -2, 0]))
        P1 = Dot(np.array([-1.5,  2.5, 0]))
        P2 = Dot(np.array([   0, -0.5, 0]))
        P3 = Dot(np.array([ 1.5,    2, 0]))
        P4 = Dot(np.array([   3,    0, 0]))
        P5 = Dot(np.array([ 1.5,   -2, 0]))
        P = VGroup(P0, P1, P2, P3, P4, P5).set_color(GRAY)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P4_P5 = Line(P4, P5)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4, P4_P5).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q4 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P5.get_center() - P4.get_center()) * t.get_value() + P4.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3, Q4)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q3_Q4 = Line().add_updater(lambda m: m.put_start_and_end_on(Q3.get_center(), Q4.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3, Q3_Q4).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R3 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q4.get_center() - Q3.get_center()) * t.get_value() + Q3.get_center()))
        R = VGroup(R0, R1, R2, R3)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center()))
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center()))
        R2_R3 = Line().add_updater(lambda m: m.put_start_and_end_on(R2.get_center(), R3.get_center()))
        R_lines = VGroup(R0_R1, R1_R2, R2_R3).set_color(PURPLE)

        S0 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S2 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R3.get_center() - R2.get_center()) * t.get_value() + R2.get_center()))
        S = VGroup(S0, S1, S2)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center()))
        S1_S2 = Line().add_updater(lambda m: m.put_start_and_end_on(S1.get_center(), S2.get_center()))
        S_lines = VGroup(S0_S1, S1_S2).set_color(GOLD)

        T0 = Dot(color=PINK).add_updater(lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))
        T1 = Dot(color=PINK).add_updater(lambda m: m.move_to((S2.get_center() - S1.get_center()) * t.get_value() + S1.get_center()))
        T = VGroup(T0, T1)

        T0_T1 = Line().add_updater(lambda m: m.put_start_and_end_on(T0.get_center(), T1.get_center())).set_color(PINK)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((T1.get_center() - T0.get_center()) * t.get_value() + T0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("五次贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S_lines)
        self.add(T, T0_T1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class tTracker(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        t = ValueTracker(0)
        value = DecimalNumber(0, num_decimal_places=3).scale(3).add_updater(lambda m: m.set_value(t.get_value())).set_color(BLACK)
        label = TextMobject("t=").scale(3).next_to(value, LEFT).set_color(BLACK)
        self.add(value, label)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class WhiteBackground(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }


class VideoCover(Scene):
    def construct(self):
        background = Rectangle(width=18, height=3.5, fill_opacity=0.7, fill_color=BLACK, stroke_width=0).shift(DOWN*0.5)
        title = VGroup(
            Text("推导/原理", font="Source Han Serif CN", color=BLUE).scale(1),
            Text("贝塞尔曲线", font="Source Han Serif CN", color=RED).scale(1.4)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title_bg = VGroup(
            Text("推导/原理", font="Source Han Serif CN", color=BLUE_B).scale(1).set_stroke(width=12, opacity=0.4),
            Text("贝塞尔曲线", font="Source Han Serif CN", color=RED_B).scale(1.4).set_stroke(width=12, opacity=0.4)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title.to_edge(RIGHT, buff=1.3).shift(DOWN*0.5)
        title_bg.to_edge(RIGHT, buff=1.3).shift(DOWN*0.5)
        author = VGroup(
            TextMobject("@有一种悲伤叫颓废", background_stroke_width=0).scale(1.1).set_color([YELLOW, RED]),
            TextMobject("@鹤翔万里", background_stroke_width=0).scale(1.1).set_color([WHITE, BLUE])
        ).arrange(DOWN, aligned_edge=LEFT)
        author.shift(LEFT*3.5 + DOWN*0.5)
        self.add(background, title_bg, title, author)

class Formula1(Scene):
    def construct(self):
        formula1 = TexMobject("""
            P^k_i(t) = \\begin{cases}
            P_i & k=0\\\\
            (1-t)P^{k-1}_i(t)+tP^{k-1}_{i+1}(t) & k\\neq 0\\\\
            \\end{cases}
        """, color=BLACK, background_stroke_width=0)
        VGroup(
            formula1[0][0], formula1[0][8], formula1[0][18], formula1[0][28], 
        ).set_color(ORANGE)
        VGroup(
            formula1[0][4], formula1[0][16], formula1[0][24], formula1[0][27], formula1[0][36], 
        ).set_color(RED)
        VGroup(
            formula1[0][2], formula1[0][9], formula1[0][22], formula1[0][32:35], 
        ).set_color(GOLD)
        VGroup(
            formula1[0][1], formula1[0][19:22], formula1[0][29:32], formula1[0][10], formula1[0][38],
        ).set_color(BLUE)
        self.add(formula1)

class Formula2(Scene):
    def construct(self):
        formula2 = TexMobject("""
            B(t) &= \\sum^n_{i=0}{n\\choose i}(1-t)^{n-i}t^iP_i\\\\
                 &= \\sum^n_{i=0}P_ib_{i,n}(t)
        """, color=BLACK, background_stroke_width=0)
        VGroup(
            formula2[0][0], formula2[0][24], formula2[0][32]
        ).set_color(ORANGE)
        VGroup(
            formula2[0][2], formula2[0][17], formula2[0][22], formula2[0][39]
        ).set_color(RED)
        VGroup(
            formula2[0][7], formula2[0][12], formula2[0][21], formula2[0][23],
            formula2[0][25], formula2[0][29], formula2[0][33], formula2[0][35], 
        ).set_color(BLUE)
        VGroup(
            formula2[0][5], formula2[0][11], formula2[0][19],
            formula2[0][27], formula2[0][37], 
        ).set_color(GOLD)
        formula2[0][34].set_color(GREEN)
        self.add(formula2.scale(1.5))
