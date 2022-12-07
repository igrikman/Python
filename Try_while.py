file = open("Data/text.txt", "w")
file.write("New Sum\n")
file.close()

x1 = 0
while x1 == 0:
    try:
        a = int(input("Number a :"))
        x1 = a
    except ValueError:
        print("Number!")

x2 = 0
while x2 == 0:
    try:
        b = int(input("Number b :"))
        x2 = b
    except ValueError:
        print("Number!")

f = a + b

try:
    with open("Data/text.txt", "a", encoding="utf-8") as file:
        file.write("Sum a + b = ")
        file.write(str(f))
except FileNotFoundError:
    print("File Not Found")
# finally:
#     print(f)

try:
    with open("Data/text.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File Not Found")