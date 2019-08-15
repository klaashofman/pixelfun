import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="My resources")
        pyxel.load("assets/my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        # pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)

        # draw bomb: img0, 16x16 pixels, x-offset = u = 0
        pyxel.blt(0, 0, 0, 0, 0, 16, 16)
        # draw ship: img0, 16x16 pixels, x-offset = u = 0
        pyxel.blt(0, 16, 0, 16, 0, 16, 16)
        # draw ennemy: img0, 16x16 pixels, x-offset = u = 0
        pyxel.blt(0, 32, 0, 32, 0, 16, 16)


App()
