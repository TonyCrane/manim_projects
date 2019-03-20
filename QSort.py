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
        self.wait(1)
        self.color()
        self.mainidea()
        self.step1()
        self.step2()

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
            "初始化"
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
        textarrowi = Arrow(texti, data[0][8]).set_color(RED)
        textarrowj = Arrow(textj,data[0][13]).set_color(RED)
        self.TextI = VGroup(texti, textarrowi)
        self.TextJ = VGroup(textj, textarrowj)
        self.textk = TextMobject("$key=$""6").set_color(GREEN).scale(0.8).to_corner(RIGHT)
        transdata8 = data[0][8].set_color(GREEN)
        self.play(
            Write(self.TextI),
            Write(self.TextJ),
            Write(self.textk),
            Transform(data[0][8], transdata8)
        )
        transtext = TextMobject(
            "1. 将指针变量$i,j$放在数组两端,最左端的数值设为$key$"
        ).scale(0.3).next_to(self.MainIdeaText, direction=DOWN, buff=0.1).set_color(YELLOW)
        self.play(Transform(text, transtext))
        self.Step1Text = transtext

    def step2(self):
        title = TextMobject(
            "第一步操作"
        ).scale(0.8).set_color(BLUE).to_corner(TOP)
        text = TextMobject(
            "将$j$逐个向左移,直至$j < key$"
        ).scale(0.6).to_corner(DOWN).set_color(YELLOW)
        self.play(
            Write(text),
            Transform(self.title, title)
        )
        TextJ = self.TextJ.next_to(data[0][12], direction=DOWN, buff=0.2)
        self.play(
            Transform(self.TextJ, TextJ)
        )
        ajkey = TextMobject(
            "$a[j] > key$"
        ).set_color(YELLOW).next_to(TextJ, direction=RIGHT)
        self.play(Write(ajkey))