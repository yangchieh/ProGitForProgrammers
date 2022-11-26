import math

class Cannonball:
  def __init__(self, angle, velocity, height):
    self.px = 0.0
    self.py = height
    theta = math.radians(angle)
    self.vx = velocity * math.cos(theta)
    self.vy = velocity * math.sin(theta)

  def simulate(self, interval):
    print('\nThe trajectory:')
    print('    x       y')
    print('--------------')
        
    while self.py >= 0:
      self.px += interval*self.vx
      vy2 = self.vy - 9.8*interval
      self.py += interval*(self.vy+vy2)/2.0
      self.vy = vy2
      print(f'{self.px:>5.1f}\t{self.py:>5.1f}')

def main():
  angle, v, h0, interval = getInputs()
  cannonball = Cannonball(angle, v, h0)
  cannonball.simulate(interval)
  print(f'\nDistance traveled: {cannonball.px:.1f} meters.')

def getInputs():
  angle = float(input('Launch angle (in degrees): '))
  v = float(input('Initial velocity (in meters/second): '))
  py = float(input('Initial height (in meters): '))
  interval = float(input('Time interval (in seconds): '))
  return angle, v, py, interval

if __name__ == '__main__':
  main()
