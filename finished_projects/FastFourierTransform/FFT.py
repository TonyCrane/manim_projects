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
        text = Text("互动", font='Source Han Serif CN', stroke_width=1.5).scale(0.7).rotate(PI / 4).next_to(square.get_edge_center(DOWN), buff=0)
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
        label_bi.add_updater(lambda m: m.next_to(dl_bi,(LEFT, RIGHT)[point.get_center()[0] < 0]))
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


class VideoFromMATH(Scene):
    def construct(self):
        icon1 = SVGMobject("video_icon").set_color(PINK).scale(0.5)
        av1   = TextMobject("av81286856")
        screen1 = ScreenRectangle(height=3)
        title1 = Text("复数能有多优美Ⅰ", font="Source Han Sans CN").scale(0.5)
        av1.next_to(icon1, RIGHT)
        screen1.next_to(VGroup(icon1, av1), DOWN)
        title1.next_to(screen1, DOWN)
        av81286856 = VGroup(icon1, av1, screen1, title1)
        av81286856.move_to([-3, 1, 0])

        icon2 = SVGMobject("video_icon").set_color(PINK).scale(0.5)
        av2   = TextMobject("av86056773")
        screen2 = ScreenRectangle(height=3)
        title2 = Text("复数能有多优美Ⅱ", font="Source Han Sans CN").scale(0.5)
        av2.next_to(icon2, RIGHT)
        screen2.next_to(VGroup(icon2, av2), DOWN)
        title2.next_to(screen2, DOWN)
        av86056773 = VGroup(icon2, av2, screen2, title2)
        av86056773.move_to([3, 1, 0])
        
        self.play(
            ShowCreation(av81286856[2]),
            ShowCreation(av86056773[2])
        )
        self.play(
            Write(av81286856[3]),
            Write(av86056773[3])
        )
        self.play(
            FadeIn(av81286856[0]),
            FadeIn(av86056773[0]),
            FadeIn(av81286856[1]),
            FadeIn(av86056773[1]),
        )
        self.wait(3)


