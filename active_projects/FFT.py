'''
  > File Name        : FFT.py
  > Author           : Tony_Wong
  > Created Time     : 2019/12/18 12:31:49
'''

from manimlib.imports import *
from manim_projects.tony_useful.imports import *

BROWN = "#8B4513"

class VideoTitle(VideoStart):
    CONFIG = {
        "title_name": "快速傅里叶变换($Fast\ Fourier\ Transform$)",
    }


class DotMap(Scene):
    def construct(self):
        dots = VGroup()
        for x in range(-7, 8):
            for y in range(-4, 5):
                dots.add(Dot().move_to(RIGHT * x + UP * y))
        text1 = Text("(-7, -4)", font='Consolas').scale(0.5).move_to(dots[0]).shift(RIGHT * 0.9 + UP * 0.5)
        text2 = Text("(7, 4)", font='Consolas').scale(0.5).move_to(dots[-1]).shift(DOWN * 0.5 + LEFT * 0.9)
        self.add(dots, text1, text2)


class FFTScene(Scene):
    def construct(self):
        FFTGraph = self.set_up()
        self.add(FFTGraph)

    def set_up(self):
        Input = VGroup(
            *[
                TexMobject("a_{}".format(down)).move_to([-5.8, 0.5 + i, 0]).scale(0.7).set_color(RED)
                for down, i in zip(range(0, 8), range(3, -5, -1))
            ]
        )

        line1 = VGroup(
            *[
                Line([-5.5, 0.5 + i, 0], [-4.5, 0.5 + i, 0]).add_tip(tip_length=0.15)
                for i in range(3, -5, -1)
            ]
        )
        for line in line1:
            line.get_tip().shift(LEFT * 0.5)
        
        start2 = [3.5, 2.5, 1.5, 0.5, -0.5, -1.5, -2.5, -3.5]
        end2 = [3.5, -0.5, 1.5, -2.5, 2.5, -1.5, 0.5, -3.5]
        line2 = VGroup(
            *[
                Line([-4.66, start2[i], 0], [-3.5, end2[i], 0])
                for i in range(0, 8)
            ]
        )

        line3 = VGroup(
            *[
                Line([-3.51, 0.5 + i, 0], [5.5, 0.5 + i, 0]).add_tip(tip_length=0.15)
                for i in range(3, -5, -1)
            ]
        )

        Output = VGroup(
            *[
                TexMobject("y_{}".format(down)).move_to([5.8, 0.5 + i, 0]).scale(0.7).set_color(RED)
                for down, i in zip(range(0, 8), range(3, -5, -1))
            ]
        )
        
        block1 = VGroup(
            *[
                VGroup(
                    Rectangle(height=1.3, width=0.6).move_to([-2.5, i, 0]).set_fill(BROWN, 0.5).set_stroke(BROWN, 3),
                    Line([-2.7, i + 0.5, 0], [-2.3, i - 0.5, 0]),
                    Line([-2.7, i - 0.5, 0], [-2.3, i + 0.5, 0]),
                    TexMobject("\\omega_2^0").scale(0.6).set_color(BLUE).move_to([-3.6, i, 0]),
                    Line([-3.3, i, 0], [-2.8, i, 0]).add_tip(tip_length=0.15).set_color(BLUE),
                    Line([-2.8, i + 0.5, 0], [-2.69, i + 0.5, 0]),
                    Line([-2.8, i - 0.5, 0], [-2.69, i - 0.5, 0]),
                    Line([-2.2, i + 0.5, 0], [-2.31, i + 0.5, 0]),
                    Line([-2.2, i - 0.5, 0], [-2.31, i - 0.5, 0]),
                )
                for i in [3, 1, -1, -3]
            ]
        )

        block2 = VGroup(
            *[
                VGroup(
                    Rectangle(height=2.3, width=0.6).move_to([-0.7, i, 0]).set_fill(BROWN, 0.5).set_stroke(BROWN, 3),
                    Line([-0.9, i + 1, 0], [-0.5, i - 1, 0]),
                    Line([-0.9, i - 1, 0], [-0.5, i + 1, 0]),
                    TexMobject("\\omega_4^0").scale(0.6).set_color(BLUE).move_to([-1.8, i - 0.5, 0]),
                    Line([-1.5, i - 0.5, 0], [-1.0, i - 0.5, 0]).add_tip(tip_length=0.15).set_color(BLUE),
                    Line([-1.0, i + 1, 0], [-0.89, i + 1, 0]),
                    Line([-1.0, i - 1, 0], [-0.89, i - 1, 0]),
                    Line([-0.4, i + 1, 0], [-0.51, i + 1, 0]),
                    Line([-0.4, i - 1, 0], [-0.51, i - 1, 0]),
                )
                for i in [2.5, -1.5]
            ]
        )

        block3 = VGroup(
            *[
                VGroup(
                    Rectangle(height=2.3, width=0.6).move_to([0.2, i, 0]).set_fill(BROWN, 0.5).set_stroke(BROWN, 3),
                    Line([0, i + 1, 0], [0.4, i - 1, 0]),
                    Line([0, i - 1, 0], [0.4, i + 1, 0]),
                    TexMobject("\\omega_4^1").scale(0.6).set_color(BLUE).move_to([-1.8, i - 0.5, 0]),
                    Line([-1.5, i - 0.5, 0], [-0.1, i - 0.5, 0]).add_tip(tip_length=0.15).set_color(BLUE),
                    Line([-0.1, i + 1, 0], [0.01, i + 1, 0]),
                    Line([-0.1, i - 1, 0], [0.01, i - 1, 0]),
                    Line([0.5, i + 1, 0], [0.39, i + 1, 0]),
                    Line([0.5, i - 1, 0], [0.39, i - 1, 0]),
                )
                for i in [1.5, -2.5]
            ]
        )

        block4 = VGroup(
            *[
                VGroup(
                    Rectangle(height=4.3, width=0.6).move_to([j, i, 0]).set_fill(BROWN, 0.5).set_stroke(BROWN, 3),
                    Line([j - 0.2, i + 2, 0], [j + 0.2, i - 2, 0]),
                    Line([j - 0.2, i - 2, 0], [j + 0.2, i + 2, 0]),
                    Line([j - 0.3, i + 2, 0], [j - 0.19, i + 2, 0]),
                    Line([j - 0.3, i - 2, 0], [j - 0.19, i - 2, 0]),
                    Line([j + 0.3, i + 2, 0], [j + 0.19, i + 2, 0]),
                    Line([j + 0.3, i - 2, 0], [j + 0.19, i - 2, 0]),
                )
                for i, j in zip([1.5, 0.5, -0.5, -1.5], [2, 2.8, 3.6, 4.4])
            ],
            *[
                VGroup(
                    TexMobject("\\omega_8^{}".format(i)).scale(0.6).set_color(BLUE).move_to([1, -i, 0]),
                    Line([1.3, -i, 0], [1.7 + i * 0.8, -i, 0]).add_tip(tip_length=0.15).set_color(BLUE),
                )
                for i in [0, 1, 2, 3]
            ]
        )

        return VGroup(
            Input, line1, line2, line3, block1, block2, block3, block4, Output
        )


