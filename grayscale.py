from PIL import Image

def open_image(path):
	image = None
	try:
		image = Image.open(path)
	except Exception as e:
		print("Image not found")
		print(e)
		return
	return image

if __name__ == '__main__':
	fileName = "images/rgb.jpg"
	outputName = "gray.jpg"

	image = open_image(fileName)
	image = image.convert('L')
	image.show()
	image.close()

	image = open_image(fileName)
	width, height = image.size

	Method 1
	for w in range(width):
		for h in range(height):
			pixel = image.getpixel((w, h))
			pixelred = pixel[0]*0.399
			pixelgreen = pixel[1]*0.117
			pixelblue = pixel[2]*0.514
			lumigray = round(pixelred+pixelblue+pixelgreen)
			image.putpixel((w,h), (lumigray, lumigray, lumigray))

	# Method 2
	# pixels = list(image.getdata())
	# for pixel in pixels:
	# 	lumigray = round((pixel[0]*0.299) + (pixel[1]*0.114) + (pixel[2]*0.587))
	# 	pixel = (lumigray, lumigray, lumigray)
	# image.putdata(pixels)

	image.show()
	image.close()
