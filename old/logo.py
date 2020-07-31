from manimlib.imports import *
from manim_sandbox.utils.imports import *

class LogoStart_white(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(self):
        logo = Logo(size=8/3, black_bg=False)
        squares = VGroup(*[Polygon(ORIGIN, UR, UL), Polygon(ORIGIN, UL, DL), Polygon(ORIGIN, DL, DR), Polygon(ORIGIN, DR, UR),])
        squares.set_fill(BLUE_C, 1).set_stroke(width=0.5, color=BLUE_C).rotate(np.arctan(0.5)).set_height(logo.inner_triangles.get_height())
        squares[0].set_fill('#C59978', 1).set_stroke(width=0.5, color='#C59978')
        for s in squares:
            s.scale(0.8)

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
        all_logo = Group(logo, text, line, img).center()
        text = Group(text, line, img)

        bg = Rectangle(height=10, width=10, fill_color=WHITE, fill_opacity=1, stroke_width=0)
        bg.add_updater(lambda m: m.move_to(logo, aligned_edge=RIGHT).shift(RIGHT*0.2))

        text.save_state()
        text.shift((text.get_right()[0]-bg.get_right()[0]+0.2)*LEFT)
        logo.save_state()
        logo.move_to(ORIGIN)
        logo.scale(1.5)

        tris = logo.inner_triangles.copy().rotate(-PI)
        tris.set_color(BLUE_C)
        tris[0].set_color('#C59978')
        self.add(text, bg)

        self.wait(0.3)
        self.add(tris)
        self.wait(0.3)
        self.remove(tris)

        self.wait(0.2)
        self.add(tris)
        self.wait(0.15)
        self.remove(tris)

        self.wait(0.1)
        self.add(tris)
        self.wait(0.1)
        self.remove(tris)
        
        self.wait(0.075)
        self.add(tris)
        self.wait(0.075)
        self.remove(tris)

        self.wait(0.05)
        self.add(tris)
        self.wait(0.05)
        self.remove(tris)

        self.wait(0.2)
        self.play(ShowSubmobjectsOneByOne(tris), rate_func=linear, run_time=0.4)
        for i in tris:
            self.add(i)
            self.wait(0.1)
        self.play(*[ReplacementTransform(tris[i], squares[i]) for i in range(4)], 
            rate_func=rush_from, run_time=0.6)
        self.wait(0.1)
        self.play(*[ReplacementTransform(squares[i], logo[i]) for i in range(4)], 
            rate_func=rush_from, run_time=0.6)
        self.wait(0.1)
        self.play(
            text.restore, logo.restore,
            rate_func=rush_from, run_time=0.8
        )
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))


class LogoStart_black(Scene):
    def construct(self):
        logo = Logo(size=8/3)
        squares = VGroup(*[Polygon(ORIGIN, UR, UL), Polygon(ORIGIN, UL, DL), Polygon(ORIGIN, DL, DR), Polygon(ORIGIN, DR, UR),])
        squares.set_fill(WHITE, 1).set_stroke(width=0.5, color=WHITE).rotate(np.arctan(0.5)).set_height(logo.inner_triangles.get_height())
        for s in squares:
            s.scale(0.8)

        img = ImageMobject("Tony.png").set_height(2)
        Group(logo, img).arrange(RIGHT, buff=1.5).center()
        line = Line(UP, DOWN, stroke_width=8, color=WHITE).move_to(mid(logo.get_right(), img.get_left()))
        line.set_length(1.4)
        text = VGroup(
            Text("Manim-Kindergarten", font="Orbitron", color=LIGHT_GRAY),
            Text("鹤翔万里", font="庞门正道标题体", color=WHITE, size=2.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(img, buff=0.5)
        text[0][0].set_color(logo.color_2[2])
        text[0][6].set_color(logo.color_1[2])
        all_logo = Group(logo, text, line, img).center()
        text = Group(text, line, img)

        bg = Rectangle(height=10, width=10, fill_color=BLACK, fill_opacity=1, stroke_width=0)
        bg.add_updater(lambda m: m.move_to(logo, aligned_edge=RIGHT).shift(RIGHT*0.2))

        text.save_state()
        text.shift((text.get_right()[0]-bg.get_right()[0]+0.2)*LEFT)
        logo.save_state()
        logo.move_to(ORIGIN)
        logo.scale(1.5)

        tris = logo.inner_triangles.copy().rotate(-PI)
        self.add(text, bg)

        self.wait(0.3)
        self.add(tris)
        self.wait(0.3)
        self.remove(tris)

        self.wait(0.2)
        self.add(tris)
        self.wait(0.15)
        self.remove(tris)

        self.wait(0.1)
        self.add(tris)
        self.wait(0.1)
        self.remove(tris)
        
        self.wait(0.075)
        self.add(tris)
        self.wait(0.075)
        self.remove(tris)

        self.wait(0.05)
        self.add(tris)
        self.wait(0.05)
        self.remove(tris)
        # square = Square().set_height(tris.get_height()).set_stroke(width=0.5, color=WHITE)
        # self.play(ReplacementTransform(square, tris), run_time=1)
        self.wait(0.2)
        self.play(ShowSubmobjectsOneByOne(tris), rate_func=linear, run_time=0.4)
        for i in tris:
            self.add(i)
            self.wait(0.1)
        self.play(*[ReplacementTransform(tris[i], squares[i]) for i in range(4)], 
            rate_func=rush_from, run_time=0.6)
        #self.play(ReplacementTransform(tris, squares), rate_func=linear, run_time=0.8)
        self.wait(0.1)
        self.play(*[ReplacementTransform(squares[i], logo[i]) for i in range(4)], 
            rate_func=rush_from, run_time=0.6)
        #self.play(ReplacementTransform(squares, logo), rate_func=linear, run_time=1.5)
        self.wait(0.1)
        self.play(
            text.restore, logo.restore,
            rate_func=rush_from, run_time=0.8
        )
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))


class DocumentHeader(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
        "font": "Orbitron",
    }
    def construct(self):
        logo = Logo(size=8/3, black_bg=False)
        text = VGroup(
            Text("Manim", font=self.font, color=BLACK, size=2),
            Text("Kindergarten", font=self.font, color=BLACK, size=2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).set_height(2.1).next_to(logo, buff=1.5).shift(DOWN*0.2)
        text[1][0].set_color(logo.color_1[2])
        text[0][0].set_color(logo.color_2[2])
        all_logo = VGroup(logo, text).center()
        line = Line(UP, DOWN, stroke_width=8, color=BLACK).move_to(mid(logo.get_right(), text.get_left()))
        line.set_length(1.4)

        mk_logo = VGroup(logo, text, line)
        document = VGroup(
            Text("中文教程文档", font="庞门正道标题体", size=1.8, color=BLACK),
            Text("manim_document_zh", font=self.font, size=1.2, color=GOLD_D),
        ).arrange(DOWN, aligned_edge=ORIGIN)
        document.next_to(mk_logo, DOWN, coor_mask=np.array([0, 1, 1]), buff=0.6)
        self.add(mk_logo, document)