class VideoCover(FFTScene):
    def construct(self):
        self.add_background()
        block = Rectangle(
            height=2, width=11.5, stroke_width=0
        ).shift(UP * 0.85).set_fill(DARK_GRAY, 0.9)
        self.add(block)
        self.add_main()
        self.add_subscripts()

    def add_main(self):
        title  = TextMobject("快\\ 速\\ 傅\\ 里\\ 叶\\ 变\\ 换").scale(2.3).set_color(BLUE).move_to(UP*0.5)
        entitle = TextMobject("\\texttt{Fast }","\\texttt{Fourier }", "\\texttt{Transform}").next_to(title, UP).set_color(YELLOW).set_width(title.get_width())
        fast1 = TextMobject("\\texttt{Fast }").set_color(GRAY).set_width(entitle[0].get_width()).next_to(entitle[0], UP)
        fast2 = TextMobject("\\texttt{Fast }").set_color(GRAY).set_width(entitle[0].get_width()).next_to(entitle[1], UP)
        tle   = TextMobject("\\texttt{TLE}").set_color(GRAY).set_height(entitle[0].get_height()).next_to(entitle[2], UP)
        xentitle = VGroup(fast1, fast2, tle)
        author = TextMobject("@鹤翔万里").scale(1.2).set_color([BLUE, YELLOW, ORANGE, RED]).next_to(title, DOWN, buff=1.2)
        line = Line(fast1.get_left(), entitle.get_right()+fast1.get_left()-entitle.get_left()).set_color(GRAY)
        
        self.add(title, entitle, author, xentitle, line)

    def add_background(self):
        FFTGraph = self.set_up().set_opacity(0.4)
        self.add(FFTGraph)

    def add_subscripts(self):
        square = Square().rotate(PI / 4).scale(1.5).set_fill(BLUE, 1).set_color(BLUE)
        square.move_to(LEFT * 7.3 + UP * 4.6)
        text = Text("???", font='Source Han Serif CN', stroke_width=1.5).scale(0.7).rotate(PI / 4).next_to(square.get_edge_center(DOWN), buff=0)
        text.shift(UP * 1.3 + RIGHT * 0.24)

        self.add(square, text)


class SubTitleOfComplexNumber(Scene):
    CONFIG = {
        "subtitle" : "复数"
    }
    def construct(self):
        main = TextMobject(
            "$\\langle$", self.subtitle, "$\\rangle$"
        )
        new_langle = TexMobject("\\langle/")
        new_langle.scale(2)
        main.scale(2)
        new_langle.move_to(main[0], RIGHT)

        self.wait(2)
        self.play(Write(main))
        self.wait(2)
        self.play(Transform(main[0], new_langle))
        self.wait(2)


class SubTitleOfUnitRoot(SubTitleOfComplexNumber):
    CONFIG = {
        "subtitle" : "单位根"
    }


class SubTitleOfPolynomial(SubTitleOfComplexNumber):
    CONFIG = {
        "subtitle" : "多项式"
    }


class SubTitleOfFFT(SubTitleOfComplexNumber):
    CONFIG = {
        "subtitle" : "DFT及FFT原理推导"
    }


class SubTitleOfCode(SubTitleOfComplexNumber):
    CONFIG = {
        "subtitle" : "C++代码实现"
    }


class SubTitleOfFastFFT(SubTitleOfComplexNumber):
    CONFIG = {
        "subtitle" : "FFT高效实现"
    }


class SubTitleOfIFFT(SubTitleOfComplexNumber):
    CONFIG = {
        "subtitle" : "FFT逆变换"
    }


class SubTitleOfConvolution(SubTitleOfComplexNumber):
    CONFIG = {
        "subtitle" : "FFT求多项式卷积"
    }
    

class PreviewVideo(Scene):
    def construct(self):
        screen_rect = ScreenRectangle(height=6).shift(UP * 0.4)
        self.wait(1)
        self.play(ShowCreation(screen_rect))
        self.wait(5)


class IndexOfPreKnowledge(Scene):
    def construct(self):
        title = Title("前置知识索引").set_color(BLUE)
        self.play(Write(title))
        topics = VGroup(
            TextMobject("复数"),
            TextMobject("单位根"),
            TextMobject("多项式"),
        )
        for topic in topics:
            topic.scale(1.3)
            dot = Dot(color=BLUE).scale(1.5)
            dot.next_to(topic, LEFT)
            topic.add(dot)
        topics.arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=LARGE_BUFF
        ).move_to(LEFT * 2 + DOWN * 0.3)
        
        self.play(Write(topics))

        self.wait(3)
        for i in range(len(topics)):
            self.play(
                topics[i + 1:].set_fill, {"opacity": 0.25},
                topics[:i].set_fill, {"opacity": 0.25},
                topics[i].set_fill, {"opacity": 1},
            )
            self.wait(4)
        self.play(
            topics[0].set_fill, {"opacity": 1},
            topics[1].set_fill, {"opacity": 1},
        )
        self.wait(4)
    

