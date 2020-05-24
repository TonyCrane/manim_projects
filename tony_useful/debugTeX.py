from manimlib.imports import *
import itertools

def debugTeX(self, texm, scale=0.6):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="Consolas").scale(scale).set_color(PURPLE)
        tex_id.move_to(j)
        self.add(tex_id)