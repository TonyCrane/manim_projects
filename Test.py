from manimlib.imports import *
from manim_projects.tony_useful.imports import *
from random import randint

'''
这个文件中是群友问问题时我写的测试代码(2020.02.03开始)
一些目的和效果已经通过文档字符串的形式给出
'''

class Test0(Scene):
    def construct(self):
        circle = Circle(radius=3)
        poly = []
        for i in range(3, 11):
            po = Polygon(
                *[
                    UP * np.sin(j * 2 * PI / i) + RIGHT * np.cos(j * 2 * PI / i)
                    for j in range(i)
                ]
            )
            poly.append(po.scale(3, about_point=ORIGIN))
        self.play(ShowCreation(circle))
        self.play(ShowCreation(poly[0]))
        self.wait()
        for i in range(1, 8):
            self.play(Transform(poly[0], poly[i]))
            self.wait()
        self.wait(2)

class Test1(Scene):
    '''Matrix类中间元素的下标布局'''
    def construct(self):
        mat = Matrix([['0', '-1', '2'], ['1', '0', '12'], ['3', '2', 'x']])
        self.add(mat)
        debugTeX(self, mat[0])

class Test2(Scene):
    '''使用\tt调TextMobject打字机字体'''
    def construct(self):
        text = VGroup(
            TextMobject("\\tt UR=np.array([ 1, 1, 0])", tex_to_color_map={"=":RED, "array":BLUE}),
            TextMobject("\\tt UL=np.array([-1, 1, 0])", tex_to_color_map={"=":RED, "array":BLUE}),
            TextMobject("\\tt DR=np.array([ 1,-1, 0])", tex_to_color_map={"=":RED, "array":BLUE}),
            TextMobject("\\tt DL=np.array([-1,-1, 0])", tex_to_color_map={"=":RED, "array":BLUE})
        ).arrange_submobjects(DOWN)
        self.add(text)

class Test3(Scene):
    '''坐标可以用ndarray，也可以用列表'''
    def construct(self):
        l = Line([0, 0, 0], [3, 3, 0])
        self.add(l)

class Test4(Scene):
    '''aligned_edge的用法'''
    def construct(self):
        sq1 = Square().shift(LEFT * 2)
        sq2 = Square().next_to(sq1.get_corner(DR), DOWN)
        sq3 = Square().shift(RIGHT * 2)
        sq4 = Square().next_to(sq3.get_corner(DR), DOWN, aligned_edge=LEFT)

        self.add(sq1, sq2, sq3, sq4)

class Test5(Scene):
    '''加号强制next_to对齐'''
    def construct(self):
        text = TextMobject("LOVE\\ DEATH\\ ", "$+$", "\\ ROBOTS", color=RED)
        text[1].next_to(text[0], RIGHT)
        text[2].next_to(text[1], RIGHT)
        self.add(text)

class Test6(Scene):
    '''FocusOn和Flash的动画效果'''
    def construct(self):
        title1 = TextMobject("FocusOn").scale(2).to_corner(UL)
        self.add(title1)
        dot = Dot(radius=0.5, color=BLUE)
        self.play(ShowCreation(dot))
        self.wait()
        self.play(FocusOn(dot))
        self.wait(2)
        title2 = TextMobject("Flash").scale(2).to_corner(UL)
        self.play(Transform(title1, title2))
        self.wait()
        self.play(Flash(dot, flash_radius=0.55))
        self.wait(3)

class Test7(Scene):
    '''白底黑字'''
    def construct(self):
        txt = TexMobject("0",
            fill_color=BLACK,
            fill_opacity=1.0,
            stroke_color=BLACK,
            stroke_opacity=1.0,
        ).scale(3)
        self.add(txt)

class Test8(Scene):
    '''使用Rectangle或者Line来强制Brace宽度'''
    def construct(self):
        rec = Rectangle(width=4)
        brac = Brace(rec, DOWN)
        self.add(brac)

class Test9(ThreeDScene):
    '''立方体三维旋转'''
    def construct(self):
        self.set_to_default_angled_camera_orientation()
        cube = Cube()
        self.add(cube)
        self.wait()
        self.play(Rotating(cube, axis=UP, radians=PI / 6))
        self.wait(2)

class Test10(Scene):
    '''文字渐变色'''
    def construct(self):
        text = TextMobject("test").scale(2).set_color_by_gradient(BLUE, RED)
        self.add(text)

class Test11(Scene):
    '''LaTeX的cases可行'''
    def construct(self):
        text = TexMobject(
            r"""
            \begin{cases}
            u^3+v^3=-q\\
            uv=-\frac{p}{3}\\
            \end{cases}
            """
        )
        self.add(text)

class Test12(Scene):
    def construct(self):
        circle0 = Circle(color=WHITE,radius=2)
        text0 = TextMobject("Gaussian \\\\ Elimination")
        vec1  =Vector(1.4*LEFT).move_to(circle0.get_center()+2.8*LEFT)
        circle1 = Circle(color=RED,radius=1.6).next_to(vec1, LEFT)
        text1 = TextMobject("System of \\\\   linear equation").move_to(circle1.get_center()+ORIGIN).scale(0.8)

        vgr1 = VGroup(text1, circle1)
        self.add(circle0, text0)
        self.add(vec1)
        self.add(vgr1)
        self.wait(2)
        pos = Dot(fill_opacity=0).move_to(circle1.get_center())
        def update_text(obj):
            obj.move_to(pos)

        vgr1.add_updater(update_text)
        self.add(vgr1)    
        self.play(
            Rotating(vec1, radians = 6 * PI, about_point = ORIGIN, axis = IN),
            Rotating(pos , radians = 6 * PI, about_point = ORIGIN, axis = IN),
            run_time=20
        )

class Test13(Scene):
    '''Uncreate效果，注意不是UnCreate'''
    def construct(self):
        sq = Square()
        self.add(sq)
        self.wait()
        self.play(Uncreate(sq))
        self.wait()

class Test14(Scene):
    def construct(self):
        rec1 = Rectangle(height=2, width=6)
        rec2 = Rectangle(height=1, width=1).shift(LEFT*2)
        rec3 = Rectangle(height=1, width=1).shift(RIGHT*2)
        rec4 = Rectangle(height=1, width=1)
        recs = VGroup(rec1, rec2, rec3, rec4)
        self.add(recs)
        self.wait()
        self.play(recs.shift, UP*2.5)
        self.wait()
        circle = Circle(radius=0.5).move_to(rec3)
        self.play(Transform(rec3, circle))
        self.wait()

class Test15(GraphScene):
    '''GraphScene的坐标轴可以FadeOut'''
    def construct(self):
        self.setup_axes(animate=True)
        self.wait()
        self.play(FadeOut(self.axes))
        self.wait()

class Test16(Scene):
    def construct(self):
        objs = [
            Square().shift(LEFT * 3),
            Square(),
            Square().shift(RIGHT * 3)
        ]
        self.add(*objs)
        self.wait()
        self.play(
            *[
                ApplyMethod(obj.shift, UP)
                for obj in objs
            ]
        )
        self.wait()

class Test17(Scene):
    '''使用index_of_submobject_to_align来对齐，注意要get_center()'''
    def construct(self):
        vg1 = VGroup(
            Circle(radius = 0.5).shift(LEFT*2),
            Circle(radius = 0.5).shift(LEFT*1),
            Circle(radius = 0.5),
            Circle(radius = 0.5).shift(RIGHT*1),
            Circle(radius = 0.5).shift(RIGHT*2),
        )
        vg2 = VGroup(
            Square(side_length=1).shift(LEFT*1),
            Square(side_length=1),
            Square(side_length=1).shift(RIGHT*1),
        )
        vg2.next_to(vg1[3].get_center(), DOWN, index_of_submobject_to_align=1)
        self.add(vg1, vg2)

class Test18(Scene):
    '''使用tex[0]来对TexMobject的每个字符进行分解'''
    def construct(self):
        tex = TexMobject("a^2+b^2=c^2")
        self.add(tex)
        debugTeX(self, tex[0])

class Test19(Scene):
    '''用AnimatedBoundary实现Line的颜色变化'''
    def construct(self):
        l = Line(LEFT * 3, RIGHT * 3)
        self.add(l)
        self.wait()
        l2 = AnimatedBoundary(l, colors=[BLUE])
        self.add(l2)
        self.wait(3)

class Test20(Scene):
    '''使用set_opacity实现闪烁效果'''
    def construct(self):
        text = TextMobject("颓废最不要脸")
        self.add(text)
        for i in range(20):
            self.play(text.set_opacity, 0, run_time=0.2)
            self.play(text.set_opacity, 1, run_time=0.2)
        self.wait()

