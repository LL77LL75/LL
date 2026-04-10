import os
filepath = os.getcwd()
with open('encrypted_note.txt',"r") as file:
    content = file.read()
word = ""
wordA=""
nexte = True
code = ""
for i in content:
    if nexte:
        code += i
    nexte = False
    if i.isalpha():
        if i.isupper():
            word+=i.lower()
        else:
            word += i
    elif i == " ":
        word = word + i
        nexte = True
print(word)
print(wordA)
print(code)
# with open("hidden_message.txt","w") as f:
#     edoc = ""
#     for i in code:
#         edoc = i.lower + edoc
#     f.write(edoc)
with open("hidden_message.txt", "w") as f:
    f.write(code[::-1])