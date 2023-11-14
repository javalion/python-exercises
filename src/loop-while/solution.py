# Loop While

x = int(input("Enter a number between 1 to 10: "))

if x < 1 or x > 10:
    print("Invalid number")
else:
    num = 1
    while num <= x:
        print(num)
        num += 1


