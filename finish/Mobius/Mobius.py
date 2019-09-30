'''
  > File Name        : Mobius.py
  > Author           : Tony
  > Created Time     : 2019/08/12 15:29:13
'''

from manimlib.imports import *
from manim_projects.MyUsefulScene.VideoStart import VideoStart


class VideoTitle(VideoStart):
    CONFIG = {
        "title_name": "莫比乌斯反演",
    }


class VideoCover(Scene):
    def construct(self):
        tex1 = VGroup(
            TexMobject("\\mu(d)=\\begin{cases}1&d=1\\\\(-1)^k&d=\\prod_{i=1}^kp_i\\ (p_i\\text{互质})\\\\0&\\text{其他情况}\\end{cases}").scale(0.8),
            TexMobject("\\sum_{d|n}\\mu(d)=[n=1]"),
        ).arrange_submobjects(
            DOWN, aligned_edge=ORIGIN, buff=MED_SMALL_BUFF
        ).set_opacity(0.1)
        tex2 = VGroup(
            TexMobject("F(n)=\\sum_{d|n}f(d)"),
            TexMobject("\\Downarrow").scale(1.2),
            TexMobject("f(n)=\\sum_{d|n}\\mu(d)F(\\frac{n}{d})").set_color(RED),
        ).scale(1.2).arrange_submobjects(
            DOWN, aligned_edge=ORIGIN, buff=1.3
        ).set_opacity(0.25).move_to(LEFT*3.1)
        tex3 = VGroup(
            TexMobject("f(n)=\\sum_{n|d}\\mu(\\frac{d}{n})F(d)").set_color(RED),
            TexMobject("\\Uparrow").scale(1.2),
            TexMobject("F(n)=\\sum_{n|d}f(d)"),
        ).scale(1.2).arrange_submobjects(
            DOWN, aligned_edge=ORIGIN, buff=1.3
        ).set_opacity(0.25).move_to(RIGHT*3.1)

        title = TextMobject("莫\\ 比\\ 乌\\ 斯\\ 反\\ 演").scale(2.3).set_color(BLUE).move_to(UP*0.5)
        entitle = TextMobject("\\texttt{Möbius Inversion}").scale(2.1).next_to(title, UP).set_color(YELLOW)
        author = TextMobject("@鹤翔万里").set_color([BLUE, YELLOW, ORANGE, RED]).next_to(title, DOWN, buff=1.2)

        self.add(tex1)
        self.add(tex2)
        self.add(tex3)
        self.add(title)
        self.add(entitle)
        self.add(author)


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
            TextMobject("给定$n,m$,求在$1\\leqslant x\\leqslant n, 1\\leqslant y\\leqslant m$范围内且"),
            TextMobject("$gcd$", "$(x,y)$","为", "质数", "的$(x,y)$有多少对"),
        )
        problem[1][0].set_color(YELLOW)
        problem[1][1].set_color(YELLOW)
        problem[1][3].set_color(RED)
        problem.arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF
        )
        problem[0].move_to(RIGHT + UP*0.5)
        problem.move_to(UP*1.5)

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
    def construct(self):
        title = Title("积性函数与完全积性函数").set_color(BLUE)
        self.play(Write(title))

        line = DashedLine(title.get_bottom(), DOWN*3)
        self.play(ShowCreation(line))

        text1 = TextMobject("积性函数").set_color(YELLOW).scale(0.8).move_to(UP*2.3+LEFT*3.2)
        self.play(Write(text1))
        self.wait()
        jixing = TextMobject("定义域为正整数的算术函数$f(x)$满足\\\\","$\\begin{cases}f(1)=1\\\\f(pq)=f(p)\\cdot f(q)\\ \\ \\text{p,q互质}\\end{cases}$").scale(0.6).next_to(text1, DOWN)
        self.play(FadeInFromDown(jixing))
        self.wait(3)
        tex1 = TexMobject("\\varphi(n) &- \\text{欧拉函数}\\\\ \\mu(n) &- \\text{莫比乌斯函数}\\\\ gcd(n,k) &- \\text{k一定的最大公约数}").scale(0.8).next_to(jixing, DOWN, buff=MED_LARGE_BUFF).set_color(GREEN)
        self.play(Write(tex1))
        self.wait(4)

        text2 = TextMobject("完全积性函数").set_color(YELLOW).scale(0.8).move_to(UP*2.3+RIGHT*3.2)
        Text1 = text1.copy()
        self.play(Transform(Text1, text2))
        self.wait()
        jixing1 = jixing.copy()
        wanquan = TextMobject("定义域为正整数的算术函数$f(x)$满足\\\\","$\\begin{cases}f(1)=1\\\\f(ab)=f(a)\\cdot f(b)\\ \\ \\text{a,b任意}\\end{cases}$").scale(0.6).next_to(text2, DOWN)
        self.play(Transform(jixing1, wanquan))
        self.wait(3)
        tex2 = TexMobject("1(n) &- \\text{值恒为1(恒等函数)}\\\\ \\epsilon(n) &- \\text{即[n=1](元函数)}\\\\ Id(n) &- \\text{值为n(单位函数)}").scale(0.8).next_to(wanquan, DOWN, buff=MED_LARGE_BUFF).set_color(GREEN)
        self.play(Write(tex2))
        self.wait(5)
        self.remove(line, text1, jixing, tex1, Text1, jixing1, tex2)

        title2 = Title("狄利克雷卷积($*$)").set_color(BLUE)
        self.play(Transform(title, title2))

        diri = TextMobject("对于两算术函数$f,g$,定义","$(f*g)$", "$(n)$", "$=\\sum_{d|n}f(d)g(\\frac{n}{d})$").next_to(title, DOWN)
        diri[1].set_color(RED)
        diri[2].set_color(RED)
        diri[3].set_color(RED)
        comment = TextMobject("$(n)$一般省略不写").scale(0.5).set_color(GREY).next_to(diri[2], DOWN, buff=0.05)
        self.play(Write(diri), FadeIn(comment))
        self.wait(2)
        
        tit = TextMobject("运算律：").set_color(RED).scale(1.1).move_to(LEFT*5+UP)
        self.play(Write(tit))
        tex = VGroup(
            TexMobject("\\text{交换律}f*g=g*f"),
            TexMobject("\\text{结合律}(f*g)*h=f*(g*h)"),
            TexMobject("\\text{分配律}f*(g+h)=f*g+f*h"),
            TexMobject("f=f*\\epsilon = \\epsilon *f"),
        ).scale(0.9).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=0.4
        ).set_color(YELLOW).next_to(diri, DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(tex))
        self.wait(5)

        self.remove(diri, comment, tit, tex)
        title3 = Title("简要证明莫比乌斯反演").set_color(BLUE)
        self.play(Transform(title, title3))
        xingzhi = TexMobject("\\sum_{d|n}\\mu(d)=[n=1]").move_to(UP*1.8+LEFT*4)
        self.play(FadeInFromDown(xingzhi))
        self.wait(2)
        tex3 = TexMobject("\\mu *1=\\epsilon").move_to(xingzhi).set_color(YELLOW)
        self.play(Transform(xingzhi, tex3))
        self.wait(2)

        F = TexMobject("F(n)=\\sum_{d|n}f(d)").move_to(UP*1.8+RIGHT*4)
        self.play(FadeInFromDown(F))
        self.wait(2)
        tex4 = TexMobject("F=f*1").move_to(F).set_color(YELLOW)
        self.play(Transform(F, tex4))
        self.wait(2)

        tex5 = TexMobject("F*\\mu =f*", "1*\\mu").move_to(UP)
        copyF = F.copy()
        self.play(Transform(copyF, tex5))
        self.wait(0.5)
        transtex5 = TexMobject("(1*\\mu )").move_to(copyF[1])
        self.play(Transform(copyF[1], transtex5))
        self.wait(0.5)
        transtex51 = TexMobject("\\epsilon").move_to(UP+RIGHT)
        self.play(Transform(copyF[1], transtex51), Transform(xingzhi.copy(), transtex51))
        self.wait()

        tex6 = TexMobject("=f").next_to(copyF[1], RIGHT, buff=0.05)
        self.play(Write(tex6))
        self.wait()

        finish = TexMobject("f=F*\\mu").scale(1.2).move_to(DOWN*0.5)
        copyG = VGroup(copyF,tex6).copy()
        self.play(Transform(copyG, finish))
        self.wait(2)
        transfinish = TexMobject("f(n)=\\sum_{d|n}\\mu(d)F(\\frac{n}{d})").scale(1.2).move_to(DOWN*0.5).set_color(RED)
        self.play(Transform(copyG, transfinish))
        self.wait(5)



