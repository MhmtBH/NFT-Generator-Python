from PIL import Image, ImageDraw, ImageFilter


# Variables

outputCount = 0

## Layers
layerImageNumber_1 = 1
layerImageNumber_2 = 1
layerImageNumber_3= 1

## The number of images in the layer
layer_3_ImageCount = 4
layer_2_ImageCount = 2
layer_1_ImageCount = 7

##########################################################################################

# Image Generator

def output():
    
    #LAYERS | Add as many layer as the image you add
    layer1 = Image.open("assets/layer-1/"+ str(layerImageNumber_1) +".png") #Background image
    layer2 = Image.open("assets/layer-2/"+ str(layerImageNumber_2) +".png")
    layer3 = Image.open("assets/layer-3/"+ str(layerImageNumber_3) +".png")

    #OUTPUT | Add as many layer"Number".paste() as the layer you add
    blend_1 = Image.alpha_composite(layer1,layer2)
    blend_2 = Image.alpha_composite(blend_1,layer3)
    blend_2.save("output/"+ str(outputCount) +".png", quality=100)

##########################################################################################


# Combination Generator


while (layerImageNumber_1 <= layer_1_ImageCount):
    
    layerImageNumber_2 = 1
    
    while (layerImageNumber_2 <= layer_2_ImageCount):
        
        layerImageNumber_3 = 1
        
        while (layerImageNumber_3 <= layer_3_ImageCount):
            
            print(str(layerImageNumber_1) + str(layerImageNumber_2) + str(layerImageNumber_3))
            output()
            outputCount += 1
            layerImageNumber_3 += 1

               
        layerImageNumber_2 += 1
    
    layerImageNumber_1 += 1

print(outputCount)


    