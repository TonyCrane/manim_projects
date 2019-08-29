'''
  > File Name        : BIT.py
  > Author           : Tony
  > Created Time     : 2019/08/26 17:17:21
'''

from manimlib.imports import *
from manim_projects.MyUsefulScene.VideoStart import VideoStart

class VideoTitle(VideoStart):
    CONFIG = {
        "title_name": "树状数组($Binary\ Indexed\ Tree$)",
    }


class VideoCover(Scene):
    def construct(self):
        a = list()  #a[1]~a[8] is valid
        a.append(Rectangle(height=0.667, width=1.5).move_to(DOWN*2.667+LEFT*5.25))
        for i in range(1, 9):
            a.append(a[0].copy().next_to(a[0], RIGHT, buff=1.5*(i-2)))
        t = list()  #t[1]~t[8] is valid
        for i in range(9):
            t.append(Rectangle())
        t[8] = Rectangle(height=0.667, width=12).move_to(UP*2.667)
        t[4] = Rectangle(height=0.667, width=6).move_to(UP*1.333+LEFT*3)
        t[2] = Rectangle(height=0.667, width=3).move_to(LEFT*4.5)
        t[1] = Rectangle(height=0.667, width=1.5).move_to(DOWN*1.333+LEFT*5.25)
        t[3] = t[1].copy().next_to(t[1], RIGHT, buff=1.5)
        t[5] = t[1].copy().next_to(t[3], RIGHT, buff=1.5)
        t[7] = t[1].copy().next_to(t[5], RIGHT, buff=1.5)
        t[6] = t[2].copy().next_to(t[2], RIGHT, buff=3)
        textt = list()
        for i in range(9):
            textt.append(TextMobject("\\texttt{t[}", "{id}".format(id=i), "\\texttt{]}").scale(0.8).move_to(t[i].get_right()+LEFT*1.15, aligned_edge=LEFT))
        texta = list()
        for i in range(9):
            texta.append(TextMobject("\\texttt{a[}", "{id}".format(id=i), "\\texttt{]}").scale(0.8).move_to(a[i].get_right()+LEFT*1.15, aligned_edge=LEFT))   
        l9_10 = Line(textt[1].get_top()+UP*0.17, textt[2].get_bottom()+DOWN*0.17).set_color(GREEN)
        l10_12 = Line(textt[2].get_top()+UP*0.17, textt[4].get_bottom()+DOWN*0.17).set_color(GREEN)
        l11_12 = Line(textt[3].get_top()+UP*0.17, textt[4].get_bottom()+DOWN*0.17).set_color(GREEN)
        l12_16 = Line(textt[4].get_top()+UP*0.17, textt[8].get_bottom()+DOWN*0.17).set_color(GREEN)
        l13_14 = Line(textt[5].get_top()+UP*0.17, textt[6].get_bottom()+DOWN*0.17).set_color(GREEN)
        l14_16 = Line(textt[6].get_top()+UP*0.17, textt[8].get_bottom()+DOWN*0.17).set_color(GREEN)
        l15_16 = Line(textt[7].get_top()+UP*0.17, textt[8].get_bottom()+DOWN*0.17).set_color(GREEN)
        l1_9 = Line(texta[1].get_top()+UP*0.17, textt[1].get_bottom()+DOWN*0.17).set_color([WHITE, GREEN])
        l2_10 = Line(texta[2].get_top()+UP*0.17, textt[2].get_bottom()+DOWN*0.17).set_color([WHITE, GREEN])
        l3_11 = Line(texta[3].get_top()+UP*0.17, textt[3].get_bottom()+DOWN*0.17).set_color([WHITE, GREEN])
        l4_12 = Line(texta[4].get_top()+UP*0.17, textt[4].get_bottom()+DOWN*0.17).set_color([WHITE, GREEN])
        l5_13 = Line(texta[5].get_top()+UP*0.17, textt[5].get_bottom()+DOWN*0.17).set_color([WHITE, GREEN])
        l6_14 = Line(texta[6].get_top()+UP*0.17, textt[6].get_bottom()+DOWN*0.17).set_color([WHITE, GREEN])
        l7_15 = Line(texta[7].get_top()+UP*0.17, textt[7].get_bottom()+DOWN*0.17).set_color([WHITE, GREEN])
        l8_16 = Line(texta[8].get_top()+UP*0.17, textt[8].get_bottom()+DOWN*0.17).set_color([WHITE, GREEN])

        BIT_tree = VGroup(
            *[a[i] for i in range(1, 9)], *[t[i].set_color(GREEN) for i in range(1, 9)],
            *[textt[i] for i in range(1, 9)], *[texta[i] for i in range(1, 9)],
            l1_9, l9_10, l10_12, l11_12, l12_16, l13_14, l14_16, l15_16,
            l1_9, l2_10, l3_11, l4_12, l5_13, l6_14, l7_15, l8_16
        )

        for element in BIT_tree:
            element.set_stroke(opacity=0.3)
        for i in range(1, 9):
            textt[i].set_opacity(0.3)
            texta[i].set_opacity(0.3)

        title = TextMobject("树\\ \\ 状\\ \\ 数\\ \\ 组").scale(3).set_color(BLUE).move_to(UP*0.5)
        entitle = TextMobject("\\texttt{Binary Indexed Tree}").scale(1.8).next_to(title, UP).set_color(YELLOW)
        author = TextMobject("@鹤翔万里").set_color([BLUE, YELLOW, ORANGE, RED]).next_to(title, DOWN, buff=1.2)
        
        self.add(BIT_tree)
        self.add(title)
        self.add(entitle)
        self.add(author)


