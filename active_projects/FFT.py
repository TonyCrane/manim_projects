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


class VideoCover(Scene):
    def construct(self):
        # self.add_main()
        self.add_background()
        # self.add_subscripts()

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
        pass

    def add_subscripts(self):
        square = Square().rotate(PI / 4).scale(1.5).set_fill(BLUE, 1).set_color(BLUE)
        square.move_to(LEFT * 7.3 + UP * 4.6)
        text = Text("???", font='AR PL KaitiM GB', stroke_width=1.5).scale(0.8).rotate(PI / 4).next_to(square.get_edge_center(DOWN), buff=0)
        text.shift(UP * 1.3 + RIGHT * 0.24)

        self.add(square, text)
        

class FFTScene(Scene):
    def construct(self):
        self.set_up()

    def set_up(self):
        lines = []

        #TODO, add a_i tex
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

        #TODO, replace place and todo with right things
        place = VGroup(
            DashedLine([1, 5, 0], [1, -5, 0]).set_color(GREEN),
            DashedLine([5, 5, 0], [5, -5, 0]).set_color(GREEN),
        )

        todo = VGroup(
            DashedLine([0.5, 0, 0], [6, 0, 0]).set_color(BLUE_C),
            DashedLine([0.5, -1, 0], [6, -1, 0]).set_color(BLUE_C),
            DashedLine([0.5, -2, 0], [6, -2, 0]).set_color(BLUE_C),
            DashedLine([0.5, -3, 0], [6, -3, 0]).set_color(BLUE_C),
        )

        self.play(ShowCreation(line1))
        self.wait()
        self.play(ShowCreation(line2))
        self.wait()
        self.play(ShowCreation(line3))
        self.wait()
        self.play(ShowCreation(place))
        self.wait()
        self.play(ShowCreation(todo))

        #TODO, FadeIn these objects
        self.add(block1, block2, block3)


class DotMap(Scene):
    def construct(self):
        dots = VGroup()
        for x in range(-7, 8):
            for y in range(-4, 5):
                dots.add(Dot().move_to(RIGHT * x + UP * y))
        text1 = Text("(-7, -4)", font='Consolas').scale(0.5).move_to(dots[0]).shift(RIGHT * 0.9 + UP * 0.5)
        text2 = Text("(7, 4)", font='Consolas').scale(0.5).move_to(dots[-1]).shift(DOWN * 0.5 + LEFT * 0.9)
        self.add(dots, text1, text2)
                


##------Time Line------##
# 19.12.05 have an idea
# 19.12.07 ~ 19.12.12 study FFT
# 19.12.13 ~ 19.12.17 write notes
# 19.12.18 create FFT.py
# 19.12.19 ~ 19.12.?? write split scene scripts
# 20.01.11 Finish VideoCover's subscript and some of the background images
# 20.01.13 write some of the background images