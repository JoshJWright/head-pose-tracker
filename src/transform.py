class Transform:
  """ Holds a six-float tuple for x, y, z, yaw, pitch, roll """
  def __init__(self, x=0.0, y = 0.0, z = 0.0, yaw = 0.0, pitch = 0.0, roll = 0.0):
    self.transform = (x, y, z, yaw, pitch, roll)

  def get(self):
    return self.transform