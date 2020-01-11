'''
  > File Name        : FFT.py
  > Author           : Tony_Wong
  > Created Time     : 2019/12/18 12:31:49
'''

from manimlib.imports import *
from manim_projects.tony_useful.imports import *

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
        line1 = VGroup(
            *[
                Line(np.array([-5.5, 0.5 + i, 0]), np.array([-4.5, 0.5 + i, 0])).add_tip(tip_length=0.15)
                for i in range(3, -5, -1)
            ]
        )
        for line in line1:
            line.get_tip().shift(LEFT * 0.5)
        
        start2 = [3.5, 2.5, 1.5, 0.5, -0.5, -1.5, -2.5, -3.5]
        end2 = [3.5, -0.5, 1.5, -2.5, 2.5, -1.5, 0.5, -3.5]
        line2 = VGroup(
            *[
                Line(np.array([-4.66, start2[i], 0]), np.array([-3.5, end2[i], 0]))
                for i in range(0, 8)
            ]
        )

        line3 = VGroup(
            *[
                Line(np.array([-3.51, 0.5 + i, 0]), np.array([5.5, 0.5 + i, 0])).add_tip(tip_length=0.15)
                for i in range(3, -5, -1)
            ]
        )

        #TODO, replace place and todo with right things
        place = VGroup(
            DashedLine(np.array([-3.4, 5, 0]), np.array([-3.4, -5, 0])).set_color(GREEN),
            DashedLine(np.array([-2, 5, 0]), np.array([-2, -5, 0])).set_color(GREEN),
            DashedLine(np.array([1, 5, 0]), np.array([1, -5, 0])).set_color(GREEN),
            DashedLine(np.array([5, 5, 0]), np.array([5, -5, 0])).set_color(GREEN),
        )

        todo = VGroup(
            DashedLine(np.array([-4, 3, 0]), np.array([-1, 3, 0])).set_color(BLUE_A),
            DashedLine(np.array([-4, 1, 0]), np.array([-1, 1, 0])).set_color(BLUE_A),
            DashedLine(np.array([-4, -1, 0]), np.array([-1, -1, 0])).set_color(BLUE_A),
            DashedLine(np.array([-4, -3, 0]), np.array([-1, -3, 0])).set_color(BLUE_A),
            DashedLine(np.array([-1.5, 2, 0]), np.array([1.5, 2, 0])).set_color(BLUE_B),
            DashedLine(np.array([-1.5, 1, 0]), np.array([1.5, 1, 0])).set_color(BLUE_B),
            DashedLine(np.array([-1.5, -2, 0]), np.array([1.5, -2, 0])).set_color(BLUE_B),
            DashedLine(np.array([-1.5, -3, 0]), np.array([1.5, -3, 0])).set_color(BLUE_B),
            DashedLine(np.array([0.5, 0, 0]), np.array([6, 0, 0])).set_color(BLUE_C),
            DashedLine(np.array([0.5, -1, 0]), np.array([6, -1, 0])).set_color(BLUE_C),
            DashedLine(np.array([0.5, -2, 0]), np.array([6, -2, 0])).set_color(BLUE_C),
            DashedLine(np.array([0.5, -3, 0]), np.array([6, -3, 0])).set_color(BLUE_C),
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