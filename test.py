from big_ol_pile_of_manim_imports import *
from colour import *

def frange(x, y, jump):
  while jump * x < jump * y:
    yield x
    x += jump

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
        self.setup_axes(animate=False)

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

class Video(Scene):
    def construct(self):
        self.drawTitle()
    
    def drawTitle(self):
        titleText = TextMobject("The Birch and Swinnerton-Dyer Conjecture")
        subText = TextMobject("by: Felix and Milo")
        subText.next_to(titleText, DOWN)
        subText.scale(0.75)

        self.add(titleText, subText)
        self.wait(2)

        self.play(FadeOut(subText))
        self.play(FadeOut(titleText))

