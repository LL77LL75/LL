def casear_shift_character(char,key,mode):
    ascii_value = ord(char)
    ascii_value -=32
    ascii_value %= 95
    if mode == "e":
        ascii_value+=key
    elif mode == "d":
        ascii_value-=key
    return chr(ascii_value+32)
def casear_shift_sentance(sentance,key,mode):
    answer = ""
    for i in sentance:
        answer+=casear_shift_character(i,key,mode)
    return answer
print(casear_shift_sentance(input("Enter a sentance: "),int(input("Enter a key: ")),input("Enter a mode (encrypt/decrypt): ")))
def encrypted(sentance,key,mode):
    if sentance:
        print(casear_shift_sentance(sentance,key,mode))
    else:
         print("No sentance entered")
def casear_shift_file(input_file,key,mode):
    import os
    filepath = os.getcwd()
    with open(input_file,"r") as file:
        content = file.read()
    casear_shift_character()
casear_shift_file(input("enter a link"),67,"encrypt")