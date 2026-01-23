wallet = int(input("How much money do you have? "))
menu = {
    "air" : 0,
    "cheeseburger": 12,
    "sturgeon":67,
    "soup":10,
    "pig":250,
    "" :0
}
for i in menu:
    print(f"{i:20} ${menu[i]}")
ans = " "
items = []
price = 0
while ans != "":
    ans = input("food ")
    if "remove" in ans:
        rem = ans[6:]
        print("your current items are: ")
        for i in items:
            print(i)
        for i in items:
            if i == rem:
                items.remove(i)
        print(f"{rem} removed")
    else:

        if input("are you sure? ")) == "y":
             print(ans + " costs $" + str(menu[ans]))
             items.append(ans)

for i in items:
    val = menu[i]
    price+=val
print("_" * 50)
print(f"the total price of what you bought is ${price}")