#Вимоги до програми:
#Користувач (Клієнт) може переглянути список доступних автомобілів.
#Користувач може обрати автомобіль та забронювати його.
#Система повинна реєструвати, який автомобіль був виданий.
#Користувач повинен отримати Підтвердження Прокату (Rental Confirmation) або Договір, який містить деталі оренди.
import pandas as pd
df = pd.read_csv("cars.csv")  #  Загружаем таблицу машин

class Car_book_system:
    def __init__(self):
        self.last_rented_id = None  #  Храним ID последней арендованной машины

    def view_car_list(self):
        #  Выводим список всех машин с их статусом
        for index, row in df.iterrows():
            print(f"{index + 1}. {row['make']} {row['model']} ({row['year']}) — Available: {row['available']}")

    def choose_car(self):
        #  Пользователь выбирает машину по номеру
        self.view_car_list()
        choice = input("Enter the number of the car you want to rent: ")

        try:
            index = int(choice) - 1
            selected_car = df.iloc[index]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            return

        if selected_car['available'] == 'yes':
            print(f"You have successfully rented the {selected_car['make']} {selected_car['model']}!")
            df.loc[df['id'] == selected_car['id'], 'available'] = 'no'  #  Обновляем статус
            df.to_csv("cars.csv", index=False)  #  Сохраняем изменения
            self.last_rented_id = selected_car['id']  # Запоминаем ID
        else:
            print("Sorry, this car is not available.")

    def reserve_car(self):
        #  Логика бронирования машины (если хочешь использовать статус "reserved")
        self.view_car_list()
        choice = input("Enter the number of the car you want to reserve: ")

        try:
            index = int(choice) - 1
            selected_car = df.iloc[index]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            return

        if selected_car['available'] == 'yes':
            print(f"You have reserved the {selected_car['make']} {selected_car['model']}.")
            df.loc[df['id'] == selected_car['id'], 'available'] = 'reserved'  # 🔄 Меняем статус
            df.to_csv("cars.csv", index=False)
        else:
            print("Sorry, this car is not available for reservation.")

    def rental_confirmation(self):
        #  Подтверждение аренды — вывод информации о последней арендованной машине
        if self.last_rented_id is None:
            print("No car has been rented yet.")
            return

        car = df.loc[df['id'] == self.last_rented_id].squeeze()
        print("Rental Confirmation:")
        print(f"Car: {car['make']} {car['model']}")
        print(f"Year: {car['year']}")
        print(f"Status: {car['available']}")
