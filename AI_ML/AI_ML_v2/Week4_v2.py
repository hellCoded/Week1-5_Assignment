import numpy as np

def main():
    filename = "numbers.txt"

    try:
        count = int(input("Enter how many numbers you want to store: "))
    except ValueError:
        print("⚠️ Please enter a valid integer.")
        return

    with open(filename, "w") as file:
        for i in range(1, count + 1):
            try:
                number = int(input(f"Enter number {i}: "))
                file.write(f"{number}\n")
            except ValueError:
                print("⚠️ Invalid input, storing 0 instead.")
                file.write("0\n")

    try:
        data = np.loadtxt(filename)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    print("\n📊 Analysis Report")
    print("-" * 30)
    print(f"Numbers from file → {data}")
    print(f"Sum   → {np.sum(data)}")
    print(f"Mean  → {np.mean(data):.2f}")
    print(f"Max   → {np.max(data)}")
    print(f"Min   → {np.min(data)}")

if __name__ == "__main__":
    main()
