'''
  > File Name        : dp_knapsack.py
  > Author           : Tony
  > Created Time     : 2019/01/30 16:23:28
'''

from big_ol_pile_of_manim_imports import *
from manim_projects.StudyManim import VideoStart

array_fini = np.array([
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ['0', '0', '3', '3', '3', '3', '3', '3', '3'],
    ['0', '0', "3", "4", "4", '7', '7', '7', '7'],
    ['0', '0', '3', '4', '5', '7', '8', '9', '9'],
    ['0', '0', '3', '4', '5', '7', '8', '9', '10']
])

class VideoTitle(VideoStart):
    CONFIG = {
        "title_name"    : "动态规划-01背包问题",
    }

class IntroProblem(Scene):
    def construct(self):
        text = TextMobject(
            "现给出一容量为 $V$ 的背包，和 $N$ 件物品，每件物品体积为 $v[i]$ ，价\\\\值为 $c[i]$ ，将几件物品装入背包内，使物品总体积不超过背包体积，并且\\\\使总价值最大。求这个最大价值?（数据见下）",
        )
        text.scale(0.8)
        text.to_corner(UP + LEFT)
        self.play(Write(text))
        data = TexMobject(
            "V = 8\\ ,\\ N = 4\\\\"
        )
        data.scale(0.8)
        data_num = Matrix(
            [["i", 1, 2, 3, 4],
            ["v", 2, 3, 4, 5],
            ["w", 3, 4, 5, 6]]
        )
        data_num.scale(0.8)
        data_num.next_to(data, direction=DOWN)
        self.play(
            FadeIn(data),
            FadeIn(data_num)
        )
        self.wait(4)
        self.play(
            FadeOut(text),
            FadeOut(data),
            FadeOut(data_num)
        )
    
