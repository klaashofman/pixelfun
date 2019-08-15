import pyxel


class App:
    def __init__(self):
        self.x = 0
        self.delta = 0
        self.old = 0

        pyxel.init(160, 120, caption="My resources")
        pyxel.load("assets/my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    # this is called at every frame
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.x = (self.x + 10) % pyxel.width

        # this is always 1
        self.delta = pyxel.frame_count - self.old
        self.old = pyxel.frame_count

    def draw(self):
        pyxel.cls(0)
        pyxel.text(100, 0, "frames/u:" + str(self.delta), 7)

        # draw bomb: img0, 16x16 pixels, u = 0
        # move at the framecount pace, this is just an ordinary counter
        offset = self.x
        pyxel.blt(0 + offset, 0, 0, 0, 0, 16, 16)

        # draw ship: img0, 16x16 pixels, u = 16, v= 0
        # move 8 times slower
        offset = (pyxel.frame_count // 8) % 160
        pyxel.blt(0 + offset, 16, 0, 16, 0, 16, 16)

        # draw ennemy: img0, 16x16 pixels, u = 32, v = 0
        # move 16 times slower
        offset = (pyxel.frame_count // 16) % 160
        pyxel.blt(0 + offset, 32, 0, 32, 0, 16, 16)


App()
