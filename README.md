# Head Pose Tracker

This project will attempt to use facial pose estimation as a head-tracking controller for use in simulators such as DCS: World. There are powerful solutions for head tracking existing, including TrackIR and OpenTrack. Starting as a closed project to prove the concept, this repository may be made open source at a later date.

The project will use the UDP input for OpenTrack to attach to software using the tracker.

## Components

### Pose Detection
A computer vision component that will extract the estimated position and rotation (6 axis - X,Y,Z,R,P,Y).
This is the key component for performance, the higher the polling rate and the more robust the output, the better the solution.

### UDP packaging
This module packages the data and sends it via UDP.
