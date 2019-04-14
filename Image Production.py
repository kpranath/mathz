# Made By Lakshya On 31/3/19

import time
import xlrd
from PIL import Image
import numpy
from random import shuffle
from itertools import combinations

# Global
data = []
pixels = []
stud=[]
rowpixels = 0
colpixels = 0
rowsheet = 0
colsheet = 0
objects = 0
visited = numpy.array([[0] * colpixels] * rowpixels)
key = [i for i in range(256)]
shuffle(key)  # This shuffles the array with value range 0-255
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
     'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '@']



# UDF


def Read():
    """Reads Values from excel sheet and stores it in a 2D array"""

    print("\nReading Data from Excel Sheet\n")
    workbook = xlrd.open_workbook("C:\\Users\\Lakshya Sharma\\Documents\\Stud_Details.xlsx")
    sheet = workbook.sheet_by_index(0)
    global rowsheet
    global colsheet
    rowsheet = sheet.nrows - 1
    colsheet = sheet.ncols

    for i in range(1, sheet.nrows):
        temp = []
        for j in range(0, sheet.ncols):
            cell = sheet.cell_value(i, j)
            if type(cell) == float:
                cell = int(cell)
            temp.append(str(cell))
        data.append(temp)
    print("Data has been read from the Excel Sheet\n")


def ImageProcessing():
    """Opens an image and identifies all the pixels to get a 2d array of pixels of an image"""

    print("Starting Image Reading\n")
    im = Image.open("C:\\Users\\Lakshya Sharma\\Desktop\\U.png")
    x = y = 0
    check = False
    temp = []
    while True:
        try:
            temp.append(im.getpixel((x, y)))
            check = False
            x += 1
        except IndexError:
            if check:
                global rowpixels
                global colpixels
                rowpixels = y
                colpixels = temp_x
                break
            temp_x = x
            y += 1
            x = 0
            check = True
    for i in range(rowpixels):
        temp1 = []
        for j in range(colpixels):
            index = i * rowpixels + j
            temp1.append(temp[index])
        pixels.append(temp1)

    print("Image has been stored\n")


def Object_Identification():
    """Identifies Objects in the image"""

    print("Object Identification is starting\n")
    global visited
    visited = numpy.array([[0] * colpixels] * rowpixels)
    check = True
    i = 0
    j = 0
    white = (255, 255, 255, 255)
    black = (0, 0, 0, 255)
    obj = 1
    used = []
    temp = 0

    def Check():
        for i in range(rowpixels):
            for j in range(colpixels):
                if visited[i][j] == 0:
                    return True
        return False

    while check:

        # Case of just going through blacks
        if pixels[i][j] == black:
            visited[i][j] = -1
            if j + 1 == colpixels:
                if i + 1 == rowpixels:
                    check = Check()
                    continue
                else:
                    j = 0
                    i = i+1
                    continue
            else:
                j = j + 1
                continue

        # Case of Object Identification
        if pixels[i][j] == white and visited[i][j] == 0:
            for k in range(j, colpixels):
                if pixels[i][k] == white and pixels[i-1][k] == white:
                    temp = k + 1
                    obj = visited[i-1][k]
                    break
                if pixels[i][k] == black:
                    if pixels[i][j-1] == white and visited[i][j-1] != 0:
                        temp = k
                        obj = visited[i][j-1]
                        break
                    else:
                        temp = k
                        obj = 1
                        while obj in used:
                            obj += 1
                        used.append(obj)
                        break
            for k in range(j, temp):
                visited[i][k] = obj
            j = temp
    #Finding No. of Objects after Completion
    objects = 1
    while objects in used:
        objects += 1
    objects -= 1
    print(objects, "Objects in the image have been identified\n")

def TestImage():
    """Just a test case"""

    white = (255, 255, 255)
    black = (0, 0, 0)
    im = Image.open("C:\\Users\\Lakshya Sharma\\Desktop\\U.png")
    for i in range(20):
        for j in range(20):
            if i in range(2, 5) and j in range(4, 7):
                im.putpixel((i, j), white)
            elif i in range(7,11) and j in range(3, 9):
                im.putpixel((i, j), white)
            elif i in range(14, 17) and j in range(2, 12):
                im.putpixel((i, j), white)
            else:
                im.putpixel((i, j), black)
    im.save("C:\\Users\\Lakshya Sharma\\Desktop\\U.png")


def Encode():
    """Encodes details of each student into an array of colours"""

    print("Student Details are being Encoded\n")
    global stud
    combination = []
    for comb in combinations(key, 3):
        combination.append(comb)
    
    for i in range(rowsheet):
        temp=[]
        for j in range(colsheet):
            for k in range(len(data[i][j])):
                a=ord(data[i][j][k])
                temp.append(combination[a])
        stud.append(temp)
    print("Student Data has been Encoded\n")
        
        
def Colour():
    """Colours the picture according to the student"""

    print("Images are being created for each student\n")
    for i in range(rowsheet):
        im = Image.open("C:\\Users\\Lakshya Sharma\\Desktop\\U.png")
        for x in range(rowpixels):
            for y in range(colpixels):
                if visited[y][x]!=-1:
                    im.putpixel((x,y),stud[i][(visited[y,x])%len(stud[i])])
        im.save("C:\\Users\\Lakshya Sharma\\Desktop\\U"+str(i+1)+".png")
    print("Images have been saved\n")


# Main

start = time.time()
Read()
#TestImage()
ImageProcessing()
Object_Identification()
Encode()
Colour()
end = time.time()
print("Time Taken : ",end-start," seconds\n")
