# Class with Name

class Product:

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


product1 = Product()
product1.set_name("Fig Bars")

print(product1.get_name())

