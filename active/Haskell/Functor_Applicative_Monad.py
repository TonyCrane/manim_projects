import functools
import types
from numpy import radians
from numpy.core.fromnumeric import put
import screeninfo
from manimlib import *


code_t2c = {
    "0": PURPLE,
    "1": PURPLE,
    "2": PURPLE,
    "3": PURPLE,
    "4": PURPLE,
    "5": PURPLE,
    "6": PURPLE,
    "7": PURPLE,
    "8": PURPLE,
    "9": PURPLE,
    "+": RED,
    "*": RED,
    "(": GREY_B,
    ")": GREY_B,
    "->": RED,
    "=>": RED,
    "::": RED,
    "==": RED,
    "\\": RED,
    "Maybe": BLUE,
    "[]": BLUE,
    "IO": BLUE,
    "Int": BLUE_B,
    "String": BLUE_B,
    "Just": BLUE_A,
    "Nothing": BLUE_A,
    "fmap": GREEN,
    "<*>": GREEN,
    ">>=": GREEN,
    "Functor": BLUE_D,
    "Applicative": BLUE_D,
    "Monad": BLUE_D,
    "~": "#333333",
    "\"": GREY_B,
    "name": YELLOW_D,
    "content": YELLOW_D,
}


class TexIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        for index, single_tex in enumerate(obj):
            tex_index = Integer(index, background_stroke_width=2) \
                .scale(self.scale_factor).set_color(self.color)
            tex_index.move_to(single_tex.get_center())
            self.add(tex_index)


class PointIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        # digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        for index, points in enumerate(obj.get_points()):
            point_id = Integer(index, background_stroke_width=2) \
                .scale(self.scale_factor).set_color(self.color)
            point_id.move_to(points)
            self.add(point_id)


class RT(ReplacementTransform):
    pass


class EmptyDot(Dot):
    CONFIG = {
        "fill_opacity": 0,
        "stroke_width": 0,
    }


class SemiBoldText(Text):
    CONFIG = {
        "font": "Source Han Serif CN",
        "weight": "SEMIBOLD"
    }


class SerifText(Text):
    CONFIG = {
        "font": "Source Han Serif CN"
    }


class TextForHaskell(Text):
    CONFIG = {
        "font": "JetBrains Monaco",
    }
    replace_map = {
        "->": "啊",
        "=>": "跛",
        "::": "呲",
        "<*>": "嘚",
        ">>=": "锕",
        "==": "梻",
    }
    def apply_space_chars(self):
        self.text = self.replace_ligtures(self.text)
        super().apply_space_chars()
    
    def find_indexes(self, word):
        word = self.replace_ligtures(word)
        return super().find_indexes(word)
    
    def replace_ligtures(self, word):
        for k, v in self.replace_map.items():
            word = word.replace(k, v)
        return word


class Haskell(TextForHaskell):
    CONFIG = {
        "t2c": code_t2c,
    }


class RoundedRectangle_(RoundedRectangle):
    def round_corners(self, radius=0.5):
        vertices = self.get_vertices()
        arcs = []
        for v1, v2, v3 in adjacent_n_tuples(vertices, 3):
            vect1 = v2 - v1
            vect2 = v3 - v2
            unit_vect1 = normalize(vect1)
            unit_vect2 = normalize(vect2)
            angle = angle_between_vectors(vect1, vect2)
            angle *= np.sign(radius)
            cut_off_length = radius * np.tan(angle / 2)
            sign = np.sign(np.cross(vect1, vect2)[2])
            arc = ArcBetweenPoints(
                v2 - unit_vect1 * cut_off_length,
                v2 + unit_vect2 * cut_off_length,
                angle=sign * angle,
                n_components=2,
            )
            arcs.append(arc)
        self.clear_points()
        arcs = [arcs[-1], *arcs[:-1]]
        for arc1, arc2 in adjacent_pairs(arcs):
            self.append_points(arc1.get_points())
            line = Line(arc1.get_end(), arc2.get_start())
            self.append_points(line.get_points())
        return self


