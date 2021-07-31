from manimlib_cairo.imports import *

class Logo(VGroup):

    CONFIG = {
        'color_1': [WHITE, BLUE_B, BLUE_D],
        'color_2': [WHITE, '#C59978', '#8D5630'],

        # 'color_3': [average_color("#CCCCCC", BLUE_C), BLUE_C, BLUE_D],
        # 'color_4': [average_color("#CCCCCC", "#C59978"), '#C59978', '#8D5630'],

        'color_3': [average_color(WHITE, BLUE_C), BLUE_C, BLUE_D],
        'color_4': [average_color(WHITE, "#C59978"), '#C59978', '#8D5630'],

        'center': ORIGIN,
        'size': 2,
        'shift_out': ORIGIN,
        'black_bg': True,
        'add_bg_square': False,
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.create_logo()

    def create_logo(self):

        p1 = Polygon(ORIGIN, RIGHT, 2 * UP, stroke_width=0).set_fill(self.color_1[0], 1)
        p2 = Polygon(1.5 * RIGHT, 3 * UR, 3 * UP, stroke_width=0).set_fill(self.color_1[1], 1)
        p3 = Polygon(2 * RIGHT, 3 * RIGHT, 3 * RIGHT + 2 * UP, stroke_width=0).set_fill(self.color_1[2], 1)
        if not self.black_bg:
            p1.set_fill(self.color_3[0], 1), p2.set_fill(self.color_3[1], 1), p3.set_fill(self.color_3[2], 1)

        self.bg = Square(stroke_width=0, fill_color=BLACK if self.black_bg else WHITE, fill_opacity=1).set_height(self.size * 2.5)
        if self.add_bg_square:
            self.add(self.bg)

        self.part_ur = VGroup(p1, p2, p3).move_to([2.5, 1., 0] + self.shift_out)
        self.part_ul = self.part_ur.copy().rotate(PI / 2, about_point=ORIGIN)
        self.part_dl = self.part_ur.copy().rotate(PI, about_point=ORIGIN)
        self.part_dr = self.part_ur.copy().rotate(3 * PI / 2, about_point=ORIGIN)

        self.add(self.part_ur, self.part_ul, self.part_dl, self.part_dr)
        self.set_height(self.size).move_to(self.center)
        if self.black_bg:
            self.part_ur[0].set_fill(self.color_2[0], 1), self.part_ur[1].set_fill(self.color_2[1], 1), self.part_ur[2].set_fill(self.color_2[2], 1)
        else:
            self.part_ur[0].set_fill(self.color_4[0], 1), self.part_ur[1].set_fill(self.color_4[1], 1), self.part_ur[2].set_fill(self.color_4[2], 1)

        self.inner_triangles = VGroup(self.part_ur[0], self.part_ul[0], self.part_dl[0], self.part_dr[0])
        self.mid_triangles = VGroup(self.part_ur[1], self.part_ul[1], self.part_dl[1], self.part_dr[1])
        self.outer_triangles = VGroup(self.part_ur[2], self.part_ul[2], self.part_dl[2], self.part_dr[2])


class OpeningScene(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#333333",
        },
        "enable_caching": False,
    }
    
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
            Text("Manim-Kindergarten", font="Orbitron bold", color=GREY_B),
            Text("鹤翔万里", font="PangMenZhengDao", color=WHITE, size=2.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(img, buff=0.5)
        text[0][0].set_color(logo.color_2[2])
        text[0][6].set_color(logo.color_1[2])
        all_logo = Group(logo, text, line, img).center()
        text = Group(text, line, img)

        bg = Rectangle(height=10, width=10, fill_color="#333333", fill_opacity=1, stroke_width=0)
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
        self.remove(bg)
        self.play(FadeOut(Group(*self.mobjects)))