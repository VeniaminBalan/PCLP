import cv2

image = cv2.imread("example.png")

# Rescale the image to half its size
rescaled_image = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)

#cv2.imshow("Rescaled Image", rescaled_image)

#gray = cv2.cvtColor(rescaled_image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image", gray)

#resized = cv2.resize(image, (200, 200))
#rotated = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)
#cv2.imshow("Resized and rotated Image", rotated)

#cv2.rectangle(rescaled_image, (50, 50), (150, 150), (0, 255, 0), 3)  # green box
#cv2.putText(rescaled_image, "Hello", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow("Image with Rectangle and Text", rescaled_image)
edges = cv2.Canny(rescaled_image, threshold1=100, threshold2=200)
print(edges)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()