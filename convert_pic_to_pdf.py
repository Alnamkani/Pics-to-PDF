from PIL import Image
import os, glob
def make_pdf(file, PATH): #this function makes and saves the dpf
    image1 = Image.open(file) 
    im1 = image1.convert('RGB') #convert to pdf
    im1.save(PATH) #save the file in the PATH provided 

def which_pic(files, PATH): #this function makes the user choose which file is the picture 
    print("Choose a file: ")
    for i in range(len(files)):
      print(str(i + 1) +') ' + files[i])
    file_index = int(input("Which One (if noun enter 0): "))
    if (file_index == 0):
        exit()
    else:
        make_pdf(files[file_index - 1],PATH)

files = [] 
PATH = 'C:\\Users\\ #username# \\Pictures\\python output' #add your username between the two # signs
pic_name = (input("Enter the name of the Picture: ")).strip() #enter the name of the file that has the picture
PATH = PATH + "\\" + pic_name + ".pdf"
pic_name = pic_name.upper()
for r,d,f in os.walk("D:\\"): #walk through the files and if the name match add the name to the files list
    try:
        files = files + (glob.glob(str(r) + "\\" + pic_name + ".*"))
    except:        
        continue
num_files = len(files)

if (num_files == 0):
    print("Couldn't find the picture")
    exit()
elif (num_files > 1):
    which_pic(files, PATH)
else:
    make_pdf(files[0], PATH)
print("Your pdf is saved as: " + PATH)




