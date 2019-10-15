from big_ol_pile_of_manim_imports import *
from manim_projects.MyUsefulScene.VideoStart import VideoStart
from manim_projects.MyUsefulScene.VideoCover import VideoCover

class LastVideo(Scene):
    def construct(self):
        title = TextMobject("硬核模拟三体运动")
        title.set_color(YELLOW)
        title.scale(1.2)
        title.to_edge(UP)
        screen_rect = ScreenRectangle(height = 6).set_color(BLACK)
        screen_rect.next_to(title, DOWN)

        self.play(Write(title))
        self.play(ShowCreation(screen_rect))
        self.wait(6)

class Prefix(Scene):
    def construct(self):
        text = Title("前置知识").set_color(BLACK)
        self.play(ShowCreation(text))

        know1 = TextMobject("万有引力定律").next_to(text, DOWN, buff=1).to_edge(LEFT, buff = 1.5).set_color(BLACK)
        detail1 = TexMobject("F=\\frac{G\\times m_1m_2}{r^2}").next_to(know1, DOWN, buff=0.85).set_color(RED)
        detail12= TexMobject("G=6.67\\times 10^{-11}Nm^2/kg^2").scale(0.5).next_to(detail1, DOWN).set_color(RED)
        self.play(Write(know1), Write(detail1), Write(detail12))
        self.wait(1)

        know2 = TextMobject("匀变速直线运动").next_to(text, DOWN, buff=1).to_edge(RIGHT, buff = 1.5).set_color(BLACK)
        detail21 = TextMobject("牛二：$F=ma$").next_to(know2, DOWN, buff=0.85).set_color(RED)
        detail22 = TexMobject("v=v_0 + at").next_to(detail21, DOWN, buff=0.65).set_color(RED)
        detail23 = TexMobject("x=x_0 + v_0t + \\frac{1}{2}at^2").next_to(detail22, DOWN, buff=0.55).set_color(RED)
        self.play(Write(know2), Write(detail21), Write(detail22), Write(detail23))
        self.wait(3)