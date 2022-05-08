# Created by Admin at 5/8/2022
for number in [0, 1, 2, 3, 4]:
    print(number)

for number in range(5):
    print(number)

list(range(10))
list(range(3, 8))
list(range(-10, 10, 4))

surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):
    print(position, surnames[position])

for surname in surnames:
    print(surname)

for position, surname in enumerate(surnames):
    print(position, surname)

people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
nationalities = ['Poland', 'India', 'South Africa', 'England']

for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

for person, age in zip(people, ages):
    print(person, age)

for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)

for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)

n = 39
remainders = []
while n > 0:
    remainder = n % 2  # remainder of division by 2
    remainders.insert(0, remainder)  # we keep track of remainders
    n //= 2  # we divide n by 2
print(remainders)
