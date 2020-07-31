'''
  > File Name        : FFTsp.py
  > Author           : Tony_Wong
  > Created Time     : 2020/02/12 11:31:49
'''

from manimlib.imports import *
from manim_projects.tony_useful.imports import *

class VideoTitle(VideoStart):
    CONFIG = {
        "title_name": "三次变两次优化 多项式乘法",
    }


class VideoCover(Scene):
    def construct(self):
        pass


class ThreeTimesFFT(Scene):
    def construct(self):
        title = Text("多项式乘法(卷积)", font="Source Han Sans CN", t2c={"多项式乘法": BLUE, "(卷积)": YELLOW})
        title.scale(0.6).to_corner(UL)
        self.wait()
        self.play(Write(title))
        self.wait()