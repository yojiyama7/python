def pass_func(*_):
    pass


import pyxel


class App:
    def __init__(self):
        pyxel.init(240, 135, caption="Framework Test", fps=60)
        pyxel.mouse(True)
        
        def obj_next_color(this):
            this.col = (this.col + 1) % 16

        self.page_manager = PageManager([
            Page([
                ObjManager([
                    RectToSlide((10, 10), (20, 20), 11, speed=2),
                    RectToSlide((20, 32), (15, 15), 3, speed=2),
                ]),
                ObjManager([
                    RectToSlide((40, 32), (20, 20), 11, speed=0, click_func=obj_next_color),
                    RectToSlide((50, 10), (15, 15), 3),
                ]),
            ]),
            Page([
                ObjManager([
                    RectToSlide((20, 90), (30, 15), 8),
                ]),
            ]),
        ])

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            # next page
            # self.page_manager.next_page()
            # オブジェクトのupdate, drawの無効化、有効化
            obj = self.page_manager.pages[0].obj_managers[0].objs[0]
            obj.is_update = not obj.is_update
            # obj.is_draw = not obj.is_draw

        self.page_manager.update()

    def draw(self):
        pyxel.cls(0)

        self.page_manager.draw()


class PageManager:
    def __init__(self, pages, display_page_num=0):
        self.pages = pages
        self.display_page_num = display_page_num

    def next_page(self):
        self.display_page_num = (self.display_page_num + 1) % len(self.pages)

    def update(self):
        page = self.pages[self.display_page_num]
        page.update()

    def draw(self):
        page = self.pages[self.display_page_num]
        page.draw()


class Page:
    def __init__(self, obj_managers):
        self.obj_managers = obj_managers

    def update(self):
        for obj_manager in self.obj_managers:
            obj_manager.update()
    
    def draw(self):
        for obj_manager in self.obj_managers:
            obj_manager.draw()


class ObjManager:
    def __init__(self, objs):
        self.objs = objs

        self.is_update = True
        self.is_draw = True
    
    def update(self):
        if not self.is_update:
            return

        for obj in self.objs:
            obj.update()
    
    def draw(self):
        if not self.is_update:
            return

        for obj in self.objs:
            obj.draw()

# object
class RectToSlide:
    def __init__(self, xy, wh, col, speed=1, click_func=pass_func):
        self.x, self.y = xy
        self.w, self.h = wh
        self.col = col
        self.speed = speed
        self.click_func = click_func
        
        self.is_update = True
        self.is_draw = True
    
    def is_in_hitbox(self, pos):
        x, y = pos
        if (self.x <= x <= self.x + self.w) and (self.y <= y <= self.y + self.h):
            return True
        return False
    
    def handle_click(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.is_in_hitbox((pyxel.mouse_x, pyxel.mouse_y)):
            self.click_func(self)

    def update(self):
        if not self.is_update:
            return

        self.handle_click()

        self.x = (self.x + self.speed) % pyxel.width
    
    def draw(self):
        if not self.is_draw:
            return

        pyxel.rect(*(self.x, self.y), *(self.w, self.h), self.col)


if __name__ == "__main__":
    App()