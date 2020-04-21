from manimlib.imports import *

class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }


class NF24P3368(Scene_):
    def construct(self):
        line = Line(LEFT*3, RIGHT*3, color=BLACK)
        nodes = VGroup(
            *[
                Circle(radius=0.25, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK)
                for _ in range(7)
            ]
        ).arrange(RIGHT, buff=0.5)
        names = VGroup(
            *[
                TextMobject(str(i), color=BLACK).scale(0.7)
                for i in range(1, 8)
            ]
        )
        edges = VGroup(
            *[
                Arrow(nodes[i].get_center(), nodes[i + 1].get_center(), buff=0.25, color=BLACK)
                for i in range(6)
            ]
        )
        infs = VGroup(
            *[
                TextMobject("inf", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges[i], UP, buff=0.1)
                for i in range(6)
            ]
        )
        costs = VGroup(
            *[
                TextMobject("0", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges[i], DOWN, buff=0.1)
                for i in range(6)
            ]
        )
        for i in range(7):
            names[i].move_to(nodes[i])
        s = VGroup(
            Circle(radius=0.25, fill_color=WHITE, fill_opacity=1, stroke_color=RED),
            TextMobject("s", color=RED, background_stroke_width=0).scale(0.75)
        ).move_to(np.array([-4.5, -1.5, 0]))
        s.add(Arrow(s.get_center(), nodes[0].get_center(), color=RED, buff=0.25))
        s.add(TextMobject("k", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(s[-1], UL, buff=-0.5))
        s.add(TextMobject("0", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(s[-2], DR, buff=-0.5))
        t = VGroup(
            Circle(radius=0.25, fill_color=WHITE, fill_opacity=1, stroke_color=RED),
            TextMobject("t", color=RED, background_stroke_width=0).scale(0.75)
        ).move_to(np.array([4.5, -1.5, 0]))
        t.add(Arrow(nodes[-1].get_center(), t.get_center(), color=RED, buff=0.25))
        t.add(TextMobject("inf", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(t[-1], UR, buff=-0.5))
        t.add(TextMobject("0", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(t[-2], DL, buff=-0.5))

        braces = VGroup(
            Brace(VGroup(Dot(nodes[0].get_center(), radius=0.01), Dot(nodes[2].get_center(), radius=0.01)), UP, color=GRAY, buff=0.52),
            Brace(VGroup(Dot(nodes[2].get_center(), radius=0.01), Dot(nodes[5].get_center(), radius=0.01)), UP, color=GRAY, buff=0.52),
            Brace(VGroup(Dot(nodes[1].get_center(), radius=0.01), Dot(nodes[3].get_center(), radius=0.01)), DOWN, color=GRAY, buff=0.52),
            Brace(VGroup(Dot(nodes[4].get_center(), radius=0.01), Dot(nodes[6].get_center(), radius=0.01)), DOWN, color=GRAY, buff=0.52),
        )
        edges2 = VGroup(
            CurvedArrow(nodes[0].get_center(), nodes[2].get_center(), buff=0.25, color=BLACK, angle=-TAU / 4).shift(UP*1),
            CurvedArrow(nodes[2].get_center(), nodes[5].get_center(), buff=0.25, color=BLACK, angle=-TAU / 4).shift(UP*1),
            CurvedArrow(nodes[1].get_center(), nodes[3].get_center(), buff=0.25, color=BLACK, angle= TAU / 4).shift(DOWN*1),
            CurvedArrow(nodes[4].get_center(), nodes[6].get_center(), buff=0.25, color=BLACK, angle= TAU / 4).shift(DOWN*1),
        )
        caps2 = VGroup(
            TextMobject("1", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges2[0], UP, buff=0.1),
            TextMobject("1", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges2[1], UP, buff=0.1),
            TextMobject("1", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges2[2], UP, buff=-0.4),
            TextMobject("1", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges2[3], UP, buff=-0.4)
        )
        costs2 = VGroup(
            TextMobject("6", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges2[0], DOWN, buff=-0.4),
            TextMobject("3", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges2[1], DOWN, buff=-0.6),
            TextMobject("2", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges2[2], DOWN, buff=0.1),
            TextMobject("4", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges2[3], DOWN, buff=0.1),
        )
        old_num = VGroup(
            TextMobject("1", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.45),
            TextMobject("6", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.45),
            TextMobject("7", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.45),
            TextMobject("8", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.45),
            TextMobject("9", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.45),
            TextMobject("10", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.45),
            TextMobject("13", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.45),
        )
        for i in range(7):
            old_num[i].next_to(nodes[i], DOWN, buff=0.08)
        comments = VGroup(
            TextMobject("蓝-流量", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.7),
            TextMobject("橙-费用", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.7)
        ).arrange(DOWN, buff=0.2).next_to(s[0], RIGHT, buff=0.8)

        self.add(line, nodes, names, s, edges, infs, costs, t, braces, edges2, caps2, costs2, old_num, comments)