class ComplexNumber(Scene):
    def construct(self):
        title = VGroup(
            Text("复数", font="Source Han Sans CN").set_color(BLUE).scale(0.8),
            Text("Complex Number", font="Monaco for Powerline").set_color(BLUE).scale(0.5)
        ).arrange_submobjects(
            RIGHT, buff=0.5, aligned_edge=DOWN
        ).move_to([-1, 3.2, 0])
        line = Line(LEFT, RIGHT).next_to([0, 2.8, 0], DOWN, buff=MED_SMALL_BUFF).set_color(BLUE).set_width(FRAME_WIDTH - 2)
        title.add(line)
        t2c = {
            "a" : BLUE_B,
            "b" : BLUE_E,
            "c" : TEAL_A,
            "d" : TEAL_E,
            "i" : GREEN,
            "e" : BLUE,
            "\\theta" : ORANGE,
            "\\over" : WHITE,
            "^2" : YELLOW_B,
            "\\sin" : WHITE,
            "\\cos" : WHITE
        }
        topics = VGroup(
            TextMobject("定义: ", "$z=a+bi$\ \ ", "其中$a,b\in \mathbb{R}\ \ i=\sqrt{-1}$", "$z=re^{i\\theta}$"),
            TexMobject("\\text{加法法则: }", "(", "a", "+", "b", "i", ")", "+", "(", "c", "+", "d", "i", ")", \
                       "=", "(", "a", "+", "c", ")", "+", "(", "b", "+", "d", ")", "i").set_color_by_tex_to_color_map(t2c),
            TexMobject("\\text{乘法法则: }", "(", "a", "+", "b", "i", ")", "(", "c", "+", "d", "i", ")", "=", \
                       "a", "c", "+", "a", "d", "i", "+", "b", "c", "i", "+", "b", "d", "i", "^2").set_color_by_tex_to_color_map(t2c),
            TexMobject("\\text{除法法则: }", "{{a", "+", "b", "i}", "\\over", "{c", "+", "d", "i}}", \
                       "=", "{{a", "c", "+", "b", "d}", "\\over", "{c", "^2", "+", "d", "^2}}", "+", \
                       "{{b", "c", "-", "a", "d}", "\\over", "{c", "^2", "+", "d", "^2}}", "i").set_color_by_tex_to_color_map(t2c),
            TexMobject("\\text{欧拉定理: }", "e", "^{i", "\\theta}", "=", "\\cos", "\\theta", "+", "i", "\\sin", "\\theta").set_color_by_tex_to_color_map(t2c)
        )
        for topic in topics:
            topic.scale(0.8)
            dot = Dot()
            dot.next_to(topic, LEFT)
            topic[0].add(dot)
            topic[0].set_color(GOLD)
        topics.arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).shift(DOWN * 0.5)
        topics[0][2].scale(0.8, about_edge=DOWN).set_color(LIGHT_GRAY)
        topics.next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(title))
        self.wait(2)
        self.play(Write(topics[0][0]))
        self.wait(0.5)
        self.play(
            Write(topics[0][1]),
            Write(topics[0][2])
        )
        self.wait(2)
        self.play(Write(topics[1][0]))
        self.play(
            *[
                Write(topics[1][i])
                for i in range(1, 15)
            ]
        )
        self.wait(2)
        self.play(
            TransformFromCopy(topics[1][2], topics[1][16]),
            TransformFromCopy(topics[1][7], topics[1][17]),
            TransformFromCopy(topics[1][9], topics[1][18]),
            run_time=2
        )
        self.play(FadeIn(topics[1][15]), FadeIn(topics[1][19]))
        self.play(Write(topics[1][20]))
        self.play(
            TransformFromCopy(topics[1][4], topics[1][22]),
            TransformFromCopy(topics[1][7], topics[1][23]),
            TransformFromCopy(topics[1][11], topics[1][24]),
            run_time=2
        )
        self.play(FadeIn(topics[1][21]), FadeIn(topics[1][25]))
        self.play(
            TransformFromCopy(VGroup(topics[1][5], topics[1][12]), topics[1][26], run_time = 1.5)
        )
        self.wait(0.5)
        self.play(ShowCreationThenDestructionAround(VGroup(*[topics[1][i] for i in range(15, 27)])))
        self.wait(3)
        self.play(
            topics[1][7].set_color, YELLOW
        )
        self.play(
            topics[1][17].set_color, YELLOW,
            topics[1][23].set_color, YELLOW
        )
        self.wait(3)
        self.play(
            topics[1][7].set_color, WHITE,
            topics[1][17].set_color, WHITE,
            topics[1][23].set_color, WHITE,
        )
        self.wait(2)

        self.play(Write(topics[2][0]))
        self.play(
            *[
                Write(topics[2][i])
                for i in range(1, 14)
            ]
        )
        self.wait(2)
        self.play(
            TransformFromCopy(topics[2][2], topics[2][14]),
            TransformFromCopy(topics[2][8], topics[2][15]),
            run_time=1.25
        )
        self.play(Write(topics[2][16]))
        self.play(
            TransformFromCopy(topics[2][2], topics[2][17]),
            TransformFromCopy(topics[2][10], topics[2][18]),
            TransformFromCopy(topics[2][11], topics[2][19]),
            run_time=1.25
        )
        self.play(Write(topics[2][20]))
        self.play(
            TransformFromCopy(topics[2][4], topics[2][21]),
            TransformFromCopy(topics[2][5], topics[2][23]),
            TransformFromCopy(topics[2][8], topics[2][22]),
            run_time=1.25
        )
        self.play(Write(topics[2][24]))
        self.play(
            TransformFromCopy(topics[2][4], topics[2][25]),
            TransformFromCopy(topics[2][10], topics[2][26]),
            TransformFromCopy(VGroup(topics[2][5], topics[2][11]), topics[2][27:]),
            run_time=1.25
        )
        self.wait(3)
        self.play(
            Transform(topics[2][24], TexMobject("-").scale(0.8).move_to(topics[2][24])),
            FadeOut(topics[2][27:])
        )
        self.wait(2)
        Final_x = TexMobject("(", "a", "c", "-", "b", "d", ")", "+", "(", "a", "d", "+", "b", "c", ")", "i").scale(0.8).move_to(topics[2][14], LEFT).set_color_by_tex_to_color_map(t2c)
        self.play(
            Transform(
                VGroup(
                    *[topics[2][i] for i in range(14, 27)]
                ), Final_x
            )
        )
        self.wait(0.5)
        self.play(ShowCreationThenDestructionAround(Final_x))
        self.wait(3)
        self.play(Write(topics[3][0]))
        self.wait(1)
        self.play(Write(topics[3][1:]))
        self.wait(3)
        self.play(Write(topics[4][0]))
        self.wait(1)
        self.play(Write(topics[4][1:]))
        self.wait(3)
        self.play(FadeInFromLarge(topics[0][3]))
        self.wait(5)


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


