### 01 02 03 ###

class Shape:
	def what_am_i(self):
		return "I am a shape"

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	
	def calculate_perimeter(self):
		return self.width * self.height
	
class Square(Shape):
	def __init__(self, one_side):
		self.one_side = one_side

	def calculate_perimeter(self):
		return self.one_side ** 2
	
	def change_size(self, n):
		self.one_side += n

shapes = [Rectangle(10, 20), Square(30)]
for shape in shapes:
	print(shape.calculate_perimeter())

print("-"*64)

shapes[1].change_size(3)
for shape in shapes:
	print(shape.calculate_perimeter())

for shape in shapes:
	print(shape.what_am_i())

### 04 ###

class Horse:
	def __init__(self, rider):
		self.rider = rider

class Rider:
	def __init__(self, name):
		self.name = name

rider = Rider("yayo256")
horse = Horse(rider)

print(horse.rider.name)