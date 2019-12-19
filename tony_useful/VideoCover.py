'''
  > File Name        : VideoCover.py
  > Author           : Tony
  > Created Time     : 2019/05/25 9:49:37
'''

from big_ol_pile_of_manim_imports import *

class VideoCover(Scene):
    CONFIG = {
        "Author"        : "@鹤翔万里",
        "author_colors" : [BLUE, YELLOW, ORANGE, RED],
        "en_title_name" : "test",
        "title_name"    : "测试",
        "subtitle_name" : "",
    }

    def construct(self):
        author = TextMobject(self.Author).set_color(self.author_colors).scale(1).to_corner(DOWN+RIGHT)
        en_title = TextMobject(self.en_title_name).scale(3).to_corner(UP+np.array((0., 2., 0.)))
        title = TextMobject(self.title_name).scale(1.9).set_color(YELLOW).next_to(en_title, DOWN, buff=0.6)
        subtitle = TextMobject(self.subtitle_name).scale(1.2).next_to(title, DOWN).set_color(BLUE)
        self.add(author, en_title, title, subtitle)