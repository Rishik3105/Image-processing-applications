Image Processing Application 🌟

This project is a simple Image Processing Tool 🖼️ built using OpenCV. It allows users to perform essential image processing operations such as blurring the image and viewing its color-space transformations.

✨ Features

Blur Your Image: Apply a median blur filter to your image for a smooth, noise-reduced effect.

View HSV Image: Convert the image to the Hue-Saturation-Value (HSV) color space and visualize it.

View LAB Image: Transform the image to the Lightness-Alpha-Beta (LAB) color space for advanced color processing.

🚀 How It Works

Input the Choice:

1 for blurring the image.

2 to convert and view the image in HSV format.

3 to convert and view the image in LAB format.

Provide the Path: Enter the file path of the image to be processed. Ensure the path is accurate!

Processing Begins:

The program reads the image using cv.imread().

Depending on your choice:

Applies median blur using cv.medianBlur().

Converts the image to HSV with cv.cvtColor() (BGR to HSV).

Converts the image to LAB with cv.cvtColor() (BGR to LAB).

Display Output: The selected transformation or effect is displayed in a new window using cv.imshow().

🛠️ Prerequisites

Python 3.x 🐍

OpenCV library (cv2)

📸 Example Input & Output

Original Image 🖼️:

File: path/to/your/image.jpg

Outputs:

Blurred Image 🌫️:

Applied with a kernel size of 7.

HSV Conversion 🌈:

Visualizes the image in the Hue-Saturation-Value domain.

LAB Conversion 🎨:

Displays the image in the Lightness, Alpha, Beta color model.

🛡️ Notes

Make sure the file path is correct; otherwise, the program might not read the image.

The window will remain open until you press any key (cv.waitKey(0)).

Feel free to fork this repository and contribute enhancements! 🚀
