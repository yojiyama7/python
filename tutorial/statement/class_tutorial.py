# 継承あり
class Creature:
    def __init__(self, lifespan, pos):
        self.lifespan = lifespan
        self.pos = pos
    
    def grow(self):
        self.lifespan = lifespan - 1

class Plant(Creature):
    def __init__(self, lifespan, pos):
        super().__init__(lifespan, pos)

class Person(Creature):
    def __init__(self, lifespan, pos, name):
        super().__init__(lifespan, pos)
        self.name = name

    def forward(self, step_len):
        self.x += step_len

# 継承なし  
# class Plant:
#     def __init__(self, lifespan, pos):
#         self.lifespan = lifespan
#         self.pos = pos
    
#     def grow(self):
#         self.lifespan = lifespan - 1

# class Person:
#     def __init__(self, lifespan, pos, name):
#         self.lifespan = lifespan
#         self.pos = pos
#         self.name = name

#     def grow(self):
#         self.lifespan = lifespan - 1

#     def forward(self, step_len):
#         self.x += step_len
