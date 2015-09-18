from PIL import ImageSequence  # iterator object that can be used to loop over an image sequence
from PIL import Image
from PIL import ImageColor
from PIL import ImageOps
import os

def open_image(path):
	image = None
	try:
		image = Image.open(path)
	except Exception as e:
		print("Image not found")
		print(e)
		return
	return image

def reduceRedPixel(pixel):
	value=getRed(pixel)
  	# setRed(pixel,value*0.5)

if __name__ == '__main__':
	
	# get image name for a user
	#pic = raw_input("Which file you want to remove red eye? (include extension):")

	#fileName = "images/" + pic
	fileName = "images/re5.jpg"
	image = open_image(fileName)
	# os.system('xdg-open ' + fileName)


	# image = image.convert('RGB')
	# get image size of x and y
	# (width, height) = image.size
	
	# max = 0

	# for w in range(1, width):
	# 	for h in range(1, height):
	# 		r, g, b = image.getpixel((w,h))
	# 		if r > max:
	# 			max = r
	# 		if (r in range (130, 255) and (g in range (1, 70) or b in range (1, 70))):
	# 			r = 0
	# 			g = 0
	# 			b = 0
	# 		#print r,g,b
	# 		#r = int(r*0.5)
	# 		image.putpixel((w,h), (r,g,b))
	# 		print r,g,b
	
	# print max

	# r, g, b = image.getpixel((187, 45))
	# print r, g, b

	#ImageOps.invert(image)
	# save_image(image, 'red.jpeg')
	#os.system('xdg-open ./red.jpeg')

	# Get the color data of every pixel in the image
	pixels = list(image.getdata())
	count = 0 # count for storing pixel count
	# For each pixel color tuple in pixels
	for pixel in pixels:
		# Prevent divide by zero error
		if(pixel[1] == 0 and pixel[2] == 0):
			pixel = (pixel[0], 1, 1)
		# Determine if pixel is too red
		redIntensity = (float(pixel[0]) / ((pixel[1] + pixel[2]) / 2))
		# If it is, set it to (Blue + Green) / 2
		if(redIntensity > 1.5):
			pixels[count] = (round((pixel[1] + pixel[2]) / 2), pixel[1], pixel[2])
		count = count + 1
	# Write the pixel data back to images
	image.putdata(pixels)
	image.show()
