from manimlib.imports import *

class Code(Text):
    CONFIG = {
        'font'         : 'Monaco for Powerline',
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

class LinedCode(Text):
    CONFIG = {
        'font'         : 'Consolas',
        'size'         : 0.5,
        'color'        : WHITE,
        'stroke_color' : WHITE,
        'stroke_weight': 0,
        'ln_color'     : GRAY,
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
            'int' : PURPLE,
            '(' : BLUE,
            ')' : BLUE,
            '{' : BLUE,
            '}' : BLUE,
            'return' : BLUE,
            '0' : ORANGE,
            'main' : '#214FB7',
            'printf' : '#214FB7',
            '\"' : BLUE,
            'Hello World' : GREEN,
            '\\n' : BLUE,
        }
    }

    def __init__(self, *text, **config):
        digest_config(self, config)
        res_text = ''
        i = 1
        for each_text in text:
            res_text += str(i) + '  ' + each_text + '\n'
            self.t2c['{}  '.format(i)] = self.ln_color
            i = i + 1
        super(LinedCode, self).__init__(res_text, **config)
        self.set_stroke(self.stroke_color, self.stroke_weight)