a = [-33, -10, -25, -58, -29, -9, 14, 38, 44, -50, -62]

def oddest(a):
    n_lst = []
    
    for i in a:
        if i % 2 != 0:
            n_lst.append(i)
    print(n_lst)
    for val in n_lst:
        if (abs(val)//2)%2 ==0:
           n_lst.remove(val)
    print(n_lst)    # else:
    #     return None

print(oddest(a))