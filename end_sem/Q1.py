customer_spending = {
    "Alice": 950,
    "Bob": 1200,
    "Charlie": 500,
    "Diana": 1800, 
    "Ethan": 2200, 
    "Fiona": 700, 
    "John": 685, 
    "Hor Kee": 1389, 
    "Siew Ling": 235, 
    "Matt": 452, 
    "Kristen": 985, 
    "Johnson": 785, 
    "Charles": 2352, 
    "Tommy": 741, 
    "Laura": 689
    }
vip = {}
non_vip = {}
for name in customer_spending:
    paid= customer_spending[name]
    if paid >= 1000:
        vip[name] = paid
    else:
        non_vip[name] = 1000-paid
for i in customer_spending:
    if i in vip:
        print(f"Hi, {i}, you are now a VIP member! Congratulations! ")
    else:
        print(f"Hi {i}, spend ${non_vip[i]} more to become a VIP member!")