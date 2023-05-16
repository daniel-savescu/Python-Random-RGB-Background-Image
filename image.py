from PIL import Image
import random

#Generate random RGB

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,2500)

rgb = (r,g,b)


newImage = Image.new(mode= "RGBA", size=(1920,1080), color=rgb)

newImage.show()

newImage.save("backgroundImage.png")

print("The image had been saved in the current script folder")