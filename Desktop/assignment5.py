first = input("Enter one positive number: ")
print(first)
second = input("Enter a second positive number: ")
print(second)
if int(first) < 0 or int(second) < 0:
                 print("You need to enter a POSITIVE number.")
else:
    print("The sum of the numbers you entered is: ", (int(first) + int(second)))
    print("The result of subtracting", second, "from", first, "is", (int(first) - int(second)))
    print("The result of multiplying the numbers you entered is ", (int(first) * int(second)))
    print("The result of dividing", first, "by", second, "is", (int(first)/int(second)))
