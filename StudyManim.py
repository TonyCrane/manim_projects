'''
  > File Name        : StudyManim.py
  > Author           : Tony
  > Created Time     : 2019/01/26 16:19:55
'''

from manimlib.imports import *
from manim_projects.tony_useful.imports import *

class Polygon(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        square = Square()

        self.play(ShowCreation(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(square))

class TextTransform(Scene):
    def construct(self):
        text = TextMobject(
            "this is a text",
            tex_to_color_map={"text": YELLOW}
        )
        trans_text = TextMobject(
            "this is another text",
            tex_to_color_map={"text": RED}
        )
        self.play(Write(text))
        self.play(Transform(text, trans_text))
        self.wait()

class TexTransform(Scene):
    def construct(self):
        tex = TexMobject(
            "\\sum_{n=1010a}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\tau^2}{6}"
        )
        trans_tex = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        self.play(Write(tex))
        self.play(Transform(tex, trans_tex))
        self.wait()

class MoveText(Scene):
    def construct(self):
        title = TextMobject(
            "Tony is trying manim",
            tex_to_color_map={"manim": RED}
        )
        trans_title = TextMobject(
            "Tony is learning manim",
            tex_to_color_map={"manim": YELLOW}
        )
        trans_title.to_corner(UP)
        transform_title = TextMobject(
            "Tony is learning manim",
            tex_to_color_map={"manim": ORANGE}
        )
        transform_title.to_corner(UP + LEFT)

        self.play(Write(title))
        self.play(Transform(title, trans_title))
        self.wait()
        self.play(Transform(title, transform_title))
        self.wait()

class GaussLaw(Scene):
	def construct(self):
		example_text = TextMobject(
			"Gauss's Law 高斯定理",
			tex_to_color_map={"Law": RED}
		)
		example_tex = TexMobject(
			"\\def\\ooint{{\\bigcirc}\\kern-12.5pt{\\int}\\kern-6.5pt{\\int}}"
			"\\ooint_S{E\\cdot dS} = {1\\over{\\epsilon_0}}\\times{{\\int}\\kern-6.5pt{\\int}\\kern-6.5pt{\\int}_V{\\rho \\cdot dV}}",
		)
		group = VGroup(example_text, example_tex)
		group.arrange_submobjects(DOWN)
		group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

		self.play(Write(example_text))
		self.play(Write(example_tex))
		self.wait()

class PrintAuthor(Scene):
    def construct(self):
        author = TextMobject(
            "@Tony鹤翔万里",
            tex_to_color_map={"@Tony鹤翔万里": [BLUE, YELLOW, ORANGE, RED]}
        )
        author.scale(1.5)
        author.to_corner(LEFT + DOWN)
        self.add(author)

class NumberPlaneTest(Scene):
    def construct(self):
        grid = NumberPlane()
        grid_title = TextMobject("空间坐标系")
        grid_title.scale(1.5)
        grid_title.to_corner(UP)

        self.play(
            Write(grid),
            FadeInFromDown(grid_title),
        )
        self.wait()
        grid_transform_title = TextMobject("放大")
        grid_transform_title.to_corner(UP)
        grid_transform_title.scale(1.5)
        grid.prepare_for_nonlinear_transform()
        self.play(
            Transform(grid_title, grid_transform_title),
            grid.apply_function,
            lambda p: p * np.array([ 2, 2, 0, ]),
            run_time=3,
        )
        self.wait()
        grid.prepare_for_nonlinear_transform()
        grid_transform_title = TextMobject("平移")
        grid_transform_title.to_corner(UP)
        grid_transform_title.scale(1.5)
        self.play(
            Transform(grid_title, grid_transform_title),
            grid.apply_function,
            lambda p: p + np.array([2, 1, 0, ]),
            run_time=3,
        )
        self.wait()
        grid.prepare_for_nonlinear_transform()
        grid_transform_title = TextMobject("线性变换")
        grid_transform_title.to_corner(UP)
        grid_transform_title.scale(1.5)
        self.play(
            Transform(grid_title, grid_transform_title),
            grid.apply_function,
            lambda p: p + np.array([ p[1] , 0, 0,]),
            run_time=3,
        )
        self.wait()
        grid.prepare_for_nonlinear_transform()
        grid_transform_title = TextMobject("非线性变换")
        grid_transform_title.to_corner(UP)
        grid_transform_title.scale(1.5)
        self.play(
            Transform(grid_title, grid_transform_title),
            grid.apply_function,
            lambda p: p + np.array([ np.sin(p[1]) , np.sin(p[0]) , 0,]),
            run_time=3,
        )

class VideoStart(Scene):
    CONFIG = {
        "Author"        : "@鹤翔万里",
        "title_name"    : "测试",
        "svg_filename"  : "TonySVG",
        "author_colors" : [BLUE, YELLOW, ORANGE, RED],
    }
    def construct(self):
        author = TextMobject(
            self.Author,
            tex_to_color_map={self.Author : self.author_colors}
        )
        svg_file = SVGMobject(file_name = self.svg_filename)
        svg_file.to_corner(UP)

        title = TextMobject(self.title_name)
        title.to_corner((BOTTOM + ORIGIN))
        self.play(
            FadeInFromDown(svg_file),
            Write(author)
        )
        self.play(
            Write(title)
        )
        self.wait()
        self.play(
            LaggedStart(FadeOutAndShiftDown, author),
            FadeOut(title),
            run_time = 0.5,
        )

class TrySurroundingRectangle(Scene):
    def construct(self):
        text = TextMobject(
            "Here is a ", "text",
        )
        text.to_edge(TOP)
        text_rect = SurroundingRectangle(text[1])
        another_text = TextMobject(
            "That ", "text", " is created by Tony"
        )
        another_text_rect = SurroundingRectangle(another_text[1])
        text_arrow = Arrow(
            another_text[1].get_top(), text[1].get_bottom(),
            tip_length = 0.1
        )

        trans_text_1 = TextMobject("TEXT", tex_to_color_map={"TEXT": BLUE})
        trans_text_2 = TextMobject("TEXT", tex_to_color_map={"TEXT": BLUE})
        trans_text_1.move_to(text[1])
        trans_text_2.move_to(another_text[1])

        self.play(Write(text))
        self.play(ShowCreation(text_rect))
        self.wait()
        self.play(Write(another_text), run_time=1)
        self.play(ShowCreation(another_text_rect))
        self.play(ShowCreation(text_arrow), run_time=1.5)
        self.wait()
        self.play(
            Transform(text[1], trans_text_1),
            Transform(another_text[1], trans_text_2)
        )
        self.wait()

class TryMatrix(Scene):
    def construct(self):
        matrix = Matrix(
            [["0", 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1, 0, 1, 0]]
        )
        self.play(Write(matrix), run_time = 3)
        trans = TextMobject("1").move_to(matrix[0][9])
        self.play(
            Transform(matrix[0][9], trans)
        )
        self.wait()

class TransformPartOfTex(Scene):
    def construct(self):
        gauss = TexMobject(
            "\\def\\ooint{{\\bigcirc}\\kern-12.5pt{\\int}\\kern-6.5pt{\\int}}"
			"\\ooint_S{E\\cdot dS} = {1\\over{\\epsilon_0}}\\times{{\\int}\\kern-6.5pt{\\int}\\kern-6.5pt{\\int}", "_{Sh}", "{\\rho \\cdot dV}}",
        )
        self.play(Write(gauss))
        trans_tex = TexMobject("_{V}")
        trans_tex.move_to(gauss[1])
        self.play(
            Transform(gauss[1], trans_tex)
        )
        self.wait()
        text = TextMobject("V", tex_to_color_map={"V": BLUE})
        text.next_to(gauss[1], direction=UP, buff=2)
        self.play(
            Transform(trans_tex, text)
        )
        text_rect = SurroundingRectangle(text)
        self.play(ShowCreation(text_rect))
        self.wait()

class TryVideoSeries(Scene):
    def construct(self):
        series = VideoSeries(num_videos=6)
        series.scale(0.8)
        series.arrange_submobjects(RIGHT, aligned_edge=LEFT, buff=1.6)
        series.to_edge(UP, buff=1)
        this_video = series[0]
        this_video.set_color(YELLOW)
        this_video.save_state()
        this_video.set_fill(opacity = 0)
        this_video.center()
        this_video.set_height(FRAME_HEIGHT)

        self.play(
            FadeIn(
                series,
                lag_ratio = 0.5,
                run_time = 2
            )
        )
        self.wait()
        self.play(
            this_video.restore, run_time=3
        )
        self.wait(2)
        
class TryOmega(Scene):
    def construct(self):
        omega = SVGMobject("OmegaCreatures_plain")
        omega.set_width(3).set_color(BLUE)
        self.add(omega)

class TryOmegaCreature(TeacherStudentsScene):
    def construct(self):
        self.student_says(
            "尝试一下$\omega$酱",
            run_time = 2
        )
        # self.play(self.get_teacher().change_mode, "happy")
        self.wait()
        self.teacher_says(
            "还可以吧 \\\\",
            "虽然没有$\pi$酱好看",
            # target_mode = "well"
        )
        self.wait()

class TryFont(Scene):
    def construct(self):
        # text = Text("test fonts", font='Consolas').shift(UP*2)
        # text2 = Text("test      blanks", font='Consolas').next_to(text, DOWN)
        # text3 = Text("test \n test", font='Consolas').next_to(text2, DOWN)
        text = Text(
            "line1\n"
            "line3",
            font='Consolas'
        )
        self.add(text)

class TryCode(Scene):
    def construct(self):
        code = Code(
            "#include <bits/stdc++.h>",
            "using namespace std; ",
        )
        self.play(Write(code))

class TryLinedCode(Scene):
    def construct(self):
        code = LinedCode(
            "#include <bits/stdc++.h>",
            "using namespace std;",
            "",
            "int main() {",
            "    printf(\"Hello World\\n\");",
            "    return 1;",
            "}",
        )
        self.play(Write(code))