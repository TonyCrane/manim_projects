##############################################################
#  > File Name        : /home/tony/GL.py
#  > Author           : Tony
#  > Created Time     : 2019年01月25日 星期五 17时31分08秒
##############################################################

from big_ol_pile_of_manim_imports import *

class GaussLaw(Scene):
	def construct(self):
		example_text = TextMobject(
			"Gauss's Law 高斯定理",
			tex_to_color_map={"Law": RED}
		)
		example_tex = TexMobject(
			"\\def\\ooint{{\\bigcirc}\\kern-12.5pt{\\int}\\kern-6.5pt{\\int}}"
			"\\ooint_S{E\\cdot dS} = {1\\over{\\epsilon_0}}\\times{{\\int}\\kern-6.5pt{\\int}\\kern-6.5pt{\\int}_V{\\rho \\cdot dV}}",
		)
		group = VGroup(example_text, example_tex)
		group.arrange_submobjects(DOWN)
		group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

		self.play(Write(example_text))
		self.play(Write(example_tex))
		self.wait()
