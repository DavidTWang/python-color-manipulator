from PIL import Image
import PIL.ImageOps

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
	fileName = "images/ak.jpg"
	image = open_image(fileName)
	inverted_image = PIL.ImageOps.invert(image)
	inverted_image.save("images/Negative.jpg")
	