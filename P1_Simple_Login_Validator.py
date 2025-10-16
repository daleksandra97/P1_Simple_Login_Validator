username = "admin"
password = "secret123"
account_locked = True
ToS_accepted = False  

if not ToS_accepted:
    print("Login failed: Terms of Service (ToS) not accepted")
elif username != "admin" or password != "secret123":
    print("Login failed: Incorrect username or password!")
elif account_locked:
    print("Login failed: Account locked!")
else:
    print("Login successful!")

