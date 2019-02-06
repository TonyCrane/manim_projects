'''
  > File Name        : dp_knapsack.py
  > Author           : Tony
  > Created Time     : 2019/01/30 16:23:28
'''

from big_ol_pile_of_manim_imports import *
from manim_projects.StudyManim import VideoStart

array_fini = np.array([
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "3", "3", "3", "3", "3", "3", "3"],
    ["0", "0", "3", "4", "4", "7", "7", "7", "7"],
    ["0", "0", "3", "4", "5", "7", "8", "9", "9"],
    ["0", "0", "3", "4", "5", "7", "8", "9", "10"]
])

class VideoTitle(VideoStart):
    CONFIG = {
        "title_name"    : "动态规划-01背包问题",
    }

class RedSurroundingRectangle(SurroundingRectangle):
    CONFIG = {
        "color" : RED,
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
            ["c", 3, 4, 5, 6]]
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
        self.Finish()
        self.ShowAnswer()
        self.Out()

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
        self.para = para
    
    def CreateArray(self):
        array = Matrix(
            [["i/j", "0", "1", "2", "3", "4", "5", "6", "7", "8"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["2", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["3", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["4", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]
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
        for i in range(23, 30):
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
        self.fade1 = under
    
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
        
        for i in range(32, 40):
            if (i - 30 < 4):
                rect = SurroundingRectangle(array[0][i])
                arrow = Arrow(array[0][i - 10].get_bottom(), array[0][i].get_top())
                old = array[0][i - 10].copy()
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
                arrow1 = Arrow(array[0][i - 10].get_bottom(), array[0][i].get_top())
                arrow2 = Arrow(array[0][i - 13].get_bottom(), array[0][i].get_top())
                text = TextMobject("+4").scale(0.7).move_to(arrow2).set_color(RED)
                trans = TextMobject(array_fini[2][i - 31]).move_to(array[0][i])
                
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
        self.fade2 = under

    def Finish(self):
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
        
        for i in range(42, 50):
            if (i - 40 < 5):
                rect = SurroundingRectangle(array[0][i])
                arrow = Arrow(array[0][i - 10].get_bottom(), array[0][i].get_top())
                old = array[0][i - 10].copy()
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
                arrow1 = Arrow(array[0][i - 10].get_bottom(), array[0][i].get_top())
                arrow2 = Arrow(array[0][i - 14].get_bottom(), array[0][i].get_top())
                text = TextMobject("+5").scale(0.7).move_to(arrow2).set_color(RED)
                trans = TextMobject(array_fini[3][i - 41]).move_to(array[0][i])
                
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

        for i in range(52, 60):
            if (i - 50 < 6):
                rect = SurroundingRectangle(array[0][i])
                arrow = Arrow(array[0][i - 10].get_bottom(), array[0][i].get_top())
                old = array[0][i - 10].copy()
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
                arrow1 = Arrow(array[0][i - 10].get_bottom(), array[0][i].get_top())
                arrow2 = Arrow(array[0][i - 15].get_bottom(), array[0][i].get_top())
                text = TextMobject("+6").scale(0.7).move_to(arrow2).set_color(RED)
                trans = TextMobject(array_fini[4][i - 51]).move_to(array[0][i])
                
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
            Transform(under, under3)
        )
        self.wait()
        self.under3 = under3
        self.fade3 = under
    
    def ShowAnswer(self):
        array  = self.array
        under3 = self.under3
        transtitle = TextMobject("查找结果($N=4,\\ V=8$)")
        transtitle.scale(0.8).to_corner(UP).set_color(YELLOW)
        under = TextMobject(
            "$F[N][V]$即为结果"
        ).scale(0.7).to_corner(DOWN)
        under4 = TextMobject(
            "$F[N][V]$即为结果"
        ).scale(0.3).to_corner(UP + RIGHT)
        under4.next_to(under3, direction=DOWN, buff=0.1)
        
        rect_n = SurroundingRectangle(array[0][50])
        rect_v = SurroundingRectangle(array[0][9])
        rect_ans = RedSurroundingRectangle(array[0][59])
        arrow1 = Arrow(array[0][50].get_right(), array[0][59].get_left())
        arrow2 = Arrow(array[0][9].get_bottom(), array[0][59].get_top())

        self.play(
            Transform(self.title, transtitle),
            Write(under)
        )
        self.play(
            ShowCreation(rect_n),
            ShowCreation(rect_v)
        )
        self.play(
            ShowCreation(arrow1),
            ShowCreation(arrow2)
        )
        self.play(
            ShowCreation(rect_ans)
        )
        self.play(
            FadeOut(rect_n),
            FadeOut(rect_v),
            FadeOut(arrow1),
            FadeOut(arrow2)
        )
        self.play(
            Transform(under, under4)
        )
        answer = TextMobject(
            "最大价值为$F[4][8]=10$"
        ).set_color(YELLOW).scale(0.7).to_corner(DOWN)
        self.play(Write(answer))
        self.wait()
        self.play(FadeOut(rect_ans))
        self.under4 = under4
        self.answer = answer
        self.fade4 = under
    
    def Out(self):
        self.play(
            FadeOut(self.para),
            FadeOut(self.array),
            FadeOut(self.title),
            FadeOut(self.array),
            FadeOut(self.fade1),
            FadeOut(self.fade2),
            FadeOut(self.fade3),
            FadeOut(self.fade4),
            FadeOut(self.answer)
        )

class TwoDArrayCode(Scene):
    def construct(self):
        dp = TextMobject("状态转移方程\\\\", "$F[i][j] = max(F[i-1][j], F[i-1][j-v[i]]+c[i])$")
        dp[0].set_color(RED)
        self.play(
            Write(dp[0])
        )
        self.play(
            FadeIn(dp[1])
        )
        self.wait(3)
        self.play(
            FadeOut(dp)
        )
        title = TextMobject("二维数组代码")
        title.set_color(YELLOW)
        title.scale(1.2)
        title.to_edge(UP)
        screen_rect = ScreenRectangle(height = 6)
        screen_rect.next_to(title, DOWN)

        self.play(Write(title))
        self.play(ShowCreation(screen_rect))
        self.wait(6)

class TwoDArrayDetail(Scene):
    def construct(self):
        title = TextMobject("再详细看一下二维数组递推方法").set_color(ORANGE).to_edge(UP)
        array = Matrix(
            [
                ["3", "3", "3", "3", "3"],
                [" ", " ", " ", " ", " "],
                ["3", "4", "4", "7", "7"]
            ]
        ).scale(1.3)
        rect1 = SurroundingRectangle(array[0][0])
        rect2 = SurroundingRectangle(array[0][4])
        rect3 = RedSurroundingRectangle(array[0][14])
        arrow1 = Arrow(array[0][0].get_bottom(), array[0][14].get_top())
        arrow2 = Arrow(array[0][4].get_bottom(), array[0][14].get_top())
        text = TextMobject("+4").scale(0.7).move_to(arrow1).set_color(RED)

        trans_array = Matrix(
            [
                ["F[i-1][j-v[i]]", " ", "F[i-1][j]"],
                [" ", " ", " "],
                [" ", " ", "F[i][j]"]
            ]
        )
        trans_rect1 = SurroundingRectangle(trans_array[0][0])
        trans_rect2 = SurroundingRectangle(trans_array[0][2])
        trans_rect3 = RedSurroundingRectangle(trans_array[0][8])
        trans_arrow1 = Arrow(trans_array[0][0].get_bottom(), trans_array[0][8].get_top())
        trans_arrow2 = Arrow(trans_array[0][2].get_bottom(), trans_array[0][8].get_top())
        trans_text   = TextMobject("+c[i]").scale(0.7).move_to(trans_arrow1).set_color(RED)
        self.play(Write(title))
        self.play(FadeIn(array))
        self.play(
            ShowCreation(rect1),
            ShowCreation(rect2),
            ShowCreation(rect3),
            ShowCreation(arrow1),
            ShowCreation(arrow2),
            Write(text)
        )
        self.wait()
        self.play(
            FadeOut(rect1),
            FadeOut(rect2),
            FadeOut(rect3),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(text),
            Transform(array, trans_array)
        )
        self.play(
            ShowCreation(trans_rect1),
            ShowCreation(trans_rect2),
            ShowCreation(trans_rect3),
            ShowCreation(trans_arrow1),
            ShowCreation(trans_arrow2),
            Write(trans_text)
        )
        self.wait(2)
        self.play(
            FadeOut(array),
            FadeOut(trans_rect1),
            FadeOut(trans_rect2),
            FadeOut(trans_rect3),
            FadeOut(trans_arrow1),
            FadeOut(trans_arrow2),
            FadeOut(trans_text)
        )
        self.play(
            FadeOutAndShiftDown(title)
        )
        self.wait()

class TwoDToOneD(Scene):
    def construct(self):
        title = TextMobject("但，使用二位数组会增加空间复杂度，可能会导致MLE").to_corner(UP).set_color(YELLOW)
        text  = TextMobject("我们可以将二维数组降为一位来节省空间").next_to(title, DOWN)
        text2 = TextMobject("仍需要两层循环，一层列举物品，一层列举容量").next_to(text, DOWN)
        dp    = TextMobject("$F[j] = max(F[j], F[j - v[i]] + c[i])$").scale(1.2).set_color(ORANGE)
        self.play(
            Write(title),
            Write(text),
            Write(text2),
        )
        self.play(
            FadeInFromDown(dp)
        )
        self.wait(3)
        self.play(
            FadeOut(title),
            FadeOut(text),
            FadeOut(text2),
            FadeOut(dp)
        )
        self.wait()

class TryOneDArray(Scene):
    def construct(self):
        array = Matrix(
            [
                ["i", "0", "1", "2", "3", "4", "5", "6", "7", "8"],
                ["F[i]", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
            ]
        )
        title = TextMobject("第一次更新").scale(0.8).to_corner(UP).set_color(YELLOW)
        self.play(
            Write(title),
            Write(array)
        )
        for i in range(13, 20):
            trans = TextMobject("3").move_to(array[0][i])
            self.play(Transform(array[0][i], trans), run_time=0.3)
        
        trans_title = TextMobject("第二次更新").scale(0.8).to_corner(UP).set_color(YELLOW)
        self.play(Transform(title, trans_title))
        under = TextMobject("每一个位置的结果都由上一次更新后的本位置和v[i]前的位置决定").scale(0.7).to_corner(DOWN)
        self.play(Write(under))
        
        for i in range(14, 18):
            if i <= 16:
                if i <= 15:
                    trans = TextMobject("4").move_to(array[0][i])
                else:
                    trans = TextMobject("7").move_to(array[0][i])
                rect  = SurroundingRectangle(array[0][i])
                arrow = Arrow(array[0][i - 3].get_right(), array[0][i].get_left())
                txt = TextMobject("+4").next_to(arrow, DOWN).set_color(RED)
                self.play(
                    ShowCreation(rect),
                    ShowCreation(arrow),
                    Write(txt)
                )
                self.play(Transform(array[0][i], trans), run_time=0.3)
                self.play(
                    FadeOut(rect),
                    FadeOut(arrow),
                    FadeOut(txt)
                )
            else:
                trans = TextMobject("8").move_to(array[0][i])
                rect  = SurroundingRectangle(array[0][i])
                arrow = Arrow(array[0][i - 3].get_right(), array[0][i].get_left())
                txt   = TextMobject("+4").next_to(arrow, DOWN).set_color(RED)
                self.play(
                    ShowCreation(rect),
                    ShowCreation(arrow),
                    Write(txt)
                )
                self.play(Transform(array[0][i], trans), run_time=0.3)
                self.wait()

                rect2 = RedSurroundingRectangle(array[0][i - 3])
                trans_under = TextMobject("但，", "这里", "的数是本轮才更新的，不能再+4，影响了结果").scale(0.7).to_corner(DOWN)
                arrow2 = Arrow(trans_under[1].get_top(), rect2.get_bottom())
                self.play(
                    Transform(under, trans_under),
                    ShowCreation(rect2),
                    ShowCreation(arrow2)
                )
                self.wait()
                self.play(
                    FadeOut(rect2),
                    FadeOut(arrow2),
                    FadeOut(txt),
                    FadeOut(rect),
                    FadeOut(arrow)
                )
        
        self.play(
            FadeOut(array),
            FadeOut(title),
            FadeOut(under)
        )
        self.wait()

class OneDArraySolve(Scene):
    def construct(self):
        array = Matrix(
            [
                ["i", "0", "1", "2", "3", "4", "5", "6", "7", "8"],
                ["F[i]", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
            ]
        )
        title = TextMobject("每次更新要倒序").scale(0.8).to_corner(UP).set_color(YELLOW)
        self.play(
            Write(title),
            Write(array)
        )
        under = TextMobject("具体步骤省略").scale(0.8).to_corner(DOWN)
        self.play(Write(under))

        for i in range(1, 5):
            for j in [8, 7, 6, 5, 4, 3, 2]:
                k = j + 11
                trans = TextMobject(array_fini[i][j]).move_to(array[0][k])
                self.play(
                    Transform(array[0][k], trans),
                    run_time = 0.3
                )
        rect = RedSurroundingRectangle(array[0][19])
        trans_title = TextMobject("查找结果").scale(0.8).to_corner(UP).set_color(YELLOW)
        trans_under = TextMobject("结果仍是$F[8] = 10$").scale(0.8).to_corner(DOWN)
        self.play(
            Transform(title, trans_title)
        )
        self.play(
            ShowCreation(rect),
            Transform(under, trans_under),
        )
        self.wait()
        self.play(
            FadeOut(array),
            FadeOut(title),
            FadeOut(under),
            FadeOut(rect)
        )
        self.wait()

class CompletePack(Scene):
    def construct(self):
        title = TextMobject("再来看一下顺推的情形").scale(0.8).to_corner(UP).set_color(YELLOW)
        array = Matrix(
            [
                ["i", "0", "1", "2", "3", "4", "5", "6", "7", "8"],
                ["F[i]", "0", "0", "3", "4", "4", "7", "8", "11", "11"]
            ]
        )
        rect  = SurroundingRectangle(array[0][17])
        arrow = Arrow(array[0][14].get_right(), array[0][17].get_left())
        txt   = TextMobject("+4").next_to(arrow, DOWN).set_color(RED)
        self.play(
            Write(title),
            Write(array),
            ShowCreation(rect),
            ShowCreation(arrow),
            Write(txt)
        )
        under = TextMobject("如果此处再次+4，则取了2次此物品，即每件物品可以取多件，这就是\\\\", "完全背包").scale(0.8).to_corner(DOWN)
        under[1].set_color(RED)
        self.play(Write(under))
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(array),
            FadeOut(rect),
            FadeOut(arrow),
            FadeOut(txt),
            FadeOut(under)
        )
        self.wait()

class OneDArrayCode(Scene):
    def construct(self):
        title = TextMobject("一维数组代码片段")
        title.set_color(YELLOW)
        title.scale(1.2)
        title.to_edge(UP)
        screen_rect = ScreenRectangle(height = 6)
        screen_rect.next_to(title, DOWN)

        self.play(Write(title))
        self.play(ShowCreation(screen_rect))
        self.wait(6)

class EndScene(Scene):
    def construct(self):
        title = TextMobject("更多算法可参考我的博客\\\\", "https://tony031218.github.io/")
        title[1].set_color(ORANGE)
        self.play(
            Write(title[0])
        )
        self.play(
            FadeInFromDown(title[1])
        )
        self.wait(4)
        self.play(
            FadeOut(title)
        )

'''
  > Finished Time     : 2019/02/04 13:12:18
  > Video Address     : https://www.bilibili.com/video/av42621196
'''