from manimlib.imports import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle(plot_depth=0).set_fill(RED, opacity=1)
        square = Square(plot_depth=-1, side_length=1.7).set_fill(BLUE, opacity=1)
    
        self.play(FadeIn(VGroup(circle, square)))  # all good
        self.play(ApplyMethod(circle.shift, UP))   # woops!
        self.wait(1)
