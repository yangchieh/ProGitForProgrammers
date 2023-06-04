class Calculator:
  def __init__(self, angle, velocity, height):
    self.px = 0.0
    self.py = height

  def add(self, left, right):
    return left + right