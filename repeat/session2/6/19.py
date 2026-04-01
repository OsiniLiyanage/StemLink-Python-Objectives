password =int(input("Enter ur password: "))

if len(password) < 6:
    print("wek password")
elif len(password) <=10:
    print("Medium password")
else:
    print("Strong passeord")