class Book:
  def __init__(self, angle, velocity, height):
    self.px = 0.0
    self.py = height

  def subtract(self, left, right):
    return left - right

  def add(self, left, right):
    return left + right

  def multiply(self, left, right):
    return left * right
    
  def divide(self, left, right):
    return left / right