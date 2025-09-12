import numpy as np

with open("numbers.txt", "w") as file:
    counter = int(input("Enter an range of Numbers will be in Numbers.txt : "))
    for i in range(1, counter + 1):
        number = int(input(f"Enter number {i} place: "))
        file.write(f"{number}")

data = np.loadtxt("numbers.txt", delimiter=" ")
print(f"Numbers from file: {data}")
print(f"Sum: {np.sum(data)}")
print(f"Mean: {np.mean(data)}")
print(f"Max: {np.max(data)}")

