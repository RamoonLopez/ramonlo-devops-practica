#Clase Usuario
class Usuario: 
    def __init__(self, Identificador, name, email):
        self.identificador = Identificador
        self.name = name
        self.email = email

    def __str__(self):
        return f"Identificador: {self.identificador}, Name: {self.name}, Email: {self.email}"

    def is_admin(self):   
        return False

class Cliente(Usuario): 
    def __init__(self, Identificador, name, email, direccion):
        super().__init__(Identificador, name, email)
        self.direccion = direccion

    def __str__(self):
        return f"Identificador: {self.identificador}, Name: {self.name}, Email: {self.email}, Direccion: {self.direccion}"
    
class Administrador(Usuario):
    def __init__(self, Identificador, name, email):
        super().__init__(Identificador, name, email)

    def __str__(self):
        return f"Identificador: {self.identificador}, Name: {self.name}, Email: {self.email}"
    
#   def is_admin(self, cliente, administrador):
#      return super().is_admin(cliente, administrador)
          
    def is_admin(self):   
        return True