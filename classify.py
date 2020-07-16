import shutil
smile = open("SMILE_list.txt")
for line in smile:
    line = line.strip()
    try:
        shutil.move("C:\\Users\\kirut\\Documents\\smile_rec\\lfwcrop_color\\faces\\"+line[:-3]+"ppm","C:\\Users\\kirut\\Documents\\smile_rec\\SMILE_list\\"+line[:-3]+"ppm")
    except :
        None
non_smile = open("NON-SMILE_list.txt")
for line in non_smile:
    line = line.strip()
    #print(line)
    try:
        shutil.move("C:\\Users\\kirut\\Documents\\smile_rec\\lfwcrop_color\\faces\\"+line[:-3]+"ppm","C:\\Users\\kirut\\Documents\\smile_rec\\NON-SMILE_list\\"+line[:-3]+"ppm")
    except :
        None