class VideoFrom3B1B(Scene):
    def construct(self):
        icon1 = SVGMobject("video_icon").set_color(PINK).scale(0.5)
        av1   = TextMobject("av11339177")
        screen1 = ScreenRectangle(height=3)
        title1 = Text("欧拉公式与初等群论", font="Source Han Sans CN").scale(0.5)
        av1.next_to(icon1, RIGHT)
        screen1.next_to(VGroup(icon1, av1), DOWN)
        title1.next_to(screen1, DOWN)
        av11339177 = VGroup(icon1, av1, screen1, title1)
        av11339177.move_to([-3, 1, 0])

        icon2 = SVGMobject("video_icon").set_color(PINK).scale(0.5)
        av2   = TextMobject("av63666593")
        screen2 = ScreenRectangle(height=3)
        title2 = Text("在3.14分钟内理解e^iπ", font="Source Han Sans CN").scale(0.5)
        av2.next_to(icon2, RIGHT)
        screen2.next_to(VGroup(icon2, av2), DOWN)
        title2.next_to(screen2, DOWN)
        av63666593 = VGroup(icon2, av2, screen2, title2)
        av63666593.move_to([3, 1, 0])
        
        self.play(
            ShowCreation(av11339177[2]),
            ShowCreation(av63666593[2])
        )
        self.play(
            Write(av11339177[3]),
            Write(av63666593[3])
        )
        self.play(
            FadeIn(av11339177[0]),
            FadeIn(av63666593[0]),
            FadeIn(av11339177[1]),
            FadeIn(av63666593[1]),
        )
        self.wait(3)


# class UnitRoot(Scene):
#     def construct(self):
        

class Polynomial_part1(Scene):
    def construct(self):
        title = Title2("多项式", font="Source Han Sans CN").set_color(BLUE)
        self.play(Write(title))
        self.wait()
        t2c = {
            
        }
        formula = TexMobject("F", "(", "x", ")", "=", "a", "_0", "+", "a", "_1", "x", "+", "a", "_2", "x", "^2", \
                             "+", "\\cdots", "+", "a", "_n", "x", "^n").set_color_by_tex_to_color_map(
            {
                "F" : ORANGE,
                "x" : RED,
                "a" : GREEN,
                "_0": BLUE_D,
                "_1": BLUE_D,
                "_2": BLUE_D,
                "_n": BLUE_D,
                "^2": BLUE_E,
                "^n": BLUE_E,
            }
        )
        formula.next_to(title, DOWN)
        formula2 = TexMobject("=", "\\sum", "_{i", "=", "0}", "^n", "a", "_i", "x", "^i").set_color_by_tex_to_color_map(
            {
                "x" : RED,
                "a" : GREEN,
                "_i": BLUE_D,
                "^i": BLUE_E,
            }
        ).next_to(formula[4], DOWN, aligned_edge=LEFT)
        formula2[3].set_color(BLUE)
        formula2[1].set_color(GOLD)
        self.play(Write(formula))
        self.wait(2)
        self.play(Write(formula2[:6]))
        self.play(
            TransformFromCopy(
                VGroup(*[formula[i] for i in [4, 5, 7, 8, 11, 12, 16, 18, 19]]),
                VGroup(formula2[6], formula2[7])
            ), run_time=2
        )
        self.play(
            TransformFromCopy(
                VGroup(*[formula[i] for i in [9, 13, 14, 16, 20, 21]]),
                VGroup(formula2[8], formula2[9])
            ), run_time=2
        )
        self.wait(2)
        deg = Text("次数: ", font="Source Han Serif CN").scale(0.6).move_to([-5, formula2.get_center()[1] - 2, 0])
        deg.set_color(GOLD)
        dot = Dot().next_to(deg, LEFT).set_color(GOLD)
        deg.add(dot)
        degree = TextMobject("degree(", "$F$", ")", "=", "$n$").next_to(deg, RIGHT)
        degree[1].set_color(ORANGE)
        degree[4].set_color(GOLD)
        self.wait(1)
        self.play(Write(deg))
        self.wait()
        self.play(Write(degree[0]), Write(degree[2]))
        self.play(TransformFromCopy(formula[0], degree[1]), run_time=1.5)
        self.play(Write(degree[3]))
        self.play(TransformFromCopy(formula2[1], degree[4]), run_time=1.5)
        self.wait(2)
        maxdeg = Text("次数界: ", font="Source Han Serif CN").scale(0.6).move_to([1.5, deg.get_center()[1], 0])
        maxdeg.set_color(GOLD)
        dot2 = Dot().next_to(maxdeg, LEFT).set_color(GOLD)
        maxdeg.add(dot2)
        maxdegree = TextMobject(">", "degree(", "$F$", ")", "=", "$n$").next_to(maxdeg, RIGHT)
        maxdegree[2].set_color(ORANGE)
        maxdegree[5].set_color(GOLD)
        self.play(Write(maxdeg))
        self.wait()
        self.play(Write(maxdegree[0]))
        self.wait()
        self.play(
            TransformFromCopy(degree, maxdegree[1:]), run_time=1.5
        )
        self.wait(3)


