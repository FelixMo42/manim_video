from big_ol_pile_of_manim_imports import *
from colour import *

def frange(x, y, jump):
  while jump * x < jump * y:
    yield x
    x += jump

class TitleScene(Scene):
    def construct(self):
        titleText = TextMobject("The Birch and Swinnerton-Dyer Conjecture")
        subText = TextMobject("by: Felix and Milo")
        subText.next_to(titleText, DOWN)
        subText.scale(0.75)

        self.add(titleText, subText)
        self.wait(2)

        self.play(FadeOut(subText))
        self.play(FadeOut(titleText))        

class TypesScene(Scene):
    def construct(self):
        types = [
            "P vs NP",
            "Probability",
            "Differential Equation",
            "F0 = F1 = 1, Fn = Fn-1 + Fn + 2"
        ]

        typesText = []
        typesFunc = []

        i = 0

        random.seed(12)

        for t in types:
            text = TextMobject(t)

            text.shift(
                random.randint(-5, 5) * UP + i * 3 * RIGHT
            )

            i += 1

            typesFunc.append(ApplyMethod(text.shift, 50 * LEFT, run_time=10.0, rate_func=linear))

            typesText.append(text)

        self.add(*typesText)
        self.play(*typesFunc)

        self.wait(1)

class WhatIsItAboutScene(Scene):
    def construct(self):
        # a2
        a2 = TextMobject("This is what mathmaticans do it for!")
        a2.scale(0.90)
        a2.set_color(YELLOW)

        # a1
        a1 = TextMobject("here it is:")
        a1.scale(0.90)
        a1.set_color(YELLOW)
        a1.next_to(a2.get_edge_center(UP + LEFT), UP + RIGHT)

        #auth
        auth = TextMobject("- Probably Euler")
        auth.scale(0.75)
        auth.next_to(a2.get_corner(DOWN+RIGHT),DOWN)

        #q4
        q4 = TextMobject("Yang–Mills existence and mass gap")
        q4.shift(3 * DOWN)

        #q3
        q3 = TextMobject("Riemann hypothesis")
        q3.shift(1 * UP)

        #q1
        q1 = TextMobject("P versus NP")
        q1.shift(3 * UP)

        #q2
        q2 = TextMobject("Hodge conjecture")
        q2.shift(2 * UP)

        #q5
        q5 = TextMobject("Navier–Stokes existence and smoothness")
        q5.shift(1 * DOWN)

        #q6
        q6 = TextMobject("Poincare conjecture")
        q6.shift(2 * DOWN)

        #q7
        q7 = TextMobject("Birch and Swinnerton-Dyer Conjecture")

        quote = TextMobject("$$ \\textrm{\"The Clay Mathmatics Institute} $$ $$ \\textrm{will further the beauty, and power} $$ $$ \\textrm{and universal of mathmatical thaught.\"} $$")
        quote.to_edge(UP)
        quote.set_color(YELLOW)

        self.play(Write(a1))
        self.wait(.5)
        self.play(Write(a2))
        self.wait(1)
        self.play(Write(auth))
        self.wait(3)

        self.play(
            FadeOut(a1),
            Transform(a2, q7),
            FadeOut(auth)
        )

        self.wait(5)

        self.play(
            Write(quote)
        )

        self.wait(2)

        self.play(
            FadeOut(quote)
        )

        self.wait(2)

        self.play(
            Write(q6),
            Write(q5),
            Write(q4),
            Write(q3),
            Write(q2),
            Write(q1)
        )

        self.wait(5)

        self.play(
            FadeToColor(q6, YELLOW)
        )

        self.wait(5)

        self.play(
            FadeOut(q6),
            FadeOut(q5),
            FadeOut(q4),
            FadeOut(q3),
            FadeOut(q2),
            FadeOut(q1),
            FadeOut(a2)
        )

