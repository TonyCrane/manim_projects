from manimlib.imports import *
from manim_sandbox.utils.imports import *
from manim_projects.active_projects.brainfuck.brainfuck import *


class OpeningSceneHelloWorld(BFScene):
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
> . +++ . ----- - . ----- --- . > +++ ."""
    }
    
    def construct(self):
        # self.add(self.static, self.titles)
        raw = BFCode("""++++++++++[>+++++++>++++++++++>+++<<<-]
>++.>+.+++++++..+++.<+++++++++++++++.
>.+++.------.--------.>+++."""
        ).scale(2)
        self.wait()
        self.play(Write(raw))
        self.wait(3)
        self.play(ReplacementTransform(raw, self.code))
        self.wait()
        self.play(FadeIn(self.memory[1]), FadeIn(self.memory[0]), FadeIn(self.output), FadeIn(self.titles))
        self.play(FadeIn(self.codepointer), FadeIn(self.memorypointer))
        while self.codeptr < len(self.code.text):
            self.exe()
        self.wait()
        self.play(FadeOut(self.codepointer))
        self.wait(2)
        self.output[1].generate_target()
        self.output[1].target.scale(2.5).center()
        self.play(
            FadeOut(VGroup(self.titles, self.memorypointer, self.output[0])),
            FadeOut(self.memory[0]), FadeOut(self.memory[1]),
            FadeOut(self.code),
            MoveToTarget(self.output[1])
        )
        self.wait(2)
