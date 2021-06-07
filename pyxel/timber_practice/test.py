import pyxel


class PyxelApp:

    def __init__(self):
        pyxel.init(240, 135)

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.text((10, 10), "Hello world!")


if __name__ == "__main__":
    PyxelApp()