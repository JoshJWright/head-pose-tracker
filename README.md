# Head Pose Tracker

This project will attempt to use facial pose estimation as a head-tracking controller for use in simulators such as DCS: World. There are powerful solutions for head tracking existing, including TrackIR and OpenTrack. Starting as a closed project to prove the concept, this repository may be made open source at a later date.

## Components

### Pose Detection
A computer vision component that will extract the estimated position and rotation (6 axis - X,Y,Z,R,P,Y).
This is the key component for performance, the higher the polling rate and the more robust the output, the better the solution.

### USB Emulation
A component that emulates a USB HID with the 6 axes to use as input to DCS.
