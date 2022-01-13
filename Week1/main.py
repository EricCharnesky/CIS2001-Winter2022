import random

value_a = int(input("enter the first number"))
value_b = int(input("enter the second number"))
value_c = int(input("enter the third number"))

print(value_b + value_a + value_c)

list_of_numbers = []

for number in range(100):
    list_of_numbers.append(random.randint(1,100)) # inclusive of both values

minimum_value = list_of_numbers[0]
maximum_value = list_of_numbers[0]
total = list_of_numbers[0]
for index in range(1, len(list_of_numbers)):
    if list_of_numbers[index] < minimum_value:
        minimum_value = list_of_numbers[index]
    if list_of_numbers[index] > maximum_value:
        maximum_value = list_of_numbers[index]
    total += list_of_numbers[index]

for number in list_of_numbers:
    if number< minimum_value:
        minimum_value = list_of_numbers[index]
    if number > maximum_value:
        maximum_value = list_of_numbers[index]
    total += number

average = total / len(list_of_numbers)

print("Min value:", minimum_value)
print("Max value:", maximum_value)
print("average:", average)

# book
# number formatting from https://www.bing.com/search?q=python+string+format+number+decimal+places&cvid=c321953d925a4c3f99ca309d2a4eff65&aqs=edge.0.0j69i57.8149j0j1&pglt=43&FORM=ANNTA1&PC=W000
print("Min: {:d} - max: {:d} - average: {:.2f}".format(
    min(list_of_numbers), max(list_of_numbers), sum(list_of_numbers) / len(list_of_numbers)))

print("Min:", min(list_of_numbers), "- max:", max(list_of_numbers), "- average: ",
      sum(list_of_numbers) / len(list_of_numbers))

gradebook = {}

gradebook['Eric'] = 'A' # keys have to be unique
gradebook['Jeb'] = 'A' # will add new value if the key doesn't exist
gradebook['Eric'] = 'B' # changes the value

name = input("Enter the name of someone to get their grade")

if name in gradebook:
    print(gradebook[name])
else:
    print("they are not in the gradebook, let's add them, what is their grade?")
    grade = input()
    gradebook[name.lower()] = grade

for key in gradebook:
    grade = gradebook[key]
    gradebook.pop(key)
    gradebook[key.lower()] = grade

print(gradebook)
