from PIL import Image
import numpy as np

def person_detected(image1_file, image2_file, t1):
    # Load images and convert to grayscale
    img1 = Image.open(image1_file).convert("L")
    img2 = Image.open(image2_file).convert("L")

    # Convert to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Compute absolute difference
    diff = np.abs(arr1 - arr2)
    total_diff = np.sum(diff)

    print("Pixel difference:", total_diff)

    # Threshold decision
    return total_diff > t1