class TwoDArraySolve(Scene):
    def construct(self):
        self.IntroPara()
        self.CreateArray()
        self.FirstRow()
        self.SecondRow()
        self.finish()

    def IntroPara(self):
        para = TextMobject(
            "用", "$F[i][j]$","表示面对前$i$种物品，背包容量为$j$时的最大价值",
            tex_to_color_map={"$F[i][j]$": RED}
        )
        para.scale(0.7)
        self.play(Write(para))
        self.wait()
        trans_para = TextMobject(
            "用", "$F[i][j]$","表示面对前$i$种物品，背包容量为$j$时的最大价值",
            tex_to_color_map={"$F[i][j]$": RED}
        )
        trans_para.scale(0.3)
        trans_para.to_corner(UP + LEFT)
        self.play(Transform(para, trans_para))
        self.wait()
    
    def CreateArray(self):
        array = Matrix(
            [["i/j", "1", "2", "3", "4", "5", "6", "7", "8"],
             ["1", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["2", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["3", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["4", "0", "0", "0", "0", "0", "0", "0", "0"]]
        )
        title = TextMobject("初始化数组$F[\\ ][\\ ]$", tex_to_color_map={"初始化数组$F[\\ ][\\ ]$": YELLOW})
        title.to_corner(UP)
        title.scale(0.8)
        self.play(Write(title))
        self.play(Write(array))
        self.wait()
        self.array = array
        self.title = title
    
    def FirstRow(self):
        array = self.array
        transtitle = TextMobject(
            "更新第一行最大价值"
        )
        transtitle.scale(0.8).to_corner(UP).set_color(YELLOW)
        under = TextMobject(
            "当$i=1$时，如果背包可以放下第一个物品，则放入，更新最大价值"
        )
        under.scale(0.7).to_corner(DOWN)

        self.play(
            Transform(self.title, transtitle),
            Write(under)
        )
        for i in range(11, 18):
            trans = TextMobject("3").move_to(array[0][i])
            self.play(
                Transform(array[0][i], trans),
                run_time=0.2
            )
        under1 = TextMobject(
            "当$i=1$时，如果背包可以放下第一个物品，则放入，更新最大价值"
        ).scale(0.3).to_corner(RIGHT + UP)
        self.play(
            Transform(under, under1)
        )
        self.wait()
        self.under1 = under1
    
    def SecondRow(self):
        array  = self.array
        under1 = self.under1
        transtitle = TextMobject("更新第二行最大价值")
        transtitle.scale(0.8).to_corner(UP).set_color(YELLOW)
        under = TextMobject(
            "基于第一行结果和背包容量，可以选或不选或只选第二件，取最大价值"
        ).scale(0.7).to_corner(DOWN)
        under2 = TextMobject(
            "基于第一行结果和背包容量，可以选或不选或只选第二件，取最大价值"
        ).scale(0.3).to_corner(UP + RIGHT)
        under2.next_to(under1, direction=DOWN, buff=0.1)

        self.play(
            Transform(self.title, transtitle),
            Write(under)
        )
        
        for i in range(19, 27):
            if (i - 18 < 3):
                rect = SurroundingRectangle(array[0][i])
                arrow = Arrow(array[0][i - 9].get_bottom(), array[0][i].get_top())
                old = array[0][i - 9].copy()
                trans = old.move_to(array[0][i])
                self.play(
                    ShowCreation(rect),
                    ShowCreation(arrow)
                )
                self.play(
                    Transform(array[0][i], trans),
                    run_time = 0.2
                )
                self.play(
                    FadeOut(rect),
                    FadeOut(arrow)
                )
            else:
                rect = SurroundingRectangle(array[0][i])
                arrow1 = Arrow(array[0][i - 9].get_bottom(), array[0][i].get_top())
                if i - 12 > 9:
                    arrow2 = Arrow(array[0][i - 12].get_bottom(), array[0][i].get_top())
                else:
                    arrow2 = Arrow(array[0][i - 12].get_right(), array[0][i].get_top())
                text = TextMobject("+4").scale(0.7).move_to(arrow2).set_color(RED)
                trans = TextMobject(array_fini[2][i - 18]).move_to(array[0][i])
                
                self.play(
                    ShowCreation(rect),
                    ShowCreation(arrow1),
                    ShowCreation(arrow2),
                    FadeIn(text)
                )
                self.play(
                    Transform(array[0][i], trans),
                    run_time = 0.2
                )
                self.play(
                    FadeOut(rect),
                    FadeOut(arrow1),
                    FadeOut(arrow2),
                    FadeOut(text)
                )

        self.play(
            Transform(under, under2)
        )
        self.wait()
        self.under2 = under2

    def finish(self):
        array  = self.array
        under2 = self.under2
        transtitle = TextMobject("更新剩余部分")
        transtitle.scale(0.8).to_corner(UP).set_color(YELLOW)
        under = TextMobject(
            "基于前一行结果和背包容量，取最大价值（同上一步）"
        ).scale(0.7).to_corner(DOWN)
        under3 = TextMobject(
            "基于前一行结果和背包容量，取最大价值（同上一步）"
        ).scale(0.3).to_corner(UP + RIGHT)
        under3.next_to(under2, direction=DOWN, buff=0.1)

        self.play(
            Transform(self.title, transtitle),
            Write(under)
        )
        
        for i in range(28, 36):
            if (i - 28 < 4):
                rect = SurroundingRectangle(array[0][i])
                arrow = Arrow(array[0][i - 9].get_bottom(), array[0][i].get_top())
                old = array[0][i - 9].copy()
                trans = old.move_to(array[0][i])
                self.play(
                    ShowCreation(rect),
                    ShowCreation(arrow)
                )
                self.play(
                    Transform(array[0][i], trans),
                    run_time = 0.2
                )
                self.play(
                    FadeOut(rect),
                    FadeOut(arrow)
                )
            else:
                rect = SurroundingRectangle(array[0][i])
                arrow1 = Arrow(array[0][i - 9].get_bottom(), array[0][i].get_top())
                if i - 12 > 19:
                    arrow2 = Arrow(array[0][i - 12].get_bottom(), array[0][i].get_top())
                else:
                    arrow2 = Arrow(array[0][i - 12].get_right(), array[0][i].get_top())
                text = TextMobject("+5").scale(0.7).move_to(arrow2).set_color(RED)
                trans = TextMobject(array_fini[3][i - 27]).move_to(array[0][i])
                
                self.play(
                    ShowCreation(rect),
                    ShowCreation(arrow1),
                    ShowCreation(arrow2),
                    FadeIn(text)
                )
                self.play(
                    Transform(array[0][i], trans),
                    run_time = 0.2
                )
                self.play(
                    FadeOut(rect),
                    FadeOut(arrow1),
                    FadeOut(arrow2),
                    FadeOut(text)
                )

        self.play(
            Transform(under, under2)
        )
        self.wait()