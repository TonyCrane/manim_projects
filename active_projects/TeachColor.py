from manimlib.imports import *
from manim_sandbox.utils.imports import *
from manim_projects.tony_useful.imports import *


class ColorText(Text):
    CONFIG = {
        "size": 0.4,
        "font": "Consolas",
        "t2c": {
            '"': YELLOW_E,
            'np': BLACK,
            'array': BLUE_D,
            '~': WHITE
        },
        "color": DARK_GRAY,
    }
    def __init__(self, color, name=None, **kwargs):
        if name:
            Text.__init__(self, name, color=color, **kwargs)
        else:
            if isinstance(color, str):
                Text.__init__(self, '"' + color + '"', color=color, **kwargs)
            elif color[0] > 1 or color[1] > 1 or color[2] > 1:
                name = 'np.array([{},~{},~{}])'.format(
                    str(int(color[0])).rjust(3, "~"), 
                    str(int(color[1])).rjust(3, "~"), 
                    str(int(color[2])).rjust(3, "~")
                )
                Text.__init__(self, name, color=rgb_to_color(color/255), **kwargs)
                self[10:name.index(",")].set_color(RED)
                self[name.index(",")+2:name.index(",", name.index(",")+1)].set_color(GREEN)
                self[name.index(",", name.index(",")+1)+2:-2].set_color(BLUE)
                self.set_color_by_t2c({"~": "#EBEBEB"})
            else:
                name = 'np.array([{},~{},~{}])'.format(color[0], color[1], color[2])
                Text.__init__(self, name, **kwargs)
                self[10:name.index(",")].set_color(RED)
                self[name.index(",")+2:name.index(",", name.index(",")+1)].set_color(GREEN)
                self[name.index(",", name.index(",")+1)+2:-2].set_color(BLUE)
                self.set_color_by_t2c({"~": "#EBEBEB"})
                


class TestColor(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        color = VGroup(
            ColorText(RED_C, "RED_C"),
            ColorText("#66CCFF"),
            ColorText(np.array([255, 165, 0])),
        ).arrange(DOWN)
        test = Text("test", font="Consolas").set_color(rgb_to_color(np.array([255/255, 165/255, 0])))
        self.add(color)


class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }


