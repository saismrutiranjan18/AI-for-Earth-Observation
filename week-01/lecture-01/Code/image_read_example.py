from PIL import Image
import matplotlib.pyplot as plt

# Read the image
img = Image.open("sample_satellite_image.jpg")

# Print information
print("Image size:", img.size)
print("Image mode:", img.mode)

# Display the image
plt.imshow(img)
plt.title("Satellite Image")
plt.axis("off")
plt.show()