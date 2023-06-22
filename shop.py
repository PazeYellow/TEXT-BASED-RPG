class Item:
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price


class Shop:
    def __init__(self):
        self.items = self.create_items()

    def create_items(self):
        items = {
            "sword": Item("Sword", 15, 50),
            "shield": Item("Shield", 10, 30),
            "potion": Item("Potion", 0, 10)
        }
        return items

    def buy_item(self, player, item_name):
        item = self.items.get(item_name.lower())
        if item:
            if player.gold >= item.price:
                player.gold -= item.price
                player.power += item.power
                print(f"You bought {item.name}!")
            else:
                print("Not enough gold to buy the item.")
        else:
            print("Item not found in the shop.")
