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


class UnitRoot(Scene):
    def construct(self):




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