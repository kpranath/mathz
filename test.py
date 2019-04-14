from random import shuffle
from itertools import permutations

x=[[i] for i in range(256)]
shuffle(x)
#print(x)
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','.','@']

#generate triplet
def generate_triplet(x):
    pe=permutations(x,3)
    return pe


#assigning array to triplet
#def asstotrip(pe,A):



#main
#perm=generate_triplet(x)
print(ord(''))


