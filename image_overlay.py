import cv2
import numpy as np
from cv2 import imread

def resize_image(image, width, height):
    resized_image = cv2.resize(image, (width, height))
    return resized_image

def convert_to_red_grayscale(input_image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Create an empty 3-channel image (all black)
    height, width = gray_image.shape
    red_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Map grayscale values to the red channel
    red_image[:, :, 2] = gray_image

    return red_image

def convert_to_blue_grayscale(input_image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Create an empty 3-channel image (all black)
    height, width = gray_image.shape
    blue_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Map grayscale values to the blue channel
    blue_image[:, :, 0] = gray_image

    return blue_image

def invert_colors(image):
    inverted_image = cv2.bitwise_not(image)
    return inverted_image



def main():
    # Load the input images
    image1 = "images\Z_FACE_compare.PNG"
    image2 = "images\Z_FACE.PNG"
    imageRead = cv2.imread(image1)
    imageRead2 = cv2.imread(image2)
    
    # Check if the images are successfully loaded
    if imageRead is None:
        print("Failed to read 1 input images.")
        if imageRead2 is None:
            print("Failed to read 2 input images.")
            exit()
        exit()

    imageRead = invert_colors(imageRead)
    imageRead2 = invert_colors(imageRead2)

    imageRead = convert_to_blue_grayscale(imageRead)
    imageRead2 = convert_to_red_grayscale(imageRead2)

    alpha = 0.5
    blended_image = cv2.addWeighted(imageRead, alpha, imageRead2, 1 - alpha, 0)

    # Show image 2 in an output window

    # Specify the output file path
    output_path = 'overlay.png'

    cv2.imwrite(output_path, blended_image)

if __name__ == '__main__':
    main()