class FunctionScene(Scene):
    def construct(self):
        nums = TextMobject("x y")
        equation = TextMobject("$$ 6x^{2} + 9y^{3} = 8x + 12y^{5} $$")
        xab = TextMobject("$$ x = \\frac{a}{b} $$")
        xab.shift(DOWN + LEFT)
        yab = TextMobject("$$ y = \\frac{c}{d} $$")
        yab.shift(DOWN + RIGHT)
        whole = TextMobject("a, b, c and d are whole numbers")
        whole.shift(DOWN * 2)
        arrow = ArrowTip()
        arrow.rotate_about_origin(TAU / 4)
        arrow.shift(UP * 2)

        self.play(
            Write(nums)
        )

        self.wait(2)

        self.play(
            Transform(nums, equation)
        )

        self.wait(2)

        self.play(
            Write(xab),
            Write(yab)
        )

        self.wait(2)

        self.play(
            Write(whole)
        )

        self.wait(2)

        self.play(
            ApplyMethod(nums.shift, UP * 3),
            FadeOutAndShiftDown(xab),
            FadeOutAndShiftDown(yab),
            FadeOutAndShiftDown(whole)
        )

        self.wait(2)

        xnn = TextMobject("$$ x = \\frac{6}{8} $$")
        xnn.shift(UP + LEFT)
        ynn = TextMobject("$$ y = \\frac{9}{12} $$")
        ynn.shift(UP + RIGHT)

        self.play(
            FadeIn(arrow),
            FadeIn(xnn),
            FadeIn(ynn)
        )

        self.wait(2)

        sol = TextMobject("$$ 6\\left(\\frac{6}{8}\\right)^{2} + 9\\left(\\frac{9}{12}\\right)^{3} = 8\\left(\\frac{9}{12}\\right) + 12\\left(\\frac{9}{12}\\right)^{5} $$")
        sol.shift(DOWN * 1)

        arrow2 = ArrowTip()
        arrow2.rotate_about_origin(TAU / 4)
        #arrow2.shift(DOWN)

        arrow3 = ArrowTip()
        arrow3.rotate_about_origin(TAU / 4)
        arrow3.shift(DOWN * 2)

        self.play(
            FadeIn(sol),
            FadeIn(arrow2)
        )

        self.wait(2)

        nums = TextMobject("14.46... = 14.46... ")
        nums.shift(DOWN * 3)

        self.play(
            FadeIn(nums),
            FadeIn(arrow3)
        )

        self.wait(2)

        self.play(
            FadeOut(nums),
            FadeOut(xnn),
            FadeOut(ynn),
            FadeOut(arrow),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(sol)
        )

class SolScene(Scene):
    def construct(self):
        p1 = TextMobject("$$ 6x^{1} = 9y^{1} + 19 $$")
        p1.shift(UP * 2)

        p2 = TextMobject("$$ 5x^{2} + 6y^{2} + 12x = 2y + 3 $$")

        p3 = TextMobject("$$ y^{2} = 9x^{3} + 43x + 2 $$")
        p3.shift(DOWN * 2)


        self.play(
            Write(p1)
        )

        self.wait(2)

        self.play(
            FadeToColor(p1, GREEN)
        )

        self.wait(2)

        self.play(
            Write(p2)
        )

        self.wait(2)

        self.play(
            FadeToColor(p2, GREEN)
        )

        self.wait(2)

        self.play(
            Write(p3)
        )

        self.wait(2)

        self.play(
            FadeToColor(p3, RED)
        )

        self.wait(2)

        bs = TextMobject("Birch and Swinnerton-Dyer Conjectrue!")

        self.play(
            FadeOut(p1),
            FadeOut(p2),
            FadeOut(p3),
            Write(bs)
        )

        func = TextMobject("$$ y^{2} = x^{3} + ax + b $$")

        self.play(
            Transform(bs, func)
        )

        self.wait(2)

