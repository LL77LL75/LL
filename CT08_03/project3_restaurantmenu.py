menu = {
    "air" : 0,
    "cheeseburger": 12,
    "sturgeon":67,
    "soup":10,
    "pig":250,
    "" :0
}
for i in menu:
    print(i)
ans = " "
items = []
price = 0
while ans != "":
    ans = input("food ")
    items.append(ans)

for i in items:
    val = menu[i]
    price+=val

print(f"the total price of what you bought is ${price}")