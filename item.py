import csv
class Item:
    instances = []
    num_of_item = 0
    pay_rate = 0.85

    def __init__(self, product: str, quanity: int, price: int):
        self.__product = product
        self.quanity = quanity
        self.price = price
        self.instances.append(self)
        Item.num_of_item += 1

    def calculate_total_price(self):
        return self.quanity * self.price

    @property
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    #@property
    #def product(self):
    #    return self.product
    #@product.setter
    #def name(self, value: str):
    #    if len(value) <= 10:
    #        self.product = value
    #    else:
     #       print("Exception: Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        results = []
        with open('items.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                __product = row['name']
                price = int(row['price'])
                quanity = int(row['quantity'])
                results.append(cls(__product, quanity, price))
        return results
    @staticmethod
    def is_integer(number):
        if number %1 ==0:
            return True
        else:
            return False


    @property
    def long_name(self):
        return self.__product
    @long_name.setter
    def long_name(self, name):
        if len(name) <= 10:
            self.__product = name
        else:
            self.__product = print("Exception: Длина наименования товара превышает 10 символов")
            #raise Exception('Длина наименования товара превышает 10 символов')





