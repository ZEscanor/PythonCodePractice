#Z Amusa
#yamusa2
#CS 111
#Project 4
#Monday 5:00-5:50
#this project prompts the user for a number then either embeds a code or extracts a code from a sound file and saves it
#this functio takes a string inputed by user and embeds it into a sound file.
def embed():
#prompt a user to pick a file
 fname = pickAFile()
 #make a sound from the selected file
 s1 = makeSound(fname)
 #request a string to be embeded into that sound
 word = requestString("What do you want to embed into the sound?")
 #make an empty sound, get samples from original sound and empty sound
 s2 = makeEmptySound(getLength(s1))
 samples1 = getSamples(s1)
 samples2 = getSamples(s2)
 #loop over our samples to "smooth" out the values, making sure they are modded by the max ASCII value 128
 for i in range(0, getLength(s1), 1):
  value = getSampleValue(samples1[i])
  valueS = value % 128
  #set value in our empty sound to oringinal sample value - the value modded by 128
  setSampleValue(samples2[i], value - valueS)
#next we get the length of the word inputed by user and loop every character into our sound
 for i in range(0, len(word) , 1):
  x = ord(word[i])
  value2 = getSampleValue(samples2[i])+ x
  setSampleValue(samples2[i],value2)
 #we can explore our new sound and save it to a file
 explore(s2)
 #prompt user for a file to save our "embedded" sound in
 file = pickAFile()
 #save it to the file user picked
 writeSoundTo(s2,file)
 #filename printed for reference
 stra = str("Your embedded message in your sound has been saved to:")
 print(stra + file)  
# this function extracts the message previously embedded and we use showinformation later to show it. Takes 2 parameters our original sound amd a "main" sound that we will return and change with the loop
def extract(s4,s5):
#loop over our sound, getting length value of original sound.
 for i in range(0, getLength(s4), 1):
  #get the values of both our orignial sound and the sound we will change.
  value3 = getSampleValue(sample4[i])
  #set the new sound value to the previous value modded by 128, this should leave just the ASCII character values. 
  value4 = value3 % 128
  #if modded value is not equal to 0 it tells our program to keep going, getting every character.
  if(value4 != 0):  
   s5 = s5+chr(value4)
  #if our modded value is equal to 0, this tells our program to stop and return the final value, in this case it will return your previously embedded message.
  if(value4 == 0):
  #as previously stated this will return our "main" sound
   return s5
#prompt user to enter 1 or 2. 1 will embed , 2 will extract.    
l = requestIntegerInRange("Press 1 to embed, Press 2 to extract",1,2)
#if l is equal to 1 embed our message.
if (l == 1):
 embed()
#if l is equal to 2 extract our message and show it in a text box.
if (l == 2):
 fname2 = pickAFile()
 s4 = makeSound(fname2)

 sample4 = getSamples(s4)
 s5 = ""
 
 s6 = extract(s4,s5)
 showInformation(s6)
 