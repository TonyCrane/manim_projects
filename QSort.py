'''
  > File Name        : QSort.py
  > Author           : Tony
  > Created Time     : 2019/03/13 14:18:39
'''

from big_ol_pile_of_manim_imports import *
from manim_projects.MyUsefulScene.VideoStart import VideoStart

class VideoTitle(VideoStart):
    CONFIG = {
        "title_name"    : "快速排序",
    }

data = Matrix(
    [["i", "0", "1", "2", "3", "4", "5"],
     ["a[i]", "6", "2", "7", "3", "9", "8"]]
)
for i in range(0, 8):
    data[0][i].set_color(DARK_BROWN)

class IntroProblem(Scene):
    def construct(self):
        problem = TextMobject(
            "现给出一数组，对其中的元素按从小到大排序"
        ).scale(0.8).to_corner(TOP)
        self.play(Write(problem))
        self.play(
            FadeIn(data),
            run_time=0.5
        )
        self.wait(3)

class QsortSolve(Scene):
    def construct(self):
        self.add(data)
        self.color()
        self.mainidea()
        self.step1()

    def color(self):
        white = TextMobject(
            "未排序"
        ).scale(0.4).set_color(WHITE).to_corner(LEFT + UP)
        green = TextMobject(
            "基准数"
        ).scale(0.4).set_color(GREEN).next_to(white, direction=DOWN, buff=SMALL_BUFF)
        red = TextMobject(
            "排序后"
        ).scale(0.4).set_color(RED).next_to(green, direction=DOWN, buff=SMALL_BUFF)
        grey = TextMobject(
            "闲置"
        ).scale(0.4).set_color(GREY).next_to(red, direction=DOWN, buff=SMALL_BUFF)
        self.play(
            FadeIn(white),
            FadeIn(green),
            FadeIn(red),
            FadeIn(grey),
            run_time=0.3
        )
        
    def mainidea(self):
        title = TextMobject(
            "主要思路"
        ).scale(0.8).set_color(BLUE).to_corner(TOP)
        text = TextMobject(
            "选取一个数，把比它小的放到左边，大的放到右边，并对左右两边同样处理"
        ).scale(0.6).to_corner(DOWN).set_color(GOLD)
        self.play(Write(title), Write(text))
        transtext = TextMobject(
            "选取一个数，把比它小的放到左边，大的放到右边，并对左右两边同样处理"
        ).scale(0.3).to_corner(RIGHT + UP).set_color(GOLD)
        self.play(Transform(text, transtext))
        self.title = title
        self.MainIdeaText = transtext

    def step1(self):
        title = TextMobject(
            "第一次操作"
        ).scale(0.8).set_color(BLUE).to_corner(TOP)
        text = TextMobject(
            "1. 将指针变量$i,j$放在数组两端,最左端的数值设为$key$"
        ).scale(0.6).to_corner(DOWN).set_color(YELLOW)
        self.play(
            Write(text),
            Transform(self.title, title)
        )
        texti = TextMobject("$i$").set_color(RED).next_to(data[0][8], direction=DOWN, buff=1.25)
        textj = TextMobject("$j$").set_color(RED).next_to(data[0][13],direction=DOWN, buff=1.25)
        textk = TextMobject("$key=$""6").set_color(GREEN).scale(0.8).to_corner(RIGHT)
        transdata8 = data[0][8].set_color(GREEN)
        self.play(
            Write(texti),
            Write(textj),
            Write(textk),
            Transform(data[0][8], transdata8)
        )
        self.title = title
        