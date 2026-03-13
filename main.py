import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def get_name_items(self):
        return self.__name_items

    @property
    def get_number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError ('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError ('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError ('Позиция отсутствует в чеке')

        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = sum(self.__item_price[item] for item in self.__name_items)
        if self.number_items > 10:
            total *= 0.1
        else:
            return total

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = [item for item in self.__name_items if self.__tax_rate[item] == 20]
        total = [self.__item_price[item] for item in twenty_percent_tax]
        tax_total = sum(price * 0.2 for price in total_prices)
        if self.number_items > 10:
            tax_total *= 0.9
        return tax_total


    def ten_percent_tax_calculation(self):
        ten_percent_tax = [item for item in self.__name_items if self.__tax_rate[item] == 10]
        total = [self.__item_price[item] for item in ten_percent_tax]
        tax_total = sum(price * 0.1 for price in total)
        if self.number_items > 10:
            tax_total *= 0.9
        return tax_total

    def total_tax(self):
        total =(self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation())
        return total

    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            str_num = str(telephone_number)
            if len(str_num) == 11:
                raise ValueError ('Необходимо ввести 10 цифр после "+7"')
            return f'+7{telephone_number}'
        except TypeError:
            raise TypeError ('Необходимо ввести цифры')