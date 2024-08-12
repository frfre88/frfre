import random

# انتخاب یک عدد تصادفی بین 1 تا 100
number_to_guess = random.randint(1, 100)

# لیستی برای ذخیره حدس‌ها
guesses = []

print("yek adad beyn 1 ta 100 hads bezanid!")

while True:
    # دریافت حدس کاربر و اضافه کردن آن به لیست
    guess = int(input("hads shoma: "))
    guesses.append(guess)

    # بررسی حدس کاربر
    if guess < number_to_guess:
        print("adad bozorrgtar vared konid!: ")
    elif guess > number_to_guess:
        print("adad kochik tar vared konid!: ")
    else:
        print(f"tabrik adad dorost bood!!: {number_to_guess} .")
        break

# نمایش تاریخچه حدس‌ها
print("hads haye shoma:", guesses)

