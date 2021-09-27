import pyxel
from board import Board
from item_char import ItemChar

class Box:
    def __init__(self):
        print("Init Box")
        self.boards = [
            Board(
                name="test",
                items=[
                    ItemChar((10, 10), "test text.", 2)
                ]
            )
        ]
        self.board_number = 0
        print(":")
    
    def update(self):
        self.boards[self.board_number].update()

    def draw(self):
        self.boards[self.board_number].draw()