class Polynomial_part2(Scene):
    def construct(self):
        title = Title2("多项式", font="Source Han Sans CN").set_color(BLUE)
        self.add(title)
        self.wait()
        title_plus = SubTopic("多项式加法").scale(0.8).move_to([-4, title.get_bottom()[1] - 0.5, 0])
        self.play(Write(title_plus))
        self.wait()
        t2c = {
            "A" : ORANGE,
            "B" : ORANGE,
            "C" : ORANGE,
            "x" : RED,
            "a" : GREEN,
            "b" : GREEN,
            "c" : GREEN,
            "_0": BLUE_D,
            "_1": BLUE_D,
            "_2": BLUE_D,
            "_n": BLUE_D,
            "^2": BLUE_E,
            "^n": BLUE_E,
            "\\cdots": WHITE
        }
        formula_A = TexMobject("A", "(", "x", ")", "=", "a", "_0", "+", "a", "_1", "x", "+", "a", "_2", "x", "^2", \
                               "+", "\\cdots", "+", "a", "_n", "x", "^n").set_color_by_tex_to_color_map(t2c)
        formula_B = TexMobject("B", "(", "x", ")", "=", "b", "_0", "+", "b", "_1", "x", "+", "b", "_2", "x", "^2", \
                               "+", "\\cdots", "+", "b", "_n", "x", "^n").set_color_by_tex_to_color_map(t2c)
        formula_C = TexMobject("C", "(", "x", ")", "=", "(", "a", "_0", "+", "b", "_0", ")", "+", "(", "a", "_1", \
                               "+", "b", "_1", ")", "x", "+", "(", "a", "_2", "+", "b", "_2", ")", "x", "^2", "\\\\", \
                               "+", "\\cdots", "+", "(", "a", "_n", "+", "b", "_n", ")", "x", "^n").set_color_by_tex_to_color_map(t2c)
        formula_A.next_to(title_plus, DOWN, aligned_edge=LEFT)
        formula_B.next_to(formula_A[4].get_center(), DOWN, index_of_submobject_to_align=4, buff=1.3)
        plus = TexMobject("+").next_to(formula_A[:4], DOWN)
        equal = TexMobject("=").rotate(PI / 2).next_to(formula_B[:4], DOWN)
        formula_C.next_to(equal.get_bottom(), DOWN, index_of_submobject_to_align=1)
        formula_C[-12:].next_to(formula_C[5], DOWN, aligned_edge=LEFT)
        self.play(Write(formula_A))
        self.wait()
        self.play(Write(formula_B))
        self.wait()
        self.play(Write(plus))
        self.wait(0.2)
        self.play(Write(equal))
        self.play(Write(formula_C[:5]))
        self.wait()
        self.play(
            TransformFromCopy(formula_A[5:7], formula_C[6:8]),
            TransformFromCopy(formula_B[5:7], formula_C[9:11]),
            run_time=1.5
        )
        self.play(FadeIn(formula_C[5]), FadeIn(formula_C[8]), FadeIn(formula_C[11]))
        self.play(TransformFromCopy(VGroup(formula_A[7], formula_B[7]), formula_C[12]))
        self.wait(2)
        self.play(
            TransformFromCopy(formula_A[8:10], formula_C[14:16]),
            TransformFromCopy(formula_B[8:10], formula_C[17:19]),
            run_time=1.5
        )
        self.play(FadeIn(formula_C[13]), FadeIn(formula_C[16]), FadeIn(formula_C[19]))
        self.play(
            TransformFromCopy(VGroup(formula_A[10], formula_B[10]), formula_C[20]),
            run_time=1.5
        )
        self.play(TransformFromCopy(VGroup(formula_A[11], formula_B[11]), formula_C[21]))
        self.wait()
        self.play(
            TransformFromCopy(formula_A[12:14], formula_C[23:25]),
            TransformFromCopy(formula_B[12:14], formula_C[26:28]),
        )
        self.play(FadeIn(formula_C[22]), FadeIn(formula_C[25]), FadeIn(formula_C[28]))
        self.play(
            TransformFromCopy(VGroup(formula_A[14:16], formula_B[14:16]), formula_C[29:31])
        )
        self.play(TransformFromCopy(VGroup(formula_A[16], formula_B[16]), formula_C[32]))
        self.wait()
        self.play(TransformFromCopy(VGroup(formula_A[17], formula_B[17]), formula_C[33]))
        self.play(TransformFromCopy(VGroup(formula_A[18], formula_B[18]), formula_C[34]))
        self.wait()
        self.play(
            TransformFromCopy(formula_A[19:21], formula_C[36:38]),
            TransformFromCopy(formula_B[19:21], formula_C[39:41])
        )
        self.play(FadeIn(formula_C[35]), FadeIn(formula_C[38]), FadeIn(formula_C[41]))
        self.play(
            TransformFromCopy(VGroup(formula_A[21:], formula_B[21:]), formula_C[42:])
        )
        self.wait(3)

        t2c2 = {
            "x" : RED,
            "a" : GREEN,
            "b" : GREEN,
            "c" : GREEN,
            "_i": BLUE_D,
            "^i": BLUE_E,
        }
        A = TexMobject("\\sum\\nolimits", "_{i", "=", "0}", "^n", "a", "_i", "x", "^i").set_color_by_tex_to_color_map(t2c2)
        B = TexMobject("\\sum\\nolimits", "_{i", "=", "0}", "^n", "b", "_i", "x", "^i").set_color_by_tex_to_color_map(t2c2)
        C = TexMobject("\\sum\\nolimits", "_{i", "=", "0}", "^n", "c", "_i", "x", "^i").set_color_by_tex_to_color_map(t2c2)
        A.move_to(formula_A[5], aligned_edge=LEFT)
        B.move_to(formula_B[5], aligned_edge=LEFT)
        C.move_to(formula_C[5], aligned_edge=LEFT)
        A[1].set_color(GOLD)
        B[1].set_color(GOLD)
        C[1].set_color(GOLD)
        A[2].set_color(BLUE)
        B[2].set_color(BLUE)
        C[2].set_color(BLUE)
        self.play(Transform(formula_A[5:], A))
        self.wait()
        self.play(Transform(formula_B[5:], B))
        self.wait()
        self.play(Transform(formula_C[5:], C))
        self.wait()
        c = TexMobject("c", "_i", "=", "a", "_i", "+", "b", "_i").set_color_by_tex_to_color_map(t2c2)
        c.next_to(C, RIGHT, buff=1)
        self.play(FadeInFrom(c, RIGHT))
        self.wait(3)


class Polynomial_part3_1(Scene):
    def construct(self):
        title = Title2("多项式", font="Source Han Sans CN").set_color(BLUE)
        self.add(title)
        self.wait()
        title_plus = SubTopic("多项式乘法").scale(0.8).move_to([-4, title.get_bottom()[1] - 0.5, 0])
        self.play(Write(title_plus))
        self.wait(4)


