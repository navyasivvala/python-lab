n = 4

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
#output
   #*
  #* *
 #*   *
#*     *
 #*   *
  #* *
   #*
        
