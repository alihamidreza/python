# a program for calculate the size of pizza

# get the shoa
shoa = input('inter the shoa of your pizza : ')

# should enter integer or float type
if (type(shoa) == int or type(shoa) == float):
    # calculate the radius**2
    r2 = shoa * shoa
    pi = 3.14 # everyone knows it :)
    # calculate size of pizza
    result = pi * r2

    # print outpot
    print (result)
else:
    print ('your input value should integer or float')     

