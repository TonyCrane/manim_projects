'''
  > File Name        : Mobius.py
  > Author           : Tony
  > Created Time     : 2019/08/12 15:29:13
'''

from manimlib.imports import *
from manim_projects.MyUsefulScene.VideoStart import VideoStart

#TODO, make audio text
#TODO, see what the Title class is
#TODO, check is there a function called get_..._by_tex()

class VideoTitle(VideoStart):
    CONFIG = {
        "title_name": "莫比乌斯反演",
    }


class TableOfContents(Scene):
    def construct(self):
        topics = VGroup(
            TextMobject("引入问题"),
            TextMobject("介绍莫比乌斯函数($\\mu(d)$)"),
            TextMobject("介绍莫比乌斯反演"),
            TextMobject("介绍狄利克雷卷积并证明莫比乌斯反演"),
            TextMobject("解决问题"),
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
            TextMobject("给定$n,m$,求在$1\\leqslant x,y\\leqslant n$范围内且"),
            TextMobject("$gcd$", "$(x,y)$","为", "质数", "的$(x,y)$有多少对"),
        )
        problem[1][0].set_color(YELLOW)
        problem[1][1].set_color(YELLOW)
        problem[1][3].set_color(RED)
        problem.arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF
        )
        problem[0].move_to(RIGHT + UP*0.5)
        problem.move_to(UP*1.5+LEFT*0.3)

        comment = TextMobject("最大公约数").scale(0.3).set_color(YELLOW).next_to(problem[1][0], UP, buff=0.05)
        luogu = TextMobject("题目来源：$Luogu\\ P2257$\\ YY的GCD").scale(0.5).move_to(RIGHT*3)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(problem), run_time=1.2)
        self.play(Write(luogu), run_time=1.2)
        self.play(FadeIn(comment))
        self.wait(5)


class MobiusFunction(Scene):
    def construct(self):
        title = Title("莫比乌斯函数\\ $\\mu(d)$").set_color(BLUE)
        self.play(Write(title))

        func = TexMobject("\\mu(d)=\\begin{cases}1&d=1\\\\(-1)^k&d=\\prod_{i=1}^kp_i\\ (p_i\\text{互质})\\\\0&\\text{其他情况}\\end{cases}")
        self.play(Write(func))
        self.wait(3)
        transfunc = TexMobject("\\mu(d)=\\begin{cases}1&d=1\\\\(-1)^k&d=\\prod_{i=1}^kp_i\\ (p_i\\text{互质})\\\\0&\\text{其他情况}\\end{cases}").scale(0.6).move_to(UP*1.5+LEFT*3)
        self.play(Transform(func, transfunc))

        line = DashedLine(title.get_bottom(), DOWN*3)
        self.play(ShowCreation(line))

        title2 = TextMobject("性质：").scale(0.9).move_to(UP*2+RIGHT).set_color(RED)
        tex = TexMobject("\\sum_{d|n}\\mu(d)=\\begin{cases}1&n=1\\\\0&n\\neq 1\\end{cases}").move_to(UP*1+RIGHT*3)
        self.play(Write(title2))
        self.play(Write(tex))

        comment1 = TextMobject("//$\\sum_{d|n}$指对于$n$的所有因子$d$进行代入求和").scale(0.5).set_color(DARK_GREY).move_to(LEFT*3+DOWN)
        arrow = Arrow(comment1.get_top()+RIGHT, tex.get_left()+DOWN*0.5, stroke_width=3, max_tip_length_to_length_ratio=3).set_color(DARK_GREY)
        self.play(Write(comment1), ShowCreation(arrow))
        self.wait(1)

        comment = TextMobject("$\\begin{cases}1&n=1\\\\0&n\\neq 1\\end{cases}$","也可记作[n=1]").scale(0.5).next_to(tex, DOWN)
        self.play(Write(comment))
        tex2 = TexMobject("\\sum_{d|n}\\mu(d)=[n=1]").set_color(YELLOW).next_to(comment, DOWN, buff=0.5)
        group = VGroup(tex, comment)
        self.wait(2)
        self.play(Transform(group.copy(), tex2))
        self.wait(4)


class MobiusInversion(Scene):
    def construct(self):
        title = Title("莫比乌斯反演").set_color(BLUE)
        self.play(Write(title))

        tex1 = VGroup(
            TexMobject("\\text{设两函数}F(x),f(x)").scale(0.8),
            TexMobject("F(n)=\\sum_{d|n}f(d)"),
            TexMobject("\\Downarrow").scale(1.2),
            TexMobject("f(n)=\\sum_{d|n}\\mu(d)F(\\frac{n}{d})").set_color(YELLOW),
        ).scale(1.2).arrange_submobjects(
            DOWN, aligned_edge=ORIGIN, buff=MED_SMALL_BUFF
        )
        for tex in tex1:
            self.play(Write(tex))
        
        self.wait(4)
        transtex1 = tex1.copy().scale(0.8).move_to(LEFT*3+UP*0.3)
        self.play(Transform(tex1, transtex1))
        line = DashedLine(title.get_bottom(), DOWN*3)
        self.play(ShowCreation(line))

        title2 = TextMobject("另一形式：").scale(0.9).move_to(UP*2.2+RIGHT*1.3).set_color(RED)
        self.play(Write(title2))
        tex2 = VGroup(
            TexMobject("F(n)=\\sum_{n|d}f(d)"),
            TexMobject("\\Downarrow").scale(1.2),
            TexMobject("f(n)=\\sum_{n|d}\\mu(\\frac{d}{n})F(d)").set_color(YELLOW),
        ).scale(1.2).arrange_submobjects(
            DOWN, aligned_edge=ORIGIN, buff=MED_SMALL_BUFF
        ).scale(0.8).move_to(RIGHT*3)
        comment = TextMobject("如何使用最后再说").scale(0.5).set_color(GREY).move_to(RIGHT*4+DOWN*3)
        self.wait()
        self.play(Transform(tex1.copy(), tex2))
        self.play(Write(comment))
        self.wait(4)


class DirichletProduct(Scene):
    pass


class ProveMobiusInversion(Scene):
    pass


class SolveProblem(Scene):
    pass


class CodeBlock(Scene):
    pass


class EndScene(Scene):
    def construct(self):
        title = Title("参考(链接在评论区置顶)").set_color(RED)
        topics = VGroup(
            TextMobject("[\\ 1\\ ]","\\ \\ Möbius inversion formula\\ -\\ Wikipedia"),
            TextMobject("[\\ 2\\ ]","\\ \\ Dirichlet convolution\\ -\\ Wikipedia"),
            TextMobject("[\\ 3\\ ]","\\ \\ Möbius function\\ -\\ Wikipedia"),
            TextMobject("[\\ 4\\ ]","\\ \\ 杜教筛\\ -\\ peng-ym的博客"),
            TextMobject("[\\ 5\\ ]","\\ \\ 莫比乌斯反演\\ -\\ peng-ym的博客"),
        ).scale(0.8)

        topics.arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF
        ).move_to(LEFT)
        
        for topic in topics:
            topic[0].set_color(BLUE)

        self.play(FadeInFromDown(title))
        self.play(Write(topics))
        self.wait(4)

        self.play(
            FadeOut(title),
            FadeOutAndShiftDown(topics),
            run_time=0.5
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


##------Time Line------##
# 19.8.12 Create and finish 3 scenes
# 19.8.13 Finish 3 scenes and make a detailed content