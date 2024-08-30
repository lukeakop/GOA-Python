def func(number):
    lst = []
    
    for num in number:
        if num % 2 == 0:
            
            lst.append(num)
    return lst
    

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        
