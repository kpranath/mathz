#Made By Lakshya On 31/3/19

import xlrd
from PIL import Image
from random import shuffle
from itertools import permutations, combinations

#Global
data = []
pixels = []
key=[i for i in range(256)]
shuffle(key)
"""This shuffles the array with value range 0-255"""
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','.','@']
#perm=set()
rowsheet=0
colsheet=0
#UDF

def Read():
    """Reads Values from excel sheet and stores it in a 2D array"""
    workbook = xlrd.open_workbook("C:\\Users\\Lenovo\\PycharmProjects\\Mathshz\\Stud_Details.xlsx")
    sheet = workbook.sheet_by_index(0)
    global rowsheet
    global colsheet
    rowsheet=sheet.nrows-1
    colsheet=sheet.ncols

    for i in range(1,sheet.nrows):
        temp = []
        for j in range(0,sheet.ncols):
            cell=sheet.cell_value(i,j)
            if type(cell) == float:
                cell=int(cell)
            temp.append(str(cell))
        data.append(temp)
    print(data)

#generate triplet
def generate_triplet():
    """This generates the triplets. this has 1 crore itemsets. so dont rint this."""
    C = []
    for comb in combinations(key,3):
        C.append(comb)
    return C
'''
def Encode1():
    """Encodes details of each student into an array of colours"""
    stud=[]

    for i in range(0,rowsheet):
        temp = []
        for j in range(0,8,4):
            temp.append(perm[len(data[i][0])])
            print(temp[j])
            temp.append(perm[len(data[i][3])])
            print(temp[j+1])
            temp.append(perm[len(data[i][6])])
            print(temp[j+2])
            temp.append(perm[len(data[i][7])])
            print(temp[j+3])
        stud.append(temp)
        print(stud[i])
'''

def Encode():
    """Encodes details of each student into an array of colours"""
    stud=[]
    for i in range(rowsheet):
        temp=[]
        for j in range(colsheet):
            for k in range(len(data[i][j])):
                a=ord(data[i][j][k])
                temp.append(perm[a])
        stud.append(temp)
        print(stud[i])



def OpenImage():
    im = Image.open("C:\\Users\\Lakshya Sharma\\Desktop\\ucd.png")
    x=y=0
    check = False
    while True:
        try:
            im.getpixel((x,y))
            check = False
        except IndexError:
            if check:
                break
            x+=1
            y=0
            check = True



#Main
Read()
perm=generate_triplet()
Encode()


