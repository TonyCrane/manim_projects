from manimlib.imports import *

class Code(Text):
    CONFIG = {
        'font'         : 'Consolas',
        'size'         : 0.5,
        'color'        : WHITE,
        'stroke_color' : WHITE,
        'stroke_weight': 0,
        't2c' : {
            '#include <' : BLUE,
            '>' : BLUE,
            'std' : YELLOW,
            'bits/stdc++.h' : GREEN,
            'using' : ORANGE,
            'namespace' : PURPLE,
            ';' : BLUE,
            'for' : BLUE,
            'if' : BLUE,
        }
    }

    def __init__(self, *text, **config):
        res_text = ''
        for each_text in text:
            res_text += each_text + '\n'
        super(Code, self).__init__(res_text, **config)
        self.set_stroke(self.stroke_color, self.stroke_weight)
        