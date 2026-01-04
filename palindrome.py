s = input("Enter a string: ")

cleaned = s.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
