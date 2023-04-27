def max_num(a, b, c):   
    return max ([a,b,c])       

print(max_num(3,18,9))        

def multi_list(lst):
    if len(lst) == 0:
        return 0 

    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod

result = multi_list([2, 3, 4, 5])
print(result)

def rev_string(string):
    return string[::-1]

print(rev_string("reverse"))

def num_within(a,b,x):
    return x in range (a,b+1)

print(num_within(10,15,20))

def pascal(n):
    row = [1]

    for i in range(n):
        print(' '.join(str(x) for x in row))

        next_row = [1]

        for j in range(len(row)-1):
            next_row.append(row[j] + row[j+1])

        next_row.append(1)

        row = next_row

pascal(1)
'''
output:
1
'''

pascal(5)
'''
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''                                                              