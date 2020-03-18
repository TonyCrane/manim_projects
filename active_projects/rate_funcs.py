from manimlib.imports import *

class Linear(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
        "rate_func": linear,
    }
    def construct(self):
        grid = NumberPlane().scale(3)
        text_0 = TexMobject("0", color=BLACK).scale(0.6).next_to(ORIGIN, DL, buff=0.2)
        text_1 = TexMobject("1", color=BLACK).scale(0.6).next_to(grid.c2p(1, 0), DOWN, buff=0.2)
        tex_1  = TexMobject("1", color=BLACK).scale(0.6).next_to(grid.c2p(0, 1), LEFT, buff=0.2)
        func = ParametricFunction(
            lambda t: [t, self.rate_func(t), 0],
            t_min=0, t_max=1, color=RED
        ).scale(3, about_point=ORIGIN)
        text = Text(str(self.rate_func.__name__), font="Consolas", size=0.5, color=BLACK)
        text.move_to(grid.c2p(0.5, -0.3))
        self.add(grid, func, text, text_0, text_1, tex_1)

class Smooth(Linear):
    CONFIG = {
        "rate_func": smooth,
    }

class RushInto(Linear):
    CONFIG = {
        "rate_func": rush_into,
    }

class RushFrom(Linear):
    CONFIG = {
        "rate_func": rush_from,
    }

class SlowInto(Linear):
    CONFIG = {
        "rate_func": slow_into,
    }

class DoubleSmooth(Linear):
    CONFIG = {
        "rate_func": double_smooth,
    }

class ThereAndBack(Linear):
    CONFIG = {
        "rate_func": there_and_back,
    }

class ThereAndBackWithPause(Linear):
    CONFIG = {
        "rate_func": there_and_back_with_pause,
    }

class RunningStart(Linear):
    CONFIG = {
        "rate_func": running_start,
    }

class NotQuiteThere(Linear):
    CONFIG = {
        "rate_func": not_quite_there(smooth),
    }

class Wiggle(Linear):
    CONFIG = {
        "rate_func": wiggle,
    }

class Lingering(Linear):
    CONFIG = {
        "rate_func": lingering,
    }

class ExponentialDecay(Linear):
    CONFIG = {
        "rate_func": exponential_decay,
    }