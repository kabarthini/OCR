import cv2
import numpy as np
import pytesseract
from PIL import Image

def mask_aadhar(image_path):
    # Load the original image
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Could not read the image at {image_path}")
        return

    # Define the regions to be masked
    region1 = (250, 410, 170, 50)  # Rectangle coordinates for the first region
    region2 = (1050, 410, 180, 50)  # Rectangle coordinates for the second region

    # Create a mask with two rectangles cutout
    mask = np.ones_like(original_image, dtype=np.uint8) * 255
    cv2.rectangle(mask, (region1[0], region1[1]), (region1[0] + region1[2], region1[1] + region1[3]), (0, 0, 0), -1)
    cv2.rectangle(mask, (region2[0], region2[1]), (region2[0] + region2[2], region2[1] + region2[3]), (0, 0, 0), -1)

    # Apply the mask to the original image
    masked_result = cv2.bitwise_and(original_image, mask)

    # Replace the masked regions with the corresponding regions from the original image
    original_image[region1[1]:region1[1]+region1[3], region1[0]:region1[0]+region1[2]] = original_image[region1[1]:region1[1]+region1[3], region1[0]:region1[0]+region1[2]]
    original_image[region2[1]:region2[1]+region2[3], region2[0]:region2[0]+region2[2]] = original_image[region2[1]:region2[1]+region2[3], region2[0]:region2[0]+region2[2]]

    # Save or display the unmasked result
    cv2.imwrite("unmasked_aadhar.jpg", original_image)
    cv2.imshow("Unmasked Aadhar", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'path/to/your/image.jpg' with the actual path to your Aadhar image
mask_aadhar(r'C:\Internship\PycharmProjects\ocr\aadar.jpg')