class SolveProblem(Scene):
    def construct(self):
        define = VGroup(
            TextMobject("$f(d)$为$gcd(i,j)=d$的个数"),
            TextMobject("$F(n)$为$gcd(i,j)=d$或$d$的倍数的个数"),
        ).arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=0.25
        )
        self.play(Write(define))
        self.wait(2)
        transdef = define.copy().scale(0.5).to_corner(UL)
        self.play(Transform(define, transdef))
        self.wait()
        deftex = VGroup(
            TexMobject("f(d)=\\sum_{i=1}^n\\sum_{j=1}^m[gcd(i,j)=d]"),
            TexMobject("F(x)=\\sum_{x|d}f(d)=\\frac{n}{x} \\cdot \\frac{m}{x}"),
        ).arrange_submobjects(
            DOWN, aligned_edge=RIGHT, buff=0.25
        ).scale(0.6).to_corner(UR).set_color(YELLOW)
        self.play(Transform(define.copy(), deftex))
        self.wait(2)

        solve = TexMobject("Ans &= \\sum_{p\\in prim}\\sum_{i=1}^n\\sum_{j=1}^m[gcd(i,j)=p]\\\\ &=\\sum_{p\\in prim}", "f(p)", "\\\\ &= ","\\sum_{T=1}^n\\sum_{t|T, t\\in prim}\\mu(\\frac{T}{t})\\cdot \\frac{n}{T} \\cdot \\frac{m}{T}").move_to(LEFT)
        self.play(Write(solve[0]))
        self.play(Write(solve[1]))
        self.wait(2)
        transsolve = TexMobject("\\sum_{p|d}\\mu(\\frac{d}{p})F(d)").move_to(solve[1], aligned_edge=LEFT)
        self.play(Transform(solve[1], transsolve))
        self.wait(2)
        transsolve2 = TexMobject("\\sum_{d=1}^{\\frac{n}{p}}\\mu(d) \\frac{n}{dp} \\cdot \\frac{m}{dp}").move_to(solve[1], aligned_edge=LEFT)
        self.play(Transform(solve[1], transsolve2))
        self.wait(2)
        self.play(Write(solve[2]), Write(solve[3]))
        self.wait(2)

        transsolve3 = TexMobject("\\sum_{T=1}^n\\frac{n}{T}\\cdot \\frac{m}{T} (\\sum_{t|T}\\mu(\\frac{T}{t}))").move_to(solve[3], aligned_edge=LEFT).set_color(RED)
        self.play(Transform(solve[3], transsolve3))
        self.wait(6)

        self.clear()
        text = TextMobject("具体实现代码请参考\\\\", "https://www.luogu.org/problemnew/solution/P2257")
        text[1].set_color(ORANGE).scale(0.9)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOutAndShiftDown(text))
        self.wait()


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
# 19.8.14 Finish all scenes