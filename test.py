from big_ol_pile_of_manim_imports import *
from colour import *

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

    def roots(a,b,c,d):
        return []

    def construct(self):
        self.setup_axes(animate=True)

        a = 1
        b = 3
        c = 1
        d = 1

        roots = self.roots(a,b,c,d)

        top_func_graph_part1 = self.get_graph(
            self.top_func(a,b,c), color=BLUE,
            x_min = roots[0], # Domain 1
            x_max = roots[1]
        )
        bot_func_graph_part1 = self.get_graph(
            self.bot_func(a,b,c), color=BLUE,
            x_min = roots[0], # Domain 1
            x_max = roots[1]
        )

        top_func_graph_part2 = self.get_graph(
            self.top_func(a,b,c), color=BLUE,
            x_min = roots[2]
        )
        bot_func_graph_part2 = self.get_graph(
            self.bot_func(a,b,c), color=BLUE,
            x_min = roots[2]
        )

        self.play(
            ShowCreation(top_func_graph_part1),
            ShowCreation(bot_func_graph_part1)
        )
        self.play(
            ShowCreation(top_func_graph_part2),
            ShowCreation(bot_func_graph_part2)
        )
        self.wait(5)

    def top_func(self, a,b,c,d):
        return lambda x : (a * x ** 3 + b * x ** 2, c * x + d) ** (.5)

    def bot_func(self, a,b,c,d):
        return lambda x : -(a * x ** 3 + b * x ** 2, c * x + d) ** (.5)

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