class Polynomial_part3_2(Scene): # Thanks @有一种悲伤叫颓废
    def construct(self):
        pos = VGroup(*[TextMobject(str(0)) for t in range(27)])\
        	.arrange(RIGHT).to_edge(UP).shift(DOWN)

        num = lambda i:TexMobject(str(i)).set_color(GREEN)
        dgt = lambda i:TexMobject("^"+str(i)).set_color(BLUE)
        add = lambda: TexMobject("+")
        sub = lambda: TexMobject("-")
        eks = lambda: TexMobject("x").set_color(RED)

        text1 = VGroup(
        	num(6), VGroup(eks(), dgt(3)), add(), num(7), VGroup(eks(), dgt(2)), sub(), num(1), num(0), eks(), add(), num(9), 
        ).arrange(RIGHT/2)

        for i in [2,5]:
        	text1[i-1][1].next_to(text1[i-1][0], (RIGHT+UP)/2).shift(DOWN*0.15)
		
        text1[0:2].move_to(pos[13:16].get_center()).align_to(pos, DOWN)
        text1[2].move_to(pos[16].get_center()).shift(UP*0.1)
        text1[3:5].move_to(pos[17:20].get_center()).align_to(pos, DOWN)
        text1[5].move_to(pos[20].get_center()).shift(UP*0.1)
        text1[6:9].move_to(pos[21:24].get_center()).align_to(pos, DOWN)
        text1[9].move_to(pos[24].get_center()).shift(UP*0.1)
        text1[10].move_to(pos[25:27].get_center()).align_to(pos, DOWN)

        text2 = VGroup(
        	sub(), num(2), VGroup(eks(), dgt(3)), add(), num(4), eks(), sub(), num(5)
        ).arrange(RIGHT/2)

        text2[2][1].next_to(text2[2][0], (RIGHT+UP)/2).shift(DOWN*0.15)
		
        pos.shift(DOWN)
        text2[0].move_to(pos[12].get_center()).shift(UP*0.1)
        text2[1:3].move_to(pos[13:16].get_center()).align_to(pos, DOWN)
        text2[3].move_to(pos[20].get_center()).shift(UP*0.1)
        text2[4:6].move_to(pos[21:24].get_center()).align_to(pos, DOWN)
        text2[6].move_to(pos[24].get_center()).shift(UP*0.1)
        text2[7].move_to(pos[25:27].get_center()).align_to(pos, DOWN)

        line1 = Line(ORIGIN, RIGHT*8).next_to(text2, DOWN, buff=0.34)\
        	.set_stroke(width=5, color=WHITE, opacity=0.5)\
        	.align_to(pos, RIGHT)
		
        self.play(Write(text1), run_time=2)
        self.wait()
        self.play(Write(text2), run_time=2)
        self.wait()
        self.play(ShowCreation(line1))
        self.wait()

        multi = TexMobject("\\times").scale(1.5).next_to(text2, LEFT).align_to(text2, DOWN).shift(LEFT*0.5)
        self.play(DrawBorderThenFill(multi))
        self.play(ScaleInPlace(multi, 3, rate_func = wiggle))

        text3 = VGroup(
        	sub(), num(3), num(0), VGroup(eks(), dgt(3)), sub(), num(3), num(5), VGroup(eks(), dgt(2)), add(), num(5), num(0), eks(), sub(), num(4), num(5), 
        ).arrange(RIGHT/2)

        for i in [4,8]:
        	text3[i-1][1].next_to(text3[i-1][0], (RIGHT+UP)/2).shift(DOWN*0.15)

        pos.shift(DOWN)
        text3[0].move_to(pos[12].get_center()).shift(UP*0.1)
        text3[1:4].move_to(pos[13:16].get_center()).align_to(pos, DOWN)
        text3[4].move_to(pos[16].get_center()).shift(UP*0.1)
        text3[5:8].move_to(pos[17:20].get_center()).align_to(pos, DOWN)
        text3[8].move_to(pos[20].get_center()).shift(UP*0.1)
        text3[9:12].move_to(pos[21:24].get_center()).align_to(pos, DOWN)
        text3[12].move_to(pos[24].get_center()).shift(UP*0.1)
        text3[13:15].move_to(pos[25:27].get_center()).align_to(pos, DOWN)

        self.play(
        	ShowCreationThenDestructionAround(text1), 
        	ShowCreationThenDestructionAround(text2[6:8])
        )
        self.play(Write(text3), run_time=2)
        self.wait()
		
        text4 = VGroup(
        	num(2), num(4), VGroup(eks(), dgt(4)), add(), num(2), num(8), VGroup(eks(), dgt(3)), sub(), num(4), num(0), VGroup(eks(), dgt(2)), add(), num(3), num(6), eks(), 
        ).arrange(RIGHT/2)

        for i in [3,7,11]:
        	text4[i-1][1].next_to(text4[i-1][0], (RIGHT+UP)/2).shift(DOWN*0.15)

        pos.shift(DOWN)
        text4[0:3].move_to(pos[9:12].get_center()).align_to(pos, DOWN)
        text4[3].move_to(pos[12].get_center()).shift(UP*0.1)
        text4[4:7].move_to(pos[13:16].get_center()).align_to(pos, DOWN)
        text4[7].move_to(pos[16].get_center()).shift(UP*0.1)
        text4[8:11].move_to(pos[17:20].get_center()).align_to(pos, DOWN)
        text4[11].move_to(pos[20].get_center()).shift(UP*0.1)
        text4[12:15].move_to(pos[21:24].get_center()).align_to(pos, DOWN)

        self.play(
        	ShowCreationThenDestructionAround(text1), 
        	ShowCreationThenDestructionAround(text2[3:6])
        )
        self.play(Write(text4), run_time=2)
        self.wait()

        text5 = VGroup(
        	sub(), num(1), num(2), VGroup(eks(), dgt(6)), sub(), num(1), num(4), VGroup(eks(), dgt(5)), add(), num(2), num(0), VGroup(eks(), dgt(4)), sub(), num(1), num(8), VGroup(eks(), dgt(3)), 
        ).arrange(RIGHT/2)

        for i in [4,8,12,16]:
        	text5[i-1][1].next_to(text5[i-1][0], (RIGHT+UP)/2).shift(DOWN*0.15)

        pos.shift(DOWN)
        for i in range(4):
        	text5[4*i].move_to(pos[4*i].get_center()).shift(UP*0.1)
        	text5[1+4*i:4+4*i].move_to(pos[1+4*i:4+4*i].get_center()).align_to(pos, DOWN)

        self.play(
        	ShowCreationThenDestructionAround(text1), 
        	ShowCreationThenDestructionAround(text2[0:3])
        )
        self.play(Write(text5), run_time=2)
        self.wait()

        line2 = Line(ORIGIN, RIGHT*12.7).next_to(text5, DOWN, buff=0.34)\
        	.set_stroke(width=5, color=WHITE, opacity=0.5)\
        	.align_to(pos, RIGHT)

        self.play(ShowCreation(line2))
        self.wait()

        text6 = VGroup(
        	sub(), num(1), num(2), VGroup(eks(), dgt(6)), sub(), num(1), num(4), VGroup(eks(), dgt(5)), add(), num(4), num(4), VGroup(eks(), dgt(4)), 
        	sub(), num(2), num(0), VGroup(eks(), dgt(3)), sub(), num(7), num(5), VGroup(eks(), dgt(2)), add(), num(8), num(6), eks(), sub(), num(4), num(5), 
        ).arrange(RIGHT/2)

        for i in [4,8,12,16,20]:
        	text6[i-1][1].next_to(text6[i-1][0], (RIGHT+UP)/2).shift(DOWN*0.15)

        pos.shift(DOWN)
        for i in range(6):
        	text6[4*i].move_to(pos[4*i].get_center()).shift(UP*0.1)
        	text6[1+4*i:4+4*i].move_to(pos[1+4*i:4+4*i].get_center()).align_to(pos, DOWN)

        text6[24].move_to(pos[24].get_center()).shift(UP*0.1)
        text6[25:27].move_to(pos[25:27].get_center()).align_to(pos, DOWN)

        text6_bg = VGroup(
        	SurroundingRectangle(VGroup(text3[12:15]), color=YELLOW, fill_opacity=0), 
        	SurroundingRectangle(VGroup(text3[8:12], text4[11:15]), color=YELLOW, fill_opacity=0), 
        	SurroundingRectangle(VGroup(text3[4:8], text4[7:11]), color=YELLOW, fill_opacity=0), 
        	SurroundingRectangle(VGroup(text3[0:4], text4[3:7], text5[12:16]), color=YELLOW, fill_opacity=0), 
        	SurroundingRectangle(VGroup(text4[0:3], text5[8:12]), color=YELLOW, fill_opacity=0), 
        	SurroundingRectangle(VGroup(text5[4:8]), color=YELLOW, fill_opacity=0), 
        	SurroundingRectangle(VGroup(text5[0:4]), color=YELLOW, fill_opacity=0), 
        )

        self.play(ScaleInPlace(text6_bg[0], 3, rate_func = wiggle))
        self.play(ReplacementTransform(text6_bg[0], text6[24:27]))
        self.wait()

        for i in range(6):
        	self.play(ScaleInPlace(text6_bg[i+1], 3, rate_func = wiggle))
        	self.play(ReplacementTransform(text6_bg[i+1], text6[20-4*i:24-4*i]))
        	self.wait()

        self.wait()


