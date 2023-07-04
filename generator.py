from PIL import Image, ImageDraw, ImageFilter

#LAYERS | Add as many layer as the image you add

background = Image.open('assets/bg.png') #Background image
foreground = Image.open('assets/tshirt.png') 
foreground2 = Image.open('assets/logo.png')

#OUTPUT | Add as many background.paste() as the layer you add

background.paste(foreground, (0, 0), foreground) 
background.paste(foreground2,(0, 0),foreground2)
background.save('output/nft.png', quality=100)