class TableOfContents(Scene):
    def construct(self):
        topics = VGroup(
            TextMobject("引入问题"),
            TextMobject("前置知识\\ -\\ \\texttt{lowbit()}操作"),
            TextMobject("树状数组\\ -\\ 思想及实现"),
            TextMobject("解决问题"),
            TextMobject("树状数组的扩展应用"),
        )
        for topic in topics:
            dot = Dot(color=BLUE)
            dot.next_to(topic, LEFT)
            topic.add(dot)
        topics.arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=LARGE_BUFF
        ).move_to(LEFT)
        self.add(topics)
        self.wait()
        for i in range(len(topics)):
            self.play(
                topics[i + 1:].set_fill, {"opacity": 0.25},
                topics[:i].set_fill, {"opacity": 0.25},
                topics[i].set_fill, {"opacity": 1},
            )
            self.wait(2)


class IntroProblem(Scene):
    def construct(self):
        title = Title("引入问题").set_color(BLUE)
        problem = VGroup(
            TextMobject("给出一个长度为$n$的数组,完成以下两种操作"),
            VGroup(
                TextMobject("将第$x$个数加上$k$"),
                TextMobject("输出区间$[x,y]$内每个数的和"),
            ).arrange_submobjects(
                DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF
            ).scale(0.8)
        ).arrange_submobjects(
            DOWN, aligned_edge=ORIGIN, buff=MED_LARGE_BUFF
        )
        problem.move_to(UP*1.5)
        for topic in problem[1]:
            dot = Dot(color=BLUE)
            dot.next_to(topic, LEFT)
            topic.add(dot)

        luogu = TextMobject("题目来源：$Luogu\\ P3374$\\ 树状数组1").scale(0.4).move_to(RIGHT*3.7)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(problem), run_time=1.2)
        self.play(Write(luogu), run_time=1.2)
        self.wait(5)

        normal = TextMobject("朴素算法: ").set_color(YELLOW).scale(0.8).move_to(LEFT*4+DOWN*0.7)
        O_normal = VGroup(
            TextMobject("单点修改: ","$O(1)$"),
            TextMobject("区间查询: ","$O(n)$"),
        ).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF
        ).scale(0.8).move_to(LEFT*3+DOWN*2)
        O_normal_final = TextMobject("$O(n^2)$").set_color(RED).scale(0.8).next_to(normal, RIGHT, buff=MED_LARGE_BUFF)
        line = DashedLine(ORIGIN, DOWN*3.8)

        self.play(Write(normal))
        self.wait(0.5)
        for topic in O_normal:
            self.play(Write(topic[0]))
            self.play(FadeInFrom(topic[1], RIGHT))
            self.wait(0.2)
        self.wait(3)
        self.play(ReplacementTransform(VGroup(O_normal[0][1], O_normal[1][1]).copy(), O_normal_final))
        self.wait()
        self.play(ShowCreation(line))
        self.wait()

        bit = TextMobject("树状数组","处理: ").set_color(YELLOW).scale(0.8).move_to(RIGHT*1.8+DOWN*0.7)
        comment = TextMobject("\\texttt{Binary\\ Indexed\\ Tree}").scale(0.3).next_to(bit[0], UP, buff=0.05).set_color(YELLOW)
        O_bit = VGroup(
            TextMobject("单点修改: ","$O(\\log_2n)$"),
            TextMobject("区间查询: ","$O(\\log_2n)$"),
        ).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF
        ).scale(0.8).move_to(RIGHT*3+DOWN*2)
        O_bit_final = TextMobject("$O(n\\log_2n)$").set_color(RED).scale(0.8).next_to(bit, RIGHT, buff=MED_LARGE_BUFF)
        
        self.play(ReplacementTransform(normal.copy(), VGroup(bit, comment)))
        self.wait(0.5)
        for topic in O_bit:
            self.play(Write(topic[0]))
            self.play(FadeInFrom(topic[1], RIGHT))
            self.wait(0.2)
        self.wait(3)
        self.play(ReplacementTransform(VGroup(O_bit[0][1], O_bit[1][1]).copy(), O_bit_final))
        self.wait(5)


