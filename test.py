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

    def construct(self):
        self.setup_axes(animate=True)

        '''ef parametric(alpha):
            t = interpolate(-3.5, 10, alpha)
            x = self.y_func(t)
            y = self.x_func(t)

            if not np.isfinite(y):
                y = 100

            if not np.isfinite(x):
                x = 100
            
            return self.coords_to_point(x, y)'''

        '''func_graph = ParametricFunction(
            parametric,
            color=RED,
        )'''

        top_func_graph = self.get_graph(self.top_func, color=BLUE)
        bot_func_graph = self.get_graph(self.bot_func, color=BLUE)

        self.play(ShowCreation(top_func_graph), ShowCreation(bot_func_graph))
        self.wait(5)

    def top_func(self, x):
        return (x ** 3 + -4.42 * x + 3) ** (.5)

    def bot_func(self, x):
        return -(x ** 3 + -4.42 * x + 3) ** (.5)

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

