from transform import Transform
import socket
import struct

class UDPSender:

  def __init__(self, ip, port):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.ip = ip
    self.port = port
  
  def sendTransform(self, transform: Transform):
    """ Packages tuple to binary and sends to configured ip:port """
    self.sock.sendto(struct.pack("<dddddd", *transform.get()), (self.ip, self.port))


if __name__ == "__main__":
  import random
  sender = UDPSender("127.0.0.1", 4242)
  while True:
    sender.sendTransform(Transform(0,0,0,0,0,0))