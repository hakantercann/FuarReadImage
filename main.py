from PIL import Image
from pytesseract import pytesseract
import cv2
import matplotlib.pyplot as plt

# Define paths to tesseract executable and input image
path_to_tesseract = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
image_path = 'images/3.png'

# Open the image and store it in an image object
img = Image.open(image_path)

# Provide the tesseract executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Extract text from the image
text = pytesseract.image_to_string(img)
print("Extracted text from image file:")
print(text.strip())

# Initialize video capture
vid = cv2.VideoCapture(0)
vid.set(3, 200)  # Set width
vid.set(4, 200)  # Set height

print("\nPress 'a' to extract text from the current frame.")
print("Press 'q' to quit the application.")

# Loop for live video frame processing
while True:
    ret, frame = vid.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Use Matplotlib to display the frame
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.001)
    plt.clf()  # Clear the figure for the next frame

    # Check if the user presses 'a' to extract text
    if cv2.waitKey(1) & 0xFF == ord('a'):
        # Convert frame to RGB format for pytesseract
        text = pytesseract.image_to_string(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        print("Extracted text from current frame:")
        print(text.strip())

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close Matplotlib windows
vid.release()
plt.close()
