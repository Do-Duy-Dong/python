# Bài 2-5: Famous Quote
print("Albert Einstein once said, “A person who never made a mistake never tried anything new.”")

# Bài 2-6: Famous Quote2
famousPerson = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."
print(f"{famousPerson} once said, “{message}”")

# Bài 2-7: Stripping Names
name = "\t  Albert Einstein  \n"
print(f"Original name: '{name}'")
print(f"Using lstrip(): '{name.lstrip()}'")
print(f"Using rstrip(): '{name.rstrip()}'")
print(f"Using strip(): '{name.strip()}'")

# Bài 2-8: Number Eight
print(5 + 3)
print(16 - 8)
print(4 * 2)
print(64 / 8)

# Bài 6-1: Rental Car
carType = input("What kind of car would you like to rent? ")
print(f"Let me see if I can find you a {carType}.")

# Bài 6-2: Restaurant Seating
numberOfPeople = int(input("How many people are in your group? "))
if number_of_people > 8:
    print("You'll need to wait for a table.")
else:
    print("Your table is ready!")

# Bài 6-3: Multiples of Ten
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

# Bài 6-4: Pizza Toppings
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"Added {topping} to your pizza.")

# Bài 6-5: Movie Tickets
age = int(input("Enter your age: "))
if age < 3:
    price = 0
elif 3 <= age <= 12:
    price = 10
else:
    price = 15
print(f"Your ticket price is ${price}.")
# Bài 6-6. Three Exits - Cách 1: Điều kiện trong while để thoát
topping = ""
while topping != 'quit':
    topping = input("Nhập lớp phủ bánh pizza (hoặc gõ 'quit' để thoát): ")
    if topping != 'quit':
        print(f"Đã thêm lớp phủ {topping} vào bánh pizza.")

# Cách 2: Sử dụng biến 'active'
active = True
while active:
    age = input("Nhập tuổi của bạn (hoặc gõ 'quit' để thoát): ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Vé miễn phí cho bạn.")
        elif 3 <= age <= 12:
            print("Giá vé là 10$.")
        else:
            print("Giá vé là 15$.")

# Cách 3: Sử dụng 'break'
while True:
    topping = input("Nhập lớp phủ bánh pizza (hoặc gõ 'quit' để thoát): ")
    if topping == 'quit':
        break
    print(f"Đã thêm lớp phủ {topping} vào bánh pizza.")

# Bài 6-7. Infinity
# Đây là một vòng lặp vô hạn, bạn có thể chạy và nhấn Ctrl+C để dừng.
while True:
    print("Vòng lặp vô hạn")
# 7.1
def display_message():
    print("Toi dang hoc ve cac ham trong chuong nay.")

display_message()

# 7.2
def favourite_book(title):
    print("Mot trong nhung cuon sach yeu thich cua toi la " + title + ".")

favourite_book("Alice in Wonderland")

# 7.3
def make_shirt(size, message):
    print("Kich thuoc ao la " + size + " va thong diep tren ao la: " + message + ".")

make_shirt("L", "Python is fun!")
make_shirt(message="Hello World!", size="M")

# 7.4
def make_shirt(size="L", message="I love Python"):
    print("Kich thuoc ao la " + size + " va thong diep tren ao la: " + message + ".")

make_shirt()
make_shirt(size="M")
make_shirt(size="S", message="Thong diep tuy chinh")