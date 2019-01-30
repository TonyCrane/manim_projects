'''
  > File Name        : dp_knapsack.py
  > Author           : Tony
  > Created Time     : 2019/01/30 16:23:28
'''

from big_ol_pile_of_manim_imports import *
from manim_projects.StudyManim import VideoStart

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
        title.scale(0.7)
        self.play(Write(title))
        self.play(Write(array))
        self.wait()
        self.play(FadeOut(title))
        self.array = array
    
    def FirstRow(self):
        array = self.array
        title = TextMobject(
            "当$i=1$时，如果背包可以放下第一个物品，则放入，更新最大价值"
        )
        title.scale(0.7)
        title.to_corner(UP)
        title.set_color(YELLOW)
        # trans = [TextMobject("3") for i in [2, 3, 4, 5, 6, 7, 8]]
        # for i in [2, 3, 4, 5, 6, 7, 8]:
        #     trans[i].move_to(array[0][i + 10])
        trans_12 = TextMobject("3").move_to(self.array[0][11])
        trans_13 = TextMobject("3").move_to(self.array[0][12])
        trans_14 = TextMobject("3").move_to(self.array[0][13])
        trans_15 = TextMobject("3").move_to(self.array[0][14])
        trans_16 = TextMobject("3").move_to(self.array[0][15])
        trans_17 = TextMobject("3").move_to(self.array[0][16])
        trans_18 = TextMobject("3").move_to(self.array[0][17])
        self.play(Write(title))
        self.play(
            Transform(array[0][11], trans_12),
            Transform(array[0][12], trans_13),
            Transform(array[0][13], trans_14),
            Transform(array[0][14], trans_15),
            Transform(array[0][15], trans_16),
            Transform(array[0][16], trans_17),
            Transform(array[0][17], trans_18)
        )
        self.wait()
        self.play(FadeOut(title))
