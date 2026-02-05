import cv2

# Load image captured from Pi camera
image = cv2.imread("images/lab5-rpicam-still.png")

if image is None:
    print("Error: Image not found.")
    exit(1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Save processed image
cv2.imwrite("lab5-edges.png", edges)

print("Edge detection complete. Saved as lab5-edges.png")
