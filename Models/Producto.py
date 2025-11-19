#Clase producto
class Producto:
    #atrubuto de la clase??
     def __init__(self, identificador, name, price, stock):
        #Atributos e la instancia
        self.identificador = identificador
        self.name = name
        self.price = price
        self.stock = stock
    
     def __str__(self):
        return f"Identificador: {self.identificador}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"
     
class ProductoElectronico (Producto):
    def __init__(self, identificador, name, price, stock, garantia):
        super().__init__(identificador, name, price, stock)
        self.garantia = garantia

    def __str__(self):
        return f"Identificador: {self.identificador}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Garantia: {self.garantia}"
    
class ProductoRopa (Producto):
    def __init__(self, identificador, name, price, stock, size, colour):
        super().__init__(identificador, name, price, stock)
        self.size = size
        self.colour = colour

    def __str__(self):
         return f"Identificador: {self.identificador}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Size: {self.size}, Colour: {self.colour}"  
    