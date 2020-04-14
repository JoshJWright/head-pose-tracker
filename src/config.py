import numpy as np 

UDP_IP = "127.0.0.1"
UDP_PORT = 4242

# Original WORLD_SPACE_POINTS places nose at center.
# WORLD_SPACE_POINTS = np.array([
#                             (0.0, 0.0, 0.0),             # Nose tip
#                             (0.0, -330.0, -65.0),        # Chin
#                             (-225.0, 170.0, -135.0),     # Left eye left corner
#                             (225.0, 170.0, -135.0),      # Right eye right corne
#                             (-150.0, -150.0, -125.0),    # Left Mouth corner
#                             (150.0, -150.0, -125.0)      # Right mouth corner
#                         ])

# New WORLD_SPACE_POINTS placing head at center
WORLD_SPACE_POINTS = np.array([
                            (0.0, 0.0, 250.0),             # Nose tip
                            (0.0, -330.0, 185.0),        # Chin
                            (-225.0, 170.0, 115.0),     # Left eye left corner
                            (225.0, 170.0, 115.0),      # Right eye right corne
                            (-150.0, -150.0, 125.0),    # Left Mouth corner
                            (150.0, -150.0, 125.0)      # Right mouth corner
                        ])

LANDMARK_IDXS = np.array([30, 8, 45, 36, 54, 48])

BIOCULAR_BREADTH = 12 # Distance between outer corners of eyes, used to scale translation