class PlotFunction(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -10,
        "y_max" : 10,
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
    }

    def roots(self,a,b,c,d):
        return [n for n in np.roots([a,b,c,d]) if np.isreal([n])[0]]

    def drawFuncs(self, a,b,c,d, intit=False):
        roots = self.roots(a,b,c,d)

        if len(roots) == 1 and a < 0:
            top_graph = self.get_graph(
                self.top_func(a,b,c,d), color=BLUE,
                x_max = roots[0]
            )
            bot_graph = self.get_graph(
                self.bot_func(a,b,c,d), color=BLUE,
                x_max = roots[0]
            )
            self.add(top_graph, bot_graph)

            def clear():
                top_graph.clear_points()
                bot_graph.clear_points()

            return clear

        if len(roots) == 1 and a > 0:
            top_graph = self.get_graph(
                self.top_func(a,b,c,d), color=BLUE,
                x_min = roots[0]
            )
            bot_graph = self.get_graph(
                self.bot_func(a,b,c,d), color=BLUE,
                x_min = roots[0]
            )
            self.add(top_graph, bot_graph)

            def clear():
                top_graph.clear_points()
                bot_graph.clear_points()

            return clear

        top_func_graph_part1 = self.get_graph(
            self.top_func(a,b,c,d), color=BLUE,
            x_min = roots[1],
            x_max = roots[2]
        )
        bot_func_graph_part1 = self.get_graph(
            self.bot_func(a,b,c,d), color=BLUE,
            x_min = roots[1],
            x_max = roots[2]
        )

        if not intit:
            self.add(
                top_func_graph_part1,
                bot_func_graph_part1
            )

        top_func_graph_part2 = None
        bot_func_graph_part2 = None

        if a > 0 and not isinstance(self.top_func(a,b,c,d)(10), complex):
            top_func_graph_part2 = self.get_graph(
                self.top_func(a,b,c,d), color=BLUE,
                x_min = roots[0]
            )
            bot_func_graph_part2 = self.get_graph(
                self.bot_func(a,b,c,d), color=BLUE,
                x_min = roots[0]
            )

            if not intit:
                self.add(
                    top_func_graph_part2,
                    bot_func_graph_part2
                )

        if a < 0 and not isinstance(self.top_func(a,b,c,d)(-10), complex):
            top_func_graph_part2 = self.get_graph(
                self.top_func(a,b,c,d), color=BLUE,
                x_max = roots[0]
            )
            bot_func_graph_part2 = self.get_graph(
                self.bot_func(a,b,c,d), color=BLUE,
                x_max = roots[0]
            )

            if not intit:
                self.add(
                    top_func_graph_part2,
                    bot_func_graph_part2
                )

        '''if intit:
            self.play(
                ShowCreation(top_func_graph_part1),
                ShowCreation(bot_func_graph_part1)
            )
            self.play(
                ShowCreation(top_func_graph_part2),
                ShowCreation(bot_func_graph_part2)
            )'''

        def clear():
            top_func_graph_part1.clear_points()
            bot_func_graph_part1.clear_points()
            if top_func_graph_part2 is not None:
                top_func_graph_part2.clear_points()
                bot_func_graph_part2.clear_points()

        return clear

    def construct(self):
        func = TextMobject("$$ y^{2} = x^{3} + ax + b $$")
        func.to_edge(UP)
        self.add(func)

        self.play(
            ApplyMethod(func.to_edge, DOWN)
        )

        self.setup_axes(animate=True)

        a = 1
        b = -3
        c = 1
        d = 1

        clear = self.drawFuncs(a,b,c,d, False)

        for a in frange(b, 3, .2):
            if a != 0:
                self.wait(.1)

                clear()
                clear = self.drawFuncs(a,b,c,d)

        self.wait(5)

    def top_func(self, a,b,c,d):
        return lambda x : (a * x ** 3 + b * x ** 2 + c * x + d) ** (.5)

    def bot_func(self, a,b,c,d):
        return lambda x : -(a * x ** 3 + b * x ** 2 + c * x + d) ** (.5)

    def y_func(self, y):
        return y ** 2

    def x_func(self, x):
        return x ** 3 - x

class FinishScene(Scene):
    def construct(self):
        e1 = TextMobject("$$ \\prod_{p\\leq x} \\approx C\\log\\left(x\\right)^r $$")
        e1.shift(UP)
        
        e2 = TextMobject("$$ \\frac{L^{(r)}(E,1)}{r!}=\\frac{Sha(E)\\Omega_E R_E \\prod_{p|n}c_p}{(E_{Tor})^2} $$")
        e2.shift(DOWN)

        self.play(
            Write(e1),
            Write(e2)
        )

        self.wait(2)

        qus = TextMobject("Do we know where it will help in real life?")

        self.play(
            FadeOut(e1),
            FadeOut(e2),
            Write(qus)
        )

        self.wait(2)

        no = TextMobject("No")
        no.scale(2)

        self.play(Transform(qus, no))

        self.wait(2)

        heart = TextMobject("$$ \\ensuremath \\heartsuit $$")
        heart.scale(10)
        heart.set_color(PINK)

        self.play(Transform(qus, heart))

        dols = TextMobject("x \\$1,000,000")
        dols.scale(2)
        dols.shift(3 * DOWN)

        self.play(
            FadeInFrom(dols, RIGHT)
        )

        self.wait(2)

        self.play(
            FadeOut(qus),
            FadeOut(dols)
        )