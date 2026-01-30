dicts = {
    'name': 2.5,
    "pencil": 0.5,
    "pen": 1.2,
    "ruler": 1.5,
    "eraser": 0.5,
    "writing_pad": 2.5,
    "marker": 2.0,
    "glue": 3.0,
    "calculator": 30.0
}
ans = ""
def get_input():
    global item,ans
    ans = input("Enter the item you want to buy: ")
    item = ans.lower()
    return item
print("welcome to the stationery shop")
print("Items available:")
for item, price in dicts.items():
    print(f"{item}: ${price}")
get_input()
total_price = 0
while ans != "":
    if item in dicts:
        quantity = int(input(f"Enter the quantity of {item} you want to buy: "))
        total_price = float(dicts[item]) * quantity + total_price
print(f"Total price: ${total_price}")
