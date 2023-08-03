
#========== Author : Sayed Mujtaba Ahmady =================================
# Facebook Page : https://www.facebook.com/profile.php?id=100075938127515 =
#==========================================================================
#First of all you need to install the Pillow library then using following command you can import it
#Never forget to read the documentation https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img.size)

# print(img.mode) ==> this line of code show you the color mode of the image

# If you want to see the excutable commnad of the image you can use the following command
# print(dir(img))

#---- After filtering don't forget to save it in png some time it can't support jpg

#Following command will blue the image
# filter_img = img.filter(ImageFilter.BLUR)
# filter_img.save("Blur.png", 'png') ==> Blur the image and save it by the name of blur.png

#Following command will Smooth the image
# filter_img = img.filter(ImageFilter.SMOOTH)
# filter_img.save("smooth.png", 'png')


# filter_img = img.filter(ImageFilter.SHARPEN)
# filter_img.save("sharp.png", 'png')

#using the following code you can change the color mode of image 
#For this command don't forget to check the documentation if you want to figure out different color mode
# filter_img = img.convert('L')
# filter_img.save("gray.png", 'png')

#following command will open the image for you
#filter_img.show()



filter_img = img.convert('L')
#the following code will rotate the image 90 degree you can change the value form 1 to 360
# crooked = filter_img.rotate(90)
# crooked.save("rotated.png", 'png')

#The following code will change the size of the image don't forget that the type of values must be tuple otherwise you will fetch an error
# resize = filter_img.resize((300, 300))
# resize.save('resize.png', 'png')

#Sing the following code you can crop the image
# Pixels of the image
box = (100, 100, 400, 400)
region = filter_img.crop(box)
region.save('crop.png', 'png')