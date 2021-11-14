#Programming the largest square of number entered
entry = int(input("enter a number:"))
n=1
if (entry == 0):
    quotient=0
else:
    while(entry-n**2>=1):
            n+=1
quotient = n-1
print("Largest square:",quotient)
print(“End”)

