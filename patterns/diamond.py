n = int(input("Enter N:"))

# Upper half
for i in range(1, n + 1):
    for j in range(n-i):
        print("", end=" ")
    for j in range(2*i-1):
         print("*",end="")
    print()

# Lower half
for i in range(n, 0, -1):
   for j in range(n-i):
        print("", end=" ")
   for j in range(2*i-1):
        print("*",end="")  
   print()
#output
#Enter N:5
    #*
   #***
  #*****
 #*******
#*********
#*********
 #*******
  #*****
   #***
    #*   
