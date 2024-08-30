def func(strings):
    lst = []

    first_input = input("Enter Your User! ")

    for word in strings:
        if len(first_input) % 2 == 0:
            lst.append(word)
        return lst
    
print(func("Lukaakofiani"))

    