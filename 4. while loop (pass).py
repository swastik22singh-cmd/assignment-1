correct_password = "python123"

while True:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("your password is correct")
        break
    else:
        print("your password is incorrect")
