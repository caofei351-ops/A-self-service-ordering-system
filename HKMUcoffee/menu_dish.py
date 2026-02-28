class Dish:
    def __init__(self, name, student_price, normal_price):
        self.name = name  
        self.student_price = student_price
        self.normal_price = normal_price

    def get_type(self):
        
        raise NotImplementedError
from base_classes import Dish

class MainCourse(Dish):
    def get_type(self):
        return "Main Course"

class Snack(Dish):
    def get_type(self):
        return "Snack"

class Drink(Dish):
    def get_type(self):
        return "Drink"

class Menu:
    def __init__(self):
        self.dishes = [] 

    def add_dish(self, dish):
        if isinstance(dish, Dish):
            self.dishes.append(dish)
        else:
            print("Add failed: Not a valid Dish object!")

    def show_menu(self):
        print("\n===== 📋 HKMUcoffee Menu =====")
        dish_types = ["Main Course", "Snack", "Drink"]
        type_titles = {"Main Course":"[all day Breakfast & hot dishes]",
                       "Snack":"[Hot Sandwiches]",
                       "Drink":"[PREMIUM COFFEE]"}
        for t in dish_types:
            print(f"\n【{t}】")
            type_dishes = [d for d in self.dishes if d.get_type() == t]
            if not type_dishes:
                print("  No dishes available")
                continue
            print(f"{'':<4} {'Name of dishes':<35} {'STAFF & STUDENT PRICE':<15} {'RETAIL PRICE':<10}")
            print("-" * 70)
            for idx, dish in enumerate(type_dishes, 1):
                print(f"  {idx:<4}. {dish.name:<35} ${dish.student_price:<14} ${dish.normal_price:<10}")

    def get_dish_by_index(self, idx):
        if 0 <= idx < len(self.dishes):
            return self.dishes[idx]
        else:
            return None
elf.add_dish(MainCourse("All-Day Breakfast", 54, 68))
        self.add_dish(MainCourse("Bolognese Pasta with Fried Egg Toast", 38, 45))
        self.add_dish(MainCourse("Custom 2-Topping Demae Ramen", 29, 36))
        self.add_dish(MainCourse("Custom 2-Topping Spicy Noodles", 34, 42))
        self.add_dish(MainCourse("Prawn Toast with Quinoa Garden Salad", 30, 36))
        self.add_dish(MainCourse("Korean Yuzu Chicken Wings with Fries", 28, 36))
        self.add_dish(MainCourse("American Hot Dog with Fries", 29, 36))
        self.add_dish(MainCourse("Avocado Cheddar Cheese Panini", 37, 48))
        self.add_dish(MainCourse("Sous Vide Chicken Caesar Panini", 37, 48))
        self.add_dish(MainCourse("Honey Mustard Beef & Mushroom Panini", 39, 50))
        self.add_dish(MainCourse("American Honey Mustard Smoked Salmon Panini", 39, 50))
        self.add_dish(MainCourse("Avocado Quinoa Veggie Burrito", 33, 43))
        self.add_dish(MainCourse("Sous Vide Chicken Caesar Burrito", 33, 43))
        self.add_dish(MainCourse("Honey Mustard Beef & Mushroom Burrito", 35, 46))
        self.add_dish(MainCourse("Smoked Salmon & Egg Scramble Burrito", 35, 45))


        self.add_dish(Snack("Latte / Cheesecake / Cappuccino", 12, 12))
        self.add_dish(Snack("Any Premium Drink", 2, 2))
        self.add_dish(Snack("Specialty Drink", 13, 13))
        self.add_dish(Snack("Seasoned Fresh Fruit Cup", 10, 10))
        self.add_dish(Snack("Daily Soup", 10, 10))
        self.add_dish(Snack("Seasoned Yogurt Parfait", 16, 16))

        self.add_dish(Drink("Double Espresso (2oz)", 16, 20))
        self.add_dish(Drink("Black Coffee", 19, 24))
        self.add_dish(Drink("White Coffee", 22, 28))
        self.add_dish(Drink("Cappuccino", 22, 28))
        self.add_dish(Drink("Café Latte", 22, 28))
        self.add_dish(Drink("Mocha Coffee", 27, 33))
        self.add_dish(Drink("Hazelnut Latte", 27, 33))
        self.add_dish(Drink("Caramel Latte", 27, 33))
        self.add_dish(Drink("Dirty Coffee", 31, 39))
        self.add_dish(Drink("Tonic Coffee", 31, 39))
        self.add_dish(Drink("Espresso Shot", 5, 5))
        self.add_dish(Drink("Swap to Oat Milk", 5, 5))
        self.add_dish(Drink("Swap to Skim Milk", 0, 0))
if __name__ == "__main__":
    hkmu_coffee_menu = Menu()

hkmu_coffee_menu.init_default_dishes()
    
    hkmu_coffee_menu.show_menu()
    
hkmu_coffee_menu.show_student_price_ranking()

