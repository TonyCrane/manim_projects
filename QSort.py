'''
  > File Name        : QSort.py
  > Author           : Tony
  > Created Time     : 2019/03/13 14:18:39
'''

from big_ol_pile_of_manim_imports import *
from manim_projects.MyUsefulScene.VideoStart import VideoStart


class VideoTitle(VideoStart):
    CONFIG = {
        "title_name": "快速排序",
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
        self.step3()
        self.step4()
        self.step5()

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
        self.play(
            FadeIn(white),
            FadeIn(green),
            FadeIn(red),
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
        self.wait(1)

    def step1(self):
        title = TextMobject(
            "初始化"
        ).scale(0.8).set_color(BLUE).to_corner(TOP)
        text = TextMobject(
            "0. 将指针变量$i,j$放在数组要排序部分两端,设$a[i]=key$"
        ).scale(0.6).to_corner(DOWN).set_color(YELLOW)
        self.play(
            Write(text),
            Transform(self.title, title)
        )
        texti = TextMobject("$i$").set_color(RED).next_to(
            data[0][8], direction=DOWN, buff=1.25)
        textj = TextMobject("$j$").set_color(RED).next_to(
            data[0][13], direction=DOWN, buff=1.25)
        textarrowi = Arrow(texti, data[0][8]).set_color(RED)
        textarrowj = Arrow(textj, data[0][13]).set_color(RED)
        self.TextI = VGroup(texti, textarrowi)
        self.TextJ = VGroup(textj, textarrowj)
        self.textk = TextMobject("$key=$""6").set_color(
            GREEN).scale(0.8).to_corner(RIGHT)
        transdata8 = data[0][8].set_color(GREEN)
        self.play(
            Write(self.TextI),
            Write(self.TextJ),
            Write(self.textk),
            Transform(data[0][8], transdata8),
            run_time=2
        )
        transtext = TextMobject(
            "0. 将指针变量$i,j$放在数组要排序部分两端,设$a[i]=key$"
        ).scale(0.3).next_to(self.MainIdeaText, direction=DOWN, buff=0.1).set_color(YELLOW)
        self.play(Transform(text, transtext))
        self.Step1Text = transtext
        self.wait(1)

    def step2(self):
        title = TextMobject(
            "第一步操作"
        ).scale(0.8).set_color(BLUE).to_corner(TOP)
        text = TextMobject(
            "1. 将$j$逐个向左移,直至$a[j] < key$,交换$a[i]$与$a[j]$"
        ).scale(0.6).to_corner(DOWN).set_color(YELLOW)
        self.play(
            Write(text),
            Transform(self.title, title)
        )
        TextJ = self.TextJ.next_to(data[0][13], direction=DOWN, buff=0.2)
        self.play(
            Transform(self.TextJ, TextJ)
        )
        ajkey = TextMobject(
            "$a[j] > key$"
        ).scale(0.7).set_color(YELLOW).next_to(TextJ, direction=RIGHT)
        self.play(Write(ajkey))
        self.play(FadeOut(ajkey))
        TextJ = self.TextJ.next_to(data[0][12], direction=DOWN, buff=0.2)
        self.play(
            Transform(self.TextJ, TextJ)
        )
        ajkey.next_to(TextJ, direction=RIGHT)
        self.play(Transform(self.TextJ, TextJ))
        self.play(Write(ajkey))
        self.play(FadeOut(ajkey))

        TextJ = self.TextJ.next_to(data[0][11], direction=DOWN, buff=0.2)
        ajKey = TextMobject(
            "$a[j] < key$"
        ).scale(0.7).set_color(GOLD).next_to(TextJ, direction=RIGHT)
        self.play(Transform(self.TextJ, TextJ))
        self.play(Write(ajKey))
        self.play(FadeOut(ajKey))

        self.play(Swap(data[0][8], data[0][11]))

        transtext = TextMobject(
            "1. 将$j$逐个向左移,直至$a[j] < key$,交换$a[i]$与$a[j]$"
        ).scale(0.3).next_to(self.Step1Text, direction=DOWN, buff=0.1).set_color(YELLOW)
        self.play(Transform(text, transtext))
        self.Step2Text = transtext
        self.wait(1)

    def step3(self):
        title = TextMobject(
            "第二步操作"
        ).scale(0.8).set_color(BLUE).to_corner(TOP)
        text = TextMobject(
            "2. 将$i$逐个向右移,直至$a[i] > key$,交换$a[j]$与$a[i]$"
        ).scale(0.6).to_corner(DOWN).set_color(YELLOW)
        self.play(
            Write(text),
            Transform(self.title, title)
        )
        TextI = self.TextI.next_to(data[0][11], direction=DOWN, buff=0.2)
        self.play(
            Transform(self.TextI, TextI)
        )
        aikey = TextMobject(
            "$a[i] < key$"
        ).scale(0.7).set_color(YELLOW).next_to(TextI, direction=LEFT)
        self.play(Write(aikey))
        self.play(FadeOut(aikey))

        TextI = self.TextI.next_to(data[0][9], direction=DOWN, buff=0.2)
        self.play(
            Transform(self.TextI, TextI)
        )
        aikey.next_to(TextI, direction=LEFT)
        self.play(Transform(self.TextI, TextI))
        self.play(Write(aikey))
        self.play(FadeOut(aikey))

        TextI = self.TextI.next_to(data[0][10], direction=DOWN, buff=0.2)
        aiKey = TextMobject(
            "$a[i] > key$"
        ).scale(0.7).set_color(GOLD).next_to(TextI, direction=LEFT)
        self.play(Transform(self.TextI, TextI))
        self.play(Write(aiKey))
        self.play(FadeOut(aiKey))

        self.play(Swap(data[0][8], data[0][10]))

        transtext = TextMobject(
            "2. 将$i$逐个向右移,直至$a[i] > key$,交换$a[j]$与$a[i]$"
        ).scale(0.3).next_to(self.Step2Text, direction=DOWN, buff=0.1).set_color(YELLOW)
        self.play(Transform(text, transtext))
        self.Step3Text = transtext
        self.wait(1)

    def step4(self):
        title = TextMobject(
            "第一轮后续操作"
        ).scale(0.8).set_color(BLUE).to_corner(TOP)
        text = TextMobject(
            "3. 重复$1,2$步,直至$i = j$,确定下$key$位置"
        ).scale(0.6).to_corner(DOWN).set_color(YELLOW)
        self.play(
            Write(text),
            Transform(self.title, title)
        )

        TextJ = self.TextJ.next_to(data[0][10], direction=DOWN, buff=0.2)
        self.play(
            Transform(self.TextJ, TextJ)
        )
        ajkey = TextMobject(
            "$a[j] > key$"
        ).scale(0.7).set_color(YELLOW).next_to(TextJ, direction=RIGHT)
        self.play(Write(ajkey))
        self.play(FadeOut(ajkey))

        TextJ = self.TextJ.next_to(self.TextI, direction=RIGHT, buff=0.1)
        self.play(
            Transform(self.TextJ, TextJ)
        )
        iej = TextMobject(
            "$i = j$"
        ).scale(0.7).set_color(GOLD).next_to(TextJ, direction=RIGHT)
        self.play(Write(iej))
        self.play(FadeOut(iej))

        transkey = data[0][8].set_color(RED)
        self.play(Transform(data[0][8], transkey))

        transtext = TextMobject(
            "3. 重复$1,2$步,直至$i = j$,确定下$key$位置"
        ).scale(0.3).next_to(self.Step3Text, direction=DOWN, buff=0.1).set_color(YELLOW)
        self.play(Transform(text, transtext))
        self.Step4Text = transtext
        self.wait(1)

    def step5(self):
        title = TextMobject(
            "递归处理左右两侧数组"
        ).scale(0.8).set_color(BLUE).to_corner(TOP)
        text = TextMobject(
            "4. 对没有排好序的子数组执行操作$0,1,2,3$,直至排好整个数组"
        ).scale(0.6).to_corner(DOWN).set_color(YELLOW)
        self.play(
            Write(text),
            Transform(self.title, title)
        )

        self.play(FadeOut(self.TextI), FadeOut(self.TextJ))
        TextI = self.TextI.next_to(data[0][11], direction=DOWN, buff=0.2)
        TextJ = self.TextJ.next_to(data[0][9], direction=DOWN, buff=0.2)
        transk = TextMobject("3").set_color(
            GREEN).scale(0.8).move_to(self.textk[4])
        transdata11 = data[0][11].set_color(GREEN)
        self.play(
            Transform(self.textk[4], transk),
            Transform(data[0][11], transdata11),
            Write(TextI),
            Write(TextJ),
            run_time=2
        )

        ajKey = TextMobject(
            "$a[j] < key$"
        ).scale(0.7).set_color(GOLD).next_to(TextJ, direction=RIGHT)
        self.play(Write(ajKey))
        self.play(FadeOut(ajKey), Swap(data[0][11], data[0][9]))

        aikey = TextMobject(
            "$a[i] < key$"
        ).scale(0.7).set_color(YELLOW).next_to(TextI, direction=LEFT)
        self.play(Write(aikey))
        self.play(FadeOut(aikey))
        TextI = self.TextI.next_to(self.TextJ, direction=LEFT, buff=0.1)
        iej = TextMobject(
            "$i = j$"
        ).scale(0.7).set_color(GOLD).next_to(TextI, direction=LEFT)
        self.play(
            Transform(self.TextI, TextI),
            Write(iej)
        )
        transdata9 = data[0][9].set_color(RED)
        transdata11 = data[0][11].set_color(RED)
        self.play(
            Transform(data[0][9], transdata9),
            Transform(data[0][11], transdata11),
            FadeOut(iej),
            FadeOut(self.TextI),
            FadeOut(self.TextJ)
        )
        self.wait(1)

        TextI = self.TextI.next_to(data[0][10], direction=DOWN, buff=0.2)
        TextJ = self.TextJ.next_to(data[0][13], direction=DOWN, buff=0.2)
        transk = TextMobject("7").set_color(
            GREEN).scale(0.8).move_to(self.textk[4])
        transdata10 = data[0][10].set_color(GREEN)
        self.play(
            Transform(self.textk[4], transk),
            Transform(data[0][10], transdata10),
            Write(TextI),
            Write(TextJ)
        )
        ajkey = TextMobject(
            "$a[j] > key$"
        ).scale(0.7).set_color(YELLOW).next_to(TextJ, direction=RIGHT)
        self.play(Write(ajkey))
        self.play(FadeOut(ajkey))
        TextJ = self.TextJ.next_to(data[0][12], direction=DOWN, buff=0.2)
        self.play(
            Transform(self.TextJ, TextJ)
        )
        ajkey = TextMobject(
            "$a[j] > key$"
        ).scale(0.7).set_color(YELLOW).next_to(TextJ, direction=RIGHT)
        self.play(Write(ajkey))
        self.play(FadeOut(ajkey))
        TextJ = self.TextJ.next_to(TextI, direction=RIGHT, buff=0.1)
        iej = TextMobject(
            "$i = j$"
        ).scale(0.7).set_color(GOLD).next_to(TextI, direction=LEFT)
        self.play(
            Transform(self.TextJ, TextJ),
            Write(iej)
        )

        transdata10 = data[0][10].set_color(RED)
        self.play(
            Transform(data[0][10], transdata10),
            FadeOut(iej),
            FadeOut(self.TextI),
            FadeOut(self.TextJ)
        )
        self.wait(1)

        TextI = self.TextI.next_to(data[0][12], direction=DOWN, buff=0.2)
        TextJ = self.TextJ.next_to(data[0][13], direction=DOWN, buff=0.2)
        transk = TextMobject("9").set_color(
            GREEN).scale(0.8).move_to(self.textk[4])
        transdata12 = data[0][12].set_color(GREEN)
        self.play(
            Transform(self.textk[4], transk),
            Transform(data[0][12], transdata12),
            Write(TextI),
            Write(TextJ)
        )
        ajKey = TextMobject(
            "$a[j] < key$"
        ).scale(0.7).set_color(GOLD).next_to(TextJ, direction=RIGHT)
        self.play(Write(ajKey))
        self.play(FadeOut(ajKey), Swap(data[0][12], data[0][13]))

        transdata12 = data[0][12].set_color(RED)
        transdata13 = data[0][13].set_color(RED)
        self.play(
            Transform(data[0][12], transdata12),
            Transform(data[0][13], transdata13),
            FadeOut(self.TextI),
            FadeOut(self.TextJ),
            FadeOut(self.textk)
        )
        self.wait(1)

        transtext = TextMobject(
            "4. 对没有排好序的子数组执行操作$0,1,2,3$,直至排好整个数组"
        ).scale(0.3).next_to(self.Step4Text, direction=DOWN, buff=0.1).set_color(YELLOW)
        self.play(Transform(text, transtext), FadeOut(self.title))
        self.Step5Text = transtext
        self.wait(2)

class QsortCode(Scene):
    def construct(self):
        title = TextMobject("所以我们可以轻松地写出代码").set_color(YELLOW).scale(0.9).to_edge(UP)
        screen_rect = ScreenRectangle(height = 6)
        screen_rect.next_to(title, DOWN)

        self.play(Write(title))
        self.play(ShowCreation(screen_rect))
        self.wait(6)

# class QsortTLE(Scene):
#     def construct(self):
