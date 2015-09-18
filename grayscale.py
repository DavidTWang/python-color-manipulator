from PIL import Image
import sys

# Opens an image at the given path
def open_image(path):
	image = None
	try:
		image = Image.open(path)
	except Exception as e:
		print("Image not found")
		print(e)
		return
	return image

def main(argv):
	if(len(argv) != 1):
		print("Invalid number of arguments. Requires image path/filename.")
		sys.exit(2)
	else:
		fileName = argv[0]

	# ===============
	# Grayscale
	# ===============
	# Opens the image
	image = open_image(fileName)
	# Convert the image mode to "Luminosity"
	image = image.convert('L')
	# Show the image in xv
	image.show()
	# Close the image
	image.close()

	# ===========================
	# Grayscale with Luminosity
	# ===========================
	# Opens the image
	image = open_image(fileName)

	# ===========================================================
	# Method 1
	# This method involves looping through every single pixel,
	# altering the color value of that pixel, and changing it
	# to grayscale based on assigned color intensity

	# width, height = image.size
	# for w in range(width):
	# 	for h in range(height):
	# 		pixel = image.getpixel((w, h))
	# 		pixelred = pixel[0]*0.399
	# 		pixelgreen = pixel[1]*0.117
	# 		pixelblue = pixel[2]*0.514
	# 		lumigray = round(pixelred+pixelblue+pixelgreen)
	# 		image.putpixel((w,h), (lumigray, lumigray, lumigray))

	# ===========================================================
	# Method 2
	# This method is similar to method 1, except it runs much faster.
	# Instead of assigning each pixel individually, it maps all the
	# pixel colors and puts the data at once.
	
	# Get the color data of every pixel in the image
	pixels = list(image.getdata())
	count = 0 # count for storing pixel count
	# For each pixel color tuple in pixels
	for pixel in pixels:
		# Get the balanced grayscale color
		lumigray = round((pixel[0]*0.299) + (pixel[1]*0.114) + (pixel[2]*0.587))
		# Set the RGB tuple to gray
		pixels[count] = (lumigray, lumigray, lumigray)
		count = count + 1
	# Write the pixel data back to images
	image.putdata(pixels)

	# Show and close the image
	image.show()
	image.close()

if __name__ == '__main__':
	main(sys.argv[1:])
