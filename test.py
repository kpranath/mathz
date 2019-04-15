import time
import xlrd
#from PIL import Image
import numpy
from random import shuffle
from itertools import combinations
from itertools import permutations

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
    workbook = xlrd.open_workbook("C:\\Users\\Lenovo\\Desktop\\mathz\\Stud_Details.xlsx")
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

def Encode():
    """Encodes details of each student into an array of colours"""

    print("Student Details are being Encoded\n")
    global stud
    combination = []
    for comb in combinations(key, 3):
        combination.append(comb)
    shuffle(combination)
    print(len(combination))
    for i in range(rowsheet):
        temp = []
        for j in range(colsheet):
            for k in range(len(data[i][j])):
                a = ord(data[i][j][k])
                temp.append(combination[a])
                temp+=([combination[a]]*5)  #this line extends generated colors...
        shuffle(temp)
        stud.append(temp)
        print(stud)


    print("Student Data has been Encoded\n")
    #print(stud)
    print(len(stud[0]))
    print(len(stud[1]))
    print(len(stud[2]))



#main
Read()
Encode()


