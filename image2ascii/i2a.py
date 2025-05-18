import cv2
import numpy as np

def linear_interpolation(minValue1, maxValue1, minValue2, maxValue2, value):
    # Ensure the value is within the original range
    if value < minValue1 or value > maxValue1:
        raise ValueError(f"Value {value} is outside the bounds of [{minValue1}, {maxValue1}]")

    # Linear interpolation formula
    return minValue2 + ((value - minValue1) / (maxValue1 - minValue1)) * (maxValue2 - minValue2)

# ASCII characters to map to pixel values
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Read the image
image = cv2.imread("OIP.jpg")

scale = 0.1
# Resize the image
image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create an empty list for the ASCII art (list of lists)
ascii_image = [["" for _ in range(gray_image.shape[1])] for _ in range(gray_image.shape[0])]

# Iterate over each pixel and map the grayscale value to an ASCII character
for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        # Get the grayscale value at the current pixel
        gray_value = gray_image[i, j]
        
        # Map the grayscale value to an ASCII character index
        index = int(linear_interpolation(0, 255,len(ascii_chars) - 1, 0, gray_value))
        
        # Ensure index is within bounds (optional, but ensures stability)
        index = min(max(index, 0), len(ascii_chars) - 1)
        
        # Assign the corresponding ASCII character to the list
        ascii_image[i][j] = ascii_chars[index]

# Save the ASCII image to a file
with open("output.txt", "w") as file:
    for row in ascii_image:
        file.write("".join(row) + "\n")

# Optionally, display the original and grayscale image (for debugging purposes)
# cv2.imshow("Original Image", image)
# cv2.imshow("Grayscale Image", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
