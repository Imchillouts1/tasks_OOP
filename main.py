"""1) Создайте класс Car, который имеет атрибуты make (марка) и model (модель).
Реализуйте метод display_info(), который выводит информацию о марке и модели автомобиля."""


class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model


    def display_info(self) -> str:
        print(f'{self.make} | {self.model}')


# car_1 = Car(make='Skoda', model='Octavia')
# car_1.display_info()


"""2) Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота). 
Реализуйте метод calculate_area(), который возвращает площадь прямоугольника."""


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


    def calculate_area(self) -> float:
        s =  0.5 * self.width * self.height
        return s


# tangle_1 = Rectangle(width=5, height=8)
# print(tangle_1.calculate_area())


"""1) Разработайте класс BankAccount, который имеет атрибуты balance (баланс) и owner (владелец). 
Реализуйте методы deposit(amount) для внесения средств на счет и withdraw(amount) для снятия средств со счета. 
Учтите возможность проверки наличия достаточного баланса перед снятием."""


class BankAccount:
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner


    def deposit(self, amount):
        self.balance += amount
        print(f'{self.balance} | {self.owner}')


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('{self.balance} | {self.owner}')
        else:
            raise ValueError('Недостаточный баланс для снятия')


# owner_1 = BankAccount(balance=1000, owner='Vasily')
# print(owner_1.deposit(amount=100))
# print(owner_1.withdraw(amount=1000))


"""2) Создайте класс Library, представляющий библиотеку. 
Класс должен иметь атрибуты books (список книг) и members (список членов библиотеки). 
Реализуйте методы add_book(book) для добавления книги в библиотеку, 
remove_book(book) для удаления книги из библиотеки, 
add_member(member) для добавления нового члена библиотеки и 
remove_member(member) для удаления члена библиотеки. 
Также реализуйте метод checkout_book(book, member) для выдачи книги члену библиотеки 
и return_book(book, member) для возврата книги в библиотеку."""


class Library:
    def __init__(self, books: list, members: list, members_with_books):
        self.books = books
        self.members = members
        self.members_with_books = members_with_books


    def add_book(self, book: str):
        self.books.append(book)
        print(self.books)


    def remove_book(self, book: str) -> list | str:
        if book in self.books:
            self.books.remove(book)
            print(self.books)
        else:
            raise ValueError('Такой книги нет в библиотеке')


    def add_member(self, member: str):
        self.members.append(member)
        print(self.members)


    def remove_member(self, member: str):
        if member in self.members:
            self.members.remove(member)
            print(self.members)
        else:
            raise ValueError('Нет такого участника')


    def checkout_book(self, book : str, member: str):
        if book not in self.books or member not in self.members:
            print('Нет книги или участника')
            for books in self.members_with_books.values():
                if book in books:
                    raise ValueError('Книга уже выдана')
        self.members_with_books[member] = book
        self.books.remove(book)
        print(self.members_with_books)


    def return_book(self, book: str, member: str):
        if member not in self.members:
            raise ValueError('Нет такого участника')
        if member not in self.members_with_books:
            raise ValueError('Нет такого участника')
        del  self.members_with_books[member]
        self.books.append(book)
        print(self.members_with_books)


# library = Library(
#     books=['Ведьмак', 'Преступление и наказание', 'Му-Му'],
#     members=['Василий', 'Максимилиан', 'Глебий'],
#     members_with_books= {}
# )
#
# print(library.checkout_book(book='Преступление и наказание', member='Василий'))
# print(library.checkout_book(book='Ведьмак', member='Глебий'))



"""1) Создайте систему регистрации на конференцию. 
Реализуйте классы Conference (конференция), Participant (участник) и RegistrationSystem (система регистрации). 
Класс Conference должен иметь атрибуты name (название) и capacity (вместимость), 
класс Participant - атрибуты name (имя) и email (электронная почта), 
а класс RegistrationSystem - атрибуты conference (конференция) и participants (список участников), 
а также методы register(participant) для регистрации участника 
и is_registration_available() для проверки доступности регистрации на конференцию. 
Реализуйте проверку наличия свободных мест на конференции перед регистрацией."""


class Conference:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity


class Participant:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class RegistrationSystem:
    def __init__(self, conference: Conference, participants: list[Participant]):
        self.conference = conference
        self.participants = participants


    def is_registration_available(self) -> bool:
        return len(self.participants) < self.conference.capacity


    def register(self, participant: Participant):
        if self.is_registration_available():
            self.participants.append(participant)
            print('Участник успешно зарегистрирован на конференцию')
        else:
            raise ValueError('Нет свободных мест')


# conference_1 = Conference(name='MudrTeam', capacity=2)
# registration = RegistrationSystem(conference_1, participants=[])
# participant_1 = Participant(name='Глеб', email='zuefgleb@gmail.com')
# participant_2 = Participant(name='Василий', email='Bozn@gmail.com')
# participant_3 = Participant(name='Артем', email='Artamon@mail.ru')
# print(registration.register(participant_1))
# print(registration.register(participant_2))
# print(registration.register(participant_3))



"""2) Создайте игру "Магазин животных". 
Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена), 
а также методом sound(), который возвращает звук, издаваемый животным. 
От него унаследуйте классы Dog, Cat и Bird, каждый из которых переопределяет метод sound() 
для возврата соответствующего звука для каждого типа животного. 
Класс Shop должен иметь атрибуты animals (список доступных животных) и budget (бюджет магазина), 
а также методы buy_animal(animal) для покупки животного и sell_animal(animal) для продажи животного. 
Реализуйте проверки наличия достаточного бюджета у магазина для покупки и наличия животного в магазине для продажи."""


class Animal:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print('Гав-Гав')


class Cat(Animal):
    def sound(self):
        print('Мяу-Мяу')


class Bird(Animal):
    def sound(self):
        print('Чирик-чирик')


class Shop:
    def __init__(self, animals: list[Animal], budget: float):
        self.animals = animals
        self.budget = budget


    def buy_animal(self, animal: Animal):
        if self.budget >= animal.price:
            self.animals.append(animal.name)
            print(self.animals)
        else:
            raise ValueError('Недостаточный бюджет для покупки животного')


    def sell_animal(self, animal: Animal):
        if animal.name in self.animals:
            self.animals.remove(animal.name)
            print(self.animals)
        else:
            raise ValueError('Такого животного нет в магазине')

#
# animal_1 = Animal(name='Кошка', price=100)
# animal_2 = Animal(name='Собака', price=100)
# animal_3 = Animal(name='Крыса', price=100)
# animal_4 = Animal(name='Глист', price=100)
#
# my_shop = Shop(animals=[], budget=1000)
# print(my_shop.buy_animal(animal_1))
# print(my_shop.buy_animal(animal_2))
# print(my_shop.buy_animal(animal_3))
# print(my_shop.sell_animal(animal_4))
# print(my_shop.sell_animal(animal_3))
