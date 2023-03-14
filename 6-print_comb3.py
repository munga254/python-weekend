my_list=[]
for z in range(0,100):
    my_list.append(z)

# Using nested for loops to generate all combinations
for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        print( my_list[j])