
#This code converts Supermodel to variant (according the variables that user gives as variant variables) and computes minimal cut set for the variant 
import cutsets 
import string
supermodel = [("TOP", "Or", ["a", "G1"]),
      ("G1", "And", ["G2", "G3"]),
      ("G2", "Or", ["b", "c"]),
      ("G3", "Or", ["d", "e"])]
print("This program computes minimal cut sets for the a variant of a determined supermodel")
print("If you want to change the supermodel, please changed it inside code")
variant = input("Pleas enter the variant variables a...z seperated with comma without any space between variables (FOR EXAMPLE: a,b,c)")
parts = variant.split(',')
print (supermodel [0])
print(type(supermodel [0]))
#supermodel_parts=supermodel.split(',')
len_supermodel= len(supermodel)
print(len_supermodel)
lower = list(string.ascii_lowercase)  
print(lower) 
variant1=supermodel
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


for i in range (len(variant1), 0, -1):
  x=variant1[i-1]
  x1=x[2][0]
  x2=x[2][1]
  if (x1 == 0 and x2 == 0):
      gate= x[0]
      for j in range (0, len(variant1)):
         y=variant1[j]
         y1=y[2][0]
         y2=y[2][1]
         if (gate == y1):
            variant1[j][2][0]=0
         if (gate == y2):
            variant[j][2][1]=0



list1=list(supermodel [0])
for x in range (0, len(supermodel)):
   print(x)
for i in parts:
   print(i)
cs = cutsets.mocus (supermodel)
print (cs)

