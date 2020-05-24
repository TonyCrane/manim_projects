from manimlib.animation.animation import Animation
from manimlib.animation.composition import AnimationGroup
from manimlib.animation.fading import FadeOut
from manimlib.animation.creation import ShowCreation
from manimlib.animation.creation import Write
from manimlib.animation.transform import ApplyMethod
from manimlib.animation.transform import MoveToTarget
from manimlib.constants import *
from manim_projects.OmegaCreature.omega_class import OmegaCreatureClass
from manimlib.mobject.mobject import Group
from manimlib.mobject.svg.drawings import SpeechBubble
from manimlib.utils.config_ops import digest_config
from manimlib.utils.rate_functions import squish_rate_func
from manimlib.utils.rate_functions import there_and_back


class Blink(ApplyMethod):
    CONFIG = {
        "rate_func": squish_rate_func(there_and_back)
    }

    def __init__(self, omega_creature, **kwargs):
        ApplyMethod.__init__(self, omega_creature.blink, **kwargs)


class OmegaCreatureBubbleIntroduction(AnimationGroup):
    CONFIG = {
        "target_mode": "speaking",
        "bubble_class": SpeechBubble,
        "change_mode_kwargs": {},
        "bubble_creation_class": ShowCreation,
        "bubble_creation_kwargs": {},
        "bubble_kwargs": {},
        "content_introduction_class": Write,
        "content_introduction_kwargs": {},
        "look_at_arg": None,
    }

    def __init__(self, omega_creature, *content, **kwargs):
        digest_config(self, kwargs)
        bubble = omega_creature.get_bubble(
            *content,
            bubble_class=self.bubble_class,
            **self.bubble_kwargs
        )
        Group(bubble, bubble.content).shift_onto_screen()

        omega_creature.generate_target()
        omega_creature.target.change_mode(self.target_mode)
        if self.look_at_arg is not None:
            omega_creature.target.look_at(self.look_at_arg)

        change_mode = MoveToTarget(omega_creature, **self.change_mode_kwargs)
        bubble_creation = self.bubble_creation_class(
            bubble, **self.bubble_creation_kwargs
        )
        content_introduction = self.content_introduction_class(
            bubble.content, **self.content_introduction_kwargs
        )
        AnimationGroup.__init__(
            self, change_mode, bubble_creation, content_introduction,
            **kwargs
        )


class OmegaCreatureSays(OmegaCreatureBubbleIntroduction):
    CONFIG = {
        "target_mode": "speaking",
        "bubble_class": SpeechBubble,
    }


class RemoveOmegaCreatureBubble(AnimationGroup):
    CONFIG = {
        "target_mode": "plain",
        "look_at_arg": None,
        "remover": True,
    }

    def __init__(self, omega_creature, **kwargs):
        assert hasattr(omega_creature, "bubble")
        digest_config(self, kwargs, locals())

        omega_creature.generate_target()
        omega_creature.target.change_mode(self.target_mode)
        if self.look_at_arg is not None:
            omega_creature.target.look_at(self.look_at_arg)

        AnimationGroup.__init__(
            self,
            MoveToTarget(omega_creature),
            FadeOut(omega_creature.bubble),
            FadeOut(omega_creature.bubble.content),
        )

    def clean_up_from_scene(self, scene=None):
        AnimationGroup.clean_up_from_scene(self, scene)
        self.omega_creature.bubble = None
        if scene is not None:
            scene.add(self.omega_creature)


class FlashThroughClass(Animation):
    CONFIG = {
        "highlight_color": GREEN,
    }

    def __init__(self, mobject, mode="linear", **kwargs):
        if not isinstance(mobject, OmegaCreatureClass):
            raise Exception("FlashThroughClass mobject must be a OmegaCreatureClass")
        digest_config(self, kwargs)
        self.indices = list(range(mobject.height * mobject.width))
        if mode == "random":
            np.random.shuffle(self.indices)
        Animation.__init__(self, mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        index = int(np.floor(alpha * self.mobject.height * self.mobject.width))
        for omega in self.mobject:
            omega.set_color(BLUE_E)
        if index < self.mobject.height * self.mobject.width:
            self.mobject[self.indices[index]].set_color(self.highlight_color)
