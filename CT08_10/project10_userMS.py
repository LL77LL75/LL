import random
def generate_password():
    length = input("enter the password length:\n or go play the password game i guess \n")
    password = ""
    characters = 0
    choices = ["uppercase_letter", "lowercase_letter", "digit", "special_character"]
    if length == "cheat":
        return "you are a cheater\nwatch the full video or diddy will be in your room tonight\nhttps://www.youtube.com/watch?v=H3ynKWEboA8"
    elif not length.isdigit():
        return "Go play the password game if u want to abuse my code >:("
    elif int(length) <= 0:
        return "password length must be a positive integer."
    else:
        if random.randint(1,1000) == 1:
            luck = True
            print("you are very lucky, now use the luck to win the lottery first try.\n then go to https://www.youtube.com/watch?v=H3ynKWEboA8")
        while characters < int(length):
            length = int(length)
            choice = random.choice(choices)
            if choice == "uppercase_letter":
                for i in range(random.randint(1, 4)):
                    uppercase_letter = chr(random.randint(65, 90))
                password += uppercase_letter
                characters += 1
            elif choice == "lowercase_letter":
                for i in range(random.randint(1, 4)):
                    lowercase_letter = chr(random.randint(97, 122))
                password += lowercase_letter
                characters += 1
            elif choice == "digit":
                for i in range(random.randint(1, 4)):
                    digit = chr(random.randint(48, 57))
                password += digit
                characters += 1
            elif choice == "special_character":
                for i in range(random.randint(1, 4)):
                    special_character = chr(random.randint(33, 47))
                password += special_character
                characters += 1
        if luck == True:
                return password + "\nyou are very lucky, now use the luck to win the lottery first try and retire.\n then go to https://www.youtube.com/watch?v=H3ynKWEboA8"
        else:
                return password
print(generate_password())
user_db = {}
def create_user(username, password):
    if username in user_db:
        return "Username already exists. Please choose a different username."
    else:
        user_db[username] = password
        return "User created successfully."
def login(username, password):
    if username in user_db and user_db[username] == password:
        return "Login successful."
    else:
        return "Invalid username or password."
create_user(input("enter a username:\n"),generate_password())
login(input("enter your username:\n"), input("enter your password:\n"))                            