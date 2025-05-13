import random

generate = lambda count: [random.randint(0, 9) for ran_num in range(count)]
display = lambda numbers: [print(num) for num in numbers]

random_numbers = generate(10)
display(random_numbers)
