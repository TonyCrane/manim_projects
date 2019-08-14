'''
  > File Name        : VisualQSort.py
  > Author           : Tony
  > Created Time     : 2019/06/05 20:09:35
'''

from big_ol_pile_of_manim_imports import *
from manim_projects.MyUsefulScene.VideoStart import VideoStart
from manim_projects.MyUsefulScene.VideoCover import VideoCover


class VideoTitle(VideoStart):
    CONFIG = {
        "title_name": "快速排序",
        "subtitle_name" : "可视化呈现(利用$Processing$)"
    }

class Cover(VideoCover):
    CONFIG = {
        "en_title_name" : "Quick Sort",
        "title_name"    : "快速排序",
        "subtitle_name" : "可视化呈现(利用$Processing$)"
    }

class Write200(Scene):
    def construct(self):
        text = TextMobject("$200$个数值").scale(5)
        self.play(Write(text))
        self.wait(4)
        self.play(FadeOutAndShift(text))

class Write500(Scene):
    def construct(self):
        text = TextMobject("$500$个数值").scale(5)
        self.play(Write(text))
        self.wait(4)
        self.play(FadeOutAndShift(text))

class Write1000(Scene):
    def construct(self):
        text = TextMobject("$1000$个数值").scale(5)
        self.play(Write(text))
        self.wait(4)
        self.play(FadeOutAndShift(text))

class End(Scene):
    def construct(self):
        text = TextMobject("本可视化使用","$Processing$","实现")
        text[1].set_color(RED)
        text2 = TextMobject("需要源码可以私信$up$主").next_to(text,DOWN).scale(0.8)
        self.play(Write(text))
        self.play(Write(text2))
        self.wait(4)
        self.play(
            FadeOut(text),
            FadeOut(text2)
        )
        self.wait(2)