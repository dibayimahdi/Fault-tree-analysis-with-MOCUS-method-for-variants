
#This code converts Supermodel to variant (according the variables that user gives as variant variables) and computes minimal cut set for the variant 
import cutsets 
import string
from copy import deepcopy

supermodel = [("TOP", "Or", ["a", "G1"]),
      ("G1", "And", ["G2", "G3"]),
      ("G2", "Or", ["b", "c"]),
      ("G3", "Or", ["d", "e"])]

print("This program computes minimal cut sets for the a variant of a determined supermodel")
print("If you want to change the supermodel, please changed it inside the code")
variant = input("Pleas enter the variant variables (a..z), seperated with comma without any space between variables (FOR EXAMPLE: a,b,c)\n")
parts = variant.split(',')
len_supermodel= len(supermodel)
lower = list(string.ascii_lowercase)  
variant1 = deepcopy(supermodel)
for i in range (0, len_supermodel):
   x=supermodel[i]
   print(x)
   print(type(x))
   x1=x[2][0]
   x2=x[2][1]
   if ((x1 in lower) and (x1 not in parts)):
      variant1[i][2][0]=0  
   if ((x2 in lower) and (x2 not in parts)):
       variant1[i][2][1]=0      

# Deleting elements with two zero 
for i in range (len(variant1), 0, -1):
  x=variant1[i-1]
  x1=x[2][0]
  x2=x[2][1]
  if (x1 == 0 and x2 == 0):
      gate= x[0]
      for j in range (0, len(variant1)-1):
         y=variant1[j]
         y1=y[2][0]
         y2=y[2][1]
         if (gate == y1):
            variant1[j][2][0]=0
         if (gate == y2):
            variant1[j][2][1]=0
      p=i-1
      poped= variant1.pop(p)

# Deleting elements with one zero 
i=0
while i< len(variant1):     
      x=variant1[i]
      x1=x[2][0]
      x2=x[2][1]
      if (x1 == 0 or x2 == 0):
         gate1= x[0]
         if(x1==0):
             gate=x2
         else: 
             gate=x1    
         poped= variant1.pop(i)
         for j in range (i, len(variant1)):
            y=variant1[j]
            y1=y[2][0]
            y2=y[2][1]
            if(y[0]==gate):
               print(type(variant1[j]))
               varlist1=list(variant1[j])
               varlist1[0]=gate1
               variant1[j]=tuple(varlist1)
            i=i+1
      i=i+1    
           
#Printing Minimal Cut Set for Supermodel and variant 
print("Minimal Cut Sets for Supermodel is:")
cs = cutsets.mocus (supermodel)
print (cs)
print("Minimal Cut Sets for variant is:")
cs = cutsets.mocus (variant1)
print (cs)


