import matplotlib.pyplot as plt

import Progression



another_progression = Progression.Progression()

numbers = []

for value in another_progression:
    numbers.append(value)
    if len(numbers) == 500:
        break



first_progression = Progression.Progression()






count = 0
for value in first_progression:
    count += 1
    print(value)
    if count == 100:
        break


second_progression = Progression.Progression()

for n in range(100):
    print(next(second_progression))

r_value = float(input('Please enter an r value between -1 and 1'))

geometric_progression = Progression.GeometricProgression(r_value)

current_sum = 0
expected_sum = 1 / (1 - r_value)

while abs(expected_sum - current_sum) > .000001:
    current_sum += next(geometric_progression)
    print(current_sum)


fib = Progression.FibonacciProgression()
next(fib) # progresses past the initial 0

digit_count = {}
for digit in range(1, 10):
    digit_count[digit] = 0

for value in range(500):
    fib_value = next(fib)

    string_fib_value = str(fib_value)
    leading_digit = int(string_fib_value[0])

    digit_count[leading_digit] += 1

print(digit_count)

plt.plot(list(digit_count.keys()), list(digit_count.values()))
plt.show()