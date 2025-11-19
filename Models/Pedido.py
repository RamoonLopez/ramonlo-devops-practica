#Clase pedido
class Pedido:
    def __init__(self, identificador, fecha, cliente, lista_productos ):
        self.identificador = identificador
        self.fecha = fecha
        self.cliente = cliente
        self.lista_productos = lista_productos

    def __str__(self):
        return f"Identificador: {self.identificador}, Cliente: {self.cliente.name}, Valor de la compra: {self.calcular_importe()}"   
        
    def calcular_importe(self):
        return sum(producto.price * cantidad for producto, cantidad in self.lista_productos)
    