import cv2
import numpy as np

# Create a blank image (white background)
width, height = 800, 600
blank_image = np.zeros((height, width, 3), dtype=np.uint8)

# Define colors (BGR format)
color_red = (0, 0, 255)
color_green = (0, 255, 0)
color_blue = (255, 0, 0)

# Draw a line
cv2.line(blank_image, (100, 100), (400, 100), color_red, thickness=2)

# Draw a rectangle
cv2.rectangle(blank_image, (200, 200), (500, 400), color_green, thickness=3)

# Draw an ellipse
cv2.ellipse(blank_image, (300, 300), (100, 50), 45, 0, 360, color_blue, thickness=2)

# Draw a circle
cv2.circle(blank_image, (600, 300), 50, color_red, thickness=-1)  # -1 for filled circle

# Display the image
cv2.imshow('Geometrical Shapes', blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
