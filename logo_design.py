from manimlib.imports import *

class MyTransform(Animation):
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


class Logo(Scene):
    CONFIG = {
        # "font": "Gray Design Bold",
        # "font": "Quicksand Bold",
        "font": "Orbitron",
        # "font": "Cairo",
        # "font": "Nexa Bold",
        # "font": "Comfortaa"
    }
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
            Text("Manim", font=self.font),
            Text("Kindergarten", font=self.font)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).set_height(2).next_to(logo, buff=1.2).shift(DOWN*0.2)
        text[1][0].set_color(BLUE_C)
        text[0][0].set_color("#8D5630")
        all_logo = VGroup(logo, text).center()

        line = Line(UP, DOWN, stroke_width=8).move_to(mid(logo.get_right(), text.get_left()))
        line.set_length(1.4)

        bg = Rectangle(height=10, width=10, fill_color=BLACK, fill_opacity=1, stroke_width=0)
        bg.add_updater(lambda m: m.move_to(logo, aligned_edge=RIGHT))

        text.save_state()
        text.shift((text.get_right()[0]-bg.get_right()[0]+0.2)*LEFT)
        logo.save_state()
        logo.center().scale(1.5)
        logo.rotate(TAU, axis=IN)
        
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
        self.add(line)