class Test21(Scene):
    '''圆弧flip的默认轴'''
    def construct(self):
        grid = NumberPlane()
        arc = Arc(0, PI / 2, color = BLUE)
        arc2 = arc.copy().flip().set_color(YELLOW)
        self.add(grid, arc, arc2)

class Test22(Scene):
    def construct(self):
        text = TextMobject("abcd")
        self.add(text)

class Test23(Scene):
    '''move_arc_center_to和不同run_time的动画同时播放'''
    def construct(self):
        sq = Square(side_length=4)
        ci = Arc(0, PI / 2, color=BLUE, radius=4).move_arc_center_to(sq.get_corner(DL))
        self.wait()
        self.play(ShowCreation(sq, run_time=2), ShowCreation(ci, run_time=4))
        self.wait()

class Test24(Scene):
    '''环绕每个字符'''
    def construct(self):
        text = TextMobject("abcdefgh")
        rec = VGroup()
        for i in text[0]:
            rec.add(SurroundingRectangle(i, buff=0))
        self.add(text, rec)

class Test25(Scene):
    '''使用LaTeX的表格'''
    def construct(self):
        tab = TextMobject(
            r"""
            \begin{table}[]
            \begin{tabular}{|l|l|l|l|l|l|}
            \hline
            a & b & c & d & e & f \\ \hline
            \end{tabular}
            \end{table}
            """
        )
        self.add(tab)
        debugTeX(self, tab[0])

class Test26(Scene):
    '''Succession，其实和多个play没什么区别'''
    def construct(self):
        group = VGroup(
            Circle(radius = 0.5).shift(LEFT*2),
            Circle(radius = 0.5).shift(LEFT*1),
            Circle(radius = 0.5),
            Circle(radius = 0.5).shift(RIGHT*1),
            Circle(radius = 0.5).shift(RIGHT*2),
        ).set_opacity(0)
        self.wait()
        self.play(
            Succession(
                *[
                    ApplyMethod(obj.set_opacity, 1)
                    for obj in group
                ]
            )
        )
        self.wait()

class Test27(Scene):
    '''UP和TOP在to_corner时的区别'''
    def construct(self):
        text = TextMobject("to\_corner UP").to_corner(UP)
        text2 = TextMobject("to\_corner TOP").to_corner(TOP) # 非标准用法
        text3 = TextMobject("move\_to TOP").move_to(TOP).set_color(YELLOW)
        self.add(text, text2, text3)

class Test28(Scene):
    '''将所有物体都FadeOut，没有add的物体也不会强制add再FadeOut'''
    def construct(self):
        sq = Square()
        ci = Circle()
        self.add(sq)
        self.wait()
        self.play(
            *[
                FadeOut(obj)
                for obj in self.mobjects
            ]
        )
        self.wait()

class Test29(Scene):
    '''Text不会自动换行'''
    def construct(self):
        text = Text("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", font="Consolas")
        self.add(text)

class Test30(Scene):
    '''字符上弧'''
    def construct(self):
        text = TextMobject("\\overarc{AB}")
        self.add(text)

class Test31(Scene):
    def construct(self):
        Gc = VGroup()
        colors = color_gradient([BLACK, WHITE], 9)
        Gc.add(Square(side_length=1).shift(LEFT*6).set_fill(colors[0], 1).set_color(colors[0]))
        for i in range(1, 9):
            Gc.add(Gc[-1].copy().set_fill(colors[i], 1).set_color(colors[i]).shift(RIGHT*1.2))
            self.play(Transform(Gc[-2], Gc[-1], rate_func=linear))
        self.wait()

class Test32(GraphScene):
    '''get_graph必须在setup_axes之后'''
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = None, 
                                    x_max = None
                                    )
        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

class Test33(Scene):
    '''用颜色灰度来实现透明度的效果，防止两透明度颜色相叠加，导致亮度突变'''
    def construct(self):
        colors = color_gradient(["#6C6C00", YELLOW], 9)
        sq = Square(side_length=1).shift(LEFT*6).set_fill(colors[0], 1).set_color(colors[0])
        for i in range(1, 9):
            self.play(
                ApplyMethod(sq.shift, RIGHT * 1.2, rate_func=linear),
                ApplyMethod(sq.set_color, colors[i]),
                ApplyMethod(sq.set_fill, colors[i], 1)
            )
        self.wait()

class Test34(ThreeDScene):
    '''cube的面'''
    def construct(self):
        self.set_to_default_angled_camera_orientation()
        cube = Cube(fill_opacity=0, stroke_width=3).set_fill(opacity=0).set_color(WHITE)
        cube[5].set_color(BLUE)
        self.add(cube)
        debugTeX(self, cube)

class Test35(GraphScene):
    '''使用updater来实现graph的更新'''
    def construct(self):
        self.setup_axes()
        line = self.get_graph(lambda x: x + 2)
        val = ValueTracker(1)
        line.add_updater(lambda m: m.become(self.get_graph(lambda x: val.get_value() * x + 2, color=BLUE)))
        self.add(line)
        self.play(val.increment_value, 4)
        self.wait()

class Test36(ThreeDScene):
    '''抛物面'''
    def construct(self):
        self.set_to_default_angled_camera_orientation()
        颓废曲面 = ParametricSurface(
            lambda u, v: [u, v, u ** 2 + v ** 2],
            u_min=-1, u_max=1, v_min=-1, v_max=1
        )
        self.add(颓废曲面)

class Test37(Scene):
    '''Transfrom前统一方向，使动画更顺滑'''
    def construct(self):
        ci = Circle()
        # sq = Square()
        sq = Square().flip()
        self.play(ShowCreation(ci))
        self.play(Transform(ci, sq))
        self.wait()

class Test38(Scene):
    '''根式上色'''
    def construct(self):
        text = TexMobject("\\sqrt{x^2+y^2+z^2}")
        text[0][2:4].set_color(RED)
        self.add(text)
        debugTeX(self, text[0])

class Test39(Scene):
    '''上色'''
    def construct(self):
        text4 = TexMobject(
            r"ds=\vert d\vec r \vert=",
            r"\sqrt{x^2+y^2+z^2}"
        )
        VGroup(
            text4
        ).set_color(YELLOW)
        VGroup(
            text4[1][2:4]
        ).set_color(RED)
        self.add(text4)
        debugTeX(self, text4[1])

class Test40(Scene):
    '''一个self.play中无法处理两个针对同一物体的ApplyMethod，但不加ApplyMethod可以'''
    def construct(self):
        dot = Dot(color=BLUE)
        up = Dot(color=YELLOW).to_edge(UP)
        self.add(dot)
        self.wait()
        # self.play(
        #     ApplyMethod(dot.next_to, up, DOWN),
        #     ApplyMethod(dot.scale, 3)
        # )
        self.play(
            dot.next_to, up, DOWN,
            dot.scale, 3
        )
        self.wait()

class Test41(Scene):
    '''replace的作用'''
    def construct(self):
        sq = Square().scale(2)
        ci = Circle().shift(RIGHT*3)
        self.add(sq, ci)
        self.play(sq.replace, ci)
        self.wait()

class Test42(Scene):
    '''使用updater时不能使用循环变量i'''
    def construct(self):
        ups = VGroup(
            *[
                Dot(color=BLUE).move_to([i, 1, 0])
                for i in range(-3, 4)
            ]
        )
        downs = VGroup(
            *[
                Dot(color=YELLOW).move_to([i, -1, 0])
                for i in range(-3, 4)
            ]
        )
        lines = VGroup(
            *[
                Line(ups[i], downs[i])
                for i in range(0, 7)
            ]
        )
        lines.add_updater(
            lambda m: m.become(
                VGroup(
                    *[
                        Line(ups[i], downs[i])
                        for i in range(0, 7)
                    ]
                )
            )
        )
        # for i in range(7):
        #     lines[i].add_updater(lambda m: m.put_start_and_end_on(ups[i].get_bottom(), downs[i].get_top()))
        self.add(ups, downs, lines)
        self.wait()
        self.play(
            ups.shift, LEFT * 2
        )
        self.play(
            downs.shift, RIGHT * 2
        )
        self.wait()
    
class Test43(Scene):
    '''和Test40同理'''
    def construct(self):
        dot = Dot(color=BLUE)
        self.add(dot)
        self.wait()
        self.play(
            ApplyMethod(dot.scale, 3), # 这个被淹没了
            ApplyMethod(dot.set_color, YELLOW)
        )
        self.wait()

