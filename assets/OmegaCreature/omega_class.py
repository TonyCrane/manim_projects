from manimlib.constants import *
from manim_projects.OmegaCreature.omega_creature import OmegaCreature
from manimlib.mobject.types.vectorized_mobject import VGroup


class OmegaCreatureClass(VGroup):
    CONFIG = {
        "width": 3,
        "height": 2
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        for i in range(self.width):
            for j in range(self.height):
                omega = OmegaCreature().scale(0.3)
                omega.move_to(i * DOWN + j * RIGHT)
                self.add(omega)
