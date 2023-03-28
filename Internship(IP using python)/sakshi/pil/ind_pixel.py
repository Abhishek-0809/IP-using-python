from PIL import Image

thresh=200
img1=Image.open('images\ladybug.jpg')
# img1.show()

gray=img1.convert('L')
# gray.show()

x,y=gray.size
print(x,y)
val=list(gray.getdata())
print(val)
# max=print(max(val))
# min=print(min(val))
# # print(type(max))
# # print(type(max))
# max=int(max)
# min=int(min)
# print(type(max))
# print(type(min))
output=list()


for i in range(0,417):
    for j in range(0,647):
      =255-val(i,j)
      

print(output(i,j))
        




        



