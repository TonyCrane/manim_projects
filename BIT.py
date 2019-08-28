'''
  > File Name        : BIT.py
  > Author           : Tony
  > Created Time     : 2019/08/26 17:17:21
'''

from manimlib.imports import *
from manim_projects.MyUsefulScene.VideoStart import VideoStart

class VideoTitle(VideoStart):
    CONFIG = {
        "title_name": "树状数组($Binary\ Indexed\ Trees$)",
    }


class VideoCover(Scene):
    def construct(self):
        pass


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
        comment = TextMobject("\\texttt{Binary\\ Indexed\\ Trees}").scale(0.3).next_to(bit[0], UP, buff=0.05).set_color(YELLOW)
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
            TextMobject("$\\mathtt{1\\ 0\\ 1\\ 1\\ 0\\ 0}$"),
            TextMobject("$\\mathtt{0\\ 1\\ 0\\ 0\\ 1\\ 1}$"),
        ).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF
        ).scale(1.2).move_to(DOWN*0.7)

        formulars2 = TextMobject("$\\mathtt{0\\ 1\\ 0\\ 1\\ 0\\ 0}$").scale(1.2).move_to(formulars[1])

        self.play(Write(title))
        self.wait()
        for topic in define:
            self.play(Write(topic))
        self.wait(2)
        self.play(FadeInFromDown(eg))
        self.wait(2)
        self.play(Write(formulars[0]))
        self.wait()
        self.play(ReplacementTransform(formulars[0].copy(), formulars[1]))
        self.wait(2)
        self.play(ReplacementTransform(formulars[1], formulars2))
        self.wait(2)





##------Time Line------##
# 19.8.26 Have an idea