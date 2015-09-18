from PIL import Image
import PIL.ImageOps

def open_image(path):
	image = None
	try:
		image = Image.open(path)
	except Exception as e:
		print("Image not found")
		print(e)
	return image

if __name__ == '__main__':
	fileName = "images/ak.jpg"
	image = open_image(fileName)
	inverted_image = PIL.ImageOps.invert(image)
	inverted_image.save("Negative.jpg")
	