class Polynomial_part3_3(Scene):
    def construct(self):
        title = Title2("多项式", font="Source Han Sans CN").set_color(BLUE)
        title_mul = SubTopic("多项式乘法").scale(0.8).move_to([-4, title.get_bottom()[1] - 0.5, 0])
        self.add(title, title_mul)
        self.wait()
        t2c2 = {
            "A" : ORANGE,
            "B" : ORANGE,
            "C" : ORANGE,
            "x" : RED,
            "a" : GREEN,
            "b" : GREEN,
            "c" : GREEN,
            "_i": BLUE_D,
            "^i": BLUE_E,
        }
        A = TexMobject("A", "(", "x", ")", "=", "\\sum\\nolimits", "_{i", "=", "0}", "^n", "a", "_i", "x", "^i").set_color_by_tex_to_color_map(t2c2)
        B = TexMobject("B", "(", "x", ")", "=", "\\sum\\nolimits", "_{i", "=", "0}", "^n", "b", "_i", "x", "^i").set_color_by_tex_to_color_map(t2c2)
        formula_C = TexMobject("C", "(", "x", ")", "=", "A", "(", "x", ")", "B", "(", "x", ")").set_color_by_tex_to_color_map(t2c2)
        C = TexMobject("C", "(", "x", ")", "=", "\\sum\\nolimits", "_{i", "=", "0}", "^{2n}", "c", "_i", "x", "^i").set_color_by_tex_to_color_map(t2c2)
        A[6].set_color(GOLD)
        B[6].set_color(GOLD)
        C[6:8].set_color(GOLD)
        A[7].set_color(BLUE)
        B[7].set_color(BLUE)
        C[8].set_color(BLUE)
        A.next_to(title_mul, DOWN, aligned_edge=LEFT)
        B.next_to(A, RIGHT, buff=2)
        C.next_to(A[4].get_center(), DOWN, index_of_submobject_to_align=4, buff=1.3)
        deg = TextMobject("degree(", "$C$", ")=degree(", "$A$", ")+degree(", "$B$", ")").scale(0.8)
        deg.next_to(C, RIGHT, buff=1)
        deg[1].set_color(ORANGE)
        deg[3].set_color(ORANGE)
        deg[5].set_color(ORANGE)
        ci = TexMobject("c", "_i", "=", "\\sum\\nolimits", "_{j", "=", "0}", "^i", "a", "_j", "b", "_{i-j}")
        ci.next_to(C, DOWN, aligned_edge=LEFT, buff=0.85)
        ci[0].set_color(GREEN)
        ci[8].set_color(GREEN)
        ci[10].set_color(GREEN)
        ci[1].set_color(BLUE_D)
        ci[9].set_color(BLUE_D)
        ci[11].set_color(BLUE_D)
        ci[4].set_color(GOLD)
        ci[5].set_color(BLUE)
        c = TexMobject("c", "=", "a", "\\otimes", "b").next_to(ci, RIGHT, buff=1)
        c[0].set_color(GREEN)
        c[2].set_color(GREEN)
        c[4].set_color(GREEN)

        self.play(Write(A))
        self.play(Write(B))
        self.wait(2)
        self.play(FadeInFromDown(deg))
        self.wait(2)
        self.play(Write(C))
        self.wait(2)
        self.play(Write(ci))
        self.wait(2)
        self.play(FadeInFrom(c, LEFT))
        self.wait(3)


