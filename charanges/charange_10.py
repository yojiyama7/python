# 02 #
import math

### 01 ###

class Apple:
	def __init__(self, color, weight, price, days):
		self.color = color
		self.weight = weight
		self.price = price
		self.days = days

### 02 ###

class Circle:
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return self.radius ** 2 * math.pi

circle = Circle(5)
print(circle.area())

### 03 ###

class Triangle:
	def __init__(self, base, height):
		self.base = base
		self.height = height
	
	def area(self):
		return self.base * self.height / 2

triangle = Triangle(10, 3)
print(triangle.area())
		
### 04 ###

class Hexagon:
	def __init__(self, s1, s2, s3, s4, s5, s6):
		self.lines = [s1, s2, s3, s4, s5, s6]

	def calculate_perimeter(self):
		return sum(self.lines)
	
hexagon = Hexagon(28, 34, 53, 32, 42, 42)
print(hexagon.calculate_perimeter())