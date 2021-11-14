#Programming a given number of elements, must find nth term, summation, minimum, and average
count=0
summation=0
minimum=0
mean=0

entr = [6,45,22,0,-1] #value of the list
count=len(entr)
count_ter=count-1 #Gets rid of the -1
print("Number of elements in the list are",count_ter)#the number of elements the list will be shown

entr.sort() #sort the list
entr.pop(0) #updates the entry list, removes -1

summation=sum(entr) #Sum all elements in the list
print("The sum of all values in the list is",summation) #value of summation will be shown

minimum = min(entr)
print("The minimum value of all the elements in the list is",minimum) #minimum value of elements will be shown

mean = summation/count_ter
print("The mean value of the elements in the list is",mean) #mean will be shown

# "it looks like I learned how to use git today"

print( "End")