class Polynomial_part4(Scene):
    def construct(self):
        mid_line = DashedLine([0, 5, 0], [0, -5, 0])
        self.play(ShowCreation(mid_line))
        self.wait()
        self.left()
        self.wait()
        self.right()
    
    def left(self):
        title1 = Text("系数表示", font="Source Han Sans CN").set_color(BLUE).scale(0.57).move_to([-5.2, 3.3, 0])
        self.play(Write(title1))
        coef = TexMobject("\\boldsymbol{a}", "=", "[", "a", "_0", ",", "a", "_1", ",", "a", "_2", ",", "\\cdots", ",", "a", "_n", "]^\\top")\
            .set_color_by_tex_to_color_map({"a":GREEN, "\\boldsymbol{a}":RED, "_0":BLUE, "_1":BLUE, "_2":BLUE, "_n":BLUE})
        coef.next_to(title1, DOWN, aligned_edge=LEFT).shift(RIGHT*0.5)
        self.play(Write(coef))
        self.wait()

        t2c = {
            "{c}" : GREEN,
            "{_i}": BLUE,
            "{a}" : GREEN,
            "{b}" : GREEN,
        }

        sub1_1 = SubTopic("加法").scale(0.8).next_to(title1, DOWN, buff=1, aligned_edge=LEFT)
        plus1 = TexMobject("{c}{_i}={a}{_i}+{b}{_i}", tex_to_color_map=t2c).move_to([-3.5, sub1_1.get_center()[1]-0.7, 0])
        O1_1 = TexMobject("O(n)").scale(0.85).next_to(sub1_1, RIGHT)
        self.play(Write(sub1_1))
        self.wait()
        self.play(Write(plus1))
        self.wait(2)
        self.play(FadeInFrom(O1_1, RIGHT))
        self.wait(2)
        sub1_2 = SubTopic("乘法").scale(0.8).next_to(sub1_1, DOWN, buff=1)
        mul1 = TexMobject("\\boldsymbol{c}", "=", "\\boldsymbol{a}", "\\otimes", "\\boldsymbol{b}").move_to([-3.5, sub1_2.get_center()[1]-0.7, 0])
        O1_2 = TexMobject("O(n^2)").scale(0.85).next_to(sub1_2, RIGHT)
        mul1[0].set_color(GREEN)
        mul1[2].set_color(GREEN)
        mul1[4].set_color(GREEN)
        self.play(Write(sub1_2))
        self.wait()
        self.play(Write(mul1))
        self.wait(2)
        self.play(FadeInFrom(O1_2, RIGHT))
        self.wait(2)
        sub1_3 = SubTopic("求值").scale(0.8).next_to(sub1_2, DOWN, buff=1)
        t2c2 = {
            "{A}": ORANGE,
            "{a}": GREEN,
            "{x}": RED,
            "{_n}": BLUE,
            "{_{n-1}}": BLUE,
            "{_{n-2}}": BLUE,
            "{_1}": BLUE,
            "{_0}": BLUE,
        }
        eva = TexMobject("{A}({x})=&(\\cdots(({a}{_n}{x}+{a}{_{n-1}}){x}+\\\\&{a}{_{n-2}}){x}+\\cdots+{a}{_1}){x}+{a}{_0}", tex_to_color_map=t2c2)
        eva.scale(0.8).move_to([-3.5, sub1_3.get_center()[1]-0.85, 0])
        O1_3 = TexMobject("O(n)").scale(0.85).next_to(sub1_3, RIGHT)
        self.play(Write(sub1_3))
        self.wait()
        self.play(Write(eva))
        self.wait(2)
        self.play(FadeInFrom(O1_3, RIGHT))
        self.wait(2)

    def right(self):
        title2 = Text("点值表示", font="Source Han Sans CN").set_color(BLUE).scale(0.57).move_to([1.5, 3.3, 0])
        self.play(Write(title2))
        t2c = {
            "{x}": RED,
            "{A}": ORANGE,
            "{B}": ORANGE,
            "{C}": ORANGE,
            "{_0}": BLUE,
            "{_1}": BLUE,
            "{_n}": BLUE,
            "{_i}": BLUE,
        }
        point = TexMobject("\\{", "({x}{_0}, {A}({x}{_0})), ({x}{_1}, {A}({x}{_1})),\\cdots ,({x}{_n}, {A}({x}{_n}))", "\\}", \
            tex_to_color_map=t2c).scale(0.7).next_to(title2, DOWN, aligned_edge=LEFT).shift(LEFT*0.2)
        self.play(Write(point))
        self.wait()

        sub2_1 = SubTopic("加法").scale(0.8).next_to(title2, DOWN, buff=1, aligned_edge=LEFT)
        plus2 = TexMobject("{C}({x}{_i})={A}({x}{_i})+{B}({x}{_i})", tex_to_color_map=t2c).move_to([3.5, sub2_1.get_center()[1]-0.7, 0])
        O2_1 = TexMobject("O(n)").scale(0.85).next_to(sub2_1, RIGHT)
        self.play(Write(sub2_1))
        self.wait()
        self.play(Write(plus2))
        self.wait(2)
        self.play(FadeInFrom(O2_1, RIGHT))
        self.wait(2)
        sub2_2 = SubTopic("乘法").scale(0.8).next_to(sub2_1, DOWN, buff=1)
        mul2 = TexMobject("{C}({x}{_i})={A}({x}{_i}){B}({x}{_i})", tex_to_color_map=t2c).move_to([3.5, sub2_2.get_center()[1]-0.7, 0])
        O2_2 = TexMobject("O(n)").scale(0.85).next_to(sub2_2, RIGHT)
        self.play(Write(sub2_2))
        self.wait()
        self.play(Write(mul2))
        self.wait(2)
        self.play(FadeInFrom(O2_2, RIGHT))
        self.wait(2)
        sub2_3 = SubTopic("插值").scale(0.8).next_to(sub2_2, DOWN, buff=1)
        t2c2 = {
            "{A}" : ORANGE,
            "{x}" : RED,
            "{_i}": BLUE
        }
        inter = TexMobject("{A}({x})=\\sum_{i=0}^n{A}({x}{_i})\\frac{\\prod_{j\\neq i}(x_{}-x_j)}{\\prod_{j\\neq i}(x_i-x_j)}", \
            tex_to_color_map=t2c2)
        inter.scale(0.8).move_to([3.5, sub2_3.get_center()[1]-0.87, 0])
        O2_3 = TexMobject("O(n^2)").scale(0.85).next_to(sub2_3, RIGHT)
        self.play(Write(sub2_3))
        self.wait()
        self.play(Write(inter))
        self.wait(2)
        self.play(FadeInFrom(O2_3, RIGHT))
        self.wait(2)



##------Time Line------##
# 19.12.05 have an idea
# 19.12.07 ~ 19.12.12 study FFT
# 19.12.13 ~ 19.12.17 write notes
# 19.12.18 create FFT.py
# 19.12.19 ~ 19.12.?? write split scene scripts
# 20.01.11 Finish VideoCover's subscript and some of the background images
# 20.01.13 write some of the background images
# 20.01.14 Finish VideoCover and FFTScene
# 20.01.16 Finish all Subtitles and two other scenes
# 20.01.17 Finish ComplexNumber Scene. Thanks @cigar666
# 20.01.18 ~ 20.01.23 homework
# 20.01.24 Finish Polynomial part1
# 20.01.25 Finish Polynomial part2 3 4. Thanks @有一种悲伤叫颓废 for part3