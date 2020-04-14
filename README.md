# Head Pose Tracker

This project will attempt to use facial pose estimation as a head-tracking controller for use in simulators such as DCS: World. There are powerful solutions for head tracking existing, including TrackIR and OpenTrack. Starting as a closed project to prove the concept, this repository may be made open source at a later date.

As most users have a webcam anyway, this will attempt to be an essentially free head tracker (for better or for worse).

This is being developed during the COVID-19 lockdown, when I do not have access to my main PC to test this in-game.

## Usage

After installing the prerequisites below:
1. Run `head-pose-tracker.py` from the `src` directory.
2. Run OpenTrack, select "UDP over Network" for the input and make sure it's listening on the correct port (default: 4242)

### Prerequisites

- [OpenCV](opencv.org) - A computer vision library used for handling the images and solving for the pose.
- [dlib](dlib.net) - A toolkit containing many algorithms, this project uses the face detector and shape predictor using a model trained by [Adrian Rosebrock](https://www.pyimagesearch.com/2017/04/17/real-time-facial-landmark-detection-opencv-python-dlib/).
- [Python 3.7](www.python.org) - The language/interpreter
- [imutils](https://www.pyimagesearch.com/2015/02/02/just-open-sourced-personal-imutils-package-series-opencv-convenience-functions/) - A package of convenience functions from Adrian Rosebrock.
- [NumPy](https://numpy.org/) - Python library for arrays etc.
- [OpenTrack](https://github.com/opentrack/opentrack) - For taking the data via UDP and inputting it to the game.
- A webcam (any kind)

## How does it work?
1. A frame is read from the camera
2. The frame is resized and reduced to a grayscale image
3. Faces are detected using `dlib.get_frontal_face_detector()`
4. For the first face, facial landmarks are found using `dlib.shape_predictor()` and the `shape_predictor_68_face_landmarks.dat` file.
5. A set of 5 landmarks are taken:
  i. Left corner of left eye
  ii. Right corner of right eye
  iii. Nose tip
  iv. Left corner of mouth
  v. Right corner of mouth
  vi. Chin
6. Using an approximation of these points in the world space (relative to the head's center) and assuming no camera distortion, the pose of these points is estimated using OpenCV's solvePnP method.
7. The vectors returned are packaged and sent via UDP to the configured IP/Port.

## Problems
- Performance: This takes a fair amount of processing power that may affect game performance. Optimising the program is important.