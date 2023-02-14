import os, shutil

source = "C:/Users/adils/Downloads"
dest = "C:/Users/adils/Desktop"

listOfFiles = os.listdir(source);
print(listOfFiles);

for file in listOfFiles:
    root, ext = os.path.splitext(file)
    if ext == "":
        continue
    elif ext in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = source + "/" + file
        path2 = dest + "/Document Files/"
        path3 = dest + "/Document Files/" + file
        if(os.path.exists(path2)):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
        print(file + " has been moved")