class UnitRoot_part1(Scene): # Thanks @cigar666
    def construct(self):
        ## Create ComplexPlane ##
        cp_scale = 1.75
        cp = ComplexPlane().scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        ### about z^n ###
        color_dict = {'z': PINK, 'x': BLUE, 'y': YELLOW, 'i': RED, '\\cos': BLUE, '\\sin': YELLOW, '\\theta}': BLUE,
                      'r': PINK, 'e': GREEN, 'n': YELLOW, 'k': YELLOW, '\\omega': PINK, '\\pi': BLUE}
        complex_z = 0.9+0.6j
        vect_z = Arrow(cp.n2p(0), cp.n2p(complex_z), buff=0, color=ORANGE)
        dot_z = Dot(cp.n2p(complex_z), color=PINK)
        angle_z = Angle(cp.n2p(1), cp.n2p(0), cp.n2p(complex_z), radius=0.6, color=BLUE)

        ## 3 forms of complex num
        xy_form = TexMobject('z', '=', 'x', '+', 'y', 'i').set_color_by_tex_to_color_map(color_dict)
        cs_form = TexMobject('z', '=', 'r', '(', '\\cos{', '\\theta}', '+', 'i', '\\sin{', '\\theta}', ')').set_color_by_tex_to_color_map(color_dict)
        exp_form = TexMobject('z', '=', 'r', 'e^{', 'i', '\\theta}', color=WHITE).set_color_by_tex_to_color_map(color_dict).scale(1.2)
        exp_form[-1].set_color(BLUE)
        xy_form.next_to(dot_z, RIGHT * 0.6)
        cs_form.next_to(dot_z, RIGHT * 0.6)
        exp_form.next_to(dot_z, RIGHT * 0.6).shift(UP * 0.25)

        ## vgroup for z_i
        vect_group = VGroup(vect_z)
        dot_group = VGroup(dot_z)
        text_group = VGroup(exp_form)
        angle_group = VGroup(angle_z)
        line_group = VGroup(Line(cp.n2p(1), cp.n2p(complex_z), color=PINK))

        n = 10
        for i in range(n-1):
            zn_1 = complex_z ** (i+2-1)
            zn = complex_z ** (i+2)
            dot_i = Dot(cp.n2p(zn), color=PINK)
            vect_i = Arrow(cp.n2p(0), cp.n2p(zn), buff=0, color=ORANGE)
            text_i = TexMobject('z^{', '%d}' % (i+2), color=PINK).shift(cp.n2p(zn)/abs(zn) * (abs(zn) + 0.25))
            angle_i = Angle(cp.n2p(zn_1), cp.n2p(0), cp.n2p(zn), radius=0.6, color=BLUE)
            vect_group.add(vect_i)
            dot_group.add(dot_i)
            text_group.add(text_i)
            angle_group.add(angle_i)
            line_group.add(VGroup(Line(cp.n2p(zn_1), cp.n2p(zn), color=PINK)))

        ### conclusions from z^n =1 ###
        text_zn = TexMobject('z^', 'n', '=', 'r^', 'n', 'e^{', 'n', '\\theta', 'i}', '=', '1').set_color_by_tex_to_color_map(color_dict)
        text_zn[7].set_color(BLUE)
        text_zn.scale(1.2).to_corner(RIGHT * 3.25 + UP * 1.2)

        right_arrow = TexMobject('\\Rightarrow').next_to(text_zn, DOWN * 3.75).align_to(text_zn, LEFT)

        text_01 = TexMobject('r', '=', '1').set_color_by_tex_to_color_map(color_dict).next_to(right_arrow, RIGHT * 2.4).shift(UP * 0.5)
        text_02 = TexMobject('n', '\\theta', '=', '2', 'k', '\\pi').set_color_by_tex_to_color_map(color_dict).next_to(right_arrow, RIGHT * 2.4).shift(DOWN * 0.5)
        text_12 = VGroup(text_01, text_02)
        brace = Brace(text_12, LEFT)

        text_03 = TexMobject('\\therefore', '\\omega^', 'n', '=', '1', '\\text{的}', 'n', '\\text{个根为：}',)\
            .set_color_by_tex_to_color_map(color_dict).next_to(text_02, DOWN * 1.4).align_to(text_zn, LEFT)

        text_wi_01 = TexMobject('\\omega', '^k', '_n', '=', 'e^{', 'i', '{2', 'k', '\\pi', '\\over', 'n}}',
                              ).set_color_by_tex_to_color_map(color_dict)
        text_wi_01.next_to(text_03, DOWN * 1.5).align_to(text_zn, LEFT)
        text_wi_02 = TexMobject('=', '\\cos{', '2', 'k', '\\pi', '\\over', 'n}', '+', 'i', '\\sin{',
                             '2', 'k', '\\pi', '\\over', 'n}').set_color_by_tex_to_color_map(color_dict)
        text_wi_02.next_to(text_wi_01, DOWN * 1.5).align_to(text_zn, LEFT)
        text_wi_02[1:].scale(0.9)
        text_k = TexMobject('(', 'k', '=', '0', ',', '1', ',', '2', ',','\\cdots', ',', 'n-1', ')').set_color_by_tex_to_color_map(color_dict)
        text_k.scale(0.75).next_to(text_wi_02, DOWN * 1.5).align_to(text_zn, LEFT)

        ### display w_i in unit circle ###
        # moved to animation part 3 #

        ### animation part 1 ###

        self.play(ShowCreation(cp))
        self.wait(1)

        self.play(ShowCreation(vect_z))
        self.wait(0.5)
        self.play(ShowCreation(dot_z))
        self.play(Write(xy_form))
        self.wait(1)
        self.play(ReplacementTransform(xy_form, cs_form))
        self.wait(1)
        self.play(ReplacementTransform(cs_form, exp_form))
        self.wait()
        self.play(ShowCreation(angle_z))

        # self.add(vect_group, text_group, dot_group, angle_group, line_group)
        for i in range(1, n):
            self.play(ShowCreation(vect_group[i]), run_time=0.8)
            self.play(ShowCreation(dot_group[i]), run_time=0.4)
            self.play(Write(text_group[i]), run_time=0.6)
            self.wait(0.2)
            self.play(ShowCreation(angle_group[i]), run_time=0.6)
            self.wait(0.4)
        self.wait()
        for i in range(0, n):
            self.play(ShowCreation(line_group[i]), run_time=0.4)
            self.wait(0.1)
        self.wait()

        all_exist = VGroup(cp, vect_group, text_group, dot_group, angle_group, line_group)
        self.play(all_exist.shift, cp.n2p(-2), run_time=1.5)
        self.wait()

        ### part 2 ###
        text_bg = Polygon(cp.n2p(2.6+2.2j), cp.n2p(5.8+2.2j), cp.n2p(5.8-2.2j), cp.n2p(2.6-2.2j),
                          stroke_width=0, fill_color=BLACK, fill_opacity=0.75)
        self.play(FadeIn(text_bg), run_time=1.2)
        self.wait(0.5)
        self.play(TransformFromCopy(text_group, text_zn[0:9]), run_time=1.2)
        self.wait()
        self.play(Write(text_zn[9:11]))
        self.wait()
        self.play(Write(right_arrow))
        self.play(ShowCreation(brace))

        self.play(TransformFromCopy(text_zn[3:5], text_01))
        self.wait()

        self.play(TransformFromCopy(text_zn[6:8], text_02[0:2]))
        self.play(Write(text_02[2:6]))
        self.wait()

        self.play(Write(text_03), run_time=2)
        self.wait(0.5)
        self.play(Write(text_wi_01), run_time=2)
        self.wait()
        self.play(Write(text_wi_02), run_time=3)
        self.wait()
        self.play(Write(text_k), run_time=2)
        self.wait(2)

        ### part 3 ###
        unit_circle = Circle(radius=cp.n2p(1)[0], color=BLUE_B).move_to(cp.n2p(0))
        self.play(ShowCreation(unit_circle))
        self.wait(0.5)
        z_new = np.exp(1j * TAU/11)
        w_1 = TexMobject('\\omega', '_n', '=', 'e^{', 'i', '{2', '\\pi', '\\over', 'n}}',).scale(0.9)\
            .set_color_by_tex_to_color_map(color_dict).move_to(cp.n2p(0)).shift((cp.n2p(z_new)-cp.n2p(0))*1.2+RIGHT*1.2)
        w_1[1].set_color(PINK)
        dot_1 = Dot(cp.n2p(z_new), color=PINK)
        vect_1 = Arrow(cp.n2p(0), cp.n2p(z_new), buff=0, color=ORANGE)
        line_1 = Line(cp.n2p(1), cp.n2p(z_new), color=PINK)
        dot_0 = Dot(cp.n2p(1), color=PINK)
        vect_0 = Arrow(cp.n2p(0), cp.n2p(1), buff=0, color=ORANGE)
        w_0 = TexMobject('\\omega', '^0', '_n', color=PINK).scale(0.8).move_to(cp.n2p(1.2))
        self.play(ShowCreation(vect_0))
        self.play(ShowCreation(dot_0), Write(w_0))
        self.play(ReplacementTransform(vect_group[0], vect_1), run_time=0.3)
        self.play(ReplacementTransform(dot_group[0], dot_1), run_time=0.3)
        self.play(ReplacementTransform(text_group[0], w_1), run_time=0.3)
        self.play(ReplacementTransform(line_group[0], line_1), run_time=0.3)
        vect_new, dot_new, line_new, text_new = VGroup(vect_1), VGroup(dot_1), VGroup(line_1), VGroup(w_1)

        for i in range(1, n):
            zn_1 = z_new ** (i+1-1)
            zn = z_new ** (i+1)
            dot_i = Dot(cp.n2p(zn), color=PINK)
            vect_i = Arrow(cp.n2p(0), cp.n2p(zn), buff=0, color=ORANGE)
            text_i = TexMobject('\\omega^{', '%d}_n' % (i+1), color=PINK).scale(0.8).move_to(cp.n2p(0)).shift((cp.n2p(zn)-cp.n2p(0))/abs(zn) * (abs(zn) + 0.2))
            line_i = Line(cp.n2p(zn_1), cp.n2p(zn), color=PINK)
            angle_i = Angle(cp.n2p(zn_1), cp.n2p(0), cp.n2p(zn), radius=0.6, color=BLUE)
            vect_new.add(vect_i), dot_new.add(dot_i), line_new.add(line_i), text_new.add(text_i)
            # vect_group[i].become(vect_i)
            # self.wait(dt)
            self.play(ReplacementTransform(vect_group[i], vect_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(angle_group[i], angle_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(dot_group[i], dot_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(text_group[i], text_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(line_group[i], line_i), run_time=0.32-0.08*np.sqrt(i))

        angle_11 = Angle(cp.n2p(1), cp.n2p(0), cp.n2p(np.exp(-1j * TAU/11)), radius=0.6, color=BLUE)
        line_11 = Line(cp.n2p(np.exp(-1j * TAU/11)), cp.n2p(1), color=PINK)
        self.play(ShowCreation(angle_11))
        self.play(ShowCreation(line_11))
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(w_1))

        self.wait(5)


class UnitRoot_part2(Scene):
    def construct(self):
        t2c = {
            "\\omega": RED,
            "_{dn}": GOLD,
            "^{dk}": YELLOW,
            "^{2k}": YELLOW,
            "^k": YELLOW,
            "^i": BLUE_A,
            "_n": GOLD,
            "^n": BLUE_A,
            "^{\\frac{2\\pi}{dn}i}": BLUE_A,
            "^{\\frac{2\\pi}{n}i}": BLUE_A,
            "proof.": ORANGE,
            "^{\\frac{n}{2}}": YELLOW,
            "_2": GOLD,
            "^{k+\\frac{n}{2}}": YELLOW,
            "^2": BLUE_A,
            "_{\\frac{n}{2}}": GOLD,
        }
        title = Text("单位根 - 三个引理", font="Source Han Sans CN", t2c={"三个引理" : YELLOW, "单位根 - " : BLUE})
        title.scale(0.6).move_to([-4, 3.3, 0])
        self.play(Write(title))
        self.wait(2)
        sub1t = SubTopic("lemma.1 消去引理: ").scale(0.8).next_to(title, DOWN, aligned_edge=LEFT)
        sub1 = TexMobject("\\omega", "^{dk}", "_{dn}", "=", "\\omega", "^k", "_n")
        sub1.set_color_by_tex_to_color_map(t2c).next_to(sub1t, RIGHT)
        self.play(Write(sub1t))
        self.wait()
        self.play(Write(sub1))
        proof1 = TexMobject("proof.", "\\omega", "^{dk}", "_{dn}", "=", "(", "e", "^{\\frac{2\\pi}{dn}i}", ")", "^{dk}", "=", \
            "(", "e", "^{\\frac{2\\pi}{n}i}", ")", "^k", "=", "\\omega", "^k", "_n")
        proof1.set_color_by_tex_to_color_map(t2c).move_to(UP * (sub1.get_center()[1]-1))
        lemma11 = TexMobject("\\omega", "^{\\frac{n}{2}}", "_n", "=", "\\omega", "_2", "=", "-1")
        lemma11.set_color_by_tex_to_color_map(t2c).next_to(sub1, RIGHT, buff=2)
        self.wait()
        self.play(Write(proof1))
        self.wait()
        self.play(TransformFromCopy(proof1[2:], lemma11))
        self.wait(3)
        sub2t = SubTopic("lemma.2 折半引理: ").scale(0.8).next_to(sub1t, DOWN, buff=1.5, aligned_edge=LEFT)
        sub2 = TexMobject("(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "^2", "=", "(", "\\omega", "^k", "_n", ")", "^2", "=", \
            "\\omega", "^k", "_{\\frac{n}{2}}")
        sub2.set_color_by_tex_to_color_map(t2c).next_to(sub2t, RIGHT)
        self.play(Write(sub2t))
        self.wait()
        self.play(Write(sub2))
        proof2 = TexMobject("proof.", "\\omega", "^{k+\\frac{n}{2}}", "_n", "=", "\\omega", "^k", "_n", "\\omega", "^{\\frac{n}{2}}", \
            "_n", "=", "-", "\\omega", "^k", "_n", "\\ ,\\ ", "(", "\\omega", "^k", "_n", ")", "^2", "=", "\\omega", "^{2k}", "_n", "=", \
            "\\omega", "^k", "_{\\frac{n}{2}}")
        proof2.set_color_by_tex_to_color_map(t2c).move_to(UP * (sub2.get_center()[1]-1))
        self.wait()
        self.play(Write(proof2[:12]))
        self.wait()
        self.play(ShowCreationThenDestructionAround(lemma11))
        self.wait()
        self.play(Write(proof2[12:17]))
        self.wait()
        self.play(Write(proof2[17:]))
        self.wait(3)
        sub3t = SubTopic("lemma.3 求和引理: ").scale(0.8).next_to(sub2t, DOWN, buff=1.5, aligned_edge=LEFT)
        sub3 = TexMobject("\\sum\\nolimits", "^{n-1}", "_{i=0}", "(", "\\omega", "^k", "_n", ")", "^i", "=", "0")
        sub3.set_color_by_tex_to_color_map(t2c).next_to(sub3t, RIGHT)
        self.play(Write(sub3t))
        self.wait()
        self.play(Write(sub3))
        proof3 = TexMobject("proof.", "\\sum\\nolimits", "^{n-1}", "_{i=0}", "(", "\\omega", "^k", "_n", ")", "^i", "=", \
            "{(", "\\omega", "^k", "_n", ")", "^n", "-1", "\\over", "\\omega", "^k", "_n", "-1}", "=", "{(", "\\omega", "^n", "_n", ")", "^k", \
            "-1", "\\over", "\\omega", "^k", "_n", "-1}", "=", "{1", "^k", "-1", "\\over", "\\omega", "^k", "_n", "-1}", "=", "0")
        proof3.set_color_by_tex_to_color_map(t2c).move_to(UP * (sub3.get_center()[1]-1.2))
        self.wait()
        self.play(Write(proof3[:11]))
        self.wait()
        self.play(Write(proof3[11:23]))
        self.wait()
        self.play(Write(proof3[23:36]))
        self.wait()
        self.play(Write(proof3[36:45]))
        self.wait()
        self.play(FadeInFrom(proof3[45:], RIGHT))
        self.wait(5)
        self.play(FadeOut(VGroup(proof1, proof2, proof3, lemma11)), run_time=2)
        self.wait(3)


class TimeClock(Scene):
    def construct(self):
        num = TextMobject("5").scale(3).set_color(GRAY)
        self.add(num)
        self.wait(0.5)
        self.play(
            Transform(num, TextMobject("4").scale(3).set_color(GRAY)),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(
            Transform(num, TextMobject("3").scale(3).set_color(GRAY)),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(
            Transform(num, TextMobject("2").scale(3).set_color(GRAY)),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(
            Transform(num, TextMobject("1").scale(3).set_color(GRAY)),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(
            Transform(num, TextMobject("0").scale(3).set_color(GRAY)),
            run_time=0.5
        )
        self.wait(0.5)


class UnitRoot_part3(Scene):
    def construct(self):
        cp1 = ComplexPlane().scale(2)
        cp1.add_coordinates(0, 1, -1, 1j, -1j).shift(LEFT * 3.5)
        cp2 = ComplexPlane().scale(2)
        cp2.add_coordinates(0, 1, -1, 1j, -1j).shift(RIGHT * 3.5)
        group1 = VGroup(cp1)
        group2 = VGroup(cp2)
        self.play(ShowCreation(cp1, run_time=2.5))
        self.play(ShowCreation(cp2, run_time=2.5))
        self.wait(2)
        c1 = Circle(radius=2).move_to(cp1.n2p(0)).set_stroke(YELLOW, opacity=0.5)
        group1.add(c1)
        c2 = Circle(radius=2).move_to(cp2.n2p(0)).set_stroke(YELLOW, opacity=0.5)
        group2.add(c2)
        self.play(ShowCreation(c1), ShowCreation(c2))
        self.wait()
        w_10 = VGroup(
            *[
                VGroup(
                    Line(cp1.n2p(0), cp1.n2p(np.cos(i * 36 * PI / 180) + 1j * np.sin(i * 36 * PI / 180))).set_stroke(GREEN, opacity=0.5),
                    Dot(cp1.n2p(np.cos(i * 36 * PI / 180) + 1j * np.sin(i * 36 * PI / 180)), color=GREEN).set_fill(GREEN, 0.5),
                    TexMobject("\\omega", "^{%d}" % i, "_{10}").set_opacity(0.9).scale(0.7).next_to(cp1.n2p(np.cos(i * 36 * PI / 180) + 1j * np.sin(i * 36 * PI / 180)), LEFT)
                )
                for i in range(10)
            ]
        )
        for i in w_10:
            i[2][0].set_color(RED)
            i[2][1].set_color(YELLOW)
            i[2][2].set_color(GOLD)
        group1.add(w_10)
        w_5 = VGroup(
            *[
                VGroup(
                    Line(cp2.n2p(0), cp2.n2p(np.cos(i * 72 * PI / 180) + 1j * np.sin(i * 72 * PI / 180))).set_stroke(GREEN, opacity=0.5),
                    Dot(cp2.n2p(np.cos(i * 72 * PI / 180) + 1j * np.sin(i * 72 * PI / 180)), color=GREEN).set_fill(GREEN, 0.5),
                    TexMobject("\\omega", "^{%d}" % i, "_5").set_opacity(0.9).scale(0.7).next_to(cp2.n2p(np.cos(i * 72 * PI / 180) + 1j * np.sin(i * 72 * PI / 180)), RIGHT)
                )
                for i in range(5)
            ]
        )
        for i in w_5:
            i[2][0].set_color(RED)
            i[2][1].set_color(YELLOW)
            i[2][2].set_color(GOLD)
        group2.add(w_5)
        for i in w_10:
            self.play(ShowCreation(i[:2]), run_time=0.45)
            self.play(Write(i[2]), run_time=0.45)
            self.wait(0.1)
        self.wait()
        for i in w_5:
            self.play(ShowCreation(i[:2]), run_time=0.45)
            self.play(Write(i[2]), run_time=0.45)
            self.wait(0.1)
        self.wait()
        self.play(
            w_10[4][0].set_color, RED,
            w_10[4][1].set_color, RED,
            w_10[4][2].set_opacity, 1,
            w_5[2][0].set_color, RED,
            w_5[2][1].set_color, RED,
            w_5[2][2].set_opacity, 1,
            run_time=2
        )
        self.play(
            w_10[4][2].scale, 1.5,
            w_5[2][2].scale, 1.5
        )
        self.wait(2)
        self.play(
            group1.shift, RIGHT * 3.5,
            group2.shift, LEFT * 3.5,
            run_time=2.5
        )
        self.play(
            w_10[4][0:2].set_opacity, 1
        )
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(VGroup(w_10[4][2], w_5[2][2]))
        )
        self.wait(5)


class UnitRoot_part4(Scene):
    def construct(self):
        cp = ComplexPlane().scale(2)
        cp.add_coordinates(0, -1, -2, 1, 2, 1j, -1j, 2j, -2j)
        c = Circle(radius=2).set_color(YELLOW)
        self.play(ShowCreation(cp, run_time=3))
        self.wait()
        self.play(ShowCreation(c))
        self.wait()
        w_8 = VGroup(
            *[
                VGroup(
                    Line(cp.n2p(0), cp.n2p(np.cos(i * 45 * PI / 180) + 1j * np.sin(i * 45 * PI / 180))).set_stroke(GREEN, opacity=0.5),
                    Dot(cp.n2p(np.cos(i * 45 * PI / 180) + 1j * np.sin(i * 45 * PI / 180)), color=GREEN).set_fill(GREEN, 0.5),
                    TexMobject("\\omega", "^{%d}" % i, "_8").set_opacity(0.9).scale(0.7).next_to(cp.n2p(np.cos(i * 45 * PI / 180) + 1j * np.sin(i * 45 * PI / 180)), LEFT)
                )
                for i in range(8)
            ]
        )
        for i in w_8:
            i[2][0].set_color(RED)
            i[2][1].set_color(YELLOW)
            i[2][2].set_color(GOLD)
        for i in w_8:
            self.play(ShowCreation(i[:2]), run_time=0.45)
            self.play(Write(i[2]), run_time=0.45)
            self.wait(0.1)
        self.wait()
        self.play(
            w_8[1][0].set_opacity, 1,
            w_8[1][0].set_color, RED,
            w_8[1][1].set_opacity, 1,
            w_8[1][1].set_color, RED,
            w_8[1][2].set_opacity, 1,
            w_8[1][2].scale, 1.5,
            w_8[5][0].set_opacity, 1,
            w_8[5][0].set_color, RED,
            w_8[5][1].set_opacity, 1,
            w_8[5][1].set_color, RED,
            w_8[5][2].set_opacity, 1,
            w_8[5][2].scale, 1.5,
            run_time=1.5
        )
        self.play(FadeOut(w_8[2][2]))
        self.wait()
        t2c = {"\\omega": RED, "^1": YELLOW, "_8": GOLD, "^2": BLUE_A, "^5": YELLOW}
        w_8_1_2 = TexMobject("(", "\\omega", "^1", "_8", ")", "^2").set_color_by_tex_to_color_map(t2c).next_to(w_8[2][1], LEFT)
        w_8_5_2 = TexMobject("(", "\\omega", "^5", "_8", ")", "^2").set_color_by_tex_to_color_map(t2c).next_to(w_8[2][1], RIGHT)
        self.play(
            Rotating(w_8[1], radians=45 * PI / 180, about_point=ORIGIN),
            Rotating(w_8[5], radians=5 * 45 * PI / 180, about_point=ORIGIN),
            Transform(w_8[1][2], w_8_1_2),
            Transform(w_8[5][2], w_8_5_2),
            run_time=2
        )
        self.wait()
        w_4 = VGroup(
            TexMobject("\\omega", "^0", "_4").next_to(w_8[0][1], RIGHT),
            TexMobject("\\omega", "^1", "_4").next_to(w_8[2][1], UP),
            TexMobject("\\omega", "^2", "_4").next_to(w_8[4][1], RIGHT),
            TexMobject("\\omega", "^3", "_4").next_to(w_8[6][1], DOWN)
        )
        for i in w_4:
            i[0].set_color(PINK)
            i[1].set_color(BLUE)
            i[2].set_color(PINK)
        for i in w_4:
            self.play(Write(i), run_time=0.9)
            self.wait(0.1)
        self.wait()
        self.play(ShowCreationThenDestructionAround(VGroup(w_4[1], w_8[1][2], w_8[5][2])))
        self.wait(5)
        

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


class DFT(Scene):
    def construct(self):
        title = Text("离散傅里叶变换", font="Source Han Sans CN", t2c={"离散" : YELLOW,"傅里叶变换" : BLUE,})
        title.scale(0.6).move_to([-4.5, 3.3, 0])
        en_title = TextMobject("D", "iscrete ", "F", "ourier ", "T", "ransform").next_to(title, RIGHT)
        en_title[0].set_color(YELLOW)
        en_title[2].set_color(BLUE)
        en_title[4].set_color(BLUE)
        self.play(Write(title))
        self.wait()
        self.play(DrawBorderThenFill(en_title))
        self.wait()
        defi = VGroup(
            TexMobject("A", "(", "x", ")", "=", "\\sum", "^{n-1}", "_{i", "=", "0}", "a", "_i", "x", "^i"),
            TextMobject("在$\\omega_n^0, \\omega_n^1, \\cdots, \\omega_n^{n-1}$处的值$y_0, y_1, \\cdots, y_{n-1}$").scale(0.9)
        ).arrange_submobjects(RIGHT)
        defi[0][0].set_color(ORANGE)
        defi[0][2].set_color(RED)
        defi[0][7].set_color(BLUE)
        defi[0][10].set_color(GREEN)
        defi[0][11].set_color(BLUE)
        defi[0][12].set_color(RED)
        defi[0][13].set_color(BLUE)
        defi.move_to([0, title.get_center()[1]-1.2, 0])
        pos = defi[0].get_center()
        defi[0].move_to(ORIGIN)
        self.play(Write(defi[0]))
        self.wait()
        self.play(defi[0].move_to, pos, run_time=1.5)
        self.wait(0.2)
        self.play(Write(defi[1]))
        self.wait(2)
        dft = TexMobject("y_i=", "A", "(", "\\omega", "_n", "^i", ")", "=\\sum", "^{n-1}", "_{j", "=", "0}", "\\omega", "_n", "^{i", "j}", "a", "_j")
        dft[1].set_color(ORANGE)
        dft[3].set_color(RED)
        dft[12].set_color(RED)
        dft[4:6].set_color(GOLD)
        dft[13].set_color(GOLD)
        dft[15].set_color(GOLD)
        dft[9].set_color(BLUE)
        dft[14].set_color(BLUE)
        dft[17].set_color(BLUE)
        dft[16].set_color(GREEN)
        dft.next_to(defi, DOWN)
        pos2 = dft[:7].get_center()
        dft[:7].move_to([0, pos2[1], 0])
        self.play(Write(dft[:7]))
        self.wait()
        self.play(dft[:7].move_to, pos2, run_time=1.5)
        self.wait()
        self.play(Write(dft[7:]))
        self.wait(2)
        dft2 = VGroup(
            TexMobject("\\boldsymbol{y}=\\text{DFT}", "_n", "(", "\\boldsymbol{a}", ")"),
            TexMobject("\\boldsymbol{y}=", "\\mathcal{F}", "\\boldsymbol{a}")
        ).arrange_submobjects(RIGHT, buff=1).next_to(dft, DOWN, buff=0.8)
        dft2[0][1].set_color(GOLD)
        dft2[0][3].set_color(GREEN)
        dft2[1][1].set_color(YELLOW)
        dft2[1][2].set_color(GREEN)
        pos3 = dft2[0].get_center()
        dft2[0].move_to([0, pos3[1], 0])
        self.play(Write(dft2[0]))
        self.wait()
        self.play(dft2[0].move_to, pos3, run_time=1.5)
        self.wait()
        self.play(Write(dft2[1]))
        self.wait(3)
        self.play(
            dft.move_to, [-3.5, pos2[1], 0],
            dft2.move_to, [3.5, pos2[1], 0],
            run_time=2    
        )
        O1 = TexMobject("O(n^2)").next_to(en_title, RIGHT).set_color(GOLD)
        self.wait()
        self.play(FadeInFrom(O1, RIGHT))
        self.wait()
        title2 = Text("快速傅里叶变换", font="Source Han Sans CN", t2c={"快速" : YELLOW,"傅里叶变换" : BLUE,})
        title2.scale(0.6).move_to([-4.5, -1.5, 0])
        en_title2 = TextMobject("F", "ast ", "{\\tiny discrete} ", "F", "ourier ", "T", "ransform").next_to(title2, RIGHT)
        en_title2[0].set_color(YELLOW)
        en_title2[2].set_color(YELLOW)
        en_title2[3].set_color(BLUE)
        en_title2[5].set_color(BLUE)
        pos4 = en_title2[3:].get_center()
        en_title2[3:].next_to(en_title2[1], RIGHT, aligned_edge=DOWN)
        self.play(Write(title2))
        self.wait()
        self.play(DrawBorderThenFill(en_title2[:2]), DrawBorderThenFill(en_title2[3:]))
        self.wait()
        self.play(en_title2[3:].move_to, pos4)
        self.wait()
        self.play(TransformFromCopy(en_title[:2], en_title2[2]), run_time=1.5)
        self.wait(3)
        O2 = TexMobject("O(n\\log n)").next_to(en_title2, RIGHT).set_color(GOLD)
        self.play(TransformFromCopy(O1, O2), run_time=1.5)
        self.wait(3)


class FFT_part1(Scene):
    def construct(self):
        title2 = Text("快速傅里叶变换", font="Source Han Sans CN", t2c={"快速" : YELLOW,"傅里叶变换" : BLUE,})
        title2.scale(0.6).move_to([-4.5, -1.5, 0])
        old_title = Text("离散傅里叶变换", font="Source Han Sans CN", t2c={"离散" : YELLOW,"傅里叶变换" : BLUE,})
        old_title.scale(0.6).move_to([-4.5, 3.3, 0])
        en_title2 = TextMobject("F", "ast ", "{\\tiny discrete} ", "F", "ourier ", "T", "ransform").next_to(title2, RIGHT)
        en_title2[0].set_color(YELLOW)
        en_title2[2].set_color(YELLOW)
        en_title2[3].set_color(BLUE)
        en_title2[5].set_color(BLUE)
        O2 = TexMobject("O(n\\log n)").next_to(en_title2, RIGHT).set_color(GOLD)
        self.add(title2, en_title2, O2)
        self.play(FadeOut(VGroup(O2, en_title2[2])))
        en_title = TextMobject("F", "ast ", "F", "ourier ", "T", "ransform").next_to(old_title, RIGHT)
        en_title[0].set_color(YELLOW)
        en_title[2].set_color(BLUE)
        en_title[4].set_color(BLUE)
        self.play(
            title2.move_to, [-4.5, 3.3, 0],
            Transform(en_title2[0:2], en_title[0:2]),
            Transform(en_title2[3:], en_title[2:])
        )
        self.wait(2)
        title = title2

        t2c = {
            "A": ORANGE,
            "x": RED,
            "\\boldsymbol{a}": GREEN,
            "a": GREEN,
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_4": BLUE,
            "_5": BLUE,
            "_{n-1}": BLUE,
            "_{n-2}": BLUE,
            "\\rightarrow": WHITE,
            "^{[0]}": GOLD,
            "^{[1]}": GOLD,
            "^2": BLUE_A,
            "^{n-1}": BLUE_A,
            "^{\\frac{n}{2}-1}": BLUE_A
        }
        A = TexMobject("A", "(", "x", ")", "\\rightarrow", "\\boldsymbol{a}", "=[", "a", "_0", ",", "a", "_1", ",",\
            "a", "_2", ",", "\\cdots", ",", "a", "_{n-1}", "]^\\top")
        A.set_color_by_tex_to_color_map(t2c)
        A.move_to([0, title.get_center()[1]-0.8, 0])
        comment = Text("FFT的n应保证为2的幂", font="Source Han Serif CN").scale(0.2).set_color(GRAY).next_to(A, RIGHT, aligned_edge=DOWN)
        a0 = TexMobject("\\boldsymbol{a}", "^{[0]}", "=[", "a", "_0", ",", "a", "_2", ",", "\\cdots", ",", "a", "_{n-2}", "]^\\top")
        a0.set_color_by_tex_to_color_map(t2c)
        a0.next_to(A[5], DOWN, aligned_edge=LEFT)
        a1 = TexMobject("\\boldsymbol{a}", "^{[1]}", "=[", "a", "_1", ",", "a", "_3", ",", "\\cdots", ",", "a", "_{n-1}", "]^\\top")
        a1.set_color_by_tex_to_color_map(t2c)
        a1.next_to(a0, DOWN, aligned_edge=LEFT)
        eve = Text("偶", font="Source Han Serif CN").scale(0.5).set_color(GOLD).next_to(a0, LEFT)
        odd = Text("奇", font="Source Han Serif CN").scale(0.5).set_color(GOLD).next_to(a1, LEFT)
        arrow0 = ArcBetweenPoints(A[0:4].get_bottom()+DOWN*0.1, eve.get_left()+LEFT*0.1).add_tip(0.2)
        arrow1 = ArcBetweenPoints(A[0:4].get_bottom()+DOWN*0.1, odd.get_left()+LEFT*0.1).add_tip(0.2)
        A0 = TexMobject("\\rightarrow", "A", "^{[0]}", "(", "x", ")").set_color_by_tex_to_color_map(t2c).next_to(a0, RIGHT).set_opacity(0.8)
        A1 = TexMobject("\\rightarrow", "A", "^{[1]}", "(", "x", ")").set_color_by_tex_to_color_map(t2c).next_to(a1, RIGHT).set_opacity(0.8)
        self.play(Write(A[:5]))
        self.wait()
        self.play(Write(A[5:]))
        self.play(FadeInFromDown(comment))
        self.wait(2)
        self.play(
            ShowCreation(arrow0),
            ShowCreation(arrow1),
            Write(eve),
            Write(odd)
        )
        self.play(
            TransformFromCopy(A[5:], a0),
            TransformFromCopy(A[5:], a1),
            run_time=2.5
        )
        self.play(
            FadeInFrom(A0, LEFT),
            FadeInFrom(A1, LEFT),
        )
        self.wait(3)

        resA = TexMobject("A", "(", "x", ")=", "a", "_0", "+", "a", "_1", "x", "+", "a", "_2", "x", "^2", "+", "\\cdots",\
            "+", "a", "_{n-1}", "x", "^{n-1}").set_color_by_tex_to_color_map(t2c).move_to([0, -0.5, 0])
        resA0 = TexMobject("A", "^{[0]}", "(", "x", ")=", "a", "_0", "+", "a", "_2", "x", "+", "a", "_4", "x", "^2", "+", "\\cdots",\
            "+", "a", "_{n-2}", "x", "^{\\frac{n}{2}-1}").set_color_by_tex_to_color_map(t2c).scale(0.8).next_to(resA[2], DOWN, aligned_edge=LEFT)
        resA1 = TexMobject("A", "^{[1]}", "(", "x", ")=", "a", "_1", "+", "a", "_3", "x", "+", "a", "_5", "x", "^2", "+", "\\cdots",\
            "+", "a", "_{n-1}", "x", "^{\\frac{n}{2}-1}").set_color_by_tex_to_color_map(t2c).scale(0.8).next_to(resA0, DOWN)
        self.play(Write(resA))
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(a0),
            ShowCreationThenDestructionAround(resA),
        )
        self.play(
            FadeIn(resA0)
        )
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(a1),
            ShowCreationThenDestructionAround(resA),
        )
        self.play(
            FadeIn(resA1)
        )
        self.wait(2)


class FFT_part2(Scene):
    def get_old(self):
        t2c = {
            "A": ORANGE,
            "x": RED,
            "\\boldsymbol{a}": GREEN,
            "a": GREEN,
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_4": BLUE,
            "_5": BLUE,
            "_{n-1}": BLUE,
            "_{n-2}": BLUE,
            "\\rightarrow": WHITE,
            "^{[0]}": GOLD,
            "^{[1]}": GOLD,
            "^2": BLUE_A,
            "^{n-1}": BLUE_A,
            "^{\\frac{n}{2}-1}": BLUE_A
        }
        old_title = Text("离散傅里叶变换", font="Source Han Sans CN", t2c={"离散" : YELLOW,"傅里叶变换" : BLUE,})
        old_title.scale(0.6).move_to([-4.5, 3.3, 0])
        title2 = Text("快速傅里叶变换", font="Source Han Sans CN", t2c={"快速" : YELLOW,"傅里叶变换" : BLUE,})
        title2.scale(0.6).move_to([-4.5, 3.3, 0])
        title = title2
        en_title = TextMobject("F", "ast ", "F", "ourier ", "T", "ransform").next_to(old_title, RIGHT)
        en_title[0].set_color(YELLOW)
        en_title[2].set_color(BLUE)
        en_title[4].set_color(BLUE)
        A = TexMobject("A", "(", "x", ")", "\\rightarrow", "\\boldsymbol{a}", "=[", "a", "_0", ",", "a", "_1", ",",\
            "a", "_2", ",", "\\cdots", ",", "a", "_{n-1}", "]^\\top")
        A.set_color_by_tex_to_color_map(t2c)
        A.move_to([0, title.get_center()[1]-0.8, 0])
        comment = Text("FFT的n应保证为2的幂", font="Source Han Serif CN").scale(0.2).set_color(GRAY).next_to(A, RIGHT, aligned_edge=DOWN)
        a0 = TexMobject("\\boldsymbol{a}", "^{[0]}", "=[", "a", "_0", ",", "a", "_2", ",", "\\cdots", ",", "a", "_{n-2}", "]^\\top")
        a0.set_color_by_tex_to_color_map(t2c)
        a0.next_to(A[5], DOWN, aligned_edge=LEFT)
        a1 = TexMobject("\\boldsymbol{a}", "^{[1]}", "=[", "a", "_1", ",", "a", "_3", ",", "\\cdots", ",", "a", "_{n-1}", "]^\\top")
        a1.set_color_by_tex_to_color_map(t2c)
        a1.next_to(a0, DOWN, aligned_edge=LEFT)
        eve = Text("偶", font="Source Han Serif CN").scale(0.5).set_color(GOLD).next_to(a0, LEFT)
        odd = Text("奇", font="Source Han Serif CN").scale(0.5).set_color(GOLD).next_to(a1, LEFT)
        arrow0 = ArcBetweenPoints(A[0:4].get_bottom()+DOWN*0.1, eve.get_left()+LEFT*0.1).add_tip(0.2)
        arrow1 = ArcBetweenPoints(A[0:4].get_bottom()+DOWN*0.1, odd.get_left()+LEFT*0.1).add_tip(0.2)
        A0 = TexMobject("\\rightarrow", "A", "^{[0]}", "(", "x", ")").set_color_by_tex_to_color_map(t2c).next_to(a0, RIGHT).set_opacity(0.8)
        A1 = TexMobject("\\rightarrow", "A", "^{[1]}", "(", "x", ")").set_color_by_tex_to_color_map(t2c).next_to(a1, RIGHT).set_opacity(0.8)
        return VGroup(
            title2, en_title, A, A0, A1, a0, a1, comment, arrow0, arrow1, eve, odd
        )

    def construct(self):
        t2c = {
            "A": ORANGE,
            "x": RED,
            "\\boldsymbol{a}": GREEN,
            "a": GREEN,
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_4": BLUE,
            "_5": BLUE,
            "_{n-1}": BLUE,
            "_{n-2}": BLUE,
            "\\rightarrow": WHITE,
            "^{[0]}": GOLD,
            "^{[1]}": GOLD,
            "^2": BLUE_A,
            "^3": BLUE_A,
            "^4": BLUE_A,
            "^5": BLUE_A,
            "^{n-1}": BLUE_A,
            "^{\\frac{n}{2}-1}": BLUE_A,
            "\\omega": RED,
            "_n": GOLD,
            "^k": BLUE_A,
            "^{k+\\frac{n}{2}}": BLUE_A,
            "_{\\frac{n}{2}}": GOLD,
        }
        old = self.get_old()
        resA = TexMobject("A", "(", "x", ")=", "a", "_0", "+", "a", "_1", "x", "+", "a", "_2", "x", "^2", "+", "\\cdots",\
            "+", "a", "_{n-1}", "x", "^{n-1}").set_color_by_tex_to_color_map(t2c).move_to([0, -0.5, 0])
        resA0 = TexMobject("A", "^{[0]}", "(", "x", ")=", "a", "_0", "+", "a", "_2", "x", "+", "a", "_4", "x", "^2", "+", "\\cdots",\
            "+", "a", "_{n-2}", "x", "^{\\frac{n}{2}-1}").set_color_by_tex_to_color_map(t2c).scale(0.8).next_to(resA[2], DOWN, aligned_edge=LEFT)
        resA1 = TexMobject("A", "^{[1]}", "(", "x", ")=", "a", "_1", "+", "a", "_3", "x", "+", "a", "_5", "x", "^2", "+", "\\cdots",\
            "+", "a", "_{n-1}", "x", "^{\\frac{n}{2}-1}").set_color_by_tex_to_color_map(t2c).scale(0.8).next_to(resA0, DOWN)
        self.add(resA, resA0, resA1, old)
        self.play(
            old.shift, UP * 3.7,
            resA.shift, UP * 3.7,
            resA0.shift, UP * 3.2,
            resA1.shift, UP * 3.1,
            run_time=2.5
        )  
        self.wait(3)
        resA0_ = TexMobject("A", "^{[0]}", "(", "x", "^2", ")=", "a", "_0", "+", "a", "_2", "x", "^2", "+", "a", "_4", "x", "^4", "+", "\\cdots",\
            "+", "a", "_{n-2}", "x", "^{n-2}").set_color_by_tex_to_color_map(t2c).scale(0.8).move_to(resA0)
        resA1_ = TexMobject("A", "^{[1]}", "(", "x", "^2", ")=", "a", "_1", "+", "a", "_3", "x", "^2", "+", "a", "_5", "x", "^4", "+", "\\cdots",\
            "+", "a", "_{n-1}", "x", "^{n-2}").set_color_by_tex_to_color_map(t2c).scale(0.8).move_to(resA1)
        self.play(
            ReplacementTransform(resA0[:3],    resA0_[:3]),
            ReplacementTransform(resA0[3],     resA0_[3:5]),
            ReplacementTransform(resA0[4:10],  resA0_[5:11]),
            ReplacementTransform(resA0[10],    resA0_[11:13]),
            ReplacementTransform(resA0[11:14], resA0_[13:16]),
            ReplacementTransform(resA0[14:16], resA0_[16:18]),
            ReplacementTransform(resA0[16:21], resA0_[18:23]),
            ReplacementTransform(resA0[21:],   resA0_[23:]),
            run_time=2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(resA1[:3],    resA1_[:3]),
            ReplacementTransform(resA1[3],     resA1_[3:5]),
            ReplacementTransform(resA1[4:10],  resA1_[5:11]),
            ReplacementTransform(resA1[10],    resA1_[11:13]),
            ReplacementTransform(resA1[11:14], resA1_[13:16]),
            ReplacementTransform(resA1[14:16], resA1_[16:18]),
            ReplacementTransform(resA1[16:21], resA1_[18:23]),
            ReplacementTransform(resA1[21:],   resA1_[23:]),
            run_time=2
        )
        self.wait(3)
        resA1__ = TexMobject("x", "A", "^{[1]}", "(", "x", "^2", ")=", "a", "_1", "x", "+", "a", "_3", "x", "^3", "+", "a", "_5", "x", "^5", "+", "\\cdots",\
            "+", "a", "_{n-1}", "x", "^{n-1}").set_color_by_tex_to_color_map(t2c).scale(0.8).move_to(resA1_)
        self.play(Write(resA1__[0]))
        self.play(ScaleInPlace(resA1__[0], 2.5, rate_func=wiggle))
        self.wait()
        self.play(
            Transform(resA1_[:8], resA1__[1:9]),
            FadeIn(resA1__[9]),
            Transform(resA1_[8:11], resA1__[10:13]),
            Transform(resA1_[11:13], resA1__[13:15]),
            Transform(resA1_[13:16], resA1__[15:18]),
            Transform(resA1_[16:18], resA1__[18:20]),
            Transform(resA1_[18:23], resA1__[20:25]),
            Transform(resA1_[23:], resA1__[25:]),
            run_time=2
        )
        self.wait(3)
        self.play(
            ShowCreationThenDestructionAround(resA[4:6]),
            ShowCreationThenDestructionAround(resA0_[6:8])
        )
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(resA[7:10]),
            ShowCreationThenDestructionAround(resA1__[7:10])
        )
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(resA[11:15]),
            ShowCreationThenDestructionAround(resA0_[9:13])
        )
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(resA[18:]),
            ShowCreationThenDestructionAround(resA1__[23:])
        )
        self.wait(2)
        res = TexMobject("A", "(", "x", ")", "=", "A", "^{[0]}", "(", "x", "^2", ")", "+",\
            "x", "A", "^{[1]}", "(", "x", "^2", ")").set_color_by_tex_to_color_map(t2c)
        res.next_to(resA1__, DOWN, buff=0.8)
        self.play(
            TransformFromCopy(resA[:4], res[:4]),
            TransformFromCopy(resA0_[:6], res[5:11]),
            TransformFromCopy(resA1__[:7], res[12:]),
            run_time=2
        )
        self.play(ShowCreationThenDestructionAround(res))
        self.wait()
        self.play(
            FadeIn(res[4]),
            FadeIn(res[11]),
        )
        self.wait(2)
        A1 = TexMobject("A", "(", "\\omega", "^k", "_n", ")", "=", "A", "^{[0]}", "(", "(", "\\omega", "^k", "_n", ")", "^2", ")", "+",\
            "\\omega", "^k", "_n", "A", "^{[1]}", "(", "(", "\\omega", "^k", "_n", ")", "^2", ")").set_color_by_tex_to_color_map(t2c)
        A1.next_to(res, DOWN)
        A2 = TexMobject("A", "(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "=", "A", "^{[0]}", "(", "(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "^2", ")", "+",\
            "\\omega", "^{k+\\frac{n}{2}}", "_n", "A", "^{[1]}", "(", "(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "^2", ")").set_color_by_tex_to_color_map(t2c)
        A2.next_to(A1, DOWN)
        A1.next_to(A2, UP, aligned_edge=LEFT)
        brace = Brace(VGroup(A1, A2), LEFT)
        self.play(ShowCreation(brace))
        self.play(Write(A1))
        self.wait()
        self.play(Write(A2))
        self.wait(3)

    
class FFT_part3(Scene):
    def construct(self):
        t2c = {
            "A": ORANGE,
            "x": RED,
            "\\boldsymbol{a}": GREEN,
            "a": GREEN,
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_4": BLUE,
            "_5": BLUE,
            "_{n-1}": BLUE,
            "_{n-2}": BLUE,
            "\\rightarrow": WHITE,
            "^{[0]}": GOLD,
            "^{[1]}": GOLD,
            "^2": BLUE_A,
            "^3": BLUE_A,
            "^4": BLUE_A,
            "^5": BLUE_A,
            "^{n-1}": BLUE_A,
            "^{\\frac{n}{2}-1}": BLUE_A,
            "\\omega": RED,
            "_n": GOLD,
            "^k": BLUE_A,
            "^{k+\\frac{n}{2}}": BLUE_A,
            "_{\\frac{n}{2}}": GOLD,
            "\\text{DFT}": WHITE
        }
        resA = TexMobject("A", "(", "x", ")=", "a", "_0", "+", "a", "_1", "x", "+", "a", "_2", "x", "^2", "+", "\\cdots",\
            "+", "a", "_{n-1}", "x", "^{n-1}").set_color_by_tex_to_color_map(t2c).move_to([0, -0.5, 0])
        resA0 = TexMobject("A", "^{[0]}", "(", "x", "^2", ")=", "a", "_0", "+", "a", "_2", "x", "^2", "+", "a", "_4", "x", "^4", "+", "\\cdots",\
            "+", "a", "_{n-2}", "x", "^{n-2}").set_color_by_tex_to_color_map(t2c).scale(0.8).next_to(resA[2], DOWN, aligned_edge=LEFT)
        resA1 = TexMobject("x", "A", "^{[1]}", "(", "x", "^2", ")=", "a", "_1", "x", "+", "a", "_3", "x", "^3", "+", "a", "_5", "x", "^5", "+", "\\cdots",\
            "+", "a", "_{n-1}", "x", "^{n-1}").set_color_by_tex_to_color_map(t2c).scale(0.8).next_to(resA0, DOWN)
        resA.shift(UP * 3.7)
        resA0.shift(UP * 3.2)
        resA1.shift(UP * 3.1)
        old = VGroup(resA, resA0, resA1)
        res = TexMobject("A", "(", "x", ")", "=", "A", "^{[0]}", "(", "x", "^2", ")", "+",\
            "x", "A", "^{[1]}", "(", "x", "^2", ")").set_color_by_tex_to_color_map(t2c)
        res.next_to(resA1, DOWN, buff=0.8)
        A1 = TexMobject("A", "(", "\\omega", "^k", "_n", ")", "=", "A", "^{[0]}", "(", "(", "\\omega", "^k", "_n", ")", "^2", ")", "+",\
            "\\omega", "^k", "_n", "A", "^{[1]}", "(", "(", "\\omega", "^k", "_n", ")", "^2", ")").set_color_by_tex_to_color_map(t2c)
        A1.next_to(res, DOWN)
        A2 = TexMobject("A", "(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "=", "A", "^{[0]}", "(", "(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "^2", ")", "+",\
            "\\omega", "^{k+\\frac{n}{2}}", "_n", "A", "^{[1]}", "(", "(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "^2", ")").set_color_by_tex_to_color_map(t2c)
        A2.next_to(A1, DOWN)
        A1.next_to(A2, UP, aligned_edge=LEFT)
        brace = Brace(VGroup(A1, A2), LEFT)

        self.add(old, res, A1, A2, brace)
        self.play(
            old.shift, UP * 3.7,
            res.shift, UP * 3.5,
            A1.shift, UP * 3.5,
            A2.shift, UP * 3.5,
            brace.shift, UP * 3.5
        )
        self.wait(2)
        lemma = TexMobject("(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "^2", "=", "(", "\\omega", "^k", "_n", ")", "^2", "=", \
            "\\omega", "^k", "_{\\frac{n}{2}}").set_color_by_tex_to_color_map(t2c)
        A1_ = TexMobject("A", "(", "\\omega", "^k", "_n", ")", "=", "A", "^{[0]}", "(", "\\omega", "^k", "_{\\frac{n}{2}}", ")", "+",\
            "\\omega", "^k", "_n", "A", "^{[1]}", "(", "\\omega", "^k", "_{\\frac{n}{2}}", ")").set_color_by_tex_to_color_map(t2c)
        A2_ = TexMobject("A", "(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "=", "A", "^{[0]}", "(", "\\omega", "^k", "_{\\frac{n}{2}}", ")", "+",\
            "\\omega", "^{k+\\frac{n}{2}}", "_n", "A", "^{[1]}", "(", "\\omega", "^k", "_{\\frac{n}{2}}", ")").set_color_by_tex_to_color_map(t2c)
        A1_.move_to(A1, aligned_edge=LEFT)
        A2_.move_to(A2, aligned_edge=LEFT)
        
        self.play(FadeIn(lemma))
        self.play(ShowCreationThenDestructionAround(lemma))
        self.wait()
        self.play(
            ReplacementTransform(A1[:10], A1_[:10]),
            ReplacementTransform(A1[10:16], A1_[10:13]),
            ReplacementTransform(A1[16:24], A1_[13:21]),
            ReplacementTransform(A1[24:30], A1_[21:24]),
            ReplacementTransform(A1[-1:], A1_[-1:]),
            run_time=2
        )
        self.wait()
        self.play(
            ReplacementTransform(A2[:10], A2_[:10]),
            ReplacementTransform(A2[10:16], A2_[10:13]),
            ReplacementTransform(A2[16:24], A2_[13:21]),
            ReplacementTransform(A2[24:30], A2_[21:24]),
            ReplacementTransform(A2[-1:], A2_[-1:]),
            run_time=2
        )
        lemma2 = TexMobject("\\omega", "^{k+\\frac{n}{2}}", "_n", "=", "-", "\\omega", "^k", "_n")
        lemma2.set_color_by_tex_to_color_map(t2c)
        self.play(ReplacementTransform(lemma, lemma2))
        self.play(ShowCreationThenDestructionAround(lemma2))
        self.wait()
        A2__ = TexMobject("A", "(", "\\omega", "^{k+\\frac{n}{2}}", "_n", ")", "=", "A", "^{[0]}", "(", "\\omega", "^k", "_{\\frac{n}{2}}", ")", "-",\
            "\\omega", "^k", "_n", "A", "^{[1]}", "(", "\\omega", "^k", "_{\\frac{n}{2}}", ")").set_color_by_tex_to_color_map(t2c)
        A2__.move_to(A2_, aligned_edge=LEFT)
        
        self.play(
            ReplacementTransform(A2_[:14], A2__[:14]),
            ReplacementTransform(A2_[14:18], A2__[14:18]),
            ReplacementTransform(A2_[18:], A2__[18:]),
            run_time=2
        )
        self.play(
            A1_.shift, [A2__[6].get_center()[0], A1_[6].get_center()[1], 0] - A1_[6].get_center()
        )
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(VGroup(A1_[7:14], A2__[7:14])),
            ShowCreationThenDestructionAround(VGroup(A1_[18:], A2__[18:]))
        )
        self.wait()
        self.play(FadeOut(lemma2))
        self.wait(2)
        old = TexMobject("\\text{DFT}", "_n", "(", "\\boldsymbol{a}", ")").set_color_by_tex_to_color_map(t2c)
        pre = VGroup(
            TexMobject("\\text{DFT}", "_{\\frac{n}{2}}", "(", "\\boldsymbol{a}", "^{[0]}", ")").set_color_by_tex_to_color_map(t2c),
            TexMobject("\\text{DFT}", "_{\\frac{n}{2}}", "(", "\\boldsymbol{a}", "^{[1]}", ")").set_color_by_tex_to_color_map(t2c),
        ).arrange_submobjects(RIGHT, buff=2).next_to(old, DOWN)
        br = Brace(pre, UP)
        old.shift(UP*0.5)
        self.play(Write(old))
        self.wait()
        self.play(ShowCreation(br), FadeInFrom(pre, UP))
        self.wait(3)
        O = TexMobject("T(n)=2T(\\frac{n}{2})+O(n)", "=", "O(n\\log n)", "<O(n^2)").next_to(pre, DOWN)
        self.play(Write(O[0]))
        self.wait()
        self.play(FadeInFrom(O[1:3], RIGHT))
        self.play(
            ShowCreationThenDestructionAround(O[2]),
            O[2].set_color, YELLOW
        )
        self.wait()
        self.play(FadeInFrom(O[3], RIGHT))
        self.wait(3)
        

class FFT_Code(Scene):
    def construct(self):
        t2c = {
            "\\boldsymbol{a}": GREEN,
            "lim": GOLD,
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_{n-1}": BLUE,
            "_{n-2}": BLUE,
            "a": GREEN,
            "_{k}": BLUE,
            "k": BLUE,
            "_{k+\\frac{n}{2}}": BLUE,
            "^{[0]}": GOLD,
            "^{[1]}": GOLD,
            "\\omega": RED,
            "_n": GOLD,
            "^{\\frac{2\\pi}{n}}": BLUE_A,
            "2\\pi/n": BLUE_A,
            "{i}": BLUE_E,
            "n/2-1": GOLD,
        }
        nums = VGroup(
            *[
                Text(str(i), font="Consolas").scale(0.45).set_color(GRAY)
                for i in range(1, 12)
            ]
        ).arrange_submobjects(DOWN, aligned_edge=RIGHT, buff=0.3).shift(LEFT*5)
        title = TexMobject("\\text{FFT}", "(", "\\boldsymbol{a}", ",\\ ", "lim", ")")
        title.set_color_by_tex_to_color_map(t2c).scale(0.8)
        title.next_to(nums, UP, aligned_edge=LEFT)
        code = VGroup()
        line1 = TexMobject("\\textbf{if}\\ \\ ", "lim", "==", "1", "\\ \\ \\ ", "\\textbf{return}")
        line1.scale(0.75).next_to(nums[0], RIGHT).set_color_by_tex_to_color_map(t2c)
        code.add(line1)
        line2 = TexMobject("\\boldsymbol{a}", "^{[0]}", "=", "(", "a", "_0", ", ", "a", "_2", ", ", "\\cdots", ", ", "a", "_{n-2}", ")")
        line2.scale(0.75).next_to(nums[1], RIGHT).set_color_by_tex_to_color_map(t2c)
        code.add(line2)
        line3 = TexMobject("\\boldsymbol{a}", "^{[1]}", "=", "(", "a", "_1", ", ", "a", "_3", ", ", "\\cdots", ", ", "a", "_{n-1}", ")")
        line3.scale(0.75).next_to(nums[2], RIGHT).set_color_by_tex_to_color_map(t2c)
        code.add(line3)
        line4 = TexMobject("\\text{FFT}", "(", "\\boldsymbol{a}", "^{[0]}", ",\\ ", "lim", ">>", "1", ")")
        line4.scale(0.75).next_to(nums[3], RIGHT).set_color_by_tex_to_color_map(t2c)
        code.add(line4)
        line5 = TexMobject("\\text{FFT}", "(", "\\boldsymbol{a}", "^{[1]}", ",\\ ", "lim", ">>", "1", ")")
        line5.scale(0.75).next_to(nums[4], RIGHT).set_color_by_tex_to_color_map(t2c)
        code.add(line5)
        line6 = TexMobject("\\omega", "_n", "=", "e", "^{\\frac{2\\pi}{n}", "i}", "=", "\\cos", "(", "2\\pi/n", ")", "+",\
            "{i}", "\\sin", "(", "2\\pi/n", ")")
        line6.scale(0.75).next_to(nums[5], RIGHT).set_color_by_tex_to_color_map(t2c)
        line6[4].set_color(BLUE_A); line6[5].set_color(BLUE_E)
        code.add(line6)
        line7 = TexMobject("\\omega", "=", "1")
        line7.scale(0.75).next_to(nums[6], RIGHT).set_color_by_tex_to_color_map(t2c)
        code.add(line7)
        line8 = TexMobject("\\textbf{for}\\ \\ ", "k", "=", "0", "\\ .\\ .\\ ", "n/2-1")
        line8.scale(0.75).next_to(nums[7], RIGHT).set_color_by_tex_to_color_map(t2c)
        code.add(line8)
        line9 = TexMobject("a", "_k", "=", "a", "^{[0]}", "_k", "+", "\\omega", "a", "^{[1]}", "_k")
        line9.scale(0.75).next_to(nums[8], RIGHT, buff=1).set_color_by_tex_to_color_map(t2c)
        code.add(line9)
        line10 = TexMobject("a", "_{k+\\frac{n}{2}}", "=", "a", "^{[0]}", "_k", "-", "\\omega", "a", "^{[1]}", "_k")
        line10.scale(0.75).next_to(nums[9], RIGHT, buff=1).set_color_by_tex_to_color_map(t2c)
        code.add(line10)
        line11 = TexMobject("\\omega", "=", "\\omega", "\\omega", "_n")
        line11.scale(0.75).next_to(nums[10], RIGHT, buff=1).set_color_by_tex_to_color_map(t2c)
        code.add(line11)
        
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeInFrom(nums[0], LEFT),)
        self.play(Write(code[0]))
        self.wait(2)
        self.play(FadeInFrom(nums[1:3], LEFT))
        self.play(Write(code[1:3]))
        self.wait(2)
        self.play(FadeInFrom(nums[3:5], LEFT))
        self.play(Write(code[3:5]))
        self.wait(2)
        self.play(FadeInFrom(nums[5], LEFT))
        self.play(Write(code[5]))
        self.wait(2)
        self.play(FadeInFrom(nums[6], LEFT))
        self.play(Write(code[6]))
        self.wait(2)
        self.play(FadeInFrom(nums[7:], LEFT))
        self.play(Write(code[7]))
        self.wait()
        self.play(Write(code[10]))
        self.wait(2)
        self.play(Write(code[8:10]))
        self.wait(3)
        sq = Rectangle(height=10, width=20).set_fill(BLACK, 1)
        self.add(sq)
        self.wait(3)
        self.remove(sq)
        self.wait(2)
        q = VGroup()
        q.add(SurroundingRectangle(VGroup(nums[0], code[0])))
        q.add(SurroundingRectangle(VGroup(nums[1:3], code[1:3])))
        q.add(SurroundingRectangle(VGroup(nums[3:5], code[3:5])))
        q.add(SurroundingRectangle(VGroup(nums[5:7], code[5:7])))
        q.add(SurroundingRectangle(VGroup(nums[7:], code[7:])))
        for m in q:
            self.play(ShowCreation(m))
            self.play(ScaleInPlace(m, 1.2, rate_func=wiggle))
            self.wait(2)
            self.play(FadeOut(m))
            self.wait(2)
        self.wait()


class FFT_improve_part1(Scene):
    def construct(self):
        t2c = {
            "\\boldsymbol{a}": GREEN,
            "lim": GOLD,
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_{n-1}": BLUE,
            "_{n-2}": BLUE,
            "a": GREEN,
            "_{k}": BLUE,
            "k": BLUE,
            "_{k+\\frac{n}{2}}": BLUE,
            "^{[0]}": GOLD,
            "^{[1]}": GOLD,
            "\\omega": RED,
            "_n": GOLD,
            "^{\\frac{2\\pi}{n}}": BLUE_A,
            "2\\pi/n": BLUE_A,
            "{i}": BLUE_E,
            "n/2-1": GOLD,
        }
        title = Text("高效实现FFT", font="Source Han Sans CN", t2c={"高效": YELLOW, "实现FFT": BLUE})
        title.scale(0.6).move_to([-4.5, 3.3, 0])
        sub = SubTopic("蝴蝶操作").scale(0.8).next_to(title, DOWN, aligned_edge=LEFT)
        text = VGroup(
            Text("公用子表达式", font="Source Han Serif CN").set_color(ORANGE).scale(0.5),
            TexMobject("\\omega", "a", "^{[1]}", "_k").set_color_by_tex_to_color_map(t2c)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([3.5, 1, 0])
        change = TexMobject("t", "=", "\\omega", "a", "^{[1]}", "_k").set_color_by_tex_to_color_map(t2c)
        change[0].set_color(BLUE)
        change.next_to(text, DOWN)
        change1 = TexMobject("a", "_k", "=", "a", "^{[0]}", "_k", "+", "t")
        change1.set_color_by_tex_to_color_map(t2c).next_to(change, DOWN)
        change1[-1].set_color(BLUE)
        change2 = TexMobject("a", "_{k+\\frac{n}{2}}", "=", "a", "^{[0]}", "_k", "-", "t")
        change2.set_color_by_tex_to_color_map(t2c).next_to(change1, DOWN)
        change2[-1].set_color(BLUE)
        
        self.play(Write(title))
        self.wait()
        self.play(Write(sub))
        self.wait(3)
        self.play(FadeInFrom(text, DOWN))
        self.wait()
        self.play(Write(change))
        self.wait()
        self.play(FadeIn(change1), FadeIn(change2))
        self.wait(2)  


class FFT_improve_part2(Scene):
    def construct(self):
        t2c = {
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_4": BLUE,
            "_5": BLUE,
            "_6": BLUE,
            "_7": BLUE,
            "a": GREEN,
            "\\omega": RED,
        }
        title = Text("高效实现FFT", font="Source Han Sans CN", t2c={"高效": YELLOW, "实现FFT": BLUE})
        title.scale(0.6).move_to([-4.5, 3.3, 0])
        self.add(title)
        sub = SubTopic("迭代实现").scale(0.8).next_to(title, DOWN, aligned_edge=LEFT)
        a = lambda i: TexMobject("a", "_"+str(i)).set_color_by_tex_to_color_map(t2c)
        com = lambda: TexMobject(",")
        tree0 = VGroup(
            *[VGroup(a(i), com()).arrange_submobjects(RIGHT, aligned_edge=DOWN) for i in range(7)],
            a(7)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).shift(UP*2)
        tree1 = VGroup(
            *[VGroup(a(i), com()).arrange_submobjects(RIGHT, aligned_edge=DOWN) for i in [0, 2, 4]],
            a(6)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([-3.5, tree0.get_center()[1]-1.2, 0])
        tree2 = VGroup(
            *[VGroup(a(i), com()).arrange_submobjects(RIGHT, aligned_edge=DOWN) for i in [1, 3, 5]],
            a(7)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([3.5, tree0.get_center()[1]-1.2, 0])
        tree3 = VGroup(
            a(0), com(), a(4)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([-5.25, tree1.get_center()[1]-1.2, 0])
        tree4 = VGroup(
            a(2), com(), a(6)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([-1.75, tree1.get_center()[1]-1.2, 0])
        tree5 = VGroup(
            a(1), com(), a(5)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([1.75, tree1.get_center()[1]-1.2, 0])
        tree6 = VGroup(
            a(3), com(), a(7)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([5.25, tree1.get_center()[1]-1.2, 0])
        leaf = VGroup(
            *[
                a(i).move_to([j, tree3.get_center()[1]-1.2, 0])
                for i, j in zip([0, 4, 2, 6, 1, 5, 3, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        
        self.wait()
        self.play(Write(sub))
        self.wait(2)
        self.play(Write(tree0))
        self.wait()
        self.play(
            TransformFromCopy(tree0[0][0], tree1[0][0]),
            TransformFromCopy(tree0[2][0], tree1[1][0]),
            TransformFromCopy(tree0[4][0], tree1[2][0]),
            TransformFromCopy(tree0[6][0], tree1[3]),
            run_time=3
        )
        self.play(FadeIn(VGroup(*[tree1[i][1] for i in range(3)])))
        self.wait()
        self.play(
            TransformFromCopy(tree0[1][0], tree2[0][0]),
            TransformFromCopy(tree0[3][0], tree2[1][0]),
            TransformFromCopy(tree0[5][0], tree2[2][0]),
            TransformFromCopy(tree0[7], tree2[3]),
            run_time=3
        )
        self.play(FadeIn(VGroup(*[tree2[i][1] for i in range(3)])))
        self.wait(2)
        self.play(
            TransformFromCopy(tree1[0][0], tree3[0]),
            TransformFromCopy(tree1[2][0], tree3[2]),
            run_time=2
        )
        self.play(FadeIn(tree3[1]))
        self.wait()
        self.play(
            TransformFromCopy(tree1[1][0], tree4[0]),
            TransformFromCopy(tree1[3], tree4[2]),
            run_time=2
        )
        self.play(FadeIn(tree4[1]))
        self.wait()
        self.play(
            TransformFromCopy(tree2[0][0], tree5[0]),
            TransformFromCopy(tree2[2][0], tree5[2]),
            TransformFromCopy(tree2[1][0], tree6[0]),
            TransformFromCopy(tree2[3], tree6[2]),
            run_time=2
        )
        self.play(FadeIn(tree5[1]), FadeIn(tree6[1]))
        self.wait(2)
        self.play(
            TransformFromCopy(tree3[0], leaf[0]),
            TransformFromCopy(tree3[2], leaf[1]),
            TransformFromCopy(tree4[0], leaf[2]),
            TransformFromCopy(tree4[2], leaf[3]),
            TransformFromCopy(tree5[0], leaf[4]),
            TransformFromCopy(tree5[2], leaf[5]),
            TransformFromCopy(tree6[0], leaf[6]),
            TransformFromCopy(tree6[2], leaf[7]),
            run_time=3
        )
        self.wait(3)


class FFT_improve_part3(Scene):
    def construct(self):
        t2c = {
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_4": BLUE,
            "_5": BLUE,
            "_6": BLUE,
            "_7": BLUE,
            "_{2}": GOLD,
            "_{4}": GOLD,
            "_{8}": GOLD,
            "a": GREEN,
            "\\omega": RED,
        }
        title = Text("高效实现FFT", font="Source Han Sans CN", t2c={"高效": YELLOW, "实现FFT": BLUE})
        title.scale(0.6).move_to([-4.5, 3.3, 0])
        sub = SubTopic("迭代实现").scale(0.8).next_to(title, DOWN, aligned_edge=LEFT)
        self.add(title, sub)
        a = lambda i: TexMobject("a", "_"+str(i)).set_color_by_tex_to_color_map(t2c)
        com = lambda: TexMobject(",")
        w = lambda i: TexMobject("\\omega", "_{"+str(i)+"}").set_color_by_tex_to_color_map(t2c).scale(0.8)
        leaf = VGroup(
            *[
                a(i).move_to([j, -1.59999, 0])
                for i, j in zip([0, 4, 2, 6, 1, 5, 3, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        self.add(leaf)
        self.play(leaf.shift, UP*3.6)
        tree3 = VGroup(
            a(0), com(), a(4)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([-5.25, leaf.get_center()[1]-1.2, 0])
        tree4 = VGroup(
            a(2), com(), a(6)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([-1.75, leaf.get_center()[1]-1.2, 0])
        tree5 = VGroup(
            a(1), com(), a(5)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([1.75, leaf.get_center()[1]-1.2, 0])
        tree6 = VGroup(
            a(3), com(), a(7)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([5.25, leaf.get_center()[1]-1.2, 0])
        tree1 = VGroup(
            *[VGroup(a(i), com()).arrange_submobjects(RIGHT, aligned_edge=DOWN) for i in [0, 2, 4]],
            a(6)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([-3.5, tree3.get_center()[1]-1.2, 0])
        tree2 = VGroup(
            *[VGroup(a(i), com()).arrange_submobjects(RIGHT, aligned_edge=DOWN) for i in [1, 3, 5]],
            a(7)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([3.5, tree3.get_center()[1]-1.2, 0])
        tree0 = VGroup(
            *[VGroup(a(i), com()).arrange_submobjects(RIGHT, aligned_edge=DOWN) for i in range(7)],
            a(7)
        ).arrange_submobjects(RIGHT, aligned_edge=DOWN).move_to([0, tree1.get_center()[1]-1.2, 0])
        w2_0 = w(2).move_to([-5.25, (leaf.get_center()[1]+tree3.get_center()[1]) / 2, 0])
        w2_1 = w(2).move_to([-1.75, (leaf.get_center()[1]+tree3.get_center()[1]) / 2, 0])
        w2_2 = w(2).move_to([ 1.75, (leaf.get_center()[1]+tree3.get_center()[1]) / 2, 0])
        w2_3 = w(2).move_to([ 5.25, (leaf.get_center()[1]+tree3.get_center()[1]) / 2, 0])
        w4_0 = w(4).move_to([-3.5, (tree1.get_center()[1]+tree3.get_center()[1]) / 2, 0])
        w4_1 = w(4).move_to([ 3.5, (tree1.get_center()[1]+tree3.get_center()[1]) / 2, 0])
        w8_0 = w(8).move_to([  0 , (tree1.get_center()[1]+tree0.get_center()[1]) / 2, 0])
        self.play(
            TransformFromCopy(leaf[0], tree3[0]),
            TransformFromCopy(leaf[1], tree3[2]),
            TransformFromCopy(leaf[2], tree4[0]),
            TransformFromCopy(leaf[3], tree4[2]),
            TransformFromCopy(leaf[4], tree5[0]),
            TransformFromCopy(leaf[5], tree5[2]),
            TransformFromCopy(leaf[6], tree6[0]),
            TransformFromCopy(leaf[7], tree6[2]),
            FadeInFrom(VGroup(w2_0, w2_1, w2_2, w2_3), UP),
            run_time=3
        )
        self.play(
            FadeIn(VGroup(tree3[1], tree4[1], tree5[1], tree6[1]))
        )
        self.wait(2)
        self.play(
            TransformFromCopy(tree3[0], tree1[0][0]),
            TransformFromCopy(tree3[2], tree1[2][0]),
            TransformFromCopy(tree4[0], tree1[1][0]),
            TransformFromCopy(tree4[2], tree1[3]),
            TransformFromCopy(tree5[0], tree2[0][0]),
            TransformFromCopy(tree5[2], tree2[2][0]),
            TransformFromCopy(tree6[0], tree2[1][0]),
            TransformFromCopy(tree6[2], tree2[3]),
            FadeInFrom(VGroup(w4_0, w4_1), UP),
            run_time=3
        )
        self.play(
            FadeIn(VGroup(tree1[0][1], tree1[1][1], tree1[2][1], tree2[0][1], tree2[1][1], tree2[2][1]))
        )
        self.wait(2)
        self.play(
            TransformFromCopy(tree1[0][0], tree0[0][0]),
            TransformFromCopy(tree1[2][0], tree0[4][0]),
            TransformFromCopy(tree1[1][0], tree0[2][0]),
            TransformFromCopy(tree1[3], tree0[6][0]),
            TransformFromCopy(tree2[0][0], tree0[1][0]),
            TransformFromCopy(tree2[2][0], tree0[5][0]),
            TransformFromCopy(tree2[1][0], tree0[3][0]),
            TransformFromCopy(tree2[3], tree0[7]),
            FadeInFrom(w8_0, UP),
            run_time=3
        )
        self.play(
            FadeIn(VGroup(*[tree0[i][1] for i in range(7)]))
        )
        self.wait(3)
        nums = VGroup(
            *[Text(str(i), font="Consolas").scale(0.5).set_color(GRAY) for i in range(4)]
        ).arrange_submobjects(DOWN, buff=0.9).next_to(leaf, LEFT, aligned_edge=UP)
        self.play(Write(nums))
        rec1 = SurroundingRectangle(w2_1[1])
        rec2 = SurroundingRectangle(tree4)
        rec3 = SurroundingRectangle(w4_0[1])
        rec4 = SurroundingRectangle(tree1)
        text1 = TexMobject("2", "^1").next_to(tree4, RIGHT, buff=0.8)
        text1[1].set_color(BLUE_A)
        text2 = TexMobject("2", "^2").next_to(tree1, RIGHT, buff=0.8)
        text2[1].set_color(BLUE_A)
        self.wait(2)
        self.play(
            ShowCreation(rec1)
        )
        self.play(
            ShowCreation(rec2),
            TransformFromCopy(tree4, w2_1[1].copy())
        )
        self.wait(2)
        self.play(FadeInFrom(text1[0], RIGHT))
        self.play(TransformFromCopy(nums[1], text1[1]))
        self.wait()
        self.play(FadeOut(VGroup(rec1, rec2)))
        self.wait(2)
        self.play(
            ShowCreation(rec3)
        )
        self.play(
            ShowCreation(rec4),
            TransformFromCopy(tree1, w4_0[1].copy())
        )
        self.wait(2)
        self.play(FadeInFrom(text2[0], RIGHT))
        self.play(TransformFromCopy(nums[2], text2[1]))
        self.wait()
        self.play(FadeOut(VGroup(rec3, rec4)))
        self.wait(3)


class FFT_improve_Code(Scene):
    def construct(self):
        t2c = {
            "a": GREEN,
            "n/2-1": GOLD,
            "dep": BLUE_A,
            "^{dep}": BLUE_A,
            "n": GOLD,
            "m": GOLD,
            "_m": GOLD,
            "2\\pi/m": BLUE_A,
            "^{\\frac{2\\pi}{m}}": BLUE_A,
            "{i}": BLUE_E,
            "\\omega": RED,
            "\\boldsymbol{a}": GREEN,
            "k": BLUE,
            "m/2-1": GOLD,
            "j": BLUE,
            "t": WHITE,
            "u": WHITE,
            "_{k+j+m/2}": BLUE,
            "_{k+j}": BLUE,
        }
        nums = VGroup(
            *[
                Text(str(i), font="Consolas").scale(0.4).set_color(GRAY)
                for i in range(1, 13)
            ]
        ).arrange_submobjects(DOWN, aligned_edge=RIGHT, buff=0.25).shift(LEFT*4)
        title = TexMobject("\\text{FFT}", "(", "\\boldsymbol{a}", ")")
        title.set_color_by_tex_to_color_map(t2c).scale(0.8)
        title.next_to(nums, UP, aligned_edge=LEFT)
        code = VGroup()
        line1 = TexMobject("\\textbf{BitReverse}\\ \\ ", "\\boldsymbol{a}")
        line1.scale(0.75).next_to(nums[0], RIGHT).set_color_by_tex_to_color_map(t2c)
        line1[0].set_color(WHITE)
        code.add(line1)
        line2 = TexMobject("\\textbf{for}\\ \\ ", "dep", "=", "1", "\\ .\\ .\\ ", "\\log_2", "n")
        line2.scale(0.75).next_to(nums[1], RIGHT).set_color_by_tex_to_color_map(t2c)
        code.add(line2)
        line3 = TexMobject("m", "=", "2", "^{dep}")
        line3.scale(0.75).next_to(nums[2], RIGHT, buff=1, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line3)
        line4 = TexMobject("\\omega", "_m", "=", "e", "^{\\frac{2\\pi}{m}", "i}", "=", "\\cos", "(", "2\\pi/m", ")", "+",\
            "{i}", "\\sin", "(", "2\\pi/m", ")")
        line4.scale(0.75).next_to(nums[3], RIGHT, buff=1, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        line4[4].set_color(BLUE_A); line4[5].set_color(BLUE_E)
        code.add(line4)
        line5 = TexMobject("\\textbf{for}\\ \\ ", "k", "=", "0", "\\ .\\ .\\ ", "n-1", "\\ \\ \\textbf{by}\\ \\ ", "m")
        line5.scale(0.75).next_to(nums[4], RIGHT, buff=1, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line5)
        line6 = TexMobject("\\omega", "=", "1")
        line6.scale(0.75).next_to(nums[5], RIGHT, buff=1.8, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line6)
        line7 = TexMobject("\\textbf{for}\\ \\ ", "j", "=", "0", "\\ .\\ .\\ ", "m/2-1")
        line7.scale(0.75).next_to(nums[6], RIGHT, buff=1.8, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line7)
        line8 = TexMobject("t", "=", "\\omega", "a", "_{k+j+m/2}")
        line8.scale(0.75).next_to(nums[7], RIGHT, buff=2.6, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line8)
        line9 = TexMobject("u", "=", "a", "_{k+j}")
        line9.scale(0.75).next_to(nums[8], RIGHT, buff=2.6, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line9)
        line10 = TexMobject("a", "_{k+j}", "=", "u", "+", "t")
        line10.scale(0.75).next_to(nums[9], RIGHT, buff=2.6, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line10)
        line11 = TexMobject("a", "_{k+j+m/2}", "=", "u", "-", "t")
        line11.scale(0.75).next_to(nums[10], RIGHT, buff=2.6, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line11)
        line12 = TexMobject("\\omega", "=", "\\omega", "\\omega", "_m")
        line12.scale(0.75).next_to(nums[11], RIGHT, buff=2.6, aligned_edge=DOWN).set_color_by_tex_to_color_map(t2c)
        code.add(line12)

        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeInFrom(nums[0], LEFT))
        self.play(Write(code[0]))
        self.wait(2)
        self.play(FadeInFrom(nums[1], LEFT))
        self.play(Write(code[1]))
        self.wait(2)
        self.play(FadeInFrom(nums[2:4], LEFT))
        self.play(Write(code[2:4]))
        self.wait(2)
        self.play(FadeInFrom(nums[4], LEFT))
        self.play(Write(code[4]))
        self.wait(2)
        self.play(FadeInFrom(nums[5], LEFT))
        self.play(Write(code[5]))
        self.wait(2)
        self.play(FadeInFrom(nums[6:], LEFT))
        self.play(Write(code[6]))
        self.wait(2)
        self.play(Write(code[11]))
        self.wait(2)
        self.play(Write(code[7:9]))
        self.wait(2)
        self.play(Write(code[9:11]))
        self.wait(3)
        sq = Rectangle(height=10, width=20).set_fill(BLACK, 1)
        self.add(sq)
        self.wait(3)
        self.remove(sq)
        self.wait(2)
        q = VGroup()
        q.add(SurroundingRectangle(VGroup(nums[0], code[0])))
        q.add(SurroundingRectangle(VGroup(nums[1:4], code[1:4])))
        q.add(SurroundingRectangle(VGroup(nums[4], code[4])))
        q.add(SurroundingRectangle(VGroup(nums[5], code[5])))
        q.add(SurroundingRectangle(VGroup(nums[6:], code[6:])))
        for m in q:
            self.play(ShowCreation(m))
            self.play(ScaleInPlace(m, 1.1, rate_func=wiggle))
            self.wait(2)
            self.play(FadeOut(m))
            self.wait(2)
        self.wait()


class FFT_improve_part4_1(Scene):
    def construct(self):
        t2c = {
            "_0": BLUE,
            "_1": BLUE,
            "_2": BLUE,
            "_3": BLUE,
            "_4": BLUE,
            "_5": BLUE,
            "_6": BLUE,
            "_7": BLUE,
            "_{2}": GOLD,
            "_{4}": GOLD,
            "_{8}": GOLD,
            "a": GREEN,
            "\\omega": RED,
        }
        title = Text("位逆序置换", font="Source Han Sans CN", t2c={"位逆序": YELLOW, "置换": BLUE})
        title.scale(0.6).move_to([-4.5, 3.3, 0])
        entitle = TexMobject("\\textbf{BitReverse}").next_to(title, RIGHT, aligned_edge=DOWN)
        self.play(Write(title))
        self.play(DrawBorderThenFill(entitle))
        self.wait()
        a = lambda i: TexMobject("a", "_"+str(i)).set_color_by_tex_to_color_map(t2c)
        leaf = VGroup(
            *[
                a(i).move_to([j, 1.8, 0])
                for i, j in zip([0, 4, 2, 6, 1, 5, 3, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        old_id = VGroup(
            *[
                Text(str(i), font="Consolas").scale(0.5).move_to([j, 2.4, 0])
                for i, j in zip([0, 1, 2, 3, 4, 5, 6, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        nold_id = VGroup(
            *[
                Text(str(i), font="Consolas").scale(0.5).move_to([j, 2.4, 0])
                for i, j in zip([0, 1, 2, 3, 4, 5, 6, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        new_id = VGroup(
            *[
                Text(str(i), font="Consolas").scale(0.5).move_to([j, 1.8, 0]).set_color(BLUE_A)
                for i, j in zip([0, 4, 2, 6, 1, 5, 3, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        self.play(FadeInFrom(old_id, UP), FadeInFrom(leaf, DOWN))
        self.wait(2)
        self.play(
            *[FadeOut(leaf[i][0]) for i in range(8)],
            *[ReplacementTransform(leaf[i][1], new_id[i]) for i in range(8)],
            run_time=3
        )
        self.wait(2)
        binary = lambda n: bin(n).replace('0b','').rjust(3,'0')
        bin_old_id = VGroup(
            *[
                Text(binary(i), font="Consolas").scale(0.5).move_to([j, 2.4, 0])
                for i, j in zip([0, 1, 2, 3, 4, 5, 6, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        bin_new_id = VGroup(
            *[
                Text(binary(i), font="Consolas").scale(0.5).move_to([j, 1.8, 0]).set_color(BLUE_A)
                for i, j in zip([0, 4, 2, 6, 1, 5, 3, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        for i in range(8):
            self.play(Transform(old_id[i], bin_old_id[i]), run_time=0.4)
            self.wait(0.1)
        self.wait()
        for i in range(8):
            self.play(Transform(new_id[i], bin_new_id[i]), run_time=0.4)
            self.wait(0.1)
        self.wait(2)
        for i in range(8):
            self.play(old_id[i].flip, UP, run_time=0.4)
            self.wait(0.1)
        self.wait(2)
        for i in range(8):
            self.play(old_id[i].flip, UP, run_time=0.4)
            self.wait(0.1)
        self.wait(2)
        self.play(*[Transform(old_id[i], nold_id[i]) for i in range(8)])
        self.wait(3)


class FFT_improve_part4_2(Scene):
    def construct(self):
        title = Text("位逆序置换", font="Source Han Sans CN", t2c={"位逆序": YELLOW, "置换": BLUE})
        title.scale(0.6).move_to([-4.5, 3.3, 0])
        entitle = TexMobject("\\textbf{BitReverse}").next_to(title, RIGHT, aligned_edge=DOWN)
        binary = lambda n: bin(n).replace('0b','').rjust(3,'0')
        old_id = VGroup(
            *[
                Text(str(i), font="Consolas").scale(0.5).move_to([j, 2.4, 0])
                for i, j in zip([0, 1, 2, 3, 4, 5, 6, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        new_id = VGroup(
            *[
                Text(binary(i), font="Consolas").scale(0.5).move_to([j, 1.8, 0]).set_color(BLUE_A)
                for i, j in zip([0, 4, 2, 6, 1, 5, 3, 7], [-6.125, -4.375, -2.625, -0.875, 0.875, 2.625, 4.375, 6.125])
            ]
        )
        self.add(old_id, new_id)
        self.add(title, entitle)
        self.wait(2)
        planA = TexMobject("O(n\\log n)", "\\text{模拟}").set_color(GOLD).next_to(new_id[2], DOWN)
        planB = TexMobject("O(n)", "\\text{预处理}").set_color(GOLD).next_to(planA, RIGHT, buff=2)
        cross = Cross(planA)
        self.play(Write(planA))
        self.wait()
        self.play(
            ShowCreation(cross),
            FadeInFrom(planB, LEFT)
        )
        self.wait(3)
        self.play(
            FadeOut(planA), FadeOut(planB), FadeOut(cross)
        )
        self.wait(2)
        sub1_title = SubTopic("规律Ⅰ: ").scale(0.8).next_to(new_id[1], DOWN, buff=0.8)
        sub1 = Text("偶数位上首位为0，奇数位上首位为1", font="Source Han Serif CN").scale(0.4).next_to(sub1_title, RIGHT)
        sub2_title = SubTopic("规律Ⅱ: ").scale(0.8).next_to(sub1_title, DOWN, aligned_edge=LEFT)
        sub2 = Text("每两个数除首位外均相同", font="Source Han Serif CN").scale(0.4).next_to(sub2_title, RIGHT)
        sub3_title = SubTopic("规律Ⅲ: ").scale(0.8).next_to(sub2_title, DOWN, aligned_edge=LEFT)
        sub3 = Text("每两个数除首位外是上一级子问题的解", font="Source Han Serif CN").scale(0.4).next_to(sub3_title, RIGHT)
        sub4_title = SubTopic("规律Ⅳ: ").scale(0.8).next_to(sub3_title, DOWN, aligned_edge=LEFT)
        sub4 = Text("前一半数除末位外是上一级子问题的解", font="Source Han Serif CN").scale(0.4).next_to(sub4_title, RIGHT)
        sol = Text("rev[i] = (rev[i>>1]>>1) | ((i&1)<<(len-1))", font="Monaco for Powerline").scale(0.4).shift(DOWN*2.3)

        self.play(
            *[
                ShowCreationThenDestructionAround(new_id[i][0])
                for i in [0, 2, 4, 6]
            ],
            run_time=1.5
        )
        self.play(
            *[
                ShowCreationThenDestructionAround(new_id[i][0])
                for i in [1, 3, 5, 7]
            ],
            run_time=1.5
        )
        self.wait(2)
        self.play(Write(sub1_title))
        self.wait()
        self.play(Write(sub1))
        self.wait(3)
        for i in [0, 2, 4, 6]:
            self.play(
                ShowCreationThenDestructionAround(new_id[i][1:]),
                ShowCreationThenDestructionAround(new_id[i + 1][1:])
            )
        self.wait(2)
        self.play(Write(sub2_title))
        self.wait()
        self.play(Write(sub2))
        self.wait(3)
        recs = []
        recs.append(SurroundingRectangle(new_id[0][1:]))
        recs.append(SurroundingRectangle(new_id[2][1:]))
        recs.append(SurroundingRectangle(new_id[4][1:]))
        recs.append(SurroundingRectangle(new_id[6][1:]))
        self.play(*[ShowCreation(m) for m in recs])
        self.wait(2)
        self.play(Write(sub3_title))
        self.wait()
        self.play(Write(sub3))
        self.play(*[FadeOut(m) for m in recs])
        self.wait(3)
        recs = []
        recs.append(SurroundingRectangle(new_id[0][:2]))        
        recs.append(SurroundingRectangle(new_id[1][:2]))        
        recs.append(SurroundingRectangle(new_id[2][:2]))
        recs.append(SurroundingRectangle(new_id[3][:2]))   
        self.play(*[ShowCreation(m) for m in recs])
        self.wait(2)
        self.play(Write(sub4_title))
        self.wait()
        self.play(Write(sub4))
        self.play(*[FadeOut(m) for m in recs])
        self.wait(3)

        self.play(Write(sol[:8]))
        self.wait(2)
        self.play(Write(sol[10:19]))
        self.wait()
        self.play(Write(sol[19:22]))
        self.wait()
        self.play(FadeIn(sol[9]), FadeIn(sol[22]))
        self.wait(2)
        self.wait()
        self.play(Write(sol[28:31]))
        self.play(FadeIn(sol[27]), FadeIn(sol[31]))
        self.wait()
        self.play(Write(sol[32:41]))
        self.wait()
        self.play(FadeIn(sol[26]), FadeIn(sol[41]))
        self.wait()
        self.play(Write(sol[24]))
        self.wait(3)


class FFT_improve_part5(FFTScene):
    def construct(self):
        graph = self.set_up()
        self.play(FadeInFrom(graph[0], LEFT))
        self.play(ShowCreation(graph[1]))
        self.wait(2)
        self.play(ShowCreation(graph[2]), run_time=1.5)
        self.wait(2)
        self.play(ShowCreation(graph[3]), run_time=2)
        self.wait(2)
        self.play(FadeInFromLarge(graph[4]), run_time=1.5)
        self.wait(2)
        self.play(FadeInFromLarge(VGroup(graph[5], graph[6])), run_time=1.5)
        self.wait(2)
        self.play(FadeInFromLarge(graph[7]), run_time=1.5)
        self.wait(2)
        self.play(Write(graph[8]))
        self.play(ScaleInPlace(graph[8], 2, rate_func=wiggle))
        self.wait(3)


class IFFT_part1(Scene):
    def construct(self):
        title = Text("快速傅里叶逆变换", font="Source Han Sans CN", t2c={"逆" : YELLOW, "快速傅里叶" : BLUE, "变换" : BLUE})
        title.scale(0.6).move_to([-4.3, 3.3, 0])
        entitle = TextMobject("I", "nverse ", "F", "ast ", "F", "ourier ", "T", "ransform").next_to(title, RIGHT)
        entitle[0].set_color(YELLOW)
        entitle[2].set_color(BLUE)
        entitle[4].set_color(BLUE)
        entitle[6].set_color(BLUE)
        self.play(Write(title))
        self.play(DrawBorderThenFill(entitle))
        self.wait(2)
        t2c = {
            "_{j}": BLUE,
            "a": GREEN,
            "\\omega": RED,
            "^{i}": GOLD,
            "^{j}": GOLD,
            "_n": GOLD,
            "\\boldsymbol{V}": ORANGE,
            "\\boldsymbol{a}": GREEN,
            "_{ij}": BLUE,
            "^{ij}": BLUE,
            "n": GOLD,
            "^{-ij}": BLUE,
            "\\boldsymbol{I}": YELLOW
        }
        formula = VGroup(
            TextMobject("DFT"),
            TexMobject("\\rightarrow"),
            TexMobject("y_i=", "\\sum", "^{n-1}", "_{j", "=", "0}", "\\omega", "_n", "^{i", "j}", "a", "_{j}").set_color_by_tex_to_color_map(t2c),
            TexMobject("\\rightarrow"),
            TexMobject("\\boldsymbol{y}", "=", "\\boldsymbol{V}", "_n", "\\boldsymbol{a}").set_color_by_tex_to_color_map(t2c)
        ).arrange_submobjects(RIGHT, aligned_edge=ORIGIN).shift(UP*2.2)
        formula[2][3].set_color(BLUE)
        formula[2][8].set_color(BLUE)
        formula[2][9].set_color(GOLD)
        formula[2][2].set_color(WHITE)
        vander = TexMobject("\\boldsymbol{V}", "_n", "=", """
            \\begin{bmatrix}
            1 & 1 & 1 & \\cdots & 1\\\\
            1 & \\omega_n & \\omega_n^2 & \\cdots & \\omega_n^{n-1}\\\\
            1 & \\omega_n^2 & \\omega_n^4 & \\cdots & \\omega_n^{2(n-1)}\\\\
            \\vdots & \\vdots & \\vdots & \\ddots & \\vdots\\\\
            1 & \\omega_n^{n-1} & \\omega_n^{2(n-1)} & \\cdots & \\omega_n^{(n-1)(n-1)}
            \\end{bmatrix}
        """).scale(0.8).shift(DOWN*0.5)
        vander[0].set_color(ORANGE)
        vander[1].set_color(GOLD)
        vander[:3].scale(1.25, about_edge=RIGHT)
        transvander = TexMobject("(", "\\boldsymbol{V}", "_n", ")", "_{ij}", "=", "\\omega", "^{ij}", "_n").set_color_by_tex_to_color_map(t2c)
        transvander.next_to(formula[0], DOWN, buff=1)
        need = TexMobject("\\boldsymbol{a}", "=", "\\boldsymbol{V}", "^{-1}", "_n", "\\boldsymbol{y}")
        need.move_to([formula[4].get_center()[0], transvander.get_center()[1], 0]).set_color_by_tex_to_color_map(t2c)
        ivander = TexMobject("(", "\\boldsymbol{V}", "^{-1}", "_n", ")", "_{ij}", "=", "{\\omega", "^{-ij}", "_n", "\\over", "n}")
        ivander.next_to(transvander, DOWN).set_color_by_tex_to_color_map(t2c)
        proof = TexMobject("(\\boldsymbol{V}^{-1}_n\\boldsymbol{V}_n)_{ij}", "&=", \
            "\\sum^{n-1}_{k=0}\\frac{\\omega^{-ki}_n}{n}\\times\\omega^{kj}_n\\\\", "&=", \
            "\\sum^{n-1}_{k=0}\\frac{\\omega^{k(j-i)}_n}{n}").scale(0.8).move_to([3.5, 0, 0])
        qed = TexMobject("\\boldsymbol{V}", "^{-1}", "_n", "\\boldsymbol{V}", "_n", "=", "\\boldsymbol{I}", "_n").next_to(proof, DOWN)
        qed.set_color_by_tex_to_color_map(t2c)
        
        self.play(Write(formula[0]))
        self.wait()
        for i in [1, 2, 3, 4]:
            self.play(FadeInFrom(formula[i], LEFT))
            self.wait()
        self.wait()
        self.play(FadeIn(vander))
        self.wait(2)
        self.play(ReplacementTransform(vander, transvander))
        self.wait(2)
        self.play(FadeInFrom(need, UP))
        self.wait(2)
        self.play(TransformFromCopy(need[2:5], ivander[1:4]))
        self.wait()
        self.play(FadeIn(VGroup(ivander[0], ivander[4], ivander[5])))
        self.wait()
        self.play(Write(ivander[6:]))
        self.wait(3)
        pos = need.get_center()
        need.next_to(ivander, DOWN)
        pos2 = need.get_center()
        need.move_to(pos)
        self.play(need.move_to, pos2)
        self.wait(2)
        self.play(Write(proof[0]))
        self.play(FadeIn(proof[1]))
        self.wait()
        self.play(Write(proof[2]))
        self.play(FadeIn(proof[3]))
        self.wait()
        self.play(Write(proof[4]))
        self.wait(2)
        self.play(FadeInFrom(qed, UP))
        self.play(ShowCreationThenDestructionAround(qed))
        self.wait(3)


class IFFT_part2(Scene):
    def construct(self):
        t2c = {
            "_{j}": BLUE,
            "a": GREEN,
            "\\omega": RED,
            "^{i}": GOLD,
            "^{j}": GOLD,
            "_n": GOLD,
            "_i": BLUE,
            "\\boldsymbol{V}": ORANGE,
            "\\boldsymbol{a}": GREEN,
            "_{ij}": BLUE,
            "^{ij}": BLUE,
            "n": GOLD,
            "^{-ij}": BLUE,
            "\\boldsymbol{I}": YELLOW
        }
        title = Text("快速傅里叶逆变换", font="Source Han Sans CN", t2c={"逆" : YELLOW, "快速傅里叶" : BLUE, "变换" : BLUE})
        title.scale(0.6).move_to([-4.3, 3.3, 0])
        entitle = TextMobject("I", "nverse ", "F", "ast ", "F", "ourier ", "T", "ransform").next_to(title, RIGHT)
        entitle[0].set_color(YELLOW)
        entitle[2].set_color(BLUE)
        entitle[4].set_color(BLUE)
        entitle[6].set_color(BLUE)
        formula = VGroup(
            TextMobject("DFT"),
            TexMobject("\\rightarrow"),
            TexMobject("y_i=", "\\sum", "^{n-1}", "_{j", "=", "0}", "\\omega", "_n", "^{i", "j}", "a", "_{j}").set_color_by_tex_to_color_map(t2c),
            TexMobject("\\rightarrow"),
            TexMobject("\\boldsymbol{y}", "=", "\\boldsymbol{V}", "_n", "\\boldsymbol{a}").set_color_by_tex_to_color_map(t2c)
        ).arrange_submobjects(RIGHT, aligned_edge=ORIGIN).shift(UP*2.2)
        formula[2][0].set_color(WHITE)
        formula[2][3].set_color(BLUE)
        formula[2][8].set_color(BLUE)
        formula[2][9].set_color(GOLD)
        formula[2][2].set_color(WHITE)
        vander = TexMobject("(", "\\boldsymbol{V}", "_n", ")", "_{ij}", "=", "\\omega", "^{ij}", "_n").set_color_by_tex_to_color_map(t2c)
        vander.next_to(formula[0], DOWN, buff=1)
        need = TexMobject("\\boldsymbol{a}", "=", "\\boldsymbol{V}", "^{-1}", "_n", "\\boldsymbol{y}")
        need.set_color_by_tex_to_color_map(t2c)
        ivander = TexMobject("(", "\\boldsymbol{V}", "^{-1}", "_n", ")", "_{ij}", "=", "{\\omega", "^{-ij}", "_n", "\\over", "n}")
        ivander.next_to(vander, DOWN).set_color_by_tex_to_color_map(t2c)
        need.next_to(ivander, DOWN)
        proof = TexMobject("(\\boldsymbol{V}^{-1}_n\\boldsymbol{V}_n)_{ij}", "&=", \
            "\\sum^{n-1}_{k=0}\\frac{\\omega^{-ki}_n}{n}\\times\\omega^{kj}_n\\\\", "&=", \
            "\\sum^{n-1}_{k=0}\\frac{\\omega^{k(j-i)}_n}{n}").scale(0.8).move_to([3.5, 0, 0])
        qed = TexMobject("\\boldsymbol{V}", "^{-1}", "_n", "\\boldsymbol{V}", "_n", "=", "\\boldsymbol{I}", "_n").next_to(proof, DOWN)
        qed.set_color_by_tex_to_color_map(t2c)
        self.add(title, entitle, formula, vander, need, ivander, proof, qed)
        self.wait()
        self.play(
            FadeOut(VGroup(formula[3:], vander, proof, qed))
        )
        self.play(formula[:3].set_opacity, 0.4)
        self.wait()
        self.play(
            ivander.shift, UP,
            need.shift, UP
        )
        self.wait()
        ifft = TexMobject("a", "_i", "=", "\\sum", "^{n-1}", "_{j", "=", "0}", "{\\omega", "^{-i", "j}", "_n", "\\over", "n}", "y_j")
        ifft.set_color_by_tex_to_color_map(t2c).move_to([3.5, ivander.get_center()[1], 0])
        ifft[4].set_color(WHITE); ifft[5].set_color(BLUE)
        ifft[9].set_color(GOLD); ifft[10].set_color(BLUE)
        idft = TexMobject("a", "_i", "=", "{1", "\\over", "n}", "\\sum", "^{n-1}", "_{j", "=", "0}", "\\omega", "^{-i", "j}", "_n", "y_j")
        idft.set_color_by_tex_to_color_map(t2c).next_to(ifft, DOWN, aligned_edge=LEFT)
        idft[7].set_color(WHITE); idft[8].set_color(BLUE)
        idft[12].set_color(GOLD); idft[13].set_color(BLUE)

        self.wait()
        self.play(TransformFromCopy(need, ifft), run_time=2)
        self.wait()
        self.play(TransformFromCopy(ifft, idft), run_time=2)
        self.wait(2)
        self.play(FadeOut(ivander), FadeOut(need), FadeOut(ifft))
        self.wait(2)
        self.play(formula[:3].set_opacity, 1)
        self.play(formula[:3].move_to, [0, 1.5, 0])
        self.wait()
        formula_idft = VGroup(
            TextMobject("IDFT"),
            TexMobject("\\rightarrow"),
            idft.copy()
        ).arrange_submobjects(RIGHT, aligned_edge=ORIGIN)
        formula_idft.next_to(formula[1].get_center(), DOWN, index_of_submobject_to_align=1, buff=1.6)
        self.play(idft.move_to, formula_idft[2].get_center())
        self.wait()
        self.play(FadeInFrom(formula_idft[:2], LEFT))
        self.wait(2)
        self.play(
            ShowCreationThenDestructionAround(formula[2][7]),
            ShowCreationThenDestructionAround(idft[12])
        )
        
        self.wait()
        t2c2 = {
            "\\omega": RED,
            "_n": GOLD,
            "^{\\frac{2\\pi}{n}}": BLUE_A,
            "^{-\\frac{2\\pi}{n}}": BLUE_A,
            "{i}": BLUE_E,
            "2\\pi/n": BLUE_A,
        }
        sol = VGroup(
            Text("将", font="Source Han Serif CN").scale(0.6).set_color(GOLD),
            TexMobject("\\omega", "_n", "=", "e", "^{\\frac{2\\pi}{n}", "i}", "=", "\\cos", "(", "2\\pi/n", ")", "+",\
                "{i}", "\\sin", "(", "2\\pi/n", ")").set_color_by_tex_to_color_map(t2c2),
            Text("改成", font="Source Han Serif CN").scale(0.6).set_color(GOLD),
            TexMobject("\\omega", "_n", "=", "e", "^{-\\frac{2\\pi}{n}", "i}", "=", "\\cos", "(", "2\\pi/n", ")", "-",\
                "{i}", "\\sin", "(", "2\\pi/n", ")").set_color_by_tex_to_color_map(t2c2),
        ).scale(0.8)
        sol[1].next_to(sol[0], RIGHT)
        sol[3].next_to(sol[2], RIGHT)
        sol[2:].next_to(sol[:2], DOWN)
        sol.next_to(formula_idft, DOWN)
        sol[1][4].set_color(BLUE_A); sol[1][5].set_color(BLUE_E)
        sol[3][4].set_color(BLUE_A); sol[3][5].set_color(BLUE_E)
        self.wait()
        self.play(Write(sol))
        self.play(ShowCreationThenDestructionAround(sol))
        self.wait(3)


class PolynomialConvolutionSolve(Scene):
    def construct(self):
        t2c = {
            "\\boldsymbol{a}": GREEN,
            "\\boldsymbol{b}": GREEN,
            "\\text{IDFT}": ORANGE,
            "\\text{DFT}": ORANGE,
            "_{2n}": GOLD
        }
        formula = TexMobject("\\boldsymbol{a}", "\\otimes", "\\boldsymbol{b}", "=", "\\text{IDFT}", \
            "_{2n}", "\\big(", "\\text{DFT}", "_{2n}", "(", "\\boldsymbol{a}", ")", "\\circ", "\\text{DFT}", \
            "_{2n}", "(", "\\boldsymbol{b}", ")", "\\big)")
        formula.set_color_by_tex_to_color_map(t2c)
        
        self.wait()
        self.play(Write(formula[:4]))
        self.wait(2)
        self.play(Write(formula[7:12]))
        self.wait()
        self.play(Write(formula[13:18]))
        self.wait()
        self.play(FadeInFrom(formula[12]))
        self.wait()
        self.play(FadeIn(VGroup(formula[4:7], formula[18])))
        self.wait()
        self.play(ShowCreationThenDestructionAround(formula))
        self.wait(3)
        self.play(formula.shift, UP*3.2)
        self.wait(4)


class EndScene(TripleScene):
    def construct(self):
        thanks = VGroup(
            Text("特别鸣谢", font="Source Han Sans CN").set_color(RED),
            Text("@cigar666", font="Source Han Serif CN").scale(0.5).set_color(BLUE),
            Text("@有一种悲伤叫颓废", font="Source Han Serif CN").scale(0.5).set_color(BLUE)
        )
        cigar = ImageMobject("cigar.jpg").scale(0.5)
        tf = ImageMobject("颓废.png").scale(0.5)
        thanks[0].shift(UP * 2)
        thanks[1].shift(LEFT*3)
        cigar.next_to(thanks[1], LEFT)
        thanks[2].shift(RIGHT*4)
        tf.next_to(thanks[2], LEFT)
        screen_rect = ScreenRectangle(height=6).shift(UP * 0.4)
        title = Title("参考").set_color(RED)
        refer = VGroup(
            Text("[1] T. H. Cormen,et al. Introduction to Algorithms, Third Edition[M]. Massachusettes:The MIT Press, 2009 : 898-919", font="Source Han Serif CN").scale(0.2),
            Text("[2] attack. 题解P3803【【模板】多项式乘法(FFT)】[EB/OL]. https://www.luogu.com.cn/blog/attack/solution-p3803, 2018-02-12", font="Source Han Serif CN").scale(0.2),
            Text("[3] Wikipedia contributors. Fast Fourier transform[G/OL]. Wikipedia,2020-01-21. https://en.wikipedia.org/wiki/Fast_Fourier\n    _transform", font="Source Han Serif CN").scale(0.2),
            Text("[4] Wikipedia contributors. Discrete Fourier transform[G/OL]. Wikipedia,2020-01-10. https://en.wikipedia.org/wiki/Discrete\n    _Fourier_transform", font="Source Han Serif CN").scale(0.2),
            Text("[5] Wikipedia contributors. Butterfly diagram[G/OL]. Wikipedia,2019-08-09. https://en.wikipedia.org/wiki/Butterfly_diagram", font="Source Han Serif CN").scale(0.2),
            Text("[6] Wikipedia contributors. Complex number[G/OL]. Wikipedia,2020-01-22. https://en.wikipedia.org/wiki/Complex_number", font="Source Han Serif CN").scale(0.2),
            Text("[7] 3Blue1Brown. 欧拉公式与初等群论[OL]. https://www.bilibili.com/video/av11339177, 2017-06-15", font="Source Han Serif CN").scale(0.2),
            Text("[8] 3Blue1Brown. 微分方程概论-第五章：在3.14分钟内理解e^iπ[OL]. https://www.bilibili.com/video/av63666593, 2019-08-14", font="Source Han Serif CN").scale(0.2),
            Text("[7] MATHEART_EVER. 复数能有多优美 I[OL]. https://www.bilibili.com/video/av81286856, 2019-12-30", font="Source Han Serif CN").scale(0.2),
            Text("[8] MATHEART_EVER. 复数能有多优美 II -- 从单位根看几何性质[OL]. https://www.bilibili.com/video/avav86056773, 2020-02-01", font="Source Han Serif CN").scale(0.2),
        ).arrange_submobjects(DOWN, aligned_edge=LEFT, buff=0.15).next_to(title, DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.wait()
        self.play(ShowCreation(screen_rect))
        self.wait(5)
        self.play(FadeOut(screen_rect))
        self.wait()
        self.play(Write(thanks[0]))
        self.wait()
        self.play(FadeIn(thanks[1:]), FadeIn(cigar), FadeIn(tf), run_time=1.5)
        self.wait(5)
        self.play(
            thanks.shift, UP*4.5,
            cigar.shift, UP*4.5,
            tf.shift, UP*4.5,
        )
        self.wait()
        self.play(FadeInFrom(title, UP))
        self.wait()
        for i in refer:
            self.play(FadeInFromDown(i), run_time=0.4)
            self.wait(0.1)
        self.wait(2)
        

        self.get_svg()
        good = self.good
        coin = self.coin
        favo = self.favo
        self.play(
            FadeInFromPoint(good, good.get_center()),
            FadeInFromPoint(coin, coin.get_center()),
            FadeInFromPoint(favo, favo.get_center())
        )
        self.wait(0.4)
        circle_coin = Circle().scale(0.7).move_to(coin).set_stroke(PINK, 6)
        circle_favo = Circle().scale(0.7).move_to(favo).set_stroke(PINK, 6)
        self.play(
            good.set_color, LIGHT_PINK,
            ShowCreation(circle_coin),
            ShowCreation(circle_favo),
            run_time=1.5
        )
        self.play(
            FadeOut(circle_coin),
            FadeOut(circle_favo),
            Flash(coin.get_center(), color=PINK, line_length=0.7, flash_radius=1.5),
            Flash(favo.get_center(), color=PINK, line_length=0.7, flash_radius=1.5),
            Flash(good.get_center(), color=PINK, line_length=0.7, flash_radius=1.5),
            coin.set_color, LIGHT_PINK,
            favo.set_color, LIGHT_PINK,
            run_time=0.3
        )
        self.wait(3)


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
# 20.01.26 Finish DFT and FFT part1 2 3
# 20.01.27 Finish FFT code and FFT_improve part1 2
# 20.01.28 Finish FFT_improve part3 4 5 code and IFFT part1 
# 20.01.29 Finish all main Scenes !!!!!!
# 20.01.30 Finish Sound Recording
# 20.01.31 Finish three extra scenes and change sounds
# 20.02.01 add some extra scenes