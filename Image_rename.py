import os

Path_From = "../min/"
Name = "min_"


def changeName(path, cName):
    i = 1
    for filename in os.listdir(path):
        print(path + filename, "=>", path + str(cName) + str(i) + ".jpg")
        os.rename(path + filename, path + str(cName) + str(i) + ".jpg")
        i += 1


changeName(Path_From, Name)
