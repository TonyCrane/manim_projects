from manimlib.imports import *

class Angle(VGroup):

    CONFIG = {
        'radius': 1,
        'color': RED,
        'opacity': 0.4,
        'stroke_width': 10,
        # 'below_180': True,
    }

    def __init__(self, A, O, B, **kwargs):

        VMobject.__init__(self, **kwargs)
        OA, OB = A-O, B-O
        theta = np.angle(complex(*OA[:2])/complex(*OB[:2])) # angle of OB to OA

        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius/2,
                     stroke_width=100 * self.radius, color=self.color).set_stroke(opacity=self.opacity).move_arc_center_to(O))
        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius,
                     stroke_width=self.stroke_width, color=self.color).move_arc_center_to(O))

class Unit_root(Scene):

    def construct(self):

        ## Create ComplexPlane ##
        cp_scale = 1.75
        cp = ComplexPlane().scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        ### about z^n ###
        color_dict = {'z': PINK, 'x': BLUE, 'y': YELLOW, 'i': RED, '\\cos': BLUE, '\\sin': YELLOW, '\\theta}': BLUE,
                      'r': PINK, 'e': GREEN, 'n': YELLOW, 'k': YELLOW, '\\omega': PINK, '\\pi': BLUE}
        complex_z = 0.9+0.6j
        vect_z = Arrow(cp.n2p(0), cp.n2p(complex_z), buff=0, color=ORANGE)
        dot_z = Dot(cp.n2p(complex_z), color=PINK)
        angle_z = Angle(cp.n2p(1), cp.n2p(0), cp.n2p(complex_z), radius=0.6, color=BLUE)

        ## 3 forms of complex num
        xy_form = TexMobject('z', '=', 'x', '+', 'y', 'i').set_color_by_tex_to_color_map(color_dict)
        cs_form = TexMobject('z', '=', 'r', '(', '\\cos{', '\\theta}', '+', 'i', '\\sin{', '\\theta}', ')').set_color_by_tex_to_color_map(color_dict)
        exp_form = TexMobject('z', '=', 'r', 'e^{', 'i', '\\theta}', color=WHITE).set_color_by_tex_to_color_map(color_dict).scale(1.2)
        exp_form[-1].set_color(BLUE)
        xy_form.next_to(dot_z, RIGHT * 0.6)
        cs_form.next_to(dot_z, RIGHT * 0.6)
        exp_form.next_to(dot_z, RIGHT * 0.6).shift(UP * 0.25)

        ## vgroup for z_i
        vect_group = VGroup(vect_z)
        dot_group = VGroup(dot_z)
        text_group = VGroup(exp_form)
        angle_group = VGroup(angle_z)
        line_group = VGroup(Line(cp.n2p(1), cp.n2p(complex_z), color=PINK))

        n = 10
        for i in range(n-1):
            zn_1 = complex_z ** (i+2-1)
            zn = complex_z ** (i+2)
            dot_i = Dot(cp.n2p(zn), color=PINK)
            vect_i = Arrow(cp.n2p(0), cp.n2p(zn), buff=0, color=ORANGE)
            text_i = TexMobject('z^{', '%d}' % (i+2), color=PINK).shift(cp.n2p(zn)/abs(zn) * (abs(zn) + 0.25))
            angle_i = Angle(cp.n2p(zn_1), cp.n2p(0), cp.n2p(zn), radius=0.6, color=BLUE)
            vect_group.add(vect_i)
            dot_group.add(dot_i)
            text_group.add(text_i)
            angle_group.add(angle_i)
            line_group.add(VGroup(Line(cp.n2p(zn_1), cp.n2p(zn), color=PINK)))

        ### conclusions from z^n =1 ###
        text_zn = TexMobject('z^', 'n', '=', 'r^', 'n', 'e^{', 'n', '\\theta', 'i}', '=', '1').set_color_by_tex_to_color_map(color_dict)
        text_zn[7].set_color(BLUE)
        text_zn.scale(1.2).to_corner(RIGHT * 3.25 + UP * 1.2)

        right_arrow = TexMobject('\\Rightarrow').next_to(text_zn, DOWN * 3.75).align_to(text_zn, LEFT)

        text_01 = TexMobject('r', '=', '1').set_color_by_tex_to_color_map(color_dict).next_to(right_arrow, RIGHT * 2.4).shift(UP * 0.5)
        text_02 = TexMobject('n', '\\theta', '=', '2', 'k', '\\pi').set_color_by_tex_to_color_map(color_dict).next_to(right_arrow, RIGHT * 2.4).shift(DOWN * 0.5)
        text_12 = VGroup(text_01, text_02)
        brace = Brace(text_12, LEFT)

        text_03 = TexMobject('\\therefore', '\\omega^', 'n', '=', '1', '\\text{的}', 'n', '\\text{个根为：}',)\
            .set_color_by_tex_to_color_map(color_dict).next_to(text_02, DOWN * 1.4).align_to(text_zn, LEFT)

        text_wi_01 = TexMobject('\\omega', '_k', '=', 'e^{', 'i', '{2', 'k', '\\pi', '\\over', 'n}}',
                              ).set_color_by_tex_to_color_map(color_dict)
        text_wi_01.next_to(text_03, DOWN * 1.5).align_to(text_zn, LEFT)
        text_wi_02 = TexMobject('=', '\\cos{', '2', 'k', '\\pi', '\\over', 'n}', '+', 'i', '\\sin{',
                             '2', 'k', '\\pi', '\\over', 'n}').set_color_by_tex_to_color_map(color_dict)
        text_wi_02.next_to(text_wi_01, DOWN * 1.5).align_to(text_zn, LEFT)
        text_wi_02[1:].scale(0.9)
        text_k = TexMobject('(', 'k', '=', '0', ',', '1', ',', '2', ',','\\cdots', ',', 'n-1', ')').set_color_by_tex_to_color_map(color_dict)
        text_k.scale(0.75).next_to(text_wi_02, DOWN * 1.5).align_to(text_zn, LEFT)

        ### display w_i in unit circle ###
        # moved to animation part 3 #

        ### animation part 1 ###

        self.play(ShowCreation(cp))
        self.wait(1)

        self.play(ShowCreation(vect_z))
        self.wait(0.5)
        self.play(ShowCreation(dot_z))
        self.play(Write(xy_form))
        self.wait(1)
        self.play(ReplacementTransform(xy_form, cs_form))
        self.wait(1)
        self.play(ReplacementTransform(cs_form, exp_form))
        self.wait()
        self.play(ShowCreation(angle_z))

        # self.add(vect_group, text_group, dot_group, angle_group, line_group)
        for i in range(1, n):
            self.play(ShowCreation(vect_group[i]), run_time=0.8)
            self.play(ShowCreation(dot_group[i]), run_time=0.4)
            self.play(Write(text_group[i]), run_time=0.6)
            self.wait(0.2)
            self.play(ShowCreation(angle_group[i]), run_time=0.6)
            self.wait(0.4)
        self.wait()
        for i in range(0, n):
            self.play(ShowCreation(line_group[i]), run_time=0.4)
            self.wait(0.1)
        self.wait()

        all_exist = VGroup(cp, vect_group, text_group, dot_group, angle_group, line_group)
        self.play(all_exist.shift, cp.n2p(-2), run_time=1.5)
        self.wait()

        ### part 2 ###
        text_bg = Polygon(cp.n2p(2.6+2.2j), cp.n2p(5.8+2.2j), cp.n2p(5.8-2.2j), cp.n2p(2.6-2.2j),
                          stroke_width=0, fill_color=BLACK, fill_opacity=0.75)
        self.play(FadeIn(text_bg), run_time=1.2)
        self.wait(0.5)
        self.play(TransformFromCopy(text_group, text_zn[0:9]), run_time=1.2)
        self.wait()
        self.play(Write(text_zn[9:11]))
        self.wait()
        self.play(Write(right_arrow))
        self.play(ShowCreation(brace))

        self.play(TransformFromCopy(text_zn[3:5], text_01))
        self.wait()

        self.play(TransformFromCopy(text_zn[6:8], text_02[0:2]))
        self.play(Write(text_02[2:6]))
        self.wait()

        self.play(Write(text_03), run_time=2)
        self.wait(0.5)
        self.play(Write(text_wi_01), run_time=2)
        self.wait()
        self.play(Write(text_wi_02), run_time=3)
        self.wait()
        self.play(Write(text_k), run_time=2)
        self.wait(2)

        ### part 3 ###
        unit_circle = Circle(radius=cp.n2p(1)[0], color=BLUE_B).move_to(cp.n2p(0))
        self.play(ShowCreation(unit_circle))
        self.wait(0.5)
        z_new = np.exp(1j * TAU/11)
        w_1 = TexMobject('\\omega', '_1', '=', 'e^{', 'i', '{2', '\\pi', '\\over', 'n}}',).scale(0.9)\
            .set_color_by_tex_to_color_map(color_dict).move_to(cp.n2p(0)).shift((cp.n2p(z_new)-cp.n2p(0))*1.2+RIGHT*1.2)
        dot_1 = Dot(cp.n2p(z_new), color=PINK)
        vect_1 = Arrow(cp.n2p(0), cp.n2p(z_new), buff=0, color=ORANGE)
        line_1 = Line(cp.n2p(1), cp.n2p(z_new), color=PINK)
        dot_0 = Dot(cp.n2p(1), color=PINK)
        vect_0 = Arrow(cp.n2p(0), cp.n2p(1), buff=0, color=ORANGE)
        w_0 = TexMobject('\\omega', '_0', color=PINK).scale(0.8).move_to(cp.n2p(1.2))
        self.play(ShowCreation(vect_0))
        self.play(ShowCreation(dot_0), Write(w_0))
        self.play(ReplacementTransform(vect_group[0], vect_1), run_time=0.3)
        self.play(ReplacementTransform(dot_group[0], dot_1), run_time=0.3)
        self.play(ReplacementTransform(text_group[0], w_1), run_time=0.3)
        self.play(ReplacementTransform(line_group[0], line_1), run_time=0.3)
        vect_new, dot_new, line_new, text_new = VGroup(vect_1), VGroup(dot_1), VGroup(line_1), VGroup(w_1)

        for i in range(1, n):
            zn_1 = z_new ** (i+1-1)
            zn = z_new ** (i+1)
            dot_i = Dot(cp.n2p(zn), color=PINK)
            vect_i = Arrow(cp.n2p(0), cp.n2p(zn), buff=0, color=ORANGE)
            text_i = TexMobject('\\omega_{', '%d}' % (i+1), color=PINK).scale(0.8).move_to(cp.n2p(0)).shift((cp.n2p(zn)-cp.n2p(0))/abs(zn) * (abs(zn) + 0.2))
            line_i = Line(cp.n2p(zn_1), cp.n2p(zn), color=PINK)
            angle_i = Angle(cp.n2p(zn_1), cp.n2p(0), cp.n2p(zn), radius=0.6, color=BLUE)
            vect_new.add(vect_i), dot_new.add(dot_i), line_new.add(line_i), text_new.add(text_i)
            # vect_group[i].become(vect_i)
            # self.wait(dt)
            self.play(ReplacementTransform(vect_group[i], vect_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(angle_group[i], angle_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(dot_group[i], dot_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(text_group[i], text_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(line_group[i], line_i), run_time=0.32-0.08*np.sqrt(i))

        angle_11 = Angle(cp.n2p(1), cp.n2p(0), cp.n2p(np.exp(-1j * TAU/11)), radius=0.6, color=BLUE)
        line_11 = Line(cp.n2p(np.exp(-1j * TAU/11)), cp.n2p(1), color=PINK)
        self.play(ShowCreation(angle_11))
        self.play(ShowCreation(line_11))

        self.wait(5)



