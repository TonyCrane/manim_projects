'''
  > File Name        : VideoStart.py
  > Author           : Tony
  > Created Time     : 2019/03/13 14:17:47
'''

from manimlib.imports import *

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
        ).scale(1.5)
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
            LaggedStart(FadeOutAndShiftDown(author)),
            FadeOut(title),
            run_time = 0.5,
        )