class PreLowbit(Scene):
    def construct(self):
        title = Title("前置知识\\ -\\ \\texttt{lowbit()}运算").set_color(BLUE)
        define = VGroup(
            TextMobject("非负整数$n$在二进制表示下","最低位1"),
            TextMobject("及其后面的0","构成的数值"),
        ).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF
        ).next_to(title, DOWN)
        define[1].move_to(LEFT*2 + UP*1.5)
        define[0][1].set_color(YELLOW)
        define[1][0].set_color(YELLOW)
        eg = TextMobject("$e.g.\\ \\mathtt{lowbit(44)=lowbit((101}$","$\\mathtt{100}$","$\\mathtt{)_2)=(}$","$\\mathtt{100}$","$\mathtt{)_2=4}$").scale(0.85).move_to(UP*0.8)
        eg[1].set_color(RED)
        eg[3].set_color(RED)

        formulars = VGroup(
            TextMobject("$\\mathtt{1\\ 0\\ 1\\ }$", "$\\mathtt{1\\ 0\\ 0}$"),
            TextMobject("$\\mathtt{0\\ 1\\ 0\\ }$", "$\\mathtt{0\\ 1\\ 1}$"),
        ).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF
        ).scale(1.2).move_to(DOWN*0.7)

        formulars2 = TextMobject("$\\mathtt{0\\ 1\\ 0\\ }$", "$\\mathtt{1\\ 0\\ 0}$").scale(1.2).move_to(formulars[1])
        curvearrow = CurvedArrow(formulars[0].get_right()+RIGHT*0.2, formulars[1].get_right()+RIGHT*0.2, angle=-TAU / 4).set_color(YELLOW)
        comment1 = TextMobject("取反", "+1").scale(0.6).set_color(YELLOW).next_to(curvearrow, RIGHT)

        self.play(Write(title))
        self.wait()
        for topic in define:
            self.play(Write(topic))
        self.wait(2)
        self.play(FadeInFromDown(eg))
        self.wait(2)
        self.play(Write(formulars[0]))
        self.wait()
        self.play(ShowCreation(curvearrow), Write(comment1[0]))
        self.play(ReplacementTransform(formulars[0].copy(), formulars[1]))
        self.wait(2)
        self.play(Write(comment1[1]))
        self.play(ReplacementTransform(formulars[1], formulars2))
        self.wait(2)

        arc = ArcBetweenPoints(formulars[0].get_left()+LEFT*0.2, formulars[1].get_left()+LEFT*0.2).set_color(YELLOW)
        comment2 = TextMobject("按位与($\\&$)").set_color(RED).scale(0.6).next_to(arc, LEFT)

        formular3 = TextMobject("$\\mathtt{0\\ 0\\ 0\\ }$", "$\\mathtt{1\\ 0\\ 0}$").scale(1.2).move_to(formulars.get_center())
        formular3[1].set_color(RED)

        self.play(ShowCreation(arc), Write(comment2))
        self.play(
            formulars[0][1].set_color, RED,
            formulars2[1].set_color, RED
        )
        self.wait()
        self.play(
            FadeOut(arc), 
            FadeOut(comment1),
            FadeOut(curvearrow),
            FadeOut(comment2),
            ReplacementTransform(VGroup(formulars[0], formulars2), formular3)
        )
        self.wait(5)

        self.remove(eg, formular3)
        self.wait(2)

        formu = TexMobject("\\mathtt{lowbit}(n)","&=","n\\&","(", "\\sim n+1", ")\\\\","&=","n\\&", "-n").scale(1.2).move_to(DOWN*1.4)
        formu2 = TexMobject("\\sim n+1","=","-n","\\ \\ (\\sim \\text{表示取反})").move_to(UP*0.2)

        self.play(*[
                Write(formu[i])
                for i in range(6)
            ],
            run_time=1
        )
        self.wait()
        self.play(FadeInFromDown(formu2))
        self.wait()
        self.play(ReplacementTransform(VGroup(formu[1], formu[2]).copy(), VGroup(formu[6], formu[7])))
        self.wait()
        self.play(ReplacementTransform(formu2[0].copy(), formu[4].copy()))
        self.play(ReplacementTransform(formu2[2].copy(), formu[8]))
        self.play(
            formu[7].set_color, RED,
            formu[8].set_color, RED
        )
        self.play(ShowCreationThenDestructionAround(VGroup(formu[7], formu[8])))
        self.wait(5)





##------Time Line------##
# 19.8.26 Have an idea
# 19.8.27 Write article
# 19.8.29 Finish 2 main scenes
# 19.8.30 Finish 1 main scene and video cover