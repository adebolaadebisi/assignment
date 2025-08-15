# task2
#super market price list
items = ["Rice", "Beans", "Wine", "Milk"]
item1_price = float(input("Rice price: "))
item2_price = float(input("Beans price: "))
item3_price = float(input("Wine price: "))
item4_price = float(input("Milk price: "))

store_items = {
    items[0]:  (f"#{item1_price}"),
    items[1]:   (f"#{item2_price}"),
    items[2]:   (f"#{item3_price}"),
    items[3]:    (f"#{item4_price}")
}
print(f"store item and prices are: {store_items}")

update_item = float(input(f"update {2} price: #"))
store_items.update({items[2] :update_item})

print(f"Available items are; {store_items.keys()}")



