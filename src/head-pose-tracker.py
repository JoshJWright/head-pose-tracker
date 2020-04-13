import config
from imutils.video import VideoStream
from poseDetector import PoseDetector
import time
from udp import UDPSender

print("[INFO] Starting Head-Pose-Tracker")
print("[INFO] Starting Camera")
vs = VideoStream().start()
time.sleep(2.0)

print("[INFO] Loading model and UDP components")
poseDetector = PoseDetector()
udp = UDPSender(config.UDP_IP, config.UDP_PORT)

while True:
  frame = vs.read()
  pose = poseDetector.detect(frame)
  if pose is None:
    pass
  else:
    udp.sendTransform(pose)