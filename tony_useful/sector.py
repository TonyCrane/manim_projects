from manimlib.imports import *

class MySectors(VGroup):
    CONFIG = {
        'stroke_width': 0,
        'fill_opacity': 1,
        'inner_radius': 1.6,
        # 'outer_radius': [],
        'gap': 0.025,
        'start_direction': UP,
        'values': [1,2,3],
        'labels': None,
        # 'data': {'labels': 1.23},
        'unit': None,
        # 'data_2d': None,
        'outer_radius_func': lambda t: t/10 + 0.32,
        'label_font': '思源黑体 CN Bold',
        'center': ORIGIN,
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.colors = color_gradient([ORANGE, RED, PINK, BLUE, GREEN, YELLOW], len(self.values))
        self.sectors, self.labels_group = VGroup(), VGroup()
        self.sectors = self.create_sectors()
        if not self.labels == None:
            self.labels_group = self.create_label()
        self.add(self.sectors, self.labels_group)


    def create_sectors(self):
        angle = TAU/len(self.values)
        colors = self.colors
        start_a = np.angle(complex(*self.start_direction[0:2]))

        for i in range(len(self.values)):
            r_i = self.inner_radius + self.outer_radius_func(self.values[i])
            sector_i = Sector(arc_center=self.center, inner_radius=self.inner_radius, outer_radius=r_i,
                              stroke_width=self.stroke_width, start_angle=start_a + i * angle,
                              angle=angle * (1 - self.gap), color=colors[i], fill_opacity=self.fill_opacity)
            self.sectors.add(sector_i)
        return self.sectors
        

    def create_label(self):
        for tex, value in zip(self.labels, self.values):
            i = self.labels.index(tex)
            r = self.inner_radius + self.outer_radius_func(self.values[i])
            size = TAU * r / len(self.values) * 0.2
            tex_i = Text(tex, font=self.label_font, color=WHITE, plot_depth=1).set_height(size)
            value_i = Text(str(value), font=self.label_font, color=WHITE, plot_depth=1).set_height(size).next_to(tex_i, DOWN * 0.64 * size)
            if not self.unit == None:
                unit_i = Text(self.unit, font=self.label_font, color=WHITE, plot_depth=1).set_height(size).next_to(value_i, RIGHT * 0.2 * size)
                VGroup(value_i, unit_i).next_to(tex_i, DOWN * 0.64 * size)
                label_i = VGroup(tex_i, value_i, unit_i)
            else:
                label_i = VGroup(tex_i, value_i)
            angle = TAU/len(self.values)
            start_a = np.angle(complex(*self.start_direction[0:2]))
            self.labels_group.add(label_i.shift(self.center + complex_to_R3((r-size * 1.2-r*0.05) * np.exp(1j * (start_a + (i + 0.5) * TAU/len(self.values))))))
        return self.labels_group

    def create_cicles(self, color=BLUE_A):

        circle_01 = Circle(radius=self.inner_radius, stroke_width=12, stroke_color=color, plot_depth=2.5)
        circle_02 = Circle(radius=self.inner_radius - 0.15, stroke_width=4, stroke_color=color, plot_depth=2.5)
        self.circles = VGroup(circle_01, circle_02).move_to(self.center)
        self.add(self.circles)
        return self.circles

    def create_circle_shadow(self, width=32, num=50, color=BLUE_A):
        self.shadow = VGroup(*[Circle(radius=self.inner_radius + (i+0.5) * width/100/num, stroke_width=width/num, stroke_color=color,
                                      stroke_opacity=(i-num) ** 2 * 1/num/num, plot_depth=2) for i in range(num+1)]).move_to(self.center)
        self.add(self.shadow)
        return self.shadow


class MyRotating(Animation):
    CONFIG = {
        "axis": OUT,
        "radians": TAU,
        "run_time": 3,
        "rate_func": linear,
        "about_point": None,
        "inner_radius": 1.5,
        'stroke_width': 0,
        'fill_opacity': 1,
        'start_direction': RIGHT,
        "len": 27,
        "gap": 0.025,
    }

    def __init__(self, mobject, target, value, angle_tracker, index, **kwargs):
        digest_config(self, kwargs)
        self.mobject = mobject
        self.target_mobject = target
        self.value_tracker = value
        self.angle_tracker = angle_tracker
        self.index = index
    
    def interpolate_mobject(self, alpha):
        # now_mobject = self.starting_mobject.copy()
        r_i = interpolate(self.starting_mobject.outer_radius, self.target_mobject.outer_radius, alpha)
        color = interpolate_color(self.starting_mobject.get_color(), self.target_mobject.get_color(), alpha)
        start_a = np.angle(complex(*self.start_direction[0:2]))
        angle = TAU / self.len
        now_mobject = Sector(
            arc_center=self.about_point,
            inner_radius=self.inner_radius,
            outer_radius=r_i,
            stroke_width=self.stroke_width, 
            start_angle=start_a, #+ 1 * angle,
            angle=angle * (1 - self.gap), 
            color=color, 
            fill_opacity=self.fill_opacity
        )
        now_mobject.rotate(
            alpha * self.radians,
            axis=self.axis,
            about_point=self.about_point,
        ).set_plot_depth(-100+self.index*2)
        self.mobject.become(now_mobject)
        self.value_tracker.set_value(r_i)
        self.angle_tracker.set_value(start_a + alpha * self.radians)
    
    # def clean_up_from_scene(self, scene):
    #     scene.remove(self.mobject)
    #     scene.add(self.target_mobject)