class Test44(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        spheres = VGroup(
            *[
                Sphere(radius=i, opacity=0.5, resolution=(20, 40))
                for i in np.arange(1, 3.1, 0.4)
            ]
        )
        self.set_to_default_angled_camera_orientation()
        self.add(axes)
        old = VGroup()
        new = VGroup()
        for i in range(len(spheres[0])):
            old.add(spheres[randint(1, 5)][i].set_opacity(randint(1, 6) / 10))
            new.add(spheres[0][i])
        self.wait()
        self.wait()
        self.play(
            FadeIn(old),
            *[
                Transform(i, j)
                for i, j in zip(old, new)
            ],
            run_time=6
        )
        self.wait()

class Test45(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_to_default_angled_camera_orientation()
        self.add(axes)
        surface = ParametricSurface(
            lambda y, z: [
                -np.sqrt(
                    1 - 9 * y ** 2 / 4 + (320 * 2 ** (1 / 3) * z ** 3) / ((
                    99532800 * y ** 2 * z ** 2 + 884736000 * z ** 3 - \
                    1990656000 * y ** 2 * z ** 3 - 884736000 * z ** 5 + np.sqrt(
                        (-115964116992000000 * z ** 9 + (99532800 * y ** 2 * z ** 2 + \
                        884736000 * z ** 3 - 1990656000 * y ** 2 * z ** 3 - 884736000 * z ** 5) ** 2) ** 2)
                    ) ** (1 / 3)) + (1 / 960 * 2 ** (1 / 3)) * (99532800 * y ** 2 * z ** 2 + \
                    884736000 * z ** 3 - 1990656000 * y ** 2 * z ** 3 - 884736000 * z ** 5 + np.sqrt(
                        (-115964116992000000 * z ** 9 + (99532800 * y ** 2 * z ** 2 + 884736000 * z ** 3 -\
                        1990656000 * y ** 2 * z ** 3 - 884736000 * z ** 5) ** 2)
                    )) ** (1 / 3)
                ),
                y, z
            ]
        )
        self.add(surface)

class Test46(Scene):
    '''Brace'''
    def construct(self):
        text = TextMobject("test")
        brace = Brace(text, DOWN)
        self.play(Write(brace))
        self.play(Write(text))

class Test47(Scene):
    '''LaTeX的dancers小人，需要下载字体包并且更改ctex_template'''
    def construct(self):
        Test = VGroup()
        for i in range(51):
            test = TextMobject("\\Pisymbol{dancers}{%d}" % i, stroke_width=1, fill_opacity=1, stroke_opacity=1).scale(200)
            Test.add(test)
        self.wait()
        self.play(Write(Test[0]))
        for i in range(1, 51):
            self.wait(0.8)
            self.play(Transform(Test[0], Test[i]))
        self.wait(2)

class Test48(Scene):
    '''plot_depth'''
    CONFIG = {
        "camera_config": {"use_plot_depth": True}
    }
    def construct(self):
        sq = Square(stroke_width=5).set_plot_depth(1)
        sq2 = Square(side_length=1, stroke_width=5).shift(RIGHT).set_color(BLUE).set_plot_depth(0)
        self.add(sq, sq2)
        self.wait()
        self.play(sq2.set_plot_depth, 2)
        self.wait()

class Test49(Scene):
    '''使用LaTeX的lstlisting写代码，需要改ctex_template'''
    def construct(self):
        text = TextMobject("""
            \\begin{lstlisting}
            int main() {

            }
            \\end{lstlisting}
        """)
        self.add(text)

class Test50(ThreeDScene):
    '''正劈锥体，渲染贼慢'''
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        self.add(axes)
        a = VGroup()
        b = VGroup()
        c = VGroup()
        for i in np.arange(-1, 1.00001, 0.0005):
            tri = Polygon([i, np.sqrt(1 - i ** 2), 0], 
                          [i, -np.sqrt(1 - i ** 2), 0],
                          [i, 0, 2], stroke_width=0, fill_color=BLUE, fill_opacity=0.75)
            a.add(tri)
        cnt = 1
        self.begin_ambient_camera_rotation(rate=0.5)
        for tri in a:
            if cnt % 2 == 0:
                self.add(tri.set_fill(color=YELLOW, opacity=0.5))
                self.wait(0.01)
                tri.set_fill(color=BLUE, opacity=0.75)
            else:
                self.add(tri)
            cnt += 1
        self.wait(5)

class Test51(ThreeDScene):
    '''棱锥到近似圆锥'''
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        self.add(axes)
        circle = Circle(radius=2)
        polys = []
        faces = []
        for i in range(3, 16):
            po = Polygon(
                *[
                    UP * np.sin(j * 2 * PI / i) + RIGHT * np.cos(j * 2 * PI / i)
                    for j in range(i)
                ], stroke_width=1, stroke_color=BLUE, fill_color=BLUE, fill_opacity=0.75
            ).scale(2, about_point=ORIGIN)
            polys.append(po)
            verts = po.get_vertices()
            faces_ = VGroup()
            for j in range(i):
                if j == i - 1:
                    face = Polygon(verts[j], verts[0], [0, 0, 3])
                else:
                    face = Polygon(verts[j], verts[j + 1], [0, 0, 3])
                face.set_stroke(width=1, color=BLUE)
                face.set_fill(color=BLUE, opacity=0.75)
                faces_.add(face)
            faces.append(faces_)
        self.play(ShowCreation(circle))
        self.play(ShowCreation(polys[0]), ShowCreation(faces[0]))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait()
        for i in range(1, 13):
            self.play(
                Transform(polys[0], polys[i]),
                Transform(faces[0], faces[i])
            )
            self.wait()
        self.wait(2)

class Test52(SpecialThreeDScene):
    '''Boxes类的test'''
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }
    def construct(self):

        self.set_camera_to_default_position()
        axes = self.get_axes()
        boxes = MyBoxes(fill_color=GRAY, resolution=(20, 20), bottom_size=(0.25, 0.25), gap=0.05)
        self.var_phi = 0
        func_01 = lambda x, y: np.sin(x ** 2 / 2.4 + y ** 2 / 2.4 + self.var_phi) * 1.
        func_02 = lambda x, y: np.sin(x ** 2 / 2.4 + y ** 2 / 2.4 + self.var_phi) * 1. - 0.25

        boxes.update_top_and_bottom_by_func(func_01, func_02)
        boxes.update_color_by_func(func_01)
        def update_boxes(b, dt):
            b.update_top_and_bottom_by_func(func_01, func_02)
            b.update_color_by_func(func_01)
            self.var_phi += 1 * DEGREES
        self.add(boxes)
        boxes.add_updater(update_boxes)
        # self.wait(2)
        # boxes.remove_updater(update_boxes)
        self.wait(12)

class Test53(ThreeDScene):
    '''MyBoxes的序号分布'''
    def construct(self):
        axes = ThreeDAxes()
        # self.set_camera_orientation(phi=70 * DEGREES, theta=225 * DEGREES)
        self.add(axes)
        boxes = MyBoxes(fill_color=GRAY, resolution=(9, 18), bottom_size=(0.5, 0.7), gap=0.2, box_height=0.5)
        self.add(boxes)
        debugTeX(self, boxes)

class Test54(ThreeDScene):
    '''测试元素周期表'''
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "should_apply_shading": False,
        }
    }
    def construct(self):
        self.set_camera_orientation(phi=50 * DEGREES, theta=240 * DEGREES, distance=50)
        boxes = ChemicalBoxes(fill_color=BLUE_E).add_label().set_block_color()
        self.add(boxes)
        self.begin_ambient_camera_rotation(rate=1)
        # self.wait(10)

class Test55(Scene):
    '''无法像这样获取圆上某一方向的点'''
    def construct(self):
        ci = Circle()
        self.add(ci)
        dot = Dot().move_to(ci.get_boundary_point(UP * 2 * np.sqrt(5) / 5 + RIGHT * np.sqrt(5) / 5))
        self.add(dot)

class Test56(Scene):
    '''带dt的updater'''
    def construct(self):
        dot = Dot().to_edge(UP)
        dot.add_updater(lambda m, dt: m.shift(0.1 * DOWN))
        self.add(dot)
        self.wait(6)

class Test57(Scene):
    '''文字上下标'''
    def construct(self):
        text = TextMobject("正文A$_{\\text{下标B}}^{\\text{上标C}}$").scale(3)
        self.add(text)

class Test58(Scene):
    '''rate_func'''
    def construct(self):
        func = ParametricFunction(
            lambda x: [x, smooth(x), 0],
            t_min=0, t_max=1
        ).scale(3, about_point=ORIGIN)
        self.add(func)

class Test59(Scene):
    '''save_image'''
    def construct(self):
        sq = Square()
        sq.save_image()
        self.add(sq)

