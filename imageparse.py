from mcpi.minecraft import Minecraft
from mcpi import block
from PIL import Image
import math
colours = [ (255, 255, 255, "00"),
            (255, 0, 0, "14"),
            (255, 128, 0, "01"),
            (0, 255, 0, "13"),
            (255,128,255,"02"),
            (50,50,255,"03"),
            (255,255,0,"04"),
            (50,255,50,"05"),
            (255,102,178,"06"),
            (96,96,96,"07"),
            (192,192,192,"08"),
            (0,200,200,"09"),
            (150,0,150,"10"),
            (0,0,255,"11"),
            (102,51,0,"12"),
            (0,0,0,"15")]          
def nearest_colour( subjects, query ):
    return min(subjects,key = lambda subject:sum((s - q) ** 2 for s,q in zip( subject, query ) ) ) #uses math to return the nearest color
def init():
	ipString = "192.168.7.226"
	mc = Minecraft.create(ipString, 4711)
	mc.setting("world_immutable",False) 
	return mc
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None
    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel
    
def main():
	mc = init()
	x,y,z=mc.player.getPos()
	selection=input("what is the name of your file? must contain the extension: ")
	img = Image.open(selection);
	img=img.convert('RGB')
	for i in range(0,img.width): #reads every pixel and attributes a color based on rgb values
		for j in range(0,img.height):
			coord=(-i,abs(img.height-1-j)) #sets coordinates based on for loop
			bloop=(img.getpixel(coord)) #gets rgb
			print(bloop) #debug 
			woolcolor=str(nearest_colour(colours, bloop))
			woolcolor=(woolcolor[-4:])
			woolcolor=(woolcolor[:2])#trims output neatly
			print(woolcolor)
			mc.setBlock(x+5+i,y+j,z,35,int(woolcolor))		
	print(img.size)
	

if __name__ == "__main__":
 main()
