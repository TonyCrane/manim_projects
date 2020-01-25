from manimlib.imports import *

class SubTopic(Text):
    CONFIG = {
        'font'         : 'Source Han Serif CN',
        'size'         : 1,
        'to_scale'     : 0.6,
        'color'        : GOLD,
    }

    def __init__(self, text, **config):
        Text.__init__(self, text, **config)
        self.scale(self.to_scale)
        dot = Dot().set_color(self.color).next_to(self, LEFT)
        self.add(dot)
