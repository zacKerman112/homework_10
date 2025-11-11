#Вимоги до програми:
#Користувач (Клієнт) може переглянути список доступних автомобілів.
#Користувач може обрати автомобіль та забронювати його.
#Система повинна реєструвати, який автомобіль був виданий.
#Користувач повинен отримати Підтвердження Прокату (Rental Confirmation) або Договір, який містить деталі оренди.

class Cars:
    def __init__(self, bmw_m1, mazda_6, opel_astra):
        self.bmw_m1 = bmw_m1
        self.mazda_6 = mazda_6
        self.opel_astra = opel_astra

class Car_book_system:
    def __init__(self, cars):
        self.cars = cars

    def view_car_list(self):
        car_list = [
            f"BMW M1: {self.cars.bmw_m1}",
            f"Mazda 6: {self.cars.mazda_6}",
            f"Opel Astra: {self.cars.opel_astra}"
        ]
        for car in car_list:
            print(car)
            
    def choose_car(self):
        print("choose your car")
        print("1 - bmw m1")
        print("2 - mazda 6")
        print("3 - opel astra")
        choice = input("type in your choice: ")
        if choice == "1":
            print("great choice! now this bmw m1 is rented by you!")
        elif choice == "2":
            print("awesome! now this mazda is under your rent!")
        elif choice == "3":
            print("reliable and affordable , congradulations on renting this opel!")        
        else:
            print("you may have entered something wrong , try again")
            return None

    def reserve_car():
        pass
    def rental_confirmation():
        pass

