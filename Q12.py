list1 = [5,10,15,20,25,50,20]
x=20
if x in list1:
    y=list1.index(x)
    print("yes it is there in the list at this position :",y)
    list1.remove(x)
    list1.insert(y,200)
print("now the updated list as per question: \n",list1)

print("now the updated again list as per question: \n",list1)
