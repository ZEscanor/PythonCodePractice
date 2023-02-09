#Z Amusa
#this program creates a 3D image!
# prompt Users for two files
file= pickAFile()
file2 = pickAFile()
#make seperate pictures based on files that you picked.
pic1 = makePicture(file)
pic2= makePicture(file2)



 # a function definiton for red Scaling an image
def makeRed(pic1):
#loop every pixel
 for y in range(0, getHeight(pic1), 1):
  for x in range(0, getWidth(pic1), 1):
    #intial RGB of pixel
    p = getPixel(pic1, x, y)
    r = getRed(p)
    g= getGreen(p)
    b = getBlue(p)
    #avg values
    avg = int(r*.299+ g*.587 + b*.114)
    #set red to avgm set blue/Green to 0
    setRed(p,avg)
    setGreen(p,0)
    setBlue(p,0)
# a function definition for Blue/Green Scaling and image
def makeBlue(pic2):
#loop every pixel
 for y in range(0, getHeight(pic2), 1):
  for x in range(0, getWidth(pic2), 1):
    #intial RGB of pixel
    p = getPixel(pic2, x, y)
    r = getRed(p)
    g= getGreen(p)
    b = getBlue(p)
    #avg
    avg = int(r*.299+ g*.587 + b*.114)
    #set red to 0, set blue/Green to Avg
    setRed(p,0)
    setGreen(p,avg)
    setBlue(p,avg)
#a function made to superimpose images based on defitions above.
def combinePic():
 for x in range(0, pic1.getWidth(), 1):
  for y in range(0, pic1.getHeight(), 1):
     #Get both pixels
     p1 = getPixel(pic1, x, y)
     p2 = getPixel(pic2, x, y)
     # red value
     r = (getRed(p1)+getRed(p2))
     #green value
     g = (getGreen(p1) + getGreen(p2))
     # blue value
     b = (getBlue(p1) + getBlue(p2))
     #Save values to new pic
     setRed(p2, r)
     setGreen(p2, g)
     setBlue(p2, b)
    
#Before program starts check to see if images are same size. If not same size exit the loop, print error message and try again. 
if (getWidth(pic1) != getWidth(pic2) and getHeight(pic1) != getHeight(pic2)):
 showError("Images need to be the same size")
# if the images are the same size run program normally. 
else: 
#call my function to RedScale the first image.
 makeRed(pic1)
 #Call my function to Blue/Green scale my second image.
 makeBlue(pic2)
 #call my funtion to superimpose both images.
 combinePic()   
 #show and save my final result
 file3= pickAFile()
 writePictureTo(pic2,file3)
 stra = str("Your superimposed picture has been saved to:")
 print(stra + file3) 
 show(pic2)
    