class Test60(Scene):
    '''根据等号对齐'''
    def construct(self):
        tex1 = TexMobject("A=\\frac{\\displaystyle\\sum^n_{i=0}}{x}")
        tex2 = TexMobject("=", "\\frac{x}{\\displaystyle\\sum^n_{i=0}}")
        tex2.next_to(tex1, RIGHT)
        tex2.next_to(tex1[0][1].get_center(), RIGHT, index_of_submobject_to_align=0, coor_mask=np.array([0, 1, 1]))
        self.add(tex1, tex2)
        texs = [
            "A=\\frac{\\displaystyle\\sum^n_{i=0}}{x}",
            "=\\frac{x}{\\displaystyle\\sum^n_{i=0}}"
        ]
        tex = TexMobject(*texs)
        self.add(tex)

class Test61(Scene):
    def construct(self):
        for1 = TexMobject(r"G(x)=\displaystyle\sum_{p=0}^{\infty}{\left( \frac{S^{p}(n)}{p!}x^p\right)}").scale(0.7).to_edge(UP+LEFT)
        for1_bg = SurroundingRectangle(for1, fill_opacity = .2)
        for2 = TexMobject(r"G(x) = \left( \frac{e^{(n+1)x}-1}{x} \right) \left( \frac{x}{e^x-1} \right)")

        forrs = [
            r"\frac{e^{(n+1)x}-1}{x}", # for3
            r"= \frac{ \left( \displaystyle\sum_{p=0}^{\infty}{\frac{{((n+1)x)}^p}{p!}} \right) -1}{x}}", #for4
            r"=\frac{1+\left( \displaystyle\sum_{p=1}^{\infty}{\frac{{((n+1)x)}^p}{p!}} \right) -1}{x}}",#for5
            r"=\displaystyle\sum_{p=1}^{\infty}{\frac{(n+1)^p}{p!}x^{p-1}}",#for6
            r"=\displaystyle\sum_{p=0}^{\infty}{\frac{(n+1)^{p+1}}{(p+1)!}x^{p}}"#for7
        ]
        forr = TexMobject(*forrs).scale(0.9)
        self.add(forr)

class Test62(Scene):
    '''三角形绕边翻转'''
    def construct(self):
        tri = Triangle()
        vert = tri.get_vertices()
        tri.generate_target()
        tri.target.flip(axis=vert[0]-vert[1], about_point=(vert[0]+vert[1])/2)
        self.add(tri)
        self.wait()
        self.play(MoveToTarget(tri))
        self.wait()

class Test63(Scene):
    '''文字渐变色的区别'''
    def construct(self):
        vg = VGroup(
            TextMobject("abcde").set_color([RED, BLUE, WHITE]),
            TextMobject("abcde").set_color_by_gradient(RED, BLUE, WHITE),
            TextMobject("abcde")
        ).arrange(DOWN)
        vg[2].shuffle(True)
        vg[2].set_color_by_gradient(RED, BLUE, WHITE)
        self.add(vg)

class Test64(Scene):
    '''CubicBezier的points只有四个点，即锚点和控制点，但ParametricFunction是好多贝塞尔曲线，好多点'''
    def construct(self):
        # line = CubicBezier([np.array([  -3, -1.5, 0]), np.array([-3.6,  1.5, 0]), np.array([   0,  1.5, 0]), np.array([   3, -1.5, 0])])
        line = ParametricFunction(
            bezier([np.array([  -3, -1.5, 0]), np.array([-3.6,  1.5, 0]), np.array([   0,  1.5, 0]), np.array([   3, -1.5, 0])]),
            t_min=0, t_max=1
        )
        self.add(line)
        points = line.get_points()
        debugTeX(self, points)

class Test65(Scene):
    '''渐变色的方向，用sheen_direction来设定'''
    def construct(self):
        sq = Square()
        sq.set_color([RED, BLUE])
        # sq.set_opacity([0, 1])
        # sq.set_fill([RED, BLUE], [0, 1])
        sq.set_sheen_direction(UP)
        self.add(sq)
        # self.wait()
        # self.play(sq.flip)
        # self.wait()

class Test66(Scene):
    '''digest_config的很愚蠢的用法'''
    CONFIG = {
        "stroke_width": 15,
    }
    def construct(self):
        line = Line()
        digest_config(line, self.CONFIG)
        self.add(line)

class Test67(Scene):
    '''arc的points，用好多贝塞尔曲线来拟合的'''
    def construct(self):
        arc = Arc().scale(3)
        self.add(arc)
        points = arc.get_points()
        debugTeX(self, points, 0.3)

class Test68(Scene):
    def construct(self):
        tex = TexMobject("{\\sin\\alpha\\over\\sin\\gamma}={n_1\\over n_2}")
        self.add(tex)
        debugTeX(self, tex[0])

class Test69(ThreeDScene):
    '''无法将三维物体Transform到fixed_in_frame_mobjects的二维物体，但可以通过z_to_vector等变换得到类似的效果'''
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=45*DEGREES)
        vec = [
            np.cos(45*DEGREES) * np.sin(60*DEGREES),
            np.sin(45*DEGREES) * np.sin(60*DEGREES),
            np.cos(60*DEGREES)
        ]
        n = z_to_vector(vec)
        tex = TexMobject("a").apply_matrix(n).rotate(PI/2, vec)
        # self.camera.add_fixed_in_frame_mobjects(tex)
        # tex.to_corner(UL)
        surface = Cube()
        self.add(surface)
        self.play(Transform(surface, tex), run_time=2)
        self.wait()

class Test70(Scene):
    '''无法通过get_points获取TexMobject的点'''
    def construct(self):
        tex = TexMobject("S").scale(2)
        self.add(tex)
        p = tex.get_points()
        print(p)

class Test71(Scene):
    def construct(self):
        grid = NumberPlane()
        vector = np.array([1, 2, 0])
        matrix = np.identity(3) - np.outer(vector, vector)
        self.add(grid, Dot([1, 2, 0], color=RED))
        self.wait()
        self.play(grid.apply_matrix, matrix, run_time=3)
        self.wait()

class Test72(Scene):
    '''光源'''
    def construct(self):
        light = AmbientLight()
        self.add(light)

class Test73(Scene):
    '''running_start的写法是六次贝塞尔曲线'''
    def construct(self):
        grid = NumberPlane().scale(3)
        func = ParametricFunction(
            lambda x: [x, running_start(x), 0],
            t_min=0, t_max=1
        ).scale(3, about_point=ORIGIN)
        func2 = ParametricFunction(
            bezier([
                np.array([0/6, 0, 0]), 
                np.array([1/6, 0, 0]), 
                np.array([2/6, -0.5, 0]), 
                np.array([3/6, -0.5, 0]),
                np.array([4/6, 1, 0]),
                np.array([5/6, 1, 0]),
                np.array([6/6, 1, 0]),
            ]),
            t_min=0, t_max=1, color=RED
        ).scale(3, about_point=ORIGIN)
        self.add(grid, func, func2)

