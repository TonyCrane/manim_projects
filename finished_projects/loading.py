from manimlib.imports import *


class SingleAnim(Animation):
    CONFIG = {
        "run_time": 6,
        "offset": 0,
        "rate_func": linear,
    }
    def interpolate_mobject(self, alpha):
        now_time = alpha * self.run_time
        off = self.offset
        self.mobject.become(self.starting_mobject)
        if now_time <= off:
            self.mobject.set_opacity(0)
        elif off < now_time <= off + 1:
            self.mobject.set_opacity(1)
            now_alpha = (self.run_time * alpha - off) / 1
            self.mobject.rotate(
                rush_from(now_alpha) * 180*DEGREES,
                axis=IN,
                about_point=ORIGIN,
            )
        elif off + 1 < now_time <= off + 2.5:
            self.mobject.set_opacity(1)
            now_alpha = (self.run_time * alpha - off - 1) / 1.5
            self.mobject.rotate(
                rush_into(now_alpha) * 180*DEGREES + 180*DEGREES,
                axis=IN,
                about_point=ORIGIN,
            )
        elif off + 2.5 < now_time <= off + 3.5:
            self.mobject.set_opacity(1)
            now_alpha = (self.run_time * alpha - off - 2.5) / 1
            self.mobject.rotate(
                rush_from(now_alpha) * 180*DEGREES,
                axis=IN,
                about_point=ORIGIN,
            )
        elif off + 3.5 < now_time <= off + 5:
            self.mobject.set_opacity(1)
            now_alpha = (self.run_time * alpha - off - 3.5) / 1.5
            self.mobject.rotate(
                rush_into(now_alpha) * 180*DEGREES + 180*DEGREES,
                axis=IN,
                about_point=ORIGIN,
            )
        else:
            self.mobject.set_opacity(0)


class OffScene(Animation):
    def interpolate_mobject(self, alpha):
        if alpha != 1:
            self.mobject.set_opacity(0)
        else:
            self.mobject.set_opacity(1)


class Loading(Scene):
    def construct(self):
        dots = [
            Dot(color=WHITE, radius=0.25).move_to(DOWN*1.5)
            for _ in range(5)
        ]
        total_anims = []
        for i, offset in zip(range(5), [0, 0.26, 0.51, 0.75, 0.99]):
            anims = Succession(
                OffScene(dots[i], run_time=offset),
                Rotating(dots[i], axis=IN, radians=160*DEGREES, about_point=ORIGIN, run_time=0.5, rate_func=rush_from),
                Rotating(dots[i], axis=IN, radians= 20*DEGREES, about_point=ORIGIN, run_time=2.0, rate_func=linear),
                Rotating(dots[i], axis=IN, radians=180*DEGREES, about_point=ORIGIN, run_time=1.0, rate_func=rush_into),
                Rotating(dots[i], axis=IN, radians=160*DEGREES, about_point=ORIGIN, run_time=0.5, rate_func=rush_from),
                Rotating(dots[i], axis=IN, radians= 20*DEGREES, about_point=ORIGIN, run_time=2.0, rate_func=linear),
                Rotating(dots[i], axis=IN, radians=180*DEGREES, about_point=ORIGIN, run_time=1.0, rate_func=rush_into),
                OffScene(dots[i], run_time=1-offset),
            )
            # print(*turn_animation_into_updater(anims))
            # self.add(turn_animation_into_updater(anims))
            total_anims.append(anims)
        self.add(*dots)
        self.wait()
        # print(total_anims)
        self.play(*total_anims)
        self.wait()


class Loading2(Scene):
    def construct(self):
        dots = [
            Dot(color=WHITE, radius=0.25).move_to(DOWN*1)
            for _ in range(5)
        ]
        self.add(dots[0])
        self.wait()
        self.play(
            SingleAnim(dots[0], offset=0),
            SingleAnim(dots[1], offset=0.26),
            SingleAnim(dots[2], offset=0.51),
            SingleAnim(dots[3], offset=0.74),
            SingleAnim(dots[4], offset=0.97),
        )
        self.wait(4/15)
        self.play(
            SingleAnim(dots[0], offset=0),
            SingleAnim(dots[1], offset=0.26),
            SingleAnim(dots[2], offset=0.51),
            SingleAnim(dots[3], offset=0.74),
            SingleAnim(dots[4], offset=0.97),
        )
        self.wait(4/15)
        self.play(
            SingleAnim(dots[0], offset=0),
            SingleAnim(dots[1], offset=0.26),
            SingleAnim(dots[2], offset=0.51),
            SingleAnim(dots[3], offset=0.74),
            SingleAnim(dots[4], offset=0.97),
        )
        self.wait()
