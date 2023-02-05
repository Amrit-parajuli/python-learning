'''numbers=[1,2,3,4,4,5]
unique= set(numbers)
duplicate= list(unique)
print(duplicate)
it is the short cut way of removing duplicate ...(without any loop)'''




numbers=[1,2,2,3,4,4]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)