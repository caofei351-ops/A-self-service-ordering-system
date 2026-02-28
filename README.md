## COMP2090SEF_course_project-task1

Group member: Cao Fei(13755803), Pan HaoWen(13752390),Xin YueYing(13795420)

## 👀:Contents
- [How did this idea come about?](#idea)
- [The usage of the OOP concepts](#function)
- [What problems can be solved?](#problem)
- [Update](#update)
- [Contact](#contact)
- [Non-Commercial Use Only Declaration](#x)
## <a name="idea"></a>🧠:How did this idea come about?
This self-service ordering system is made to fix the common problems we face in daily campus life:

1➡️The cafeteria always has long lines during peak time, and it’s a big waste of time for both students and staff.

2➡️Cashiers often make mistakes when taking orders by hand, such as mixing up orders or giving wrong dishes, and the service is always slow because of these errors.

3➡️There was no clear digital way to track orders before, so both students and cafeteria workers often feel confused and unhappy with the service.

We want to build a simple and practical system based on OOP knowledge to automate the ordering process, cut down human mistakes, and let everyone check the order progress easily. The system is designed to be modular, scalable and easy to maintain, which is in line with the software design principles we learned in class.
## <a name="function"></a>🤔: The usage of the OOP concepts
1➡️ **Abstraction** hides complex implementation details and exposes only essential features (via abstract classes/methods).
- Dish and User in base_classes,py are abstract classes with @abstractmethod(These methods define a "contract" (required behavior) for subclasses but do not implement logic themselves.).

🌟for example:
 ```shell
    from abc import ABC, abstractmethod
    class Dish(ABC):
        def __init__(self, name, student_price, teacher_price, normal_price):
            self.name = name          
            self.student_price = student_price  
            self.teacher_price = teacher_price  
            self.normal_price = normal_price   

        @abstractmethod
        def get_type(self):
            pass
 ```

2➡️ **Inheritance** allows a class to reuse code from a parent class and extend its functionality.eg: In the menu_dish.py, the parent calss is Dish. and the children class are Main Course, Snack, and Drink. 

🌟for example:

![image alt](https://github.com/caofei351-ops/A-self-service-ordering-system/blob/bf5d1e309110b66c0719e8fdad8a9e12d1b72837/Inheritance.png)

3➡️ **Polymorphism** allows different subclasses to implement the same method in unique ways which makse the code more flexible and scalable.

🌟for example:

(1) get-type() for Dishes
- MainCourse.get_type() → “Main Course"
- Snack.get_type() → “Snack"
- Drink.get_type() → “Drink"

The menu system (Menu.show_menu()) calls get_type() on any Dish subclass(no need to checj the exact type:
 ```shell
    type_dishes = [d for d in self.dishes if d.get_type() == t]
 ```
(2) get_discount() for Users
- Student.get_discount() → “0.9"(10% off)
- Teacher.get_discount() → “0.9"(10% off)
- NormalUser.get_discount() →“1.0"（no discount)

The cart (Cart.calculate_total()) uses user.get_discount():
 ```shell
    discount = self.user.get_discount() # work for any user subclass
 ```

4➡️ The **encapsulation** combines data (attributes) and the methods for operating on these data into a class, and restricts direct access to the internal state through access modifiers/conventions (Prevents invalid state and centralizes validation logic).

🌟for example:
- Private/Protected Attributes: SalesRecord uses _instance to enforce the Singleton pattern (prevents direct modification).
 ```shell
    class SalesRecord:
    _instance = None 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
 ```
- Controlled Access via Methods: Instead of directly modifying balance, users call recharge() & Instead of directly changing selected_dishes, cart uses add_dish()/remove_dish().
```shell
    class Student(User):
    def recharge(self, amount):
        if amount >= 0:  # Validation logic
            self.balance += amount
        else:
            print("The amount cannot be negative!")
```
5➡️ **Singleton Pattern**:A specialized OOP pattern ensuring a class has only one instance (global access to a single object).

🌟for example:
- SalesRecord in sales_record.py implements Singleton to track total sales across the system:
```shell
    class SalesRecord:
    _instance = None  
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.total_sales = 0.0  
        return cls._instance
```
- The HKMUCoffeeSystem initializes self.sales_record = SalesRecord()—all orders share the same SalesRecord instance, so total sales are aggregated correctly.

6➡️ **Composition** uses objects of other classes as attributes to build complex functionality (Builds modular, reusable components).

🌟for example:
- Cart has-a User and Menu (depends on them to calculate totals/add dishes):
```shell
    class Cart:
    def __init__(self, user: User, menu: Menu):
        self.user: User = user        
        self.menu: Menu = menu   
```
- Order has-a copy of Cart details (uses copy.deepcopy to preserve order history):
```shell
    self.cart_detail: List[Tuple[Dish, int]] = copy.deepcopy(cart.selected_dishes)
```

## <a name="problem"></a>🦯:What problems can be solved?

This self-service ordering system effectively resolves key inefficiencies in traditional campus cafeteria dining with practical real-life solutions, and adopts Python built-in basic data structures for standardized, efficient data management—laying a foundation for functional stability and subsequent expansion with complex data structures in Task 2, fully meeting the course’s problem definition and technical design requirements:

1➡️Long waiting queues in peak hours

Campus cafeterias have long lines during lunch and dinner breaks, making students and teachers waste 10–20 minutes waiting for meals daily. The system supports terminal-based pre-ordering; users can place orders in classrooms or dormitories in advance and pick up prepared meals directly at the cafeteria, completely avoiding queuing and saving precious study and work time.

2➡️ Frequent human errors in manual order-taking

Cashiers often mix up dish flavors, portions or user customization requirements (e.g. serving spicy Mapo Tofu Rice to non-spicy eaters) when taking orders by hand. The system lets users select dishes and set requirements independently, with all order information recorded digitally and no manual intervention, ensuring 100% order accuracy and reducing service disputes from wrong orders.

3➡️ Lack of transparent order tracking for both sides

After manual ordering, users wait blindly without knowing meal preparation progress, and cafeteria staff cannot confirm the owner of uncollected meals—causing unnecessary food waste. The system displays real-time order status (Pending/In Progress/Completed) for users, and shows detailed user and order information for staff, making the entire ordering and meal preparation process open and transparent.

4➡️ Troublesome, error-prone discount application for different groups

HKMU students and teachers are entitled to a 10% dining discount, but cashiers often forget to apply discounts or miscalculate final prices during manual checkout. The system automatically identifies user roles (student/teacher/normal user) at checkout, applies the corresponding discount rate in real time, and calculates the final payable amount instantly—eliminating human calculation errors and simplifying the payment process.

5➡️ Cafeteria’s lack of sales data for operational optimization

Cafeteria operators only judge popular dishes by daily experience, with no specific sales data support. This leads to over-purchasing of some ingredients and insufficient preparation of popular ones, causing serious food waste and low operational efficiency. The system’s SalesRecord module tracks real-time daily sales volume and revenue of each dish, providing concrete data for operators to adjust menus and ingredient purchase quantities—effectively reducing food waste and improving operational efficiency.

6➡️ Difficult expansion of traditional manual dining systems

To add new dish categories (e.g. breakfast sets, desserts) or user benefits, traditional manual systems require re-training all cashiers and adjusting the entire order-taking process, which is time-consuming and labor-intensive. Our modular OOP design allows adding new functions only by creating new subclasses (e.g. a BreakfastSet class inheriting from the base Dish class) without modifying any core system code, making system expansion simple and fast.

7➡️ Disorganized dish and order data management (core data structure application)

The cafeteria previously recorded dish information and order records with paper lists and Excel spreadsheets—these are easy to lose, and hard to query or modify quickly. Our project uses Python built-in lists and dictionaries as the core basic data structures for unified, efficient data management, with clear division of usage to match business needs:

• Lists: Store all dish objects and cart-selected dish objects for fast sequential traversal, category sorting (e.g. filtering Main Course/Drink via get_type()) and dynamic addition/removal of elements—ideal for scenarios requiring ordered, modifiable data sets.

• Dictionaries: Map unique order IDs to detailed order objects (user info, dish list, total amount) and store user account information (ID → user object) for O(1) fast query and key-value matching—perfect for scenarios requiring quick data lookup by a unique identifier.
This standardized data management method ensures data security and easy operation, and also lays a solid foundation for integrating more complex data structures (e.g. binary search trees for fast dish search, heaps for sales data sorting) in Task 2 of the project.

8➡️ Unregulated user balance and sales data tracking

Manual recording of user meal balances and cafeteria sales data is easy to have typos and data inconsistencies. The system encapsulates balance management in user classes (with negative recharge validation) and uses a singleton SalesRecord class to track global sales data—both relying on Python numeric types and basic data structures for real-time, accurate data update and storage, ensuring data integrity and consistency across the entire system.


## <a name="update"></a>🕵️:Update
- **2026.01.29**: We form our group and study what is Github and how to use it.
- **2026.02.03**: We reviewed the specific requirements for the group project. At the same time we analyzed some project examples from the previous semester and Github. Finally, we chose the ordering system of HLMU coffee as our task 1.
- **2026.02.06**:The specific process of the code has been determined.
- **2026.02.06**:The specific division of labor for Task 1 has been determined.
- **2026.02.17**:CaoFei finishs the major code for task1.
- **2026.02.27**:Pan Hao Wen polished the code for task1.
  
## <a name="contact"></a>💙:Contact
If you have any questions about our project, please email us with `s1375580@live.hkmu.edu.hk`,`s1375239@live.hkmu.edu.hk`,`s1379542@live.hkmu.edu.hk`.

## <a name="x"></a>Non-Commercial Use Only Declaration

