from manimlib.imports import *

def debugTeX(self, texm):
    for i, j in zip(range(100), texm):
        tex_id = Text(str(i), font="Consolas").scale(0.1).set_color(PURPLE)
        tex_id.move_to(j)
        self.add(tex_id)