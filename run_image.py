import cv2
import matplotlib.pyplot as plt
import copy
import numpy as np

from src import model
from src import util
from src.body import Body

body_estimation = Body('model/body_pose_model.pth')

img = 'images/wl-man-3.png'
frame = cv2.imread(img)  # B,G,R order
candidate, subset = body_estimation(frame)
canvas = copy.deepcopy(frame)
print((subset))
print((candidate))
canvas = util.draw_bodypose(canvas, candidate, subset)

cv2.imshow('Preview', canvas)
cv2.waitKey(0)

# plt.imshow(canvas[:, :, [2, 1, 0]])
# plt.axis('off')
# plt.show()