class OpeningScene(Scene_):
    def construct(self):
        t2c = {"manim": average_color(PINK, RED),
               "颜色": BLUE_D}
        text_color = DARK_GRAY

        font = "PangMenZhengDao"
        text_1 = Text("大家好!", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 2, buff=1)
        text_2 = Text("欢迎来到manim视频教程", font=font,
                      color=text_color, size=1, t2c=t2c).to_edge(UP * 3.2, buff=1)
        text_3 = Text("这一期我们将学习manim中", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 1.8, buff=1)
        text_4 = Text("颜色的表示和相关方法", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 3., buff=1)
        text_34, text_12 = VGroup(text_3, text_4), VGroup(text_1, text_2)


        methods = [['Color', 'constants', 'hex', 'RGB'],
                   ['color_to_rgb', 'rgb_to_color', 'rgb_to_hex', 'hex_to_rgb'],
                   ['invert_color, ', 'color_gradient, ', 'average_color, ', 'random_color,'],
                   ['set_color, ', 'set_color_by_gradient, ', 'set_sheen']]
        m_group_1 = VGroup(*[Text(tex + ', ', size=0.42, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[0]]).arrange(RIGHT)
        m_group_2 = VGroup(*[Text(tex + ', ', size=0.42, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[1]]).arrange(RIGHT)
        m_group_3 = VGroup(*[Text(tex, size=0.42, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[2]]).arrange(RIGHT)
        m_group_4 = VGroup(*[Text(tex, size=0.42, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[3]]).arrange(RIGHT)
        m_group = VGroup(m_group_1, m_group_2, m_group_3, m_group_4).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        methodes_group = VGroup(*m_group_1, *m_group_2, *m_group_3, *m_group_4).next_to(text_34, DOWN, buff=0.5)

        # self.add(picture)
        self.wait(0.5)
        self.play(Write(text_1))
        self.wait(0.5)
        self.play(WriteRandom(text_2), run_time=1.5)
        self.wait(1.8)
        self.play(ReplacementTransform(text_12, text_34), run_time=1.2)
        self.wait(1.2)
        self.play(FadeInRandom(methodes_group), run_time=2.4)
        self.wait(2.6)
        self.play(FadeOutRandom(methodes_group), FadeOutRandom(text_3),
                  FadeOutRandom(text_4), run_time=1.8)
        self.wait(1)


class ExpressAColor(Scene_):
    def start(self):
        t2c = {"manim": GOLD,
               "颜色": BLUE_D}
        title = VGroup(
            Text("Chapter Ⅰ.", font="Monaco for Powerline", color=BLUE_D, size=0.5, t2c=t2c),
            Text("manim中颜色的表示", font="Source Han Sans CN Bold", color=DARK_GRAY, size=0.5, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "在manim中,颜色使用RGB模式",
            "可以用定义的常量、十六进制和RGB数组来表示",
            "constants.py中定义了这54种颜色常量,可以直接使用",
            "以_C结尾的也可以省去_C,例如BLUE_C也可写作BLUE",
            "所有的GRAY也可写作GREY(GREY_BROWN除外)",
            "也可以使用十六进制来表示颜色",
            "具体为一个字符串,以#开头,后接六位十六进制颜色(hex)",
            "也可以使用一个ndarray来表示RGB颜色",
            "并使用相应方法转化为hex或Color(后面会讲)",
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        
        colors = VGroup(
            VGroup(
                *[
                    VGroup(
                        *[
                            ColorText(color, name) for name, color in list(COLOR_MAP.items())[i:i + 5]
                        ]
                    ).arrange(DOWN, aligned_edge=LEFT)
                    for i in range(3, 43, 5)
                ]
            ).arrange(RIGHT),
            VGroup(
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[:3]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[43:46]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[47:52:2]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[53:56]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[-2:]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
            ).arrange(RIGHT)
        ).arrange(DOWN, buff=0.5)
        colors[1][1][0].add_background_rectangle(buff=0.1)
        withoutc = VGroup(
            ColorText(BLUE, "BLUE").move_to(colors[0][0][2], aligned_edge=LEFT),
            ColorText(TEAL, "TEAL").move_to(colors[0][1][2], aligned_edge=LEFT),
            ColorText(GREEN, "GREEN").move_to(colors[0][2][2], aligned_edge=LEFT),
            ColorText(YELLOW, "YELLOW").move_to(colors[0][3][2], aligned_edge=LEFT),
            ColorText(GOLD, "GOLD").move_to(colors[0][4][2], aligned_edge=LEFT),
            ColorText(RED, "RED").move_to(colors[0][5][2], aligned_edge=LEFT),
            ColorText(MAROON, "MAROON").move_to(colors[0][6][2], aligned_edge=LEFT),
            ColorText(PURPLE, "PURPLE").move_to(colors[0][7][2], aligned_edge=LEFT),
        )
        recs = VGroup(
            *[
                SurroundingRectangle(colors[0][i][2], color=GOLD)
                for i in range(8)
            ]
        )
        grey = VGroup(
            ColorText(LIGHT_GREY, "LIGHT_GREY").move_to(colors[1][1][2]),
            ColorText(GREY, "GREY").move_to(colors[1][2][0]),
            ColorText(DARK_GREY, "DARK_GREY").move_to(colors[1][2][1]),
            ColorText(DARKER_GREY, "DARKER_GREY").move_to(colors[1][2][2]),
        )
        recs2 = VGroup(
            SurroundingRectangle(colors[1][1][2], color=GOLD),
            SurroundingRectangle(colors[1][2][0], color=GOLD),
            SurroundingRectangle(colors[1][2][1], color=GOLD),
            SurroundingRectangle(colors[1][2][2], color=GOLD),
        )

        self.play(Write(caps[0]))
        self.wait(3)
        self.play(Transform(caps[0], caps[1]))
        self.wait(3)
        self.play(Transform(caps[0], caps[2]))
        self.wait()
        self.play(Write(colors[0]))
        self.play(Write(colors[1]))
        self.wait(4)
        self.play(Transform(caps[0], caps[3]))
        self.wait(2)
        self.play(ShowCreation(recs, lag_ratio=0.8))
        self.play(
            *[
                Transform(colors[0][i][2], withoutc[i])
                for i in range(8)
            ]
        )
        self.play(FadeOut(recs))
        self.wait(2)
        self.play(Transform(caps[0], caps[4]))
        self.wait(2)
        self.play(ShowCreation(recs2, lag_ratio=0.8))
        self.play(
            Transform(colors[1][1][2], grey[0]),
            Transform(colors[1][2][0], grey[1]),
            Transform(colors[1][2][1], grey[2]),
            Transform(colors[1][2][2], grey[3]),
        )
        self.play(FadeOut(recs2))
        self.wait(3)
        self.play(Transform(caps[0], caps[5]))
        self.wait(2)
        self.play(FadeOut(colors))
        self.play(Transform(caps[0], caps[6]))
        hex_color = VGroup(
            ColorText("#66CCFF", size=0.55),
            ColorText("#00FFCC", size=0.55),
            ColorText("#EE0000", size=0.55),
        ).arrange(DOWN)
        self.play(
            *[
                FadeIn(VGroup(color[:2], color[-1]))
                for color in hex_color
            ]
        )
        self.wait()
        self.play(
            *[
                Write(color[2:-1])
                for color in hex_color
            ]
        )
        self.wait(2)
        self.play(Transform(caps[0], caps[7]))
        self.wait()
        rgb = VGroup(
            ColorText(hex_to_rgb("#66CCFF") * 255, size=0.55),
            ColorText(hex_to_rgb("#00FFCC") * 255, size=0.55),
            ColorText(hex_to_rgb("#EE0000") * 255, size=0.55)
        ).arrange(DOWN)
        self.play(
            *[
                Transform(hex_color[i], rgb[i])
                for i in range(3)
            ]
        )
        self.wait(3)
        self.play(Transform(caps[0], caps[8]))
        self.wait(3)
        self.play(
            FadeOut(caps[0]), FadeOut(hex_color)
        )


class ConvertColor(Scene_):
    def start(self):
        t2c = {"manim": GOLD,
               "颜色": BLUE_D}
        title = VGroup(
            Text("Chapter II.", font="Monaco for Powerline", color=BLUE_D, size=0.5, t2c=t2c),
            Text("颜色表示方法的相互转换", font="Source Han Sans CN Bold", color=DARK_GRAY, size=0.5, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "manimlib/utils/color.py中包含一些转换颜色表示方法的函数",
            "首先再次明确manim中颜色的表示",
            "manim表示颜色有hex,rgb,int_rgb,Color类四种",
            "rgb与int_rgb的区别是前者RGB值为0至1,后者为0至255",
            "Color类是最终的颜色,一切表示方法都将转化为Color类",
            "hex与rgb相互转换可以使用hex_to_rgb和rgb_to_hex函数",
            "rgb和int_rgb之间互相转换使用乘/除255就可以解决",
            "rgb和Color转换可以使用rgb_to_color和color_to_rgb函数",
            "另外还有color_to_int_rgb函数将Color转换为int_rgb",
            "hex和Color没有必要相互转换",
            "但是在manim中,可以放入set_color等方法的仅有hex和Color",
            "使用rgb或者int_rgb时需要先转换为hex或者Color"
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        func_list = [
            "hex_to_rgb", "rgb_to_hex",
            "color_to_rgb", "rgb_to_color",
            "color_to_int_rgb"
        ]
        path = CodeLine("manimlib/utils/color.py")
        func = VGroup(
            *[
                CodeLine(each) for each in func_list
            ]
        ).arrange(DOWN)
        first = VGroup(path, func).arrange(RIGHT)
        path.save_state()

        self.play(Write(caps[0]))
        path.center()
        self.play(Write(path))
        self.play(path.restore, FadeInFromDown(func))
        self.wait(2)
        self.play(FadeOut(first), Transform(caps[0], caps[1]))
        self.wait(3)
        self.play(Transform(caps[0], caps[2]))

        color_type = VGroup(
            CodeLine("hex", size=0.5),
            CodeLine("rgb", size=0.5),
            CodeLine("int_rgb", size=0.5),
            CodeLine("Color", size=0.55)
        ).arrange(DOWN, buff=1.5)
        color_type[-1].next_to(color_type[1], RIGHT, buff=4)
        color_type.center()
        dar1 = DoubleArrow(color_type[1].get_bottom(), color_type[2].get_top(), color=ORANGE)
        dars = VGroup(
            *[Arrow(mob.get_right(), color_type[-1].get_left()).set_color([PURPLE, GREEN]).set_sheen_direction(RIGHT)
            for mob in color_type[:-1]]
        )
        for each in dars:
            each.tip.set_color(GREEN)
        times255 = CodeLine("×255").add_background_rectangle(color=WHITE).move_to(dar1)

        self.play(Write(color_type[:-1]))
        self.play(Write(color_type[-1]))
        self.wait(2)
        self.play(Transform(caps[0], caps[3]))
        self.play(Write(dar1))
        self.play(Write(times255))
        self.wait(2)
        self.play(Transform(caps[0], caps[4]))
        self.play(Write(dars))
        self.wait(3)

        self.play(Transform(caps[0], caps[5]), FadeOut(VGroup(color_type, dar1, dars, times255)))
        convert_hex_and_rgb = VGroup(
            CodeLine("hex"),
            TexMobject("\\Longleftrightarrow", color=ORANGE, background_stroke_width=0),
            CodeLine("rgb")
        ).arrange(RIGHT).scale(1.4).to_corner(UL, buff=1)
        code1 = VGroup(
            VGroup(
                CodeLine("hex_to_rgb(", size=0.4),
                ColorText("#66CCFF"),
                CodeLine(")", size=0.4),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(hex_to_rgb("#66CCFF"))
            ).arrange(RIGHT),
            VGroup(
                CodeLine("rgb_to_hex(", size=0.4),
                ColorText(hex_to_rgb("#66CCFF")),
                CodeLine(")", size=0.4),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText("#66CCFF")
            ).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT)
        code1[:2].shift(UP*0.5)
        code1[2:].shift(DOWN*0.5)
        bg = Rectangle(stroke_width=1, fill_color="#EBEBEB", plot_depth=-10, stroke_color=DARK_GRAY, fill_opacity=1)
        bg.surround(code1, buff=0.5)
        self.play(Write(convert_hex_and_rgb), FadeInFromDown(bg))
        self.play(Write(code1[0][0][:-1]), Write(code1[2][0][:-1]))
        self.wait(2)
        self.play(Write(VGroup(code1[0][0][-1], code1[0][1:])))
        self.play(Write(code1[1]))
        self.wait()
        self.play(Write(VGroup(code1[2][0][-1], code1[2][1:])))
        self.play(Write(code1[3]))
        self.wait(4)
        self.play(
            Transform(caps[0], caps[6]),
            FadeOut(VGroup(bg, code1, convert_hex_and_rgb))    
        )
        convert_rgb_and_int = VGroup(
            CodeLine("rgb"),
            TexMobject("\\rightleftharpoons", color=ORANGE, background_stroke_width=0).set_width(1.6, True),
            CodeLine("int_rgb")
        ).arrange(RIGHT, buff=0.25).scale(1.4)
        times255.remove(times255.background_rectangle).next_to(convert_rgb_and_int[1], UP)
        divide255 = CodeLine("÷255").next_to(convert_rgb_and_int[1], DOWN)
        self.play(Write(convert_rgb_and_int[0]), Write(convert_rgb_and_int[-1]))
        self.play(Write(convert_rgb_and_int[1]))
        self.wait()
        self.play(Write(times255))
        self.play(Write(divide255))
        self.wait(2)
        self.play(
            Transform(caps[0], caps[7]),
            FadeOut(VGroup(convert_rgb_and_int, times255, divide255))
        )
        self.wait()

        convert_rgb_and_color = VGroup(
            CodeLine("rgb"),
            TexMobject("\\Longleftrightarrow", color=ORANGE, background_stroke_width=0),
            CodeLine("Color")
        ).arrange(RIGHT).scale(1.4).to_corner(UL, buff=0.6)
        code2 = VGroup(
            VGroup(
                CodeLine("rgb_to_color(", size=0.35),
                ColorText(hex_to_rgb("#66CCFF"), size=0.35),
                CodeLine(")", size=0.35),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.35).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                CodeLine("<Color #6cf>", size=0.35)
            ).arrange(RIGHT),
            CodeLine("color = Color(\"#66CCFF\")"),
            VGroup(
                CodeLine("color_to_rgb(", size=0.35),
                CodeLine("color", size=0.35),
                CodeLine(")", size=0.35),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.35).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(hex_to_rgb("#66CCFF"), size=0.35)
            ).arrange(RIGHT),
            CodeLine("color_to_int_rgb( color )", size=0.35),
            VGroup(
                CodeLine("~~~~", size=0.35).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(hex_to_rgb("#66CCFF")*255, size=0.35)
            ).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT)
        code2[:2].shift(UP*0.5)
        code2[2:].shift(DOWN*0.2)
        bg2 = Rectangle(stroke_width=1, fill_color="#EBEBEB", plot_depth=-10, stroke_color=DARK_GRAY, fill_opacity=1)
        bg2.surround(code2, buff=0.5).set_height(4.8, True)
        self.play(Write(convert_rgb_and_color), FadeInFromDown(bg2))
        self.play(Write(code2[0][0][:-1]), Write(code2[3][0][:-1]))
        self.wait(2)
        self.play(Write(VGroup(code2[0][0][-1], code2[0][1:])))
        self.play(Write(code2[1]))
        self.wait()
        self.play(Write(code2[2]))
        self.play(Write(VGroup(code2[3][0][-1], code2[3][1:])))
        self.play(Write(code2[4]))
        self.wait(2)
        self.play(Transform(caps[0], caps[8]))
        self.play(Write(code2[5]))
        self.play(Write(code2[6]))
        self.wait(2)

        self.play(Transform(caps[0], caps[9]))

        self.wait(2)
        self.play(FadeOut(VGroup(bg2, code2, convert_rgb_and_color)))
        self.wait()
        dar2 = DoubleArrow(color_type[0].get_bottom(), color_type[1].get_top(), color=ORANGE)
        self.play(Transform(caps[0], caps[10]), FadeIn(VGroup(color_type, dars, dar1, dar2)))
        self.wait()
        recs = VGroup(
            SurroundingRectangle(color_type[0]),
            SurroundingRectangle(color_type[3]),
        )
        self.play(Write(recs))
        self.wait(2)
        self.play(Transform(caps[0], caps[11]))
        self.wait(4)
        self.play(FadeOut(VGroup(*self.mobjects)))



        









class CodeLine(Text):
    CONFIG = {
        't2c': {
            'x': average_color(BLUE, PINK),
            'y': average_color(BLUE, PINK),
            'z': average_color(BLUE, PINK),
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'IN': ORANGE,
            'OUT': ORANGE,
            'ORIGIN': ORANGE,
            'DL': ORANGE,
            'DR': ORANGE,
            'UL': ORANGE,
            'UR': ORANGE,
            'TOP': ORANGE,
            'BOTTOM': ORANGE,
            'LEFT_SIDE': ORANGE,
            'RIGHT_SIDE': ORANGE,
            'manim': GOLD,
            'constants.py': GOLD,
            'manimlib/utils/color.py': GOLD,
            '#': GOLD,
            '_C': BLUE,
            'BLUE_C': BLUE,
            'BLUE': BLUE,
            'RGB': PURPLE,
            'rgb': PURPLE,
            'int_rgb': PURPLE,
            'hex': PURPLE,
            'Color': GREEN,
            'FRAME_HEIGHT': BLUE_D,
            'FRAME_WIDTH': BLUE_D,
            'PIXEL_HEIGHT': RED_B,
            'PIXEL_WIDTH': RED_B,
            'np': BLACK,
            'array': BLUE_D,
            'ndarray': BLUE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'arrange': BLUE_D,
            'VGroup': BLUE_D,
            'VMobject': BLUE_D,
            'ImageMobject': BLUE_D,
            'list': BLUE_D,
            'append': BLUE_D,
            'remove': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'GREY_BROWN': GREY_BROWN,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'add_to_back': BLUE_D,
            'vector': ORANGE,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'aligned_edge': RED,
            'center': RED,
            ">>>": RED,
            'coor_mask': RED,
            'point_or_mobject': RED,
            'python': GOLD,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'True': average_color(BLUE, PINK),
            '2D': RED_B,
            '3D': RED_B,
            'self': PINK,
            'mob': RED_D,
            'mob1': RED_D,
            'mob2': RED_D,
            'mob3': RED_D,
            'mob0': RED_D,
            "~": WHITE,
            "vg2": DARK_GRAY,
            'hex_to_rgb': BLUE_D,
            'rgb_to_hex': BLUE_D,
            'color_to_rgb': BLUE_D,
            'rgb_to_color': BLUE_D,
            'color_to_int_rgb': BLUE_D,
            'get_hex_l': BLUE_D,
            '#6cf': "#66CCFF",
            '#66CCFF': "#66CCFF",
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)