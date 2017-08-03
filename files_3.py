number1=int(input("Enter number 1:"))
number2=int(input("Enter number 2:"))
in_file = open("number.txt", "w")
in_file.write(str(number1))
in_file.write(str(number2))
total = number1 +number2
in_file.write(str(total))

in_file.close()

in_file = open("number.txt", "r")

data =in_file.readline()
for each in data:
    print(data)
in_file.close()