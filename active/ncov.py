from manimlib.imports import *
from manim_projects.tony_useful.imports import *

class Test_MySectors(Scene):
    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
            "use_plot_depth": True,
        },
    }

    def add_comment(self):
        rect_1 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_11 = Text('数据为3月14日前无新增确诊病例的27个省（市，区）', font='思源黑体 CN Bold', color=color).set_height(0.24).next_to(rect_1, RIGHT * 0.32).align_to(rect_1, DOWN)
        text_11.set_color_by_t2c({'3月14日': BLUE})
        text_line_01 = VGroup(rect_1, text_11).to_corner(LEFT * 16 + UP * 1.)
        rect_2 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_12 = Text('数据来源：@央视新闻', font='思源黑体 CN Bold', color=color).set_height(0.24).next_to(rect_2, RIGHT * 0.32).align_to(rect_2, DOWN)
        text_12.set_color_by_t2c({'@央视新闻': ORANGE})
        text_line_02 = VGroup(rect_2, text_12).to_corner(LEFT * 16 + UP * 1.75)
        rect_3 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_13 = Text('作者：@cigar666', font='思源黑体 CN Bold', color=color).set_height(0.24).next_to(rect_3, RIGHT * 0.32).align_to(rect_3, DOWN)
        text_13.set_color_by_t2c({'@cigar666': PINK})
        text_line_03 = VGroup(rect_3, text_13).to_corner(LEFT * 16 + UP * 2.5)
        self.add(text_line_01, text_line_02, text_line_03)


    def construct(self):
        values = [2, 2, 2, 3, 9, 9, 10, 11, 14, 15, 15, 15, 15, 16, 18, 18, 18,
                  19, 22, 23, 23, 24, 24, 25, 26, 37, 44]
        labels = ['广东', '山东', '河南', '黑龙江', '四川', '浙江', '宁夏', '辽宁',
                  '湖南', '天津', '河北', '江西', '安徽', '福建', '山西', '广西', '重庆',
                  '吉林', '云南', '海南', '陕西', '内蒙古', '江苏', '新疆', '贵州', '青海', '西藏']

        center = UP * 0.5 + LEFT * 2.25

        graph_01 = MySectors(inner_radius=1.5, values=values, labels=labels, start_direction=RIGHT,
                             unit='天', center=center)
        color = average_color(BLUE_C, BLACK, BLACK)
        graph_01.create_cicles(color)
        graph_01.create_circle_shadow(color=color)
        graph_01.circles.set_plot_depth(5)
        graph_01.shadow.set_plot_depth(5)

        font='思源宋体 CN Heavy'
        text_01 = Text('多个省市区', font=font, color=color, size=0.32)
        text_02 = Text('确诊病例连续多日', font=font, color=color, size=0.32).next_to(text_01, DOWN * 0.25)
        text_03 = Text('零新增', font=font, color=color, size=0.75).next_to(text_02, DOWN * 0.4)
        texts = VGroup(text_01, text_02, text_03).move_to(center)

        # self.add_comment()

        start_mobjects = VGroup()
        value_trackers = []
        angle_trackers = []
        start_a = np.angle(complex(*RIGHT[0:2]))
        for i in range(len(values)):
            start_mobjects.add(graph_01[0][0].copy().set_plot_depth(-100+2*(len(values)-1-i)))
            value_trackers.append(ValueTracker(graph_01[0][0].outer_radius))
            angle_trackers.append(ValueTracker(start_a+0*TAU/len(values)))
        def updater(obj):
            for index in range(len(values)):
                r = value_trackers[index].get_value()
                size = TAU * r / len(values) * 0.2
                angle = TAU / len(values)
                angle_ = angle_trackers[index].get_value()
                start_a = np.angle(complex(*RIGHT[0:2]))
                obj[index].set_height(2 * size)
                obj[index].move_to(center + complex_to_R3((r-size*1.2-r*0.05)*np.exp(1j*(angle_+0.5*angle))))
        graph_01[1].add_updater(updater)
        self.add(start_mobjects, *graph_01[1], graph_01[2:], texts)
        self.wait(1)
        self.play(
            *[
                MyRotating(start_mobjects[i], graph_01[0][-1-i], value_trackers[-1-i], angle_trackers[-1-i], len(values)-1-i, radians=TAU-(i+1)*TAU/len(values),
                about_point=center, len=len(values), rate_func=smooth)
                for i in range(len(values))
            ]
        )
        self.wait(2)

class Test_MySectors_0315(Scene):

    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
        },
    }

    def construct(self):

        values = [3, 3, 4, 10, 11, 12, 15, 16, 16, 16, 16, 17, 19, 19, 19,
                  20, 23, 24, 24, 25, 25, 26, 27, 38, 45]
        labels = ['山东', '河南', '黑龙江', '四川', '宁夏', '辽宁',
                  '湖南', '天津', '河北', '江西', '安徽', '福建', '山西', '广西', '重庆',
                  '吉林', '云南', '海南', '陕西', '内蒙古', '江苏', '新疆', '贵州', '青海', '西藏']

        center = UP * 0.5 + LEFT * 2.25

        graph_01 = MySectors(inner_radius=1.5, values=values, labels=labels, start_direction=RIGHT,
                             unit='天', center=center)
        color = average_color(BLUE_B, BLACK, BLACK)
        graph_01.create_cicles(color)
        graph_01.create_circle_shadow(color=color)

        font='思源宋体 CN'
        text_01 = Text('多个省市区', font=font, color=color, size=0.32)
        text_02 = Text('确诊病例连续多日', font=font, color=color, size=0.32).next_to(text_01, DOWN * 0.25)
        text_03 = Text('零新增', font=font, color=color, size=0.75).next_to(text_02, DOWN * 0.4)
        texts = VGroup(text_01, text_02, text_03).move_to(center)

        rect_1 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_11 = Text('数据为3月15日前无新增确诊病例的25个省（市，区）', font='思源黑体 CN Bold', color=color).set_height(0.24).next_to(rect_1, RIGHT * 0.32).align_to(rect_1, DOWN)
        text_11.set_color_by_t2c({'3月15日': BLUE})
        text_line_01 = VGroup(rect_1, text_11).to_corner(LEFT * 16 + UP * 1.)
        rect_2 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_12 = Text('数据来源：@央视新闻', font='思源黑体 CN Bold', color=color).set_height(0.24).next_to(rect_2, RIGHT * 0.32).align_to(rect_2, DOWN)
        text_12.set_color_by_t2c({'@央视新闻': ORANGE})
        text_line_02 = VGroup(rect_2, text_12).to_corner(LEFT * 16 + UP * 1.75)
        rect_3 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_13 = Text('作者：@cigar666', font='思源黑体 CN Bold', color=color).set_height(0.24).next_to(rect_3, RIGHT * 0.32).align_to(rect_3, DOWN)
        text_13.set_color_by_t2c({'@cigar666': PINK})
        text_line_03 = VGroup(rect_3, text_13).to_corner(LEFT * 16 + UP * 2.5)

        self.add(graph_01, texts, text_line_01, text_line_02, text_line_03)
        self.wait(5)