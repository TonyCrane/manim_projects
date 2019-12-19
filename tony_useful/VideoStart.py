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
        "subtitle_name" : "",
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
        # subtitle = TextMobject(self.subtitle_name).scale(0.8).set_color(BLUE)
        # subtitle.next_to(title, DOWN, buff=0.75)
        self.play(
            FadeInFromDown(svg_file),
            Write(author)
        )
        self.play(
            Write(title),
            # Write(subtitle),
        )
        self.wait()
        self.play(
            LaggedStart(FadeOutAndShiftDown(author)),
            FadeOut(title),
            # FadeOut(subtitle),
            run_time = 0.5,
        )