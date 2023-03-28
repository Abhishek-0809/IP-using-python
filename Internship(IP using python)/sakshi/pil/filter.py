from PIL import Image,ImageFilter
img=Image.open('images\ladybug.jpg')
img.show()
edges_image = img.filter(ImageFilter.FIND_EDGES)
edges_image.save('images\ladybug_edges.jpg')
edges_image.show()


blur_image = img.filter(ImageFilter.BLUR)
blur_image.save('images\ladybug_blur.jpg')
blur_image.show()

sharpend_image = img.filter(ImageFilter.SHARPEN)
sharpend_image.save('images\ladybug_sharpend.jpg')
sharpend_image.show()

