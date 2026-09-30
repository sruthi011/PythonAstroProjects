import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


file_names = [
    "M13_blue_0001.fits",
    "M13_blue_0002.fits",
    "M13_blue_0003.fits",
    "M13_blue_0004.fits",
    "M13_blue_0005.fits"
]

images = []

for file_name in file_names:
    file_path = "data/" + file_name

    with fits.open(file_path) as hdul:
        image = hdul[0].data

    images.append(image)


print("Number of images:", len(images))

for i, image in enumerate(images):
    print("Image", i + 1, "shape:", image.shape)


stacked_image = np.mean(images, axis=0)

print("Stacked image shape:", stacked_image.shape)


vmin = np.percentile(stacked_image, 5)
vmax = np.percentile(stacked_image, 99)

vmin = np.percentile(stacked_image, 50)
vmax = np.percentile(stacked_image, 99.5)

plt.imshow(
    stacked_image,
    cmap="gray",
    vmin=vmin,
    vmax=vmax
)

plt.colorbar()
plt.title("M13 - Contrast Enhanced")
plt.xlabel("Pixel X")
plt.ylabel("Pixel Y")

plt.show()

print("Minimum:", np.min(stacked_image))
print("5th percentile:", np.percentile(stacked_image, 5))
print("50th percentile:", np.percentile(stacked_image, 50))
print("95th percentile:", np.percentile(stacked_image, 95))
print("99th percentile:", np.percentile(stacked_image, 99))
print("Maximum:", np.max(stacked_image))

plt.hist(stacked_image.flatten(), bins=100)

plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.title("M13 Stacked Image - Pixel Intensity Distribution")

plt.show()
