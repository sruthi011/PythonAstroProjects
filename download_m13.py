from urllib.request import urlretrieve

base_url = "http://data.astropy.org/tutorials/FITS-images/"

files = [
    "M13_blue_0001.fits",
    "M13_blue_0002.fits",
    "M13_blue_0003.fits",
    "M13_blue_0004.fits",
    "M13_blue_0005.fits"
]

for filename in files:
    url = base_url + filename
    destination = "data/" + filename

    urlretrieve(url, destination)

    print("Downloaded:", filename)

print("All M13 images downloaded!")