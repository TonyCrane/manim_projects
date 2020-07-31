from manimlib.imports import *

class ArticleCover(Scene):
    def construct(self):
        title = VGroup(
            Text("如何使用", font="Source Han Serif CN").scale(1),
            TextMobject("manim").scale(2.5),
            Text("制作一期视频", font="Source Han Serif CN").scale(1)
        )
        title[0].set_color(BLUE_D)
        title[2][:4].set_color(BLUE_D)
        title[2][4:].set_color(RED_D)
        title[1][0][0].set_color(BLUE)
        title[1][0][1:].set_color(YELLOW)
        title[1].next_to(title[0], RIGHT, aligned_edge=DOWN)
        title[2].next_to(title[1], DOWN, aligned_edge=RIGHT)
        title.move_to(RIGHT * 2 + UP * 0.5)
        back = VGroup(
            Text("如何使用", font="Source Han Serif CN").set_stroke(width=8, opacity=0.4),
            Text("制作一期视频", font="Source Han Serif CN").set_stroke(width=8, opacity=0.4)
        ).set_color(BLUE_B)
        back[1][4:].set_color(RED_B)
        back[0].move_to(title[0])
        back[1].move_to(title[2])
        title2 = Text("& 停 更 通 知", font="Source Han Serif CN").set_stroke(width=2).scale(0.5)
        title2.set_color(GOLD).scale(1.2).next_to(title[2], DOWN, aligned_edge=RIGHT)
        author = TextMobject("@鹤翔万里").scale(1).set_color([BLUE, YELLOW, ORANGE, RED]).next_to(title, DOWN, buff=1.2)
        author.next_to(title2, LEFT, buff=1)
        
        self.add(back, title, title2, author)
        self.wait()