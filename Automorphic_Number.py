n = int(input()) 
m = len(str(n))
a = n**2  
b = a%pow(10,m)  
if b == n:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number") 