class Test74(Scene):
    '''幼儿园小练习1'''
    CONFIG = {
        "camera_config": {
            "use_plot_depth": True,
        },
    }

    def setup(self):
        self.A = np.array([1, 0, 0])
        self.B = np.array([-1, 0, 0])
        self.C = np.array([-0.3, 1.3, 0])

        self.main_tri = Polygon(
            self.A, self.B, self.C,
            color=BLUE, fill_color=BLUE, fill_opacity=0.8
        )

        label_a = TexMobject("a").scale(0.7).next_to((self.B+self.C)/2, UL, buff=0.08)
        label_b = TexMobject("b").scale(0.7).next_to((self.A+self.C)/2, UR, buff=0.08)
        label_c = TexMobject("c").scale(0.7).next_to((self.B+self.A)/2, DOWN, buff=0.08)
        self.labels = VGroup(label_a, label_b, label_c).set_plot_depth(5)

        sq_a = Polygon(self.B, self.C, np.array([-1.6, 2, 0]), np.array([-2.3, 0.7, 0]), color=WHITE)
        sq_b = Polygon(self.C, self.A, np.array([2.3, 1.3, 0]), np.array([1, 2.6, 0]), color=WHITE)
        sq_c = Polygon(self.A, self.B, np.array([-1, -2, 0]), np.array([1, -2, 0]), color=WHITE)
        self.sq = VGroup(sq_a, sq_b, sq_c).set_plot_depth(-1)

        tri_a = Polygon(self.A, np.array([1, -2, 0]), np.array([2.3, 1.3, 0]), color=RED, fill_color=RED, fill_opacity=0.8)
        tri_b = Polygon(self.B, np.array([-2.3, 0.7, 0]), np.array([-1, -2, 0]), color=YELLOW, fill_color=YELLOW, fill_opacity=0.8)
        tri_c = Polygon(self.C, np.array([1, 2.6, 0]), np.array([-1.6, 2, 0]), color=GREEN, fill_color=GREEN, fill_opacity=0.8)
        self.tri = VGroup(tri_a, tri_b, tri_c)

        equation = TexMobject("S_{\\ } = S_{\\ } = S_{\\ } = S_{\\ }").scale(1.5).to_corner(UR, buff=1.1)
        tri_1 = self.main_tri.copy().set_stroke(width=0).set_fill(opacity=1).scale(0.2).next_to(equation[0][0], RIGHT+DOWN*3, buff=-0.08)
        tri_2 = tri_a.copy().rotate(PI/2).set_stroke(width=0).set_fill(opacity=1).scale(0.2).next_to(equation[0][2], RIGHT+DOWN*3, buff=-0.08)
        tri_3 = tri_b.copy().rotate(PI/2, axis=IN).set_stroke(width=0).set_fill(opacity=1).scale(0.2).next_to(equation[0][4], RIGHT+DOWN*3, buff=-0.08)
        tri_4 = tri_c.copy().rotate(PI/4, axis=IN).set_stroke(width=0).set_fill(opacity=1).scale(0.2).next_to(equation[0][6], RIGHT+DOWN*3, buff=-0.08)
        self.equation = VGroup(equation, tri_1, tri_2, tri_3, tri_4)

        # self.add(self.main_tri, self.labels, self.sq, self.tri, equation, tri_1, tri_2, tri_3, tri_4)

    def construct(self):
        self.wait()
        self.play(ShowCreation(self.main_tri))
        self.wait()
        self.play(FadeIn(self.labels))
        self.wait(2)
        self.play(*[ShowCreation(i.set_plot_depth(-5)) for i in self.sq], run_time=2)
        self.wait()
        self.play(*[ShowCreation(i) for i in self.tri], run_time=2)
        self.wait()
        self.play(
            *[
                WiggleOutThenIn(i)
                for i in self.tri
            ], run_time=2
        )
        self.wait(2)
        self.play(
            FadeOut(self.sq),
            Rotating(self.tri[0], radians=PI/2, about_point=self.A),
            Rotating(self.tri[1], radians=PI/2, about_point=self.B),
            Rotating(self.tri[2], radians=PI/2, about_point=self.C),
            run_time=3
        )
        self.wait()
        self.play(
            self.main_tri.shift, LEFT*2.5+DOWN,
            self.tri.shift, LEFT*2.5+DOWN,
            self.labels.shift, LEFT*2.5+DOWN,
        )
        self.labels.set_plot_depth(6)
        self.wait(2)
        self.play(
            WiggleOutThenIn(self.tri[0]), 
            WiggleOutThenIn(self.main_tri)
        )
        self.play(
            FadeIn(self.equation[0][0][:3]),
            TransformFromCopy(self.main_tri, self.equation[1]),
            TransformFromCopy(self.tri[0], self.equation[2]),
            run_time=2
        )
        self.wait(2)
        self.play(
            WiggleOutThenIn(self.tri[1]), 
            WiggleOutThenIn(self.main_tri)
        )
        equation_copy_1 = self.equation[1].copy()
        equation_copy_2 = self.equation[1].copy()
        self.play(
            FadeIn(self.equation[0][0][3:5]),
            TransformFromCopy(self.main_tri, equation_copy_1),
            TransformFromCopy(self.tri[1], self.equation[3]),
            run_time=2
        )
        self.wait(2)
        self.play(
            WiggleOutThenIn(self.tri[2]), 
            WiggleOutThenIn(self.main_tri)
        )
        self.play(
            FadeIn(self.equation[0][0][5:]),
            TransformFromCopy(self.main_tri, equation_copy_2),
            TransformFromCopy(self.tri[2], self.equation[4]),
            run_time=2
        )
        self.wait(3)
        self.play(FadeOut(VGroup(self.equation[0][0][:2], self.equation[1], equation_copy_1, equation_copy_2)))
        self.equation[0][0][:2].set_opacity(0)
        self.equation[1].set_fill(opacity=0)
        self.equation.generate_target()
        self.equation.target.scale(1.3).shift(DOWN+LEFT)
        self.play(MoveToTarget(self.equation))
        self.wait(5)

class Test75(Scene):
    '''对坐标轴的非线性变换'''
    def construct(self):
        grid = ComplexPlane().prepare_for_nonlinear_transform(50)
        self.add(grid)
        self.wait()
        self.play(
            grid.apply_function,
            lambda point: complex_to_R3(R3_to_complex(point)**2),
            run_time=5
        )
        self.wait()

class Test76(Scene):
    '''交换点的顺序实现五角星'''
    def construct(self):
        poly = RegularPolygon(5)
        verts = poly.get_vertices()
        poly2 = Polygon(verts[0], verts[2], verts[4], verts[1], verts[3]).set_fill(BLUE, opacity=0.5)
        self.add(poly2)
        debugTeX(self, verts)

class Test77(Scene):
    '''对Imageset_color，所有rgb均替换为指定颜色，但保留alpha'''
    def construct(self):
        image = ImageMobject("GZTime.png").set_color(RED)
        self.add(image)

class MyTransform(Animation):
    '''继承Animation类，自定义动画，用于下一个场景'''
    CONFIG = {
        "radians": PI/2,
        "axis": OUT,
        "about_point": None,
        "remover": True,
    }
    def __init__(self, mobject, target, **kwargs):
        digest_config(self, kwargs)
        self.mobject = mobject.copy()
        self.target = target
    def clean_up_from_scene(self, scene):
        if self.is_remover():
            scene.remove(self.mobject)
            scene.add(self.target)
    def interpolate_mobject(self, alpha):
        now = self.starting_mobject.copy()
        now.rotate(
            alpha * self.radians,
            axis=self.axis,
            about_point=self.about_point,
        )
        for i in range(3):
            now[i].set_color(interpolate_color(self.starting_mobject[i].get_color(), self.target[i].get_color(), alpha))
        self.mobject.become(now)

class Test78(Scene):
    '''logo的一种动画方案'''
    def construct(self):
        logo1 = VGroup(
            Polygon(np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 2, 0])),
            Polygon(np.array([1.5, 0, 0]), np.array([3, 3, 0]), np.array([0, 3, 0])),
            Polygon(np.array([2, 0, 0]), np.array([3, 0, 0]), np.array([3, 2, 0])),
        ).set_stroke(width=0).center()
        logo1[0].set_fill(WHITE, 1)
        logo1[1].set_fill(BLUE_B, 1)
        logo1[2].set_fill(BLUE_C, 1)
        logo1.move_to(np.array([2.5, 1, 0]))
        logo2 = logo1.copy().rotate(PI/2, about_point=ORIGIN)
        logo3 = logo2.copy().rotate(PI/2, about_point=ORIGIN)
        logo4 = logo3.copy().rotate(PI/2, about_point=ORIGIN)
        logo = VGroup(logo1, logo2, logo3, logo4).scale(1/3)
        logo[0][1].set_fill("#C59978", 1)
        logo[0][2].set_fill("#8D5630", 1)
        text = VGroup(
            Text("Manim", font="Nexa Bold"),
            Text("Kindergarten", font="Nexa Bold")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).set_height(2).next_to(logo, buff=0.8).shift(DOWN*0.2)
        all_logo = VGroup(logo, text).center()
        bg = Rectangle(height=10, width=10, fill_color=BLACK, fill_opacity=1, stroke_width=0)
        bg.add_updater(lambda m: m.move_to(logo, aligned_edge=RIGHT))
        text.save_state()
        text.shift((text.get_right()[0]-bg.get_right()[0]+0.2)*LEFT)
        logo.save_state()
        logo.center().scale(1.5)
        
        self.add(text, bg)
        self.play(FadeIn(logo[0]))
        self.wait()
        for i in range(3):
            self.play(MyTransform(logo[i], logo[i+1], about_point=logo.get_center()), run_time=0.25, rate_func=smooth)
        self.wait(2)
        self.play(
            text.restore, logo.restore,
            rate_func=smooth, run_time=1
        )
        self.wait()

class Test79(Scene):
    '''逐字上颜色'''
    def construct(self):
        tex = TextMobject("text or object")
        self.add(tex)
        self.wait(0.5)
        for letter in tex:
            self.play(
                LaggedStart(
                    *[
                        ApplyMethod(i.set_color, YELLOW)
                        for i in letter
                    ],
                    run_time=2
                )
            )
        self.wait()

class Test80(Scene):
    '''rate_func的细节效果'''
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.wait()
        self.play(dot.shift, RIGHT*3, rate_func=func, run_time=2)
        self.wait()

