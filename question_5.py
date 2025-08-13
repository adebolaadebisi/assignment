#modify tuple indirectly
shopping_list = tuple(input(f"Enter item {i+1}: ") for i in range(3))
shopping_list_list = list(shopping_list)
for i in range(2):
    new_item = (input(f"Enter extra item {i+1}: "))
    shopping_list_list.append(new_item)
    shopping_list = tuple(shopping_list_list)
    print("updated shopping list:", ", ".join(shopping_list))