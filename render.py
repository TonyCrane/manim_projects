from manimlib.imports import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle(plot_depth=0).set_fill(RED, opacity=1)
        square = Square(plot_depth=-1, side_length=1.7).set_fill(BLUE, opacity=1)
        print("at the beginning...")
        print(f"circle plot_depth = {circle.plot_depth}")
        print(f"square plot_depth = {square.plot_depth}")
    
        self.play(FadeIn(circle), FadeIn(square))  # all good
        print("after FadeIn...")
        print(f"circle plot_depth = {circle.plot_depth}")
        print(f"square plot_depth = {square.plot_depth}")
        print(self.mobjects)
        self.play(ApplyMethod(circle.shift, UP))   # woops!
        print("after ApplyMethod...")
        print(f"circle plot_depth = {circle.plot_depth}")
        print(f"square plot_depth = {square.plot_depth}")
        print(self.mobjects)
        self.wait(1)
        print("after wait...")
        print(f"circle plot_depth = {circle.plot_depth}")
        print(f"square plot_depth = {square.plot_depth}")