class Test81(Scene):
    '''白底logo的配色方案'''
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        logo1 = VGroup(
            Polygon(np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 2, 0])),
            Polygon(np.array([1.5, 0, 0]), np.array([3, 3, 0]), np.array([0, 3, 0])),
            Polygon(np.array([2, 0, 0]), np.array([3, 0, 0]), np.array([3, 2, 0])),
        ).set_stroke(width=0).center()
        logo1[0].set_fill("#cccccc", 1)
        logo1[1].set_fill(BLUE_D, 1)
        logo1[2].set_fill(BLUE_E, 1)
        logo1.move_to(np.array([2.5, 1, 0]))
        logo2 = logo1.copy().rotate(PI/2, about_point=ORIGIN)
        logo3 = logo2.copy().rotate(PI/2, about_point=ORIGIN)
        logo4 = logo3.copy().rotate(PI/2, about_point=ORIGIN)
        logo = VGroup(logo1, logo2, logo3, logo4).scale(0.7).center()
        logo[0][1].set_fill("#C59978", 1)
        logo[0][2].set_fill("#8D5630", 1)
        self.add(logo)

class Test82(Scene):
    def construct(self):
        tex = TextMobject("ab")
        self.add(tex)

class Test83(LogoGenerationTemplate):
    '''3B1B的logo动效，并不是想要的效果'''
    CONFIG = {
        "random_seed": 2,
    }

    def get_logo_animations(self, logo):
        layers = logo.spike_layers
        for layer in layers:
            random.shuffle(layer.submobjects)
            for spike in layer:
                spike.save_state()
                spike.scale(0.5)
                spike.apply_complex_function(np.log)
                spike.rotate(-90 * DEGREES, about_point=ORIGIN)
                spike.set_fill(opacity=0)

        return [
            FadeIn(
                logo.iris_background,
                rate_func=squish_rate_func(smooth, 0.25, 1),
                run_time=3,
            ),
            AnimationGroup(*[
                LaggedStartMap(
                    Restore, layer,
                    run_time=3,
                    path_arc=180 * DEGREES,
                    rate_func=squish_rate_func(smooth, a / 3.0, (a + 0.9) / 3.0),
                    lag_ratio=0.8,
                )
                for layer, a in zip(layers, [0, 2, 1, 0])
            ]),
            Animation(logo.pupil),
        ]

class Test84(Scene):
    '''坐标系非线性复变换'''
    def construct(self):
        grid = ComplexPlane().prepare_for_nonlinear_transform(50)
        self.add(grid)
        self.wait()
        self.play(grid.apply_complex_function, np.exp, run_time=3, rate_func=linear)
        self.wait()

class Test85(Scene):
    '''由Line+VGroup拼成的多边形无法上色'''
    def construct(self):
        vg = VGroup(
            Line(ORIGIN, RIGHT),
            Line(RIGHT, UP),
            Line(UP, ORIGIN)
        ).set_fill(BLUE, 1)
        self.add(vg)

class Test86(Scene):
    '''PointCouldDot的细节，有一个个像素点构成的点'''
    def construct(self):
        test = PointCloudDot().scale(30)
        self.add(test)

class Test87(Scene):
    '''无法用Polygon表示折线，因为Polygon强制首尾相接'''
    def construct(self):
        lines = Polygon(ORIGIN, UP, RIGHT)
        self.add(lines)

class Lines(VMobject):
    '''利用set_points_as_corner实现的折线类'''
    def __init__(self, *points, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.set_points_as_corners(points)

class Test88(Scene):
    '''上面的折线类和VGroup+Line构造的折线的ShowCreation效果相同'''
    def construct(self):
        # lines = Lines(ORIGIN, UP, RIGHT)
        lines = VGroup(
            Line(ORIGIN, UP),
            Line(UP, RIGHT)
        )
        self.play(ShowCreation(lines))

class Test89(Scene):
    '''测试PMobject，用于画点，stroke_width表示点大小'''
    def construct(self):
        points = PMobject(stroke_width=1080)
        points.add_points([ORIGIN], color=BLUE)
        self.add(points)

class Test90(Scene):
    '''mk的一次作业，测试包络线'''
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        },
    }
    def construct(self):
        circle = Circle(radius = 3, color = DARK_BLUE, plot_depth=3).flip()
        center = Dot(color=GREEN)
        A = Dot(np.array([-2, 0, 0]), color = RED)
        alpha = ValueTracker(0.0001)
        B = Dot(color=BLUE, radius=0.07, plot_depth=4)
        B.add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())))
        line1 = DashedLine(A.get_center(), B.get_center(), color=DARK_BROWN)
        line1.add_updater(lambda m: m.put_start_and_end_on(A.get_center(), B.get_center()))
        C = Dot(color=BLUE, radius=0.07, plot_depth=4)
        C.add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())).flip(axis=B.get_center()-A.get_center(), about_point=ORIGIN))
        line2 = Line(B.get_center(), C.get_center(), color=ORANGE, stroke_width=3)
        line2.add_updater(lambda m: m.put_start_and_end_on(B.get_center(), C.get_center()))

        trace = VGroup()
        self.i = 0
        def update_trace(m):
            self.i += 1
            if self.i % 4 == 0:
                m.add(line2.copy().clear_updaters())

        self.wait(3)
        self.play(ShowCreation(circle), ShowCreation(center))
        self.wait()
        self.play(ShowCreation(A))
        alpha.set_value(0.2)
        self.play(ShowCreation(B))
        self.play(alpha.increment_value, 0.6, run_time=1.5)
        self.play(alpha.increment_value, -0.6, run_time=1.6)
        self.play(ShowCreation(line1))
        self.wait()
        ra = Right_angle(corner=B.get_center(), on_the_right=False, stroke_color=BLUE)
        ra.move_corner_to(B.get_center())
        ra.change_angle_to(line1.get_angle()+PI/2)
        self.play(ShowCreation(C), ShowCreation(line2), ShowCreation(ra))
        self.wait(2)
        self.play(FadeOut(ra))
        self.play(alpha.increment_value, 0.6, run_time=1.5)
        self.play(alpha.increment_value, -0.7999, run_time=2, rate_func=linear)
        self.wait()
        self.add(trace)
        line2.set_stroke(width=2)
        self.wait(2)
        trace.add_updater(update_trace)
        alpha.set_value(0)
        anim = ApplyMethod(alpha.increment_value, 1, run_time=8, rate_func=linear)
        self.play(anim)
        self.wait(2)

        ellipse = Ellipse(width=6, height=2*np.sqrt(5), color=GREEN, plot_depth=10, run_time=2.5)
        self.play(ShowCreationThenDestruction(ellipse))
        self.wait(5)

class Test91(Scene):
    '''tex上色后会拆开'''
    def construct(self):
        tex = TexMobject("abcdefghijk")
        VGroup(tex[0][:2], tex[0][3:5]).set_color(RED)
        self.add(tex)
        self.wait()
        tex2 = VGroup(tex[0][2], tex[0][5])
        self.play(tex2.set_color, BLUE)
        self.wait(2)
        self.remove(*tex[0])
        self.wait(2)

class Test92(Scene):
    '''测试shift多参数'''
    def construct(self):
        plane = NumberPlane()
        dot = Dot().shift(RIGHT, UP, LEFT)
        self.add(plane, dot)

class Test93(Scene):
    '''测试切线，适用于所有带路径的，包括文字'''
    def construct(self):
        circle = Circle()
        text = SingleStringTexMobject("j").scale(8)
        tl = TangentLine(text[0], 0, length=5, stroke_width=1, color=BLUE)
        value = ValueTracker(0)
        tl.add_updater(
            lambda m: m.become(
                TangentLine(text[0], value.get_value(), length=5, stroke_wodth=1, color=BLUE)
            )
        )
        self.add(text, tl)
        self.wait()
        self.play(value.increment_value, 1, run_time=10, rate_func=linear)
        self.wait()

class Test94(ThreeDScene):
    '''3D移动相机中心，但是好像没有动画效果'''
    def construct(self):
        self.set_to_default_angled_camera_orientation()
        cube = Cube()
        axes = ThreeDAxes()
        self.add(axes, cube)
        self.wait()
        self.play(self.camera.frame_center.move_to, LEFT*2, run_time=3)
        self.wait()

class Test95(Scene):
    '''修Text的bug时用的，现在应该不好使了'''
    def construct(self):
        text = Text("abcdefghijklmnopqrstuvwkyz", font="庞门正道标题体", fill_opacity=0, debug=True).scale(1).set_stroke(width=5, opacity=1)
        diff = VGroup(
            Text("庞门正道标题体", font="庞门正道标题体", fill_opacity=0).scale(1).set_stroke(width=5, opacity=1),
            Text("庞门正道标题体", font="庞门正道标题体", fill_opacity=0, debug=True).scale(1).set_stroke(width=5, opacity=1)
        ).arrange(DOWN)
        # points = text[0].get_points()
        # print(points)
        self.add(diff)
        # debugTeX(self, points, 0.2)

