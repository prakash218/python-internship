#Task 1

a = {'a':1}
b = {'b':2}

merged = {**a,**b}

print(merged)


#Task 2
dictionary = merged.copy()
dictionary.pop('a')

print(dictionary)

#Task 3
list1 = [1,2,3,4]
list2 = [5,6,7,8]

dictionary = dict(zip(list1,list2))

print(dictionary)



#Task 4
set1 = set(list1)

print(len(set1))


#Task 5
set1 = {1,2,3,4,5,6}
set2 = {1,3,5,7,9,11}

set1.difference_update(set2)

print(set1)

