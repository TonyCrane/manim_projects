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
        # screen_rect = ScreenRectangle(height = 6)
        # screen_rect.next_to(title, DOWN)

        self.play(Write(title))
        # self.play(ShowCreation(screen_rect))
        self.wait(6)

class QsortTime(Scene):
    def construct(self):
        title = TextMobject("下面来对时间复杂度进行分析").set_color(YELLOW).scale(1.2)
        self.play(Write(title));
        self.wait(1)
        self.remove(title);
        self.best()
        self.worst()
        self.ave()
    
    def best(self):
        self.title = Title("最好情况").set_color(BLUE)
        self.play(Write(self.title));

        text = TextMobject(
            "最好情况发生在整", "个数组被分成两段长度相等的子数组时,递推式如下:"
        ).scale(0.7).next_to(self.title, DOWN)
        self.play(Write(text))
        tex = TexMobject(
            "T(n) =\\begin{cases} \\Theta(1)& \\text{n=1} \\\\ 2T(\\frac{n}{2})+\\Theta(n)& \\text{n>1} \\end{cases}"
        ).next_to(text, DOWN).set_color(YELLOW)
        self.play(FadeIn(tex));
        self.wait(1)
        text2 = TextMobject(
            "经过数学推导可得:"
        ).next_to(text[0], DOWN, buff=2)
        tex2 = TexMobject(
            "T(n)=\\Theta(n\\log_2 n)"
        ).scale(1.3).next_to(tex, DOWN, buff=1.5).set_color(RED)
        self.play(Write(text2))
        self.play(Write(tex2))
        self.wait(2.5)
        self.remove(text, tex, text2, tex2)

    def worst(self):
        transtitle = Title("最坏情况").set_color(BLUE)
        self.play(Transform(self.title, transtitle));

        text = TextMobject(
            "最坏情况发生在整", "个数组被分成长度为$0$和$n-1$的子数组时,递推式如下:"
        ).scale(0.7).next_to(self.title, DOWN)
        self.play(Write(text))
        tex = TexMobject(
            "T(n) =\\begin{cases} \\Theta(1)& \\text{n=1} \\\\ T(n-1)+\\Theta(n)& \\text{n>1} \\end{cases}"
        ).next_to(text, DOWN).set_color(YELLOW)
        self.play(FadeIn(tex));
        self.wait(1)
        text2 = TextMobject(
            "经过数学推导可得:"
        ).next_to(text[0], DOWN, buff=2)
        tex2 = TexMobject(
            "T(n)=\\Theta(n^2)"
        ).scale(1.3).next_to(tex, DOWN, buff=1.5).set_color(RED)
        self.play(Write(text2))
        self.play(Write(tex2))
        self.wait(2.5)
        self.remove(text, tex, text2, tex2)
    
    def ave(self):
        transtitle = Title("平均情况").set_color(BLUE)
        self.play(Transform(self.title, transtitle));

        text = TextMobject(
            "实际上", ",除最坏情况外,均会产生深度为$\Theta(\log_2 n)$的递归树,\\\\而每层均是$\Theta(n)$"
        ).scale(0.8).next_to(self.title, DOWN)
        self.play(Write(text))
        text2 = TextMobject(
            "所以:"
        ).next_to(text[0], DOWN, buff=1)
        tex2 = TexMobject(
            "T(n)=\\Theta(n\\log_2 n)"
        ).scale(1.3).next_to(text, DOWN, buff=1.5).set_color(RED)
        self.play(Write(text2))
        self.play(Write(tex2))
        self.wait(2.5)
        self.remove(text, text2, tex2)
    

class QsortTLE(Scene):
    def construct(self):
        text = TextMobject(
            "但是,这样做对于某些数据会非常卡,导致$TLE$"
        ).scale(1.2)
        text2 = TextMobject(
            "所以我们要进行一些优化"
        ).next_to(text, DOWN).set_color(YELLOW)
        self.play(Write(text))
        self.play(Write(text2))
        self.wait(6)

