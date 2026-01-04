filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        words = f.read().split()
        print("Word count:", len(words))
except FileNotFoundError:
    print("Error: File not found")
