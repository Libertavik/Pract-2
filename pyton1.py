age = int(input("Введите возраст"))
name = input("Введите имя")

print(f"Кабан {age}")
#print(f"Кабан {age}")

# if age > 20:
#     print("Молодой кабан {age}")
# elif age < 20:
#     print("Старый кабан {age}")


# for i in name:
#     print(f"Молодой кабан {i}")

i = 0
while i <= age:
    print(f"Молодой кабан {i}")
    i += 1