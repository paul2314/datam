i=int(input("Enter  i:  "))
j=int(input("Enter  j:  ")) 
print("Cluster  Size:",  i**2+i*j+j**2) 
mesh=[['.'  for  z  in  range(10*j)]for  k  in  range(10*i)] 
mesh[5+i][5+j]='o' 
mesh[5+i-j][5+j+i+j]='z' 
mesh[5+i+j][5+j-i-j]='z' 
mesh[5+i-i-j][5+j-j]='y' 
mesh[5+i+i+j][5+j+j]='y'
mesh[5+i-i-j][5+j+i]='x' 
mesh[5+i+i+j][5+j-i]='x' 
mesh[5+i-i][5+j-i-j]='x' 
mesh[5+i+i][5+j+i+j]='x' 
for  m  in  mesh: 
	print(m) 