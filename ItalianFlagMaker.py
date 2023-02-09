#Z Amusa  
#yamusa2  
#this project makes the italian flag. It will use redscaling, greenscaling, and greyscaling to make the images. It will also use cropping to make sure the images are equal in size.
#this function will make a picture red
def makeRed(picC):
#we loop over every pixel in our picture
 for y in range(0, getHeight(picC), 1):
  for x in range(0, getWidth(picC), 1):
    #get the RGB of original picture
    p = getPixel(picC, x, y)
    r = getRed(p)
    g= getGreen(p)
    b = getBlue(p)
    #avg value formula
    avg = int(r*.299+ g*.587 + b*.114)
    #set red to avg set b/g to 0
    setRed(p,avg)
    setGreen(p,0)
    setBlue(p,0)
 #returrn our picture that we will use later
 return picC
#this function makes a picture green
def makeGreen(picA):
#loop every pixel
 for y in range(0, getHeight(picA), 1):
  for x in range(0, getWidth(picA), 1):
    #intial RGB of pixel
    p = getPixel(picA, x, y)
    r = getRed(p)
    g= getGreen(p)
    b = getBlue(p)
    #avg
    avg = int(r*.299+ g*.587 + b*.114)
    #set red/Blue to 0, set Green to Avg
    setRed(p,0)
    setGreen(p,avg)
    setBlue(p,0)
 #return our green picture which we will use later
 return picA
 #this function makes a picture greyscale   
def makeGrey(picB):    
 #loop over every pixel in our picture
 for y in range(0, getHeight(picB), 1):
  for x in range(0, getWidth(picB), 1):
    #get rgb
    p = getPixel(picB, x, y)
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    #average rgb values
    avg = int(r*.299 + g*.587 + b*.114)
    #set rgb values to my new average value
    setRed(p, avg)
    setGreen(p, avg)
    setBlue(p, avg)
 #return our greyscale picture which we will use later   
 return picB
 # this picture collages two picture together, for our project we will call this funtion two times to successfully make our flag   
def collage(outpic1, outpic2):
 #define tallest as a variable and number
  tallest = 0
  #we want to set the overall y value to our tallest picture, so our combined image will have the same height, to do this we use an if/else statement to determine which picture is taller than the other.
  if (getHeight(outpic1) > getHeight(outpic2)):
    tallest = getHeight(outpic1)
  #if above isnt true then pic 2 is taller
  else:
    tallest = getHeight(outpic2)
    
   #make our picture using addint the widths of our two pictures then setting the y value to our tallest height from above.
  outputpic = makeEmptyPicture(getWidth(outpic1) + getWidth(outpic2), tallest)

  #we will loop over first picture, copy it to our output
  for x in range(0, getWidth(outpic1), 1):
    for y in range(0, getHeight(outpic1), 1):
      inputpix = getPixel(outpic1, x, y)
      color = getColor(inputpix)
      outputpix = getPixel(outputpic, x,y)
      setColor(outputpix, color)
 
  #loop over second picture, copy to our output
  for x in range(0, getWidth(outpic2), 1):
    for y in range(0, getHeight(outpic2), 1):
      inputpix = getPixel(outpic2, x, y)
      color = getColor(inputpix)
      outputpix = getPixel(outputpic, x + getWidth(outpic1),y)
      setColor(outputpix, color)     
  #we shall overall return our picture
  return outputpic
#this function will crop our desired picture, we use the end and start x and y to crop our picture successfully by our desired amount.
def crop(inputpic, startx, starty, endx, endy):
  #create a new picture with the correct dimensions
  outputpic = makeEmptyPicture(endx-startx, endy-starty)
  #loop over every pixel
  for x in range(startx, endx, 1):
    for y in range(starty, endy, 1):
      origpixel = getPixel(inputpic, x, y)
      color = getColor(origpixel)
      newpixel = getPixel(outputpic, x - startx, y - starty)
      setColor(newpixel, color)
  #return our value
  return outputpic
# now after we defined our functions, we now use pickafile to select the directory
fname = pickAFile()
#prints what directory you selected
print(fname)


#in order to hard code our files we need to use the \. This signifies the program to stop right at that point.
directorypos = fname.rfind("\\")
#if our user doesnt have a PC the above will return -1, in order for this code to work with MAC's we use / instead. if above returns -1 the code will instead look for a /.
if (directorypos == -1):
  directorypos = fname.rfind("/")
#now we are ready to add our filenames that we saved, we want the position after the \ or /.
dirname = fname[0:directorypos+1]

print(dirname)
#now we add our filenames to our dirname to get correct pictures
pizzafile = dirname + "pizza.jpg"
pastafile = dirname + "pasta.jpg"
winefile= dirname + "wine.jpg"
print(pizzafile)
print(pastafile)
print(winefile)
#make a picture using every filename above
picA = makePicture(pizzafile)
picB = makePicture(pastafile)
picC = makePicture(winefile)
#now we call our functions to make the corresponding colors of the Italian flag
#first we make red
makeRed(picC)
#next green
makeGreen(picA)
#next grey
makeGrey(picB)
# we have return values in our above functions set another variable equal to our modified pictures
# this is our red picture
picD = picC
#this is our green picture
picE = picA
#This is our grey/white picture
picF = picB
#now we are going to first crop every picture before proceeding to collage.
outpic1 = crop(picE, 250, 0, 489, 380)
outpic2 = crop(picF, 250, 0, 489, 380)
outpic3 = crop(picD, 250, 0, 489, 380)
#now we are ready to make our flag! first we enter our outpic1(Green Picture) and our outpic2(Grey/white Picture) to collage first
output = collage(outpic1, outpic2)
#after we collage the two pictures we return the result and then collage the result by the last picture.
flag = collage(output , outpic3)
#then we show our beutiful italian Flag!
show(flag)
