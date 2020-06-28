from manimlib.imports import *
from manim_sandbox.utils.imports import *


class BFMemory(VGroup):
    CONFIG = {
        "num_cells": 5,
        "cell_config": {
            "stroke_color": GRAY,
            "fill_opacity": 0,
            "buff": 0.2
        },
    }
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pointer = 0
        self.values = [0 for i in range(self.num_cells)]
        self.get_single_cell()
        self.get_cells()
        self.numbers = self.get_numbers()
        self.add(self.numbers)
        self.add_updater(lambda m: m.update_numbers())

    def get_single_cell(self):
        max_num = Integer(
            255,
            edge_to_fix=ORIGIN,
        )
        self.basic_cell = SurroundingRectangle(
            max_num,
            **self.cell_config,
        )
    
    def get_cells(self):
        self.cells = VGroup()
        for _ in range(self.num_cells):
            self.cells.add(self.basic_cell.copy())
        self.cells.arrange(RIGHT, buff=0.25)
        self.add(self.cells)
    
    def get_numbers(self):
        basic_number = Integer(
            0,
            edge_to_fix=ORIGIN,
        ).set_stroke(color=WHITE, width=1.5, background=True)
        numbers = VGroup()
        for i in range(self.num_cells):
            numbers.add(basic_number.copy().set_value(self.values[i]).move_to(self[0][i]))
        return numbers
            
    def update_numbers(self):
        self[1].become(self.get_numbers())

    def increment(self, pos):
        self.values[pos] += 1
        if self.values[pos] == 256:
            self.values[pos] = 0
    
    def decrement(self, pos):
        self.values[pos] -= 1
        if self.values[pos] == -1:
            self.values[pos] = 255
    
    def copy(self):
        return self.deepcopy()
    
    def get_char(self, pos):
        text = TextMobject(
            chr(self.values[pos]), 
            color=RED, 
            background_stroke_color=RED, 
            background_stroke_width=2
        ).scale(1.2)
        text.next_to(self.cells[pos], UP, buff=0.1)
        return text


class BFPointer(VGroup):
    CONFIG = {
        "tick_config": {
            "fill_opacity": 1,
            "stroke_width": 0,
        },
        "pointer_color": GOLD,
        "read_color": RED,
    }

    def __init__(self, cells, **kwargs):
        super().__init__(**kwargs)
        self.cells = cells
        self.vect = cells[0][1].get_center() - cells[0][0].get_center()
        self.get_rect()
        self.get_tick()
    
    def get_rect(self):
        self.rect = self.cells[0][0].copy().set_color(self.pointer_color)
        self.add(self.rect)
    
    def get_tick(self):
        self.tick = Triangle(**self.tick_config).scale(0.2)
        self.tick.add_updater(lambda m: m.next_to(self.rect, DOWN, buff=0))
        self.tick.add_updater(lambda m: m.match_color(self.rect))
        self.add(self.tick)

    def move(self, delta):
        self.rect.shift(self.vect * delta)
        return self
    
    def move_left(self):
        return self.move(-1)
    
    def move_right(self):
        return self.move(1)
    
    def read_number(self):
        self.rect.set_color(self.read_color)
        return self

    def finish_reading(self):
        self.rect.set_color(self.pointer_color)
        return self
    
    def copy(self):
        return self.deepcopy()


