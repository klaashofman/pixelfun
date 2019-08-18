import math
import pyxel


class App:
    def __init__(self):
        self.rotation = 0
        self.speed = 2;
        pyxel.init(160, 120, caption="My Movement")
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_UP):
            self.speed += 10
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.speed -= 10

        self.rotation += self.speed;

    def draw_bearing(self):
        # from degrees to radians
        theta = self.rotation * math.pi / 180
        len = 30
        dx = len * math.cos(theta)
        dy = len * math.sin(theta)
        pyxel.line(pyxel.width / 2, pyxel.height / 2, pyxel.width / 2 + dx, pyxel.height / 2 + dy, 4)

    def vector_transform(self, x0, y0, x1, y1, c = 6):
        # 2-dimensional vector rotation (https://en.wikipedia.org/wiki/Rotation_(mathematics))
        # x' = x cos (theta) - y sin (theta)
        # y' = x sin (theta) + y cos (theta)
        theta = self.rotation * math.pi / 180

        # start of the line
        dx0 = x0 * math.cos(theta) - y0 * math.sin(theta)
        dy0 = x0 * math.sin(theta) + y0 * math.cos(theta)

        # end of the line
        dx1 = x1 * math.cos(theta) - y1 * math.sin(theta)
        dy1 = x1 * math.sin(theta) + y1 * math.cos(theta)

        # put it in the middle of the screen
        # don't put the offset (width or height) in the equation above
        # as x and y are vectors
        pyxel.line(dx0 + pyxel.width / 2, dy0 + pyxel.height / 2, dx1 + pyxel.width / 2, dy1 + pyxel.height / 2, col=c)

    def draw(self):
        pyxel.cls(0)
        self.draw_bearing()

        # draw a rotating box
        self.vector_transform(x0 = 0, y0 = 0, x1 = 10, y1 = 0)
        self.vector_transform(x0 = 0, y0 = 0, x1 = 0, y1 = 10)
        self.vector_transform(x0 = 10, y0 = 0, x1 = 10, y1 = 10)
        self.vector_transform(x0 = 0, y0 = 10, x1 = 10, y1 = 10)

        # draw spaceship
        self.vector_transform(x0 = -10, y0 =0, x1 = 10, y1 = 0, c = 1)
        self.vector_transform(x0 = -10, y0 =0, x1 = 0, y1 = 30, c = 1)
        self.vector_transform(x0 = 10, y0 = 0, x1 = 0, y1 = 30, c = 1)

App()
