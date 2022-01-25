#QUESTION 6
p=int(input("ENTER FIRST SIDE OF TRIANGLE"))
q=int(input("ENTER SECOND SIDE OF TRIANGLE"))
r=int(input("ENTER THIRD SIDE OF TRIANGLE"))
if((p+q)>r and (q+r)>p and (r+p)>q and p>0 and q>0 and r>0): #All sides should be positive and sum of two sides should be greater than third side
    print("Yes")
else:
    print("No")
