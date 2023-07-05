# 🖼 NFT Generator 🖼

Hello, this program is an nft generator that can combine your images with different combinations.

⭐Star This Repo⭐

___

### How To Use App

* Add your images with the same canvas size into the /layer folders in the /assets folder and run the code.
<br>

___
# If you need more layers

### First Step :

* Add /layer-(Your Layer Number) folder inside the /assets folder.

### Second Step :

Add the following variables between the #Variables.
```python

## Layers
layerImageNumber_("Your Layer Number") = 1

## The number of images in the layer
layer_("Your Layer Number")_ImageCount = ("The number of images in the layer")
```



### Third Step :

Add the following codes into the output() function.
```python


#LAYERS | Add as many layer as the image you add
layer("Your Layer Number") = Image.open("assets/layer-("Your Layer Number")/"+ str(layerImageNumber_("Your Layer Number")) +".png")

#OUTPUT | Add as many layer"Number".paste() as the layer you add
blend_("Next Layer Number") = Image.alpha_composite(blende_("Previous Layer Number"),layer("Your Layer Number"))
blend_("Next Layer Number").save("output/"+ str(outputCount) +".png", quality=100)
```



### Fourth Step : 

Add the following code inside the nested while loop inside the #Combination Generator.
```python
layerImageNumber_("Your Layer Number")= 1
        
        while layerImageNumber("Your Layer Number") <= layer_3_ImageCount:
            
            print(str(layerImageNumber_1) + str(layerImageNumber_2) + str(layerImageNumber_3) + str("Your Layer Number"))
            output()
            outputCount += 1
            layerImageNumber_("Your Layer Number") += 1

            
        
        layerImageNumber_("Previous Layer Number") += 1
```