class BFOutput(VGroup):
    CONFIG = {
        "rect_config": {
            "stroke_width": 1.5,
            "stroke_color": WHITE,
            "fill_opacity": 0,
            "stroke_opacity": 1,
            "corner_radius": 0.2
        },
        "buff": 0.15,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_rect()
        self.init_chars()
    
    def get_rect(self):
        output = TextMobject(
            "A" * 15,
        )
        self.rect = RoundedRectangle(
            width=output.get_width()+2*self.buff,
            height=output.get_height()+2*self.buff,
            **self.rect_config
        )
        self.add(self.rect)
    
    def init_chars(self):
        self.chars = VGroup()
        self.add(self.chars)
    
    def append_char(self, text):
        text.generate_target()
        text.target.set_color(WHITE).set_stroke(color=WHITE, background=True)
        text.target.scale(5/6)
        if self.chars:
            text.target.next_to(self.chars, RIGHT, buff=0.06, aligned_edge=DOWN)
        else:
            text.target.next_to(self.rect.get_left(), RIGHT, buff=self.buff)
        self.chars.add(text)
        return MoveToTarget(text)
    
    def copy(self):
        return self.deepcopy()


class BFCode(Text):
    CONFIG = {
        "code": "",
        "font": "Consolas",
        "size": 0.58,
        "color": WHITE,
        "t2c": {
            "[": RED,
            "]": RED,
            "<": BLUE,
            ">": BLUE,
            ".": GREEN,
        }
    }

    def __init__(self, code=None, **kwargs):
        digest_config(self, kwargs)
        self.code = code if code else self.code
        Text.__init__(
            self,
            self.code,
            **kwargs
        )
        for each in self:
            if isinstance(each, Dot):
                self.remove(each)
        self.text = ''.join(filter(lambda x: x in ['.', '[', ']', '<', '>', '+', '-'], self.code))
    
    def copy(self):
        return self.deepcopy()


class BFCodePointer(RoundedRectangle):
    CONFIG = {
        "stroke_width": 2,
        "stroke_color": YELLOW,
        "fill_opacity": 0,
        "stroke_opacity": 1,
        "corner_radius": 0.05,
        "text_config": {
            "font": "Consolas",
            "size": 0.58,
            "color": WHITE,
        },
    }

    def __init__(self, code, **kwargs):
        digest_config(self, kwargs)
        base_char = Text(
            "[", **self.text_config
        )
        RoundedRectangle.__init__(
            self,
            width=base_char.get_width()+0.1,
            height=base_char.get_height()+0.1,
            **kwargs
        )
        self.code = code
        self.move_to(self.code[0])
    
    def move(self, pos):
        if self.code.text[pos] == '.':
            self.move_to(self.code[pos], coor_mask=np.array([1, 0, 0]))
        else:
            self.move_to(self.code[pos])
        return self
    
    def copy(self):
        return self.deepcopy()


def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap

# do not support input (",")
class BFScene(Scene):
    CONFIG = {
        "code": "",
    }
    
    def setup(self):
        self.memory = BFMemory()
        self.code = BFCode(self.code)
        self.output = BFOutput()
        self.static = VGroup(self.memory, self.code, self.output).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        self.memorypointer = BFPointer(self.memory)
        self.codepointer = BFCodePointer(self.code)
        self.titles = VGroup(
            TextMobject("Cells", color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.5),
            TextMobject("Code", color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.5),
            TextMobject("Output", color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.5),
        )
        for i in range(3):
            self.titles[i].next_to(self.static[i], LEFT, buff=0.8)
        self.ptr = 0
        self.codeptr = 0
        self.bracemap = buildbracemap(self.code.text)

    def construct(self):
        self.add(self.static, self.titles)
        self.wait()
        self.play(FadeIn(self.codepointer), FadeIn(self.memorypointer))
        while self.codeptr < len(self.code.text):
            self.exe()
        self.wait()
        self.play(FadeOut(self.codepointer))
        self.wait(3)
    
    def exe(self):
        command = self.code.text[self.codeptr]
        if command == '>':
            self.play(self.memorypointer.move_right)
            self.ptr += 1
        elif command == '<':
            self.play(self.memorypointer.move_left)
            self.ptr -= 1
        elif command == '+':
            self.wait(0.1)
            self.memory.increment(self.ptr)
            self.wait(0.1)
            self.codeptr += 1
            self.play(self.codepointer.move, self.codeptr, run_time=0.2)
            return
        elif command == '-':
            self.wait(0.1)
            self.memory.decrement(self.ptr)
            self.wait(0.1)
            self.codeptr += 1
            self.play(self.codepointer.move, self.codeptr, run_time=0.2)
            return
        elif command == "[" and self.memory.values[self.ptr] == 0: 
            self.codeptr = self.bracemap[self.codeptr]
            self.play(self.codepointer.move, self.codeptr, run_time=0.2)
        elif command == "]" and self.memory.values[self.ptr] != 0: 
            self.codeptr = self.bracemap[self.codeptr]
            self.play(self.codepointer.move, self.codeptr, run_time=0.2)
        elif command == ".":
            text = self.memory.get_char(self.ptr)
            self.play(
                self.memorypointer.read_number, 
                FadeInFromDown(text), 
                run_time=0.5
            )
            self.wait(0.5)
            self.play(
                self.memorypointer.finish_reading, 
                self.output.append_char(text), 
                run_time=0.5
            )
            self.wait(0.5)
            
        self.codeptr += 1
        if self.codeptr == len(self.code.text):
            return
        self.play(self.codepointer.move, self.codeptr, run_time=0.2)
        


class BrainFuckExample(BFScene):
    CONFIG = {
        "code": """+++++ +++++ +
[
    > +++++ +
    < -
]
> .
++++ .""",
    }


class HelloWorld(BFScene):
    CONFIG = {
        "code": """+++++ +++++
[
    > +++++ ++
    > +++++ +++++
    > +++
    <<< -
]
> ++ . > + . +++++ ++ . .
+++ . < +++++ +++++ +++++ .
> . +++ . ----- - . ----- --- . > +++ .""",
    }