class Test96(Scene):
    '''修Text的bug时用的，现在应该不好使了'''
    def construct(self):
        text = Text("a  b", font="庞门正道标题体",      debug=True).scale(3).shift(UP*2)
        text3 = Text("abcd", font="庞门正道标题体",     debug=True).scale(3).shift(DOWN*2)
        text4 = Text("啦 啦 啦", font="庞门正道标题体", debug=True).scale(3).shift(UP*2)
        dot = Dot(ORIGIN, color=BLUE)
        self.add(dot)
        self.wait()
        self.play(Write(text))
        self.wait(2)
        self.play(Transform(text, text3))
        self.wait(2)
        self.play(Transform(text, text4))
        self.wait(3)
        
class Test97(Scene):
    '''修Text的bug时用的，现在应该不好使了'''
    def construct(self):
        text = VGroup(
            Text("manim", font="庞门正道标题体", debug=True).set_stroke(width=15, opacity=0.5),
            Text("manim", font="庞门正道标题体", debug=True, fill_opacity=0).set_stroke(width=5)
        ).scale(8).arrange(DOWN)
        self.add(text)
        for i in range(5):
            points = text[1][i].get_points()
            debugTeX(self, points)
            
class Test98(Scene):
    '''修Text的bug时用的，现在应该不好使了'''
    def construct(self):
        text = VGroup(
            Text("a  b", font="庞门正道标题体", debug=False).scale(3).shift(UP*1.5),
            Text("a  b", font="庞门正道标题体").scale(3).shift(DOWN*1.5),
        )
        comment = VGroup(
            Text("before:", font="Consolas").scale(2).next_to(text[0], LEFT, buff=1),
            Text("after:", font="Consolas").scale(2).next_to(text[1], LEFT, buff=1),
        )
        self.add(text, comment)
        for i in text:
            debugTeX(self, i, 0.8)

class Test99(Scene):
    '''修Text的bug时用的，现在应该不好使了'''
    def construct(self):
        title = Text("default size compare", font="Consolas", color=BLUE).scale(1.5).shift(UP*2)
        text = VGroup(
            VGroup(
                Text("before", font="Consolas").scale(2),
                TextMobject("before"),
            ).arrange(RIGHT),
            VGroup(
                Text("after", font="Consolas"),
                TextMobject("after"),
            ).arrange(RIGHT),
        ).arrange(DOWN, buff=1)
        self.add(text, title)

class Test100(Scene):
    '''测试ImageMobject导入gif，只保留第一帧，无动图'''
    def construct(self):
        img = ImageMobject("Test96.gif")
        self.add(img)
        self.wait(5)

class Test101(Scene):
    '''试验黑背景遮罩'''
    CONFIG = {
        "reverse_order": False,
    }
    def construct(self):
        img = ImageMobject("latexlive.png", height=8)
        self.add(img)
        rects = VGroup(*[Rectangle() for x in range(2)])
        rects.set_stroke(width=0)
        rects.set_fill(GREY, 0.5)
        rects.set_height(2.2, stretch=True)
        rects.set_width(7.4, stretch=True)
        rects[0].move_to(DOWN*0.1)
        rects[1].set_height(1.5, stretch=True)
        rects[1].set_width(3, stretch=True)
        rects[1].move_to(DOWN*2.75)
        inv_rects = VGroup()
        for rect in rects:
            fsr = FullScreenFadeRectangle()
            fsr.append_points(rect.points[::-1])
            inv_rects.add(fsr)
        inv_rects.set_fill(BLACK, 0.7)
        self.wait(2)
        self.play(VFadeIn(inv_rects[0]))
        self.wait(2)
        self.play(Transform(inv_rects[0], inv_rects[1]))
        self.wait(2)
        self.play(VFadeOut(inv_rects[0]))
        self.wait(2)

class Test102(Scene):
    '''同大小Image的Transform'''
    def construct(self):
        img1 = ImageMobject("latexlive.png", height=8)
        img2 = ImageMobject("latexhelp.png", height=8)
        self.add(img1)
        self.wait(2)
        self.play(
            Transform(img1, img2), run_time=2
        )
        self.wait(2)

class Test103(Scene):
    '''测试Code'''
    def construct(self):
        helloworldcpp = Code(
            "helloworldcpp.cpp",
            tab_width=4,
            insert_line_no=True,
            style="autumn",
            background_stroke_color=BLACK,
            background="window",
            language="cpp",
        )
        self.add(helloworldcpp)

class Test104(Scene):
    '''修Text的bug时用的'''
    def construct(self):
        text1 = Text("  ab\ncd", font="Consolas", size=2)
        text2 = Text("ef\ngh", font="Consolas", size=2)
        self.add(text1)
        self.wait()
        self.play(Transform(text1, text2))
        self.wait()

class Test105(Scene):
    '''修Text的bug时用的'''
    def construct(self):
        text = Text("  ab\ncd\nef", font="Consolas", size=2)
        text2 = Text("ab\n  cd\nef", font="Consolas", size=2)
        text[2].set_color(YELLOW)
        self.add(text)
        self.wait()
        self.play(Transform(text, text2))
        self.wait()
        debugTeX(self, text)

class Test106(Scene):
    '''https://github.com/3b1b/manim/pull/1072'''
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        plane = NumberPlane(axis_config={"stroke_color": BLACK})
        plane.add_coordinates(number_config={"color": BLACK})
        self.add(plane)

class Test107(Scene):
    '''临时做的一张图'''
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        main = Text("粉丝问答", font="思源黑体 CN Heavy", color=BLACK).set_width(6)
        comment = Text("(凑够9张图)", font="思源黑体 CN Light", color=BLUE_D)
        comment.next_to(main, DOWN)

        self.add(main, comment)

class Test108(Scene):
    '''https://github.com/3b1b/manim/issues/1095'''
    CONFIG = {
        "v_coord_strings" : ["-1", "2"],
    }
    def construct(self):
        rule = TexMobject(
            "\\text{Transformed}\\vec{\\textbf{v}}",
            " = %s"%self.v_coord_strings[0],
            "(\\text{Transformed}\\hat{\\imath})",
            "+%s"%self.v_coord_strings[1],
            "(\\text{Transformed}\\hat{\\jmath})",
        )
        self.add(rule)

