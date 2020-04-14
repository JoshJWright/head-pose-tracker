from config import BIOCULAR_BREADTH
from config import LANDMARK_IDXS
from config import WORLD_SPACE_POINTS
import cv2 as cv 
import dlib
import imutils
from imutils import face_utils
import math
import numpy as np 
from transform import Transform

class PoseDetector:
  """ This class handles image processing using the dlib library for extracting pose from an image """

  def __init__(self):
    self.detector = dlib.get_frontal_face_detector()
    self.predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")

  def detect(self, frame):
    """ Detects pose of the first face found. assumes full size color image """
    # Resize image and take grayscale
    frame = imutils.resize(frame, width = 400)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect first face and facial landmarks
    faceRects = self.detector(frame, 0)
    if len(faceRects) == 0:
      return None
    landmarks = face_utils.shape_to_np(self.predictor(frame, faceRects[0]))

    # Get image /camera parameters
    imSize = frame.shape
    focal_length = imSize[1]
    center = (imSize[1]/2, imSize[0]/2)
    cam_matrix = np.array(
      [[focal_length, 0, center[0]],
      [0, focal_length, center[1]],
      [0, 0, 1]], dtype = "double"
    )
    dist_coeffs = np.zeros((4,1)) # Assumes no lens distortion

    # Get relevant landmarks
    points = []
    for x in LANDMARK_IDXS:
      points.append(landmarks[x])
    imagePoints = np.array(points, dtype="double")

    # Get pose
    (success, rotV, tranV) = cv.solvePnP(WORLD_SPACE_POINTS, imagePoints, cam_matrix, dist_coeffs, flags=cv.SOLVEPNP_ITERATIVE)

    # Handling values, convert rotation to degrees and scale translation using biocular width
    rotV = [math.degrees(r) for r in rotV]
    # this scalar should convert pixels to centimeters by approximating the size of the head
    translation_scale = BIOCULAR_BREADTH / (landmarks[45][0] - landmarks[36][0])
    tranV = [translation_scale * x for x in tranV]

    if success:
      # N.B. OpenTrack rotation order is Yaw, Pitch, Roll, OpenCV is Pitch, Yaw, Roll
      # Also, Pitch is inverted from solvePnP
      return Transform(x = tranV[0], y = tranV[1], z = tranV[2],
                       yaw = rotV[1], pitch = -rotV[0], roll = rotV[2])
    else:
      return None