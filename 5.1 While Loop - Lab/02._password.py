user_name = input()
password = input()
new_password = input()

while new_password != password:
    new_password = input()
print(f"Welcome {user_name}!")