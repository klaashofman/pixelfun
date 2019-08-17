import math
import pyxel


class App:
    def __init__(self):
        self.rotation = 0
        self.speed = 10;
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

    def draw(self):
        pyxel.cls(0)
        #              (x2,y2)
        #            /
        #           /
        #   (x1,y1)/ alpha
        # from degrees to radians
        theta  = self.rotation * math.pi / 180
        len = 30
        dx = len * math.cos (theta)
        dy = len * math.sin (theta)
        pyxel.line(pyxel.width / 2, pyxel.height /2 , pyxel.width / 2 + dx, pyxel.height / 2 + dy, 4)

App()
