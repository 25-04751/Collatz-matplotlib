import matplotlib.pyplot as plt

counter = 0

while True:
    try:
        choice = int(input("Pick a number. We'll use Collatz Conjecture on it. "))
        if choice > 0:
            break
        print("Number must be greater than 0.")
    except ValueError:
        print("Are you kidding me?")

numbers = []

numbers.append(choice)

while choice != 1:
    if choice % 2 == 0:
        choice = choice // 2
        counter += 1
        print(f"{choice} | Steps: {counter}")
        numbers.append(choice)
    else:
        choice = choice * 3 + 1
        counter += 1
        print(f"{choice} | Steps: {counter}")
        numbers.append(choice)

plt.plot(numbers)
plt.show()