class Test109(Scene):
    '''生成README中的头图'''
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        logo = Logo(black_bg=False).set_height(2)
        img = ImageMobject("Tony.png").set_height(2)
        Group(logo, img).arrange(RIGHT, buff=1.5).center()
        line = Line(UP, DOWN, stroke_width=8, color=BLACK).move_to(mid(logo.get_right(), img.get_left()))
        line.set_length(1.4)
        text = VGroup(
            Text("Manim-Kindergarten", font="Orbitron", color=DARK_GRAY),
            Text("鹤翔万里", font="庞门正道标题体", color=BLACK, size=2.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(img, buff=0.5)
        text[0][0].set_color(logo.color_2[2])
        text[0][6].set_color(logo.color_1[2])
        self.add(logo, img, line, text)
        Group(*self.mobjects).center()

class Test110(Scene):
    """给cigar的头图，效果不太好"""
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        logo = Logo(black_bg=False).set_height(2)
        img = ImageMobject("cigar.png").set_height(2)
        Group(logo, img).arrange(RIGHT, buff=1.5).center()
        line = Line(UP, DOWN, stroke_width=8, color=BLACK).move_to(mid(logo.get_right(), img.get_left()))
        line.set_length(1.4)
        text = VGroup(
            Text("Manim-Kindergarten", font="Orbitron", color=DARK_GRAY),
            Text("cigar666", font="庞门正道标题体", color=BLACK, size=2.1)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(img, buff=0.5)
        text[0][0].set_color(logo.color_2[2])
        text[0][6].set_color(logo.color_1[2])
        self.add(logo, img, line, text)
        Group(*self.mobjects).center()

class Test111(Scene):
    """Fade和VFade的区别"""
    def construct(self):
        sq = VGroup(
            Square(stroke_width=15, color=RED, opacity=0.5, fill_opacity=0.8),
            Square(stroke_width=15, color=RED, opacity=0.5, fill_opacity=0.8),
        ).arrange(RIGHT, buff=1)
        texts = VGroup(
            Text("FadeIn", font="Consolas", size=1.3).next_to(sq[0], DOWN),
            Text("VFadeIn", font="Consolas", size=1.3).next_to(sq[1], DOWN),
        )
        text = VGroup(
            Text("FadeOut", font="Consolas", size=1.3).next_to(sq[0], DOWN),
            Text("VFadeOut", font="Consolas", size=1.3).next_to(sq[1], DOWN),
        )
        self.add(texts)
        self.wait()
        self.play(
            FadeIn(sq[0]),
            VFadeIn(sq[1]),
            run_time=3
        )
        self.wait()
        self.play(Transform(texts[0], text[0]), Transform(texts[1], text[1]))
        self.wait()
        self.play(
            FadeOut(sq[0]),
            VFadeOut(sq[1]),
            run_time=3
        )
        self.wait()

class Test112(Scene):
    """给VGroup用for循环施加updater，需要转换全局变量i为局部变量n"""
    def construct(self):
        ups = VGroup(
            *[
                Dot(color=BLUE).move_to([i, 1, 0])
                for i in range(-3, 4)
            ]
        )
        downs = VGroup(
            *[
                Dot(color=YELLOW).move_to([i, -1, 0])
                for i in range(-3, 4)
            ]
        )
        lines = VGroup(
            *[
                Line(ups[i], downs[i])
                for i in range(0, 7)
            ]
        )
        for i in range(7):
            lines[i].add_updater(lambda m, n=i: m.put_start_and_end_on(ups[n].get_bottom(), downs[n].get_top()))
        self.add(ups, downs, lines)
        self.wait()
        self.play(
            ups.shift, LEFT * 2
        )
        self.play(
            downs.shift, RIGHT * 2
        )
        self.wait()

class Test113(Scene):
    def construct(self):
        svg = SVGMobject("afed61182cb6d368.svg")
        self.add(svg)

class Test114(Scene):
    """字母也能做切线"""
    def construct(self):
        ratio = ValueTracker(0)
        text = TexMobject("S", fill_opacity=0, stroke_width=2).set_height(7)
        point = Dot().add_updater(
            lambda m: m.move_to(text[0][0].point_from_proportion(ratio.get_value()))
        )
        self.add(text, point)
        self.wait()
        self.play(ratio.set_value, 1, run_time=3, rate_func=linear)
        self.wait()

class Test115(Scene):
    """Write的具体细节"""
    def construct(self):
        text = TextMobject("+").set_height(5)
        self.wait()
        progress = NumberLine(x_min=0, x_max=1, unit_size=10, tick_frequency=0.5).center().to_edge(DOWN)
        alpha = ValueTracker(0)
        tick = Triangle(fill_opacity=1).scale(0.2).rotate(PI)
        tick.add_updater(lambda m: m.move_to(progress.n2p(alpha.get_value()), aligned_edge=DOWN))
        self.add(progress, tick)
        self.play(Write(text, stroke_width=30), alpha.set_value, 1, run_time=5, rate_func=linear)
        self.wait()

class Test116(Scene):
    def construct(self):
        test = ParametricFunction(
            lambda t: np.array([
                2*np.sin(3*t)*np.cos(t),
                2*np.sin(3*t)*np.sin(t),
                0
            ]),
            t_min=0, t_max=2*PI,
        )
        debugTeX(self, test.points)
        self.add(test)

class Test117(Scene):
    def construct(self):
        grid = NumberPlane(
            center_point=LEFT*3,
            x_max=15
        )
        self.add(grid)

class Test118(Scene):
    """好像是测试妈咪叔的latexlive写的"""
    def construct(self):
        text = TextMobject("\\begin{equation}  x = a_0 \+ \\cfrac{1}{a_1           \+ \\cfrac{1}{a_2           \+ \\cfrac{1}{a_3 \+ \\cfrac{1}{a_4} } } }\\end{equation}")
        self.add(text)

class Test119(Scene):
    """mk的logo"""
    def construct(self):
        logo = Logo().set_height(8)
        self.add(logo)


class Test120(Scene):
    """MaintainPositionRelativeTo"""
    def construct(self):
        dot = Dot()
        circle = Circle()
        triangle = Triangle()

        self.play(
            Write(circle),
            Write(dot),
            Write(triangle),
            run_time=3
        )
        self.play(
            dot.shift, UP,
            MaintainPositionRelativeTo(triangle, dot)
        )

class Test121(Scene):
    """VectorizedPoint不会被显示"""
    def construct(self):
        v = VectorizedPoint([1, 1, 0], stroke_width=10, stroke_opacity=1, fill_opacity=0, color=YELLOW, artificial_width=10, artificial_height=10)
        self.add(v)

class Test122(Scene):
    """StreamLines"""
    def construct(self):
        sl = StreamLines(
            lambda p: rotate_vector(p / 3, 90 * DEGREES), color_by_magnitude=True, color_by_arc_length=False
        )
        self.add(sl)
        self.wait()
        self.play(ShowPassingFlashWithThinningStrokeWidth(sl))
        self.wait()

class Test123(Scene):
    """和Test112类似"""
    def construct(self):
        heights = [2, 3, 5, 7, 9]
        trackers = [ValueTracker(h) for h in heights]
        num_tex = [DecimalNumber(t.get_value())\
                .add_updater(lambda v, x=t: v.set_value(x.get_value()))\
                for t in trackers
                ]
        for i in range(len(num_tex)):
            tex = num_tex[i]
            tex.shift(i*RIGHT)
            self.play(Write(tex))

class Test124(Scene):
    """discord上有个人问的动画"""
    def construct(self):
        tex = TexMobject("f(n)+f(n)=2f(n)")
        self.wait()
        self.play(Write(tex[0][:9]))
        self.play(Write(tex[0][9]))
        self.wait()
        self.play(
            TransformFromCopy(tex[0][:4], tex[0][-4:]),
            TransformFromCopy(tex[0][5:9], tex[0][-4:].copy()),
            FadeInFrom(tex[0][-5], RIGHT)
        )
        self.wait()

class Test125(Scene):
    """同上"""
    def construct(self):
        tex = TexMobject("f(n)+f(n)")
        two = TexMobject("2").next_to(tex, LEFT, buff=0.02)
        self.wait()
        self.play(Write(tex))
        self.wait()
        self.play(
            Transform(tex[0][5:], tex[0][:4].copy()),
            FadeOut(tex[0][4]),
            Write(two)
        )
        self.wait()

class Test126(Scene):
    """给LaTeX改字体，失败了qwq"""
    def construct(self):
        text = TextMobject("测试字体test")
        self.add(text)

class Test127(Scene):
    """和Axes有关的测试"""
    def construct(self):
        axes = Axes(
            x_min=-14, x_max=14,
            y_min=-8,  y_max=8,
            number_line_config={
                "unit_size": 0.5,
                "tick_frequency": 2,
            }
        )
        axes.add_coordinates(
            [-6, -4, -2, 2, 4, 6],
            [-4, -2, 2, 4]
        )
        graph = VGroup()
        graph.add(axes.get_graph(lambda x: -(np.exp(-x)-3), color=RED, x_min=-2.9))
        graph.add(axes.get_graph(lambda x: x, color=PURPLE))
        graph.add(axes.get_graph(lambda x: -np.log(3-x), color=BLUE, step_size=0.001))
        self.add(axes, graph)

class Test128(Scene):
    """给action_renderer项目做的头图"""
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        logo = Logo(black_bg=False).set_height(2)
        img = ImageMobject("action.png").set_height(2)
        Group(logo, img).arrange(RIGHT, buff=1.3).center()
        line = Line(UP, DOWN, stroke_width=8, color=BLACK).move_to(mid(logo.get_right(), img.get_left()))
        line.set_length(1.4)
        text = VGroup(
            Text("Manim-Kindergarten", font="Orbitron", color=DARK_GRAY),
            Text("manim_action_renderer", font="庞门正道标题体", color=BLACK, size=1.4)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(img, buff=0.5)
        text[0][0].set_color(logo.color_2[2])
        text[0][6].set_color(logo.color_1[2])
        self.add(logo, img, line, text)
        Group(*self.mobjects).center()

class Test129(Scene):
    """updater中特判点重合"""
    def construct(self):
        A = Dot(3 * RIGHT)
        B = Dot(2 * RIGHT)
        label_A = TexMobject('A').next_to(A, DOWN, buff=SMALL_BUFF)
        label_B = TexMobject('B').next_to(B, DOWN, buff=SMALL_BUFF)

        m = -5*RIGHT
        C = A.copy()
        l = Line(A.get_center(), C.get_center())
        label_C = TexMobject('C').next_to(C, UP, buff=SMALL_BUFF)
        label_C.add_updater(lambda m: m.next_to(C, UP, buff=SMALL_BUFF))

        def up_loca(mbj):
            if all(A.get_center() == C.get_center()):
                pass
            else:
                mbj.put_start_and_end_on(A.get_center(), C.get_center())

        l.add_updater(up_loca)
        self.add(A, B, label_A, label_B, label_C, l)
        self.play(C.move_to, m, run_time=5)
