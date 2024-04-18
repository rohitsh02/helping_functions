from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')

# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)

# crooked.save("grey.png", 'png')

# resize = filtered_img.resize((300, 300))
# resize.save("roh.png", 'png')

# box = (100, 100, 400, 400)
# region = img.crop(box)
# region.save("crop.png", 'png')

# img2 = Image.open('./Pokedex/astro.jpg')

# print(img2.size)

# new_img = img2.resize((400, 400))
# new_img.save('thumbnail.jpg')

# img2.thumbnail((400, 400))
# img2.save("thumb2.jpg")

# print(img2.size)