class Box(VGroup):
    CONFIG = {
        "corner_radius": 0.2
    }
    def __init__(self, width, height, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.create_box(width, height)
    
    def create_box(self, width, height):
        box = RoundedRectangle_(
            width=width,
            height=height,
            corner_radius=self.corner_radius,
        )
        points = box.get_points()
        top = VGroup()
        top.set_points(points[:15])
        bottom = VGroup()
        bottom.set_points(points[15:])

        # lock = Rectangle(width=0.06, height=0.2, fill_color=WHITE, fill_opacity=1, stroke_width=0)
        # lock.next_to(points[0], RIGHT, buff=0)
        # top.add(lock)

        self.top = top 
        self.bottom = bottom
        self.add(top, bottom)
    
    def open(self):
        points = self.top.get_points()
        self.top.rotate(PI - 10*DEGREES, about_point=points[14])
        return self
    
    def copy(self):
        return self.deepcopy()


class FunctionBox(VGroup):
    CONFIG = {
        "lines_length": 0.6,
        "rotate_degrees": 20*DEGREES,
    }

    def __init__(self, content, **kwargs):
        VGroup.__init__(self, **kwargs)
        # self.func = Text(content, color="#333333", background_stroke_color="#333333")
        self.func = content
        self.create_box()
    
    def create_box(self):
        box_ = SurroundingRectangle(
            self.func, buff=0.1, 
            fill_opacity=0, fill_color=WHITE, 
            stroke_width=0
        )
        vertices = box_.get_vertices()
        box = VGroup(
            Line(vertices[0], vertices[1], stroke_color=WHITE),
            Line(vertices[2], vertices[3], stroke_color=WHITE),
        )
        input_lines = VGroup(
            Line(vertices[1], vertices[1] + LEFT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=IN , about_point=vertices[1]),
            Line(vertices[2], vertices[2] + LEFT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=OUT, about_point=vertices[2]),
        )
        output_lines = VGroup(
            Line(vertices[0], vertices[0] + RIGHT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=OUT, about_point=vertices[0]),
            Line(vertices[3], vertices[3] + RIGHT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=IN , about_point=vertices[3]),
        )
        self.box = box
        self.lines = VGroup(input_lines, output_lines)
        self.add(self.lines) 
        self.add(box)


class KleisliBox(FunctionBox):
    def create_box(self):
        box_ = SurroundingRectangle(
            self.func, buff=0.1, 
            fill_opacity=0, fill_color=WHITE, 
            stroke_width=0
        )
        box_.set_height(box_.get_height()*4/3, stretch=True)
        vertices = box_.get_vertices()
        box = VGroup(
            Line(vertices[0], vertices[1], stroke_color=WHITE),
            Line(vertices[2], vertices[3], stroke_color=WHITE),
        )
        input_lines = VGroup(
            Line(vertices[1], vertices[1] + LEFT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=IN , about_point=vertices[1]),
            Line(vertices[2], vertices[2] + LEFT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=OUT, about_point=vertices[2]),
        )
        output_lines = VGroup(
            Line(vertices[0], vertices[0] + RIGHT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=OUT, about_point=vertices[0]),
            Line(vertices[3], vertices[3] + RIGHT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=IN , about_point=vertices[3]),
        )
        output_lines.set_width(output_lines.get_width()*2/3, stretch=True, about_edge=LEFT)
        output_lines.add(
            Line(output_lines[0].get_end(), output_lines[0].get_end()+RIGHT*output_lines.get_width()/2),
            Line(output_lines[1].get_end(), output_lines[1].get_end()+RIGHT*output_lines.get_width()/2)
        )
        self.box = box
        self.lines = VGroup(input_lines, output_lines)
        self.add(self.lines) 
        self.add(box)


class GetLineBox(FunctionBox):
    def create_box(self):
        box_ = SurroundingRectangle(
            self.func, buff=0.1, 
            fill_opacity=0, fill_color=WHITE, 
            stroke_width=0
        )
        box_.set_height(box_.get_height()*4/3, stretch=True)
        box_.set_width(box_.get_width()*6/5, stretch=True)
        vertices = box_.get_vertices()
        box = VGroup(
            Line(vertices[0], vertices[1], stroke_color=WHITE),
            Line(vertices[1], vertices[2], stroke_color=WHITE),
            Line(vertices[2], vertices[3], stroke_color=WHITE),
        )
        output_lines = VGroup(
            Line(vertices[0], vertices[0] + RIGHT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=OUT, about_point=vertices[0]),
            Line(vertices[3], vertices[3] + RIGHT*self.lines_length, stroke_color=WHITE).rotate(self.rotate_degrees, axis=IN , about_point=vertices[3]),
        )
        output_lines.set_width(output_lines.get_width()*2/3, stretch=True, about_edge=LEFT)
        output_lines.add(
            Line(output_lines[0].get_end(), output_lines[0].get_end()+RIGHT*output_lines.get_width()/2),
            Line(output_lines[1].get_end(), output_lines[1].get_end()+RIGHT*output_lines.get_width()/2)
        )
        self.box = box
        self.lines = output_lines
        self.add(self.lines) 
        self.add(box)


class SceneWithBox(Scene):
    def openbox(self, box, radians=PI-10*DEGREES, run_time=0.45):
        self.add_sound("chestopen")
        self.play(Rotate(box.top, radians, about_point=box.top.get_points()[14], run_time=run_time))
    
    def closebox(self, box, radians=PI-10*DEGREES, run_time=0.45):
        self.add_sound("chestclosed")
        self.play(Rotate(box.top, radians, about_point=box.top.get_points()[14], run_time=run_time, axis=IN))


class Scene_(SceneWithBox):
    def make_title(self, main_title, skip_anim=False):
        title_tex = TexText(
            main_title, color=BLUE, 
            background_stroke_color=BLUE, font_size=48
        )
        titlebg = Rectangle(
            width=FRAME_WIDTH, height=0.76, 
            color=GREY_D, fill_opacity=1, stroke_width=0
        ).shift(UP*3.02)
        title_tex.move_to(titlebg).to_edge(LEFT, buff=0.75)
        sub_topic_sign = VMobject(
            fill_opacity=0, stroke_width=5, color="#333333",
        ).set_points_as_corners([[-1, 3, 0], [1, 0, 0], [-1, -3, 0]])
        sub_topic_sign.set_height(titlebg.get_height()+0.2)
        self.sub_topic_sign = sub_topic_sign
        self.titlebg = titlebg 
        self.title_tex = title_tex
        if not skip_anim:
            titlebg.save_state()
            titlebg.shift(FRAME_WIDTH * LEFT)
            self.play(titlebg.animate.restore(), rate_func=smooth, run_time=0.5)
            self.play(Write(title_tex))
            self.wait()
        else:
            self.add(titlebg, title_tex)

    def add_sub_title(self, mob, skip_anim=False):
        self.sub_topic_sign.next_to(self.title_tex, RIGHT)
        mob.next_to(self.sub_topic_sign, RIGHT)
        if not skip_anim:
            self.play(Write(self.sub_topic_sign), run_time=0.5)
            self.play(FadeIn(mob, RIGHT))
        else:
            self.add(self.sub_topic_sign, mob)
    
    def applyfunc(self, inp, out, func_box):
        inp.next_to(func_box, LEFT, buff=0)
        inp.save_state()
        inp.shift(LEFT*1)
        out.next_to(func_box, RIGHT, buff=0)

        self.play(Write(inp))
        self.play(inp.animate.restore(), rate_func=rush_into)
        self.play(FadeOut(inp, RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        self.add_sound("levelup")
        self.play(FadeIn(out, RIGHT*0.5), rate_func=rush_into, run_time=0.5)
        self.play(out.animate.shift(RIGHT), rate_func=rush_from, run_time=1)


class TestLigatures(Scene):
    def construct(self):
        text = TextForHaskell("fmap :: Functor f => (a -> b) -> f a -> f b", font="JetBrains Monaco")
        t2c = {
            "f": GOLD,
            "fmap": BLUE,
            "Functor": ORANGE,
            "=>": RED,
            "->": GREEN,
            "::": PURPLE,
        }   
        text.set_color_by_t2c(t2c)
        self.add(text)
        

class TestSound(Scene):
    def construct(self):
        circle = Circle(radius=1)
        self.add(circle)
        self.add_sound("chestopen")
        self.play(circle.animate.scale(3))
        self.wait()
        self.add_sound("chestclosed")
        self.play(circle.animate.scale(1/3))
        self.wait()


class TestBox(Scene):
    def construct(self):
        box = Box(1.5, 1.5)
        # box2 = Box(3, 1)
        # VGroup(box, box2).arrange(RIGHT)
        self.add(box)#, box2)
        # box2 = box.deepcopy().open()
        # self.add(box2)
        self.play(Rotate(box.top, PI-10*DEGREES, about_point=box.top.get_points()[14], run_time=1))
        # self.add(PointIndex(box[0], scale_factor=0.2))
        # self.add(PointIndex(box2[0], scale_factor=0.2))


class TestSceneWithBox(SceneWithBox):
    def construct(self):
        box = Box(1.5, 1.5)
        self.add(box)
        self.openbox(box)
        self.wait(2)
        self.closebox(box)
        self.wait()


class TestFunctionBox(Scene):
    def construct(self):
        box = FunctionBox("(+3)")
        self.add(box)


class TestKleisliBox(Scene):
    def construct(self):
        func = Haskell("\\x -> Just (x+1)", font_size=42)
        func = Haskell("readFile", font_size=42)
        funcbox = KleisliBox(func)
        self.add(func, funcbox)


class TestGetLineBox(Scene):
    def construct(self):
        func = Haskell("getLine", font_size=42)
        funcbox = GetLineBox(func)
        self.add(func, funcbox)


class WarningScene(Scene):
    def construct(self):
        text = VGroup(
            SemiBoldText("本期视频只是一个试验性视频", t2c={"试验性视频": RED_B}),
            VGroup(
                SemiBoldText("面向人群：", color=GOLD),
                SerifText("有一点Haskell基础"),
                SerifText("且对于Functor等概念感到困惑"),
            ).arrange(DOWN, aligned_edge=LEFT),
            SemiBoldText("（如果反馈好的话，可以考虑做一系列Haskell入门的视频）", font_size=32, color=GREY_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.75)
        text[1][1:].shift(RIGHT)

        self.play(Write(text[0]))
        self.wait()
        self.play(FadeIn(text[1:], run_time=2))
        self.wait(5)
        self.play(FadeOut(text, run_time=0.75))


class RecallFunctions(Scene_):
    def construct(self):
        self.make_title("Functions")

        subtitle = TexText(
            "Currying", color=YELLOW, 
            background_stroke_color=YELLOW, font_size=48
        )
        self.add_sub_title(subtitle)
        self.wait()

        function_example = Tex("f", background_stroke_color=WHITE, font_size=64)
        function_example_box = FunctionBox(
            function_example, lines_length=0.6
        )
        input_example = Tex("x", background_stroke_color=WHITE, font_size=60)
        output_example = Tex("f(x)", background_stroke_color=WHITE, font_size=60)

        self.wait()
        self.play(Write(function_example), run_time=0.5)
        self.play(FadeIn(function_example_box), run_time=0.5)
        self.applyfunc(input_example, output_example, function_example_box)
        self.wait(2)
        self.play(
            FadeOut(function_example_box),
            FadeOut(function_example),
            FadeOut(output_example),
            run_time=0.5
        )
        
        function = TextForHaskell("(+)", t2c=code_t2c, font_size=60)
        function_box = FunctionBox(function, lines_length=0.6)
        innum = TextForHaskell("1", t2c=code_t2c, font_size=60)
        outfunc = TextForHaskell("(+1)", t2c=code_t2c, font_size=60)

        self.wait()
        self.play(Write(function), run_time=0.5)
        self.play(FadeIn(function_box), run_time=0.5)
        self.applyfunc(innum, outfunc, function_box)
        self.play(
            FadeOut(VGroup(function, function_box), LEFT),
            outfunc.animate.center(), run_time=1
        )

        outfunc_box = FunctionBox(outfunc, lines_length=0.6)
        innum_ = TextForHaskell("2", t2c=code_t2c, font_size=60)
        outnum = TextForHaskell("3", t2c=code_t2c, font_size=60)

        innum_.next_to(outfunc_box, LEFT, buff=0)
        innum_.save_state()
        innum_.shift(LEFT*1)
        outnum.next_to(outfunc_box, RIGHT, buff=0)

        self.play(FadeIn(outfunc_box), run_time=0.5)
        self.applyfunc(innum_, outnum, outfunc_box)
        self.play(Flash(outnum.get_center(), line_length=0.3, flash_radius=0.7))

        show = TextForHaskell("show", font_size=60)
        show_box = FunctionBox(show, lines_length=0.6)
        in_ = TextForHaskell("123", t2c=code_t2c, font_size=60)
        out = TextForHaskell('"123"', t2c={'"': GREY_B, "123": YELLOW_D}, font_size=60)

        self.play(RT(outfunc, show), RT(outfunc_box, show_box), FadeOut(outnum))
        self.applyfunc(in_, out, show_box)
        self.wait()

        f = Tex("f", background_stroke_color=WHITE, font_size=64)
        fbox = FunctionBox(f, lines_length=0.6)
        inp = Tex("x", background_stroke_color=WHITE, font_size=60)
        outp = Tex("f(x)", background_stroke_color=WHITE, font_size=60)

        self.play(RT(show, f), RT(show_box, fbox), FadeOut(out))

        inp.next_to(fbox, LEFT, buff=0)
        outp.next_to(fbox, RIGHT, buff=0)
        inp_ = inp.copy()

        self.play(Write(inp))
        self.add(inp_)
        self.play(FadeOut(inp, RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        self.add_sound("levelup")
        self.play(FadeIn(outp, RIGHT*0.5), rate_func=rush_into, run_time=0.5)

        typesign = TextForHaskell("a -> b", font_size=64, t2c=code_t2c).next_to(fbox, UP, buff=0.75)
        self.play(
            TransformFromCopy(inp_, typesign[0]),
            TransformFromCopy(outp, typesign[-1]),
        )
        self.play(Write(typesign[2]), run_time=0.5)
        self.wait()
        title2 = TexText(
            "Type constructors", color=BLUE, 
            background_stroke_color=BLUE, font_size=48
        ).move_to(self.titlebg).to_edge(LEFT, buff=0.75)
        self.play(
            VGroup(inp_, outp, typesign, f, fbox).animate.scale(0.75).shift(DOWN*0.75).to_edge(LEFT).fade(0.5),
            FadeOut(self.sub_topic_sign), FadeOut(subtitle),
        )
        self.play(RT(self.title_tex, title2))


class RecallTypeConstructors(Scene_):
    def construct(self):
        # < from previous scene
        self.make_title("Type constructors", skip_anim=True)
        func = VGroup(
            TextForHaskell("a -> b", font_size=64, t2c=code_t2c),
            Tex("f", background_stroke_color=WHITE, font_size=64),
            Tex("x", background_stroke_color=WHITE, font_size=60),
            Tex("f(x)", background_stroke_color=WHITE, font_size=60),
        )
        func.add(FunctionBox(func[1], lines_length=0.6))
        func[2].next_to(func[-1], LEFT, buff=0)
        func[3].next_to(func[-1], RIGHT, buff=0)
        func[0].next_to(func[-1], UP, buff=0.75)
        func.save_state()
        func.scale(0.75).shift(DOWN*0.75).to_edge(LEFT).fade(0.5)
        self.add(func)
        # from previous scene >

        constructors = VGroup(
            TextForHaskell("Maybe", t2c=code_t2c, font_size=64),
            TextForHaskell("[]", t2c=code_t2c, font_size=64),
            TextForHaskell("IO", t2c=code_t2c, font_size=64),
            TextForHaskell("Maybe", t2c=code_t2c, font_size=64),
        ).arrange(ORIGIN, aligned_edge=RIGHT)
        typeint = TextForHaskell("Int", t2c=code_t2c, font_size=64)
        VGroup(constructors, typeint).arrange(RIGHT, buff=0.5)
        VGroup(constructors[0], constructors[-1]).shift(DOWN*0.05)
        self.play(Write(typeint))
        self.play(FadeIn(constructors[0], DOWN), run_time=0.5)
        self.play(
            FadeIn(constructors[1], DOWN),
            FadeOut(constructors[0], DOWN), run_time=0.5
        )
        self.play(
            FadeIn(constructors[2], DOWN),
            FadeOut(constructors[1], DOWN), run_time=0.5
        )
        self.play(
            FadeIn(constructors[3], DOWN),
            FadeOut(constructors[2], DOWN), run_time=0.5
        )
        maybeint = VGroup(constructors[3], typeint)
        
        kind = TextForHaskell("* -> *", t2c=code_t2c, font_size=60).next_to(constructors[3], UP, buff=0.75)
        self.wait()
        self.play(TransformFromCopy(typeint, kind[0]), run_time=0.75)
        self.play(Write(kind[2]), run_time=0.5)
        self.play(TransformFromCopy(maybeint, kind[-1]), run_time=0.75)
        self.wait()
        self.play(FadeOut(kind))
        maybeint.save_state()
        self.play(maybeint.animate.scale(0.75).shift(DOWN*1.25))

        just1 = TextForHaskell("Just 1", t2c=code_t2c, font_size=64)
        self.play(Write(just1))
        self.wait(2)
        self.play(FadeOut(just1[:-1]), just1[-1].animate.center())
        box = Box(1, 1).set_fill(WHITE, 0.25)
        box.open()
        box.save_state()
        box.shift(DOWN*0.7)
        self.wait(2)
        self.add_sound("wood1")
        self.add(box)
        self.wait(0.5)
        self.play(box.animate.restore(), run_time=0.5)
        self.closebox(box)
        self.wait(2)

        nothing = TextForHaskell("Nothing", t2c=code_t2c, font_size=64)
        self.play(FadeOut(VGroup(just1[-1], box)), FadeIn(nothing, UP))
        emptybox = Box(1, 1).set_fill(RED, 0.25)
        self.wait(2)
        self.play(FadeOut(nothing), FadeIn(emptybox))
        self.wait(2)
        self.play(FadeOut(emptybox), maybeint.animate.restore())
        self.wait()

        fa = TextForHaskell("f a", font_size=64).next_to(maybeint, UP, buff=0.75)
        f = fa[0].copy()
        self.play(TransformFromCopy(maybeint[0], f))
        self.wait()
        self.play(TransformFromCopy(maybeint, fa))
        self.remove(f)
        self.wait(3)
        tc = VGroup(maybeint, fa)

        title2 = TexText(
            "Functor", color=BLUE, 
            background_stroke_color=BLUE, font_size=48
        ).move_to(self.titlebg).to_edge(LEFT, buff=0.75)
        self.play(
            RT(self.title_tex, title2),
            func.animate.restore().shift(LEFT*3+DOWN*0.5),
            tc.animate.shift(RIGHT*3+DOWN*0.5)
        )
        function = VGroup(
            TextForHaskell("(+3)", t2c=code_t2c, font_size=60),
        )
        function.add(FunctionBox(function[0], lines_length=0.6))
        function.move_to(func[-1])
        just1_ = VGroup(
            Haskell("1", font_size=60),
            Box(0.8, 0.8).set_fill(WHITE, 0.25)
        ).move_to(maybeint)
        self.wait()
        self.play(
            RT(VGroup(func[1], func[-1]), function), FadeOut(VGroup(func[2:4])),
            FadeTransform(maybeint, just1_)
        )
        self.wait()

        dot = Dot(fill_opacity=0, stroke_width=0).move_to(just1_)
        dot_ = Dot(fill_opacity=0, stroke_width=0).next_to(function[-1], LEFT, buff=0.4)
        dot__ = dot.copy()
        dot___ = dot_.copy()
        just1_.add_updater(lambda m: m.move_to(dot))
        self.play(RT(dot, dot_, path_arc=PI/2, path_arc_axis=IN))
        self.wait()
        just1_.clear_updaters()
        just1_.save_state()
        self.play(just1_.animate.move_to(function[-1].lines[0]), run_time=0.25)
        self.play(
            WiggleOutThenIn(just1_), 
            ShowCreationThenDestruction(Cross(function[-1].lines[0]))
        )
        self.play(just1_.animate.restore(), run_time=0.25)
        just1_.add_updater(lambda m: m.move_to(dot___))
        self.play(RT(dot___, dot__, path_arc=PI/2, path_arc_axis=OUT))
        self.wait()
    
        
class FunctorIntroduction(Scene_):
    def construct(self):
        # < from previous scene
        self.make_title("Functor", skip_anim=True)
        func = VGroup(
            TextForHaskell("a -> b", font_size=64, t2c=code_t2c),
            Tex("f", background_stroke_color=WHITE, font_size=64),
            Tex("x", background_stroke_color=WHITE, font_size=60),
            Tex("f(x)", background_stroke_color=WHITE, font_size=60),
        )
        func.add(FunctionBox(func[1], lines_length=0.6))
        func[2].next_to(func[-1], LEFT, buff=0)
        func[3].next_to(func[-1], RIGHT, buff=0)
        func[0].next_to(func[-1], UP, buff=0.75)
        func.shift(LEFT*3+DOWN*0.5)
        function = VGroup(
            TextForHaskell("(+3)", t2c=code_t2c, font_size=60),
        )
        function.add(FunctionBox(function[0], lines_length=0.6))
        function.move_to(func[-1])
        a2b = func[0]
        self.add(a2b, function)

        constructors = TextForHaskell("Maybe", t2c=code_t2c, font_size=64)
        typeint = TextForHaskell("Int", t2c=code_t2c, font_size=64)
        VGroup(constructors, typeint).arrange(RIGHT, buff=0.5)
        constructors.shift(DOWN*0.05)
        maybeint = VGroup(constructors, typeint)
        fa = TextForHaskell("f a", font_size=64).next_to(maybeint, UP, buff=0.75)
        VGroup(maybeint, fa).shift(RIGHT*3+DOWN*0.5)
        just1 = VGroup(
            Haskell("1", font_size=60),
            Box(0.8, 0.8).set_fill(WHITE, 0.25)
        ).move_to(maybeint)
        self.add(just1, fa)
        # title + a2b + function + fa + just1
        # from previous scene >

        subtitle = Haskell("fmap", font_size=34)
        self.add_sub_title(subtitle)
        fmaptype = Haskell(
            ":: Functor f => (a -> b) -> f a -> f b",
            #0 123456789012 34567 89012 345678 9012
            font_size=34
        ).next_to(subtitle, RIGHT, buff=0.3)
        self.play(Write(fmaptype[0]))
        self.wait()
        self.play(FadeIn(fmaptype[2:13], LEFT))
        self.wait(2)
        self.play(Write(fmaptype[14]), Write(fmaptype[20]))
        self.wait(2)
        self.play(RT(a2b, fmaptype[15:20]))
        self.play(Write(fmaptype[22]))
        self.play(RT(fa, fmaptype[24:27]))
        self.wait(2)
        self.play(Write(fmaptype[28]), FadeIn(fmaptype[30:], LEFT))
        self.wait(2)

        self.play(
            function.animate.scale(1.2).shift(RIGHT*0.5),
            just1.animate.scale(1.2).shift(LEFT*0.5),
            run_time=0.5
        )
        dotl = EmptyDot().move_to(function)
        dotr = EmptyDot().move_to(just1)
        function.add_updater(lambda m: m.move_to(dotl))
        just1.add_updater(lambda m: m.move_to(dotr))
        self.play(Swap(dotl, dotr))
        function.clear_updaters()
        just1.clear_updaters()
        self.wait()

        code = Haskell("fmap (+3) (Just 1)").next_to(self.titlebg, DOWN)
        self.play(Write(code))
        self.wait(2)
        self.openbox(just1[1])
        self.wait(2)
        self.play(just1[0].animate.shift(UP))
        self.wait()
        self.closebox(just1[1])
        self.play(just1[0].animate.next_to(function, LEFT, buff=0), rate_func=rush_into)
        self.play(FadeOut(just1[0], RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        res = Haskell("4", font_size=60).scale(1.2).next_to(function, RIGHT, buff=0)
        self.add_sound("levelup")
        self.play(FadeIn(res, RIGHT*0.5), rate_func=rush_into, run_time=0.5)
        self.wait(2)

        right = VGroup(function, res)
        dotl = EmptyDot().move_to(just1[1])
        dotr = EmptyDot().move_to(right)
        just1[1].add_updater(lambda m: m.move_to(dotl))
        right.add_updater(lambda m: m.move_to(dotr))
        self.add(right, just1[1])
        self.play(Swap(dotl, dotr))
        right.clear_updaters()
        just1[1].clear_updaters()
        self.wait(2)
        self.play(res.animate.move_to(just1[1]).shift(UP))
        self.openbox(just1[1])
        self.play(res.animate.shift(DOWN))
        self.closebox(just1[1])
        self.wait(2)
        resbox = VGroup(res, just1[1])
        self.play(
            WiggleOutThenIn(resbox),
            Flash(resbox, line_length=0.4, flash_radius=1.4)
        )
        rescode = Haskell("= Just 4", font_size=42).next_to(code, RIGHT)
        self.wait()
        self.play(FadeIn(rescode, RIGHT))

        self.wait(2)
        self.play(FadeOut(rescode))
        code2 = Haskell("fmap (+3) [1, 2, 3]").next_to(self.titlebg, DOWN)
        self.play(RT(code, code2))
        box2 = VGroup(
            VGroup(*[
                Haskell(s, font_size=60).scale(1.2)
                for s in ["1", "2", "3"]
            ]).arrange(RIGHT, buff=0.25).move_to(resbox)
        )
        box2.add(Box(1.8, 1).set_fill(WHITE, 0.25).scale(1.2).move_to(resbox))
        self.play(FadeTransform(resbox, box2))

        self.wait(2)
        res2 = VGroup(*[
            Haskell(s, font_size=60).scale(1.2)
            for s in ["4", "5", "6"]
        ]).next_to(function, RIGHT, buff=0)
        self.openbox(box2[1])
        for i in [0, 1, 2]:
            self.play(box2[0][i].animate.shift(UP), run_time=0.5)
            place = box2[0][i].copy()
            self.play(
                Transform(
                    box2[0][i], box2[0][i].copy().next_to(function, LEFT, buff=0),
                    path_arc=PI/2, path_arc_axis=OUT, rate_func=rush_into
                )
            )
            self.play(FadeOut(box2[0][i], RIGHT*0.5), rate_func=rush_from, run_time=0.5)
            self.add_sound("levelup")
            self.play(FadeIn(res2[i], RIGHT*0.5), rate_func=rush_into, run_time=0.5)
            self.play(res2[i].animate.move_to(place), rate_func=rush_from)
            self.play(res2[i].animate.shift(DOWN), run_time=0.5)
            self.wait()
        self.closebox(box2[1])
        rescode2 = Haskell("= [4, 5, 6]", font_size=42).next_to(code2, RIGHT)
        self.play(
            WiggleOutThenIn(VGroup(res2, box2[1])),
            FadeIn(rescode2, LEFT)
        )
        self.wait(3)

        self.play(FadeOut(rescode2))
        code3 = Haskell("fmap (+3) Nothing").next_to(self.titlebg, DOWN)
        self.play(RT(code2, code3))
        eb = Box(1, 1).scale(1.2).set_fill(RED, 0.25).move_to(box2[1])
        self.play(FadeTransform(VGroup(res2, box2[1]), eb))
        self.wait()
        self.openbox(eb)
        self.closebox(eb)
        self.play(WiggleOutThenIn(eb))
        self.wait(2)
        self.play(Flash(eb, line_length=0.4, flash_radius=1.4))
        self.wait()
        rescode3 = Haskell("= Nothing", font_size=42).next_to(code3, RIGHT)
        self.play(FadeIn(rescode3, LEFT))
        self.wait(4)
        
        self.play(FadeOut(rescode3))
        self.wait()

        code4 = Haskell("fmap (+) (Just 3)").next_to(self.titlebg, DOWN)
        self.play(RT(code3, code4))
        func2 = VGroup(
            TextForHaskell("(+)", t2c=code_t2c, font_size=60),
        )
        func2.add(FunctionBox(func2[0], lines_length=0.6))
        func2.scale(1.2).move_to(function)
        just3 = VGroup(
            Haskell("3", font_size=60),
            Box(1, 1).set_fill(WHITE, 0.25)
        ).scale(1.2).move_to(eb)
        self.play(FadeTransform(eb, just3), RT(function, func2))
        self.wait(2)

        place = just3[1].copy()
        self.openbox(just3[1])
        self.play(just3[0].animate.shift(UP))
        res_ = Haskell("(+3)", font_size=60).scale(1.2).next_to(func2, RIGHT, buff=0)
        self.play(
            Transform(
                just3[0], just3[0].copy().next_to(func2, LEFT, buff=0),
                path_arc=PI/2, path_arc_axis=OUT
            ),
            rate_func=rush_into
        )
        self.play(FadeOut(just3[0], RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        self.add_sound("levelup")
        self.play(FadeIn(res_, RIGHT*0.5), run_time=0.5, rate_func=rush_into)
        self.play(res_.animate.scale(0.6).move_to(place).shift(UP))
        self.play(res_.animate.shift(DOWN), run_time=0.5)
        self.closebox(just3[1])
        self.wait()

        resbox_ = VGroup(res_, just3[1])
        self.play(
            WiggleOutThenIn(resbox_),
            Flash(resbox_, line_length=0.4, flash_radius=1.4)
        )
        self.wait()
        rescode4 = Haskell("= Just (+3)", font_size=42).next_to(code4, RIGHT)
        self.play(FadeIn(rescode4, LEFT))
        self.wait(3)
        self.play(FadeOut(rescode4), FadeOut(code4))
        just1_ = VGroup(
            Haskell("1", font_size=60),
            Box(1, 1).set_fill(WHITE, 0.25)
        ).scale(1.2).move_to(place).shift(LEFT*0.5)
        self.play(
            resbox_.animate.move_to(func2).shift(RIGHT*0.5+DOWN*0.05),
            FadeOut(func2),
            FadeIn(just1_)
        )
        arrow = Arrow(just1_.get_left(), resbox_.get_right(), color=ORANGE)
        fa2b = Haskell("f (a -> b)", font_size=64).next_to(resbox_, UP, buff=0.75)
        fa_  = Haskell("f a", font_size=64).next_to(just1_, UP, buff=0.75)
        self.play(
            FadeIn(fa2b, UP),
            FadeIn(fa_, UP),
            GrowArrow(arrow, rate_func=there_and_back), run_time=2
        )
        self.wait()
        self.play(
            WiggleOutThenIn(resbox_)
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(
                self.sub_topic_sign,
                subtitle,
                fmaptype
            ))
        )
        self.wait(2)

        title2 = TexText(
            "Applicative", color=BLUE, 
            background_stroke_color=BLUE, font_size=48
        ).move_to(self.titlebg).to_edge(LEFT, buff=0.75)
        self.play(
            RT(self.title_tex, title2)
        )
        self.wait(2)


class ApplicativeIntroduction(Scene_):
    def construct(self):
        # < from previous scene
        self.make_title("Applicative", skip_anim=True)
        funcbox = VGroup(
            Haskell("(+3)", font_size=60).scale(1.2).scale(0.6),
            Box(1, 1).set_fill(WHITE, 0.25).scale(1.2)
        ).move_to([-2.20210062, -0.55, 0])
        fa2b = Haskell("f (a -> b)", font_size=64).next_to(funcbox, UP, buff=0.75)

        just1 = VGroup(
            Haskell("1", font_size=60),
            Box(1, 1).set_fill(WHITE, 0.25)
        ).scale(1.2).move_to([2.20210062, -0.55, 0])
        fa = Haskell("f a", font_size=64).next_to(just1, UP, buff=0.75)
        self.add(fa2b, funcbox, fa, just1)
        # title + fa2b + funcbox + fa + just1
        # from previous scene >

        subtitle = Haskell("(<*>)", font_size=30)
        self.add_sub_title(subtitle)
        apptype = Haskell (
            ":: Applicative f => f (a -> b) -> f a -> f b",
            #0 1234567890123456 7890123 45678 901234 5678
            font_size=30
        ).next_to(subtitle, RIGHT, buff=0.3)
        self.play(Write(apptype[0]))
        self.wait()
        self.play(FadeIn(apptype[2:17], LEFT))
        self.wait(2)
        self.play(RT(fa2b, apptype[18:27]))
        self.play(Write(apptype[28]))
        self.play(RT(fa, apptype[30:33]))
        self.wait(2)
        self.play(Write(apptype[34]), FadeIn(apptype[36:], LEFT))
        self.wait(2)

        code = Haskell("Just (+3) <*> Just 1").next_to(self.titlebg, DOWN)
        self.play(Write(code))
        self.wait(2)
        self.openbox(funcbox[1])
        plus3box = FunctionBox(funcbox[0].copy().scale(1.667), lines_length=0.6)
        self.play(
            funcbox[1].animate.shift(DOWN*1.5),
            funcbox[0].animate.scale(1.667),
            FadeIn(plus3box)
        )
        self.wait(2)
        self.openbox(just1[1])
        self.play(just1[1].animate.shift(DOWN*1.5))
        self.wait(2)
        place = just1[0].copy()
        
        res1 = Haskell("4", font_size=60).scale(1.2).next_to(plus3box, RIGHT, buff=0)
        self.play(
            Transform(
                just1[0], just1[0].copy().next_to(plus3box, LEFT, buff=0),
                path_arc=PI/2, path_arc_axis=OUT
            ), rate_func=rush_into
        )
        self.play(FadeOut(just1[0], RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        self.add_sound("levelup")
        self.play(FadeIn(res1, RIGHT*0.5), rate_func=rush_into, run_time=0.5)
        self.play(res1.animate.move_to(place), rate_func=rush_from, run_time=1.5)
        self.wait(2)
        self.play(
            FadeOut(plus3box),
            funcbox[0].animate.scale(0.6),
            funcbox[1].animate.shift(UP*1.5),
            just1[1].animate.shift(UP*1.5)
        )
        self.add_sound("chestclosed")
        self.play(
            Rotate(
                funcbox[1].top, PI-10*DEGREES, axis=IN,
                about_point=funcbox[1].top.get_points()[14], 
            ),
            Rotate(
                just1[1].top, PI-10*DEGREES, axis=IN,
                about_point=just1[1].top.get_points()[14], 
            ), run_time=0.5
        )
        resbox = VGroup(res1, just1[1])
        self.play(
            WiggleOutThenIn(resbox),
            Flash(resbox, line_length=0.4, flash_radius=1.4)
        )
        rescode = Haskell("= Just 4", font_size=42).next_to(code, RIGHT)
        self.wait()
        self.play(FadeIn(rescode, LEFT))
        self.wait(3)
        
        self.play(FadeOut(rescode), run_time=0.5)
        code2 = Haskell("[(+1), (*2)] <*> [2, 3]").next_to(self.titlebg, DOWN)
        self.play(TransformMatchingShapes(code, code2))
        func = VGroup(
            VGroup(
                Haskell("(+1)", font_size=60),
                Haskell("(*2)", font_size=60)
            ).scale(1.2).scale(0.6).arrange(RIGHT, buff=0.3),
            Box(2.1, 1).set_fill(WHITE, 0.25).scale(1.2)
        ).move_to(funcbox[1], RIGHT).shift(RIGHT*0.5)
        vall = VGroup(
            VGroup(
                Haskell("2", font_size=60),
                Haskell("3", font_size=60)
            ).scale(1.2).arrange(RIGHT, buff=0.6),
            Box(2, 1).set_fill(WHITE, 0.25).scale(1.2)
        ).move_to(just1[1], LEFT)
        self.wait()
        self.play(
            FadeTransform(funcbox, func),
            FadeTransform(resbox, vall),
            run_time=0.5
        )

        func_box = VGroup(
            FunctionBox(func[0][0].copy().scale(1.667), lines_length=0.6),
            FunctionBox(func[0][1].copy().scale(1.667), lines_length=0.6),
        )
        res2 = VGroup(*[
            Haskell(str(s), font_size=56)
            for s in [3, 4, 4, 6]
        ])
        res2[:2].next_to(func_box[0], RIGHT, buff=0)
        res2[2:].next_to(func_box[1], RIGHT, buff=0)
        places = res2.copy().arrange(RIGHT, buff=0.23).move_to(vall[1]).shift(DOWN*1.5)

        self.add_sound("chestopen")
        self.play(
            Rotate(
                func[1].top, PI-10*DEGREES, 
                about_point=func[1].top.get_points()[14], 
            ),
            Rotate(
                vall[1].top, PI-10*DEGREES, 
                about_point=vall[1].top.get_points()[14], 
            ), run_time=0.5
        )
        self.play(
            VGroup(func[1], func[0][1]).animate.shift(DOWN*1.5),
            vall[1].animate.shift(DOWN*1.5),
            func[0][0].animate.scale(1.667),
            FadeIn(func_box[0])
        )
        self.wait(2)
        
        for i in [0, 1]:
            now = vall[0][i].copy()
            self.play(
                Transform(
                    now, now.copy().next_to(func_box[0], LEFT, 0),
                    path_arc=PI/2, path_arc_axis=OUT
                ), rate_func=rush_into
            )
            self.play(FadeOut(now, RIGHT*0.5), rate_func=rush_from, run_time=0.5)
            self.add_sound("levelup")
            self.play(FadeIn(res2[i], RIGHT*0.5), rate_func=rush_into, run_time=0.5)
            self.play(res2[i].animate.move_to(places[i]), run_time=1)
        
        self.play(
            FadeOut(func_box[0], DOWN*1.5),
            FadeIn(func_box[1], UP*1.5),
            func[0][0].animate.scale(0.6).shift(DOWN*1.5),
            func[0][1].animate.shift(UP*1.5).scale(1.667),
        )
        self.wait()
        for i in [0, 1]:
            now = vall[0][i]
            self.play(
                Transform(
                    now, now.copy().next_to(func_box[1], LEFT, 0),
                    path_arc=PI/2, path_arc_axis=OUT
                ), rate_func=rush_into
            )
            self.play(FadeOut(now, RIGHT*0.5), rate_func=rush_from, run_time=0.5)
            self.add_sound("levelup")
            self.play(FadeIn(res2[i+2], RIGHT*0.5), rate_func=rush_into, run_time=0.5)
            self.play(res2[i+2].animate.move_to(places[i+2]), run_time=1)
        
        self.wait(2)
        self.add(func[0][0])
        self.play(
            FadeOut(func_box[1]),
            func[1].animate.shift(UP*1.5),
            vall[1].animate.shift(UP*1.5),
            func[0][0].animate.shift(UP*1.5),
            func[0][1].animate.scale(0.6),
            res2.animate.shift(UP*1.5),
            run_time=0.5
        )
        self.wait()
        self.add_sound("chestclosed")
        self.play(
            Rotate(
                func[1].top, PI-10*DEGREES, axis=IN,
                about_point=func[1].top.get_points()[14], 
            ),
            Rotate(
                vall[1].top, PI-10*DEGREES, axis=IN,
                about_point=vall[1].top.get_points()[14], 
            ), run_time=0.5
        )
        self.wait(2)
        resbox_ = VGroup(res2, vall[1])
        self.play(
            WiggleOutThenIn(resbox_),
            Flash(resbox_, line_length=0.4, flash_radius=2)
        )
        rescode2 = Haskell("= [3, 4, 4, 6]", font_size=42).next_to(code2, RIGHT)
        place = code2.copy()
        VGroup(place, rescode2).move_to(ORIGIN, coor_mask=np.array([1, 0, 1]))
        self.wait()
        self.play(
            FadeIn(rescode2, LEFT),
            code2.animate.move_to(place)
        )
        self.wait(3)
        self.play(FadeOut(VGroup(
            code2, rescode2
        )))

        func_ = Haskell("\\x -> Just (x+3)", font_size=42).move_to(RIGHT*2.5)
        func__box = KleisliBox(func_, lines_length=0.6)
        a2fb = Haskell("a -> f b", font_size=60).next_to(func__box, UP)
        just1_ = VGroup(
            Haskell("1", font_size=60),
            Box(1, 1).set_fill(WHITE, 0.25)
        ).shift(LEFT*3)
        res_ = VGroup(
            Haskell("4", font_size=60),
            Box(1, 1).set_fill(WHITE, 0.25)
        ).next_to(func__box, RIGHT, 0)
        self.wait()
        self.play(
            FadeTransform(func, VGroup(func_, func__box)),
            FadeTransform(resbox_, just1_)
        )
        self.play(
            FadeIn(a2fb, UP), run_time=0.5
        )
        self.wait(2)
        code3 = Haskell("fmap (\\x -> Just (x+3)) (Just 1)", font_size=42).next_to(self.titlebg, DOWN)
        self.play(Write(code3))
        self.wait()

        place_ = just1_[1].copy()
        just1_0 = just1_[0].copy()
        self.openbox(just1_[1])
        self.play(just1_[1].animate.shift(DOWN))
        self.play(just1_[0].animate.next_to(func__box, LEFT, 0), rate_func=rush_into)
        self.play(FadeOut(just1_[0], RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        self.add_sound("levelup")
        self.play(FadeIn(res_, RIGHT*0.5), rate_func=rush_into, run_time=0.5)
        self.wait(2)
        self.play(
            Transform(
                res_, res_.copy().move_to(place_),
                path_arc=PI/2, path_arc_axis=OUT
            ), rate_func=rush_from
        )
        self.play(just1_[1].animate.shift(UP).scale(1.2, about_point=res_.get_center()))
        self.closebox(just1_[1])
        rescode3 = Haskell("= Just (Just 4)", font_size=36).next_to(code3, RIGHT)
        place = code3.copy()
        VGroup(place, rescode3).move_to(ORIGIN, coor_mask=np.array([1, 0, 1]))
        resbox__ = VGroup(res_, just1_[1])
        self.play(
            WiggleOutThenIn(resbox__),
            Flash(resbox__, line_length=0.4, flash_radius=1.4),
            FadeIn(rescode3, LEFT),
            code3.animate.move_to(place)
        )
        self.wait()
        self.play(ShowCreationThenDestructionAround(rescode3[2:]))
        self.wait(3)
        self.play(
            FadeIn(just1_0),
            just1_[1].animate.scale(1/1.2),
            FadeOut(res_),
            FadeOut(code3),
            FadeOut(rescode3),
            FadeOut(self.sub_topic_sign),
            FadeOut(subtitle),
            FadeOut(apptype),
            run_time=0.5
        )
        self.wait(2)

        title2 = TexText(
            "Monad", color=BLUE, 
            background_stroke_color=BLUE, font_size=48
        ).move_to(self.titlebg).to_edge(LEFT, buff=0.75)
        self.play(
            RT(self.title_tex, title2)
        )
        self.wait(2)


class MonadIntroduction(Scene_):
    def construct(self):
        # < from previous scene 
        self.make_title("Monad", skip_anim=True)
        just1 = VGroup(
            Haskell("1", font_size=60),
            Box(1, 1).set_fill(WHITE, 0.25)
        ).shift(LEFT*3)
        func = VGroup(
            Haskell("\\x -> Just (x+3)", font_size=42).move_to(RIGHT*2.5)
        ).move_to(RIGHT*2.5)
        func.add(KleisliBox(func, lines_length=0.6))
        a2fb = Haskell("a -> f b", font_size=60).next_to(func[1], UP)
        fa = Haskell("f a", font_size=60).next_to(just1, UP)
        self.add(just1, func, a2fb)
        self.play(FadeIn(fa, UP), run_time=0.5)
        # title + just1 + func + a2fb
        # from previous scene >

        subtitle = Haskell("(>>=)", font_size=32)
        self.add_sub_title(subtitle)
        bindtype = Haskell(
            ":: Monad f => f a -> (a -> f b) -> f b",
            #0 1234567890 123456 78901 2345678 9012
            font_size=32
        ).next_to(subtitle, RIGHT, buff=0.3)
        self.play(Write(bindtype[0]))
        self.wait()
        self.play(FadeIn(bindtype[2:11], LEFT))
        self.wait(2)
        self.play(RT(fa, bindtype[12:15]))
        self.play(
            Write(bindtype[16]),
            Write(bindtype[18]),
            Write(bindtype[26]),
        )
        self.play(RT(a2fb, bindtype[19:26]))
        self.wait(2)
        self.play(Write(bindtype[28]), FadeIn(bindtype[30:], LEFT))
        self.wait(2)

        code = Haskell("Just 1 >>= \\x -> Just (x+3)", font_size=42).next_to(self.titlebg, DOWN)
        self.play(
            Write(code),
            func.animate.shift(LEFT*2.5),
            just1.animate.next_to(func, LEFT, 0).shift(LEFT*3.5)
        )
        res = VGroup(
            Haskell("4", font_size=60),
            Box(1, 1).set_fill(WHITE, 0.25)
        ).next_to(func, RIGHT, 0)
        self.wait()
        self.openbox(just1[1])
        self.play(just1[1].animate.shift(DOWN))
        self.wait()
        self.play(just1[0].animate.shift(RIGHT), rate_func=rush_into)
        self.play(FadeOut(just1[0], RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        self.add_sound("levelup")
        self.play(FadeIn(res, RIGHT*0.5), rate_func=rush_into, run_time=0.5)
        self.play(res.animate.shift(RIGHT), rate_func=rush_from)
        self.wait()
        self.play(
            WiggleOutThenIn(res),
            Flash(res, line_length=0.4, flash_radius=1.4)
        )
        self.wait()

        rescode = Haskell("= Just 4", font_size=40).next_to(code, RIGHT)
        place = code.copy()
        VGroup(place, rescode).move_to(ORIGIN, coor_mask=np.array([1, 0, 1]))
        self.play(
            FadeIn(rescode, LEFT),
            code.animate.move_to(place)
        )
        self.wait(3)
        self.play(FadeOut(VGroup(
            code, rescode, just1[1], func, res
        )))
        self.wait(2)


class MonadUsage(Scene_):
    def construct(self):
        # < from previous scene
        self.make_title("Monad", skip_anim=True)
        subtitle = Haskell("(>>=)", font_size=32)
        self.add_sub_title(subtitle, skip_anim=True)
        bindtype = Haskell(
            ":: Monad f => f a -> (a -> f b) -> f b",
            #0 1234567890 123456 78901 2345678 9012
            font_size=32
        ).next_to(subtitle, RIGHT, buff=0.3)
        self.add(bindtype)
        # title, subtitle, bindtype 
        # from previous scene >
        self.wait(2)

        codes = VGroup(
            Haskell("getLine", font_size=42),
            Haskell(">>= readFile", font_size=42),
            Haskell(">>= putStrLn", font_size=42)
        ).arrange(RIGHT, 0.3).next_to(self.titlebg, DOWN)
        codes[1].shift(UP*0.04)
        for code in codes:
            code.save_state()
        
        sideeffects = VGroup(
            Haskell("getLine"),
            Haskell("putStrLn"),
            Haskell("readFile"),
            Haskell("getArgs"),
            Haskell("...")
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        io = Haskell("IO", font_size=52)
        sideeffects.next_to(io, LEFT, buff=1)
        brace = Brace(sideeffects, RIGHT)
        returns = VGroup(
            Haskell("String"),
            Haskell("()"),
            Haskell("String"),
            Haskell("[String]"),
            Haskell("...")
        ).arrange(ORIGIN, aligned_edge=LEFT).next_to(io, RIGHT)
        self.play(Write(sideeffects), Write(brace))
        self.wait()
        self.play(FadeIn(io, RIGHT*0.7))
        self.wait()
        for i in range(5):
            self.play(
                sideeffects[:i].animate.set_fill(opacity=0.25),
                sideeffects[i].animate.set_fill(opacity=1),
                sideeffects[i+1:].animate.set_fill(opacity=0.25),
                FadeIn(returns[i], DOWN),
                FadeOut(returns[i-1], DOWN) if i != 0 else Animation(returns[i]),
                run_time=0.5
            )
        
        iobox = Box(1.2, 1.2).set_fill(WHITE, 0.25)
        self.play(
            FadeOut(sideeffects, LEFT),
            FadeOut(brace, LEFT),
            returns[-1].animate.center(),
            RT(io, iobox),
        )
        self.wait(2)
        self.play(FadeOut(iobox), FadeOut(returns[-1]))
        self.wait(2)

        getLine = VGroup(Haskell("getLine", font_size=42))
        getLine.add(GetLineBox(getLine[0]))
        getLine.scale(0.8)
        readFile = VGroup(Haskell("readFile", font_size=42))
        readFile.add(KleisliBox(readFile[0]))
        readFile.scale(0.8)
        putStrLn = VGroup(Haskell("putStrLn", font_size=42))
        putStrLn.add(KleisliBox(putStrLn[0]))
        putStrLn.scale(0.8)
        VGroup(getLine, readFile, putStrLn).arrange(RIGHT, buff=2)
        monitor = SVGMobject(
            "monitor", width=putStrLn[0].get_width(),
            stroke_width=0, color="#C1C1C1"
        ).next_to(putStrLn[1].box, UP, buff=0.02)
        keyboard = SVGMobject(
            "keyboard", width=getLine[0].get_width(),
            stroke_width=0, color="#C1C1C1"
        ).next_to(getLine[1].box, DOWN, buff=0.02)
        keyboard[0].set_fill(opacity=0).set_stroke(width=3, opacity=0.75)
        database = SVGMobject(
            "database", height=keyboard.get_height(),
            stroke_width=0, color="#C1C1C1"
        ).next_to(readFile[1].box, DOWN, buff=0.02)

        name = VGroup(
            Haskell("name", font_size=24),
            Box(1, 1).set_fill(WHITE, 0.25).scale(0.8)
        ).next_to(getLine[1], RIGHT, buff=0)
        content = VGroup(
            Haskell("\"content\"", font_size=24),
            Box(1.7, 1).set_fill(WHITE, 0.25).scale(0.8)
        ).next_to(readFile[1], RIGHT, buff=0)
        end = VGroup(
            Haskell("()", font_size=42),
            Box(1, 1).set_fill(WHITE, 0.25).scale(0.8)
        ).next_to(putStrLn[1], RIGHT, buff=0)
        
        self.play(
            Write(codes[0]),
            Write(getLine[0]),
            FadeIn(getLine[1]),
            FadeIn(keyboard)
        )
        self.wait()
        self.add_sound("levelup")
        self.play(FadeIn(name, RIGHT*0.5), rate_func=rush_into, run_time=0.5)
        self.play(name.animate.move_to(
            mid(getLine.get_right(), readFile.get_left())
        ), rate_func=rush_from, run_time=0.5)
        self.wait(2)
        self.play(
            Write(readFile[0]),
            FadeIn(readFile[1]),
            FadeIn(database)
        )
        self.wait()
        self.openbox(name[1])
        self.play(name[1].animate.shift(DOWN))
        self.play(name[0].animate.next_to(readFile, LEFT, buff=0), rate_func=rush_into, run_time=0.5)
        self.play(FadeOut(name[0], RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        self.add_sound("levelup")
        self.play(FadeIn(content, RIGHT*0.5), rate_func=rush_into, run_time=0.5)
        self.play(content.animate.move_to(
            mid(readFile.get_right(), putStrLn.get_left())
        ), rate_func=rush_from, run_time=0.5)
        self.play(FadeIn(codes[1], LEFT))
        self.play(
            Write(putStrLn[0]),
            FadeIn(putStrLn[1]),
            FadeIn(monitor)
        )
        self.wait()
        self.openbox(content[1])
        self.play(content[1].animate.shift(DOWN))
        self.play(content[0].animate.next_to(putStrLn, LEFT, buff=0), rate_func=rush_into, run_time=0.5)
        self.play(FadeOut(content[0], RIGHT*0.5), rate_func=rush_from, run_time=0.5)
        self.add_sound("levelup")

        screen = Haskell("content", font_size=28).move_to(monitor).shift(UP*0.1)
        self.play(
            FadeIn(end, RIGHT*0.5),
            FadeIn(screen, UP*0.8), 
            run_time=0.5
        )
        self.wait()
        self.play(FadeIn(codes[2], LEFT))
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(codes))
        self.wait(3)

        self.play(FadeOut(VGroup(
            codes, screen, end, getLine, readFile, putStrLn,
            keyboard, database, monitor,
            name[1], content[1]
        )))
        self.wait(2)

        title2 = TexText(
            "Summary", color=BLUE, 
            background_stroke_color=BLUE, font_size=48
        ).move_to(self.titlebg).to_edge(LEFT, buff=0.75)
        self.play(
            FadeOut(self.sub_topic_sign),
            FadeOut(subtitle),
            FadeOut(bindtype)
        )
        self.play(
            RT(self.title_tex, title2)
        )
        self.wait(2)


class MonadGraph(Scene_):
    def construct(self):
        getLine = VGroup(Haskell("getLine", font_size=42))
        getLine.add(GetLineBox(getLine[0]))
        getLine.scale(0.8)
        readFile = VGroup(Haskell("readFile", font_size=42))
        readFile.add(KleisliBox(readFile[0]))
        readFile.scale(0.8)
        putStrLn = VGroup(Haskell("putStrLn", font_size=42))
        putStrLn.add(KleisliBox(putStrLn[0]))
        putStrLn.scale(0.8)
        VGroup(getLine, readFile, putStrLn).arrange(RIGHT, buff=2)
        monitor = SVGMobject(
            "monitor", width=putStrLn[0].get_width(),
            stroke_width=0, color="#C1C1C1"
        ).next_to(putStrLn[1].box, UP, buff=0.02)
        keyboard = SVGMobject(
            "keyboard", width=getLine[0].get_width(),
            stroke_width=0, color="#C1C1C1"
        ).next_to(getLine[1].box, DOWN, buff=0.02)
        keyboard[0].set_fill(opacity=0).set_stroke(width=3, opacity=0.75)
        database = SVGMobject(
            "database", height=keyboard.get_height(),
            stroke_width=0, color="#C1C1C1"
        ).next_to(readFile[1].box, DOWN, buff=0.02)

        name = VGroup(
            Haskell("name", font_size=24),
            Box(1, 1).set_fill(WHITE, 0.25).scale(0.8)
        ).next_to(getLine[1], RIGHT, buff=0)
        content = VGroup(
            Haskell("\"content\"", font_size=24),
            Box(1.7, 1).set_fill(WHITE, 0.25).scale(0.8)
        ).next_to(readFile[1], RIGHT, buff=0)
        end = VGroup(
            Haskell("()", font_size=42),
            Box(1, 1).set_fill(WHITE, 0.25).scale(0.8)
        ).next_to(putStrLn[1], RIGHT, buff=0)
        screen = Haskell("content", font_size=28).move_to(monitor).shift(UP*0.1)

        name.move_to(
            mid(getLine.get_right(), readFile.get_left())
        )
        content.move_to(
            mid(readFile.get_right(), putStrLn.get_left())
        )

        self.add(getLine, readFile, putStrLn, keyboard, database, monitor, name, content, end, screen)


class SummaryAndEndScene(Scene_):
    def construct(self):
        self.make_title("Summary", skip_anim=True)
        summary = VGroup(
            Haskell("Functor —— fmap  ::     Functor f =>   (a -> b) -> f a -> f b", font_size=32),
                    #012345678901234567 8901234567890123 4567890 12345 678901 2345
            Haskell("Applicative —— (<*>) :: Applicative f => f (a -> b) -> f a -> f b", font_size=32),
                    #01234567890123456  789 0123456789012345 6789012 34567 890123 4567
            Haskell("Monad —— (>>=) ::       Monad m => m a -> (a -> m b) -> m b", font_size=32)
                    #01234567890  123 4567890123456789 012345 67890 1234567 8901
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.5).shift(UP*0.5)
        
        self.play(*[
            Write(line) for line in summary
        ])
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(summary[0][37:44]),
            ShowCreationThenDestructionAround(summary[1][37:46]),
            ShowCreationThenDestructionAround(summary[2][37:46]),
        )
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(summary[0][47:50]),
            ShowCreationThenDestructionAround(summary[1][49:52]),
            ShowCreationThenDestructionAround(summary[2][31:34]),
        )
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(summary[0][-3:]),
            ShowCreationThenDestructionAround(summary[1][-3:]),
            ShowCreationThenDestructionAround(summary[2][-3:]),
        )
        self.wait(3)

        bg = Rectangle(width=16, height=10).set_fill(color=BLACK, opacity=0.8)
        self.wait()
        warningtext = VGroup(
            SemiBoldText("本视频仅是为便于直观理解三个函数的作用", font_size=26),
            SemiBoldText("不能做到足够严谨，但有严重错误还请在评论区指出", font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL).set_color(GREY_C).shift(DOWN)
        self.play(FadeIn(bg), FadeIn(warningtext))
        # self.play()

        thanks = Group(
            Text("特别鸣谢", font="Source Han Sans CN", font_size=52).set_color(RED),
            ImageMobject("GZTime_new.png").scale(0.24),
            Text("@GZTime", font="Source Han Serif CN", font_size=36).set_color(BLUE),
        )
        thanks[0].to_corner(UR)
        thanks[2].next_to(thanks[0], DOWN, aligned_edge=RIGHT, buff=0.5)
        thanks[1].next_to(thanks[2], LEFT, buff=0.1)
        # thanks[1:].next_to(thanks[0], DOWN, aligned_edge=RIGHT)

        refer = VGroup(
            Text("参考", font="Source Han Sans CN", font_size=52).set_color(RED),
            Text("[1] https://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html", font="Source Han Serif CN", font_size=26),
            Text("[2] Learn You a Haskell http://learnyouahaskell.com/chapters", font="Source Han Serif CN", font_size=26),
            Text("[3] Typeclassopedia - Haskell wiki https://wiki.haskell.org/Typeclassopedia", font="Source Han Serif CN", font_size=26),
            Text("[4] Haskell/Category theory https://en.wikibooks.org/wiki/Haskell/Category_theory", font="Source Han Serif CN", font_size=26),
        )
        refer.arrange(DOWN, aligned_edge=LEFT)
        refer.to_corner(DL)

        self.wait()
        self.play(FadeIn(thanks, UP))
        self.play(FadeIn(refer))
        self.wait(10)






