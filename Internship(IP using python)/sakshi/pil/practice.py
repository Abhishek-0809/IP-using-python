from PIL import Image

img1=Image.open('images\ladybug.jpg')
img=img1.convert('L')
pixel_color=list(img.getdata())
print(pixel_color)


#negative transformation function
def neg_trans(img):

  #get width and height of image
  width,height=img.size

  #traverse through pixels
  for x in range(width):
    for y in range(height):

      

      #if image is RGB, subtract individual RGB values
      if type(pixel_color) == tuple: 

        #s=(L-1)-r
        red_pixel=256-1-pixel_color[0]
        green_pixel=256-1-pixel_color[1]
        blue_pixel=256-1-pixel_color[2]

        #replace the pixel 
        img.putpixel((x,y),(red_pixel,green_pixel,blue_pixel))
      
      #if image is greyscale, subtract pixel intensity
      else:

        #s=(L-1)-r
        pixel_color=256-1-pixel_color 

        #replace the pixel
        img.putpixel((x,y),pixel_color)
  return img