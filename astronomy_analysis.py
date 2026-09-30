import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


file_path = "data/HorseHead.fits"

with fits.open(file_path) as hdul:
    image_data = hdul[0].data


print("Data type:", type(image_data))
print("Image shape:", image_data.shape)

plt.imshow(image_data, cmap="gray")
plt.colorbar()
plt.title("Horsehead Nebula")
plt.xlabel("Pixel X")
plt.ylabel("Pixel Y")
plt.show()

print("Minimum:", np.min(image_data))
print("Maximum:", np.max(image_data))
print("Mean:", np.mean(image_data))
print("Median:", np.median(image_data))
print("Standard deviation:", np.std(image_data))

pixel_values = image_data.flatten()

plt.hist(pixel_values, bins=100)
plt.title("Pixel Intensity Distribution")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()

row_number = image_data.shape[0] // 2

x_values = np.arange(image_data.shape[1])
y_values = image_data[row_number, :]

plt.scatter(x_values, y_values, s=2)
plt.title("Pixel Intensity Across Image")
plt.xlabel("Pixel X Position")
plt.ylabel("Pixel Intensity")
plt.show()

