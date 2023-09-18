# Revision Checking Tool :)
This Python script is designed for document checking, enabling users to overlay two images. The images are color inverted, and the black lines in the documents are either redrawn in red or blue. When the lines in the documents are in the same place, they are drawn in the combined color purple. This tool is particularly useful for reviewing engineering drawings and easily identifying changes between versions.

## How to Use

1. Make sure you have openCV installed.
2. Place the two images you want to overlay in the specified variables "image1" and "image2" within the script (yes its manual lmao because this was mostly used by me).
3. View the result, image should be saved as 'overlay.png'
4. profit?

## Overview of image_overlay.py 
|function | what it does  |
----------------------------|------------------------------------------------------- |
|resize_image(image, width, height) |  Resizes the input image to the specified width and height. |
|  convert_to_red_grayscale(input_image) |   Converts the input image to grayscale and redraws the lines in red. |  
| convert_to_blue_grayscale(input_image)  | Converts the input image to grayscale and redraws the lines in blue.  |  
| invert_colors(image)  |  Inverts the colors of the input image. |  



