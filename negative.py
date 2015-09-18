from PIL import Image
import PIL.ImageOps
import sys

#error handling for when an image cannot be found
def open_image(path):
	image = None
	try:
		image = Image.open(path)
	except Exception as e:
		print("Image not found")
		print(e)
	return image

#Find the image and turn it to 
#negative image then save it with the name specified
if __name__ == '__main__':
	fileName = str(sys.argv[1])
	image = open_image(fileName)
	#The invert command subtracts the original color 
	#value from 255 to "negate" the image
	inverted_image = PIL.ImageOps.invert(image)
	inverted_image.save("images/Negative.jpg")
	