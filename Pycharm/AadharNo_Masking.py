import cv2
import numpy as np
import pytesseract

def mask_aadhar(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print(f"Error: Could not read the image at {image_path}")
        return

    # Define the regions to be masked
    region1 = (250, 410, 170, 50)  # Rectangle coordinates for the first region
    region2 = (1050, 410, 180, 50)  # Rectangle coordinates for the second region

    # Create a mask with two rectangles cutout
    mask = np.ones_like(image, dtype=np.uint8) * 255
    cv2.rectangle(mask, (region1[0], region1[1]), (region1[0] + region1[2], region1[1] + region1[3]), (0, 0, 0), -1)
    cv2.rectangle(mask, (region2[0], region2[1]), (region2[0] + region2[2], region2[1] + region2[3]), (0, 0, 0), -1)

    # Apply the mask to the image
    masked_result = cv2.bitwise_and(image, mask)

    # Save or display the masked result
    cv2.imwrite("masked_aadhar.jpg", masked_result)
    cv2.imshow("Masked Aadhar", masked_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Extract numbers from the masked regions
    masked_numbers_region1 = pytesseract.image_to_string(masked_result[region1[1]:region1[1]+region1[3], region1[0]:region1[0]+region1[2]], config='--psm 8')
    masked_numbers_region2 = pytesseract.image_to_string(masked_result[region2[1]:region2[1]+region2[3], region2[0]:region2[0]+region2[2]], config='--psm 8')



# Replace 'path/to/your/image.jpg' with the actual path to your Aadhar image
mask_aadhar(r'C:\Internship\PycharmProjects\ocr\aadar.jpg')
