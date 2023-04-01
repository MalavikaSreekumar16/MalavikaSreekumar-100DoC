string=input("enter values separated by commas to find sum:")
values=string.split(",")
my_array=[]
for val in values:
    my_array.append(float(val))

    sum=0
for items in my_array:
    sum+=items
print("sum of values is ",sum)