class QsortOptimization(Scene):
    def construct(self):
        self.opt1()
        self.opt2()
        self.opt3()
        self.opt4()

    def opt1(self):
        self.title = Title("I.\\ 减少交换次数").set_color(BLUE)
        self.play(Write(self.title))
        self.wait(1.25)
        text = TextMobject(
            "在左右分别找到需要交换的元素后,如果$i$和$j$相遇则与基准元素交换,否则将$a[i]$与$a[j]$交换,也可达到目的,同时将交换次数缩短了一半"
        ).scale(0.7).next_to(self.title, DOWN)
        self.play(Write(text))
        self.wait(6)
        self.remove(text)
    
    def opt2(self):
        transtitle = Title("II.\\ 随机化").set_color(BLUE)
        self.play(Transform(self.title, transtitle))
        self.wait(1.25)
        text = TextMobject(
            "快速排序的最差时间复杂度很高,而平均和最好几乎一样,为了使时间复杂度达到期望值,可以每次","随机", "选一个数作为基准数"
        ).scale(0.7).next_to(self.title, DOWN)
        text[1].set_color(YELLOW)
        self.play(Write(text))
        self.wait(6)
        self.remove(text)

    def opt3(self):
        transtitle = Title("III.\\ 小区间插入排序").set_color(BLUE)
        self.play(Transform(self.title, transtitle))
        self.wait(1.25)
        text = TextMobject(
            "在一个小区间内,使用插入排序比快速排序递归效率高。因此,可以在区间长度", "小于$10$", "后改为", "插入排序"
        ).scale(0.7).next_to(self.title, DOWN)
        text[1].set_color(YELLOW)
        text[3].set_color(YELLOW)
        self.play(Write(text))
        self.wait(6)
        self.remove(text)
    
    def opt4(self):
        transtitle = Title("IV.\\ 聚拢重复元素").set_color(BLUE)
        self.play(Transform(self.title, transtitle))
        self.wait(1.25)
        text = TextMobject(
            "在$j$向前移动时,每次遇到和基准元素", "相同的元素", ",就将其与前方", "第一个异于基准元素的元素", "交换位置,然后继续移动。如果在$i$之前没有找到任何一个异于基准元素的元素,说明此时$i$与$j$之间已经全部都是与基准元素相同的","重复元素","实现了重复元素的聚拢"
        ).scale(0.7).next_to(self.title, DOWN)
        text[1].set_color(YELLOW)
        text[3].set_color(YELLOW)
        text[5].set_color(YELLOW)
        text2 = TextMobject(
            "由于代码相对复杂,在此不展示,可以前往简介中[4]查看完整代码"
        ).scale(0.5).next_to(text, DOWN, buff=1).set_color(ORANGE)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeInFromDown(text2))
        self.wait(5)
        self.remove(text, text2)
        self.play(FadeOutAndShiftDown(self.title), run_time=0.5)

class CppSTLSort(Scene):
    def construct(self):
        self.stlsort()
        self.timecompare()

    def stlsort(self):
        text = TextMobject(
            "C++语言的STL为我们设计好了一个sort()函数(algorithm头中)\\\\它混合了插入排序与堆排序,将时间复杂度稳定在了","$\Theta(n\log_2 n)$"
        ).scale(0.8)
        text[1].set_color(RED)
        self.play(Write(text))
        self.wait(4)
        self.remove(text)
    
    def timecompare(self):
        title = Title("时间对比(供参考)").set_color(BLUE)
        comment = TextMobject("数据来自up主Luogu P1177前4个测试点的时间").scale(0.4).next_to(title, DOWN).to_edge(RIGHT)
        self.play(Write(title), Write(comment))
        tab = TexMobject(
            "\\begin{tabular}{ccccccc} \\hline 优化情况& \\#1& \\#2& \\#3& \\#4\\\\ \\hline 无& 3ms& TLE& TLE& TLE\\\\ I.& 3ms& 46ms& TLE& TLE\\\\ I.II.& 3ms& 45ms& 120ms& 1086ms\\\\ I.II.III.& 3ms& 31ms& 117ms& 668ms\\\\ I.II.III.IV.& 3ms& 42ms& 52ms& 28ms\\\\ sort()& 3ms& 39ms& 26ms& 24ms\\\\ \\hline \\end{tabular}"
        ).next_to(title, DOWN, buff=1)
        self.play(Write(tab))
        self.wait(7)
        self.play(FadeOutAndShiftDown(title), FadeOutAndShiftDown(comment), FadeOutAndShiftDown(tab), run_time=0.5)

class VideoEnd(Scene):
    def construct(self):
        title = Title("参考(链接放在视频简介里)").set_color(RED)
        text1 = TextMobject("[1] Introduction to Algorithms(Third Edition)").scale(0.8).next_to(title, DOWN, buff=0.7).to_corner(LEFT)
        text2 = TextMobject("[2] Quicksort\\ -\\ Wikipedia").scale(0.8).next_to(text1, DOWN).to_corner(LEFT)
        text3 = TextMobject("[3] 快速排序算法\\ -\\ 百度百科").scale(0.8).next_to(text2, DOWN).to_corner(LEFT)
        text4 = TextMobject("[4] 快速排序题解\\ -\\ Adam\\_Ding的博客").scale(0.8).next_to(text3, DOWN).to_corner(LEFT)
        text5 = TextMobject("[5] STL sort源码剖析\\ -\\ imAkaka的博客").scale(0.8).next_to(text4, DOWN).to_corner(LEFT)

        self.play(FadeInFromDown(title))
        self.play(Write(text1), Write(text2), Write(text3), Write(text4), Write(text5))
        self.wait(4)
        self.play(
            FadeOutAndShiftDown(title),
            FadeOutAndShiftDown(text1),
            FadeOutAndShiftDown(text2),
            FadeOutAndShiftDown(text3),
            FadeOutAndShiftDown(text4),
            FadeOutAndShiftDown(text5),
            run_time=0.2
        )

        title2 = TextMobject("更多算法可参考我的博客\\\\", "https://tony031218.github.io/")
        title2[1].set_color(ORANGE)
        title2[1].scale(1.3)
        self.play(
            Write(title2[0])
        )
        self.play(
            FadeInFromDown(title2[1])
        )
        self.wait(4)
        self.play(
            FadeOut(title2)
        )
        self.wait(2)


'''
  > Finished Time     : 2019/05/24 16:22:18
  > Video Address     :
'''