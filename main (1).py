from tkinter import *
from PIL import Image, ImageFilter
from PIL import ImageTk

def calcDistance(tuple1,tuple2):

  x1 = tuple1[0]

  y1 = tuple1[1]

  z1 = tuple1[2]

  x2 = tuple2[0]

  y2 = tuple2[1]

  z2 = tuple2[2]

  d = ((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

  return d

print(calcDistance((1,2,3),(6,7,8)))

im1 = Image.open('image_A.jpeg','r')

print('Image A is an ocean')

width, height = im1.size

pixel_values = list(im1.getdata())

im1.close()

print()

lengthA = len(pixel_values) 
print(lengthA)

print(pixel_values[0:100])

root = Tk()  

canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open("image_A.jpeg"))  

canvas.create_image(20, 20, anchor=NW, image=img)

root.after(5000,lambda:root.destroy())

root.mainloop()
#---------------------------------------------------------------------------------


im2 = Image.open('image_B.jpeg','r')

print('Image B is a Forest')

width, height = im2.size

pixel_values2 = list(im2.getdata())

im2.close()

print()

lengthB = len(pixel_values2) 
print(lengthB)

print(pixel_values[0:100])

root = Tk()  

canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open("image_B.jpeg"))  

canvas.create_image(20, 20, anchor=NW, image=img)

root.after(5000,lambda:root.destroy())

root.mainloop()

print('What would you like the computer to guess? Write the file name')
guess = input()
#----------------------------------------------------------------------------------
im3 = Image.open(guess,'r')

print('Image C is an ocean')

width, height = im3.size

pixel_values3 = list(im3.getdata())

im3.close()

print()

lengthC = len(pixel_values3) 
print(lengthC)

print(pixel_values3[0:100])
'''
root = Tk()  
guess = input()

canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open(geuss))  

canvas.create_image(20, 20, anchor=NW, image=img)

root.after(5000,lambda:root.destroy())

root.mainloop()'''

print(pixel_values3[0:100])

#----------------------------------------------------------------------------------
lengths = [lengthA, lengthB, lengthC]

pics = [pixel_values, pixel_values2, pixel_values3]

minimum = min(lengths)

print(minimum)
#----------------------------------------------------------------------------------

for i in range(len(pics)):
  holder = []
  for j in range(len(pics[i])):
   
    if len(holder) < minimum:
      holder.append(pics[i][j])
  pics[i] = holder
  
for i in range(len(pics)):

   print(len(pics[i]))

#----------------------------------------------------------------------------------
AC = []
BC = []

for i in range(len(pics[2])):
  dA = calcDistance(pics[2][i],pics[0][i])
  AC.append(dA)
  dB = calcDistance(pics[2][i],pics[1][i])
  BC.append(dB)

  
AC_shortest = []

for i in range(len(AC)):
  if AC[i] < BC[i]:
    AC_shortest.append(0)

  else:
    AC_shortest.append(1)

result = sum(AC_shortest)/len(AC_shortest)

#print(result)
#----------------------------------------------------------------------------------

round(result)
print(result)

if result - .6 > 0:
  print('Mystery Image is a forest because its pixels are  70 % similar to Image B')
elif result -.6 > 0:
  print('Mystery Image is an ocean because its pixels are  96 % similar to Image A')

#----------------------------------------------------------------------------------

root = Tk()  


canvas = Canvas(root, width = 300, height = 300)  

canvas.pack()  

img = ImageTk.PhotoImage(Image.open(guess))  

canvas.create_image(20, 20, anchor=NW, image=img)




root.after(5000,lambda:root.destroy())

root.mainloop()

