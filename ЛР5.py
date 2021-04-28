class Tech:
    pass


class Worker:
    company = 'MAIstore'
    boss_name = 'Александрова С.С.'


class Cassier(Worker):
    pass
    salary = 40000
    name = 'Алина'
    position = 'кассир'

    def greet_c(self):
        print('Здравствуйте, рада помочь с вашими покупками. Пожалуйста, выложите их на ленту.')

    def goodbye_c(self):
        print('Спасибо за покупку, приходите еще!')

    def get_name(self):
        print(self.name)


class Manager(Worker):
    pass
    name = 'Григорий'
    position = 'менеджер'
    salary = 30000

    def greet_m(self):
        print('Здравствуйте! Добро пожаловать в MAIstore! Меня зовут', self.name, ', могу я вам чем-то помочь?')

    def set_manager(self, name, position):
        self.name = name
        self.position = position

    def ask_what_buy(self):
        the_thing = int(input("Что вас интересует? Введите число: 1 - телевизоры, 2 - микроволновки, 3 - ноутбуки, 4 - принтеры, 5 - мониторы: "))
        if the_thing == 5:
            print("Могу порекомендовать нашу последнюю новинку - Apple высшего качества, всего за 30000!")
            printing = str(input("Согласны? (Да/Нет)"))
            if printing == 'Да':
                print('Замечательно, пройдите на кассу.')
            else:
                print("Тогда можете пройти в нужный отдел, я покажу вам другие модели")
        elif the_thing == 4:
            print("Могу порекомендовать нашу последнюю новинку - Laserget высшего качества, всего за 3000!")
            printing = str(input("Согласны? (Да/Нет)"))
            if printing == 'Да':
                print('Замечательно, пройдите на кассу.')
            else:
                print("Тогда можете пройти в нужный отдел, я покажу вам другие модели")
        elif the_thing == 3:
            print("Могу порекомендовать нашу последнюю новинку - HP высшего качества, всего за 30000!")
            printing = str(input("Согласны? (Да/Нет)"))
            if printing == 'Да':
                print('Замечательно, пройдите на кассу.')
            else:
                print("Тогда можете пройти в нужный отдел, я покажу вам другие модели")
        elif the_thing == 2:
            print("Могу порекомендовать нашу последнюю новинку - Bomgo высшего качества, всего за 14000!")
            printing = str(input("Согласны? (Да/Нет)"))
            if printing == 'Да':
                print('Замечательно, пройдите на кассу.')
            else:
                print("Тогда можете пройти в нужный отдел, я покажу вам другие модели")
        elif the_thing == 1:
            print("Могу порекомендовать нашу последнюю новинку - HP высшего качества, всего за 20000!")
            printer = str(input("Согласны? (Да/Нет)"))
            if printer == 'Да':
                print('Замечательно, пройдите на кассу.')
            else:
                print("Тогда можете пройти в нужный отдел, я покажу вам другие модели")
        else:
            print('Простите, неверная команда')


class Customer:
    name = ['Иван', 'Петр', 'Семен']

    def get_name(self):
        print(self.name)

    def set_laptop(self, laptop):
        self.laptop = laptop

    def set_microwave(self, microwave):
        self.microwave = microwave

    def set_printer(self, printer):
        self.printer = printer

    def set_name(self, name):
        self.name = name

    def ask_name(self):
        client_name = input("Здравствуйте, как вас зовут? ")
        self.name = client_name
        print("Очень приятно, ", self.name)


class Televisor(Tech):
    pass
    model = 'HP'
    price = 20000
    quality = 10

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_quality(self, quality):
        self.quality = quality

    def choose_TV(self, choose_TV):
        pass

    def start_tv(self):
        print('Телевизор включен')

    def stop_tv(self):
        print('Телевизор выключен')

class Laptop(Tech):
    pass
    model = 'HP'
    price = '30000'
    quality = 10

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_quality(self, quality):
        self.quality = quality

    def choose_laptop(self, choose_TV):
        pass


    def start_laptop(self):
        print('Ноутбук включен')

    def stop_laptop(self):
        print('Ноутбук выключен')


class Printer(Tech):
    pass
    model = 'Laserget'
    price = '3000'
    quality = 10

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_quality(self, quality):
        self.quality = quality

    def choose_printer(self, choose_TV):
        pass

    def start_printer(self):
        print('Принтер включен')

    def stop_printer(self):
        print('Принтер выключен')


class Microwave(Tech):
    pass
    model = 'Bomgo'
    price = 14000
    quality = 10

    def __init__(self, model, price, quality):
        self.model = model
        self.price = price
        self.quality = quality

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_quality(self, quality):
        self.quality = quality

    def choose_microwave(self, choose_TV):
        pass

    def start_microwave(self):
        print('Микроволновка включена')

    def stop_microwave(self):
        print('Микроволновка выключена')


manager = Manager()
customer = Customer()
cassier = Cassier()
manager.greet_m()
customer.ask_name()

manager.ask_what_buy()
cassier.greet_c()
cassier.goodbye_c()
