class User:
    def login(self):
        print("User logged in")

class Admin(User):
    def login(self):
        print("Admin logged in with extra security")

class Guest(User):
    def login(self):
        print("Guest logged in with limited access")

for u in (Admin(), Guest()):
    u.login()