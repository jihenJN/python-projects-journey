#shopping cart system

foods=[]
prices=[]
total=0
while True:
    food=input("enter the food you order (q for quit): ")
    if food=="q":
        break
    else:
        price=float(input(f"enter the price for {food}: $"))
        foods.append(food)
        prices.append(price)
print("------ CART -----")
# zip() pairs items by index
for food,price in zip(foods,prices):
       print(f"{food}........${price}")
for price in prices:
    total+=price
print(f"\ntotal:${total}")   
    