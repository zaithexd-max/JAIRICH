#doubles = [expression for value in iterable if condition]
#doubles = [x*2 for x in range(1,11)]
#triples = [y*3 for y in range(1,11)]
#square =  [z*z for z in range(1,11)]
#print(doubles)
#print(triples)
#print(square)
#fruits = ["apple","orange","banana","coconut"]
#fruit_chars = [fruit[0] for fruit in fruits]
#rint(fruit_chars)
#numbers = [1,-2,3,-4,-5,-6,8,9]
#positive_nums = [num for num in numbers #if num>=0]
#print(positive_nums)
#negative_nums = [num for num in numbers #if num<=0]
#print(negative_nums)
#odd_nums = [num for num in numbers if num%2 !=0]
#print(odd_nums)
grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade > 60]
print(passing_grades)