from datetime import datetime
from Usuario import Usuario, Cliente, Administrador  
from Producto import Producto                         
from Pedido import Pedido                             



#Clase tienda service
class TiendaService:
    def __init__(self):
        self.productos = []
        self.usuarios = []
        self.pedidos = []


 #USUARIO
    
    def crear_usuario(self, tipo,  identificador, name, email, direccion = None): 
        if tipo.lower() == "cliente":
            usuario = Cliente(identificador, name, email, direccion)
        else:
            usuario = Administrador(identificador, name, email)

        self.usuarios.append(usuario)
        return usuario

#PRODUCTO
  
    def añadir_producto(self, producto):
        self.productos.append(producto)  #Cada producto tiene un id, un nombre, precio y una cantidad en stock

    def eliminar_producto(self, producto_id):
        self.productos = [p for p in self.productos if p.identificador != producto_id]

    def ver_productos(self):
        return self.productos

#PEDIDO

    from datetime import datetime

    def realizar_pedido(self, usuario, pedido):
        
        #Busco si ya esta regidtrado el cliente
        cliente = None 
        for u in self.usuarios:
            if u.identificador == usuario:
                cliente = u 
                break 
        
        if cliente is None:
            print("Error, usuario no encontrado")
            return None

        #Compruebo la cantidad de producto en stock
        for producto, cantidad in pedido:
            if producto.stock < cantidad:
                print(f"No hay suficientes unidades de {producto.name}")
                return None

        #Creo el pedido   
        nuevo_pedido = Pedido(identificador = len(self.pedidos) + 1, fecha = datetime.now(), cliente = cliente, lista_productos = pedido)

        #Elimino los productos comprados de la lista original
        for producto, cantidad in pedido:
            producto.stock -= cantidad

        #Archivo el pedido para que quede constancia de el
        self.pedidos.append(nuevo_pedido)

        return nuevo_pedido
